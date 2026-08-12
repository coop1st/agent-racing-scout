#!/usr/bin/env python3
"""
Parse VirtualStable (US, Equibase) and HorseTracker (UK/Ireland, irishracing.com)
notification emails into data/tracked/tracked-horses.xlsx.

Input: a JSON file (default: tracked_emails_raw.json in the current directory)
containing a list of objects:
    {
        "source": "virtualstable" | "horsetracker",
        "date": "<RFC3339 email received timestamp>",
        "subject": "<email subject>",
        "text": "<email snippet or full plaintext body>"
    }

For BOTH sources, `text` must be the FULL plaintext body (get_message with
messageFormat=PLAIN_TEXT) -- not the search snippet. Gmail's snippet for
virtualstable emails is prefixed with an unpredictable internal list/nickname
token (e.g. "Equibase", "NYTBDF", "Pewter") with no reliable punctuation
boundary before the actual sentence, which the parser cannot safely strip; the
full body's own layout (blank lines / table pipes) avoids that ambiguity. For
horsetracker, a single digest email can list many horses and the snippet only
shows the first one.

Output: data/tracked/tracked-horses.xlsx, one row per horse per upcoming race
(deduped, future-dated only, relative to --as-of, default today UTC).
"""
import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

STATUS_RANK = {
    "runs": 3,
    "race day": 3,
    "declared": 2,
    "entered": 1,
    "final entry": 1,
}

MONTH_ABBR = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def strip_md_links(text: str) -> str:
    """Strip markdown-ish '[label](url)' and bare '[](url)' artifacts left by
    plaintext extraction of HTML emails, and collapse whitespace."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text


VS_BOILERPLATE = "Having trouble viewing this email? Check your notifications online here."


def parse_virtualstable(item: dict) -> list[dict]:
    subject = item.get("subject", "")
    if subject not in ("Final Entry Notification", "Race Day Notification"):
        return []

    text = strip_md_links(item["text"])
    text = text.replace(VS_BOILERPLATE, "\n")
    email_dt = datetime.fromisoformat(item["date"].replace("Z", "+00:00"))

    m = re.search(
        r"([A-Za-z0-9'\- ]+?)\s+is entered (?:on ([A-Za-z]+ \d{1,2}, \d{4})|(today)) at ([A-Z][A-Za-z0-9 '\-]+?)\.",
        text,
    )
    if not m:
        return []
    horse, date_str, today_flag, track = m.groups()
    horse = horse.strip()
    track = track.strip()

    if today_flag:
        race_date = email_dt.date()
    else:
        race_date = datetime.strptime(date_str, "%B %d, %Y").date()

    race_time = None
    tm = re.search(r"Race:\s*\d+\s*-\s*(\d{1,2}:\d{2}\s*[AP]M)", text)
    if tm:
        try:
            race_time = datetime.strptime(tm.group(1).replace(" ", ""), "%I:%M%p").strftime("%H:%M")
        except ValueError:
            race_time = None

    notes = None
    sm = re.search(r"\|\s*STAKES\s*\|\s*([^|]+?)\s*\|", text)
    if sm:
        notes = sm.group(1).strip()

    status = "final entry" if subject == "Final Entry Notification" else "race day"

    return [{
        "horse": horse,
        "country": "USA",
        "track": track,
        "race_date": race_date,
        "race_time": race_time,
        "status": status,
        "source": "virtualstable",
        "notes": notes,
        "email_date": email_dt.date(),
    }]


HT_STATUS_PATTERNS = [
    ("declared", re.compile(r"declared to run at\s+(?P<track>.+?)\s+on\s+(?P<day>[A-Za-z]+)\s+(?P<num>\d{1,2})(?:st|nd|rd|th)\s+(?P<mon>[A-Za-z]{3})\s+(?P<time>\d{1,2}\.\d{2})")),
    ("runs", re.compile(r"\brun[s]? at\s+(?P<track>.+?)\s+on\s+(?P<day>[A-Za-z]+)\s+(?P<num>\d{1,2})(?:st|nd|rd|th)\s+(?P<mon>[A-Za-z]{3})\s+(?P<time>\d{1,2}\.\d{2})")),
    ("entered", re.compile(r"\bentered at\s+(?P<track>.+?)\s+on\s+(?P<day>[A-Za-z]+)\s+(?P<num>\d{1,2})(?:st|nd|rd|th)\s+(?P<mon>[A-Za-z]{3})\s+(?P<time>\d{1,2}\.\d{2})")),
]
HT_IGNORE = re.compile(r"\bfinished\b|\bnon runner\b")

HT_HEADER_RE = re.compile(r"^#{2,3}\s*(?P<horse>[A-Za-z0-9'.\- ]+?)\s*\((?P<country>[A-Z]{2,4})\)\s*$")
HT_INLINE_HORSE_RE = re.compile(r"^(?P<horse>[A-Za-z0-9'.\- ]+?)\s*\((?P<country>[A-Z]{2,4})\)\s+(?P<rest>.+)$")


def _ht_status_and_fields(fragment: str):
    if HT_IGNORE.search(fragment):
        return None
    for status, pat in HT_STATUS_PATTERNS:
        m = pat.search(fragment)
        if m:
            return status, m
    return None


def _resolve_ht_date(day_num: int, mon_abbr: str, time_str: str, email_dt: datetime):
    mon = MONTH_ABBR.get(mon_abbr.lower()[:3])
    if not mon:
        return None, None
    year = email_dt.year
    try:
        race_date = datetime(year, mon, day_num).date()
    except ValueError:
        return None, None
    # handle year wraparound: if the parsed date looks like it's long in the
    # "past" relative to the email, it must actually be next year
    if (email_dt.date() - race_date).days > 200:
        race_date = datetime(year + 1, mon, day_num).date()
    hour_str, _, min_str = time_str.partition(".")
    hour = int(hour_str)
    minute = int(min_str.ljust(2, "0")[:2])
    if hour < 12:
        hour += 12
    race_time = f"{hour:02d}:{minute:02d}"
    return race_date, race_time


def parse_horsetracker(item: dict) -> list[dict]:
    text = strip_md_links(item["text"])
    email_dt = datetime.fromisoformat(item["date"].replace("Z", "+00:00"))
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]

    results = []
    current_horse = None
    current_country = None

    for line in lines:
        header_m = HT_HEADER_RE.match(line)
        if header_m:
            current_horse = header_m.group("horse").strip()
            current_country = header_m.group("country")
            continue

        inline_m = HT_INLINE_HORSE_RE.match(line)
        if inline_m:
            horse = inline_m.group("horse").strip()
            country = inline_m.group("country")
            fragment = inline_m.group("rest")
            sf = _ht_status_and_fields(fragment)
            if sf:
                status, m = sf
                race_date, race_time = _resolve_ht_date(
                    int(m.group("num")), m.group("mon"), m.group("time"), email_dt
                )
                if race_date:
                    results.append({
                        "horse": horse, "country": country,
                        "track": m.group("track").strip(),
                        "race_date": race_date, "race_time": race_time,
                        "status": status, "source": "horsetracker",
                        "notes": None, "email_date": email_dt.date(),
                    })
            current_horse, current_country = horse, country
            continue

        # continuation line (status-only, referring to current_horse from a header)
        if current_horse and (line.startswith("*") or line.startswith("entered")
                               or line.startswith("declared") or line.startswith("runs")
                               or "entered at" in line or "declared to run at" in line
                               or re.match(r"^runs? at", line)):
            sf = _ht_status_and_fields(line)
            if sf:
                status, m = sf
                race_date, race_time = _resolve_ht_date(
                    int(m.group("num")), m.group("mon"), m.group("time"), email_dt
                )
                if race_date:
                    results.append({
                        "horse": current_horse, "country": current_country,
                        "track": m.group("track").strip(),
                        "race_date": race_date, "race_time": race_time,
                        "status": status, "source": "horsetracker",
                        "notes": None, "email_date": email_dt.date(),
                    })

    return results


def build(raw_items: list[dict], as_of) -> pd.DataFrame:
    rows = []
    for item in raw_items:
        if item["source"] == "virtualstable":
            rows.extend(parse_virtualstable(item))
        elif item["source"] == "horsetracker":
            rows.extend(parse_horsetracker(item))

    if not rows:
        return pd.DataFrame(columns=[
            "Horse", "Country", "Track", "Race Date", "Race Time",
            "Status", "Source", "Notes", "Last Updated",
        ])

    df = pd.DataFrame(rows)
    df = df[df["race_date"] >= as_of]

    df["rank"] = df["status"].map(STATUS_RANK).fillna(0)
    df = df.sort_values(["horse", "race_date", "rank", "email_date"])
    df = df.drop_duplicates(subset=["horse", "race_date", "track"], keep="last")

    df = df.sort_values(["race_date", "horse"])
    df = df.rename(columns={
        "horse": "Horse", "country": "Country", "track": "Track",
        "race_date": "Race Date", "race_time": "Race Time",
        "status": "Status", "source": "Source", "notes": "Notes",
        "email_date": "Last Updated",
    })
    return df[["Horse", "Country", "Track", "Race Date", "Race Time",
               "Status", "Source", "Notes", "Last Updated"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="tracked_emails_raw.json")
    ap.add_argument("--output", default="data/tracked/tracked-horses.xlsx")
    ap.add_argument("--as-of", default=None, help="YYYY-MM-DD, defaults to today UTC")
    args = ap.parse_args()

    as_of = (
        datetime.strptime(args.as_of, "%Y-%m-%d").date()
        if args.as_of else datetime.now(timezone.utc).date()
    )

    raw_items = json.loads(Path(args.input).read_text(encoding="utf-8"))
    df = build(raw_items, as_of)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(out_path, index=False)
    print(f"Wrote {len(df)} upcoming tracked-horse rows to {out_path}")


if __name__ == "__main__":
    main()
