# Scouted Horses — Mon 23–Tue 24 Nov 2026

Generated 2026-11-22. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## News

**UK**
- Godolphin has appointed newly-crowned champion jockey Billy Loughnane as a retained rider alongside William Buick, starting in December — Loughnane already rides several Godolphin/Charlie Appleby juveniles this cycle (e.g. Zajal and Mythical Tale at Wolverhampton Tuesday).

_(Ireland, France and USA omitted — see coverage notes below; nothing notable turned up for Ireland/France given no Flat fixtures found in range, and no main-scope USA track races in this window.)_

## Top Tier

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Kaaranah (IRE) | John Butler | David Egan | Wolverhampton (AW) | UK | 18:30 Mon 23 Nov | N/A | Tracked horse (tracked-horses.xlsx) — 0-75 handicap, Class 5, 1m4f51y. Course winner (C), recent form 511322 |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Angelcatcher (IRE) | K R Burke | Sam James | Newcastle (AW) | UK | 17:15 Mon 23 Nov | N/A | via trainer follow: Karl Burke (K R Burke) — Fillies' Novice Stakes | Sire: Starman (sourced separately from the racecard; not fully confirmed against trainer) |
| Capricious Star (IRE) | K R Burke | Clifford Lee | Wolverhampton (AW) | UK | 17:00 Mon 23 Nov | N/A | via trainer follow: Karl Burke (K R Burke) — nursery handicap. Also appears entered in a Wolverhampton nursery handicap Tue 24 Nov 18:30 (0-85); only one declaration will stand, final target unconfirmed |
| Queen Of Christmas (IRE) | K R Burke | Clifford Lee | Wolverhampton (AW) | UK | 17:30 Mon 23 Nov | N/A | via trainer follow: Karl Burke (K R Burke) — 2yo maiden. Sire not obtainable from sources used |
| The Watcher | K R Burke | Clifford Lee | Wolverhampton (AW) | UK | 20:00 Mon 23 Nov | N/A | via trainer follow: Karl Burke (K R Burke) — 0-85 handicap |
| Manolin | Andrew Balding | Callum Hutchinson | Wolverhampton (AW) | UK | 17:30 Tue 24 Nov | N/A | via trainer follow: Andrew Balding — 2yo maiden (Div I). Sire not obtainable from sources used |
| Haldon Fire | Andrew Balding | Callum Hutchinson | Wolverhampton (AW) | UK | 18:00 Tue 24 Nov | N/A | via trainer follow: Andrew Balding — 2yo maiden (Div II). Sire not obtainable from sources used |
| Silent Strike (IRE) | Andrew Balding | Callum Hutchinson | Wolverhampton (AW) | UK | 19:00 Tue 24 Nov | N/A | via trainer follow: Andrew Balding — 0-95 handicap |
| Nanoscience | Andrew Balding | Callum Hutchinson | Wolverhampton (AW) | UK | 19:30 Tue 24 Nov | N/A | via trainer follow: Andrew Balding — fillies' 0-85 handicap |
| Kashooda | Andrew Balding | Jason Watson | Lingfield (AW) | UK | 11:38 Tue 24 Nov | N/A | via trainer follow: Andrew Balding — 0-75 handicap |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding | Sire: Frankel")._

## Coverage notes / limitations this cycle

- **Tracked-horses file:** `data/tracked/tracked-horses.xlsx` was parsed directly (its underlying XML, since it's a binary spreadsheet the standard Read tool rejects). Of the 12 tracked entries, exactly one falls in this cycle's date range: Kaaranah (IRE) at Wolverhampton, Mon 23 Nov 18:30, status "declared" — added to Top Tier per the fixed rule. No tracked entries fall on Tue 24 Nov.
- **UK Flat racing found:** Newcastle (AW) and Wolverhampton (AW) on Mon 23 Nov; Lingfield (AW) and Wolverhampton (AW) on Tue 24 Nov. These are the only Flat fixtures Racing Post listed for GB on these dates (all other GB meetings in the window — Kempton, Bangor-on-Dee, Huntingdon on the 23rd; Southwell, Tramore, Wincanton (abandoned) on the 24th — are Jumps/NH and were excluded).
- **Ireland:** No Irish Flat (or any) fixtures were found for 23–24 Nov 2026. Dundalk, Ireland's all-weather track, runs a Wednesday/Friday pattern this month (4/11/18/25 Nov Wed, 6/13/20/27 Nov Fri) with nothing on the Monday/Tuesday in scope. horseracingireland.ie could not be reached in this session (network restriction) so this is based on irishracing.com/Racing Post signals rather than the official HRI fixture list directly.
- **France:** No French Flat (Plat) meeting could be confirmed for 23–24 Nov 2026. France Galop's official "toutes les courses" page requires a login redirect that this session can't complete, its Nov/Dec 2026 Plat programme brochure wasn't locatable, and several standard French racing sources (geny.com, zeturf.fr, paris-turf.com, equidia.fr, pmu.fr, turfoo.fr, hippodrome-cotedazur.fr, ressources.anj.fr) are outside this session's allowed network and returned DNS failures. Indirect evidence (Deauville racing only on Saturdays at this time of year; Cagnes-sur-Mer's winter meeting confirmed not starting until 2 Dec 2026) suggests there is in fact no French Flat fixture in this window, but this is not fully verified against an official daily card.
- **USA:** None of the eight in-scope tracks (Santa Anita, Del Mar, Keeneland, Churchill Downs, Belmont, Aqueduct, Saratoga, Gulfstream Park) race on 23 or 24 Nov 2026. Horse Racing Nation's full national card for both dates lists only Mahoning Valley, Parx Racing, Finger Lakes, Zia Park, Mountaineer (plus Delta Downs/Evangeline Downs on the 24th) — all out-of-scope smaller tracks with no stakes day significant enough to invoke the "big race day" exception. Churchill Downs' Fall Meet and Del Mar's Fall Meet both run Wed–Sun only (dark Mon/Tue); Aqueduct's NYRA fall card is also a Thu–Sun pattern around this date; Gulfstream Park's Championship Meet doesn't open until Thanksgiving Day, 26 Nov 2026 — all consistent with no main-track racing in this window.
- **Sire data for maiden/novice runners:** Racing Post's AW racecards (as rendered via this session's fetch tool) generally did not expose sire/breeding information inline, and most of the lightly-raced 2yos in this cycle's maiden races aren't yet indexed elsewhere with pedigree detail. This limited full application of the top-sire/damsire criterion across maiden races this cycle (applied only where sire could be confirmed, e.g. Angelcatcher).
