# Scouting criteria

This file grows as we develop and refine criteria/systems together. When a new rule is added, note roughly when/why it came in so we can track what's working.

## Tiering in the Scouted Horses output

Every qualifying horse is placed in one of two lists in the output/email: **Top Tier** or **The Rest**. Each criterion below is tagged with which tier it produces. Fixed rule (not a criterion, always applies): **Notebook horses are always Top Tier.** Qualifying purely via a followed trainer (no other criterion met) is The Rest, unless a specific criterion says otherwise.

## Active criteria

### 1. Top sire/damsire in maiden or novice races (added 2026-08-11) — Tier: The Rest
In a maiden or novice race, a horse qualifies if its **sire** or **damsire** appears on the top sire list (`data/criteria/top-sires.csv`) — first-time/lightly-raced form tells you little, so pedigree from a proven sire line is the signal here. Applies to maiden/novice races only, any of the four jurisdictions. The top sire list starts with: Wootton Bassett, Dubawi, Frankel, Sea the Stars, Duke of Marmalade, Montjeu, Justify, Into Mischief, Gun Runner, Vekoma, Lope de Vega, Kingman, No Nay Never — and grows over time as the user adds sires.

### 2. 2nd career start for a followed trainer (added 2026-08-11) — Tier: Top Tier
A horse qualifies if it's having its **2nd race ever** (career start #2) and is trained by a trainer on the follow list (`data/notebook/trainers.csv`). A strong trainer's move with a horse this lightly raced is a stronger signal than the trainer follow alone, so this goes straight to Top Tier rather than The Rest.

### 3. Dropping in class off a good group/graded run (added 2026-08-11) — Tier: Top Tier
A horse qualifies if its **last race** was a Group/Grade 1, 2, or 3 race and it finished in the **top 5**, and its **current race** is a handicap or a Listed race (a stakes race, but not Group/Graded). Class relief off a competitive run at a much higher level is a strong signal, so this is Top Tier.

### 4. Top trainer dropping from MSW to maiden claimer — USA only (added 2026-08-11) — Tier: Top Tier
USA racing only. A horse qualifies if it's trained by a trainer on the follow list (`data/notebook/trainers.csv`) and its **last race** was a Maiden Special Weight (MSW), and its **current race** is a Maiden Claimer (maiden claiming).

## Retired / didn't work out

_(none yet)_
