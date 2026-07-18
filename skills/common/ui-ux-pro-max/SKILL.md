---
name: ui-ux-pro-max
description: Search and apply a local UI/UX design-intelligence library with 84 styles, 192 color palettes, 74 font pairings, 99 UX guidelines, 25 chart patterns, 1,923 Google Fonts, 105 icon records, and 22 technology stacks. Use to plan, implement, review, or improve web, mobile, and desktop interfaces, design systems, accessibility, responsive behavior, interaction states, typography, color, charts, and stack-specific UI code.
---

# UI/UX Pro Max

Use the bundled local database to make design choices traceable and project-specific. Inspect the existing product and code before recommending a visual direction.

## Resolve the skill directory

Set skill-dir to the directory containing this SKILL.md. Run scripts by absolute path derived from skill-dir; do not assume a host-specific skills root or current working directory.

Check Python with python --version. If python is unavailable, use the workflow manually from the CSV data and report that script search was unavailable. Do not install runtimes without authorization.

## Core workflow

1. Inspect the product.
   - Identify audience, primary tasks, platform, current stack, brand constraints, and existing design tokens.
   - Preserve established patterns unless the user asks for a redesign.

2. Generate a design direction before implementation.

~~~text
python "<skill-dir>/scripts/search.py" "<product> <industry> <audience> <tone>" --design-system -p "<project>" -f markdown
~~~

Use optional design dials only when the request justifies them:

~~~text
python "<skill-dir>/scripts/search.py" "<query>" --design-system --variance 1-10 --motion 1-10 --density 1-10
~~~

3. Query details as needed.

~~~text
python "<skill-dir>/scripts/search.py" "<query>" --domain style
python "<skill-dir>/scripts/search.py" "<query>" --domain color
python "<skill-dir>/scripts/search.py" "<query>" --domain typography
python "<skill-dir>/scripts/search.py" "<query>" --domain ux
python "<skill-dir>/scripts/search.py" "<query>" --domain chart
python "<skill-dir>/scripts/search.py" "<query>" --stack <stack>
~~~

Supported domains include style, color, chart, landing, product, ux, typography, icons, motion, React performance, web interface, and Google Fonts. Ask the script for available stacks rather than inventing a stack name.

4. Translate recommendations into a coherent system.
   - Define semantic color, type, spacing, radius, elevation, motion, and component-state tokens.
   - Explain why the selected style fits the product and where it should not be used.
   - Prefer one visual language over mixing unrelated fashionable effects.

5. Implement in the project's existing framework.
   - Reuse established components and tokens.
   - Cover default, hover, focus, active, disabled, loading, empty, error, and success states.
   - Keep responsive behavior and keyboard interaction explicit.

6. Validate the result.
   - Check contrast, semantic structure, labels, focus order, reduced motion, zoom, touch targets, and screen-size behavior.
   - Check loading performance, layout shift, image sizing, and unnecessary animation.
   - If visual inspection tools exist, inspect the rendered interface at representative mobile and desktop sizes.

## Persistent design systems

Use --persist only when the user wants durable project files. It writes a master design system and optional page overrides to the selected output directory.

~~~text
python "<skill-dir>/scripts/search.py" "<query>" --design-system --persist -p "<project>" --output-dir "<project-dir>"
python "<skill-dir>/scripts/search.py" "<query>" --design-system --persist -p "<project>" --page "dashboard" --output-dir "<project-dir>"
~~~

Read page overrides before the master when both exist; page rules override only the fields they define.

## Output contract

For design work, provide:

- selected direction and rationale;
- core tokens or implementation changes;
- accessibility and responsive checks;
- alternatives considered and why they lost;
- verification performed and remaining limitations.

## Boundaries

- Do not hardcode a provider, model name, or host-specific path.
- Do not invent database results when the script fails.
- Do not replace existing brand language with generic trends without justification.
- Do not use color alone for meaning or animation without reduced-motion behavior.
- Do not persist files during a read-only review.

See references/provenance.md for the upstream version, commit, licensing, and curated-data changes.
