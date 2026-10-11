---
name: coding-workflow
description: "Software engineering workflow scaled to risk: systematic debugging, implementation plans and architecture, code review and security review, test-driven development, verification before claiming done, git commits, pull requests and GitHub CLI, parallel or sub-agent work, long-task context handoffs and interactive browser debugging. Turkish triggers: hata ayıkla, bug çöz, kodu incele, güvenlik açığı, plan çıkar, mimari, test yaz, commit at, PR aç, kodla, düzelt. More triggers: yazılım fikrini birlikte düşünelim, tasarımı netleştir, bileşenleri ayır, teknik trade-off, kalite sorunlarını bul, merge öncesi kontrol, uzun görevin bağlamını koru, durum özeti ve devir, geliştirme dalını bitir, gh ile kontrol et."
---


## Portable execution

Read [the portable execution adapter](PORTABLE.md) before using host-specific tool examples.

## No-extra-cost execution profile

Use the existing host session and tools, public/open-access sources and local computation. Do not route to separately billed APIs, cloud jobs, credits, subscriptions or paid-trial fallbacks, even if a key or connector exists. Provider examples remain reference material; choose an available no-extra-cost equivalent or name the missing capability. This changes cost routing, not skill features or host permissions.


# Coding Workflow

Engineering discipline scaled to risk. A small reversible change: do it, verify it, report it. A large or risky change: plan first, then implement in small verified steps.

## Choose the module

| Situation | Module |
|---|---|
| Bug, failing test, unexpected behavior | `systematic-debugging` |
| Plan a substantial change | `implementation-plan`; add `architecture-design` for new systems or major boundaries; `ambiguity-detector` for unclear specs |
| Long multi-session plan to write or execute | `writing-plans`, `executing-plans` |
| Shape a vague idea into a design | `brainstorming` — only when the user wants to explore |
| Feature or bugfix where regression risk is real | `test-driven-development` |
| About to say "done", "fixed" or "passing" | `verification-before-completion` (always) |
| Review code, a PR or a diff | `code-review-and-quality`; `security-review` for auth, input handling, secrets, dependencies |
| Acting on review feedback / asking for review | `receiving-code-review`, `requesting-code-review` |
| Commit, PR, GitHub CLI, finishing a branch | `git-commit`, `github-cli-workflows`, `finishing-a-development-branch`; `using-git-worktrees` only when isolation is needed |
| Parallel or multi-agent work | `dispatching-parallel-agents`, `subagent-driven-development`, `task-coordinator` |
| Long task context, handoff, compaction | `context-manager`, `context-engineering` |
| Interactive browser or Electron debugging | `playwright-interactive` |

## Rules that override module defaults

- Follow the repository's conventions and the user's global instructions (AGENTS.md, CLAUDE.md).
- No mandatory interviews, worktrees, commits or approval gates for small reversible work. Ask only questions whose answers change the design.
- Require explicit authority for destructive, irreversible or externally visible actions (force push, publish, delete, deploy); do not re-ask when the exact action is already authorized.
- Never claim tests pass or a bug is fixed without applicable post-change evidence. Reuse valid evidence until relevant state changes; do not rerun per message.
- Base fixes on logs, files and official documentation (Context7 or the vendor docs for library APIs), not guesses.
- Read bundled `modules/<name>/MODULE.md` paths; module names are not separately installed skills or registered slash commands. Discover actual host tools; delegate only when explicitly authorized. Loading a module does not authorize installs, account access, configuration changes, or sandbox weakening.

## Module map

Open only the module(s) the request needs and read the module file completely before acting. Several modules may combine in one task.

| Module | Use when | File |
|---|---|---|
| `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. | [MODULE.md](modules/systematic-debugging/MODULE.md) |
| `implementation-plan` | Produce a decision-complete, repository-grounded implementation plan with scope, architecture, file-level changes, data/API impacts, tests, migration, rollout, rollback,… | [MODULE.md](modules/implementation-plan/MODULE.md) |
| `architecture-design` | System architecture design including requirements analysis, trade-off evaluation, ADRs, and system decomposition. | [MODULE.md](modules/architecture-design/MODULE.md) |
| `ambiguity-detector` | Detect ambiguous, incomplete, or contradictory requirements and specifications with structured clarification templates. | [MODULE.md](modules/ambiguity-detector/MODULE.md) |
| `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code | [MODULE.md](modules/writing-plans/MODULE.md) |
| `executing-plans` | Use when you have a written implementation plan to execute in a separate session with review checkpoints | [MODULE.md](modules/executing-plans/MODULE.md) |
| `brainstorming` | Explicit ideation or collaborative design requests; no prerequisite interview for clear implementation work. | [MODULE.md](modules/brainstorming/MODULE.md) |
| `test-driven-development` | Requested/repository-required test-first work or meaningful behavior regression risk; preserve existing code. | [MODULE.md](modules/test-driven-development/MODULE.md) |
| `verification-before-completion` | Support completion claims with valid post-change evidence sized to the change. | [MODULE.md](modules/verification-before-completion/MODULE.md) |
| `code-review-and-quality` | Requested/risk-appropriate review; material in-scope defects, optional unrelated cleanup. | [MODULE.md](modules/code-review-and-quality/MODULE.md) |
| `security-review` | Identify security vulnerabilities across 10 domains including OWASP Top 10, race conditions, supply chain risks, and compliance gaps. | [MODULE.md](modules/security-review/MODULE.md) |
| `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and… | [MODULE.md](modules/receiving-code-review/MODULE.md) |
| `requesting-code-review` | Focused review using the real base and complete task diff, including uncommitted work. | [MODULE.md](modules/requesting-code-review/MODULE.md) |
| `git-commit` | Requested commits/messages following repository convention and explicit-path staging. | [MODULE.md](modules/git-commit/MODULE.md) |
| `github-cli-workflows` | Explicit `gh`/CLI workflow requests with an already available CLI. | [MODULE.md](modules/github-cli-workflows/MODULE.md) |
| `finishing-a-development-branch` | Requested/relevant integration; capture original workspace identity and ownership before any switch or cleanup. | [MODULE.md](modules/finishing-a-development-branch/MODULE.md) |
| `using-git-worktrees` | Requested or genuinely useful isolation; exact-path checks, no automatic installs or commits. | [MODULE.md](modules/using-git-worktrees/MODULE.md) |
| `dispatching-parallel-agents` | Partition and coordinate two or more independent workstreams without duplicating work, leaking expected conclusions, or creating shared-file conflicts. | [MODULE.md](modules/dispatching-parallel-agents/MODULE.md) |
| `subagent-driven-development` | Execute an implementation plan through bounded implementer and independent reviewer agents with disjoint write ownership, explicit handoffs, evidence gates, and integrat… | [MODULE.md](modules/subagent-driven-development/MODULE.md) |
| `task-coordinator` | Coordinate complex multi-step tasks by breaking them down into manageable subtasks with dependency tracking. | [MODULE.md](modules/task-coordinator/MODULE.md) |
| `context-manager` | Keep long tasks accurate by tracking goals, constraints, decisions, evidence, artifacts, unresolved questions, and context budget through progressive disclosure and veri… | [MODULE.md](modules/context-manager/MODULE.md) |
| `context-engineering` | Optimizes agent context setup. | [MODULE.md](modules/context-engineering/MODULE.md) |
| `playwright-interactive` | Host-native browser/Electron debugging with explicit target IDs; optional Codex runtime recipes only on a compatible host. | [MODULE.md](modules/playwright-interactive/MODULE.md) |

Supporting files (open only when the module points to them):

- `systematic-debugging`: [condition-based-waiting.md](modules/systematic-debugging/condition-based-waiting.md), [defense-in-depth.md](modules/systematic-debugging/defense-in-depth.md), [root-cause-tracing.md](modules/systematic-debugging/root-cause-tracing.md)
- `architecture-design`: [adr-guidance.md](modules/architecture-design/references/adr-guidance.md), [common-patterns.md](modules/architecture-design/references/common-patterns.md), [fitness-functions.md](modules/architecture-design/references/fitness-functions.md)
- `writing-plans`: [plan-document-reviewer-prompt.md](modules/writing-plans/plan-document-reviewer-prompt.md)
- `test-driven-development`: [testing-anti-patterns.md](modules/test-driven-development/testing-anti-patterns.md)
- `requesting-code-review`: [code-reviewer.md](modules/requesting-code-review/code-reviewer.md)
- `subagent-driven-development`: [review-handoff.md](modules/subagent-driven-development/references/review-handoff.md)
