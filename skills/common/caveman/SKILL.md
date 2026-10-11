---
name: caveman
description: "Official Caveman voice and companions: Caveman, Ultra/Ultracave, Wenyan/Megacave, commit, review, compress and code-work patterns. Activate on /caveman, /ultracave, /megacave or explicit Caveman mode request. TR: Caveman modunu aç, Caveman Ultra. Status/audit mentions do not activate it."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

# Caveman — official modes, portable routing

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.

Load only the requested mode, then follow its complete upstream text:

- `/caveman`, `lite`, `full`: [Caveman](modules/caveman/MODULE.md).
- `/caveman ultra`, `/ultracave`: [Ultracave](modules/ultracave/MODULE.md).
- `/caveman wenyan`, legacy `wenyan-*`, `/megacave`: [Megacave](modules/megacave/MODULE.md). An explicit Turkish reply-language request still wins.
- `off`, “stop caveman”, “normal mode”: return to normal prose.
- `status`: report the mode actually followed; without a hook say “not tracked by this host”. Do not activate or invent persisted state.

Use explicit activation as in the existing Yiğit edition; merely auditing the skill or asking for a short reply is not activation. Keep technical facts, code, negation, numbers, units and the user’s language. Preserve [Yiğit clarity guidance](yigit/YIGIT-WORKFLOW.md), especially medical/financial and irreversible-action clarity. Skill loading changes neither host permissions nor model/tool availability.

## Companions

Named companion requests load `modules/<name>/MODULE.md`: `caveman-commit`, `caveman-review`, `caveman-compress`, `caveman-help`, `caveman-stats`, `cavecrew`, `investigate-first`, `lean-build`, `surgical-patch`, `safe-refactor`, `migration`, `verify-and-stop`. Their full upstream files, assets and Yiğit editions remain bundled. Resolve upstream sibling-skill examples to these module paths.

Engine/Cloud companions also remain documented: `caveman-setup`, `caveman-discover`, `caveman-learn`, `caveman-manage`, `caveman-optimize`, `caveman-explore`, `caveman-evidence-review`. Do not start a separately billed provider/gateway call under the no-extra-cost profile. If a companion needs that service, use an existing host/local equivalent or explain the missing runtime. For compression, the host can perform the prose transformation and local validation without a new paid API. No hooks, proxy, CLI or plugin are installed by this skill update.

## Provenance

Official [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman/tree/2e08b9177c07bb7249a8a2d1a6758e5db281d002), checked 2026-10-11. Modes are now separate upstream skills: the older local multi-level prose has been replaced by the official on-demand mode texts, not silently shortened. Legacy aliases remain available. No token-saving percentage or quality equivalence is claimed without a measured comparison. Current upstream Apache-2.0 license and NOTICE accompany the imported files; earlier local MIT license and Yiğit files are retained.
