# yigit-writer

[English](yigit-writer.en.md) · [Türkçe](yigit-writer.tr.md) · [Library](../../README.md)

**Write and revise clear messages, articles and academic prose without changing factual meaning.**

## Try it

> Rewrite this message in natural Turkish while preserving technical terms and numbers.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Writes and rewrites the user's messages and texts: email, WhatsApp, SMS, DM, complaint, request, follow-up, school, teacher, hospital and company messages; prepares difficult conversations; builds a personal writing-style profile; drafts sourced articles, blog posts and long-form content; keeps a brand voice consistent; removes AI-sounding writing patterns. Turkish triggers: ne yazayım, mesajı düzelt, daha kibar/sert yaz, mail yaz, nasıl söyleyeyim, zor konuşma, sınır koy, blog/makale yaz, üslubumu çıkar. More triggers: yapay zeka gibi durmasın, doğal yaz, marka dili, ses tonu, üslup rehberi, kaynaklı içerik yaz, taslağı geliştir, konuşmayı prova yap, mesajın etkisi ne olur.

</details>

## How it works

Identify audience and intent; preserve supplied facts/voice; draft or revise; check meaning, names, quantities and unsupported claims.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/yigit-writer/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [ai-writing-detox](../../skills/common/yigit-writer/modules/ai-writing-detox/MODULE.md) | Eliminates AI-generated writing patterns that erode reader trust. Use when writing or editing articles, docs, or press releases. |
| [brand-voice](../../skills/common/yigit-writer/modules/brand-voice/MODULE.md) | Define, discover, apply, or audit a brand voice across copy, decks, pages, prompts, and product messaging. Use for tone of voice, messaging consistency, editorial rules, brand lang |
| [content-research-writer](../../skills/common/yigit-writer/modules/content-research-writer/MODULE.md) | Automatically help plan, research, draft, cite, and revise a substantial blog post, article, newsletter, tutorial, case study, thought-leadership piece, or sourced long-form conten |
| [difficult-conversation-prep](../../skills/common/yigit-writer/modules/difficult-conversation-prep/MODULE.md) | Prepare a difficult personal or professional conversation: clarify the goal and boundary, map perspectives and likely reactions, choose safe timing/channel, draft an opening and ke |
| [message-writer](../../skills/common/yigit-writer/modules/message-writer/MODULE.md) | Draft, rewrite, shorten, strengthen, or review copy-ready email, WhatsApp, SMS, DM, complaint, request, follow-up, school, healthcare, company, support, or institutional messages.  |
| [setup-writing-style](../../skills/common/yigit-writer/modules/setup-writing-style/MODULE.md) | Build or recalibrate a private, evidence-based writing-style profile from text the user explicitly places in scope. Use when the user asks to analyze/capture their voice across fut |
