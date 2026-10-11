# Module: git-commit

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/git-commit/`).
> Trigger scope: Requested Git commits or commit messages using repository conventions, diff inspection, and explicit-path staging. This module does not register a slash command. Turkish triggers: git commit oluştur, değişiklikleri gözden geçir ve commit mesajı yaz.

# Git Commit with Conventional Commits

## Overview

Inspect repository instructions and recent messages first. Follow its commit convention; Conventional Commits below are an optional fallback. This module does not register a `/commit` command. A message-only request does not authorize staging or committing.

## Conventional Commit Format

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Commit Types

| Type       | Purpose                        |
| ---------- | ------------------------------ |
| `feat`     | New feature                    |
| `fix`      | Bug fix                        |
| `docs`     | Documentation only             |
| `style`    | Formatting/style (no logic)    |
| `refactor` | Code refactor (no feature/fix) |
| `perf`     | Performance improvement        |
| `test`     | Add/update tests               |
| `build`    | Build system/dependencies      |
| `ci`       | CI/config changes              |
| `chore`    | Maintenance/misc               |
| `revert`   | Revert commit                  |

## Breaking Changes

```
# Exclamation mark after type/scope
feat!: remove deprecated endpoint

# BREAKING CHANGE footer
feat: allow config to extend other configs

BREAKING CHANGE: `extends` key behavior changed
```

## Workflow

### 1. Analyze Diff

```bash
# If files are staged, use staged diff
git diff --staged

# If nothing staged, use working tree diff
git diff

# Also check status
git status --porcelain
```

### 2. Stage Files (if needed)

If nothing is staged or you want to group changes differently:

```bash
# Stage specific files
git add -- "path/to/file1" "path/to/file2"
git diff --cached --stat
git diff --cached
```

Use explicit reviewed paths, not broad globs or `git add .`. Never run unattended `git add -p`; interactive staging requires an attended session. If unrelated changes share a file, use a reviewed noninteractive patch or clarify that material boundary. Preserve pre-existing staged and unstaged user changes; never unstage them automatically. **Never commit secrets** (.env, credentials.json, private keys).

### 3. Generate Commit Message

Analyze the diff to determine:

- **Type**: What kind of change is this?
- **Scope**: What area/module is affected?
- **Description**: One-line summary of what changed (present tense, imperative mood, <72 chars)

### 4. Execute Commit

Only after commit authorization. Multiline heredocs below are Bash; in PowerShell use repeated `git commit -m "subject" -m "body"` arguments or a UTF-8 message file with `-F`.

```bash
# Single line
git commit -m "<type>[scope]: <description>"

# Multi-line with body/footer
git commit -m "$(cat <<'EOF'
<type>[scope]: <description>

<optional body>

<optional footer>
EOF
)"
```

## Best Practices

- One logical change per commit
- Present tense: "add" not "added"
- Imperative mood: "fix bug" not "fixes bug"
- Reference issues: `Closes #123`, `Refs #456`
- Keep description under 72 characters

## Git Safety Protocol

- NEVER update git config
- NEVER run destructive commands (--force, hard reset) without explicit request
- NEVER skip hooks (--no-verify) unless user asks
- NEVER force push to main/master
- If commit fails due to hooks, fix and create NEW commit (don't amend)
