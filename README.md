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

---

## Setup

**1. Publish**

Settings → Pages → Source: `main`, folder: `/ (root)`. Live at
`https://YOURNAME.github.io/maker-weeks/weeks.html`

**2. Turn on saving**

`weeks.html` ships with in-memory state so it previews cleanly. Once hosted,
apply the change described in the comment at the bottom of the file — two lines,
swaps it to `localStorage`.

**3. Make the QR codes**

```
pip install "qrcode[pil]"
cd qr && python3 make_qr.py      # edit BASE first
```

**4. Print the handbook**

```
cd print && pip install weasyprint && python3 make_spreads.py
```

Writes one PDF per block — `block1-weeks2-5.pdf`, `block2-weeks6-10.pdf` — into
`print/`. Half-letter landscape, 1-sided, 0.85in left margin for 3-hole punch.

---

## Adding a week

**Screen** — append one object to the `WEEKS` array in `weeks.html`:

```js
{
  n:6, block:2, title:"Hello, micro:bit",
  sub:"Today you'll make the micro:bit smile at you.",
  open:{label:"Open MakeCode", url:"https://makecode.microbit.org/"},
  steps:["...", "...", "..."],          // 5 max, one line each
  challenge:"...",                       // the remix
  fixes:[["Symptom","Fix"], ...],        // 3 max
  video:"Watch Dad do step 2 (40 sec)"
}
```

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

## `videos/`

Drop 30–60 second clips of the tricky step here. They're linked from the
"Something's wrong" section on each week's page.
