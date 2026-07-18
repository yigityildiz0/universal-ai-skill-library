---
name: caveman-help
description: "One-shot reference card for this plugin's Caveman levels and companion skills. Use only when the user explicitly invokes $caveman-help or asks how to use the Caveman skill family. Do not activate a mode or change files."
---

# Caveman Help

Return a compact reference card. Do not activate a mode, create state, or
promise environment-variable, hook, status-line, or config-file behavior.

## Modes

| Request | Result |
|---|---|
| `$caveman lite` | Tight, complete sentences. |
| `$caveman` or `$caveman full` | Clear fragments; all facts retained. |
| `$caveman ultra` | Minimum unambiguous wording. |
| `$caveman wenyan-lite` | Light classical-Chinese register. |
| `$caveman wenyan-full` | Compact classical-Chinese register. |
| `$caveman wenyan-ultra` | Maximum safe classical compression. |
| `normal mode` or `stop caveman` | Return to normal prose. |

## Companion skills

| Skill | Invocation | Purpose |
|---|---|---|
| `caveman-commit` | `$caveman-commit` | Draft a terse Conventional Commit message. |
| `caveman-review` | `$caveman-review` | Produce concise, evidence-backed review findings. |
| `caveman-compress` | `$caveman-compress` | Build and validate a preview before changing a text file. |
| `caveman-help` | `$caveman-help` | Show this one-shot card. |

Only `caveman` may be inferred from explicit Caveman wording. Companion skills
are manual to prevent collisions with general commit, review, and compression
skills.
