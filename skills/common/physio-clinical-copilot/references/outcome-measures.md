# Measurement selection method

> Method status checked 2026-07-22. Verify live tool versions, official forms, translations, and licenses.

## Source order

1. [COSMIN tools and database](https://www.cosmin.nl/cosmin-tools/)
2. [COMET Core Outcome Set database](https://comet-initiative.org/Resources/Database)
3. Current systematic reviews of measurement instruments
4. Original development, validation, responsiveness, and cross-cultural studies
5. Official developer manual, scoring instructions, license, and language version
6. [Rehabilitation Measures Database](https://www.sralab.org/rehabilitation-measures/database) for discovery only; verify claims in original sources

## COSMIN logic

Use the current [COSMIN manual](https://www.cosmin.nl/cosmin-tools/) to separate:

1. risk of bias of each measurement-property study;
2. whether the reported result meets criteria for a sufficient property;
3. certainty of the accumulated evidence.

Do not compute one psychometric total score. Prioritize content validity—relevance, comprehensiveness, and comprehensibility—for the intended construct and population.

## Required property fields

| Property | Record |
|---|---|
| Content validity | Construct definition, relevance, comprehensiveness, comprehensibility, patient/professional input |
| Structural validity | Factor/IRT model, dimensionality, fit, sample adequacy |
| Internal consistency | Alpha/omega and confidence interval only under adequate unidimensionality |
| Reliability | ICC/kappa type and model, confidence interval, retest interval, stability, raters |
| Measurement error | SEM and SDC/MDC method, unit, confidence level |
| Construct validity | Prespecified hypotheses, comparator constructs, results |
| Criterion validity | Defensible gold standard and intended use |
| Cross-cultural validity | Translation process plus invariance/DIF evidence |
| Responsiveness | Change hypotheses, comparator/anchor, follow-up, analysis |
| Interpretability | Score direction, norms, floor/ceiling, MIC/MCID, responder threshold |

Do not apply `alpha ≥ .70` or a 15% floor/ceiling rule as a universal pass/fail law.

## SEM, MDC/SDC, and MIC/MCID

- SEM estimates measurement error for a score; it is not standard error of the sample mean.
- SDC95/MDC95 is often `1.96 × √2 × SEM`; preserve the study's model and units.
- MDC/SDC asks whether change exceeds measurement error.
- MIC/MCID asks whether change is important under a defined anchor/context.
- Prefer `MDC < MIC`, but do not transform either into a universal responder definition.
- Evaluate anchor relevance, interpretability, correlation, follow-up, method, baseline dependency, and uncertainty.

## Diagnostic-accuracy path

Use current [QUADAS-3](https://www.bristol.ac.uk/population-health-sciences/projects/quadas/) for primary diagnostic test-accuracy estimates. STARD is reporting guidance, not a bias tool.

```text
LR+ = sensitivity / (1 - specificity)
LR- = (1 - sensitivity) / specificity
post-test odds = pretest odds × LR
post-test probability = odds / (1 + odds)
```

Use confidence intervals and a prespecified threshold. Examine spectrum, intended role, partial/differential verification, reference-standard bias, blinding, flow/timing, missing data, and threshold selection.

## Performance-test safety

Before gait, balance, step, endurance, maximal/submaximal strength, transfer, or exertional testing, check:

- medical and symptom stability;
- disease-specific monitoring and stop criteria;
- falls/syncope and transfer risk;
- prescribed device, orthosis, oxygen, and assistance;
- environment, space, surface, emergency plan, and trained supervision;
- whether remote administration has been validated and is safe for this person.

A normal single vital sign does not override concerning symptoms.

## Feasibility and language

Report time, items, respondent/evaluator burden, equipment, space, training, cost/license, safety, fatigue, sensory/cognitive/literacy needs, digital access, and repeatability. A linguistic translation alone is not cross-cultural validity. Do not reproduce copyrighted forms or scoring items without permission.

