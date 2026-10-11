# Module: security-review

> Part of the `coding-workflow` skill. Paths below are relative to this module folder (`modules/security-review/`).
> Trigger scope: Assess relevant attack surfaces or perform a requested full security audit across ten domains, including injection, authorization, concurrency, and supply-chain risk. Tool availability and review scope determine checks; no mandatory scanner installation or external upload.

# Code Review - Security Review

Identify security vulnerabilities across 10 candidate domains. This module can stand alone or complement [code-review-and-quality](../code-review-and-quality/MODULE.md); it does not require a separately installed six-phase skill suite.

Scope by affected attack surfaces and risk. Use available, configured scanners only; inspect repository scripts and tool help first. Do not install tools, upload source/dependency inventories, or run paid/authenticated scans merely because they are listed. Select suitable alternatives rather than running every scanner. Report skipped/unavailable coverage accurately and continue manual review. Dependency audits are not source-code static analysis.

## When to Use This Skill

Use this skill when you need to:

- Conduct security audit
- Identify vulnerabilities across all attack surfaces
- Check OWASP Top 10 compliance
- Assess supply chain security
- Analyze race conditions and concurrency risks
- Prepare for penetration testing
- Meet security compliance requirements

**Trigger phrases**: "security review", "vulnerability scan", "OWASP", "security audit", "penetration test prep", "CVE check", "security assessment", "race condition"

## What This Skill Does

### OWASP Top 10 (2021) Mapping

| ID | Vulnerability | Covered By Domain |
|----|---------------|-------------------|
| A01 | Broken Access Control | Domain 2: AuthN/AuthZ |
| A02 | Cryptographic Failures | Domain 8: Cryptography |
| A03 | Injection | Domain 1: Input/Output Safety |
| A04 | Insecure Design | Domain 2 + Domain 10 |
| A05 | Security Misconfiguration | Domain 6: CORS & Headers |
| A06 | Vulnerable Components | Domain 5: Supply Chain |
| A07 | Authentication Failures | Domain 2 + Domain 3: JWT |
| A08 | Data Integrity Failures | Domain 10: Data Integrity |
| A09 | Logging Failures | Domain 4: Secrets/PII |
| A10 | SSRF | Domain 1: Input/Output Safety |

### Severity Classification

| Level | Alias | Description |
|-------|-------|-------------|
| **P0** | CRITICAL | Immediate exploit risk, data breach potential |
| **P1** | HIGH | Significant vulnerability requiring urgent fix |
| **P2** | MEDIUM | Security weakness to address |
| **P3** | LOW | Minor hardening improvement |

## Instructions

### Step 1: Dependency Vulnerability Scan

```bash
# Python
pip-audit
safety check

# JavaScript
npm audit
snyk test

# Java
mvn dependency-check:check
```

### Step 2: Static Security Analysis

```bash
# Python
bandit -r src/

# JavaScript: use an existing configured ESLint/security script
# Example only, after confirming the plugin is already configured:
eslint src/

# Java: run the repository's existing SpotBugs/FindSecBugs build target
# (configuration-specific, not a literal command)
```

### Step 3: 10-Domain Security Scan

Reference: the ten domain checklists below and [code-review-and-quality](../code-review-and-quality/MODULE.md).

Work through relevant domains, applying diagnostic questions. For a full audit document all ten as checked or justified not-applicable; a targeted review need not manufacture findings in unaffected domains:

#### Domain 1: Input/Output Safety
**Diagnostic**: "Does any user-controlled input reach a sensitive sink without sanitization?"
- XSS (innerHTML, dangerouslySetInnerHTML, unescaped template output)
- SQL/NoSQL/Command/GraphQL injection
- SSRF (user-controlled URLs in server requests)
- Path traversal (../ in file paths)
- Prototype pollution (deep merge of user objects)

#### Domain 2: Authentication & Authorization
**Diagnostic**: "Can an authenticated user access resources belonging to another user or tenant?"
- Missing auth guards on endpoints
- Missing tenant checks in multi-tenant systems
- IDOR (direct object references without ownership check)
- Privilege escalation via client-provided roles
- Session fixation (session ID not rotated after login)

#### Domain 3: JWT & Token Security
**Diagnostic**: "What happens if an attacker captures a valid token? How long can they use it?"
- Algorithm confusion (accepting `none` or wrong algorithm)
- Hardcoded signing secrets
- Missing expiration validation
- Sensitive data in JWT payload
- Missing issuer/audience validation

#### Domain 4: Secrets and PII
**Diagnostic**: "If I grep for common secret patterns, what do I find?"
- API keys, credentials in source code
- Secrets in git history
- PII in logs without masking
- Secrets in error messages
- Unencrypted password storage

#### Domain 5: Supply Chain & Dependencies
**Diagnostic**: "If a dependency is compromised, what is the blast radius?"
- Unpinned dependencies (version ranges)
- Dependency confusion risks
- External scripts without SRI integrity
- Known CVEs in dependencies
- Abandoned packages (no maintenance 12+ months)

#### Domain 6: CORS & Security Headers
**Diagnostic**: "What security headers are set? Which are missing?"
- Permissive CORS on authenticated endpoints
- Missing CSP, X-Frame-Options, X-Content-Type-Options
- Missing HSTS
- Exposed internal headers (server version, debug info)

#### Domain 7: Runtime Risks
**Diagnostic**: "Can an attacker cause this service to become unresponsive with a single crafted request?"
- Unbounded loops controlled by user input
- Missing timeouts on external calls
- Missing rate limiting on public endpoints
- Sync I/O in async context
- ReDoS (catastrophic regex backtracking)

#### Domain 8: Cryptography
**Diagnostic**: "Are we using well-vetted cryptographic libraries with secure defaults?"
- Weak algorithms (MD5, SHA1 for security)
- Hardcoded IVs/salts
- Encryption without authentication (AES-CBC without HMAC)
- Insufficient key length
- Custom crypto implementations
- Insecure random (Math.random, random.random for security)

#### Domain 9: Race Conditions (Deep Dive)
**Diagnostic questions**:
1. "Is any shared state accessed by multiple threads/processes/requests without synchronization?"
2. "Are there check-then-act patterns where check and action are not atomic?"
3. "Do database operations that read and write the same row use appropriate isolation?"
4. "In distributed components, what happens if the same event is processed twice?"

Sub-categories:
- **9a: Shared State**: Unsynchronized concurrent access, non-thread-safe collections, global mutable state
- **9b: Check-Then-Act (TOCTOU)**: if-exists-then-use, balance-check-then-deduct, permission check separate from action
- **9c: Database Concurrency**: Missing locking, non-atomic counters, read-modify-write without isolation
- **9d: Distributed Systems**: Missing distributed locks, cache invalidation races, event ordering, split-brain

#### Domain 10: Data Integrity
**Diagnostic**: "If this operation fails halfway through, what state is the data left in?"
- Missing transactions for multi-step operations
- Weak validation before persistence
- Missing idempotency on retry-able paths
- Lost updates from concurrent writes
- Cascade failures from unguarded deletes

### Step 4: Document Findings

For each finding, document both **exploitability** (how easy to exploit) and **impact** (what damage results).

````markdown
## Security Finding

**Vulnerability**: [Type]
**File**: [path/to/file.py:42]
**Severity**: P0 (CRITICAL)
**Domain**: [1-10]
**OWASP**: [A01-A10 if applicable]
**CVE**: [If applicable]

### Description
[Detailed description]

### Exploitability
[How easy to exploit: trivial / moderate / complex]

### Impact
[What damage results: data breach / service disruption / data corruption]

### Vulnerable Code
```python
[problematic code]
```

### Remediation
```python
[fixed code]
```

### References
- [Relevant OWASP link or advisory]
````

## Common Vulnerabilities by Language

### Python
- SQL injection (raw queries, f-strings in SQL)
- Command injection (subprocess with shell=True)
- Pickle deserialization (arbitrary code execution)
- Insecure randomness (random module for security)

### JavaScript
- XSS (innerHTML, dangerouslySetInnerHTML)
- Prototype pollution (deep merge, Object.assign)
- Eval injection (eval, Function constructor)
- Path traversal (user input in require/readFile)

### Java
- SQL injection (string concatenation in queries)
- XXE (XML External Entity)
- Insecure deserialization (ObjectInputStream)
- Log injection (user input in log statements)

### C# / .NET
- SQL injection (string concatenation in SqlCommand)
- Insecure deserialization (BinaryFormatter)
- Path traversal (user input in File.Open)
- LDAP injection

### Go
- SQL injection (fmt.Sprintf in queries)
- `exec.Command` does not invoke a shell by default: separate argv is not automatically shell injection. Inspect executable selection, option/argument injection, the target program's semantics, and explicit `sh -c`/`cmd /c` use; allowlist commands and constrain arguments as needed.
- Race conditions (goroutine shared state without mutex)
- Insecure TLS configuration

## Quality Checklist

- [ ] Relevant available dependency scan completed, or limitation documented
- [ ] Relevant configured static analysis run, or manual-review coverage documented
- [ ] In-scope domains checked; full audits account for all ten
- [ ] Race conditions analyzed (all 4 sub-categories)
- [ ] OWASP Top 10 mapped
- [ ] Exploitability and impact documented for each finding
- [ ] Language-specific vulnerabilities checked
- [ ] Findings documented with severity (P0-P3)

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "We have no sensitive data, so security doesn't apply" | Injection flaws and SSRF can compromise the underlying server even when the application itself holds no sensitive data, giving attackers a foothold into the broader network. |
| "The framework handles security for us" | Frameworks prevent common pitfalls but cannot prevent IDOR — a developer must still verify ownership before returning a record. Dozens of real-world breaches (e.g., Optus 2022) happened despite using secure frameworks. |
| "We'll add security later before launch" | Security findings discovered post-architecture (e.g., algorithm confusion in JWT, hardcoded secrets) require far more rework than findings caught during initial development. |
| "Our internal API isn't internet-facing so OWASP doesn't apply" | Insider threats and supply chain compromises mean internal APIs are regularly attacked; the Capital One breach in 2019 originated from an internal SSRF call. |
| "We passed a pentest last quarter, so we're fine" | A pentest is a point-in-time snapshot; new code paths, dependency CVEs, and configuration changes introduced after the test are not covered. |
| "Race conditions only matter at scale" | Check-Then-Act race conditions in balance deduction logic have been exploited at low request volumes via simple two-tab browser attacks, enabling duplicate payments and negative balances. |

## Verification

- [ ] In-scope domains checked; full audits mark other domains not applicable with reasons
- [ ] Available appropriate dependency scan evidence recorded; missing tooling is disclosed, not automatically installed
- [ ] Configured static-analysis findings reviewed, or the exact coverage limitation recorded
- [ ] Every finding includes severity (P0-P3), exploitability assessment, and remediation code
- [ ] OWASP Top 10 items are explicitly mapped to findings or marked "not applicable" with justification
- [ ] Race condition sub-categories (9a shared state, 9b TOCTOU, 9c database, 9d distributed) each addressed

## Related Modules

- [context-engineering](../context-engineering/MODULE.md) — relevant project context
- [code-review-and-quality](../code-review-and-quality/MODULE.md) — quality, performance, tests, and report
- [verification-before-completion](../verification-before-completion/MODULE.md) — support claims with actual evidence

Discover optional specialist tooling by capability; do not invoke uninstalled phase/skill aliases.

---

**Version**: 2.0.0
**Last Updated**: February 2026
**Based on**: DevAI-Hub code review methodology + code-review-expert


### Iterative Refinement Strategy
This skill is optimized for an iterative approach:
1. **Execute**: Perform the core steps defined above.
2. **Review**: Critically analyze the output (coverage, quality, completeness).
3. **Refine**: If targets aren't met, repeat the specific implementation steps with improved context.
4. **Loop**: Continue until the definition of done is satisfied.
