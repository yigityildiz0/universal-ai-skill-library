---
name: caveman-review
description: "Produce concise code-review findings with exact locations, evidence, impact, and a concrete fix while retaining necessary rationale for high-risk issues. Use only when the user explicitly invokes $caveman-review or asks for a Caveman-style review. Do not trigger for ordinary review requests."
---

# Caveman Review

Review first; compress only the presentation. Do not change code, post
comments, approve, or request changes unless the user separately authorizes
that action.

## Workflow

1. Inspect the full relevant diff and surrounding code.
2. Verify each finding is introduced or exposed by the change.
3. Rank findings by impact and confidence.
4. Omit praise, narration, and speculative nits.

## Finding format

Use:

`[P1] path/to/file:L42 - Null user reaches email access. Guard before dereference.`

- `P0`: immediate, broad catastrophic impact.
- `P1`: high-priority correctness, security, or data-loss defect.
- `P2`: normal actionable defect.
- `P3`: low-priority but real issue.

Include exact file, tight line range, failing condition, consequence, and
actionable fix. If location is unavailable, name the exact symbol.

## Clarity overrides

Use a normal paragraph when a one-line comment would hide:

- exploitability, privacy impact, or a security boundary;
- migration, compatibility, or data-loss consequences;
- architectural tradeoffs or uncertainty;
- reproduction steps needed to establish the defect.

Lead with findings. If none exist, say so and name any untested residual risk.
