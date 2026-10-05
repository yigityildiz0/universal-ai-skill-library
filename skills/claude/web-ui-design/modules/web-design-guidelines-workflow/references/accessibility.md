# Accessibility

Use WCAG 2.2 AA as the standards baseline when mapping criteria. Review the actual interaction, not only markup or an automated scan.

## Review order

1. Complete the primary flow with keyboard only.
2. Inspect each control's accessible name, role, state, and relationship.
3. Check focus order, visibility, trapping, and restoration.
4. Exercise forms, errors, dynamic updates, loading, and overlays.
5. Test zoom, reflow, reduced motion, target size, and forced-colors behavior as applicable.

## Native semantics first

- Use `<button>` for actions and `<a href>` for navigation. Never use a clickable `<div>` when a native element fits.
- Prefer native `<dialog>` with `showModal()` when it meets the product need.
- Use one visible primary `<main>`. Label repeated landmarks such as multiple navigation regions.
- Choose heading elements from document structure, then style them visually.
- A role is a promise: custom tabs, menus, listboxes, dialogs, and comboboxes must implement the matching ARIA Authoring Practices keyboard model.
- No ARIA is better than incorrect ARIA. Never hide a focusable element with `aria-hidden="true"`.

## Focus and keyboard

- Preserve the browser focus indicator when possible. If customizing it, use `:focus-visible`, at least a clearly visible 2px-equivalent perimeter, offset it from the control, and verify it against every adjacent color and in forced-colors mode.
- Never remove an outline without a verified replacement.
- Use `:focus-within` for compound controls when the wrapper needs a focus state.
- Use `tabindex="0"` only to join natural order and `tabindex="-1"` for programmatic focus. Never use positive values.
- Composite widgets use roving tabindex: one active item at `0`, peers at `-1`; arrow keys move inside the widget and Tab leaves it.
- Escape closes the most recently opened transient layer. Enter and Space activate buttons; Enter activates links.
- When repeated chrome precedes content, make a skip link the first focusable element and add `scroll-margin-top` to anchored headings below sticky chrome.

## Dialogs and route changes

- On modal open, make the background inert and focus the first meaningful control. For destructive confirmation, initially focus the least destructive action.
- Trap focus inside; Escape closes; closing returns focus to the trigger or the nearest logical successor.
- Add `overscroll-behavior: contain` to overlays that scroll.
- On client-side route changes, update the page title and move focus to the new heading or main region. Restore scroll on back/forward and use the product convention for forward navigation.

## Forms

- Every control has a programmatic and preferably visible label. A placeholder is an example, never the only label.
- Labels and checkbox/radio controls share one hit target with no dead zone.
- Add meaningful `name`, `autocomplete`, correct `type`, and `inputmode`. Do not block paste or fight password managers and one-time-code autofill.
- Keep submit available until the request starts. During submission, retain the action label, show progress, and prevent duplicate requests.
- Validate on submit, mark fields with `aria-invalid`, connect inline errors with `aria-describedby`, and focus the first invalid field.
- Errors include a recovery action and never rely on a red border alone.
- Use native `disabled` when a control is truly unavailable. Use `aria-disabled` only when retaining focusability is intentional, and then block activation in code and explain why it is unavailable.

## Accessible names and media

- Icon-only controls need a concise action or destination name. Hide decorative icons from assistive technology.
- The visible label must be contained in the accessible name so voice-control commands work.
- Decorative images use `alt=""`; informative images describe the meaning they add; functional images describe the action. Complex charts need a short alternative plus nearby text or data.
- Meaningful inline SVG uses `role="img"` with a name; decorative SVG uses `aria-hidden="true"` and is not focusable.
- Prerecorded video needs captions; audio needs an equivalent transcript. Never autoplay sound.

## Dynamic updates

Choose the first applicable announcement:

1. Focus already moves to the new content: no extra live announcement.
2. The update belongs to a control: connect it with `aria-describedby`.
3. Non-urgent independent update: use a stable polite status region.
4. Urgent independent error: use an alert sparingly.

Keep polite live regions in the DOM before updating their text. Do not move focus to a toast. Errors, undo actions, and other actionable information must not disappear on a short timer.

## Target size, zoom, and motion

- WCAG 2.5.8 AA uses a 24×24 CSS-pixel baseline with defined exceptions. Aim around 44×44 in touch contexts and 40×40 in desktop interfaces when density allows.
- The visible glyph may stay smaller if a non-overlapping pseudo-element or wrapper expands the hit area.
- Never allow adjacent expanded hit areas to overlap.
- Support 200% text zoom and reflow at 320 CSS pixels without two-dimensional page scrolling except for genuinely two-dimensional content.
- Avoid fixed heights on text containers. Never disable pinch zoom.
- Make motion opt-in with `prefers-reduced-motion: no-preference` when practical. Under reduced motion, remove parallax and autoplay, replace large movement with a subtle crossfade, and keep functional state feedback.
- Moving or updating content lasting more than five seconds needs a visible pause or stop mechanism when the applicable WCAG rule requires it.

## Evidence limits

- Automated tools catch only a subset of issues and do not prove conformance.
- A screenshot cannot prove semantics, keyboard order, announcements, or screen-reader output.
- Code inspection cannot prove final contrast over composited backgrounds, visible focus in every state, or assistive-technology interoperability.
