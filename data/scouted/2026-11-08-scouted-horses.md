# Scouted Horses — Sun 8 Nov 2026

Generated 2026-11-07. Covers Flat races in UK, Ireland, France, USA on Sunday 8 November 2026 only.

## Coverage notes / gaps (read before relying on this list)

- **`data/tracked/tracked-horses.xlsx` checked separately.** The scouting subagent's own session had no tool able to open the binary `.xlsx`, but it was read afterwards with a Python/openpyxl script run outside that subagent. Result: the file has **no rows dated 2026-11-08** at all — its latest entries run Nov 1–6 plus a few future-dated Nov 15/21 entries, with nothing for the 8th. So the empty Top Tier table below is confirmed correct, not a data gap. (Separately, every row in the file is a UK/Ireland National Hunt/Jumps meeting — Curragh, Plumpton, Musselburgh, Kempton, Newbury, Newcastle, Southwell, Fontwell, Cheltenham, Punchestown — so even on a date with entries, none would be in scope for this Flat-only scout. Worth flagging to the user that the tracked-horses feed may currently be Jumps-skewed or simply hasn't picked up any Flat runners recently; recommend giving the scouting agent itself a way to read xlsx, e.g. via Bash/openpyxl, to remove this recurring gap at the source.)
- **UK: no Flat racing anywhere in Britain on 8 Nov 2026.** Racing Post's worldwide racecard index for the date lists only Sandown and Ffos Las (both Jumps) in Britain. Cross-checked against Lingfield Park's own "Sunday afternoon November all-weather racing 2026" fixture, which is dated **Sunday 22 November**, not the 8th — confirming no UK all-weather Sunday card this week. Treated as a confirmed absence, not a data gap.
- **Ireland: no Flat racing on 8 Nov 2026.** The only Irish fixture on the date is Naas (Jumps). Dundalk's November 2026 all-weather fixtures run Wednesdays and Fridays only (4th, 6th, 11th, 13th, 18th, 20th, 25th, 27th) — no Sunday card. Confirmed absence, not a gap.
- **France: Saint-Cloud runs a 2-race Flat card** — the Listed Prix Tantième (13:33 local) and Listed Prix Solitude (16:00 local), both confirmed via Racing Post's dated racecard. No followed trainer, Notebook horse, or top-sire/damsire maiden-race match applies here (both races are Listed, not maiden/novice, so the top-sire criterion doesn't apply). Criterion #3 (class-drop off a Group 1–3 top-5 run into a handicap/Listed race) is the one that could plausibly apply to a Listed race like this, but checking it properly means confirming the most recent run and finish position for every one of the roughly 22 declared runners — not feasible within this session's research budget. One runner flagged in News below (Legacy Link, Gosden) looked like a plausible candidate, but her most recent form returned conflicting results (a 2nd in the Epsom Oaks vs. a reported 9th in the Yorkshire Oaks as the more recent run) and she was left out rather than guessed onto the list.
- **USA: Santa Anita (fall meet closed 1 Nov 2026), Keeneland (fall meet closed 24 Oct 2026 ahead of hosting the Breeders' Cup on 30–31 Oct), Saratoga (meet ended Labor Day) and Aqueduct (permanently ceased live racing; NYRA's downstate racing moved to the rebuilt Belmont Park) are all dark/inactive — confirmed via Horse Racing Nation's daily track listing, which omits all four for this date.** Churchill Downs, Belmont Park, Gulfstream Park and Del Mar all carded and were fully checked (all races, all runners, sires and morning-line odds).
- **Criteria #2 (2nd career start for a followed trainer) and #4 (USA top-trainer MSW→maiden-claimer drop) could not be confirmed.** Three Maiden Claiming runners by followed trainers — Prairie Princess (Chad Brown), Thunder Roll (William Mott), Sfumato (William Mott) — are exactly the shape of horse criterion #4 is designed for, but none of the sources used (Horse Racing Nation entries, web search) reliably surfaced each horse's start count or most recent race type/class; searches returned unreliable or conflicting results. All three are listed below only via plain trainer-follow (The Rest), which may understate Top Tier.
- Everything below was researched via Racing Post (France, and the UK/Ireland absence check) and Horse Racing Nation's dated entries pages (USA: Churchill Downs, Belmont Park, Gulfstream Park, Del Mar).

## News

**France**
- Saint-Cloud's Listed Prix Solitude (16:00 local) draws John & Thady Gosden's Legacy Link (GB) — Frankel's niece and a runner-up in this year's Epsom Oaks — for Colin Keane, alongside Donnacha O'Brien's Glyfada (IRE) and Alessandro Botti's Aurora Beau Real (IRE).

**USA**
- With Keeneland's fall meet having closed ahead of hosting the Breeders' Cup (30–31 Oct) and Santa Anita's fall meet closed since 1 Nov, Sunday's US card is confined to Churchill Downs, Belmont Park, Gulfstream Park and Del Mar; Del Mar's Grade 3 Betty Grable Stakes (7f, fillies & mares) closes out its fall meet with Sean McCarthy's Grand Slam Smile a short-priced favourite.

_(UK and Ireland omitted — no Flat racing in either country on this date; see coverage notes above.)_

## Top Tier

No horses qualified as Top Tier this cycle. The tracked-horses.xlsx check (see coverage notes above) confirms there are no tracked horses running on this date, so this is not a result of missing data. No Notebook horse, confirmed 2nd-career-start-for-followed-trainer case, confirmed Group-to-handicap/Listed class-drop case, or confirmed MSW-to-maiden-claimer drop for a followed USA trainer could be established from the data gathered.

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Prairie Princess | Chad C. Brown | Tyler Gaffalione | Churchill Downs | USA | 18:00 | 7/5 | via trainer follow: Chad Brown — maiden claiming; Sire: Essential Quality |
| Free Verse (AE) | Brad H. Cox | Florent Geroux | Churchill Downs | USA | 18:58 | 6/5 | via criterion: top sire/damsire (Justify) — maiden special weight; Sire: Justify; also-eligible, may not run |
| Bedeviled | Steven M. Asmussen | Luis Saez | Churchill Downs | USA | 20:26 | 9/2 | via criterion: top sire/damsire (Gun Runner) — maiden claiming; Sire: Gun Runner |
| Thunder Roll | William I. Mott | Junior Alvarado | Churchill Downs | USA | 20:26 | 7/2 | via trainer follow: William Mott — maiden claiming; Sire: Hard Spun |
| Hypnotica | Chad C. Brown | Flavien Prat | Belmont Park | USA | 18:40 | 5/2 | via trainer follow: Chad Brown — maiden special weight; Sire: Charlatan |
| Candidly | Chad C. Brown | Manuel Franco | Belmont Park | USA | 18:40 | 7/2 | via trainer follow: Chad Brown — maiden special weight; Sire: Medaglia d'Oro |
| Franklin Delano | Todd A. Pletcher | Flavien Prat | Belmont Park | USA | 19:10 | 6/5 | via trainer follow: Todd Pletcher — claiming (not maiden) |
| Crowned Moment (GB) | Ilkay Kantarmaci | Christopher Elliott | Belmont Park | USA | 19:41 | 20/1 | via criterion: top sire/damsire (Kingman) — maiden claiming; Sire: Kingman (GB) |
| Eske Castle (IRE) | Wesley A. Ward | Antonio Fresu | Belmont Park | USA | 19:41 | 2/1 | via criterion: top sire/damsire (No Nay Never) — maiden claiming; Sire: No Nay Never |
| Sellonthenews (GB) | Chad C. Brown | Manuel Franco | Belmont Park | USA | 20:12 | 2/1 | via trainer follow: Chad Brown | via criterion: top sire/damsire (Lope de Vega) — maiden special weight; Sire: Lope de Vega (IRE) |
| Inflect | Chad C. Brown | Flavien Prat | Belmont Park | USA | 20:12 | 5/2 | via trainer follow: Chad Brown — maiden special weight; Sire: Uncle Mo |
| Royal Victoria | William I. Mott | Antonio Fresu | Belmont Park | USA | 20:12 | 8/1 | via trainer follow: William Mott | via criterion: top sire/damsire (Into Mischief) — maiden special weight; Sire: Into Mischief |
| Golden Ember | William I. Mott | Katie Davis | Belmont Park | USA | 20:12 | 20/1 | via trainer follow: William Mott — maiden special weight; Sire: Constitution |
| Time to Win | Chad C. Brown | Flavien Prat | Belmont Park | USA | 20:43 | 4/5 | via trainer follow: Chad Brown — allowance optional claiming (not maiden) |
| Sfumato | William I. Mott | Jose Lezcano | Belmont Park | USA | 21:14 | 3/1 | via trainer follow: William Mott — maiden claiming; Sire: Connect |
| Whatastarr (IRE) | Leonard Powell | Micah Meeks | Del Mar | USA | 22:03 | 6/1 | via criterion: top sire/damsire (No Nay Never) — maiden claiming; Sire: No Nay Never |
| Himari | Bob Baffert | Juan J. Hernandez | Del Mar | USA | 23:03 | 6/5 | via trainer follow: Bob Baffert — allowance optional claiming (not maiden) |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding | Sire: Frankel"). "AE"/"also-eligible" horses may be scratched before racing._

_No qualifying horses were found at Gulfstream Park on this card — no followed trainer, Notebook horse, or top-sire match turned up among its ten races._

_USA race times are converted to Irish time assuming Churchill Downs, Belmont Park and Gulfstream Park are on US Eastern (EST, UTC−5) and Del Mar is on US Pacific (PST, UTC−8) — both zones having already left daylight saving time by 8 Nov 2026 (DST ended 1 Nov in the US). Irish time = US Eastern + 5 hours, or US Pacific + 8 hours._
