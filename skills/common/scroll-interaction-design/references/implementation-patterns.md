# Implementation Patterns

Use this file when writing or revising scroll-linked motion code.

## Platform Choice

| Context | First Choice | Use When |
| --- | --- | --- |
| Simple web reveal/progress/parallax | CSS scroll-driven animations | Browser support is acceptable and effects map cleanly to keyframes |
| Robust reveal-on-enter | IntersectionObserver plus CSS transitions | Needs broad fallback and simple enter/exit states |
| React component motion | Motion for React `useScroll` | Values map to component transforms, opacity, filter, or clip-path |
| Complex art-directed web scenes | GSAP ScrollTrigger | Needs scrubbed timelines, pinning, snapping, sequencing, or complex callbacks |
| Smooth scroll with parallax | Native-scroll-based smoother only | Must preserve focus, anchors, keyboard, and touch expectations |
| Real 3D scene | Three.js | Needs camera/object/shader/particle motion, not just CSS transforms |
| React Native app | Reanimated scroll handlers | Needs UI-thread scroll-linked values and gesture-native feel |

## CSS Scroll-Driven Animation Pattern

Use for simple progress bars, reveal ranges, stacking cards, and parallax when support is acceptable.

```css
@keyframes reveal-up {
  from {
    opacity: 0;
    transform: translateY(32px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.reveal {
  animation: reveal-up 1ms linear both;
  animation-timeline: view();
  animation-range: entry 15% cover 35%;
}

@media (prefers-reduced-motion: reduce) {
  .reveal {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

Rules:

- Declare `animation-timeline` after any `animation` shorthand.
- Use `animation-range` to finish while the element is still visible.
- Use `@supports (animation-timeline: view())` when adding fallbacks.
- Keep keyframes transform/opacity oriented.

## IntersectionObserver Reveal Pattern

Use when compatibility and simplicity matter more than scrubbed progress.

```js
const observer = new IntersectionObserver(
  entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) entry.target.classList.add("is-visible");
    }
  },
  { threshold: 0.2, rootMargin: "0px 0px -10% 0px" }
);

document.querySelectorAll("[data-reveal]").forEach(el => observer.observe(el));
```

```css
[data-reveal] {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 420ms ease, transform 420ms cubic-bezier(.2, 0, 0, 1);
}

[data-reveal].is-visible {
  opacity: 1;
  transform: translateY(0);
}

@media (prefers-reduced-motion: reduce) {
  [data-reveal] {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

## Motion For React Pattern

Use when React composition and scroll progress mapping matter.

```tsx
import { motion, useScroll, useTransform } from "motion/react";
import { useRef } from "react";

export function ScrollPanel() {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"],
  });

  const y = useTransform(scrollYProgress, [0, 1], [80, -80]);
  const opacity = useTransform(scrollYProgress, [0, 0.2, 0.8, 1], [0, 1, 1, 0]);

  return (
    <section ref={ref} className="min-h-[140vh]">
      <motion.div style={{ y, opacity }}>Scroll-linked content</motion.div>
    </section>
  );
}
```

Rules:

- Do not set React state on every scroll frame for visual transforms.
- Map motion values directly to style.
- Prefer transform, opacity, filter, and clip-path.
- Add reduced-motion logic through CSS or platform hooks.

## GSAP ScrollTrigger Pattern

Use for pinned sections, timeline scrubbing, and complex choreography.

```js
gsap.registerPlugin(ScrollTrigger);

const timeline = gsap.timeline({
  scrollTrigger: {
    trigger: ".story",
    start: "top top",
    end: "+=1800",
    scrub: true,
    pin: true,
    anticipatePin: 1,
  },
});

timeline
  .to(".scene-title", { yPercent: -40, opacity: 0 }, 0)
  .fromTo(".product", { rotateY: -18 }, { rotateY: 18, scale: 1.08 }, 0)
  .to(".background", { yPercent: -18 }, 0);
```

Rules:

- One scroll owner per section.
- Pin only containers with clear height and exit behavior.
- Clean up triggers in React component unmounts.
- Avoid smooth-scroll wrappers unless they preserve native scroll behavior.

## Three.js Scroll Scene Pattern

Use for real 3D camera or object movement.

```js
const state = { progress: 0 };

function updateScrollProgress() {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  state.progress = max > 0 ? window.scrollY / max : 0;
}

window.addEventListener("scroll", updateScrollProgress, { passive: true });

renderer.setAnimationLoop(() => {
  const p = state.progress;
  camera.position.z = 6 - p * 2;
  camera.position.y = p * 1.5;
  mesh.rotation.y = p * Math.PI * 2;
  renderer.render(scene, camera);
});
```

Rules:

- Keep scroll event handlers passive and cheap.
- Render through the renderer animation loop.
- Cap pixel ratio on heavy scenes.
- Provide a loading/static fallback.
- Verify canvas is nonblank at desktop and mobile sizes.

## Native App Pattern

Use Reanimated or platform-native APIs for scroll-linked values.

```tsx
const scrollY = useSharedValue(0);

const onScroll = useAnimatedScrollHandler(event => {
  scrollY.value = event.contentOffset.y;
});

const headerStyle = useAnimatedStyle(() => ({
  transform: [{ translateY: interpolate(scrollY.value, [0, 120], [0, -64], Extrapolation.CLAMP) }],
  opacity: interpolate(scrollY.value, [0, 80], [1, 0], Extrapolation.CLAMP),
}));
```

Rules:

- Keep gesture-linked motion on the UI/native animation thread.
- Use clamped interpolation for headers and card depth.
- Respect reduced-motion settings.
- Avoid custom scroll physics unless the product requires it.

## Visual Recipes

- Progress bar: map page scroll progress to `scaleX`.
- Hero depth: slow background y, medium image y, stable text.
- Sticky product reveal: pin section, rotate object 10-25 degrees, swap copy at progress ranges.
- Stacking cards: `position: sticky`, z-index per card, scale previous cards down slightly.
- 3D cover flow: map horizontal or vertical progress to rotation and z-depth.
- Mobile collapsing header: clamp translation and opacity over the first 80-160 px.
