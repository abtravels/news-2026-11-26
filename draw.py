#!/usr/bin/env python3
"""Draw the 26 November 2026 world-news front page (1024x1024 PNG).

Fresh artwork for make.fun news-image-20261126. All six stories were
first reported on Thursday 26 November 2026 (Reuters, verified
2026-11-26). No photos: every panel is drawn from scratch with Pillow.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
BLUE = (23, 63, 120)
TEAL = (14, 110, 105)
GOLD = (176, 124, 22)
GREY = (90, 86, 78)
LINE = (200, 192, 172)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    """Wrap text to fit pixel width, returning a list of lines."""
    lines = []
    for para in text.split("\n"):
        words, cur = para.split(), ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= width:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def block(draw, x, y, w, text, fnt, fill=INK, leading=None, align="left"):
    leading = leading or int(fnt.size * 1.28)
    lines = wrap(draw, text, fnt, w)
    for ln in lines:
        if align == "center":
            tw = draw.textlength(ln, font=fnt)
            draw.text((x + (w - tw) / 2, y), ln, font=fnt, fill=fill)
        else:
            draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x, y, w, weight=2, fill=INK):
    draw.rectangle([x, y, x + w, y + weight - 1], fill=fill)


def kicker(draw, x, y, label, color):
    f = font(SANS_B, 17)
    tw = draw.textlength(label, font=f) + 16
    draw.rectangle([x, y, x + tw, y + 26], fill=color)
    draw.text((x + 8, y + 3), label, font=f, fill=(255, 255, 255))
    return tw


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=3)

# ---------------- Masthead ----------------
y = 20
d.text((512, y), "THE WORLD IN ONE DAY", font=font(SERIF_B, 54),
       fill=INK, anchor="ma")
y += 66
rule(d, 40, y, W - 80, 3)
y += 10
d.text((512, y), "THURSDAY  26  NOVEMBER  2026", font=font(SANS_B, 30),
       fill=RED, anchor="ma")
y += 40
d.text((512, y), "Six stories from one day around the world",
       font=font(SERIF, 22), fill=GREY, anchor="ma")
y += 30
rule(d, 40, y, W - 80, 3)
y += 12

# ---------------- Lead story: Bank of Korea ----------------
lx, ly, lw = 40, y, W - 80
kicker(d, lx, ly, "SEOUL  ·  LEAD", RED)
d.text((lx, ly + 36), "Seoul hikes rates again",
       font=font(SERIF_B, 40), fill=INK)
d.text((lx, ly + 88),
       "Bank of Korea lifts its base rate a quarter point to 3.25%,",
       font=font(SERIF, 22), fill=INK)
d.text((lx, ly + 116),
       "resuming tightening after an October pause as a chip-led",
       font=font(SERIF, 22), fill=INK)
d.text((lx, ly + 144),
       "export boom keeps inflation and house prices high.",
       font=font(SERIF, 22), fill=INK)
# Mini rate chart on the right of the lead
cx, cy, cw, ch = 700, ly + 34, 244, 130
d.rectangle([cx, cy, cx + cw, cy + ch], outline=INK, width=2, fill=(255, 255, 255))
bars = [("JUL", 2.75, 34), ("AUG", 3.00, 52), ("OCT", 3.00, 52), ("NOV", 3.25, 78)]
bw = 44
for i, (lab, val, bh) in enumerate(bars):
    bx = cx + 14 + i * 58
    col = RED if i == 3 else BLUE
    d.rectangle([bx, cy + ch - 22 - bh, bx + bw, cy + ch - 22], fill=col)
    d.text((bx + bw / 2, cy + ch - 20), lab, font=font(SANS_B, 12),
           fill=INK, anchor="ma")
d.text((cx + cw / 2, cy + 6), "BASE RATE  3.25%", font=font(SANS_B, 15),
       fill=RED, anchor="ma")
lead_bottom = ly + 170
rule(d, 40, lead_bottom, W - 80, 2)
y = lead_bottom + 14

# ---------------- Row: markets + Vietnam (two columns) ----------------
col_w = (W - 80 - 24) // 2
# Story 2 — Asia markets
x = 40
kicker(d, x, y, "MARKETS", BLUE)
yy = block(d, x, y + 38, col_w,
           "Asia shares bounce as Wall Street steadies",
           font(SERIF_B, 27), leading=34)
yy = block(d, x, yy + 6, col_w,
           "Nikkei +1.6%, Korea +1.9% in a holiday-thinned session. "
           "US markets shut for Thanksgiving.",
           font(SERIF, 19), leading=25)
# tiny up-arrow chart
ay = yy + 12
pts = [(x, ay + 46), (x + 90, ay + 40), (x + 180, ay + 44),
       (x + 270, ay + 22), (x + 360, ay + 12), (x + 440, ay + 2)]
d.line(pts, fill=TEAL, width=5)
d.polygon([(x + 440, ay + 2), (x + 424, ay + 2), (x + 440, ay + 18)],
          fill=TEAL)
d.text((x, ay + 54), "NIKKEI +1.6%   ·   KOSPI +1.9%   ·   S&P FUTURES +0.5%",
       font=font(SANS_B, 15), fill=TEAL)

# Story 3 — Vietnam
x2 = 40 + col_w + 24
kicker(d, x2, y, "HANOI", TEAL)
yy2 = block(d, x2, y + 38, col_w,
            "Vietnam races US to finish trade deal",
            font(SERIF_B, 27), leading=34)
yy2 = block(d, x2, yy2 + 6, col_w,
            "Hanoi says it is working with Washington to complete a "
            "trade deal as soon as possible, hours after the US proposed "
            "new tariffs on 14 partners.",
            font(SERIF, 19), leading=25)
d.text((x2, yy2 + 10), "“AS SOON AS POSSIBLE” — TRADE MINISTRY",
       font=font(SANS_B, 15), fill=TEAL)
row2_bottom = max(ay + 76, yy2 + 40)
rule(d, 40, row2_bottom, W - 80, 2)
y = row2_bottom + 14

# ---------------- Row: BOJ + Indonesia mine (two columns) ----------------
x = 40
kicker(d, x, y, "TOKYO", GOLD)
yy = block(d, x, y + 38, col_w,
           "BOJ's Tamura: be ready to hike faster",
           font(SERIF_B, 27), leading=34)
yy = block(d, x, yy + 6, col_w,
           "Board member Naoki Tamura says the Bank of Japan must "
           "“respond swiftly” to signs of an inflation overshoot, "
           "including faster rate rises.",
           font(SERIF, 19), leading=25)

x2 = 40 + col_w + 24
kicker(d, x2, y, "BOGOR, INDONESIA", RED)
yy2 = block(d, x2, y + 38, col_w,
            "Mine rescue resumes: 13 dead, 13 trapped",
            font(SERIF_B, 27), leading=34)
yy2 = block(d, x2, yy2 + 6, col_w,
            "Search teams return to a flooded illegal gold mine in West "
            "Java. Twenty-six workers were trapped 100 metres down "
            "when heavy rain inundated the shaft on Monday.",
            font(SERIF, 19), leading=25)
row3_bottom = max(yy, yy2) + 4
rule(d, 40, row3_bottom, W - 80, 2)
y = row3_bottom + 14

# ---------------- Bottom strip: Uber ----------------
kicker(d, 40, y, "BUSINESS", BLUE)
y = block(d, 40, y + 38, W - 80,
          "Uber names Rakesh Ranjan to lead India and South Asia "
          "from 4 January 2027.",
          font(SERIF_B, 20), leading=27)
y += 8
rule(d, 40, y, W - 80, 3)

# ---------------- Footer ----------------
fy = y + 10
d.text((512, fy),
       "All six events first reported THURSDAY 26 NOVEMBER 2026  ·  Sources: Reuters",
       font=font(SANS_B, 16), fill=INK, anchor="ma")

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
