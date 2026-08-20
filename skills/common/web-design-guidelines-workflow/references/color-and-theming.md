# Color and Theming

Color communicates meaning and hierarchy. Preserve the project's notation and semantic tokens unless the task includes a color-system change.

## Semantic use

- Name colors by role: surface, text, border, action, success, warning, danger, focus.
- Do not borrow a token outside its meaning because its current value happens to look right.
- Keep one color associated with one meaning. If the accent hue signals interaction, do not reuse it on inert decoration that looks clickable.
- When filled color encodes priority, use one primary colored action in the current decision context and keep peer actions neutral. Preserve a different established hierarchy if it already works.
- Never rely on color alone for status, validation, or selection. Add text, shape, icon, underline, or another stable cue.
- Check cultural meaning when status colors are load-bearing across locales.

## Contrast

Measure the rendered foreground/background pair in every relevant state and theme.

Use WCAG 2.2 thresholds for WCAG 2.x claims:

| Content | AA threshold |
| --- | --- |
| Normal text | 4.5:1 |
| Large text | 3:1 |
| UI components and graphical objects covered by 1.4.11 | 3:1 against adjacent colors |

Large text follows the WCAG definition, not a visual guess. Disabled controls and logos have specific exceptions; do not apply a threshold blindly.

APCA may be used as a supplementary perceptual diagnostic, especially while tuning a palette. Label it clearly and never substitute it for WCAG 2.x conformance.

For translucent surfaces, gradients, images, and blur effects, test the lightest and darkest backgrounds the foreground can encounter. A token name alone does not prove contrast.

## OKLCH

Use OKLCH when the project already uses it, when creating a new palette, or when the user requests conversion. Do not introduce one isolated OKLCH value into a consistent hex/RGB codebase.

Format:

```css
oklch(L C H)
oklch(L C H / alpha)
```

- Lightness is perceptual; hue remains more stable across a ramp than in HSL.
- The display gamut is finite. Clamp chroma while preserving lightness and hue when a value falls outside the target gamut.
- Equal absolute chroma does not look equally vivid across hues. Compare each hue relative to its available gamut.
- When fixing contrast, adjust lightness first, preserve hue and chroma when possible, then remeasure the rendered pair.

## Palettes and themes

- Build palette steps with controlled lightness, hue, and gamut rather than mechanically changing HSL lightness.
- Separate primitive values from semantic roles. Components consume semantic roles.
- Dark mode is not a mechanical reversal. Remap semantic tokens, tune values for the dark appearance, and recheck every foreground/background pair.
- Provide explicit colors for native controls where platform dark mode can otherwise produce unreadable combinations.
- Set `color-scheme` and theme metadata when the implementation needs native browser chrome to match.
- Test light, dark, increased-contrast, hover, active, focus, selected, disabled, loading, error, and success states.

## Wide gamut

Provide an sRGB-safe base when shipping a Display-P3 enhancement:

```css
.accent {
  color: oklch(0.7 0.2 150);
}

@media (color-gamut: p3) {
  .accent {
    color: oklch(0.7 0.3 150);
  }
}
```

Check the target browser matrix before adding a compatibility fallback. Do not claim a color is safe from notation alone; verify its mapped result.
