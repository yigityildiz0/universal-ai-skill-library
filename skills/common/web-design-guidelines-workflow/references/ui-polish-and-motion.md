# UI Polish and Motion

Polish comes after semantics, structure, and content. Match the component library, design tokens, icon set, density, and motion language already present.

## Surfaces and corners

For closely nested rounded surfaces with an even inset:

```text
outer radius = inner radius + inset
```

Use this as a visual relationship, not a universal law. When the inset is large, asymmetric, or the surfaces are independent, use the design-system tokens that fit each layer.

- Use borders for structure and state: dividers, table boundaries, inputs, selected and focus states.
- Use subtle layered shadows when a card, button, menu, or modal needs elevation rather than separation.
- Avoid combining heavy border, large shadow, and tinted background without a hierarchy reason.
- When an image edge disappears into its surface, a neutral low-opacity 1px inner outline can restore separation. Do not tint it with the accent color or apply it indiscriminately.

## Optical alignment

- Correct buttons with asymmetric text/icon weight by adjusting the icon, SVG view box, or side padding slightly.
- Play triangles and directional glyphs often need a small optical shift.
- Judge baselines, cap height, perceived center, and dark/light mass at final render size.
- Prefer fixing the icon asset over accumulating component-specific nudges.

## Icons

- Use one coherent icon family per surface.
- Match icon optical weight to nearby text. On a 24px stroke grid, 1.5px often fits regular text and 2px often fits semibold text, but preserve an icon set's intentional system.
- Size inline icons around the text's cap-height relationship and test at the smallest rendered size.
- Use a single `currentColor` SVG for color states rather than separate assets.
- Outline is a useful default and fill can signal an active state when the icon set supports both.
- Flip only direction-dependent icons in RTL. Do not mirror logos, checkmarks, physical objects, or conventional media controls without a specific reason.

## Motion

- Use CSS transitions for interruptible state changes. Use keyframes for deliberate one-shot sequences.
- Transition only the properties that change. Never use `transition: all`.
- Prefer compositor-friendly `transform` and `opacity`; use `filter` sparingly and measure it.
- Add `will-change` only after observing a first-frame problem; every layer costs memory.
- High-frequency interactions get instant feedback or a brief, restrained transition. Reserve expressive motion for infrequent moments.
- Exit motion is usually shorter and quieter than entrance motion.
- Motion is never the only signal. Preserve a static color, icon, label, or shape change.
- Respect reduced-motion preferences and verify the static version.

When a staged entrance improves hierarchy, split content into semantic groups and stagger lightly. Avoid turning routine lists, tabs, or hovers into repeated entrance animations.

For stateful icon swaps, a restrained crossfade using opacity, small scale, and optional blur can work. Reuse the project's motion library if already installed; otherwise use CSS. Do not add a dependency solely for one micro-interaction.

A press scale near `0.96` is a useful starting point for tactile feedback. Keep it optional, avoid values below `0.95`, and omit it when the product's motion language or task frequency makes it distracting.

## Performance and state checks

- Inspect hover, focus, active, selected, disabled, loading, success, error, open, and closed states.
- Replay complex animation slowly with developer tools when available.
- Verify rapid reversal and repeated triggering; interactions must not queue or snap.
- Confirm first render does not animate a control's default state unintentionally.
- Measure layout stability and avoid animating geometry that causes reflow when a transform can express the same effect.
