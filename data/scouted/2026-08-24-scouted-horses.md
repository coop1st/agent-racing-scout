# Scouted Horses — Mon 24–Tue 25 Aug 2026

Generated 2026-08-23. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## News

**UK**
- Andrew Balding sends a strong three-runner raid to Windsor's Monday evening card (Nakila Sun GER, Cape Fear, Berkshire Boom IRE), all booked for stable rider Oisin Murphy.
- Karl Burke (K R Burke) has runners on both days at Musselburgh — Astral Calling and Light The Night Up on Monday, debutant-adjacent maiden Vegasmile IRE on Tuesday.

**Ireland**
- Bellewstown's Tuesday evening card is well stocked with follow-list interest: Ger Lyons (3 runners), Joseph O'Brien (3) and Aidan O'Brien (1) are all represented across the card's two maiden races.
- Joseph O'Brien's Salamina steps up to just her second career start in the Bellewstown maiden (16:20) after a promising debut — a stronger signal per the 2nd-start criterion.

**USA**
- Saratoga and Del Mar are both dark Monday and Tuesday this week (their summer meets run Wednesday–Sunday), leaving Gulfstream Park as the only in-scope US track racing over this cycle; nothing on its Monday card matched the Notebook, tracked list, follow list, or current criteria.

_(France omitted — see coverage note below; no meeting could be confirmed via the designated sources.)_

## Top Tier

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Salamina | Joseph Patrick O'Brien | Shay Wallace | Bellewstown | Ireland | Tue 16:20 | N/A | via criterion: 2nd-start top trainer (Joseph O'Brien) — this is her 2nd career start | Sire: not obtainable this cycle (see coverage note) |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Astral Calling | K R Burke | Jack Nicholls | Musselburgh | UK | Mon 14:45 | N/A | via trainer follow: Karl Burke |
| Light The Night Up | K R Burke | Jack Nicholls | Musselburgh | UK | Mon 15:45 | N/A | via trainer follow: Karl Burke |
| Nakila Sun GER | Andrew Balding | Oisin Murphy | Windsor | UK | Mon 17:48 | N/A | via trainer follow: Andrew Balding | Sire: not obtainable this cycle (Restricted Novice Stakes) |
| Cape Fear | Andrew Balding | Oisin Murphy | Windsor | UK | Mon 18:18 | N/A | via trainer follow: Andrew Balding |
| Berkshire Boom IRE | Andrew Balding | Oisin Murphy | Windsor | UK | Mon 18:48 | N/A | via trainer follow: Andrew Balding |
| Vegasmile IRE | K R Burke | Clifford Lee | Musselburgh | UK | Tue 14:15 | N/A | via trainer follow: Karl Burke | Sire: not obtainable this cycle (Maiden) |
| Floating Market | Andrew Balding | Isobelle Chalmers | Lingfield (AW) | UK | Tue 16:30 | N/A | via trainer follow: Andrew Balding | Sire: not obtainable this cycle (Restricted Novice Stakes) |
| Thunder Goddess | Andrew Balding | William Carver | Lingfield (AW) | UK | Tue 17:02 | N/A | via trainer follow: Andrew Balding |
| Camino Lad | G M Lyons (Ger Lyons) | Colin Keane | Bellewstown | Ireland | Tue 16:20 | N/A | via trainer follow: Ger Lyons | Sire: not obtainable this cycle (Maiden) |
| Willofthepeople | G M Lyons (Ger Lyons) | Gary Carroll | Bellewstown | Ireland | Tue 16:20 | N/A | via trainer follow: Ger Lyons | Sire: not obtainable this cycle (Maiden) |
| Mosel | Joseph Patrick O'Brien | Dylan Browne McMonagle | Bellewstown | Ireland | Tue 16:20 | N/A | via trainer follow: Joseph O'Brien | Sire: not obtainable this cycle (Maiden) |
| Elusive Path | G M Lyons (Ger Lyons) | Colin Keane | Bellewstown | Ireland | Tue 18:02 | N/A | via trainer follow: Ger Lyons |
| Cosmetic | A P O'Brien (Aidan O'Brien) | Wayne Lordan | Bellewstown | Ireland | Tue 19:32 | N/A | via trainer follow: Aidan O'Brien | Sire: not obtainable this cycle (Fillies Maiden) |
| Mawhibah QA | Joseph Patrick O'Brien | Dylan Browne McMonagle | Bellewstown | Ireland | Tue 19:32 | N/A | via trainer follow: Joseph O'Brien | Sire: not obtainable this cycle (Fillies Maiden) |

## Coverage notes / gaps this cycle

- **Tracked horses (`data/tracked/tracked-horses.xlsx`) checked separately after the initial pass** (the scouting subagent had no tool capable of parsing the binary .xlsx spreadsheet). The file's earliest upcoming entry is Equus Victor at Navan on Thu 27 Aug 2026 — no rows fall within this cycle's 24–25 Aug window, so no tracked horse was missed.
- **Sire/pedigree data was not obtainable for any UK or Ireland runner this cycle.** Racing Post's racecard pages (both meeting-level and individual horse profile pages) render pedigree information in a form the WebFetch tool could not extract (JS-rendered or omitted from the simplified content), and Timeform's racecards returned 403 Forbidden. This means the top-sire/damsire maiden-novice criterion could not be screened across any UK/Ireland maiden or novice field this cycle, and the "append sire to Notes" requirement for maiden/novice qualifiers above is unfulfilled (flagged individually in each row). USA sire data was available directly via Horse Racing Nation and was checked (no matches against the top-sire list in Gulfstream Park's maiden claiming races).
- **France: no meeting could be confirmed via the designated sources (France Galop, Racing Post) for 24–25 Aug 2026.** Racing Post's UK racecard pages showed no French fixture on either date, and France Galop's site only exposes PDF programme documents that weren't extractable via WebFetch. Web search turned up secondary references to smaller provincial flat meetings at Vittel and Dieppe on Monday 24 Aug, but entry-level detail wasn't reachable — every French racing/PMU site tried (zone-turf.fr, geny.com, turfoo.fr, coursesvichy.fr, hippodrome-dieppe.com, c-f.fr, vittel.hippodromes-est.fr) was blocked by the network egress proxy. Deauville, Chantilly, and other major French tracks were checked and do not appear to have Group/notable fixtures on these two dates (Deauville's final Group 1s of the meeting were on Sunday 23 Aug, one day before this cycle's window). Flagging this as a genuine coverage gap rather than an assumption of "no racing."
- **Odds:** Racing Post's racecard pages did not reliably expose current betting-forecast odds through WebFetch (returned career form-figure strings instead in several cases); rather than risk presenting incorrect prices, odds are shown as N/A throughout. USA odds (Gulfstream Park) were available but not needed since no USA horse qualified.
- **USA scope:** confirmed via Horse Racing Nation's full daily track index that none of Santa Anita, Del Mar, Keeneland, Churchill Downs, Belmont, Aqueduct, or Saratoga are racing on 24–25 Aug 2026 (Saratoga/Del Mar summer meets run Wed–Sun; the others are between meets). Gulfstream Park was the only in-scope US track live, Monday only, with full entries checked — no qualifiers.
- Ballinrobe (Ireland, Mon 24 Aug) and Stratford (UK, Tue 25 Aug) were confirmed Jumps/National Hunt meetings and correctly excluded from this Flat-only scan.
