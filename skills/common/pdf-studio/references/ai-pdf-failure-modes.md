# How AI-made PDFs fail — and the cheap prevention

Compiled from print-CSS and PDF-engine documentation and troubleshooting guides (page-break behaviour in Chromium,
repeated table headers, orphan headings, missing-glyph "tofu" boxes, base-14 font limits in ReportLab) plus the failures seen
in real AI-built decks and guides. Vendor blog claims were treated as hints and verified by rendering. The prevention rules
change mechanics only; they never shorten or simplify the content.

| # | Failure | Why it happens | Prevention (default in the kit) | How it is caught |
|---|---|---|---|---|
| 1 | Table cut across pages; a row sliced in half | browsers split rows when nothing forbids it | `tr,td,th{break-inside:avoid}`; short tables get `.keep`; very tall rows are rewritten shorter | `pdf_audit` table check + look at the page |
| 2 | Header row not repeated on continuation pages | `thead` missing or `display` overridden | real `<thead>`; `thead{display:table-header-group}` | `html_lint`, `pdf_audit` |
| 3 | Heading alone at the bottom of a page | no keep-with-next | `h1–h4{break-after:avoid}`, `h2+*{break-before:avoid}` | `pdf_audit` orphan-heading warning |
| 4 | Figure or caption split from its image, or image cut at the page edge | image and caption are siblings; no width limit | `<figure>` with `<figcaption>`, `break-inside:avoid`, `max-width:100%` | audit + look |
| 5 | Text past the margin or off the page; long URLs/words overflow | fixed widths, no wrapping rule, `nowrap` | `overflow-wrap:anywhere` on cells/links/code; no fixed heights; unsafe-band check | `pdf_audit` edge-band ERROR |
| 6 | Overlapping blocks | absolute positioning, negative margins, flex/grid collisions | normal document flow; no `position:absolute` for text | `html_lint`, `pdf_audit` overlap ERROR |
| 7 | Content silently cut off | `height` + `overflow:hidden` | `min-height` only | `html_lint` ERROR |
| 8 | Turkish letters or symbols as squares / `?` / missing | font lacks the glyph; ReportLab built-in Helvetica cannot draw ı ğ ş İ; font path wrong so it silently falls back | font stacks with full Latin-Extended coverage; register a Unicode TTF before using ReportLab/fpdf; test the string `ığşİĞŞçöüÇÖÜ` | `pdf_audit` U+FFFD ERROR, look at the page |
| 9 | Emoji or dingbats print as empty boxes | no colour-emoji font in the print engine | use words, SVG icons or images | `html_lint` emoji warning |
| 10 | Font changes on another computer | font not embedded / not installed | print to PDF (embeds subsets); safe stacks; avoid rare fonts | `pdf_audit` font-embedding warning |
| 11 | Page size surprises (Letter vs A4), margins differ, headers/footers added by the browser | defaults of the engine | explicit `@page{size:A4;margin:…}`; `--no-pdf-header-footer` | `pdf_audit` size warning |
| 12 | Blank pages or a lone line on a page | forced breaks + `break-before` on an element that already starts a page; margin collapse | one break mechanism (`.page-break`), never a stack of empty divs | `pdf_audit` blank-page warning |
| 13 | Blurry images, tiny text | low-resolution images; text shrunk to "make it fit" | ≥150 dpi at printed size; move content to a new page or landscape section instead of shrinking | `pdf_audit` dpi/size warnings |
| 14 | Colour only meaning, low contrast, unreadable in black-and-white | design without a print check | contrast ≥4.5:1; icons + words; the minimal theme as a check | look at a grayscale render |
| 15 | Page numbers missing, "Page X of Y" wrong | numbering added in body text or by hand | `@page` margin boxes `counter(page)/counter(pages)`; cover without number | look at footers |
| 16 | Unwanted decorative clutter, inconsistent styles between sections | each section styled separately | one theme class, one stylesheet, a few components (`callout`, `card`, `kpi`) | review |
| 17 | Layout that looks right on screen but not in print | screen-only CSS (`vh`, scroll areas, sticky) | print-first CSS; `vh/vw` banned | `html_lint` |
| 18 | Remote fonts/images blank offline | links to URLs | local files only | `html_lint` |
| 19 | Invented content to fill space (numbers, quotes, references) | pressure to look complete | content only from user material or cited sources; mark gaps | review against sources |
| 20 | "Fixed" by shrinking everything until it fits | easiest edit | floors: body ≥10 pt, table ≥9 pt, footnote ≥8.5 pt; use page breaks, landscape sections, splitting | `pdf_audit` min-size warning |

## Rules that keep quality high

- Always look at every rendered page image. A PDF that passes all checks can still look wrong; a check that fails usually
  points to a CSS rule that was not applied (an `!important` conflict, a flex ancestor, an old browser).
- Fix the cause once in the stylesheet, rebuild, re-audit. Do not patch single pages by hand.
- Keep the long, rich version of the content. If a table is too wide, rotate that section to landscape; if a figure does not
  fit, start it on a new page; if a heading would be orphaned, let the whole block move.
- Tell the user what could not be checked (for example, no PyMuPDF → no geometry audit; no Edge/Chrome → fallback engine).

## Engine notes

- Chromium (Edge/Chrome print-to-PDF): best CSS support; honours `break-*`, `@page` margin boxes (page counters) in current
  versions; ignores `target-counter()` (no automatic page numbers inside a table of contents).
- WeasyPrint: strong paged-media support incl. `target-counter`; needs system fonts + Pango.
- wkhtmltopdf: old WebKit; poor modern CSS; avoid for new work.
- ReportLab/fpdf2: precise but manual: register Unicode TTF, use `KeepTogether`, `repeatRows=1`, `Paragraph` for wrapping.
- LibreOffice (DOCX/ODT → PDF): good when the user needs an editable source too; use styles, not manual spacing.
