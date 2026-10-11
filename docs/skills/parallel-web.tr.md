# parallel-web

[English](parallel-web.en.md) · [Türkçe](parallel-web.tr.md) · [Library](../../README.tr.md)

**Parallel belgelerini korur; bu sürümde ek ücret gerektirmeyen mevcut araştırma araçlarını kullanır.**

## Örnek istek

> Ücretli araştırma servisi eklemeden birden fazla kaynağı araştır.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Use ONLY when the user explicitly asks for Parallel (parallel.ai) or parallel-cli / Parallel Search MCP is configured: web search, URL extraction, deep research reports, FindAll entity discovery, bulk data enrichment, web monitoring, run status/results and setup. Upstream parallel-web/parallel-agent-skills. Turkish triggers: Parallel ile ara, Parallel deep research, Parallel ile listeyi zenginleştir, Parallel ile web'i izle.

</details>

## Çalışma mantığı

Araştırma ihtiyacını belirler; mevcut arama/fetch veya yerel veriyi kullanır; sağlayıcı örneklerini referans tutar; eksik kabiliyeti açıklar.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/parallel-web/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [choose-your-parallel-api](../../skills/common/parallel-web/modules/choose-your-parallel-api/MODULE.md) | Choose the right Parallel API and configuration for cost, latency, and answer quality. Use when adding live web data to an app: current events and prices, a cited answer in a chat, |
| [migrate-to-parallel](../../skills/common/parallel-web/modules/migrate-to-parallel/MODULE.md) | Migrate Exa, Tavily, Perplexity, or Firecrawl web-data integrations completely to the appropriate Parallel products while preserving application behavior. Use when replacing these  |
| [parallel-cli-setup](../../skills/common/parallel-web/modules/parallel-cli-setup/MODULE.md) | Set up and maintain the Parallel CLI (install, auth, balance, skills install) |
| [parallel-data-enrichment](../../skills/common/parallel-web/modules/parallel-data-enrichment/MODULE.md) | Bulk data enrichment. Adds web-sourced fields (CEO names, funding, contact info) to lists of companies, people, or products. Use for enriching CSV files or inline data. Supports mu |
| [parallel-deep-research](../../skills/common/parallel-web/modules/parallel-deep-research/MODULE.md) | ONLY use when user explicitly says 'deep research', 'exhaustive', 'comprehensive report', or 'thorough investigation'. Slower and more expensive than parallel-web-search. For norma |
| [parallel-findall](../../skills/common/parallel-web/modules/parallel-findall/MODULE.md) | Discover entities (companies, people, products, etc.) matching a natural-language description. Use when the user asks to 'find all X' or 'list every Y that…' — e.g., 'Find AI start |
| [parallel-mcp-setup](../../skills/common/parallel-web/modules/parallel-mcp-setup/MODULE.md) | Use when installing, configuring, or troubleshooting an authenticated Parallel Search MCP connection in Bifrost, including gateway-level search settings and downstream tool access. |
| [parallel-memory](../../skills/common/parallel-web/modules/parallel-memory/MODULE.md) | Recall past Parallel Task, Monitor, and FindAll runs when they may help; evict runs or clear memory when asked. |
| [parallel-monitor](../../skills/common/parallel-web/modules/parallel-monitor/MODULE.md) | Continuously track the web for changes on a recurring cadence. Use when the user asks to 'monitor', 'track changes to', 'watch', or 'alert me when' something on the web changes — e |
| [parallel-search-setup](../../skills/common/parallel-web/modules/parallel-search-setup/MODULE.md) | Use when verifying, using, or troubleshooting the anonymous Parallel Search MCP server bundled with this plugin — when the user installs the plugin, says "set up Parallel Search",  |
| [parallel-web-extract](../../skills/common/parallel-web/modules/parallel-web-extract/MODULE.md) | CLI-backed URL extraction. Use when the user explicitly invokes this skill, needs CLI-only controls or saved JSON output, or no Parallel web_fetch MCP tool is available. When the b |
| [parallel-web-search](../../skills/common/parallel-web/modules/parallel-web-search/MODULE.md) | CLI-backed web search. Use when the user explicitly invokes this skill, needs CLI-only controls or saved JSON output, or no Parallel web_search MCP tool is available. When the bund |
| [result](../../skills/common/parallel-web/modules/result/MODULE.md) | Get completed research task result by run ID |
| [status](../../skills/common/parallel-web/modules/status/MODULE.md) | Check running research task status by run ID |
