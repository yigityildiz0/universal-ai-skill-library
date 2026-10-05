# Physiotherapy documentation framework

## Mandatory draft and integrity boundary

Every generated note must start exactly:

`DRAFT — clinician verification required`

AI output is an editable aid, not a final legal or billing record. The responsible clinician must compare it with the actual encounter and source record before any lawful use.

- Never backdate, authenticate, sign, finalize, or submit a note or billing item.
- Never claim or imply that an encounter, examination, intervention, consent, attendance, adverse event review, handoff acceptance, or clinician verification occurred unless that fact was supplied and is supported by the source record.
- Never create a certification, clearance, official referral acceptance, or submission-ready record.
- Never invent, validate, or select a billing code as if confirmed. If the user explicitly needs coding support, provide only `POSSIBLE CODE — authorized reviewer must verify`, tied to documented facts and current local rules.
- Keep every unknown field visibly marked. Do not fill it with a plausible default.
- Name the responsible clinician role that must verify the draft; do not impersonate that person or add a signature.

## Source anchors

- [World Physiotherapy documentation and records management](https://world.physio/guideline/records-management) covers examination/assessment, evaluation, diagnosis, prognosis/plan, intervention, response, status change, re-examination, and discharge; it emphasizes confidentiality and applicable national/local requirements.
- [APTA documentation](https://www.apta.org/your-practice/documentation) separates initial examination/evaluation, visit, re-examination, and conclusion-of-episode records. Its legal, payer, and terminology context is US-specific unless independently applicable.
- [WHO ICF](https://www.who.int/classifications/international-classification-of-functioning-disability-and-health) provides a common functioning framework.

## Core record types

### Initial examination/evaluation

- reason for encounter/referral and patient goals;
- relevant history, systems review, medications, precautions, prior function, context;
- tests/measures and standardized baseline;
- safety screen and referral/consultation decision;
- physiotherapy problem representation/diagnosis as locally permitted;
- prognosis range, goals, plan of care, frequency/duration rationale;
- options, consent, education, and planned reassessment.

### Encounter/visit note

- status change and interval events;
- safety/precaution check;
- intervention and actual dose;
- assistance, equipment, cueing, modification;
- response during/after, adverse event, and education;
- progress toward goals and next action.

### Re-examination/progress

- standardized comparison under the same protocol;
- meaningful change versus measurement error/important change when supported;
- goal status and patient perspective;
- adherence/exposure and barriers;
- revised hypothesis, prognosis, goals, and plan with rationale.

### Discharge/conclusion

- reason and status at conclusion;
- outcome and goal comparison;
- remaining limitation/risk;
- self-management, equipment, referrals, follow-up, and safety-net;
- patient/caregiver understanding and transition responsibility.

### Referral/consultation/handoff

Use a concise structure such as situation, relevant background, assessment/findings, concern, action already taken, and explicit request/recommendation. Include urgency and contact pathway according to local policy. Do not imply another professional accepted the handoff unless confirmed.

## Integrity rules

- Use `patient reports`, `observed/measured`, `clinician interpretation`, and `plan` labels when ambiguity is possible.
- Keep laterality, units, time, instrument version, assistance, device, and testing conditions consistent.
- Do not carry forward a finding without confirming it for the current encounter.
- Mark `not assessed`, `not provided`, or `unable to assess`; never turn a blank into normal.
- Record uncertainty and competing hypotheses when relevant.
- Document the reason for deviation from protocol or evidence-based plan.

## Privacy and data minimization

Use the minimum necessary data. Before external processing, remove names, identity/record numbers, exact dates/addresses, contact details, faces, DICOM/EXIF metadata, and unnecessary institution/clinician identifiers. Follow current local health-data law, security, access, retention, correction, and disposal requirements.

For Türkiye, health and sexual-life data are special-category personal data; verify current [KVKK official guidance](https://www.kvkk.gov.tr/Icerik/8184/Ozel-Nitelikli-Kisisel-Verilerin-Islenmesine-Iliskin-Rehber). Do not treat this repository as legal advice.

## AI-assisted draft check

The responsible clinician must verify:

- every fact against the encounter/source record;
- clinical reasoning and safety;
- scope, local terminology, mandatory fields, consent, and authentication;
- that no generated phrase overstates examination, causation, diagnosis, or outcome;
- that the final note reflects the patient's voice and actual shared decision.

Only the authorized responsible clinician—not the model—may remove the draft label after completing all required checks under applicable institutional and legal rules.
