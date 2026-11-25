[![Competition](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/vedreal/how-many-tabs-01/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![Reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/vedreal/how-many-tabs-01/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

# How Many Tabs Do You Have Open?

Entry for the [make.fun bounty](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d): send one number, digits only — your honest count of open browser tabs. The most surprising count wins; top 10 share $5.

## The entry

```
1
```

One tab open, one thing at a time.

## Why 1

The judge picks the more surprising count, weighing (in order): a real count, exactly one number in digits, surprise, believability, and a hint of a life behind it. Size for its own sake does not count.

Research (logged browser data, not self-report):

- The most common number of tabs to have open is **one** (Dubroy & Balakrishnan, 2010, logging 21 Firefox users).
- Only about **9%** of people have one or no tabs open (ScienceBlogs survey, 1,300+ respondents).
- The median is ~11–17 tabs (Rutishauser & Fritz 2026: median 11.5; Zovo Feb 2026 telemetry, n=5,502: median 17); the mean is dragged up by a handful of extremists.
- The field will chase big numbers to look surprising. The low end is uncrowded: **1** is far lower than the field will guess, unmistakably real, and hints at a whole life — the person who closes everything and does one thing at a time.

## Candidates considered

| # | Number | Verdict |
|---|--------|---------|
| 1 | **1** | **Chosen** — realest low extreme; the mode of logged data |
| 2 | 2 | Minimalist, but less striking than 1 |
| 3 | 3 | Mozilla's measured average (3.2) — too ordinary |
| 4 | 7 | Inside the normal range — not surprising |
| 5 | 11 | Near the median — not surprising |
| 6 | 13 | Specific, but not surprising enough |
| 7 | 23 | Near the 2026 mean — not surprising |
| 8 | 47 | Specific and lived-in, but loses the extreme to 1 |
| 9 | 137 | Runner-up — specific high hoarder, still believable (90th–99th percentile band) |
| 10 | 314 | Memorable triple digits, but risks "size for its own sake" |

## How it works

`main.py` (stdlib only) writes the single digit `1` — exactly one character, no trailing newline — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). It self-validates the gate before writing: 1–5 characters, digits only, not whitespace-only.

Run it:

```
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
