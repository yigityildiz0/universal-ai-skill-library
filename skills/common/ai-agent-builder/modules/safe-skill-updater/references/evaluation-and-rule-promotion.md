# Evaluation and Rule Promotion

Use only for an explicitly named update/audit scope. This is a conservative evaluation method, not an auto-update engine.

## Candidate rule gate

Promote a cross-skill rule only when all are true:

1. At least two independent in-scope sources support the same operational principle.
2. The rule has a concrete trigger, benefit, exception, and non-goal.
3. It does not override a user-authored, security, provider, or host-specific contract.
4. An evidence map identifies source file, section, and the behavior being preserved.
5. A smaller local fix cannot solve the issue.

Reject slogans, style preferences, broad “always/never” claims, and rules supported only by popularity.

## Candidate evaluation

Create representative should-trigger, should-not-trigger, edge, and failure cases. Compare baseline and candidate behavior on a held-out subset. For high-risk changes, use an independent blind reviewer with raw artifacts rather than a desired outcome. Check assertion quality: an assertion must discriminate a genuine regression rather than always pass.

Record behavior, time/context cost, structural validation, and rollback. Keep a proposed rule only if it improves the target behavior without regressing accepted contracts or causing material trigger/context overhead.

## Apply

Produce a semantic diff and request the authority required for the target scope. Never write global instructions, change providers/models, delete rules, or propagate host-specific guidance without explicit authorization and a verified rollback path.
