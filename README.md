# Agent Racing Scout

Personal project for scouting horse racing across the **UK, Ireland, France, and USA**, shortlisting horses worth a closer look for betting purposes via the **Racing Scout** agent. Criteria are developed and refined over time, not fixed up front.

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
- [ ] Add first criteria to `data/criteria/criteria.md`
- [ ] GitHub repo pushed (needed for the cloud scheduled routine)
- [ ] Email delivery wired up (Gmail — checking for an MCP connector vs. local fallback)
- [ ] Sunday/Wednesday 2pm Irish time routine created
- [ ] Run first scouting session
