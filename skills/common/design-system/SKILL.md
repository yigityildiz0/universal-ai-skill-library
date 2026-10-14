---
name: design-system
description: "Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strategic slide creation. Use for design tokens, systematic design, brand-compliant presentations. Turkish triggers: design system kur, token ve bileşenler, varyant ve tema, tasarım tokenları, marka uyumlu sunum."
license: MIT
metadata:
  author: claudekit
  version: "1.0.0"
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# Design System

Token architecture, component specifications, systematic design, slide generation.

## When to Use

- Design token creation
- Component state definitions
- CSS variable systems
- Spacing/typography scales
- Design-to-code handoff
- Tailwind theme configuration
- **Slide/presentation generation**

## Token Architecture

Load: `references/token-architecture.md`

### Three-Layer Structure

```
Primitive (raw values)
       ↓
Semantic (purpose aliases)
       ↓
Component (component-specific)
```

**Example:**
```css
/* Primitive */
--color-blue-600: #2563EB;

/* Semantic */
--color-primary: var(--color-blue-600);

/* Component */
--button-bg: var(--color-primary);
```

## Script Paths

Script paths in this skill and its `references/` are relative to the directory that contains this SKILL.md, not to the project: `scripts/<file>` is this skill's own `scripts/` folder, and `../<skill>/scripts/<file>` is a sibling sub-skill installed alongside it. Build the full path from that directory (Claude Code reports it as the skill's base directory when the skill loads) and keep the working directory at the project root — the scripts read and write project files such as `docs/brand-guidelines.md`, `assets/design-tokens.json` or `src/` relative to it.

## Quick Start

**Generate tokens:**
```bash
node scripts/generate-tokens.cjs --config tokens.json -o tokens.css
```

**Validate usage:**
```bash
node scripts/validate-tokens.cjs --dir src/
```

## References

| Topic | File |
|-------|------|
| Token Architecture | `references/token-architecture.md` |
| Primitive Tokens | `references/primitive-tokens.md` |
| Semantic Tokens | `references/semantic-tokens.md` |
| Component Tokens | `references/component-tokens.md` |
| Component Specs | `references/component-specs.md` |
| States & Variants | `references/states-and-variants.md` |
| Tailwind Integration | `references/tailwind-integration.md` |

## Component Spec Pattern

| Property | Default | Hover | Active | Disabled |
|----------|---------|-------|--------|----------|
| Background | primary | primary-dark | primary-darker | muted |
| Text | white | white | white | muted-fg |
| Border | none | none | none | muted-border |
| Shadow | sm | md | none | none |

## Scripts

| Script | Purpose |
|--------|---------|
| `generate-tokens.cjs` | Generate CSS from JSON token config |
| `validate-tokens.cjs` | Check for hardcoded values in code |
| `search-slides.py` | BM25 search + contextual recommendations |
| `slide-token-validator.py` | Validate slide HTML for token compliance |
| `fetch-background.py` | Fetch images from Pexels/Unsplash |

## Templates

| Template | Purpose |
|----------|---------|
| `design-tokens-starter.json` | Starter JSON with three-layer structure |

## Integration

**With brand:** Extract primitives from brand colors/typography
**With ui-styling:** Component tokens → Tailwind config

**Skill Dependencies:** brand, ui-styling
**Primary Agents:** ui-ux-designer, frontend-developer

## Slide System

Brand-compliant HTML presentations using design tokens + Chart.js + contextual decision system. For a full HTML deck workflow use `html-slides`. Every editable PowerPoint/PPTX deck goes to `presentation-studio` (never an HTML rename). Academic/FTR argument comes from `academic-study-coach`; tokens can support the approved visual direction.

### Source of Truth

| File | Purpose |
|------|---------|
| `docs/brand-guidelines.md` | Brand identity, voice, colors |
| `assets/design-tokens.json` | Token definitions (primitive→semantic→component) |
| `assets/design-tokens.css` | CSS variables (import in slides) |
| `assets/css/slide-animations.css` | CSS animation library |

### Slide Search (BM25)

```bash
# Basic search (auto-detect domain)
python scripts/search-slides.py "investor pitch"

# Domain-specific search
python scripts/search-slides.py "problem agitation" -d copy
python scripts/search-slides.py "revenue growth" -d chart

# Contextual search (Premium System)
python scripts/search-slides.py "problem slide" --context --position 2 --total 9
python scripts/search-slides.py "cta" --context --position 9 --prev-emotion frustration
```

### Decision System CSVs

| File | Purpose |
|------|---------|
| `data/slide-strategies.csv` | 15 deck structures + emotion arcs + sparkline beats |
| `data/slide-layouts.csv` | 25 layouts + component variants + animations |
| `data/slide-layout-logic.csv` | Goal → Layout + break_pattern flag |
| `data/slide-typography.csv` | Content type → Typography scale |
| `data/slide-color-logic.csv` | Emotion → Color treatment |
| `data/slide-backgrounds.csv` | Slide type → Image category (Pexels/Unsplash) |
| `data/slide-copy.csv` | 25 copywriting formulas (PAS, AIDA, FAB) |
| `data/slide-charts.csv` | 25 chart types with Chart.js config |

### Contextual Decision Flow

```
1. Parse goal/context
        ↓
2. Search slide-strategies.csv → Get strategy + emotion beats
        ↓
3. For each slide:
   a. Query slide-layout-logic.csv → layout + break_pattern
   b. Query slide-typography.csv → type scale
   c. Query slide-color-logic.csv → color treatment
   d. Query slide-backgrounds.csv → image if needed
   e. Apply animation class from slide-animations.css
        ↓
4. Generate HTML with design tokens
        ↓
5. Validate with slide-token-validator.py
```

### Pattern Breaking (Duarte Sparkline)

Premium decks alternate between emotions for engagement:
```
"What Is" (frustration) ↔ "What Could Be" (hope)
```

System calculates pattern breaks at 1/3 and 2/3 positions.

### Slide Requirements

Choose the format and audience; all three modes remain supported:

- **HTML marketing/pitch:** import the project’s actual token stylesheet, use its CSS variables, and include keyboard/click navigation and progress. Chart.js remains available when it fits the existing stack. Centering and persuasion are composition choices, not universal requirements.
- **Academic/clinical/data-heavy:** prioritize methods, uncertainty, readable tables, axis units, sample size, confidence intervals and claim-adjacent sources. Use left-aligned reading blocks when clearer; no forced conversion narrative. Coordinate the outline with `academic-study-coach`.
- **Editable PPTX:** use a native presentation-capable tool and map semantic tokens to theme colors/fonts. HTML, screenshots and PDF are not editable PPTX. This mode does not require CSS or Chart.js.

### Chart.js Integration

```html
<!-- Load the project’s existing Chart.js bundle first; this example assumes global Chart. -->
<canvas id="revenueChart" role="img" aria-label="Illustrative series: Sep 5, Oct 12, Nov 28, Dec 45"
        style="color: var(--color-primary)">Illustrative values, not observed revenue.</canvas>
<script>
const canvas = document.getElementById('revenueChart');
// Resolve the actual theme color; canvas does not interpret CSS var() strings.
const seriesColor = getComputedStyle(canvas).color;
new Chart(canvas, {
    type: 'line',
    data: {
        labels: ['Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            data: [5, 12, 28, 45],
            label: 'Illustrative values',
            borderColor: seriesColor,
            backgroundColor: seriesColor,
            fill: false,
            tension: 0
        }]
    }
});
</script>
```

For real data, include units, source, date and an accessible data table. Refresh resolved colors when the theme changes. See [Chart.js colors](https://www.chartjs.org/docs/latest/general/colors.html).

### Token Compliance

```css
/* CORRECT - uses token */
background: var(--slide-bg);
color: var(--color-primary);
font-family: var(--typography-font-heading);

/* WRONG - hardcoded */
background: #0D0D0D;
color: #FF6B6B;
font-family: 'Space Grotesk';
```

### Reference Implementation

Working example with all features:
```
assets/designs/slides/claudekit-pitch-251223.html
```

### Command

```bash
/slides:create "10-slide investor pitch for ClaudeKit Marketing"
```

## Best Practices

1. Never use raw hex in components - always reference tokens
2. Semantic layer enables theme switching (light/dark)
3. Component tokens enable per-component customization
4. Use HSL format for opacity control
5. Document every token's purpose
6. **HTML slides reuse the project token stylesheet; native slides map the same semantic roles to the presentation theme.**

## the user's working rules (added)

The upstream design workflow is retained with local slide-format and token-example corrections. the user's earlier customized workflow for this skill is kept in [yigit/YIGIT-WORKFLOW.md](yigit/YIGIT-WORKFLOW.md). Read it as well; where it is stricter (keep the existing stack, no new dependencies, verify accessibility and the rendered result, preserve brand assets), follow it. Otherwise the upstream instructions apply.
