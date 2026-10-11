# Module: executing-plans

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/executing-plans/`).
> Original trigger scope: Use when you have a written implementation plan to execute in a separate session with review checkpoints

# Executing Plans

## Overview

Load plan, review critically, execute all tasks, report when complete.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

If subagent support is available and the user or applicable instructions explicitly authorize delegation, use [subagent-driven-development](../subagent-driven-development/MODULE.md) where beneficial. Otherwise execute in this session; these are bundled modules, not separately installed skills.

## The Process

### Step 1: Load and Review Plan
1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. Resolve concerns from evidence; ask only for material missing decisions and continue independent work
4. If no concerns: create or update a visible task plan with the current host's planning mechanism, then proceed

### Step 2: Execute Tasks

For each task:
1. Mark as in_progress
2. Follow the plan, adapting stale technical details to verified repository reality; escalate material scope changes
3. Run verifications as specified
4. Mark as completed

### Step 3: Complete Development

After all tasks complete and verified:
- Report the scoped implementation and verification evidence.
- Only when branch integration or cleanup is requested/relevant, read [finishing-a-development-branch](../finishing-a-development-branch/MODULE.md) and execute the authorized choice.

## When to Stop and Ask for Help

**Pause dependent work and ask only when investigation cannot resolve a material blocker:**
- Inspect a failing test or missing dependency first with [systematic-debugging](../systematic-debugging/MODULE.md); a failure is evidence to investigate, not an automatic user handoff
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for material clarification rather than guessing; continue unblocked tasks.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

Do not force dependent changes through unresolved material blockers; investigate and continue independent work.

## Remember
- Review plan critically first
- Follow verified plan intent and review meaningful changes
- Don't skip verifications
- Read bundled modules by their actual paths
- Pause only blocked work, don't guess material requirements
- Follow repository branch policy and ownership; do not invent a branch/worktree approval gate for an authorized small edit

## Integration

**Related bundled modules:**
- [using-git-worktrees](../using-git-worktrees/MODULE.md) — isolation only when needed
- [writing-plans](../writing-plans/MODULE.md) — scalable plan creation
- [finishing-a-development-branch](../finishing-a-development-branch/MODULE.md) — integration only when relevant/authorized
