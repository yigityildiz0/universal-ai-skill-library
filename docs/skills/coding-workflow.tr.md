# coding-workflow

[English](coding-workflow.en.md) · [Türkçe](coding-workflow.tr.md) · [Library](../../README.tr.md)

**Kod sorununu kapsamı belli uygulamaya ve doğrulanmış sonuca dönüştürür.**

## Örnek istek

> Bu başarısız testin nedenini bul ve en küçük güvenilir düzeltmeyi yap.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Software engineering workflow scaled to risk: systematic debugging, implementation plans and architecture, code review and security review, test-driven development, verification before claiming done, git commits, pull requests and GitHub CLI, parallel or sub-agent work, long-task context handoffs and interactive browser debugging. Turkish triggers: hata ayıkla, bug çöz, kodu incele, güvenlik açığı, plan çıkar, mimari, test yaz, commit at, PR aç, kodla, düzelt. More triggers: yazılım fikrini birlikte düşünelim, tasarımı netleştir, bileşenleri ayır, teknik trade-off, kalite sorunlarını bul, merge öncesi kontrol, uzun görevin bağlamını koru, durum özeti ve devir, geliştirme dalını bitir, gh ile kontrol et.

</details>

## Çalışma mantığı

Mevcut projeyi inceler; sorunu yeniden üretir veya daraltır; odaklı değişiklik yapar; ilgili testleri çalıştırır.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/coding-workflow/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [ambiguity-detector](../../skills/common/coding-workflow/modules/ambiguity-detector/MODULE.md) | Detect ambiguous, incomplete, or contradictory requirements and specifications with structured clarification templates. Use when reviewing requirements, user stories, API specifica |
| [architecture-design](../../skills/common/coding-workflow/modules/architecture-design/MODULE.md) | System architecture design including requirements analysis, trade-off evaluation, ADRs, and system decomposition. Use when designing new systems, evaluating architectures, or docum |
| [brainstorming](../../skills/common/coding-workflow/modules/brainstorming/MODULE.md) | brainstorming |
| [code-review-and-quality](../../skills/common/coding-workflow/modules/code-review-and-quality/MODULE.md) | code review and quality |
| [context-engineering](../../skills/common/coding-workflow/modules/context-engineering/MODULE.md) | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when you need to configure rules files and cont |
| [context-manager](../../skills/common/coding-workflow/modules/context-manager/MODULE.md) | Keep long tasks accurate by tracking goals, constraints, decisions, evidence, artifacts, unresolved questions, and context budget through progressive disclosure and verified handof |
| [dispatching-parallel-agents](../../skills/common/coding-workflow/modules/dispatching-parallel-agents/MODULE.md) | Partition and coordinate two or more independent workstreams without duplicating work, leaking expected conclusions, or creating shared-file conflicts. Use for parallel research, m |
| [executing-plans](../../skills/common/coding-workflow/modules/executing-plans/MODULE.md) | Use when you have a written implementation plan to execute in a separate session with review checkpoints |
| [finishing-a-development-branch](../../skills/common/coding-workflow/modules/finishing-a-development-branch/MODULE.md) | finishing a development branch |
| [git-commit](../../skills/common/coding-workflow/modules/git-commit/MODULE.md) | git commit |
| [github-cli-workflows](../../skills/common/coding-workflow/modules/github-cli-workflows/MODULE.md) | Interact with GitHub through an already available `gh` CLI using focused issue, pull-request, CI-run, and API workflows. Use when the user explicitly wants GitHub CLI commands or a |
| [implementation-plan](../../skills/common/coding-workflow/modules/implementation-plan/MODULE.md) | Produce a decision-complete, repository-grounded implementation plan with scope, architecture, file-level changes, data/API impacts, tests, migration, rollout, rollback, risks, and |
| [playwright-interactive](../../skills/common/coding-workflow/modules/playwright-interactive/MODULE.md) | playwright interactive |
| [receiving-code-review](../../skills/common/coding-workflow/modules/receiving-code-review/MODULE.md) | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical rigor and verificati |
| [requesting-code-review](../../skills/common/coding-workflow/modules/requesting-code-review/MODULE.md) | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| [security-review](../../skills/common/coding-workflow/modules/security-review/MODULE.md) | security review |
| [subagent-driven-development](../../skills/common/coding-workflow/modules/subagent-driven-development/MODULE.md) | Execute an implementation plan through bounded implementer and independent reviewer agents with disjoint write ownership, explicit handoffs, evidence gates, and integration tests.  |
| [systematic-debugging](../../skills/common/coding-workflow/modules/systematic-debugging/MODULE.md) | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes. Turkish triggers: sistematik hata ayıklama, log ve kanıtla kök neden bul, tahmin etmede |
| [task-coordinator](../../skills/common/coding-workflow/modules/task-coordinator/MODULE.md) | Coordinate complex multi-step tasks by breaking them down into manageable subtasks with dependency tracking. Covers multi-agent architectural patterns (supervisor, swarm, hierarchi |
| [test-driven-development](../../skills/common/coding-workflow/modules/test-driven-development/MODULE.md) | test driven development |
| [using-git-worktrees](../../skills/common/coding-workflow/modules/using-git-worktrees/MODULE.md) | using git worktrees |
| [verification-before-completion](../../skills/common/coding-workflow/modules/verification-before-completion/MODULE.md) | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any succ |
| [writing-plans](../../skills/common/coding-workflow/modules/writing-plans/MODULE.md) | Use when you have a spec or requirements for a multi-step task, before touching code |
