<p align="center"><img src="assets/library-hero.svg" alt="Universal Agent Skill Library compatibility switchboard" width="100%"></p>

<p align="center"><a href="README.md">English</a> · <a href="https://yigityildiz0.github.io/universal-ai-skill-library/">Search all skills</a> · <a href="CATALOG.md">Full table</a> · <a href="INSTALL.md">Install guide</a> · <a href="THIRD_PARTY_NOTICES.md">Licenses</a></p>

# Evrensel Agent Skill Kütüphanesi

Claude Code, OpenAI Codex ve OpenCode için **531 benzersiz Agent Skill adı** içeren, iki dilli ve aranabilir kütüphane. Ortak çekirdeği, küçük host overlay’lerini, tekil ZIP’leri, toplu platform paketlerini, progressive-disclosure router’ını ve 21 çakışan gömülü varyantı sessizce birleştirmeden korur.

| Claude Code | OpenAI Codex | OpenCode | Katalog | Lisans sinyali belirsiz |
|---:|---:|---:|---:|---:|
| 524 | 530 | 525 | 531 | 405 |

## Önerilen toplu indirmeler

[⬇ Claude Code](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude.zip) · [⬇ OpenAI Codex](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex.zip) · [⬇ OpenCode](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode.zip)

Seçilmiş paketler **100 Claude**, **106 Codex** veya **101 OpenCode** üst seviye skill içerir. Her pakette, ilk skill listesini yüzlerce kayıtla doldurmadan gömülü kataloğu gerektiğinde açan `skill-library-router` bulunur.

## Genişletilmiş paketler

[⬇ Claude Code expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude-expanded.zip) · [⬇ OpenAI Codex expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex-expanded.zip) · [⬇ OpenCode expanded](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode-expanded.zip)

Genişletilmiş paketler bütün uyumlu adları doğrudan yükler (524 / 530 / 525). Çevrimdışı arşiv için uygundur; yüzlerce skill’i doğrudan yüklemek keşif metadata bütçesini doldurabilir. Seçilmiş paket veya tekil indirme daha sağlıklıdır.

## Skill bul

- [İngilizce/Türkçe etkileşimli katalog](https://yigityildiz0.github.io/universal-ai-skill-library/) — arama, kategori, platform, risk ve lisans filtresi.
- [Tam İngilizce tablo](CATALOG.md) — her skill, platform davranışı, capability/risk sinyali, lisans ve indirme.
- [Tam Türkçe tablo](CATALOG.tr.md).
- Makine-okur [JSON](manifests/catalog.json) ve [CSV](manifests/catalog.csv).

## Mimari

```text
skills/common/                 taşınabilir ortak çekirdek
skills/platforms/codex/        Codex metadata veya yalnız Codex skill’leri
skills/platforms/opencode/     yalnız OpenCode skill’leri
skills/archive-variants/       çakışan gömülü sürümler; otomatik birleşmez
packages/common/               tekil taşınabilir ZIP’ler
packages/<platform>/           eşleşen host varyantları
release-assets/                yerel release dosyaları; GitHub Releases ile yayınlanır
```

## Güven sınırı

Kaynak katalogdaki `hosts` alanı tek başına runtime uyumluluk kanıtı sayılmaz. Tablo; host terimleri, MCP/slash-command sinyalleri, paket kurulumları, yönetici işlemleri, yıkıcı kalıplar, ağ/API kullanımı ve lisans boşluklarını ayrı ayrı gösterir. Araç yetkisi vermeden önce incele.

**Lisans uyarısı:** birçok pakette yerel lisans veya upstream kaynak işareti yok. Deponun MIT lisansı yalnız katalog, belge, site ve paketleme kodunu kapsar; skill içeriğini kapsamaz. [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) dosyasını oku.
