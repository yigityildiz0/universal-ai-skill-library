# Design languages

Pick from these or mix with the user's input. In the kit, add one class to `<body>` (`theme-akademik`, `theme-klinik`,
`theme-editoryal`, `theme-teknik`, `theme-modern`, `theme-minimal`). All themes keep the same layout rules (print.css), so
pagination stays safe whatever the look.

| Language | Feel | Fonts (all cover Turkish) | Accent | Best for |
|---|---|---|---|---|
| Akademik sade | scholarly, calm, authoritative | Cambria/Caladea/Georgia headings, Calibri/Carlito body | bordo `#8e2330`, lacivert text | thesis chapters, seminar summaries, literature notes |
| Klinik temiz | clean, airy, trustworthy | Calibri/Carlito throughout | turkuaz `#0e7c86` | clinical guides, patient handouts, rehabilitation protocols, exam study sheets |
| Editoryal | magazine, warm, generous whitespace | Georgia/DejaVu Serif body and headings | tuğla `#b4561f` | essays, long reads, newsletters |
| Teknik rapor | dense, structured, numbered | Calibri body, tighter leading | mavi `#2f5da8` | methods, protocols, data reports, measurement tables |
| Modern kartlı | soft panels, bold numbers | Calibri | mor `#5b4bdb` | one-pagers, KPI summaries, infographics-lite |
| Minimal siyah-beyaz | no fills, print-friendly | Calibri | black | forms, printouts, legal-style documents |

## Choosing

- Topic first: clinical/health → Klinik temiz or Akademik sade; data-heavy → Teknik rapor; story → Editoryal; short summary → Modern kartlı;
  to be printed in bulk → Minimal.
- Reader and medium: printed in grayscale → check with Minimal; screen-only → colour accents allowed to be stronger.
- Offer 3–4 relevant options with a one-line mood each, not the whole list.

## Customising safely

- Change variables only: `--accent`, `--accent-soft`, `--ink`, `--muted`, `--rule`, `--font-head`, `--font-body`, `--body-size`.
- Keep body 10.5–11.5 pt, line height 1.4–1.6, contrast ≥4.5:1, one accent colour plus its soft tint.
- A brand colour that fails contrast is used for rules and fills, not for small text.
- Cover: title, subtitle, author, course/organisation, date. No decorative images that need `position:absolute`.
- Components available: `.callout` (key message), `.card`, `.kpi`, `blockquote`, `figure`, `table.keep`, `.cols-2`, `.small`.

## Layout recipes

- **Study guide:** cover → contents → sections with `.callout` "Özetle" → tables → key terms table → references.
- **Report:** summary page → method → results (figure + table pairs) → discussion → references; landscape section for wide tables.
- **Handout (1–2 pages):** large title, three `.kpi`, one table, one figure, checklist with `ul`.
- **CV / one-pager:** `.cols-2` for side-by-side blocks (not flex), consistent date format, no photos unless asked.
