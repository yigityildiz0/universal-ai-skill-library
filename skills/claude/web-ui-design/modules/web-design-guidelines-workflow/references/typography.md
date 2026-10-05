# Typography

Good interface typography uses a restrained scale, clear hierarchy, comfortable spacing, and robust wrapping. Preserve the existing type system unless the task explicitly changes it.

## Fonts and files

- Use `.woff2` for web delivery. Keep `.woff` only for an unusually old support matrix; avoid serving desktop `.ttf` or `.otf` files when a web format is available.
- Rarely use more than three families. Pair for clear role contrast rather than near-duplicate styles.
- Use display faces and thin weights only where their size and contrast support them. Below 18px, start at weight 400 or above.
- Variable fonts are useful when the design needs several weights, optical sizes, widths, or custom axes; they are not automatically smaller.
- Prefer high-level CSS properties such as `font-weight`, `font-optical-sizing`, and `font-variant-numeric` over raw variation or feature tags when a property exists.
- Load intended weights and styles. Disable synthesis only after verifying every emphasis state and the full fallback stack.

## Type system

Define a small role-based scale and deviate sparingly. A reasonable starting point when no system exists:

| Role | Size | Line height | Weight |
| --- | --- | --- | --- |
| Display | 36px | 1.1 | 600 |
| Title | 24px | 1.2 | 600 |
| Heading | 18px | 1.3 | 600 |
| Body | 16px | 1.5 | 400 |
| Caption | 13px | 1.4 | 400 |

Map visual heading prominence to the document hierarchy. Adjacent deep levels may share a size when weight or spacing still separates them. Do not choose heading tags for browser-default size.

- Keep headings near 1.1–1.3 line height.
- Keep body copy near 1.5–1.6.
- Any text wrapping to three or more lines needs about 1.4 or more.
- Large headings may use slightly negative tracking; small uppercase labels may need positive tracking; body copy usually needs neither.

Treat the values as starting points. Judge them in the actual typeface, platform, density, and content.

## Measure and wrapping

- Cap long-form text around 60–75 characters per line.
- Use `text-wrap: balance` on short headings and `text-wrap: pretty` on short descriptions when supported.
- Use `overflow-wrap: break-word` for long identifiers and URLs.
- Use `white-space: nowrap` only where a break would damage a short label or badge.
- Avoid justified text in ordinary interfaces.
- For flex/grid text that must shrink, ensure the child can shrink and has an intentional overflow strategy.

## Numbers, truncation, and content access

- Use `font-variant-numeric: tabular-nums` for changing values and aligned numeric comparisons.
- Single-line ellipsis requires overflow clipping and no wrapping; multi-line truncation uses a line clamp.
- Truncation hides information. Keep meaningful full text available through expansion, a tooltip that is also keyboard-accessible, or a detail view.
- Keep useful text selectable. Use `user-select: none` only on a specific drag or gesture surface where selection demonstrably interferes.

## Forms and mobile

- Keep input text at 16px on mobile to avoid iOS focus zoom. Smaller desktop sizes may begin at a breakpoint.
- Never block zoom to compensate for undersized inputs.
- Placeholder styling remains readable but visually subordinate; the visible label owns the field name.

## Language and punctuation

- Set the correct `lang` and `dir`.
- Use `<bdi>` or an equivalent isolation strategy for mixed-direction values where adjacent text disturbs order.
- Do not manually reverse digits in RTL content.
- Store natural source text and use CSS for `text-transform`.
- Use appropriate punctuation for prose and locale; keep code characters literal.

## Rendering and verification

- Check actual font loading, fallback changes, synthetic styles, and layout shift.
- Test the smallest and largest viewports, 200% zoom, long localized strings, mixed-direction content, and dynamic numeric values.
- Optical corrections such as text trimming or font smoothing are progressive, project-specific choices. Do not force them globally merely because the property exists.
