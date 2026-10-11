# Module: using-git-worktrees

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/using-git-worktrees/`).
> Trigger scope: Use when requested or when feature work genuinely needs isolation; executing a plan alone does not require a worktree. Reuse suitable existing isolation.

# Using Git Worktrees

## Overview

Use isolation when it provides a concrete benefit. Prefer suitable available native worktree tools, otherwise Git. No automatic commits or dependency installation. Bash examples must be adapted to PowerShell on Windows; check each command's exit status before proceeding.

**Core principle:** Detect existing isolation first. Then use native tools. Then fall back to git. Never fight the harness.

**Announce at start:** "I'm using the using-git-worktrees skill to set up an isolated workspace."

## Step 0: Detect Existing Isolation

**Before creating anything, check if you are already in an isolated workspace.**

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

**Submodule guard:** `GIT_DIR != GIT_COMMON` is also true inside git submodules. Before concluding "already in a worktree," verify you are not in a submodule:

```bash
# If this returns a path, you're in a submodule, not a worktree — treat as normal repo
git rev-parse --show-superproject-working-tree 2>/dev/null
```

**If `GIT_DIR != GIT_COMMON` (and not a submodule):** You are already in a linked worktree. Skip to Step 3 (Project Setup). Do NOT create another worktree.

Report with branch state:
- On a branch: "Already in isolated workspace at `<path>` on branch `<name>`."
- Detached HEAD: "Already in isolated workspace at `<path>` (detached HEAD, externally managed). Branch creation needed at finish time."

**If `GIT_DIR == GIT_COMMON` (or in a submodule):** You are in a normal repo checkout.

Has the user already indicated their worktree preference in your instructions? If not, ask for consent before creating a worktree:

> "Would you like me to set up an isolated worktree? It protects your current branch from changes."

Honor any existing declared preference without asking. If the user declines consent, work in place and skip to Step 3.

## Step 1: Create Isolated Workspace

**You have two mechanisms. Try them in this order.**

### 1a. Native Worktree Tools (preferred)

The user has asked for an isolated workspace (Step 0 consent). Do you already have a way to create a worktree? It might be a tool with a name like `EnterWorktree`, `WorktreeCreate`, a `/worktree` command, or a `--worktree` flag. If you do, use it and skip to Step 3.

Native tools handle directory placement, branch creation, and cleanup automatically. Using `git worktree add` when you have a native tool creates phantom state your harness can't see or manage.

Only proceed to Step 1b if you have no native worktree tool available.

### 1b. Git Worktree Fallback

**Only use this if Step 1a does not apply** — you have no native worktree tool available. Create a worktree manually using git.

#### Directory Selection

Follow this priority order. Explicit user preference always beats observed filesystem state.

1. **Check your instructions for a declared worktree directory preference.** If the user has already specified one, use it without asking.

2. **Check for an existing project-local worktree directory:**
   ```bash
   ls -d .worktrees 2>/dev/null     # Preferred (hidden)
   ls -d worktrees 2>/dev/null      # Alternative
   ```
   If found, use it. If both exist, `.worktrees` wins.

3. **Check for an existing global directory:**
   ```bash
   project=$(basename "$(git rev-parse --show-toplevel)")
   ls -d ~/.config/superpowers/worktrees/$project 2>/dev/null
   ```
   If found, use it (backward compatibility with legacy global path).

4. **If there is no other guidance available**, default to `.worktrees/` at the project root.

#### Safety Verification (project-local directories only)

**MUST verify directory is ignored before creating worktree:**

```bash
# SELECTED_RELATIVE_PATH is the exact proposed worktree path within this repo.
git check-ignore -q -- "$SELECTED_RELATIVE_PATH"
# Check this command's exit status. Ignoring another directory is not sufficient.
```

**If NOT ignored:** Use an authorized repository ignore rule or local `.git/info/exclude` rule for the selected path, then recheck that exact path. Do not automatically commit ignore changes. If modifying exclusions is not authorized, use an appropriate external location or clarify only that choice.

**Why critical:** Prevents accidentally committing worktree contents to repository.

Global directories (`~/.config/superpowers/worktrees/`) need no verification.

#### Create the Worktree

```bash
project=$(basename "$(git rev-parse --show-toplevel)")

# Determine path based on chosen location
# For project-local: path="$LOCATION/$BRANCH_NAME"
# For global: path="$HOME/.config/superpowers/worktrees/$project/$BRANCH_NAME"

git worktree add -b "$BRANCH_NAME" -- "$path" || exit 1
cd "$path" || exit 1
# Record exact path, branch, start commit, and task ownership for later cleanup.
```

**Permission failure:** Do not weaken sandbox settings. Investigate the actual error; work in place only if current-workspace ownership, cleanliness, and requested isolation permit it. Otherwise pause dependent edits and report the blocker.

## Step 3: Project Setup

Inspect repository instructions, manifests, lockfiles, and already available tools. Reuse existing environments. Run only required authorized setup; a manifest is not permission to install packages, download dependencies, execute lifecycle scripts, or modify lockfiles. If a dependency is missing, report it and continue independent checks rather than auto-installing.

## Step 4: Verify Clean Baseline

Run tests to ensure workspace starts clean:

```bash
# Use project-appropriate command
# Select the actual repository check (e.g. npm test, cargo test, pytest, or go test ./...).
```

**If tests fail:** Investigate and record baseline failures; continue independent work if safe. Ask only when the failure prevents meaningful verification or requires a material decision.

**If tests pass:** Report ready.

### Report

```
Worktree ready at <full-path>
Tests passing (<N> tests, 0 failures)
Ready to implement <feature-name>
```

## Quick Reference

| Situation | Action |
|-----------|--------|
| Already in linked worktree | Skip creation (Step 0) |
| In a submodule | Treat as normal repo (Step 0 guard) |
| Native worktree tool available | Use it (Step 1a) |
| No native tool | Git worktree fallback (Step 1b) |
| `.worktrees/` exists | Use it (verify ignored) |
| `worktrees/` exists | Use it (verify ignored) |
| Both exist | Use `.worktrees/` |
| Neither local path exists | Use instructed path, else existing global path, else `.worktrees/` |
| Global path exists | Use only when no explicit preference or existing local path takes priority |
| Selected path not ignored | Add an authorized ignore/exclude rule, recheck exact path; no automatic commit |
| Permission error on create | Sandbox fallback, work in place |
| Tests fail during baseline | Investigate, record, continue independent work |
| Missing dependencies | No automatic install; report precise limitation |

## Common Mistakes

### Fighting the harness

- **Problem:** Using `git worktree add` when the platform already provides isolation
- **Fix:** Step 0 detects existing isolation. Step 1a defers to native tools.

### Skipping detection

- **Problem:** Creating a nested worktree inside an existing one
- **Fix:** Always run Step 0 before creating anything

### Skipping ignore verification

- **Problem:** Worktree contents get tracked, pollute git status
- **Fix:** Always use `git check-ignore` before creating project-local worktree

### Assuming directory location

- **Problem:** Creates inconsistency, violates project conventions
- **Fix:** Follow priority: explicit user/project instruction > existing local > existing global > default

### Proceeding with failing tests

- **Problem:** Can't distinguish new bugs from pre-existing issues
- **Fix:** Record baseline failures and investigate; clarify only material blockers

## Red Flags

**Never:**
- Create a worktree when Step 0 detects existing isolation
- Use `git worktree add` when you have a native worktree tool (e.g., `EnterWorktree`). This is the #1 mistake — if you have it, use it.
- Skip Step 1a by jumping straight to Step 1b's git commands
- Create worktree without verifying it's ignored (project-local)
- Skip baseline test verification
- Conceal baseline failures or claim checks passed when they failed

**Always:**
- Run Step 0 detection first
- Prefer native tools over git fallback
- Follow priority: explicit user/project instruction > existing local > existing global > default
- Verify directory is ignored for project-local
- Inspect setup requirements; run only authorized necessary setup
- Verify clean test baseline
