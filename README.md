# Maker Weeks

A 25-week STEM curriculum: Scratch → micro:bit → electronics → 3D printing → invention.

Two halves that stay in sync:
- **`weeks.html`** — the page she scans on the iPad. One file, hash-routed (`#week1`, `#week2`…).
- **`print/`** — the printed handbook spreads she writes in.

---

## Blocks

| Block | Weeks | Topic | Accent |
|---|---|---|---|
| 1 | 1–5 | Scratch | `#E8552D` |
| 2 | 6–10 | micro:bit | `#2E8B8B` |
| 3 | 11–15 | Electronics | `#7B4FBF` |
| 4 | 16–20 | Tinkercad + printing | `#C4183C` |
| 5 | 21–25 | Independent invention | `#1F7A3D` |

All 25 weeks are written — every block complete on screen and in print.

---

## Setup

**1. Publish**

Settings → Pages → Source: `main`, folder: `/ (root)`. Live at
`https://confidevop.github.io/maker-weeks/weeks.html`

Progress saves on the device by itself (`localStorage`), and falls back to
memory anywhere storage is blocked. Nothing to switch on.

**2. Make the QR codes**

```
pip install "qrcode[pil]"
cd qr && python3 make_qr.py
```

`week01.png` … `week25.png` are already checked in, pointing at
`confidevop.github.io`. Re-run this only if your Pages URL is different —
edit `BASE` first.

**3. Print the handbook**

```
cd print && pip install weasyprint && python3 make_spreads.py
```

Writes one PDF per block — `block1-weeks2-5.pdf` through
`block5-weeks21-25.pdf` — into `print/`. Week 1 is its own `week01.pdf`.
Half-letter landscape, 1-sided, 0.85in left margin for 3-hole punch.

---

## Adding a week

**Screen** — append one object to the `WEEKS` array in `weeks.html`:

```js
{
  n:26, block:5, title:"Hello, micro:bit",
  sub:"Today you'll make the micro:bit smile at you.",
  open:{label:"Open MakeCode", url:"https://makecode.microbit.org/"},
  steps:["...", "...", "..."],          // 5 max, one line each
  challenge:"...",                       // the remix
  fixes:[["Symptom","Fix"], ...],        // 3 max
  video:"Watch Dad do step 2 (40 sec)"
}
```

`open` is optional — leave it off for a week with no screen (21, 22, 25 do).

**Print** — append the matching dict to `WEEKS` in `print/make_spreads.py` and re-run.

Same content, two shapes. Keep them side by side when editing.

---

## Design rules

- One idea per page. Five steps max, one line each.
- Every instruction starts with a verb: Click, Drag, Press.
- Every week ends in something that visibly *does a thing*.
- iPad is the guide. Laptop is the workbench. Scratch's `when [key] pressed`
  doesn't fire on iPad, so building always happens on the laptop.
- Colour-coded by block — she finds her place by edge colour alone.

## Parts

micro:bits ×2 already on hand. Block 2 also needs micro-USB cables ×2 (data,
not charge-only) and AAA battery holders ×2 — weeks 9 and 10 go untethered.

Block 3 onward is bought once and reused: edge connector breakout ×2, half-size
breadboard ×2, jumper wires + alligator-to-male clips, LEDs + 220Ω resistors,
piezo buzzer ×2, SG90 servo ×2, galvanised nails for a moisture probe.

Block 4 needs a Tinkercad login and printer time. Block 5 needs cardboard,
tape, and people willing to be handed something and told nothing.

## `videos/`

Drop 30–60 second clips of the tricky step here. They're linked from the
"Something's wrong" section on each week's page.
