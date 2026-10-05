# Architecture Design — Extended Guidance

### Step 4: Document Decisions with ADRs

**ADR Template**:

```markdown
# ADR-{NNN}: {Short Title}

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-XXX]

## Date
YYYY-MM-DD

## Context
[What is the issue that motivates this decision? What forces are at play?]

## Decision
[What is the change we are making? State it in active voice: "We will ..."]

## Consequences

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Cost or risk 1]
- [Cost or risk 2]

### Neutral
- [Side effect that is neither positive nor negative]

## Alternatives Considered

### Alternative 1: [Name]
- **Pros**: ...
- **Cons**: ...
- **Why rejected**: ...

### Alternative 2: [Name]
- **Pros**: ...
- **Cons**: ...
- **Why rejected**: ...
```

**Example ADR**:

```markdown
# ADR-007: Use Event Sourcing for Order Lifecycle

## Status
Accepted

## Date
2026-02-15

## Context
The order management system requires a complete audit trail of every
state change. Regulatory requirements mandate that we can reconstruct
the exact state of any order at any point in time. The current
CRUD-based approach overwrites previous state, making auditing
dependent on application-level logging that has proven unreliable.

## Decision
We will use Event Sourcing for the Order aggregate. All state changes
will be captured as immutable domain events in an append-only event
store. Current state will be derived by replaying events. A CQRS read
model will serve query traffic.

## Consequences

### Positive
- Complete, immutable audit trail satisfies regulatory requirements
- Temporal queries ("what was the state at time T?") become trivial
- Natural fit for event-driven integration with downstream services

### Negative
- Increased complexity for developers unfamiliar with event sourcing
- Event schema evolution requires careful versioning (upcasting)
- Read model rebuild time grows linearly with event count

### Neutral
- Team needs training on event sourcing patterns (2-week ramp-up)

## Alternatives Considered

### Alternative 1: CRUD with Audit Log Table
- **Pros**: Familiar pattern, simple implementation
- **Cons**: Audit table can diverge from reality, no temporal queries
- **Why rejected**: Cannot guarantee audit fidelity under all failure modes

### Alternative 2: Database CDC (Change Data Capture)
- **Pros**: No application code changes, captures all mutations
- **Cons**: Captures physical changes, not domain intent
- **Why rejected**: Regulatory auditors need business-level event descriptions
```
