# Review and Handoff Protocol

## Implementer handoff

Record scope, files changed, acceptance criteria, tests/results, assumptions, skipped checks, rollback, and unresolved questions. A handoff reports evidence; it does not self-approve completion.

## Two-pass review

1. **Specification review:** read the task contract and changed artifacts. Check whether each acceptance criterion is met and whether scope expanded.
2. **Quality/security review:** inspect correctness, maintainability, test coverage, failure handling, safety, and integration risk without relying on the implementer’s conclusion.

Return only evidence-backed findings with severity, location, rationale, and a bounded fix contract. Re-review the fix, then run combined integration validation. Keep durable progress notes outside the skill body and do not include secrets or unrelated project data.
