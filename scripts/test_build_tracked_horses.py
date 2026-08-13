#!/usr/bin/env python3
"""Regression tests for build_tracked_horses.py, run against real (anonymized
none-needed -- these are the user's own tracked-horse emails) sample bodies
pulled from virtualstable@equibase.com and horsetracker@irishracing.com.

Run with: python scripts/test_build_tracked_horses.py
"""
import json
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_tracked_horses import build, build_merged  # noqa: E402

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


def test_virtualstable_country_suffix_name():
    df = build(FIXTURES, date(2025, 8, 1))
    records = df.to_dict("records")
    rows = {(r["Horse"], r["Track"], str(r["Race Date"])): r for r in records}
    assert ("Milliat (IRE)", "PRESQUE ISLE DOWNS", "2025-09-19") in rows
    print("test_virtualstable_country_suffix_name OK")


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


def test_merge_preserves_prior_batches():
    with tempfile.TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "tracked.xlsx"
        batch1 = [{"source": "horsetracker", "date": "2026-08-05T12:00:00Z", "subject": "HorseTracker Update",
                   "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*entered at Lingfield on Thursday 13th Aug 5.25*"}]
        build(batch1, date(2026, 8, 1)).to_excel(out_path, index=False)

        batch2 = [{"source": "horsetracker", "date": "2026-08-06T12:00:00Z", "subject": "HorseTracker Update",
                   "text": "## Tracked Horses\n### Manaar (IRE)\n\n*declared to run at Kempton on Wednesday 12th Aug 6.00*"}]
        merged = build_merged(batch2, date(2026, 8, 1), out_path)
        assert set(merged["Horse"]) == {"Kaaranah", "Manaar"}
        print("test_merge_preserves_prior_batches OK")


def test_merge_updates_status_of_existing_row():
    with tempfile.TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "tracked.xlsx"
        batch1 = [{"source": "horsetracker", "date": "2026-08-05T12:00:00Z", "subject": "HorseTracker Update",
                   "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*entered at Lingfield on Thursday 13th Aug 5.25*"}]
        build(batch1, date(2026, 8, 1)).to_excel(out_path, index=False)

        batch2 = [{"source": "horsetracker", "date": "2026-08-09T12:00:00Z", "subject": "HorseTracker Update",
                   "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*declared to run at Lingfield on Thursday 13th Aug 5.30*"}]
        merged = build_merged(batch2, date(2026, 8, 1), out_path)
        assert len(merged) == 1
        assert merged.iloc[0]["Status"] == "declared"
        assert merged.iloc[0]["Race Time"] == "17:30"
        print("test_merge_updates_status_of_existing_row OK")


def test_merge_reapplies_future_filter_to_existing_rows():
    with tempfile.TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "tracked.xlsx"
        batch1 = [{"source": "horsetracker", "date": "2026-08-05T12:00:00Z", "subject": "HorseTracker Update",
                   "text": "## Tracked Horses\n### Kaaranah (IRE)\n\n*entered at Lingfield on Thursday 13th Aug 5.25*"}]
        build(batch1, date(2026, 8, 1)).to_excel(out_path, index=False)

        # A later run, as_of has now passed the existing row's race date -- it should drop out.
        merged = build_merged([], date(2026, 8, 20), out_path)
        assert len(merged) == 0
        print("test_merge_reapplies_future_filter_to_existing_rows OK")


if __name__ == "__main__":
    test_full_sample_set()
    test_future_filter()
    test_virtualstable_country_suffix_name()
    test_status_dedup_keeps_most_advanced()
    test_merge_preserves_prior_batches()
    test_merge_updates_status_of_existing_row()
    test_merge_reapplies_future_filter_to_existing_rows()
    print("All tests passed.")
