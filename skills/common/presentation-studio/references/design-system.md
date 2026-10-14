# Design system: layouts, hierarchy, colour, anti-patterns

Read before planning any slide. These rules exist because two real decks on the same topic and
sources came out very differently: the weak one used one layout for 59 slides, put every text role
at the same size, and decorated slides with stripes and title underlines. The strong one varied
layouts, used real photos cropped to the point, big-number callouts and dark section breaks, and
was rendered and fixed before delivery.

## 1. Layout families

Every content slide declares exactly one layout. The deck kit (`assets/deck-kit/kit.js`) implements
all of them; other tools should reproduce the same geometry.

| Layout | Use for | Must contain |
|---|---|---|
| `cover` | first slide | title, subtitle, presenter/course/date, one strong real photo (right half) |
| `agenda` | the 3–6 questions/sections the talk answers | numbered chips, one line per item |
| `section` | start of every main part (dark) | big section number, section title, one-line promise |
| `stat` | one or more numbers that carry the message | 1–3 big numbers (60–110 pt), label under each, one takeaway sentence |
| `cards` | 2–4 parallel concepts (types, units, categories) | equal cards, mark/icon/image + head + ≤12 words body |
| `photoSteps` | a protocol, test, technique, exercise, positioning | numbered steps (≤8 words each) + real photo cropped to the action + result callout |
| `compare` | A vs B (make/break, old/new, two devices, two groups) | two panels, same structure on both sides, one takeaway |
| `process` | a sequence or decision path (3–5 steps) | chips joined by arrows, short head + body per step |
| `chart` | a quantitative result | native editable chart, labelled values, interpretation box |
| `table` | ≤5 rows × ≤4 columns of comparable facts | header row, zebra rows; bigger tables go to notes or handout |
| `bullets` | only when nothing else fits | ≤4 bullets, ≤12 words each, preferably with an image on the right |
| `quote` | a key definition, guideline sentence or take-home message | one sentence, attribution |
| `closing` | summary / take-home (dark) | 3–4 conclusions that answer the agenda questions |
| `references` | bibliography (light) | full references, split across slides rather than shrinking |

Rules:
- No layout three times in a row (references excepted). Alternate dark (`cover`, `section`,
  `closing`) and light content slides: the "sandwich" rhythm marks structure.
- Every content slide carries a visual: photo, diagram, chart, table, numbered chips or big number.
  A slide that is only title + paragraph is a defect, not a style.
- Prefer one idea per slide. Two ideas → two slides. Detail goes to speaker notes, not smaller type.

## 2. Type roles and sizes

The brief sets the floor (default 36 pt for every on-slide text). Sizes are by ROLE, never one size
for everything:

| Role | Default | Note |
|---|---|---|
| title | 40 pt bold | one line preferred, two max; a title is a claim, not a topic label |
| body / bullets / steps / labels / chart labels / table text | 36 pt | the floor |
| big number | 60–110 pt bold | accent colour |
| section title / cover title | 48–54 pt bold | on dark background |
| kicker (section label above the title) | 20 pt caps | OFF by default — only if the user agrees; otherwise a ≥36 pt subtitle |
| source line | 16 pt | exception — bottom left, every content slide |
| image credit | 14 pt | exception |
| slide number | 14 pt | exception |
| references slide | 14–16 pt | exception — split slides instead of going smaller |

Any exception not listed in the brief must be asked about (see SKILL.md conflict protocol). If
text does not fit at the floor: shorten, split the slide, or move detail to notes — never shrink.

## 3. Fonts that survive any computer

Use **Calibri** for everything by default (titles bold) — it ships with Office on Windows and macOS,
exists in Google Slides, has a metric-compatible substitute (Carlito) in LibreOffice, and is narrow
enough to keep 36 pt lines readable. Fallback: **Arial** (Liberation Sans substitute). Also safe:
Cambria/Georgia/Times New Roman for serif titles, Verdana/Tahoma. Never ship Segoe UI, Aptos,
Montserrat, Roboto, Poppins or any downloaded font unless the user insists and accepts the risk (ask
via the conflict protocol): the classroom computer or Google Slides conversion substitutes a font with
different widths and lines break differently. One family for the whole deck; at most two.

## 4. Colour

- Choose one palette per deck and keep it: dark (backgrounds of cover/section/closing), ink (text),
  muted (source/credit), light/card (panels), one dominant accent + two supporting accents.
- The dominant accent carries 60–70 % of colour weight; accents are for numbers, chips, keywords.
- Contrast: dark text on light, white text on dark; never mid-grey text on a photo.
- Topic-appropriate palette: clinical/teal, academic/navy-crimson, neutral/graphite-blue, nature/green
  (kit themes `klinik`, `akademik`, `sade`, `doga`). An institution template overrides all of this.

## 5. Anti-patterns (each is a defect to remove in QA)

- Thin full-width colour stripe at the top or bottom of every slide; vertical stripe on one edge.
- Line under the title; accent border on one side of a card.
- The same title + paragraph frame on every slide.
- Text-only slides; bullet walls; paragraphs longer than two lines on the slide.
- Every text at one size (titles, body and source lines indistinguishable).
- Content squeezed into the top half with the bottom half empty, or the reverse.
- The same schematic reused on several slides to illustrate different points.
- Decorative clip art, stock "business people" photos, emoji, WordArt, 3-D charts, shadows on text.
- Centred body text (centre only titles of section/cover slides, callouts and big numbers).
- Number and unit split across lines (`5` / `cm`) — the kit inserts no-break spaces.
- Images stretched, pixelated (<1000 px wide for a half-slide image) or with watermarks.
- AI-generated images presented as clinical photographs.

## 6. Visual motif

Pick one motif and repeat it: numbered circular chips + rounded cards (kit default), or photo frames
with a caption bar. Do not mix motifs. Icons, when used, come from one set and one colour.

## 7. Sample-slide gate

Before building the whole deck, build 4 representative slides (cover, a photo/protocol slide, a
compare or stat slide, the densest content slide), render them and check them against this file.
Fix the system (kit/theme), then generate the rest. Continue without asking when the brief is clear;
ask only if a choice would change the result (template, colour family, count).
