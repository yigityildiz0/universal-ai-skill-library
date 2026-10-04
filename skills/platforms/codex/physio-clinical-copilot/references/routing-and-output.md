# Routing and output contract

## Depth selector

| Mode | Use when | Minimum output |
|---|---|---|
| Quick explanation | Stable anatomy or terminology question without a current clinical decision | Direct explanation + only necessary glossary |
| Evidence answer | Effectiveness, safety, comparison, dose, guideline, or prognosis | Structured question + current search + certainty + clinical translation |
| Paper appraisal | A specific publication or document is supplied/named | Design-specific appraisal + evidence passages + applicability |
| Case reasoning | Symptoms, examination, surgery, injury, or rehabilitation plan | Safety first + hypotheses + ICF + goals + options + reassessment |
| Measurement decision | Test/scale or change-detection choice | Construct/purpose + population match + properties + feasibility |
| Program design | A safe case formulation already exists | Phase/session plan + dose provenance + progression/regression/stop rules |
| Patient communication | A patient-facing explanation or handout is requested | Plain language + options + teach-back + safety-net |
| Documentation | A record, handoff, referral, or discharge artifact is requested | Traceable facts + reasoning + outcome change + plan; no fabrication |
| Learning/CPD | Professional growth or journal club | Competency gap + learning activity + practice transfer + evidence of impact |

## Required labels

- **GRADE-informed rapid assessment—not a formal GRADE process** when independent duplicate review and a full protocol were not completed.
- **Abstract only** when the full text was unavailable.
- **Study dose—not an individual prescription** for research dosage.
- **No evidence found in the searched sources** rather than “ineffective” when the search is empty.
- **Conflicting evidence** when direction or magnitude differs; explain PICO and method differences.
- **Translation is not endorsement** when translating clinical instructions or claims.

## Internal module context object

Carry only the fields the next module needs:

- `question_type`
- `population_and_setting`
- `safety_status`
- `patient_priorities`
- `PICO_or_equivalent`
- `target_constructs_and_outcomes`
- `evidence_summary_and_certainty`
- `dose_provenance`
- `constraints_and_preferences`
- `reassessment_and_stop_rules`
- `jurisdiction_and_role_if_relevant`

Never pass identifying patient data to another module, tool, or external search.
