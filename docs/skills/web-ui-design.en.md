# web-ui-design

[English](web-ui-design.en.md) · [Türkçe](web-ui-design.tr.md) · [Library](../../README.md)

**Design interfaces around real tasks, hierarchy, responsiveness and accessibility.**

## Try it

> Redesign this settings page so the primary action is clear on small screens.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Designs, builds and reviews web and app interfaces: distinctive visual direction (frontend-design), layout, spacing and typography polish per web design guidelines, screenshot-to-code, UX microcopy, accessibility (WCAG) audits, real-browser testing and developer handoff. Styles/palettes/fonts → ui-ux-pro-max; tokens → design-system; Tailwind/shadcn → ui-styling. Turkish triggers: site tasarla, arayüzü güzelleştir, tasarım dengesiz/yamuk, responsive yap, ekran görüntüsünü koda çevir, erişilebilirlik, buton metni, tarayıcıda test et. More triggers: geliştiriciye devret, ölçü ve durumlar, acceptance criteria, UI polish.

</details>

## How it works

Understand user tasks; prioritize information/actions; design states/layout; review keyboard, contrast and responsive behavior.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/web-ui-design/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [accessibility-review](../../skills/common/web-ui-design/modules/accessibility-review/MODULE.md) | Audit a web, mobile, desktop, document, or product flow for practical accessibility issues using current WCAG 2.2 AA-oriented checks, code, screenshots, and interaction evidence. U |
| [browser-testing-with-devtools](../../skills/common/web-ui-design/modules/browser-testing-with-devtools/MODULE.md) | Test and debug web interfaces in a real browser using whatever browser, DevTools, Playwright, or computer-use capability is already available. Use for DOM, console, network, access |
| [design-handoff](../../skills/common/web-ui-design/modules/design-handoff/MODULE.md) | Create or review a design-to-engineering handoff with intent, responsive behavior, tokens, states, interaction rules, edge cases, assets, acceptance criteria, and open decisions. U |
| [frontend-design](../../skills/common/web-ui-design/modules/frontend-design/MODULE.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't rea |
| [ux-copy](../../skills/common/web-ui-design/modules/ux-copy/MODULE.md) | Write or review interface copy for labels, buttons, onboarding, forms, empty states, errors, confirmations, permissions, and help text. Use for UX copy, microcopy, button text, err |
| [visual-reference-to-code](../../skills/common/web-ui-design/modules/visual-reference-to-code/MODULE.md) | Turn a screenshot, generated design reference, or visual brief into a polished responsive interface through measurable visual analysis, implementation, and screenshot comparison. U |
| [web-design-guidelines-workflow](../../skills/common/web-ui-design/modules/web-design-guidelines-workflow/MODULE.md) | Build, improve, or review web and product interfaces as one coherent system across layout and optical balance, accessibility, UX writing, typography, color, surfaces, icons, motion |
