# Scouted Horses — Sun 22 Nov 2026

Generated 2026-11-21. Covers Flat races in UK, Ireland, France, USA on Sunday 22 November 2026.

## Coverage notes (read before relying on this list)

- **`data/tracked/tracked-horses.xlsx` — re-checked and resolved.** The initial research pass couldn't open the `.xlsx` file; it has since been read directly (13 rows). **No tracked horse has a race on 22 Nov 2026** — all listed races fall on other dates (15–29 Nov, 5 Dec) and at other tracks (Navan, Cheltenham, Wolverhampton, Southwell, Newcastle, Punchestown, Newbury, Fairyhouse, Aintree — mostly Jumps venues anyway). So this gap did not actually cost any Top Tier horse for this date.
- **UK — Lingfield (AW):** confirmed via Racing Post as the only Flat fixture in Britain on 22 Nov (9 races, 11:25–15:25, Polytrack). Runner-level declarations were **independently re-checked and confirmed not yet published** as of Saturday 21 Nov afternoon (UK declarations typically come out ~24h ahead, i.e. Saturday evening/night for Sunday racing) — this is a timing gap, not a tooling failure. Re-running this lookup Saturday evening or Sunday morning would likely find the card.
- **Ireland:** no Flat fixtures today. Racing Post's full GB+IRE racecards index for 22 Nov lists only Punchestown and Cork, both jumps (out of scope) — confirmed absence, not a data gap.
- **France — Fontainebleau, Toulouse, Nancy (flat portion):** all three confirmed via france-galop.com's own "tomorrow" programme (race times, names, distances, categories). Partants were **independently re-checked and confirmed not yet published** ("contenu de la réunion sera prochainement disponible") — French partants are also typically released the evening before, so this is the same timing issue as Lingfield, not a tooling failure.
- **USA:** Churchill Downs, Belmont Park, Del Mar and Gulfstream Park (the four in-scope main tracks racing today) were fully retrieved via Horse Racing Nation with runner/trainer/jockey/sire/odds detail, and checked in full. Santa Anita, Keeneland and Saratoga are not racing today (confirmed via the day's full US card list); Aqueduct is not racing today either — Belmont Park is still the active NYRA fall-meet track in its place.
- Net effect: everything below is sourced from USA racing only. UK and France declarations for this date simply weren't out yet at the time of research (normal for a Saturday-afternoon cycle looking at next-day racing) — don't read the absence of UK/France horses as "nothing qualified" there; it means "not yet declared." Ireland has no Flat fixture today, confirmed. The tracked-horses gap has been resolved and cost nothing (see above).

## News

**France**
- Fontainebleau stages the Listed Grand Prix de Fontainebleau (2,000m) as today's feature on a heavy-ground card; Toulouse's evening card includes the Group 3 Prix Ourour for three-year-olds.

**USA**
- Belmont Park hosts the Grade 3 Manila Stakes (1m, turf, 3yo) as its feature; per NYRA's preview, Kentucky homebred Print is trying to step up in class against Grade 2-placed runners Let's Be Frank and McCready.

_(UK and Ireland omitted — see coverage notes above: no Irish Flat fixture today, and no usable news/card detail retrieved for Lingfield.)_

## Top Tier

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| _none_ | | | | | | | No Notebook horses found running; tracked-horses list could not be read this cycle (see coverage notes); no Top Tier criterion could be confirmed from entries-only data (criteria needing past-start/result history weren't verifiable from today's sources). |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Wauwinet | Gregory D. Foley | Edgar Morales | Churchill Downs | USA | 19:27 | 20/1 | via criterion: top sire/damsire \| Sire: Into Mischief |
| Theorize | H. James Bond | Edgard J. Zayas | Belmont Park | USA | 19:10 | 9/2 | via criterion: top sire/damsire \| Sire: Into Mischief |
| My Vekoma | George Weaver | Dylan Davis | Belmont Park | USA | 18:40 | 5/1 | via criterion: top sire/damsire \| Sire: Vekoma |
| Camber | Bruno Tessore | Jorge Ruiz | Belmont Park | USA | 19:10 | 12/1 | via criterion: top sire/damsire \| Sire: Gun Runner |
| Guns of Roses | Saffie A. Joseph, Jr. | Micah J. Husbands | Gulfstream Park | USA | 18:22 | 8/5 | via criterion: top sire/damsire \| Sire: Gun Runner |
| Rahab | Richard E. Mandella | Joel Rosario | Del Mar | USA | 22:02 | 5/1 | via criterion: top sire/damsire \| Sire: Into Mischief |
| Dear Diary | Richard E. Mandella | Mike E. Smith | Del Mar | USA | 22:02 | 4/1 | via criterion: top sire/damsire \| Sire: Into Mischief |
| Bunners | Bob Baffert | Emisael Jaramillo | Del Mar | USA | 22:02 | 5/2 | via trainer follow: Bob Baffert \| Sire: Girvin |
| Youthful | Todd A. Pletcher | John R. Velazquez | Belmont Park | USA | 19:10 | 8/1 | via trainer follow: Todd Pletcher \| Sire: Practical Joke |
| Turn N Burn | Chad C. Brown | Flavien Prat | Belmont Park | USA | 17:40 | 7/5 | via trainer follow: Chad Brown \| Sire: Maclean's Music |
| Hedge Book | Chad C. Brown | Flavien Prat | Belmont Park | USA | 19:10 | 4/1 | via trainer follow: Chad Brown \| Sire: Practical Joke |
| Material Girl | Chad C. Brown | Manuel Franco | Belmont Park | USA | 19:41 | 7/2 | via trainer follow: Chad Brown |
| Ellesmere Island | Chad C. Brown | Jose L. Ortiz | Churchill Downs | USA | 22:24 | 6/1 | via trainer follow: Chad Brown |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding | Sire: Frankel"). All races above are Maiden Special Weight except Material Girl (NY Stallion Staten Island S., a state-bred stakes) and Ellesmere Island (allowance) — sire not appended for those two since they aren't maiden/novice races._

_Criteria #2 (2nd career start for a followed trainer) and #4 (MSW-to-maiden-claimer drop) require each horse's past-start history; today's sources were entries-only (no accessible past-performance/chart data — Equibase blocks automated access and DRF's entries are paywalled), so these two criteria could not be reliably checked. Criterion #4 is moot regardless today: none of the followed trainers have a runner in a maiden claiming race. Criterion #3 (class drop off a Group/Grade top-5) likewise needs last-race result history not available from entries alone, so it wasn't checked._
