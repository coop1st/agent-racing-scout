#!/usr/bin/env python3
"""Regression tests for build_tracked_horses.py, run against real (anonymized
none-needed -- these are the user's own tracked-horse emails) sample bodies
pulled from virtualstable@equibase.com and horsetracker@irishracing.com.

Run with: python scripts/test_build_tracked_horses.py
"""
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_tracked_horses import build  # noqa: E402

FIXTURES = json.loads((Path(__file__).parent / "test_samples.json").read_text())


def test_full_sample_set():
    df = build(FIXTURES, date(2026, 7, 1))
    records = df.to_dict("records")
    rows = {(r["Horse"], r["Track"], str(r["Race Date"])): r for r in records}

    assert ("Moonlight", "DEL MAR", "2026-07-25") in rows
    assert rows[("Moonlight", "DEL MAR", "2026-07-25")]["Race Time"] == "18:40"
    assert rows[("Moonlight", "DEL MAR", "2026-07-25")]["Notes"] == "Bing Crosby S. - Grade: 1"

    assert ("The Institute", "FINGER LAKES", "2026-08-18") in rows
    assert ("The Institute", "FINGER LAKES", "2026-08-04") in rows

    assert ("Kaaranah", "Lingfield", "2026-08-13") in rows
    assert rows[("Kaaranah", "Lingfield", "2026-08-13")]["Race Time"] == "17:25"

    cork_horses = {h for (h, t, d) in rows if t == "Cork"}
    assert cork_horses == {
        "Alwaysanangel", "Beibhinn", "Princess Child", "Ankara", "Nyra",
        "Snapretend", "Salamina", "Spinning Around", "Chosen One",
    }

    # "finished"/"non runner" lines must never appear
    assert not any(h in ("Cladach", "Stugardia", "Greydreambeliever") for (h, _, _) in rows)
    print(f"test_full_sample_set OK ({len(df)} rows)")


def test_future_filter():
    df = build(FIXTURES, date(2026, 8, 12))
    assert ("Moonlight", "DEL MAR", "2026-07-25") not in {
        (r["Horse"], r["Track"], str(r["Race Date"])) for r in df.to_dict("records")
    }
    print(f"test_future_filter OK ({len(df)} rows)")


def test_status_dedup_keeps_most_advanced():
    items = [
        {"source": "horsetracker", "date": "2026-08-05T12:00:00Z", "subject": "HorseTracker Update",
         "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*entered at Lingfield on Thursday 13th Aug 5.25*"},
        {"source": "horsetracker", "date": "2026-08-09T12:00:00Z", "subject": "HorseTracker Update",
         "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*declared to run at Lingfield on Thursday 13th Aug 5.30*"},
    ]
    df = build(items, date(2026, 8, 1))
    assert len(df) == 1
    assert df.iloc[0]["Status"] == "declared"
    assert df.iloc[0]["Race Time"] == "17:30"
    print("test_status_dedup_keeps_most_advanced OK")


if __name__ == "__main__":
    test_full_sample_set()
    test_future_filter()
    test_status_dedup_keeps_most_advanced()
    print("All tests passed.")
