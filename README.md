# The World in One Day — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/abtravels/news-2026-11-26/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/abtravels/news-2026-11-26/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

A newspaper front page summing up the world's news of Thursday 26 November 2026 in one image. Every story below happened, or was first reported, on that day (Reuters, verified 26 November 2026).

## The six stories

1. **Seoul hikes rates again** — the Bank of Korea raises its base rate a quarter point to 3.25%, resuming tightening after an October pause as a chip-led export boom keeps inflation and house prices high.
2. **Asia shares bounce as Wall Street steadies** — Nikkei +1.6%, Korea +1.9% in a holiday-thinned session; US markets shut for Thanksgiving.
3. **Vietnam races the US to finish a trade deal** — Hanoi says it is working with Washington to complete a trade deal as soon as possible, hours after the US proposed new tariffs on 14 partners.
4. **BOJ's Tamura: be ready to hike faster** — Bank of Japan board member Naoki Tamura says the bank must "respond swiftly" to signs of an inflation overshoot, including faster rate rises.
5. **Mine rescue resumes in Indonesia** — search teams return to a flooded illegal gold mine in West Java: 13 dead, 13 still trapped 100 metres down.
6. **Uber names Rakesh Ranjan** to lead India and South Asia, in the job from 4 January 2027.

## Run it

`main.ts` (Node 22, standard library only) only copies the pre-rendered `entry.png` into the output directory — it never runs Python or draws anything at grade time:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The image itself is drawn from scratch by `draw.py` (Pillow) and shipped here as `entry.png` (1024×1024, under 1 MiB).
