# Quality Preservation Rubric

Score the current and proposed skill independently. A rewrite may ship only if no critical category regresses and the targeted category improves with evidence.

| Category | Questions |
|---|---|
| Trigger precision | Does the description state what and when without swallowing neighboring skills? |
| Workflow correctness | Is the sequence executable in the target host? |
| Coverage | Are common, edge, and failure cases preserved? |
| Dependencies | Do all tools, scripts, references, and assets exist with fallbacks where appropriate? |
| Verification | Are outcomes checked proportionally to risk? |
| Safety and authority | Are destructive/external actions bounded and confirmed? |
| Portability | Is shared logic provider-neutral and host-specific logic isolated? |
| Context efficiency | Is always-loaded metadata concise and deep detail progressively disclosed? |
| Maintainability | Are names valid, links shallow, and responsibilities coherent? |

## Automatic Rejects

Reject the update when it:

- removes a proven capability without an explicit replacement;
- replaces working scripts with untested prose;
- copies managed-plugin instructions without their tools;
- adds fixed provider/model selection to a shared skill;
- broadens authority, weakens safety, or silently deletes user data;
- increases length without adding non-obvious operational value;
- relies on a heuristic score as proof of quality.

## Evidence Pack

Keep the before/after hashes, semantic diff matrix, validator output, representative test results, independent review result for high-risk changes, and rollback path outside the skill body.
