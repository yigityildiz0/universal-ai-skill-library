# Layout and pagination rules

## Page

- A4 (210×297 mm) default; US Letter only when asked. Margins 18–20 mm sides, 19 mm top, 21 mm bottom (footer room). Never below 12 mm;
  keep 8 mm clear of the edge for any text (printers clip there).
- Bind margin: add 6–8 mm to the inner side for double-sided print.
- Page numbers `n / N` in the footer, none on the cover. Set title/author metadata.
- Landscape only for sections that need it (`.landscape`) and for wide tables; do not mix orientations without a reason.

## Text

- Body 10.5–11.5 pt, leading 1.4–1.6, measure 60–90 characters per line (one column on A4 portrait at 11 pt).
- Floors: body ≥10 pt, table ≥9 pt (8.5 only for dense reference tables), footnote/caption ≥8.5 pt.
- Left aligned. Justify only with hyphenation tested for the language; otherwise rivers appear.
- Turkish: keep `ı/i`, `İ/I`, `ğ ş ç ö ü` correct; use a decimal comma (0,978), non-breaking space between number and unit
  (`5&nbsp;cm`), correct quotes (“ ”), en dash for ranges (10–15).
- Headings are claims or clear labels; two levels in short documents, three in long ones. Number only when cross-referenced.

## Keep-together rules (what never splits)

| Element | Rule |
|---|---|
| Heading | stays with the next block (`break-after:avoid`); a heading + table/figure moves together |
| Paragraph | ≥3 lines at the bottom and top of a break (`orphans/widows:3`) |
| Figure + caption | one unit |
| Callout, card, quote, code block, formula | one unit |
| Table ≤ ~1/2 page | `table.keep` — whole table on one page |
| Long table | rows never split; header repeats; add a "continued" cue only if the design needs it |
| List item | not split; keep intro sentence with the first items |
| Cover | own page |

If an element is taller than a page, do not rely on keep rules: split the content on a logical boundary (table by row
groups with a repeated header, figure into two panels) and say so.

## Tables

- `<table>` with `<caption>` (label above), `<thead>`, `<tbody>`; first column left, numbers right-aligned or decimal-aligned.
- Column widths by content; long text wraps (`overflow-wrap:anywhere`); no horizontal scroll or overflow.
- Wide table: first try shorter headers and units in the header; then `.wide` (−7 %); then a landscape section; never <9 pt.
- Sources and notes under the table in `.small`, inside the same keep block when the table is short.

## Figures and images

- Local files, ≥150 dpi at printed size (1000 px for half width, 1800 px for full width on A4), width set, alt text, caption below.
- SVG for diagrams. Photos keep aspect ratio; crop to the point; do not stretch.
- Credit and licence in the caption (`Kaynak: …, CC BY 4.0`).
- Charts: print-first colours, direct labels, units on axes; one message per chart; a sentence beside it that states the result.

## Colour and accessibility

- Text contrast ≥4.5:1 (large text ≥3:1); do not rely on colour alone (add icons, words, patterns); test in grayscale.
- Reading order = source order; real headings and lists; language attribute; meaningful link text (URLs wrap).
- Avoid text in images; if unavoidable, repeat in alt text.

## Checks before delivery

1. `html_lint.py` — no errors.
2. `pdf_audit.py --render` — no errors; warnings explained or fixed.
3. Looked at every page: nothing cut, no stranded heading, tables intact, figures whole, footer numbers right, no odd white gaps
   (a gap of up to a third of a page above a moved figure or table is normal; larger gaps mean the block should be reduced or split).
4. Opened in a second viewer if possible (browser + Acrobat/Edge) — fonts and layout agree.
5. File name and metadata correct; size reasonable (images optimised).
