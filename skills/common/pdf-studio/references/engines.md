# Engines, fonts and fallbacks

## Preferred: HTML + CSS → headless Chromium (Edge or Chrome)

`python scripts/build_pdf.py document.html out.pdf --size A4 --orientation portrait`

- Windows: Microsoft Edge is preinstalled (`msedge.exe`); the script finds Edge or Chrome automatically; macOS/Linux: Chrome/Chromium.
- No extra install, no network. Fonts are embedded as subsets by the print engine.
- Direct command if needed: `msedge --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf=out.pdf file:///path/doc.html`
  (use a temporary `--user-data-dir`).
- Page numbers via `@page` margin boxes need a recent Chromium (≈ v131+). If footers are missing, update the browser or add the numbers with PyMuPDF
  after rendering (`page.insert_text`).

## Audit tooling

- `python -m pip install pymupdf` gives geometry checks and page PNGs (`pdf_audit.py --render pages/`). Without it only a reduced check runs.
- Use the PNGs to read each page. No poppler is needed.

## When there is no browser

| Situation | Option |
|---|---|
| Linux/server without Chromium | WeasyPrint (`pip install weasyprint`; needs Pango) — supports `@page`, `break-*`, `target-counter` |
| Need an editable source too | write DOCX with styles, convert with LibreOffice `soffice --headless --convert-to pdf` |
| Pure Python, no HTML | ReportLab Platypus or fpdf2 (see below) |
| Only a chat interface with a code tool | build HTML, run the Python tool to produce PDF with WeasyPrint/ReportLab, show page images |
| No tool can run code | deliver the HTML (print-ready, Ctrl+P → "Save as PDF", margins "Default", background graphics ON) and say the PDF was not produced |

## ReportLab / fpdf2 essentials (Turkish-safe)

```python
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont("Body", r"C:\Windows\Fonts\calibri.ttf"))        # or DejaVuSans.ttf / NotoSans-Regular.ttf
pdfmetrics.registerFont(TTFont("Body-Bold", r"C:\Windows\Fonts\calibrib.ttf"))
pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body", boldItalic="Body-Bold")
# set styles['Normal'].fontName = "Body" etc.; the built-in Helvetica cannot draw ı ğ ş İ
# Platypus: KeepTogether([heading, table]); Table(data, repeatRows=1); Paragraph for wrapping; never canvas.drawString for variable text
```

- Check the registered path exists; a wrong path may silently fall back to a font without the glyphs.
- Test the string `ığşİĞŞçöüÇÖÜ ₺ — – “ ” ≥ ≤ ±` in every font used.

## Fonts

- Safe stacks (already in `print.css`): body `Calibri, Carlito, "Noto Sans", "DejaVu Sans", Arial, "Liberation Sans"`; serif `Cambria, Caladea, Georgia, "DejaVu Serif", "Times New Roman"`.
- Carlito and Caladea are metric-compatible with Calibri and Cambria (layout stays the same on Linux).
- Do not use Segoe UI, Aptos or downloaded fonts unless the user insists and the fonts are embedded and licensed.
- Do not rely on `font-weight: 600` for fonts that have only regular and bold; use 400/700.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Rule ignored (rows still cut) | rule overridden, ancestor is flex/grid, very tall row | check computed CSS, move content out of flex/grid, shorten the row |
| Everything tiny | viewport meta/zoom or `vw` units | remove, use pt/mm |
| Background colours missing | print backgrounds off | `print-color-adjust: exact` (in print.css) |
| Squares for letters | font lacks glyph / wrong font path | change stack, install font, register TTF |
| Blank last page | trailing forced break or margin | remove trailing `.page-break`, `body{margin:0}` |
| Images missing | file path relative to wrong folder | keep HTML and images together; use `build_pdf.py` (it uses the HTML's folder) |
| Footer numbers missing | old Chromium | update browser or stamp numbers with PyMuPDF |
