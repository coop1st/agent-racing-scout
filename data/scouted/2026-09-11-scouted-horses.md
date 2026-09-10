# Scouted Horses — Fri 11–Sat 12 Sept 2026

Generated 2026-09-10. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## News

**UK**
- The St Leger Festival concludes at Doncaster on Saturday with the Betfred St Leger Stakes (Group 1) itself, featuring four Aidan O'Brien runners (Action, Christmas Day, Pierre Bonnard, Amelia Earhart) as he chases a record-extending Leger, plus Joseph O'Brien's Enceladus and Highwayman, Andrew Balding's Galiyan and Hatteen, and Karl Burke's Golden Story.

**Ireland**
- The Irish Champions Festival opens at Leopardstown on Saturday, built around two Group 1s: the Irish Champion Stakes, where a strong British raiding party (Andrew Balding's Item, Ed Walker's Almaqam, George Scott's Wimbledon Hawkeye) takes on Aidan O'Brien's trio of Lambourn, Constitution River and Hawk Mountain as he seeks a record-extending 14th win in the race; and the Matron Stakes, where Karl Burke's Fallen Angel defends her crown against Andrew Balding's unbeaten-in-four Blue Bolt, bidding for a third straight Group 1.

**France**
- Saint-Cloud stages a Listed card on Friday headlined by the Prix Turenne (3-year-olds, 8 runners) — full details for the rest of the card weren't accessible via the sources used this cycle (see coverage note below).

**USA**
- With Del Mar and Saratoga both having closed for the season over Labor Day weekend (7 Sept), and Santa Anita/Keeneland not yet open, Churchill Downs is the marquee US card this weekend: four stakes on Saturday (Open Mind S., Louisville Thoroughbred Society S., Pocahontas S., Locust Grove S., Iroquois S.), with Bob Baffert fielding runners in six of the card's eleven races across the two days.

## Coverage notes (read before relying on this list)

- **`data/tracked/tracked-horses.xlsx` was cross-checked in a follow-up pass** (the drafting agent's toolset couldn't open the binary file; it was read separately and reconciled against live racecards). Of 7 tracked-horse entries falling in 11–12 Sept: **Without Compromise** (Doncaster, 17:20) and **James J Braddock** (Leopardstown, 15:15) were confirmed running and are in Top Tier; **Pierre Bonnard** was also confirmed running (Doncaster 15:35, St Leger day) but the tracker's own track/time (Leopardstown, 13:00) doesn't match the current racecard — likely a stale entry from when he was originally entered elsewhere, superseded by his St Leger entry. The remaining four tracker rows for this window — **Equus Victor** (Doncaster), **Benvenuto Cellini**, **Montreal**, and **Puerto Rico** (all listed against Leopardstown) — could not be found on the current Doncaster/Leopardstown racecards at all despite a full-card check, so they're **not** included; all four tracker rows are "entered" status dating back to May–July 2026 and look stale. Recommend the weekly `build_tracked_horses.py` refresh be checked/re-run so this file reflects current declarations.
- **Saint-Cloud (France, Fri 11 Sept):** only the feature Prix Turenne (Listed, 13:53 local) came through in runner-level detail. Secondary sources indicate a fuller card (Prix Kaldoun, Prix Astaria, Prix Bend'Or, Prix Fiterari among the race names mentioned), but Racing Post's page only rendered the feature race for the tools available — the rest of the card wasn't checked against the Notebook/trainer/criteria lists.
- **Ballinrobe (Ireland, Fri 11 Sept)** was a Jumps/National Hunt fixture and is excluded, as is any other NH racing across the weekend.
- **USA scheduling:** of the eight in-scope US tracks, only **Churchill Downs** and **Gulfstream Park** are actually racing on 11–12 September 2026. Del Mar and Saratoga closed for the season on Labor Day (7 Sept), Santa Anita's autumn meet doesn't open until 25 Sept, Keeneland's fall meet doesn't open until 2 Oct, and Belmont Park's fall meet doesn't open until 18 Sept (Aqueduct's live racing closed permanently in June 2026). This is a scheduling fact, not a data-access failure.
- **Deep-form criteria** (2nd career start for a followed trainer; class-drop off a Group/Grade 1–3 top-5 run into a handicap/Listed race) were only applied where past-form context surfaced naturally during research. This was an exceptionally busy weekend for followed trainers (St Leger Festival + Irish Champions Weekend, ~120+ qualifying runners), and a full past-performance check on every single trainer-follow horse wasn't feasible — so some horses sitting in The Rest below may actually deserve Top Tier on closer inspection.
- **Sire** could not be confirmed for several maiden/novice runners despite specifically checking (noted per horse below); Racing Post's pedigree data wasn't reliably rendered by the tools available this cycle.
- **Notebook horses:** none of Gstaad, Bow Echo, or Sovereignty have a runner in this date range — Gstaad's next confirmed start is the Queen Elizabeth II Stakes at Ascot (17 Oct), Bow Echo has been retired, and Sovereignty is being targeted at the Jockey Club Gold Cup at Belmont (18 Sept) — so per standing instructions none of them appear in the tables below.

## Top Tier

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Without Compromise | Antony Brittain | Cam Hardie | Doncaster | UK | 17:20 | 20/1 | via tracked horse (status: entered, source: horsetracker) |
| James J Braddock (GB) | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 15:15 | — | via tracked horse (status: entered, source: horsetracker); also via trainer follow: Joseph O'Brien |
| Pierre Bonnard (IRE) | Aidan O'Brien | Wayne Lordan | Doncaster | UK | 15:35 | — | via tracked horse (status: entered, source: horsetracker — tracker listed Leopardstown/13:00 but current racecard confirms this runner at the St Leger meeting, Doncaster 15:35); also via trainer follow: Aidan O'Brien |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Bellesque | Joseph Patrick O'Brien | Declan McDonogh | Leopardstown | Ireland | 13:35 | — | via trainer follow: Joseph O'Brien |
| Blonde Over Blue (GB) | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 13:35 | — | via trainer follow: Joseph O'Brien |
| Ibelieveicanfly (USA) | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 13:35 | — | via trainer follow: Aidan O'Brien |
| Maire Rua (GB) | Ger Lyons | Colin Keane | Leopardstown | Ireland | 13:35 | — | via trainer follow: Ger Lyons |
| Snowing | Aidan O'Brien | Pierre-Charles Boudot | Leopardstown | Ireland | 13:35 | — | via trainer follow: Aidan O'Brien |
| Andab | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 14:10 | — | via trainer follow: Joseph O'Brien |
| Dorset | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 14:10 | — | via trainer follow: Aidan O'Brien |
| Howd'yadoit | Ger Lyons | Gary Carroll | Leopardstown | Ireland | 14:10 | — | via trainer follow: Ger Lyons |
| Krasimir | Ger Lyons | Reese Holohan | Leopardstown | Ireland | 14:10 | — | via trainer follow: Ger Lyons |
| Aix La Chapelle (USA) | Aidan O'Brien | Christophe Soumillon | Leopardstown | Ireland | 14:45 | 14/1 | via trainer follow: Aidan O'Brien |
| Darkness Falls | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 14:45 | 33/1 | via trainer follow: Aidan O'Brien |
| Green Dreamer | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 14:45 | — | via trainer follow: Joseph O'Brien |
| Jesus Green | Joseph Patrick O'Brien | Colin Keane | Leopardstown | Ireland | 14:45 | 2/1 | via trainer follow: Joseph O'Brien |
| Shakespeare (GB) | Aidan O'Brien | Pierre-Charles Boudot | Leopardstown | Ireland | 14:45 | — | via trainer follow: Aidan O'Brien |
| Victory Speech | Aidan O'Brien | Gavin Ryan | Leopardstown | Ireland | 14:45 | — | via trainer follow: Aidan O'Brien |
| Zarak Pasha | Joseph Patrick O'Brien | Declan McDonogh | Leopardstown | Ireland | 14:45 | — | via trainer follow: Joseph O'Brien |
| Sons And Lovers (GB) | Joseph Patrick O'Brien | Oisin Murphy | Leopardstown | Ireland | 15:15 | — | via trainer follow: Joseph O'Brien |
| Goodie Two Shoes | Joseph Patrick O'Brien | Declan McDonogh | Leopardstown | Ireland | 15:15 | — | via trainer follow: Joseph O'Brien |
| Piazza San Marco (USA) | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 15:15 | — | via trainer follow: Aidan O'Brien |
| Blue Bolt | Andrew Balding | Colin Keane | Leopardstown | Ireland | 15:55 | — | via trainer follow: Andrew Balding |
| City Of Memphis | Paddy Twomey | W J Lee | Leopardstown | Ireland | 15:55 | — | via trainer follow: Paddy Twomey |
| Fallen Angel (GB) | Karl Burke | James Doyle | Leopardstown | Ireland | 15:55 | — | via trainer follow: Karl Burke |
| Precise | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 15:55 | — | via trainer follow: Aidan O'Brien |
| True Love | Aidan O'Brien | Pierre-Charles Boudot | Leopardstown | Ireland | 15:55 | — | via trainer follow: Aidan O'Brien |
| Cowardofthecounty | Joseph Patrick O'Brien | Declan McDonogh | Leopardstown | Ireland | 16:25 | — | via trainer follow: Joseph O'Brien |
| Expanded | Aidan O'Brien | Pierre-Charles Boudot | Leopardstown | Ireland | 16:25 | — | via trainer follow: Aidan O'Brien |
| Faiyum (GB) | Ger Lyons | Colin Keane | Leopardstown | Ireland | 16:25 | — | via trainer follow: Ger Lyons |
| Princess Child (FR) | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 16:25 | — | via trainer follow: Joseph O'Brien |
| Charles Fort (GB) | Aidan O'Brien | Christophe Soumillon | Leopardstown | Ireland | 16:25 | — | via trainer follow: Aidan O'Brien |
| Isaac Newton | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 16:25 | — | via trainer follow: Aidan O'Brien |
| Lambourn | Aidan O'Brien | Declan McDonogh | Leopardstown | Ireland | 17:00 | — | via trainer follow: Aidan O'Brien |
| Constitution River | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 17:00 | — | via trainer follow: Aidan O'Brien |
| Hawk Mountain | Aidan O'Brien | Pierre-Charles Boudot | Leopardstown | Ireland | 17:00 | — | via trainer follow: Aidan O'Brien |
| Item | Andrew Balding | Colin Keane | Leopardstown | Ireland | 17:00 | — | via trainer follow: Andrew Balding |
| Comfort Zone | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 17:35 | — | via trainer follow: Joseph O'Brien |
| Dawn Rising | Joseph Patrick O'Brien | Declan McDonogh | Leopardstown | Ireland | 17:35 | — | via trainer follow: Joseph O'Brien |
| Port Of Spain | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 17:35 | — | via trainer follow: Aidan O'Brien |
| Glenroyal | Joseph Patrick O'Brien | Chris Hayes | Leopardstown | Ireland | 17:35 | — | via trainer follow: Joseph O'Brien |
| Cannes | Joseph Patrick O'Brien | Colin Keane | Leopardstown | Ireland | 17:35 | — | via trainer follow: Joseph O'Brien |
| Yousaynothingatall | Joseph Patrick O'Brien | Oisin Murphy | Leopardstown | Ireland | 17:35 | — | via trainer follow: Joseph O'Brien |
| Quebec | Joseph Patrick O'Brien | J M Sheridan | Leopardstown | Ireland | 18:10 | — | via trainer follow: Joseph O'Brien |
| Suzie Songs | Ger Lyons | Colin Keane | Leopardstown | Ireland | 18:10 | — | via trainer follow: Ger Lyons |
| Mallavelly | Ger Lyons | Gary Carroll | Leopardstown | Ireland | 18:10 | — | via trainer follow: Ger Lyons |
| Drop Dead Gorgeous | Aidan O'Brien | Ryan Moore | Leopardstown | Ireland | 18:10 | — | via trainer follow: Aidan O'Brien |
| Varzi | Karl Burke | Sam James | Doncaster | UK | 13:15 | 12/1 | via trainer follow: Karl Burke |
| Vega King | Karl Burke | Clifford Lee | Doncaster | UK | 13:15 | 25/1 | via trainer follow: Karl Burke |
| Forbidden Fire | Andrew Balding | Oisin Murphy | Doncaster | UK | 13:15 | 11/4 | via trainer follow: Andrew Balding |
| Fast Track (IRE) | Andrew Balding | Tom Marquand | Doncaster | UK | 14:25 | 50/1 | via trainer follow: Andrew Balding |
| Berkshire Sundance (IRE) | Andrew Balding | P J McDonald | Doncaster | UK | 15:00 | 16/1 | via trainer follow: Andrew Balding |
| Ruby Wedding | Andrew Balding | Oisin Murphy | Doncaster | UK | 15:35 | 11/2 | via trainer follow: Andrew Balding |
| Godspeed Girl (GER) | Andrew Balding | P J McDonald | Doncaster | UK | 16:10 | 6/1 | via trainer follow: Andrew Balding (maiden race; sire not obtainable from sources used) |
| She's Got A Way (IRE) | Karl Burke | Ryan Moore | Doncaster | UK | 16:10 | — | via trainer follow: Karl Burke (maiden race; sire not obtainable from sources used) |
| Launch Sequence | Karl Burke | James Doyle | Doncaster | UK | 16:45 | 6/1 | via trainer follow: Karl Burke |
| Beresford Gap | Andrew Balding | Oisin Murphy | Doncaster | UK | 16:45 | 7/1 | via trainer follow: Andrew Balding |
| Scutari | Karl Burke | Shane Gray | Chester | UK | 15:53 | — | via trainer follow: Karl Burke |
| Diamont Katie (IRE) | Karl Burke | Jack Nicholls | Chester | UK | 16:28 | — | via trainer follow: Karl Burke |
| Empress Jingu | Andrew Balding | Callum Hutchinson | Sandown | UK | 15:10 | 5/1 | via trainer follow: Andrew Balding (maiden race; sire not confirmed with confidence — sources gave conflicting details) |
| Allegrino (IRE) | Andrew Balding | Callum Hutchinson | Sandown | UK | 16:57 | — | via trainer follow: Andrew Balding |
| Gesayed | Karl Burke | Billy Loughnane | Sandown | UK | 16:57 | — | via trainer follow: Karl Burke |
| Royal Authority (IRE) | Andrew Balding | William Carver | Salisbury | UK | 15:41 | — | via trainer follow: Andrew Balding (novice race; sire not obtainable from sources used) |
| Relentless Hero | Andrew Balding | William Carver | Salisbury | UK | 18:28 | — | via trainer follow: Andrew Balding |
| Drexel Drive | Mark E. Casse | Luis Saez | Churchill Downs | USA | 19:13 | 10/1 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Greatest Hits | Brad H. Cox | Flavien Prat | Churchill Downs | USA | 19:13 | 7/2 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Getaway Girl | Cherie DeVaux | Tyler Gaffalione | Churchill Downs | USA | 19:13 | 9/2 | via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| Rockie Rockie | Bob Baffert | Flavien Prat | Churchill Downs | USA | 19:13 | 3/1 (also-eligible) | via trainer follow: Bob Baffert (maiden race) \| Sire: Mo Donegal |
| Mischief Bound | Brendan P. Walsh | Tyler Gaffalione | Churchill Downs | USA | 20:50 | 4/1 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Roguishness | Cherie DeVaux | Jose L. Ortiz | Churchill Downs | USA | 22:25 | 4/1 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Wicked Gun | Steven M. Asmussen | Flavien Prat | Churchill Downs | USA | 22:25 | 3/1 | via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| One More Time | Bob Baffert | Rafael Bejarano | Churchill Downs | USA | 22:25 | 5/2 | via trainer follow: Bob Baffert (maiden race) \| Sire: Collected |
| Draw | Riley Mott | Jaime A. Torres | Churchill Downs | USA | 18:16 | 4/1 | via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| Love Divine | Steven M. Asmussen | Keith J. Asmussen | Churchill Downs | USA | 18:16 | 8/1 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Lunar Loop | Rick Hiles | Mario Gutierrez | Churchill Downs | USA | 18:16 | 20/1 | via criterion: top sire/damsire (maiden race) \| Sire: Vekoma |
| Sassy One | William I. Mott | Cristian A. Torres | Churchill Downs | USA | 18:16 | 15/1 | via trainer follow: William Mott; via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Permutation | Chad C. Brown | Tyler Gaffalione | Churchill Downs | USA | 18:16 | 6/1 | via trainer follow: Chad Brown (maiden race) \| Sire: Maxfield |
| Lightning Run | Joe Sharp | Jose L. Ortiz | Churchill Downs | USA | 18:46 | 5/1 | via criterion: top sire/damsire (maiden race) \| Sire: Vekoma |
| Oblivion | Bob Baffert | Florent Geroux | Churchill Downs | USA | 19:49 | 5/1 | via trainer follow: Bob Baffert; via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| Justification | George R. Arnold II | Axel Concepcion | Churchill Downs | USA | 19:49 | 15/1 | via criterion: top sire/damsire (maiden race) \| Sire: Justify |
| Fullback | William I. Mott | Tyler Gaffalione | Churchill Downs | USA | 19:49 | 20/1 | via trainer follow: William Mott; via criterion: top sire/damsire (maiden race) \| Sire: Justify |
| Usha | Bob Baffert | Flavien Prat | Churchill Downs | USA | 20:21 | 5/2 | via trainer follow: Bob Baffert |
| Cash Call | Bob Baffert | Florent Geroux | Churchill Downs | USA | 20:21 | 7/2 | via trainer follow: Bob Baffert |
| Splendora | Bob Baffert | Flavien Prat | Churchill Downs | USA | 21:58 | 3/5 | via trainer follow: Bob Baffert |
| Salahudin | Bob Baffert | Florent Geroux | Churchill Downs | USA | 22:29 | 8/5 | via trainer follow: Bob Baffert |
| Poise | Steven M. Asmussen | Jose L. Ortiz | Churchill Downs | USA | 23:01 | 5/2 | via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| Sweet Reward | William I. Mott | Luis Saez | Churchill Downs | USA | 23:01 | 5/1 | via trainer follow: William Mott (maiden race) \| Sire: Candy Ride (ARG) |
| Zenick | David Fawkes | Diego A. Herrera | Gulfstream Park | USA | 17:52 | 2/1 | via criterion: top sire/damsire (maiden race) \| Sire: Gun Runner |
| Activity | Juan D. Arias | Jonathan Ocasio | Gulfstream Park | USA | 21:28 | 20/1 | via criterion: top sire/damsire (maiden race) \| Sire: Into Mischief |
| Vekoma City | Cam M. Gambolati | Miguel Angel Vasquez | Gulfstream Park | USA | 20:28 | — | via criterion: top sire/damsire (maiden race) \| Sire: Vekoma |
| Berkshire Regal (IRE) | Andrew Balding | Jason Watson | Doncaster | UK | 13:10 | 2/1 | via trainer follow: Andrew Balding (maiden race) \| Sire: Calyx |
| Bombora | Karl Burke | Clifford Lee | Doncaster | UK | 13:10 | — | via trainer follow: Karl Burke (maiden race; sire not obtainable from sources used) |
| Royal Quest (IRE) | Andrew Balding | David Probert | Doncaster | UK | 13:10 | — | via trainer follow: Andrew Balding (maiden race; sire not obtainable from sources used) |
| Gentle Hurricane (IRE) | Andrew Balding | Jason Watson | Doncaster | UK | 13:45 | 12/1 | via trainer follow: Andrew Balding |
| Rosberg | Karl Burke | Clifford Lee | Doncaster | UK | 13:45 | — | via trainer follow: Karl Burke |
| Super Soldier (IRE) | Karl Burke | Jack Nicholls | Doncaster | UK | 14:20 | — | via trainer follow: Karl Burke |
| Never So Brave (IRE) | Andrew Balding | Daniel Tudhope | Doncaster | UK | 14:55 | — | via trainer follow: Andrew Balding |
| Flora Of Bermuda (IRE) | Andrew Balding | Callum Rodriguez | Doncaster | UK | 14:55 | — | via trainer follow: Andrew Balding |
| Galiyan | Andrew Balding | Daniel Tudhope | Doncaster | UK | 15:35 | — | via trainer follow: Andrew Balding |
| Hatteen (IRE) | Andrew Balding | Faleh Bughenaim | Doncaster | UK | 15:35 | — | via trainer follow: Andrew Balding |
| Golden Story (IRE) | Karl Burke | Clifford Lee | Doncaster | UK | 15:35 | — | via trainer follow: Karl Burke |
| Action (IRE) | Aidan O'Brien | Sean Levey | Doncaster | UK | 15:35 | — | via trainer follow: Aidan O'Brien |
| Christmas Day (IRE) | Aidan O'Brien | Ronan Whelan | Doncaster | UK | 15:35 | — | via trainer follow: Aidan O'Brien |
| Amelia Earhart (IRE) | Aidan O'Brien | Tom Marquand | Doncaster | UK | 15:35 | — | via trainer follow: Aidan O'Brien |
| Enceladus (IRE) | Joseph Patrick O'Brien | Billy Loughnane | Doncaster | UK | 15:35 | — | via trainer follow: Joseph O'Brien |
| Highwayman (FR) | Joseph Patrick O'Brien | Saffie Osborne | Doncaster | UK | 15:35 | — | via trainer follow: Joseph O'Brien |
| Mister Winston | Andrew Balding | Jason Watson | Doncaster | UK | 16:15 | — | via trainer follow: Andrew Balding |
| Storm Star | Andrew Balding | David Probert | Doncaster | UK | 16:15 | — | via trainer follow: Andrew Balding |
| Inspired (IRE) | Karl Burke | Jack Nicholls | Doncaster | UK | 16:15 | — | via trainer follow: Karl Burke |
| Thunder Run (IRE) | Karl Burke | Clifford Lee | Doncaster | UK | 16:48 | — | via trainer follow: Karl Burke |
| Old Harrovian | Andrew Balding | Jason Watson | Doncaster | UK | 16:48 | — | via trainer follow: Andrew Balding |
| Plage De Havre | Andrew Balding | Callum Hutchinson | Chester | UK | 13:30 | — | via trainer follow: Andrew Balding |
| Spirit Mixer | Andrew Balding | Alfie Redman | Chester | UK | 14:05 | — | via trainer follow: Andrew Balding |
| Gentle Warrior | Karl Burke | Cam Hardie | Chester | UK | 14:05 | — | via trainer follow: Karl Burke |
| Dunkeld Dreamer | Karl Burke | Finlay Bassett | Chester | UK | 14:05 | — | via trainer follow: Karl Burke |
| Regency Royal (GER) | Andrew Balding | Callum Hutchinson | Chester | UK | 14:40 | — | via trainer follow: Andrew Balding (maiden race; sire not obtainable from sources used) |
| Naval Cop | Andrew Balding | Isobelle Chalmers | Chester | UK | 15:20 | — | via trainer follow: Andrew Balding |
| Tele Red | Karl Burke | Shane Gray | Chester | UK | 16:30 | — | via trainer follow: Karl Burke |
| Crazee Icon | Andrew Balding | Callum Hutchinson | Chester | UK | 17:10 | — | via trainer follow: Andrew Balding |
| Hebridean Nomad | Andrew Balding | Charlie Tucker | Lingfield (AW) | UK | 14:13 | — | via trainer follow: Andrew Balding |
| Greta Tintin | Andrew Balding | William Carver | Bath | UK | 14:30 | — | via trainer follow: Andrew Balding (maiden race; sire not obtainable from sources used) |
| Vegasmile (IRE) | Karl Burke | Sam James | Musselburgh | UK | 16:42 | 4/1 | via trainer follow: Karl Burke (maiden race; sire not obtainable from sources used) |
| Royal Strike (IRE) | Karl Burke | Pierre-Louis Jamin | Musselburgh | UK | 17:20 | — | via trainer follow: Karl Burke |
