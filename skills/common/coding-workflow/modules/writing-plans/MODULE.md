# Module: writing-plans

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/writing-plans/`).
> Original trigger scope: Use when you have a spec or requirements for a multi-step task, before touching code

# Writing Plans

## Overview

Write an executable plan sized to risk and handoff needs: goal, exact file scope, dependencies, decisions, acceptance criteria, and verification. Small work can use a short checklist. Include complete code only for tricky contracts/examples or when needed for a reliable handoff; do not duplicate the entire implementation in every plan. Commits and worktrees are optional authorized operations.

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. Assume they don't know good test design very well.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Context:** If isolation is needed, use [using-git-worktrees](../using-git-worktrees/MODULE.md) at execution time; these are internal modules, not separately installed skills.

**Save plans to:** `docs/plans/YYYY-MM-DD-<feature-name>.md`
- (User preferences for plan location override this default)

## Scope Check

If the spec covers multiple independent subsystems, it should have been broken into sub-project specs during brainstorming. If it wasn't, suggest breaking this into separate plans — one per subsystem. Each plan should produce working, testable software on its own.

## File Structure

Before defining tasks, map out which files will be created or modified and what each one is responsible for. This is where decomposition decisions get locked in.

- Design units with clear boundaries and well-defined interfaces. Each file should have one clear responsibility.
- You reason best about code you can hold in context at once, and your edits are more reliable when files are focused. Prefer smaller, focused files over large ones that do too much.
- Files that change together should live together. Split by responsibility, not by technical layer.
- In existing codebases, follow established patterns. If the codebase uses large files, don't unilaterally restructure - but if a file you're modifying has grown unwieldy, including a split in the plan is reasonable.

This structure informs the task decomposition. Each task should produce self-contained changes that make sense independently.

## Bite-Sized Task Granularity

**Use focused verifiable steps; 2-5 minutes is a rough planning example, not a required duration:**
- "Write the failing test" - step
- "Run it to make sure it fails" - step
- "Implement the minimal code to make the test pass" - step
- "Run the tests and make sure they pass" - step
- "Commit" - only when authorized and useful

## Plan Document Header

**Suggested header for a substantial saved plan:**

```markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** Read coding-workflow's `modules/subagent-driven-development/MODULE.md` only when delegation is explicitly authorized, otherwise `modules/executing-plans/MODULE.md` for inline work. Resolve these paths from the skill root, not the saved plan directory. Track verifiable tasks with checkboxes.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

```python
def function(input):
    return expected
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit, if authorized**

```bash
git add -- tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

## No Placeholders

Every step needs enough detail to execute without guessing material requirements. Avoid:
- "TBD", "TODO", "implement later", "fill in details"
- "Add appropriate error handling" / "add validation" / "handle edge cases"
- "Write tests for the above" without specifying the behavior, cases, and pass/fail criterion
- Unresolvable cross-references; link precise shared context instead of duplicating code
- Steps missing important contracts or acceptance criteria; full implementation code is optional
- References to types, functions, or methods not defined in any task

## Remember
- Exact file paths always
- Sufficient contracts, file scope, and examples; complete code only where it adds value
- Exact commands with expected output
- DRY, YAGNI, risk-appropriate tests, commits only when authorized

## Self-Review

After writing the complete plan, look at the spec with fresh eyes and check the plan against it. This is a checklist you run yourself — not a subagent dispatch.

**1. Spec coverage:** Skim each section/requirement in the spec. Can you point to a task that implements it? List any gaps.

**2. Placeholder scan:** Search your plan for red flags — any of the patterns from the "No Placeholders" section above. Fix them.

**3. Type consistency:** Do the types, method signatures, and property names you used in later tasks match what you defined in earlier tasks? A function called `clearLayers()` in Task 3 but `clearFullLayers()` in Task 7 is a bug.

If you find issues, fix them inline, then recheck changed sections and dependent tasks for coverage/type consistency. Do not repeat unrelated checks without a reason. Add missing requirements within authorized scope.

## Execution Handoff

If implementation is already requested, continue without asking whether to execute. Read [executing-plans](../executing-plans/MODULE.md); use [subagent-driven-development](../subagent-driven-development/MODULE.md) only if delegation is explicitly authorized and useful. For plan-only requests, deliver the plan and stop. Ask only about a material unresolved decision, not a routine execution preference.
