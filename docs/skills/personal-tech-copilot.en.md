# personal-tech-copilot

[English](personal-tech-copilot.en.md) · [Türkçe](personal-tech-copilot.tr.md) · [Library](../../README.md)

**Troubleshoot everyday devices, apps and setup using the tools actually available.**

## Try it

> Diagnose why this Windows application fails to start.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Personal technology help: diagnoses and fixes Windows, macOS, Android and iPhone problems, apps, device setup, compatibility, networking, displays, peripherals, storage, backups and cross-device workflows; read-only PC health checks for slow computers (disk, RAM, CPU, startup); tech purchase compatibility; read-only Harness/DSH GUI health checks. Turkish triggers: nasıl yaparım, neden çalışmıyor, hata veriyor, bilgisayar yavaş, kurulum, ayar, uyumlu mu, telefon veya PC sorunu. More triggers: disk dolu, RAM, başlangıç programları, Wi-Fi, yazıcı, yedekleme, Harness sağlık kontrolü, DSH araç eksik.

</details>

## How it works

Inspect symptoms and environment; narrow likely causes; propose or perform scoped repairs; verify the observed result.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/personal-tech-copilot/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [computer-health-check](../../skills/common/personal-tech-copilot/modules/computer-health-check/MODULE.md) | Perform a bounded, read-only health check of a Windows, macOS, or Linux computer, covering storage, memory pressure, CPU activity, startup load, battery where available, updates, a |
| [harness-health-check](../../skills/common/personal-tech-copilot/modules/harness-health-check/MODULE.md) | harness health check |
