# Scouted Horses — Mon 16 – Tue 17 Nov 2026

Generated 2026-11-15. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## News

**UK**
- The All-Weather Championship's Season 14 is underway, with both Wolverhampton (Mon) and Southwell (Tue) staging AWC-branded novice and handicap races as part of the build-up to Finals Day at Newcastle next spring.

**Ireland**
- No Flat racing takes place in Ireland on either day this window — the only Irish fixture, Limerick on Tuesday, is entirely National Hunt, so no Irish runners qualify this cycle.

**France**
- A Flat meeting is confirmed for Marseille Pont-de-Vivaux on Monday (8 races, 15:32–19:31 local), but runner-level details weren't accessible from the sources available this cycle — see coverage note below.

**USA**
- None of the main tracks in scope have live racing on either day: Churchill Downs' fall meet runs Wednesday–Sunday only, Del Mar's and Gulfstream's current meets run Friday–Sunday only, Belmont has no Monday/Tuesday cards this week, Aqueduct's live racing has permanently ended (moved to Belmont), and Santa Anita/Keeneland/Saratoga are all between meets.

## Top Tier

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| El Bufalo | not confirmed from sources used | not confirmed from sources used | Wolverhampton (AW) | UK | 18:30 Mon | N/A | via tracked horse: Status "declared", Source horsetracker |
| Without Compromise | not confirmed from sources used | not confirmed from sources used | Southwell (AW) | UK | 18:00 Tue | N/A | via tracked horse: Status "entered", Source horsetracker |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Aloisi Star (IRE) | Karl Burke (K R Burke) | Dougie Costello | Wolverhampton (AW) | UK | 17:00 Mon | N/A | via trainer follow: Karl Burke \| Sire: not confirmed from sources used |
| Ruby Punch | Andrew Balding | William Carver | Wolverhampton (AW) | UK | 17:00 Mon | N/A | via trainer follow: Andrew Balding \| Sire: Oasis Dream |
| Bayside Waltz (IRE) | Andrew Balding | William Carver | Wolverhampton (AW) | UK | 17:30 Mon | N/A | via trainer follow: Andrew Balding \| Sire: not confirmed from sources used |
| Laurel Crown (FR) | Andrew Balding | William Carver | Wolverhampton (AW) | UK | 18:00 Mon | N/A | via trainer follow: Andrew Balding \| Sire: not confirmed from sources used |
| Ted Le Saux | Andrew Balding | Charlie Tucker (7) | Wolverhampton (AW) | UK | 20:00 Mon | N/A | via trainer follow: Andrew Balding |
| Fahidi | Andrew Balding | Charlie Tucker (7) | Southwell (AW) | UK | 17:30 Tue | 7/2 | via trainer follow: Andrew Balding |
| Allaire | Andrew Balding | William Carver | Southwell (AW) | UK | 18:00 Tue | 7/2 | via trainer follow: Andrew Balding \| Sire: not confirmed from sources used |
| Moving Shadow | Karl Burke (K R Burke) | Dougie Costello | Southwell (AW) | UK | 18:30 Tue | 11/2 | via trainer follow: Karl Burke |
| Lehbab Prince | Andrew Balding | William Carver | Southwell (AW) | UK | 20:00 Tue | 8/1 | via trainer follow: Andrew Balding \| Sire: not confirmed from sources used |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding \| Sire: Frankel")._

## Coverage notes / gaps

- **Tracked-horses list: applied after the fact.** The racing-scout subagent had no tool capable of opening `data/tracked/tracked-horses.xlsx` (binary spreadsheet, no shell/Python access). The orchestrating session read it separately with Python and found two tracked horses running in this window — El Bufalo (Wolverhampton, Mon 18:30, status "declared") and Without Compromise (Southwell, Tue 18:00, status "entered") — both added to Top Tier above. Trainer/jockey for both could not be confirmed from the sources checked (no current racecard for either date was found via search), so those fields are blank; odds unavailable too.
- **France — Marseille Pont-de-Vivaux (Mon 16 Nov, Flat, 8 races) confirmed to exist via Racing Post's overview page, but no runner-level data obtained.** Racing Post's overview listed times/race count but no race links or runner names for this meeting. Equidia.fr, PMU.fr, Sky Sports, Timeform, and AWChampionships.co.uk were all unreachable from this session (DNS/network block); At The Races loaded but is JS-rendered and unusable via the fetch tool; France Galop's own dated PDF programme URLs (www7.france-galop.com/pgm/...) 404'd for both dates. Net effect: Notebook/trainer-follow/criteria checks could not be run against this card.
- **No French Flat meeting confirmed for Tuesday 17 Nov** (Racing Post's full meeting list for that date showed only Limerick, Carlisle, Southwell, and an abandoned Leicester — no French fixture).
- **Sire data mostly unavailable.** None of the UK racecard sources used (Racing Post, irishracing.com) show sire/pedigree on the racecard itself, and targeted searches for individual 2yo/lightly-raced horses mostly returned no reliable match (debutants have little web footprint). Only Ruby Punch's sire (Oasis Dream) could be confirmed, via a direct Racing Post horse-profile hit. This also means the top-sire/damsire criterion could not be reliably checked against the wider field in the five novice races on this cycle's cards — it was only checked for horses already qualifying by trainer follow.
- **Wolverhampton odds unavailable.** Racing Post's Wolverhampton card didn't show morning-line/forecast prices, and the alternative source tried (Oddschecker) was unreachable from this session.
- **USA** — confirmed via NYRA, Del Mar, Gulfstream Park, Churchill Downs, Santa Anita, and Keeneland scheduling sources (see News) that no main-scope track races Monday or Tuesday this week; this is a genuine schedule gap, not a research failure, so no USA section appears in the tables.
- UK and Ireland coverage otherwise complete: every meeting on both days (Plumpton, Wolverhampton AW, Limerick, Carlisle, Southwell AW, Leicester-abandoned) was identified and checked; no Notebook horses were running.
