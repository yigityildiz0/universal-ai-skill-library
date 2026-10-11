# mental-health-crisis-support

[English](mental-health-crisis-support.en.md) · [Türkçe](mental-health-crisis-support.tr.md) · [Library](../../README.md)

**Support a calm, safety-oriented response to mental-health crisis signals.**

## Try it

> Help me respond supportively to someone who may be in immediate danger.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Immediate, supportive, safety-first response when the user or someone else may be at risk of suicide or serious self-harm: wanting to die, a plan or means, or how to help someone in crisis. Turkish triggers: kendimi öldürmek, yaşamak istemiyorum, canıma kıymak, intihar düşüncesi/planı, kendine zarar, arkadaşım intihar edecek. Checks imminent danger and connects to local emergency and crisis help (Türkiye: 112).

</details>

## How it works

Prioritize immediate safety and direct communication; establish location when resources matter; offer appropriate human support without pretending to diagnose.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/mental-health-crisis-support/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Standalone root workflow; references are linked by the entry point.
