# UX Writing

Write from the reader's side of the interface. Preserve the product's established terminology and brand voice when they remain clear and appropriate.

## Voice and tone

- Use one consistent product voice. Let tone vary with stakes.
- Success, onboarding, and empty states may be warm.
- Routine controls and settings stay neutral and brief.
- Errors and destructive actions stay calm, direct, and free of jokes.
- Security and data-loss messages are explicit.
- Address the reader directly when instructions need a subject. Avoid first-person or “we” when it obscures responsibility or recovery.

## Controls and flows

- Start action labels with a specific verb: “Save draft,” “Delete project,” “Send message.”
- Consequential confirmations repeat the consequence. Use “Delete project” and “Cancel,” not “Yes” and “No.”
- Keep one vocabulary through a flow. Do not alternate “Next,” “Continue,” and “Proceed” without a reason.
- Links describe their destination out of context. Replace “Click here” and repeated bare “Learn more” with specific labels.
- Label toggles for the enabled state: “Send read receipts,” not “Don't disable read receipts.”
- Prefer sentence case unless the product has a deliberate, consistent alternative.

## Plain and localizable language

- Prefer familiar, concrete words over clever copy, idioms, and filler.
- Name what people recognize and control, not internal implementation.
- Use “select” when the interface supports both touch and pointer; use device-specific verbs only when the device is known.
- Avoid assembling sentences from translated fragments. Use full localized templates and plural rules.
- Keep source text in natural case and use CSS for visual casing.
- Do not add unnecessary gender or culture-specific humor.

## Errors

An error states:

1. what failed;
2. what the reader can do next;
3. where the fix belongs.

Place field errors beside the field. Use positive, actionable instructions such as “Use at least 8 characters.” Avoid blame, “Oops,” exclamation marks, and vague “Something went wrong” messages.

If the same error repeatedly affects many people, improve the interaction rather than endlessly rewriting the message.

## Empty and loading states

- An empty state says what the area is, why it is useful when needed, and the next action.
- Search/filter emptiness names the query or filter and offers an exit.
- Never place persistent critical guidance only in an empty state because it disappears once content exists.
- Loading labels use the product's punctuation convention and remain distinguishable from failure.

## Forms

- Placeholders demonstrate expected format; they do not replace labels.
- Hints appear before the error when the constraint can be explained in advance.
- Keep labels, help text, validation, button text, and success messages on the same vocabulary.

## Review checks

Inspect nearby copy, localization files, variable interpolation, plurals, destructive flows, error recovery, narrow-width wrapping, and screen-reader link lists. Treat a difference from generic plain language as a finding only when it creates ambiguity, inconsistency, translation risk, or an inappropriate tone.
