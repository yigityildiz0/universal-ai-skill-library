# ai-agent-builder

[English](ai-agent-builder.en.md) · [Türkçe](ai-agent-builder.tr.md) · [Library](../../README.tr.md)

**Skill, ajan iş akışı ve MCP entegrasyonu geliştirir, inceler ve bakımını yapar.**

## Örnek istek

> Bu skill paketini incele; özellik kaybetmeden yönlendirmesini iyileştir.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Builds and maintains AI tooling: writes, merges, ports and audits skills and plugins, security-checks downloaded skill packages, builds MCP servers and ChatGPT Apps SDK apps, converts Claude Code agent kits for Codex, audits context and skill budgets, and compares AI models, providers and subscriptions for a task. Turkish triggers: skill yaz/düzenle/birleştir, eklenti kur, bu skill güvenli mi, MCP sunucusu yap, ChatGPT app, hangi model daha iyi, Claude mu ChatGPT mi, context şişti. More triggers: becerileri karşılaştır, tetikleyiciyi düzelt, kaliteyi koruyarak güncelle, skill senkronla, guardrail ve komutları uyarla, API karşılaştır, yerel mi bulut mu.

</details>

## Çalışma mantığı

Yazım, güncelleme, güvenlik veya entegrasyon modülünü seçer; ortamı inceler; sınırlı değişikliği doğrular.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/ai-agent-builder/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [ai-model-route-evaluator](../../skills/common/ai-agent-builder/modules/ai-model-route-evaluator/MODULE.md) | Compare current AI models, providers, gateways, subscriptions, local routes, and free/paid endpoints for a concrete task. Evaluate exact model identity, modality, Turkish and multi |
| [chatgpt-apps](../../skills/common/ai-agent-builder/modules/chatgpt-apps/MODULE.md) | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools. Turkish triggers: ChatGPT  |
| [codex-agent-dev-kit](../../skills/common/ai-agent-builder/modules/codex-agent-dev-kit/MODULE.md) | Convert Claude Code agent-kit setups into Codex-compatible skills, project instructions, guardrail scripts, command workflows, and subagent guidance. Use when migrating an agent ki |
| [context-budget](../../skills/common/ai-agent-builder/modules/context-budget/MODULE.md) | Audit actual context consumption and routing overhead across instructions, skill metadata and bodies, tool schemas, agent definitions, conversation output, and project files. Use w |
| [mcp-builder](../../skills/common/ai-agent-builder/modules/mcp-builder/MODULE.md) | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers  |
| [safe-skill-updater](../../skills/common/ai-agent-builder/modules/safe-skill-updater/MODULE.md) | Audit, compare, merge, repair, or improve user-owned Codex and ChatGPT skill variants while preserving proven behavior. Use for skill regression analysis, semantic diffs, trigger r |
| [skill-package-security-audit](../../skills/common/ai-agent-builder/modules/skill-package-security-audit/MODULE.md) | Perform a static, read-only security and trust preflight on a downloaded or third-party skill, plugin, ZIP, repository, installer, or update. Use before import, installation, execu |
| [writing-skills](../../skills/common/ai-agent-builder/modules/writing-skills/MODULE.md) | Create, edit, split, merge, port, or validate agent skills and SKILL.md packages. Use for skill architecture, trigger descriptions, supporting references/scripts, host variants, re |
