# Scouted Horses — Fri 6 Nov – Sat 7 Nov 2026

Generated 2026-11-05. Covers Flat races in UK, Ireland, France, USA over the stated date range.

## Coverage notes / gaps (read before using this list)

- **`data/tracked/tracked-horses.xlsx`** could not be read by the research sub-agent (no tool capable of opening a binary `.xlsx` file in that step), but was cross-checked separately with a Python/pandas read. Only one row falls in this window — Paso Doble at Fontwell on 6 Nov — and Fontwell is a Jumps/National Hunt track, correctly out of scope for this Flat-only list. So the tracked-horses gap does **not** affect Top Tier this cycle. This tool-access gap has recurred across multiple cycles (see git history) and is worth fixing at the source — e.g. giving the research step a tool that can parse the xlsx, or maintaining a CSV mirror alongside it.
- **UK/Ireland maiden and novice races: sire data was almost entirely unavailable.** Racing Post's and irishracing.com's racecard pages (the only sources that returned runner-level detail — Timeform, At The Races and Sporting Life all failed to render) did not show sire/pedigree for Newcastle, Southwell, Doncaster or Dundalk runners. Follow-up web searches for individual 2yo pedigrees mostly returned unreliable or mismatched results (wrong horse of the same name, broodmare records, etc.) and were not trusted. The one exception used below is Paddy Twomey's **Drive On There** (Dundalk, Sire: Justify), sourced from a single secondary betting-preview snippet rather than a primary racecard — flagged as unconfirmed. So the top-sire/damsire criterion could only be reliably checked for USA maiden/novice races this cycle. Betting odds were also blank on the Newcastle, Southwell and Doncaster racecards fetched (Dundalk did show probable SP, used below).
- **France: no Flat (plat) meeting could be confirmed for 6 or 7 November 2026.** Racing Post's daily meeting index for both dates listed no French course at all (only UK/Ireland/UAE). France Galop's own site has a published flat programme PDF through September–October 2026 but no November/December 2026 edition could be located despite several searches. Treat this as a genuine coverage gap rather than a confirmed absence of racing.
- **USA — Churchill Downs, Belmont Park, Gulfstream Park and Del Mar all card both days; Santa Anita, Aqueduct, Keeneland and Saratoga are dark.** Santa Anita and Aqueduct are confirmed absent from Horse Racing Nation's daily track listing for both 6 and 7 Nov (checked directly, not just absent from search). Keeneland's 2026 fall meet closed in late October (around the Breeders' Cup) and Saratoga's meet ended in September, so neither has racing in this window.
- **2nd-career-start and class-drop-from-Group/Graded criteria could not be applied.** None of the sources used (Racing Post, irishracing.com, Horse Racing Nation) surfaced number of career starts or prior-race class/finish for individual runners, so criteria #2 and #3 in `criteria.md` weren't checked this cycle. As a result every qualifying horse below landed in **The Rest** (trainer-follow and top-sire/damsire are both The Rest-tier criteria) — this may understate Top Tier rather than reflect a genuinely quiet cycle. (The tracked-horses.xlsx gap noted above, by contrast, has been confirmed not to affect Top Tier this cycle.)
- **Belmont Park's Saturday 7 Nov card lists several named stakes (Pumpkin Pie S., Dwyer S., Carle Place S., Mother Goose S.)** that are traditionally run at other points in the NYRA season (e.g. Mother Goose and Dwyer are normally June/July races). This is simply what Horse Racing Nation's entries page returned — flagging it as worth double-checking against NYRA's official stakes calendar rather than treating it as certain.
- Everything else below was researched via Racing Post and irishracing.com individual racecard pages (UK/Ireland) and Horse Racing Nation dated entries pages (USA).

## News

**UK**
- Doncaster's Saturday card closes out the 2026 British turf Flat season with the Virgin Bet November Handicap (15:25, 23 runners) as the finale, alongside two well-filled Listed races — the Wentworth Stakes (21 runners) and the Irish EBF Gillies Fillies' Stakes (17 runners) — both drawing runners from Aidan O'Brien, Andrew Balding and Karl Burke's yards.

**Ireland**
- Dundalk's Friday night card is unusually stacked with followed trainers: Aidan O'Brien, Joseph O'Brien, Ger Lyons, Paddy Twomey and Karl Burke all have runners in the Listed Irish Stallion Farms EBF Cooley Stakes (18:45) alone, and Joseph O'Brien/Paddy Twomey/Ger Lyons also clash directly in the two juvenile maidens on the same card.

**USA**
- Churchill Downs' Saturday card carries two $300,000 features — the River City Stakes (turf) and the Bet on Sunshine Stakes (dirt) — with Bob Baffert sending Greenwich Village into the latter.

_(France omitted — no meeting could be confirmed; see coverage notes above.)_

## Top Tier

_(No Notebook horses or Top-Tier-criterion matches found this cycle. Tracked horses were cross-checked directly and don't apply to this window (see coverage notes). The 2nd-start/class-drop criteria remain unverifiable from the sources used, so this list may still understate Top Tier.)_

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## The Rest

| Horse | Trainer | Jockey | Track | Country | Race Time (Irish) | Odds | Notes |
|---|---|---|---|---|---|---|---|
| Black Chiffon | Andrew Balding | Callum Hutchinson | Newcastle (AW) | UK | Fri 14:53 | N/A | via trainer follow: Andrew Balding |
| Moonlight Warrior (IRE) | Andrew Balding | Marco Ghiani | Newcastle (AW) | UK | Fri 14:53 | N/A | via trainer follow: Andrew Balding |
| Capricious Star (IRE) | K R Burke (Karl Burke) | Pierre-Louis Jamin | Newcastle (AW) | UK | Fri 17:00 | N/A | via trainer follow: Karl Burke — maiden; sire not available from sources used |
| Mobilizing (IRE) | K R Burke (Karl Burke) | Saffie James | Newcastle (AW) | UK | Fri 17:00 | N/A | via trainer follow: Karl Burke — maiden; sire not available from sources used |
| Ellusive Butterfly | K R Burke (Karl Burke) | Clifford Lee | Doncaster | UK | Sat 14:10 | N/A | via trainer follow: Karl Burke — Wentworth S. (Listed) |
| Lam Yai | K R Burke (Karl Burke) | Sam James | Doncaster | UK | Sat 14:10 | N/A | via trainer follow: Karl Burke — Wentworth S. (Listed) |
| Copacabana Sands | Andrew Balding | Oisin Murphy | Doncaster | UK | Sat 14:10 | N/A | via trainer follow: Andrew Balding — Wentworth S. (Listed) |
| Zgharta | Andrew Balding | Oisin Murphy | Doncaster | UK | Sat 14:45 | N/A | via trainer follow: Andrew Balding — Gillies Fillies' S. (Listed) |
| Garden Party | A P O'Brien (Aidan O'Brien) | Oisin Orr | Doncaster | UK | Sat 14:45 | N/A | via trainer follow: Aidan O'Brien — Gillies Fillies' S. (Listed) |
| Moments Of Joy | A P O'Brien (Aidan O'Brien) | Ryan Moore | Doncaster | UK | Sat 14:45 | N/A | via trainer follow: Aidan O'Brien — Gillies Fillies' S. (Listed) |
| Together Now | A P O'Brien (Aidan O'Brien) | Wayne Lordan | Doncaster | UK | Sat 14:45 | N/A | via trainer follow: Aidan O'Brien — Gillies Fillies' S. (Listed) |
| Prosperity | K R Burke (Karl Burke) | Clifford Lee | Doncaster | UK | Sat 14:45 | N/A | via trainer follow: Karl Burke — Gillies Fillies' S. (Listed) |
| Abrouq | Andrew Balding | P J McDonald | Southwell (AW) | UK | Sat 14:40 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Berkshire Tango (IRE) | Andrew Balding | Rob Hornby | Southwell (AW) | UK | Sat 14:40 | N/A | via trainer follow: Andrew Balding — novice; sire not available from sources used |
| Otsana | P Twomey (Paddy Twomey) | W J Lee | Dundalk (AW) | Ireland | Fri 17:15 | 66/1 | via trainer follow: Paddy Twomey — maiden; sire not available from sources used |
| Corsican Night | Joseph Patrick O'Brien | D P McDonogh | Dundalk (AW) | Ireland | Fri 17:45 | 11/2 | via trainer follow: Joseph O'Brien — maiden; sire not available from sources used |
| Ladies Gossip | Joseph Patrick O'Brien | J M Sheridan | Dundalk (AW) | Ireland | Fri 17:45 | 5/2 | via trainer follow: Joseph O'Brien — maiden; sire not available from sources used |
| Sensational Filly | P Twomey (Paddy Twomey) | W J Lee | Dundalk (AW) | Ireland | Fri 17:45 | 7/4 | via trainer follow: Paddy Twomey — maiden; sire not available from sources used |
| Suzie Songs | G M Lyons (Ger Lyons) | George F Carroll | Dundalk (AW) | Ireland | Fri 18:45 | 7/2 | via trainer follow: Ger Lyons — Cooley Fillies' S. (Listed) |
| Prevalence | G M Lyons (Ger Lyons) | Colin T Keane | Dundalk (AW) | Ireland | Fri 18:45 | 8/1 | via trainer follow: Ger Lyons — Cooley Fillies' S. (Listed) |
| Dancing Saxon | Joseph Patrick O'Brien | D P McDonogh | Dundalk (AW) | Ireland | Fri 18:45 | 10/3 | via trainer follow: Joseph O'Brien — Cooley Fillies' S. (Listed) |
| Duchess Of Kenli | Joseph Patrick O'Brien | J M Sheridan | Dundalk (AW) | Ireland | Fri 18:45 | 33/1 | via trainer follow: Joseph O'Brien — Cooley Fillies' S. (Listed) |
| Leading Dancer | K R Burke (Karl Burke) | Clifford Lee | Dundalk (AW) | Ireland | Fri 18:45 | 9/2 | via trainer follow: Karl Burke — Cooley Fillies' S. (Listed) |
| White Sand Beach | A P O'Brien (Aidan O'Brien) | Wayne M Lordan | Dundalk (AW) | Ireland | Fri 18:45 | 20/1 | via trainer follow: Aidan O'Brien — Cooley Fillies' S. (Listed) |
| On Just Terms | Joseph Patrick O'Brien | J M Sheridan | Dundalk (AW) | Ireland | Fri 19:15 | 11/10 | via trainer follow: Joseph O'Brien — maiden; sire not available from sources used |
| Warrior Of Siam | Joseph Patrick O'Brien | D P McDonogh | Dundalk (AW) | Ireland | Fri 19:15 | 10/1 | via trainer follow: Joseph O'Brien — maiden; sire not available from sources used |
| Drive On There | P Twomey (Paddy Twomey) | W J Lee | Dundalk (AW) | Ireland | Fri 19:15 | 4/1 | via trainer follow: Paddy Twomey — maiden; Sire: Justify (unconfirmed — single secondary source, not shown on primary racecard) |
| Naval Gazer | G M Lyons (Ger Lyons) | Colin T Keane | Dundalk (AW) | Ireland | Fri 19:15 | 10/1 | via trainer follow: Ger Lyons — maiden; sire not available from sources used |
| Daler | G M Lyons (Ger Lyons) | Colin T Keane | Dundalk (AW) | Ireland | Fri 19:45 | 15/8 | via trainer follow: Ger Lyons |
| Sweet Reward | William I. Mott | Junior Alvarado | Churchill Downs | USA | Fri 18:29 | 9/2 | via trainer follow: William Mott — maiden; Sire: Candy Ride (ARG) |
| Lowcountry Promise | Peter Eurton | Luis Saez | Churchill Downs | USA | Fri 18:00 | 6/1 | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Sutura | Jack Sisterson | Tyler Gaffalione | Churchill Downs | USA | Fri 18:29 | 5/2 | via criterion: top sire/damsire (Vekoma) — maiden; Sire: Vekoma |
| Diversification | Chad C. Brown | Tyler Gaffalione | Churchill Downs | USA | Sat 18:29 | 3/1 | via trainer follow: Chad Brown — maiden claiming; Sire: Quality Road |
| Viaggio | Mark E. Casse | Florent Geroux | Churchill Downs | USA | Sat 21:55 | 8/1 | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Justify Joey | Brad H. Cox | Tyler Gaffalione | Churchill Downs | USA | Sat 22:55 | 6/1 | via criterion: top sire/damsire (Justify) — maiden; Sire: Justify |
| Greenwich Village | Bob Baffert | Jose L. Ortiz | Churchill Downs | USA | Sat 22:25 | 9/2 | via trainer follow: Bob Baffert — Bet on Sunshine S. |
| Bletchley | Chad C. Brown | Flavien Prat | Belmont Park | USA | Fri 17:40 | 8/5 | via trainer follow: Chad Brown \| via criterion: top sire/damsire (Gun Runner) — maiden; Sire: Gun Runner |
| Le Patron | William I. Mott | Jose Lezcano | Belmont Park | USA | Fri 17:40 | 12/1 | via trainer follow: William Mott — maiden; Sire: American Pharoah |
| Ogugua | Rudy R. Rodriguez | Dalila A. Rivera | Belmont Park | USA | Fri 18:40 | 8/1 | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Kotlikoff | William I. Mott | Jose Lezcano | Belmont Park | USA | Fri 19:10 | 5/1 | via trainer follow: William Mott — maiden; Sire: Tacitus |
| Kid's Khanclusion | Chad C. Brown | Flavien Prat | Belmont Park | USA | Fri 19:10 | 5/2 | via trainer follow: Chad Brown — maiden; Sire: Medaglia d'Oro |
| Big Frosty | Todd A. Pletcher | John R. Velazquez | Belmont Park | USA | Fri 19:10 | 3/1 | via trainer follow: Todd Pletcher — maiden; Sire: Big Brown |
| Zipline | Mark E. Casse | Dylan Davis | Belmont Park | USA | Fri 20:12 | 6/1 | via criterion: top sire/damsire (Vekoma) — maiden optional claiming; Sire: Vekoma |
| Classicist | Todd A. Pletcher | John R. Velazquez | Belmont Park | USA | Fri 20:43 | 6/1 | via trainer follow: Todd Pletcher |
| Tuscan Sky | Todd A. Pletcher | Flavien Prat | Belmont Park | USA | Fri 20:43 | 9/2 | via trainer follow: Todd Pletcher |
| Market Perception | Chad C. Brown | Flavien Prat | Belmont Park | USA | Sat 17:10 | N/A | via trainer follow: Chad Brown — maiden optional claiming; Sire: Olympiad |
| Instant Stardom | Rudy R. Rodriguez | Pedro Pena | Belmont Park | USA | Sat 17:10 | N/A | via criterion: top sire/damsire (Into Mischief) — maiden optional claiming; Sire: Into Mischief |
| Beauty Reigns | William I. Mott | Junior Alvarado | Belmont Park | USA | Sat 19:10 | N/A | via trainer follow: William Mott — Pumpkin Pie S. |
| Stimulate | William I. Mott | Junior Alvarado | Belmont Park | USA | Sat 20:12 | N/A | via trainer follow: William Mott — Dwyer S. |
| Sea Strike | Chad C. Brown | Flavien Prat | Belmont Park | USA | Sat 20:12 | N/A | via trainer follow: Chad Brown — Dwyer S. |
| Ted Noffey | Todd A. Pletcher | John R. Velazquez | Belmont Park | USA | Sat 20:12 | N/A | via trainer follow: Todd Pletcher — Dwyer S. |
| Answered Prayers | William I. Mott | Junior Alvarado | Belmont Park | USA | Sat 20:43 | N/A | via trainer follow: William Mott — Mother Goose S. |
| Ati Girl | William I. Mott | John R. Velazquez | Belmont Park | USA | Sat 20:43 | N/A | via trainer follow: William Mott — Mother Goose S. |
| Major Bourbon | Mark A. Hennig | Reylu Gutierrez | Belmont Park | USA | Sat 21:14 | N/A | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Pax Mundi | Jose Francisco D'Angelo | Yolber Torres | Gulfstream Park | USA | Fri 19:00 | 7/5 | via criterion: top sire/damsire (Gun Runner) — maiden; Sire: Gun Runner |
| Wild Night | Todd A. Pletcher | Miguel Angel Vasquez | Gulfstream Park | USA | Fri 20:36 | 9/2 | via trainer follow: Todd Pletcher — maiden; Sire: Liam's Map |
| Just a Girl | Todd A. Pletcher | Diego A. Herrera | Gulfstream Park | USA | Fri 20:36 | 8/5 | via trainer follow: Todd Pletcher \| via criterion: top sire/damsire (Justify) — maiden; Sire: Justify |
| Siena Belle | J. Kent Sweezey | Jose E. Morelos | Gulfstream Park | USA | Sat 19:00 | N/A | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Four Amigos | Alfredo P. Marquez | Kyle Frey | Del Mar | USA | Fri 21:32 | 12/1 | via criterion: top sire/damsire (Vekoma) — maiden claiming; Sire: Vekoma |
| Cheever | Mark Glatt | Joel Rosario | Del Mar | USA | Sat 22:00 | N/A | via criterion: top sire/damsire (Into Mischief) — maiden; Sire: Into Mischief |
| Duntov | Bob Baffert | Juan J. Hernandez | Del Mar | USA | Sat 22:00 | N/A | via trainer follow: Bob Baffert — maiden; Sire: Maxfield |
| Huber | Bob Baffert | Emisael Jaramillo | Del Mar | USA | Sat 22:00 | N/A | via trainer follow: Bob Baffert — maiden; Sire: Omaha Beach |
| Deluge | Bob Baffert | Juan J. Hernandez | Del Mar | USA | Sat 22:30 | N/A | via trainer follow: Bob Baffert — allowance optional claiming |

_Notes column is filled only when the horse is in the Notebook (`data/notebook/horses.csv`) — carries that entry's note. Otherwise it names which criterion/trainer-follow qualified the horse (e.g. "via trainer follow: <name>", "via criterion: 2nd-start top trainer", "via criterion: top sire/damsire"). For maiden/novice races, the sire is appended too (e.g. "via trainer follow: Andrew Balding | Sire: Frankel")._

_UK and Irish race times shown are already local/Irish time (both on GMT, UTC+0, in November). USA race times are converted assuming US Eastern tracks (Churchill Downs, Belmont Park, Gulfstream Park) are on EST (UTC-5) and US Pacific tracks (Del Mar) are on PST (UTC-8) — i.e. Irish time = US Eastern + 5 hours, or US Pacific + 8 hours, for this cycle (both zones having already left daylight saving time by 6–7 Nov)._
