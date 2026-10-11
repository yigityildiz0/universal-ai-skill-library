# Module: requesting-code-review

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/requesting-code-review/`).
> Original trigger scope: Use when completing tasks, implementing major features, or before merging to verify work meets requirements

# Requesting Code Review

Run a focused code review before issues cascade. If the current host supports subagents and user or project rules permit delegation, use one; otherwise perform the same review in the current session. Give the reviewer a concise brief and the work product rather than the session's full history.

**Core principle:** Review early, review often.

## When to Request Review

**Use a focused review when risk or repository policy warrants it:**
- After integrating substantial delegated changes
- After completing a major feature
- Before a merge where repository policy requires review

**Optional but valuable:**
- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to Request

**1. Determine the real review scope:**

Use the recorded task-start commit, actual PR base, or verified merge-base for the feature. Never assume `HEAD~1` covers the work. Include staged, unstaged, and untracked task files when work is uncommitted; preserve unrelated user edits. In a non-Git workspace use explicit files and the known baseline.
```bash
BASE_SHA=$(git merge-base <verified-target-ref> HEAD)
HEAD_SHA=$(git rev-parse HEAD)
git diff "$BASE_SHA" HEAD -- <review-paths>
git diff --cached -- <review-paths>
git diff -- <review-paths>
git ls-files --others --exclude-standard -- <review-paths>
```

**2. Run the code review:**

Read the bundled [code-reviewer.md](code-reviewer.md) template, relative to this module. Use a supported subagent only when explicitly authorized; otherwise apply it directly. Do not assume `Task` exists. Include the uncommitted file scope and baseline, not just commit SHAs.

**Placeholders:**
- `{DESCRIPTION}` - Brief summary of what you built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` - Starting commit
- `{HEAD_SHA}` - Ending commit

**3. Act on feedback:**
- Fix Critical issues immediately
- Fix important in-scope issues before dependent integration; continue independent work
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Example

```
[Just completed Task 2: Add verification function]

You: Let me request code review before proceeding.

BASE_SHA=<recorded-task-start-or-verified-merge-base>
HEAD_SHA=$(git rev-parse HEAD)

[Run focused code review]
  DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types
  PLAN_OR_REQUIREMENTS: Task 2 from docs/superpowers/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661

[Subagent returns]:
  Strengths: Clean architecture, real tests
  Issues:
    Important: Missing progress indicators
    Minor: Magic number (100) for reporting interval
  Assessment: Ready to proceed

You: [Fix progress indicators]
[Continue to Task 3]
```

## Integration with Workflows

**Subagent-Driven Development:**
- Review at dependency/risk-appropriate checkpoints
- Catch issues before they compound
- Resolve material issues before dependent integration

**Executing Plans:**
- Review after each task or at natural checkpoints
- Get feedback, apply, continue

**Ad-Hoc Development:**
- Review before merge
- Review when stuck

## Red Flags

**Never:**
- Skip a required or risk-justified review
- Ignore Critical issues
- Merge with unresolved important in-scope issues
- Argue with valid technical feedback

**If reviewer wrong:**
- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification

See [code-reviewer.md](code-reviewer.md), relative to this module directory.
