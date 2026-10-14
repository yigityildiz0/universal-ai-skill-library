---
name: pdf-studio
description: "Make clean, reliable PDFs (study guides, reports, handouts, summaries, CVs, brochures, forms of any topic): asks the right questions first (orientation, purpose, design language, sources), builds from HTML/CSS with print rules so tables, headings and figures never split badly and nothing overflows, then renders and audits every page. Turkish triggers: PDF hazırla, PDF yap, PDF oluştur, rapor PDF, çalışma kılavuzu, el notu, özet PDF, PDF düzenle, sayfa bölünüyor, tablo ikiye bölündü."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# PDF Studio

Owns every request to create or redo a PDF document. Related: `presentation-studio` (slide decks and their PDF export),
`office-docs-qa` (read/merge/split/OCR/redact existing PDFs), `academic-study-coach` and `medical-evidence-research`
(content). This skill is about the document as an object: layout, pagination, fonts, readability and checks.

Why it exists: AI-made PDFs fail in the same few ways: a table or figure cut across two pages, a heading stranded at the
bottom of a page, text running past the margin, Turkish letters shown as squares, overlapping blocks, blurry images,
a layout nobody asked for. Each failure has a known cause and a cheap prevention (`references/ai-pdf-failure-modes.md`).
The rules below remove those failures without limiting what the document can say or how it looks.

## Step 1 — Ask first (batched, short)

Before writing anything, ask the intake questions in `references/intake-questions.md` in ONE message, as a numbered list of
multiple-choice questions (use the host's question tool if it has one). Always cover:
1. **Purpose and reader** (study, share, print, submit, present, archive).
2. **Orientation and size**: portrait or landscape; A4 default (Letter only on request).
3. **Design language**: offer 3–4 options that fit the topic (`references/design-languages.md`), each in one line with its mood.
4. **Content source**: what to use (files, pasted text, topic to research), what must be quoted or cited, language.
5. **Length and structure**: pages or sections, cover/contents/references yes or no.
6. **Special needs**: logo/brand colours, print in black-and-white, figures/tables expected, accessibility.

Skip a question only when the user already answered it or a saved preference exists. Do not ask what the defaults below already
decide. When the user says "you decide", choose the best fit, say what you chose in one line, and continue.

If the user's instruction conflicts with a rule here (for example "fit everything on one page at 7 pt"), ask one short
question: rule or your wish, this document or permanently. Never silently pick.

## Step 2 — Build (HTML/CSS → PDF)

1. Write one self-contained `document.html` that links `assets/pdf-kit/print.css` (layout rules) and one theme from
   `themes.css`. Structure with real elements: `h1–h3`, `p`, `ul/ol`, `table` with `thead`, `figure/figcaption`,
   `.callout`, `.keep` (never split), `.page-break` (forced new page).
2. Fonts: use the stacks in the kit (Calibri/Carlito, Cambria/Georgia, Arial/Liberation/Noto). All must cover Turkish
   `ı İ ğ Ğ ş Ş ç ö ü` and the symbols you use. Never rely on a font that may be missing on the build machine.
3. Images: local files, ≥150 dpi at printed size, `width` set, alt text, caption inside the same `figure`.
4. Run `python scripts/html_lint.py document.html` → fix every ERROR.
5. Render: `python scripts/build_pdf.py document.html out.pdf --size A4 --orientation portrait`
   (uses headless Edge/Chrome; fallbacks in `references/engines.md`).
6. Audit: `python scripts/pdf_audit.py out.pdf --render pages/` (needs `pip install pymupdf`; without it, it runs the reduced
   check and says so). Look at EVERY page image. Fix causes in the HTML/CSS, not by shrinking text.
7. Deliver the PDF, state page count, orientation, fonts, and anything not verified.

Direct-to-PDF libraries (ReportLab, fpdf2) only when HTML is impossible: register a Unicode TTF first
(`references/engines.md`), flow content with Platypus `KeepTogether` / repeat table headers, never draw text at fixed
coordinates for variable-length content.

## Defaults that apply without asking

- A4, margins 18–20 mm (never below 12 mm; keep 6 mm clear of any trim), body 10.5–11.5 pt, line height 1.4–1.6, one text
  column unless the design language says otherwise, left-aligned (justify only with hyphenation tested).
- Minimum 9 pt for any text (footnotes 8.5 pt); table text 9.5 pt+.
- Headings never at the bottom of a page; tables, figures, callouts, code blocks and quotes are not cut by page breaks;
  long tables repeat the header row and keep rows whole; paragraphs keep ≥3 lines at both ends of a break.
- Page numbers in the footer (`n / N`), document title in metadata, `lang="tr"` (or the document language).
- Colours: text contrast ≥4.5:1; works in black-and-white; never colour as the only meaning.
- Everything inside the page: no horizontal overflow; long URLs and words wrap (`overflow-wrap:anywhere`).
- Content never invented: numbers and quotes come from the user's material or a cited source.

## Do not lose quality for safety

The rules constrain mechanics, not substance: keep depth, nuance, examples and tables. Prefer splitting a long table on a
row boundary with a repeated header over deleting rows; prefer a landscape section for a wide table over shrinking it; prefer
a new page for a figure that does not fit over a smaller figure.

## Files

| Need | File |
|---|---|
| Question bank, how to ask | `references/intake-questions.md` |
| Design languages with tokens | `references/design-languages.md` |
| Pagination, tables, figures, margins, accessibility | `references/layout-rules.md` |
| Known AI failure modes and fixes | `references/ai-pdf-failure-modes.md` |
| Engines, fonts, fallbacks, install | `references/engines.md` |
| CSS kit and starter | `assets/pdf-kit/` (`print.css`, `themes.css`, `template.html`) |
| Scripts | `scripts/build_pdf.py`, `pdf_audit.py`, `html_lint.py` |
| Turkish user guide | `KULLANIM-KILAVUZU.md` |
