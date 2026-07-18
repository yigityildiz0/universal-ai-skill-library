# Research Basis

This reference records the implementation basis used by the skill. Use it when explaining choices or updating the skill.

## Sources Checked

- MDN CSS scroll-driven animation timelines: https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines
- Chrome for Developers scroll-driven animations: https://developer.chrome.com/docs/css-ui/scroll-driven-animations
- Motion for React `useScroll`: https://motion.dev/docs/react-use-scroll
- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- GSAP ScrollSmoother: https://gsap.com/docs/v3/Plugins/ScrollSmoother/
- Three.js WebGLRenderer: https://threejs.org/docs/pages/WebGLRenderer.html
- React Native Reanimated `useAnimatedScrollHandler`: https://docs.swmansion.com/react-native-reanimated/docs/scroll/useAnimatedScrollHandler/
- MDN `prefers-reduced-motion`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion
- Apple Human Interface Guidelines, Motion: https://developer.apple.com/design/human-interface-guidelines/motion

## Key Findings

- Scroll-driven CSS links animation progress directly to scroll progress or element visibility.
- CSS scroll animations need `animation-timeline` declared after `animation` shorthand.
- View timelines should often finish before the element leaves the viewport; use animation ranges intentionally.
- Main-thread scroll event animation can jank; prefer declarative timelines, motion values, or UI-thread/native animation systems.
- Motion for React maps `scrollYProgress` through motion values and can keep transform-like properties hardware accelerated.
- GSAP ScrollTrigger is appropriate for complex scrubbed and pinned timelines; ScrollSmoother emphasizes native scroll behavior.
- Three.js recommends renderer-managed animation loops for compatibility.
- React Native Reanimated scroll handlers connect scrollable components to UI-thread shared values.
- Reduced motion is mandatory for large scroll, scale, camera, and parallax effects.

## Skill Design Implications

- The skill should choose the simplest mechanism that satisfies the desired interaction.
- It should require a motion map before implementation for complex sequences.
- It should separate layout, progress measurement, animation mapping, and validation.
- It should always include reduced-motion behavior and runtime visual checks.
