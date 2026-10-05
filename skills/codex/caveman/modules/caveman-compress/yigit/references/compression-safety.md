# Compression safety policy

## Semantic ledger

Before drafting, list the source's distinct:

1. facts, decisions, owners, actors, and scope;
2. requirements, prohibitions, permissions, and priorities;
3. conditions, exceptions, fallback behavior, and step order;
4. causal claims, uncertainty, severity, and unresolved questions;
5. dates, versions, quantities, units, thresholds, identifiers, and names;
6. paths, commands, URLs, citations, code, and examples that carry unique
   meaning.

Map every ledger item to the candidate. Shorter wording is allowed; deletion,
polarity change, stronger/weaker obligation, reordered dependency, and
invented certainty are not.

## Preserve byte-level content

Keep these exact:

- YAML/frontmatter, including delimiters and ordering;
- fenced and indented code blocks;
- inline-code spans;
- URLs, Markdown link destinations, and file-system paths;
- headings and ordered/unordered list structure;
- table count, header rows, row count, column count, and alignment markers;
- numeric literals with versions, dates, units, percentages, and ranges;
- negation and constraint phrases such as `not`, `never`, `only`, `unless`,
  `before`, and `after`.

If exact preservation prevents useful compression, keep the original passage.

## Candidate rules

- Remove greetings, filler, repeated conclusions, and redundant examples.
- Prefer familiar short words and complete causal statements.
- Do not invent acronyms or replace prose with ambiguous symbols.
- Keep one example only when the removed examples add no unique edge case.
- Preserve the user's language and terminology.
- Never compress warnings, approval language, or destructive-operation
  consequences into fragments.

## Validation interpretation

The script compares structure and protected token multisets. A pass means those
mechanical invariants survived; it does not certify meaning.

Treat any of these as a stop condition:

- a ledger item has no candidate mapping;
- the diff changes who must act or when;
- a condition, exception, negation, number, or risk level is less explicit;
- the candidate is shorter only because useful examples or evidence vanished;
- source context is too specialized to review confidently.

In a stop condition, leave the source untouched and report the uncertainty.
