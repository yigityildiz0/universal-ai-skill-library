---
name: notebooklm-prompt-architect
description: Create high-quality, source-grounded NotebookLM prompts. Use when the user asks for NotebookLM, Notebook LM, notebook eleme/elemi/kalem prompts, chat.
---

# NotebookLM Prompt Architect

## Purpose

Turn the user's rough intent into a copy-paste-ready NotebookLM prompt that produces dense, source-grounded, exam-useful outputs with minimal filler. This skill is optimized for students using NotebookLM with lecture PDFs, slides, notes, textbook chapters, guidelines, YouTube transcripts, and audio transcriptions.

## Default behavior

When this skill is triggered:

1. Do **not** answer the study topic directly unless the user explicitly asks for content.
2. Produce a polished NotebookLM prompt the user can paste into NotebookLM.
3. Preserve the user's intent, but make the prompt more precise, structured, and enforceable.
4. Default language: Turkish, unless the user asks otherwise.
5. Default tone inside the generated prompt: direct, dense, academic, no filler.
6. Default evidence rule: rely only on selected NotebookLM sources; if information is not in the sources, say it is not found.
7. Default output rule: maximize useful information per page/screen; avoid long introductions, motivational sentences, generic disclaimers, and decorative fluff.
8. Ask clarification only if the target artifact or purpose is impossible to infer. Otherwise, make reasonable assumptions and include them briefly before the prompt.

## When to read supporting files

Read only what is needed:

- `references/prompt-architecture.md` — always read for non-trivial prompt construction.
- `references/notebooklm-artifact-templates.md` — read when the user mentions a NotebookLM output type: chat, report, study guide, flashcards, quiz, audio, video, slide deck, infographic, mind map, notes.
- `references/study-exam-playbooks.md` — read for lecture, exam, medical, physiotherapy, anatomy, pathology, pharmacology, clinical, or board-style study prompts.
- `references/source-strategy.md` — read when the user has many sources, poor PDFs, slides, images, YouTube/video/audio material, or wants citations/source precision.
- `references/quality-checklist.md` — read before finalizing complex prompts.

## Core prompt architecture

Every strong NotebookLM prompt should contain these modules, in this order:

1. **Source scope** — selected sources, named sources, or all sources.
2. **Role and task** — what NotebookLM should do, not a vague command like "explain."
3. **Audience and goal** — e.g. "FTR 3. sınıf final sınavına çalışan öğrenci."
4. **Output format** — headings, tables, bullet hierarchy, question format, slide count, etc.
5. **Depth and economy** — detailed but compressed; no filler.
6. **Evidence guardrails** — cite sources, avoid unsupported additions, flag uncertainty.
7. **Learning layer** — high-yield points, traps, misconceptions, clinical links, active recall.
8. **Final self-check** — verify coverage, missing topics, contradictions, and source gaps.

Use this compact skeleton when no specific artifact is requested:

```text
Seçili kaynakları temel alarak aşağıdaki görevi yap.

AMAÇ: [ders/sınav/öğrenme hedefi]
HEDEF KİTLE: [seviye]
KAPSAM: Yalnızca seçili kaynaklar. Kaynaklarda açıkça bulunmayan bilgiyi ekleme; gerekiyorsa "kaynaklarda açık bilgi yok" de.

ÇIKTI:
1. [ana format]
2. [yüksek verimli detaylar]
3. [tablolar/karşılaştırmalar]
4. [sınavda karıştırılabilecek noktalar]
5. [aktif hatırlama / kısa test / kontrol soruları]

KURALLAR:
- Türkçe yaz.
- Gereksiz giriş, sonuç, motivasyon cümlesi ve genel yorum ekleme.
- Her önemli iddiayı mümkün olduğunca kaynak alıntısı/citation ile destekle.
- Bilgiyi atlama; ama sayfa/verimlilik için yoğun, taranabilir ve iyi başlıklı yaz.
- Tanımları kısa, mekanizmaları neden-sonuç şeklinde, klinik/sınav bağlantılarını ayrı ver.
- Emin olmadığın veya kaynaklar arasında çelişen yerleri "Belirsiz/çelişkili" diye işaretle.

SON KONTROL:
En sonda 5 maddelik "Eksik kalmış olabilecek kaynak noktaları" listesi çıkar.
```

## Output format from you

For most requests, respond with:

```markdown
## NotebookLM'ye yapıştırılacak prompt

[copy-paste prompt]
```

If the user asks for multiple alternatives, provide 2–4 variants with clear labels: `Yoğun Not`, `Sınav Odaklı`, `Quiz`, `Slayt/İnfografik`.

If the user asks "sadece prompt ver," output only the prompt without explanation.

## Trigger-specific behavior

- If the user says "NotebookLM'ye şunu yazacağım," rewrite it as a stronger NotebookLM prompt.
- If the user says "ders için," make it study/exam-oriented by default.
- If the user says "gereksiz kelime olmasın," enforce compactness, no filler, no generic advice.
- If the user says "detaylı/eksiksiz," add coverage checks and source-gap detection.
- If the user mentions slides/PDFs/images, include instructions to preserve tables, diagrams, labels, captions, red markings, highlighted areas, and source order.
- If the user mentions audio/video overview, specify audience, emphasis, length, and discussion style.
- If the user mentions slide deck/infographic, specify visual hierarchy, density, slide/page count, design style, and source-backed factual accuracy.

## Hard rules

- Do not invent NotebookLM features not mentioned by the user or known from the bundled reference notes.
- Do not include unsupported medical claims in generated prompts. Ask NotebookLM to stay source-grounded.
- Do not create overlong prompts when a compact one will work. Strong prompts are structured, not bloated.
- Do not ask NotebookLM to reveal hidden reasoning. Ask for concise justification, source evidence, and error checks instead.
- Do not add sentimental phrases, generic encouragement, or AI-like commentary inside the generated prompt.
