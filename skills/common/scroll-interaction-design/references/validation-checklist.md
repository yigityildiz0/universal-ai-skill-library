# Validation Checklist

Run this before finishing scroll or motion work.

## Visual

- Text does not overlap, clip, or become unreadable during scroll.
- Pinned sections enter, hold, and exit cleanly.
- Parallax layers preserve hierarchy instead of distracting from content.
- The animation completes at common viewport heights.
- Mobile does not feel trapped, rubber-banded, or disconnected from finger movement.
- 3D/canvas content is nonblank and framed correctly.

## Performance

- Scroll handlers are passive and cheap.
- Visual animation avoids layout properties where transforms work.
- No React state updates on every scroll frame for visual values.
- Heavy assets are lazy-loaded or compressed.
- Canvas pixel ratio is capped when needed.
- DevTools or browser testing shows no obvious jank on normal hardware.

## Accessibility

- Reduced motion disables or simplifies large motion.
- Keyboard focus remains visible and reaches all interactive controls.
- Anchor links and focus scrolling still work.
- Motion is not the only way to understand progress or state.
- Smooth scrolling does not replace native scrolling with inaccessible fake scrollbars.

## Responsive

- Desktop, tablet, and mobile breakpoints have distinct scroll distances when needed.
- Sticky and pinned sections account for browser UI height on mobile.
- Images and 3D scenes maintain aspect ratio.
- Long words and labels fit inside controls while animated.

## Shipping

- Browser or app preview was run when possible.
- If using GSAP, ScrollTrigger instances are cleaned up in component lifecycles.
- If using Three.js, resize handling and cleanup are present.
- If using native apps, scroll handlers run on the animation/UI thread.
- The final implementation includes a static or low-motion fallback.
