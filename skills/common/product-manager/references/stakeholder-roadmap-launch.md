# Product Manager — Extended Guidance

### Step 5: Stakeholder Alignment

Misalignment between stakeholders causes more project delays than technical complexity. Use explicit frameworks to prevent ambiguity about who decides what.

**RACI Matrix**:

Define roles for every major decision and deliverable.

```
RACI MATRIX: [Project Name]
───────────────────────────
                    PM    Eng Lead   Designer   QA    Exec
Scope decisions     A     C          C          I     I
Technical approach  C     A          I          C     I
UX design           C     C          A          C     I
Release timing      A     R          I          C     I
Quality sign-off    C     C          I          A     I
Go/no-go decision   R     C          I          C     A

R = Responsible (does the work)
A = Accountable (makes the final call)
C = Consulted (provides input before decision)
I = Informed (notified after decision)
```

Rules:
- Every row has exactly one "A"
- "A" and "R" can be the same person but not always
- If a row has more than two "C" entries, the decision process will be slow; consider reducing

**Decision Log Template**:

Record every significant decision to prevent re-litigation.

```
DECISION LOG
────────────
ID:          DEC-001
Date:        [YYYY-MM-DD]
Decision:    [What was decided]
Context:     [Why this decision was needed]
Options:     [Options considered with brief pros/cons]
Chosen:      [Which option and why]
Decided by:  [Name and role]
Reversible:  [Yes/No - and what would trigger reversal]
```

**Cross-Functional Dependency Map**:

```
DEPENDENCY MAP: [Project Name]
──────────────────────────────
Deliverable          | Depends On              | Owner       | Status    | Risk
─────────────────────|─────────────────────────|─────────────|───────────|──────
API endpoint         | Schema design           | Backend     | Done      | Low
Frontend integration | API endpoint            | Frontend    | Blocked   | High
Load testing         | Staging environment      | DevOps      | In progress| Med
Documentation        | API endpoint + UX final  | Tech Writer | Not started| Low
```

**Communication Cadence**:

```
COMMUNICATION PLAN: [Project Name]
───────────────────────────────────
Audience        | Channel     | Frequency    | Content                    | Owner
────────────────|─────────────|──────────────|────────────────────────────|──────
Core team       | Standup     | Daily        | Blockers, progress         | Eng Lead
Stakeholders    | Status email| Weekly       | Milestones, risks, asks    | PM
Leadership      | Slide deck  | Biweekly     | KPIs, timeline, decisions  | PM
Customers       | Changelog   | At launch    | What's new, migration notes| PM
```

**Escalation Paths**:

```
ESCALATION FRAMEWORK
────────────────────
Level 1: Team-level (Eng Lead resolves within 1 business day)
  Triggers: Blocked tasks, minor scope questions, technical disagreements

Level 2: Cross-team (PM + Eng Lead + counterpart, resolve within 2 days)
  Triggers: Dependency delays, resource conflicts, scope changes >2 days

Level 3: Leadership (Director/VP, resolve within 3 days)
  Triggers: Timeline at risk, budget overrun, strategic pivot needed

Rule: Every escalation includes a written summary of the problem, options considered, and a recommended path forward. Never escalate without a recommendation.
```

### Step 6: Roadmap and Sequencing

A roadmap is a communication tool, not a commitment to exact dates. Use time horizons and dependency awareness to create realistic plans.

**Now/Next/Later Framework**:

```
ROADMAP: [Product Area]
───────────────────────

NOW (current sprint/iteration, committed)
  - [Feature A] - solves [problem], measured by [metric]
  - [Feature B] - prerequisite for [Feature D]

NEXT (1-2 sprints out, high confidence)
  - [Feature C] - depends on [Feature A] completion
  - [Feature D] - validated by [research/data]

LATER (3+ sprints, directional, subject to change)
  - [Feature E] - pending validation of [assumption]
  - [Feature F] - blocked by [external dependency]

WILL NOT DO (explicitly rejected)
  - [Feature G] - reason: [low impact, high cost]
```

Rules for the Now/Next/Later roadmap:
- "Now" items have acceptance criteria and an owner
- "Next" items have a problem statement and rough scope
- "Later" items have a hypothesis and a trigger condition for promotion
- Items move between columns only through explicit discussion, never silently

**Dependency-Aware Sequencing**:

```
SEQUENCING PLAN
───────────────
Phase 1 (Week 1-2): Foundation
  [Task A] ──→ [Task B] ──→ [Task C]
                  │
                  ▼
Phase 2 (Week 3-4): Core Features
  [Task D] ──→ [Task E]
  [Task F] (parallel, no dependencies)

Phase 3 (Week 5): Integration and Polish
  [Task G] (requires Task E + Task F)
  [Task H] (requires Task C)

Critical path: A → B → D → E → G
Float tasks (can slip without affecting deadline): F, H
```

**Milestone Definition**:

```
MILESTONE TEMPLATE
──────────────────
Name:           [M1: Core API Complete]
Target date:    [YYYY-MM-DD]
Definition:     [All CRUD endpoints deployed to staging with passing tests]
Deliverables:   [List of specific artifacts]
Exit criteria:  [What must be true to declare this milestone done]
Dependencies:   [What must be complete before this milestone starts]
Risk:           [Primary risk and mitigation]
```

**Risk-Adjusted Timeline**:

Add buffers based on uncertainty, not optimism.

```
TIMELINE ESTIMATION
───────────────────
Task              | Best Case | Likely | Worst Case | Risk-Adjusted
──────────────────|───────────|────────|────────────|──────────────
Task A            | 2d        | 3d     | 5d         | 3.5d
Task B            | 1d        | 2d     | 4d         | 2.5d
Task C            | 3d        | 5d     | 10d        | 6d
Integration       | 1d        | 2d     | 5d         | 3d
──────────────────|───────────|────────|────────────|──────────────
Total             | 7d        | 12d    | 24d        | 15d

Risk-Adjusted = (Best + 4*Likely + Worst) / 6  (PERT estimate)

Buffer policy: Add 20% to the risk-adjusted total for unknowns.
Communicate the risk-adjusted estimate externally, not the best case.
```

**Feature Flagging Strategy**:

Decouple deployment from release to reduce launch risk.

```
FEATURE FLAG PLAN: [Feature Name]
─────────────────────────────────
Flag name:          [feature-name-enabled]
Default state:      OFF
Rollout stages:
  1. Internal team only (dogfooding)          - 1 week
  2. 5% of users (canary)                     - 3 days
  3. 25% of users (early adopter ring)        - 1 week
  4. 100% of users (general availability)     - permanent
Rollback trigger:   [Error rate >1% or P95 latency >500ms]
Flag removal:       [Remove flag and dead code within 30 days of GA]
Owner:              [Name]
```

### Step 7: Launch and Validation

Launching is not the finish line. It is the start of validation. Plan for measurement, iteration, and (if needed) rollback.

**Launch Checklist**:

```
PRE-LAUNCH CHECKLIST: [Feature Name]
─────────────────────────────────────
Category          | Item                                    | Status
──────────────────|─────────────────────────────────────────|───────
Engineering       | All acceptance criteria passing          | [ ]
Engineering       | Load test completed at 2x expected load  | [ ]
Engineering       | Feature flag tested (on/off/rollback)    | [ ]
Engineering       | Monitoring and alerts configured          | [ ]
Engineering       | Runbook written for on-call team          | [ ]
Quality           | QA sign-off on staging                    | [ ]
Quality           | Accessibility audit passed                | [ ]
Quality           | Security review completed                 | [ ]
Documentation     | User-facing docs updated                  | [ ]
Documentation     | Internal knowledge base updated           | [ ]
Documentation     | API changelog entry written               | [ ]
Communication     | Release notes drafted                     | [ ]
Communication     | Support team briefed                      | [ ]
Communication     | Stakeholders notified of launch date      | [ ]
Rollback          | Rollback plan documented and tested       | [ ]
Rollback          | Data migration reversal verified          | [ ]
```

**Feature Flag Rollout Plan**:

```
ROLLOUT SCHEDULE: [Feature Name]
────────────────────────────────
Stage    | Audience         | Duration | Success Gate            | Rollback Gate
─────────|──────────────────|──────────|─────────────────────────|──────────────
Canary   | Internal team    | 3 days   | No P0/P1 bugs           | Any P0 bug
Ring 1   | 5% of users      | 5 days   | Error rate <0.5%         | Error rate >2%
Ring 2   | 25% of users     | 5 days   | P95 latency <300ms       | P95 >800ms
Ring 3   | 50% of users     | 3 days   | NPS/CSAT stable          | NPS drop >5pts
GA       | 100% of users    | Permanent| Metric targets met       | Exec decision
```

**A/B Test Design**:

When validating a feature with an experiment:

```
A/B TEST PLAN: [Experiment Name]
────────────────────────────────
Hypothesis:      [Changing X will improve Y by Z%]
Primary metric:  [Conversion rate, engagement, retention, etc.]
Guardrail metrics: [Metrics that must not degrade]
Control group:   [Current experience, 50% of traffic]
Treatment group: [New feature enabled, 50% of traffic]
Sample size:     [Minimum users needed for statistical significance]
Duration:        [Minimum runtime, typically 2-4 weeks]
Significance:    [p < 0.05 or 95% confidence interval]
Decision rule:   [Ship if primary metric improves >X% with significance]
Owner:           [Name]
```

**Success Metric Dashboard**:

Define what to monitor post-launch and where to find it.

```
POST-LAUNCH DASHBOARD: [Feature Name]
──────────────────────────────────────
Metric                | Source        | Baseline | Target  | Alert Threshold
──────────────────────|──────────────|──────────|─────────|────────────────
Adoption rate         | Analytics    | 0%       | 30%/30d | <10% at day 14
Error rate            | APM          | 0.1%     | <0.5%   | >1%
P95 response time     | APM          | 150ms    | <300ms  | >500ms
User satisfaction     | Survey/NPS   | N/A      | >4.0/5  | <3.0
Support ticket volume | Help desk    | 5/week   | <10/week| >20/week
```

**Post-Launch Review Template**:

Conduct a review 2-4 weeks after launch.

```
POST-LAUNCH REVIEW: [Feature Name]
───────────────────────────────────
Date:           [YYYY-MM-DD]
Participants:   [Names and roles]

1. RESULTS
   - Primary metric: [Target] vs [Actual]
   - Secondary metrics: [Summary]
   - Unexpected findings: [Any surprises]

2. WHAT WENT WELL
   - [Item 1]
   - [Item 2]

3. WHAT COULD IMPROVE
   - [Item 1 with specific action]
   - [Item 2 with specific action]

4. FOLLOW-UP ACTIONS
   | Action                    | Owner      | Due Date   |
   |---------------------------|------------|------------|
   | [Action 1]                | [Name]     | [Date]     |
   | [Action 2]                | [Name]     | [Date]     |

5. DECISION
   - [ ] Keep as-is (metrics met)
   - [ ] Iterate (metrics partially met, specific improvements identified)
   - [ ] Roll back (metrics not met, user impact negative)
   - [ ] Expand (metrics exceeded, roll out to additional segments)
```
