# Agent Racing Scout

Personal project for scouting **Flat** horse racing across the **UK, Ireland, France, and USA**, shortlisting horses worth a closer look for betting purposes via the **Racing Scout** agent. Criteria are developed and refined over time, not fixed up front. Jumps/National Hunt racing is out of scope here — a separate scout will be built for that later.

## Layout

```
Agent_Racing_Scout/
├── .claude/agents/racing-scout.md   Racing Scout subagent definition
└── data/
    ├── criteria/criteria.md         Evolving criteria/systems (starts blank)
    ├── notebook/horses.csv          Individual horses flagged to follow, with notes
    ├── notebook/trainers.csv        Trainers flagged to follow
    ├── races/                       Racecard/meeting data, per day or meeting
    ├── scouted/                     Generated Scouted Horses lists (one per cycle)
    └── research/                    Ad-hoc scouting write-ups outside the regular cycle
```

## Using the Racing Scout

Open Claude Code in this folder (`Agent_Racing_Scout/`) and:
- give it a horse name + notes to add to the **Notebook**
- tell it a trainer to add to the **follow list**
- teach it a new criterion/system any time — it records these in `data/criteria/criteria.md`
- ask it to scout a date/track/country ad hoc, or produce the **Scouted Horses** list

## Scouted Horses cadence

- **Sunday afternoon** → covers racing **Monday–Wednesday**
- **Wednesday afternoon** → covers racing **Thursday–Sunday**

Each run checks the Notebook, the trainer follow list, and current criteria against racecards across UK/Ireland/France/USA, and produces a table of: Horse, Trainer, Jockey, Track, Country, Race Time (Irish), Odds, Notes — saved to `data/scouted/` and emailed. Delivery/automation setup is tracked below.

## Status

- [x] Folder structure
- [x] Racing Scout agent
- [x] Notebook + trainer follow list structure
- [x] GitHub repo pushed (needed for the cloud scheduled routine)
- [x] Email delivery wired up (Gmail MCP connector — drafts only, no send capability, so the agent creates/updates a Gmail draft each cycle for the user to send manually). The Gmail connector is permanently parked on **cooperkevin1985@gmail.com** (decided 2026-08-15) — this is also the account the horsetracker/virtualstable tracked-horse emails land in, so no account-swapping or forwarding filter is needed. Scouted Horses drafts are self-addressed to cooperkevin1985@gmail.com.
- [x] Criteria added to `data/criteria/criteria.md` (4 so far: top sire/damsire in maiden-novice, 2nd career start for a followed trainer, class-drop off Group form, USA top-trainer MSW-to-claimer drop)
- [x] Sunday/Wednesday 2pm Irish time routine created (cloud routines `trig_012sduS8BWEiDkkicECJSokm` Sun, `trig_01HCT4cvt9yD9CYUuSmJ6Y23` Wed)
- [x] Run first scouting session (infrastructure confirmed working: network access to UK/Ireland/France sources plus Horse Racing Nation/NYRA for USA, Gmail draft creation, and GitHub push all verified via test runs)
- [x] Tracked-horses 15-month backfill (completed 2026-08-15 — 479 threads/messages processed across a 455-day window, `data/tracked/tracked-horses.xlsx` now holds current upcoming tracked horses from HorseTracker + VirtualStable)
- [x] Tracked horses wired into Scouted Horses Top Tier criteria (`.claude/agents/racing-scout.md` step 2/3, `data/criteria/criteria.md` tiering section — any horse in `tracked-horses.xlsx` running in a cycle's date range is automatic Top Tier, same as a Notebook horse)
- [x] Weekly incremental tracked-horses update schedule (cloud routine `trig_015nKv5NzNkE272gbNwiARnC`, 08:00 UTC every Sunday — 8-day lookback, ahead of the 14:00 UTC Sunday Scouted Horses cycle)
