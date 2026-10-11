# web-animation

[English](web-animation.en.md) · [Türkçe](web-animation.tr.md) · [Library](../../README.md)

**Apply GSAP/Motion patterns while preserving accessibility and existing integrations.**

## Try it

> Add a restrained scroll reveal that respects reduced motion.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Scroll and web animation: GSAP ScrollTrigger and Framer Motion/Motion v12 recipes (scroll-triggered reveals, parallax, pinned sections, horizontal scroll, text animations, useScroll/whileInView), plus GSAP timelines/SplitText/Flip/Lenis, 60fps performance, accessible motion, micro-interactions, page transitions, SVG, Lottie. Upstream github/awesome-copilot gsap-framer-scroll-animation + iart-ai/web-animation-skills. Turkish triggers: scroll animasyonu, kaydırınca animasyon, parallax, sabitlenen bölüm, yatay kaydırma, sayfa geçişi, mikro etkileşim, GSAP, Framer Motion, akıcı animasyon.

</details>

## How it works

Inspect installed animation tooling; choose a suitable recipe; integrate with the current UI; assess motion preference and performance.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/web-animation/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [60fps-animation](../../skills/common/web-animation/modules/60fps-animation/MODULE.md) | This skill should be used when the user asks to "fix janky CSS animation", "make animation 60fps", "stop layout thrashing", "animate width/height/top/left smoothly", "convert anima |
| [accessible-animation](../../skills/common/web-animation/modules/accessible-animation/MODULE.md) | This skill should be used when the user asks to "respect prefers-reduced-motion", "honor reduced motion", "make my animations accessible", "fix vestibular / motion-sickness issues" |
| [ascii-animation](../../skills/common/web-animation/modules/ascii-animation/MODULE.md) | This skill should be used when the user asks to "make an ASCII animation", "build a terminal/CLI intro or loader", "convert an image or video to ASCII art", "add an ASCII shader/po |
| [glassmorphism](../../skills/common/web-animation/modules/glassmorphism/MODULE.md) | This skill should be used when the user asks to "add a glassmorphism effect", "frosted glass UI", "Apple liquid glass style", "frosted blur card", "translucent glass panel animatio |
| [gsap-web](../../skills/common/web-animation/modules/gsap-web/MODULE.md) | This skill should be used when the user asks to "build a scroll animation", "add ScrollTrigger", "pin a section while scrolling", "scrub an animation to scroll", "create a hero tim |
| [lottie-animation](../../skills/common/web-animation/modules/lottie-animation/MODULE.md) | This skill should be used when the user asks to "add a Lottie animation", "play a .lottie or .json animation", "integrate a Bodymovin/After Effects animation on web or mobile", "co |
| [micro-interaction](../../skills/common/web-animation/modules/micro-interaction/MODULE.md) | This skill should be used when the user asks to "add a hover/press effect", "animate a toggle or switch", "build an animated like button", "make a toast/snackbar slide in", "animat |
| [page-transition-animation](../../skills/common/web-animation/modules/page-transition-animation/MODULE.md) | This skill should be used when the user asks to "animate page or route transitions", "add a page transition or crossfade between views", "animate route changes in Next.js App Route |
| [svg-animation](../../skills/common/web-animation/modules/svg-animation/MODULE.md) | This skill should be used when the user asks to "animate an SVG", "make a line draw itself on", "do a stroke draw-on / signature animation", "morph one shape into another", "move a |
