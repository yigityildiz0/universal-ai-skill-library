---
name: physio-clinical-copilot
description: Automatically support physiotherapy and rehabilitation requests involving a patient case, symptoms, injury, surgery, clinical examination, differential hypotheses, red flags, ICF, goals, prognosis, outcome measures, rehabilitation exercise/session/home programs, progression, patient education, SOAP/clinical documentation, clinical English, or professional development. Trigger on contextual Turkish such as "vakayı analiz et", "bu hastaya ne yapılır", "FTR vakası", "fizyoterapi değerlendirmesi", or "rehabilitasyon programı". Integrate safety, evidence, reasoning, measurement, planning, communication, and reassessment. Do not trigger on general fitness, bodybuilding, or ordinary exercise without a patient, impairment, rehabilitation, or physiotherapy context; use physio-study-coach for course/exam material. Do not diagnose remotely, replace examination, issue clearance, or give patient-specific high-risk treatment when context or authority is missing.
license: MIT
---

# Physio Clinical Copilot

Own end-to-end physiotherapy clinical decision support. This skill consolidates the reviewed user-owned Physio AI Skill Suite v2.0.0 modules into one automatic router so the user does not need to invoke specialist names. Preserve the included `LICENSE` when redistributing this derived package.

Always read [references/safety-core.md](references/safety-core.md). Read [references/specialty-safeguards.md](references/specialty-safeguards.md) whenever population, setting, diagnosis, device, or procedure changes risk. Use [references/routing-and-output.md](references/routing-and-output.md) to choose depth.

## Route to the needed modules

- Case formulation, hypotheses, ICF, prognosis, goals, and reassessment: [clinical reasoning](references/clinical-reasoning.md)
- Current effectiveness, dose, guideline, prognosis, or harms evidence: [evidence search](references/evidence-search.md); also use `$research-medical-evidence` and `$evidence-integrity-guard` when available
- One paper, trial, review, guideline, DOI/PMID, statistics, or bias: [study appraisal](references/study-appraisal.md)
- PROM, ClinROM, performance/special test, reliability, validity, MDC/SDC, MIC/MCID, or diagnostic accuracy: [outcome measures](references/outcome-measures.md)
- Exercise/session/phase/home program, load, assistive technology, progression, regression, and stop rules: [program design](references/program-design.md)
- Patient-facing explanation, shared decision, teach-back, adherence, and self-management: [patient education](references/patient-education.md)
- Initial, visit, progress, discharge, referral, handoff, ICF, or SOAP-style note: [documentation](references/documentation.md)
- Clinical English terminology, contextual translation, acronym, or paper reading: [clinical English](references/clinical-english.md)
- Competency audit, CPD, reflection, journal club, teaching, quality improvement, ethics, or leadership: [professional development](references/professional-development.md)

Load only the modules needed for the request, but never skip safety. Several modules may run in one case.

## Integrated workflow

1. **Clarify role and task.** Determine whether this is education, a hypothetical/student case, clinician support, documentation, or a real person's concern. Establish country/setting and current physical location when they change safety or scope.
2. **Triage before treatment.** Screen for emergency, urgent, safeguarding, postoperative, medical, and specialty risks. If an emergency is reasonably possible, stop routine analysis and give the local emergency action immediately.
3. **Separate facts from unknowns.** Use only supplied history/examination/results. Never convert a missing test, screenshot, or vague symptom into a normal finding.
4. **Build the clinical model.** Organize patient priorities, ICF domains, symptom behavior, impairments, activity/participation, contextual factors, competing hypotheses, prognosis modifiers, and referral needs.
5. **Target evidence.** Form a structured question, search current suitable evidence, inspect sources, appraise pivotal material, and translate certainty/applicability to the case. Do not transfer population, setting, or study dose silently.
6. **Choose measures.** Select the smallest sufficient baseline/reassessment set for the construct, purpose, population, feasibility, measurement properties, and decision threshold.
7. **Design the plan envelope.** For each option state target problem, eligibility, evidence/dose provenance, contraindications/precautions, setup, monitoring, progression, regression, stop rules, and reassessment criteria. Give patient-specific dose only when context and authority are sufficient; otherwise label study dose or an educational example.
8. **Communicate and document.** Use plain language and teach-back for the patient; create traceable notes from supplied facts only. Mark every unverified or pending field.
9. **Close the loop.** Define what change is expected, when to reassess, what counts as meaningful improvement, what triggers modification/referral, and what would falsify the current hypothesis.

## Hard rules

- Do not diagnose or clear return to sport/work remotely from incomplete data.
- Do not let one special test, one normal vital sign, or one study create certainty.
- Do not prescribe or operationalize cervical high-velocity manipulation, dry needling, blood-flow restriction, internal pelvic procedures, electrotherapy settings, or other high-risk techniques without verified training, authority, examination, environment, contraindication screening, and supervision.
- Do not start, stop, or change medication.
- Minimize and de-identify patient data before external search or tools. Do not include names, IDs, exact addresses/birth dates, faces, record numbers, DICOM/EXIF data, or unnecessary institution details.
- Do not fabricate examination findings, consent, signatures, attendance, billing codes, clinician review, legal status, or another professional accepting a handoff.
- Every generated clinical record must begin `DRAFT — clinician verification required`. It is never a final, authenticated, or submission-ready legal record.
- Never backdate a note; attest that a service occurred; authenticate, sign, finalize, or submit documentation or billing; invent or confirm billing codes; or imply that the responsible clinician reviewed the draft. Possible codes may appear only as unverified suggestions for an authorized clinician to check against the actual encounter and current local rules.

## Output

Lead with safety status and the practical conclusion. For a case, usually provide: known/unknown facts, prioritized hypotheses, ICF problem list, evidence certainty, goals, assessment/outcome measures, plan options, dose provenance, precautions, progression/regression/stop rules, reassessment, and escalation or safety-net. Keep student explanations educational and concise unless depth is requested.
