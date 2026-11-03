# Scouted Horses — Wed 4 Nov – Thu 5 Nov 2026

Generated 2026-11-03. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## Coverage notes / gaps (read before using this list)

- **`data/tracked/tracked-horses.xlsx` could not be read this cycle.** This session had no tool capable of opening a binary `.xlsx` spreadsheet (the Read tool explicitly rejects binary files, and no shell/script tool was available to unzip and parse it). This is a real gap, not a "nothing found" — any horse currently on the tracked list with a race in this window may be missing from Top Tier below. Recommend re-running the tracked-horses check with a tool that can parse the file, or converting it to CSV for this agent to read directly.
- **UK/Ireland maiden and novice races: sire data was not available from the sources used.** Racing Post's racecard pages (the only ones that loaded with runner-level detail — Timeform, At The Races and Sporting Life all failed to render or returned errors) consistently omitted sire/pedigree information in the fetched content. So the top-sire/damsire criterion could only be checked for USA maiden/novice races this cycle, not UK/Irish ones — only the Notebook, tracked-horse, and trainer-follow checks were completed for Kempton, Musselburgh, Nottingham, Dundalk, Chelmsford and Southwell maiden/novice races. Betting odds were likewise blank on every UK/Ireland racecard fetched.
- **France: no Flat (plat) meeting could be confirmed for 4 or 5 November 2026.** France Galop's own official "Programme National Officiel — Plat" brochure explicitly covers only 1 September to 31 October 2026, and no November/December 2026 edition could be found despite repeated searches (the 2025 equivalent exists and was found, but not a 2026 one — it may simply not be published yet). Several standard French sources are not reachable from this sandbox at all (geny.com, equidia.fr, canalturf.com, ressources.anj.fr/ANJ official calendar, planetsport.com — all DNS-blocked), and Timeform/At The Races failed to render for French tracks too. Racing Post's and HRI's daily listings didn't show any French meeting either. This is a genuine coverage gap — it is plausible French flat racing is between its autumn turf programme and the Côte d'Azur winter meeting (which other sources suggest opens ~1–2 December 2026 at Cagnes-sur-Mer), but that could not be confirmed either way.
- **USA — only Churchill Downs (both days) and Belmont Park (Thu 5 Nov only) have cards among the 8 in-scope tracks.** Santa Anita, Del Mar, Keeneland, Saratoga, Gulfstream Park and Aqueduct are all confirmed **dark** on both 4 and 5 Nov via Horse Racing Nation's daily track listings — this was checked directly, not just absent from search, so treat it as confirmed rather than a gap. Keeneland's 2026 fall meet closed 24 Oct and the Breeders' Cup (30–31 Oct) was its final card before an off period.
- **2nd-career-start and class-drop criteria could not be applied.** Neither Racing Post's nor Horse Racing Nation's fetched content reliably surfaced number of career starts or prior-race class/finish for individual runners, so criteria #2 and #3 in `criteria.md` weren't checked this cycle beyond what was visible at a glance (no Group/Graded races appeared in this window's card anyway, so #3 likely didn't apply regardless).
- Everything else below was researched via Racing Post individual racecard pages (UK/Ireland — fetched race-by-race since the meeting-summary pages don't expose runner detail) and Horse Racing Nation dated entries pages (USA).

## News

**UK**
- Andrew Balding has an unusually large six runners in novice/maiden/handicap company at Kempton's Wednesday card, including three of the fourteen runners in the 16:30 British EBF Future Stayers Maiden Stakes alone.

**Ireland**
- Dundalk's Wednesday 17:45 maiden (3yo+) pits Ger Lyons' Jenny Spider and Justiciar against Paddy Twomey's Otsana, a notable three-way followed-trainer clash in a single maiden race.

**USA**
- Belmont Park's fall card on Thursday is part of its first full season back since the track's September 2026 reopening after redevelopment.
- Into Mischief-sired maidens are thick on the ground at Churchill Downs across both days (six qualify on pedigree alone under the top-sire criterion), reflecting how dominant that sire line remains in US maiden fields this season.

_(France omitted — no meeting could be confirmed; see coverage notes above.)_

## Top Tier

_(No Notebook horses, confirmed tracked horses, or Top-Tier-criterion matches found this cycle — but see the tracked-horses.xlsx gap noted above; this may be incomplete rather than genuinely empty.)_

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Almanueva | Andrew Balding | Jason Watson | Kempton (AW) | UK | Wed 15:30 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Stringalong | Andrew Balding | Callum Hutchinson | Kempton (AW) | UK | Wed 16:00 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Ghost Fire | Andrew Balding | William Carver | Kempton (AW) | UK | Wed 16:30 | N/A | via trainer follow: Andrew Balding — maiden; sire not available from sources used |
| Imperial Soldier | Andrew Balding | Callum Hutchinson | Kempton (AW) | UK | Wed 16:30 | N/A | via trainer follow: Andrew Balding — maiden; sire not available from sources used |
| Noble Archer | Andrew Balding | Jason Watson | Kempton (AW) | UK | Wed 16:30 | N/A | via trainer follow: Andrew Balding — maiden; sire not available from sources used |
| Berkshire Whisper (IRE) | Andrew Balding | Alfie Redman (7) | Kempton (AW) | UK | Wed 17:00 | N/A | via trainer follow: Andrew Balding |
| Hello Friend (IRE) | K R Burke (Karl Burke) | Clifford Lee | Nottingham | UK | Wed 13:20 | N/A | via trainer follow: Karl Burke |
| Marquetry (IRE) | Andrew Balding | P J McDonald | Nottingham | UK | Wed 13:50 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Tele Red | K R Burke (Karl Burke) | Pierre-Louis Jamin | Nottingham | UK | Wed 14:20 | N/A | via trainer follow: Karl Burke |
| Jenny Spider | G M Lyons (Ger Lyons) | Nicola Burns (5) | Dundalk (AW) | Ireland | Wed 17:45 | N/A | via trainer follow: Ger Lyons — maiden; sire not available from sources used |
| Justiciar | G M Lyons (Ger Lyons) | Jack Kearney | Dundalk (AW) | Ireland | Wed 17:45 | N/A | via trainer follow: Ger Lyons — maiden; sire not available from sources used |
| Otsana | P Twomey (Paddy Twomey) | Siobhan Rutledge | Dundalk (AW) | Ireland | Wed 17:45 | N/A | via trainer follow: Paddy Twomey — maiden; sire not available from sources used |
| Lifes Reward | Chris A. Hartman | Danny Sheehy | Churchill Downs | USA | Wed 18:58 | 6/1 | via criterion: top sire/damsire (Into Mischief) — maiden claiming; Sire: Into Mischief |
| Barrel Roll | Chad C. Brown | Tyler Gaffalione | Churchill Downs | USA | Wed 20:26 | 9/2 | via trainer follow: Chad Brown \| via criterion: top sire/damsire (Gun Runner) — maiden; Sire: Gun Runner |
| Grantchester | Ian R. Wilkes | Brian Joseph Hernandez, Jr. | Churchill Downs | USA | Wed 20:26 | 8/1 | via criterion: top sire/damsire (Vekoma) — maiden; Sire: Vekoma |
| Veblen | William I. Mott | Junior Alvarado | Churchill Downs | USA | Wed 20:55 | 9/2 (AE) | via trainer follow: William Mott — maiden; Sire: Tapit |
| Belzoni | William I. Mott | Junior Alvarado | Churchill Downs | USA | Wed 22:24 | 3/1 | via trainer follow: William Mott \| via criterion: top sire/damsire (Gun Runner) — maiden; Sire: Gun Runner |
| Intermediation | Steven M. Asmussen | Keith J. Asmussen | Churchill Downs | USA | Wed 22:24 | 8/1 | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Berkshire Dream | Andrew Balding | Jason Watson | Chelmsford (AW) | UK | Thu 16:45 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Bombora | K R Burke (Karl Burke) | Clifford Lee | Southwell (AW) | UK | Thu 16:00 | N/A | via trainer follow: Karl Burke — novice; sire not available from sources used |
| Global Investment (GB) | Chad C. Brown | Samuel Marin | Belmont Park | USA | Thu 18:10 | N/A | via trainer follow: Chad Brown \| via criterion: top sire/damsire (Frankel) — maiden; Sire: Frankel (GB) |
| Fango Creek | William I. Mott | Jose Lezcano | Belmont Park | USA | Thu 18:10 | N/A | via trainer follow: William Mott — maiden; Sire: Candy Ride (ARG) |
| Sky Chart | William I. Mott | John R. Velazquez | Belmont Park | USA | Thu 18:10 | N/A | via trainer follow: William Mott — maiden; Sire: Liam's Map |
| Black Mountain | Chad C. Brown | Dylan Davis | Belmont Park | USA | Thu 18:10 | N/A | via trainer follow: Chad Brown — maiden; Sire: Street Boss |
| Proper Jack | Chad C. Brown | Javier Castellano | Belmont Park | USA | Thu 19:41 | N/A | via trainer follow: Chad Brown — maiden; Sire: Jackie's Warrior |
| General Partner | Chad C. Brown | Samuel Marin | Belmont Park | USA | Thu 20:12 | N/A | via trainer follow: Chad Brown |
| Our Patricia Ann | Larry Rivelli | Walter A. Rodriguez | Churchill Downs | USA | Thu 21:25 | 7/2 | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Trouble Maker | Victoria H. Oliver | Luis Saez | Churchill Downs | USA | Thu 21:25 | 6/1 | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Swirlin Mischief | Wesley A. Ward | Yomar Ortiz, Jr. | Churchill Downs | USA | Thu 21:25 | 9/2 | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Encrypting | Albert M. Stall, Jr. | Brian Joseph Hernandez, Jr. | Churchill Downs | USA | Thu 21:25 | 15/1 (AE) | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Clever Miss | Steven M. Asmussen | Flavien Prat | Churchill Downs | USA | Thu 22:24 | 6/1 | via criterion: top sire/damsire (Gun Runner) — maiden; Sire: Gun Runner |
| Joy of Life | William I. Mott | Junior Alvarado | Churchill Downs | USA | Thu 22:24 | 5/1 | via trainer follow: William Mott — maiden; Sire: Speaker's Corner |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding | Sire: Frankel")._

_USA race times are converted assuming US Eastern clocks are on EST (UTC-5, having changed from EDT on 1 Nov 2026) and Irish/UK clocks are on GMT (UTC+0) — i.e. Irish time = US Eastern time + 5 hours for this cycle. UK and Irish race times shown are already local/Irish time._
