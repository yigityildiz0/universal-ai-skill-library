# caveman

[English](caveman.en.md) · [Türkçe](caveman.tr.md) · [Library](../../README.md)

**Use official Caveman, Ultracave and Megacave modes for concise communication.**

## Try it

> /caveman ultra

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

Caveman requires explicit activation; Ultra loads the Ultracave module. A status query is not activation.

<details>
<summary>Exact source description</summary>

Official Caveman voice and companions: Caveman, Ultra/Ultracave, Wenyan/Megacave, commit, review, compress and code-work patterns. Activate on /caveman, /ultracave, /megacave or explicit Caveman mode request. TR: Caveman modunu aç, Caveman Ultra. Status/audit mentions do not activate it.

</details>

## How it works

Require explicit mode activation; load only that upstream mode; preserve facts/code; keep status and deactivation honest.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/caveman/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [cavecrew](../../skills/common/caveman/modules/cavecrew/MODULE.md) | cavecrew |
| [caveman](../../skills/common/caveman/modules/caveman/MODULE.md) | caveman |
| [caveman-commit](../../skills/common/caveman/modules/caveman-commit/MODULE.md) | caveman commit |
| [caveman-compress](../../skills/common/caveman/modules/caveman-compress/MODULE.md) | caveman compress |
| [caveman-discover](../../skills/common/caveman/modules/caveman-discover/MODULE.md) | caveman discover |
| [caveman-evidence-review](../../skills/common/caveman/modules/caveman-evidence-review/MODULE.md) | caveman evidence review |
| [caveman-explore](../../skills/common/caveman/modules/caveman-explore/MODULE.md) | caveman explore |
| [caveman-help](../../skills/common/caveman/modules/caveman-help/MODULE.md) | caveman help |
| [caveman-learn](../../skills/common/caveman/modules/caveman-learn/MODULE.md) | caveman learn |
| [caveman-manage](../../skills/common/caveman/modules/caveman-manage/MODULE.md) | caveman manage |
| [caveman-optimize](../../skills/common/caveman/modules/caveman-optimize/MODULE.md) | caveman optimize |
| [caveman-review](../../skills/common/caveman/modules/caveman-review/MODULE.md) | caveman review |
| [caveman-setup](../../skills/common/caveman/modules/caveman-setup/MODULE.md) | caveman setup |
| [caveman-stats](../../skills/common/caveman/modules/caveman-stats/MODULE.md) | caveman stats |
| [investigate-first](../../skills/common/caveman/modules/investigate-first/MODULE.md) | investigate first |
| [lean-build](../../skills/common/caveman/modules/lean-build/MODULE.md) | lean build |
| [megacave](../../skills/common/caveman/modules/megacave/MODULE.md) | megacave |
| [migration](../../skills/common/caveman/modules/migration/MODULE.md) | migration |
| [safe-refactor](../../skills/common/caveman/modules/safe-refactor/MODULE.md) | safe refactor |
| [surgical-patch](../../skills/common/caveman/modules/surgical-patch/MODULE.md) | surgical patch |
| [ultracave](../../skills/common/caveman/modules/ultracave/MODULE.md) | ultracave |
| [verify-and-stop](../../skills/common/caveman/modules/verify-and-stop/MODULE.md) | verify and stop |
