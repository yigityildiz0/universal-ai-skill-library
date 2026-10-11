# physio-clinical-copilot

[English](physio-clinical-copilot.en.md) · [Türkçe](physio-clinical-copilot.tr.md) · [Library](../../README.md)

**Support clinician-reviewed rehabilitation reasoning, assessment and draft planning.**

## Try it

> Draft an assessment framework for this rehabilitation case and identify missing information.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Physiotherapy/FTR clinical copilot for patient cases: triage and red flags, clinical reasoning and ICF, differential hypotheses, goals and prognosis, rehabilitation exercise and home programs (dose, progression, stop rules), outcome measures and special tests (reliability, MCID), patient education, SOAP/progress/discharge documentation and professional development. Turkish triggers: vakayı analiz et, fizyoterapi/FTR vakası, rehabilitasyon veya egzersiz programı yaz, hangi test/ölçek, hastaya anlat, SOAP notu, epikriz, değerlendirme formu. More triggers: klinik akıl yürütme, kırmızı bayrak, ev programı, hedef ve prognoz. Short TR/EN requests: fizyo / physio; fizyoterapi / physiotherapy. Fizyo: vakayı analiz et; physio: assess case; rehabilitasyon / rehabilitation.

</details>

## How it works

Organize the case; check red flags; select relevant assessment/outcomes; connect evidence to a draft and document uncertainty.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/physio-clinical-copilot/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [physio-clinical-reasoning](../../skills/common/physio-clinical-copilot/modules/physio-clinical-reasoning/MODULE.md) | Structure safety-first, evidence-based physiotherapy reasoning for a patient case. Use for vaka/case prompts involving symptoms, examination findings, surgery or injury, triage, di |
| [physio-documentation](../../skills/common/physio-clinical-copilot/modules/physio-documentation/MODULE.md) | Draft accurate, traceable physiotherapy documentation from supplied facts. Use for initial evaluation, visit/daily note, re-examination/progress report, discharge or episode summar |
| [physio-outcome-measures](../../skills/common/physio-clinical-copilot/modules/physio-outcome-measures/MODULE.md) | Select and compare physiotherapy PROMs, ClinROMs, performance tests, and diagnostic special tests using population-specific evidence. Use for test/ölçek selection, baseline or chan |
| [physio-patient-education](../../skills/common/physio-clinical-copilot/modules/physio-patient-education/MODULE.md) | Create safe, accessible, evidence-aligned physiotherapy patient education and shared-decision materials. Use for plain-language explanations, diagnosis/rehabilitation expectations, |
| [physio-professional-development](../../skills/common/physio-clinical-copilot/modules/physio-professional-development/MODULE.md) | Build evidence-based physiotherapy professional development, research, and practice-improvement plans. Use for competency self-audit, CPD portfolio, learning goals, literature watc |
| [physio-program-design](../../skills/common/physio-clinical-copilot/modules/physio-program-design/MODULE.md) | Convert a safe physiotherapy case formulation and evidence summary into a reproducible rehabilitation program. Use for exercise prescription, FITT-VP, treatment phase/session desig |
