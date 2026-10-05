# Claude-to-Codex Mapping

Use this when a user provides Claude Code agent-kit material and wants it configured for Codex.

## Component Map

| Claude concept | Codex target | Notes |
| --- | --- | --- |
| `CLAUDE.md` | `AGENTS.md` or `SKILL.md` | Use `AGENTS.md` for repo-specific memory; use a skill for reusable workflows. |
| `.claude/commands/*.md` | Skill workflow sections, `agents/openai.yaml` default prompt, scripts | Codex does not consume Claude slash-command files directly. |
| `.claude/hooks/*.sh` | Skill/plugin `scripts/` guardrails | Codex skills cannot enforce global pre/post tool hooks; make checks explicit and runnable. |
| `.claude/rules/*.md` | `AGENTS.md` or skill body | Keep path-specific rules concise; avoid hidden behavior. |
| `.claude/agents/*.md` | Delegation guidance | Codex subagents require explicit user intent for delegation. |
| `.claude/settings.json` | Review manually; maybe `config.toml` only if requested | Do not port Claude permissions/model settings blindly. |
| Claude plugin zip | Codex plugin folder | Must include `.codex-plugin/plugin.json`; do not upload raw `.claude` zip. |

## Recommended Codex Structure

```text
%USERPROFILE%\.codex\skills\<skill-name>\
  SKILL.md
  agents\openai.yaml
  scripts\
  references\

<repo>\AGENTS.md

<repo>\plugins\<plugin-name>\
  .codex-plugin\plugin.json
  skills\<skill-name>\SKILL.md
  assets\
  scripts\

<repo>\.agents\plugins\marketplace.json
```

## Translation Rules

- Preserve intent, not syntax.
- Convert commands into workflows with clear inputs and outputs.
- Convert hooks into named checks the agent can run before risky operations.
- Convert "auto memory" into written, reviewable project guidance.
- Convert plugin packaging into Codex manifest format and marketplace entry.
- Keep reusable and project-specific knowledge separate.

## Examples From The Screenshots

`fix-issue` command:
- Codex version: a workflow section named "Fix GitHub issue" plus optional use of GitHub tools when available.
- Keep steps: inspect issue, locate files, implement minimal fix, add regression test, run tests, commit only if requested.

`pre-commit.sh` hook:
- Codex version: a guardrail script or checklist that runs type checks, lint, and tests before a commit.
- Do not make it an invisible global blocker unless the runtime supports and the user explicitly asks.

`frontend-design` skill:
- Codex version: a normal skill with frontmatter `name` and `description`, plus UI standards in the body.
- If the rules are only for one repo, put them in `AGENTS.md` instead.

`settings.json` allow/deny:
- Codex version: review case by case.
- Never import dangerous deny bypasses or broad shell allowlists.

## Useful Acceptance Checks

- The skill validates with `quick_validate.py`.
- `SKILL.md` has no TODO placeholders.
- Plugin paths are relative and begin with `./`.
- Marketplace entry name matches plugin folder and manifest name.
- The user can invoke the skill by name, and it also has a useful trigger description.
