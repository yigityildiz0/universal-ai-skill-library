# Layout and Optical Balance

Layout communicates hierarchy before the words are read. Preserve the project's density and spacing scale when they remain usable.

## Grouping

Use grouping tools in this order:

1. negative space;
2. a background surface when the group acts as one unit;
3. separator lines for dense structures where space is too expensive.

Make the gap between groups at least twice the gap within a group as a strong starting point. Avoid combining a large gap and a separator when either one already communicates the boundary.

Interactive elements must look interactive through shape, border, underline, or consistent placement. Static content should not impersonate a control.

## Alignment, symmetry, and balance

- Choose a small set of shared alignment edges and keep text, icons, cards, headers, and actions on them.
- Use one repeated indent step per hierarchy level.
- Align text to the leading edge and tabular numbers to the trailing edge.
- Check baselines and cap-height relationships, not only bounding boxes.
- Compare visual weight, not just width: a dark icon or dense text block may need more space than a light element of the same geometry.
- Correct asymmetric icons and glyphs optically. Do not force geometric centering when it looks wrong.
- Preserve intentional asymmetry when it establishes focus. Flag unexplained one-off offsets, unequal gutters, drifting baselines, inconsistent padding, and accidental mismatched heights.

Use logical CSS properties for direction-dependent layout: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`. Reserve physical directions for genuinely physical geometry.

## Hierarchy and disclosure

- Put the primary content and action near the start of the reading order.
- Keep one clear primary decision per view; group secondary actions when they compete.
- Hidden, clipped, or horizontally scrollable content needs a visible cue. A useful fallback is a 16–32px peek of the next item or a specific disclosure label such as “Show 12 more results.”
- Do not truncate important content without a way to reveal it.

## Spacing and edges

When no established scale exists, start near:

| Relationship | Starting point |
| --- | --- |
| Adjacent bordered or filled controls | 12px |
| Clearance around borderless controls | 24px |
| Unrelated control groups | 24px or at least 2× the inner gap |
| Mobile content margin | 16px |

These are heuristics, not replacements for the project's usable density. Target-size rules still apply and expanded hit areas must not overlap.

Keep content-layout actions inside margins and safe areas. Full-bleed backgrounds and media may reach the viewport edge; text and controls usually remain inset. Sticky and fixed controls account for `env(safe-area-inset-*)`.

## Responsive structure

- Derive breakpoints from where content stops fitting, not from a device-name preset.
- Prefer container queries for reusable components.
- Test the smallest and largest supported sizes first, then intermediate widths.
- Preserve expanded structure until it genuinely breaks; do not collapse early without benefit.
- Use grid and flex layout before JavaScript measurement.
- Keep primary actions reachable when panes resize, keyboards open, or modal content scrolls.

## Content growth

- Avoid fixed widths sized to one language and fixed heights on text containers.
- Let buttons size from their labels; use padding rather than a fixed width.
- Test real content, empty values, long identifiers, dynamic numbers, and pseudo-localized strings.
- Keep flex children shrinkable when text must truncate (`min-width: 0` or the framework equivalent).
- Make tables, code blocks, maps, and other truly two-dimensional content scroll inside their own container instead of forcing page-wide horizontal scrolling.
