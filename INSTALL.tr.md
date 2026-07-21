# Kurulum rehberi

<p align="center"><a href="INSTALL.md"><strong>English</strong></a> · <a href="README.tr.md">README’ye dön</a> · <a href="CATALOG.tr.md">Skill’lere göz at</a> · <a href="https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest">Son sürüm</a></p>

Bu rehber; tekil skill, platform paketi, Windows/macOS/Linux yolları, güncelleme, kaldırma, checksum doğrulaması ve yaygın hataları kapsar.

## Neyi indireceğini seç

| Hedef | İndirme |
|---|---|
| Belirli bir skill kurmak | [CATALOG.tr.md](CATALOG.tr.md) dosyasını aç, skill’i bul ve platform indirmesini kullan. |
| Önerilen başlangıç kütüphanesini kurmak | Aşağıdaki agentına uygun seçilmiş paketi kullan. |
| Her şeyi çevrimdışı saklamak | [Son sürümdeki](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest) genişletilmiş paketi kullan. |

> Kuruluma hazır paket istiyorsan GitHub’ın yeşil **Code → Download ZIP** düğmesini kullanma. O düğme repo kaynak kodunu indirir.

## Platform kökleri

| Agent | Kişisel — macOS/Linux | Kişisel — Windows | Proje |
|---|---|---|---|
| Claude Code | `~/.claude/skills/` | `%USERPROFILE%\.claude\skills\` | `.claude/skills/` |
| OpenAI Codex | `~/.agents/skills/` | `%USERPROFILE%\.agents\skills\` | `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `%USERPROFILE%\.config\opencode\skills\` | `.opencode/skills/` |

Windows’ta `~`, genellikle `C:\Users\<kullanıcı>` olan kullanıcı klasöründür.

OpenCode, Claude ve Codex skill köklerindeki uyumlu skill’leri de tarar. Özel OpenCode paketi kurulumun açık kalması için `.opencode/skills` kullanır.

## Seçilmiş toplu paketi kur

| Agent | Paket |
|---|---|
| Claude Code | [⬇ İndir](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-claude.zip) |
| OpenAI Codex | [⬇ İndir](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-codex.zip) |
| OpenCode | [⬇ İndir](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest/download/universal-ai-skill-library-opencode.zip) |

### Kişisel kurulum

1. Agentına uygun paketi indir.
2. ZIP’i incele ve değiştirdiğin aynı adlı skill klasörlerini yedekle.
3. ZIP’i kullanıcı/ana klasörüne aç. Arşiv `.claude/skills`, `.agents/skills` veya `.opencode/skills` yolunu hazır içerir.
4. Son yapıda `<skills-root>/<skill-adı>/SKILL.md` bulunduğunu doğrula.
5. Skill’ler görünmüyorsa host’u yeniden başlat.

Codex için Windows PowerShell örneği:

```powershell
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\universal-ai-skill-library-codex.zip" -DestinationPath $env:USERPROFILE
```

Codex için macOS/Linux örneği:

```bash
unzip ~/Downloads/universal-ai-skill-library-codex.zip -d "$HOME"
```

### Proje kurulumu

Paketi ana klasör yerine proje köküne aç. Proje kapsamındaki skill’leri yalnız lisansları ve repo politikan izin veriyorsa commit et.

## Tek skill kur

1. [CATALOG.tr.md](CATALOG.tr.md) dosyasını aç.
2. Skill’i bul ve platform indirmesine tıkla.
3. ZIP içindeki `SKILL.md`, script, bağımlılık ve dış servis gereksinimlerini incele.
4. Skill klasörünü doğru kişisel veya proje kökünün altına aç.
5. Şu yapıyı doğrula:

```text
<skills-root>/
└── skill-adı/
    ├── SKILL.md
    ├── references/   isteğe bağlı
    ├── scripts/      isteğe bağlı
    └── assets/       isteğe bağlı
```

- Yanlış: `<skills-root>/skill-adı/skill-adı/SKILL.md`
- Doğru: `<skills-root>/skill-adı/SKILL.md`

## Metadata ve güvenliği doğrula

- Dosya adı tam olarak büyük harfli `SKILL.md` olmalı.
- YAML frontmatter geçerli `name` ve `description` içermeli.
- Klasör adı, frontmatter içindeki `name` ile eşleşmeli.
- Script’i çalıştırmadan önce oku; ZIP’in bu katalogda olması tek başına güvenli olduğunu kanıtlamaz.
- Paket kurulumu, ağ/API erişimi, kimlik bilgisi, yönetici işlemi, silme ve yayınlama ihtiyaçlarını kontrol et.
- Katalogdaki platform eşlemesi, her bağımlılığın o hostta test edildiği anlamına gelmez.

## Checksum doğrula

Windows PowerShell:

```powershell
Get-FileHash .\universal-ai-skill-library-codex.zip -Algorithm SHA256
```

macOS/Linux:

```bash
sha256sum universal-ai-skill-library-codex.zip
```

Sonucu [manifests/SHA256SUMS.txt](manifests/SHA256SUMS.txt) ile karşılaştır. Toplu paketler bu dosyada `release-assets/` altında listelenir.

## Skill veya paket güncelle

1. Yeni sürümü indir.
2. Özellikle yerel değişiklik yaptıysan kurulu kopyayla karşılaştır.
3. Değiştireceğin kesin skill klasörünü yedekle.
4. Yalnız doğruladığın klasörü değiştir veya ad çakışmalarını inceledikten sonra güncel paketi aç.
5. Değişiklik otomatik yüklenmezse host’u yeniden başlat.

Özelleştirilmiş skill’lerin üstüne körlemesine yazma.

## Kaldır

1. Tam skill klasörünü belirle: `<skills-root>/<skill-adı>/`.
2. Kaldırmak istediğin skill’i içerdiğini doğrula.
3. Yalnız bu klasörü dosya yöneticisiyle veya anladığın platforma özgü bir komutla sil.
4. Skill kökünün tamamını silme.
5. Kaldırılan skill önbellekte görünüyorsa host’u yeniden başlat.

## Hata çözümü

### Skill görünmüyor

- Doğru agent kökünü kullandığını kontrol et.
- Çift klasör oluşmadığını kontrol et.
- Dosya adının tam olarak `SKILL.md` olduğunu doğrula.
- YAML frontmatter’ı ve `name` ile klasör adının eşleşmesini kontrol et.
- Özellikle skill kökünü ilk kez oluşturduysan agentı yeniden başlat.

### Skill görünüyor ama çalışmıyor

- [CATALOG.tr.md](CATALOG.tr.md) içindeki platform notunu oku.
- Gerekli yerel araç, runtime, ortam değişkeni, dış servis ve yetkileri kontrol et.
- Biçim uyumluluğu ile çalışmaya hazır olmayı ayrı değerlendir.

### Yüzlerce skill keşfi gürültülü hâle getiriyor

Seçilmiş paketi veya tekil skill’leri kullan. Genişletilmiş arşiv bilinçli çevrimdışı/denetim kullanımı içindir.

### ZIP veya bağlantı yok

[Son sürümü](https://github.com/yigityildiz0/universal-ai-skill-library/releases/latest) aç, asset adını kontrol et ve bozuk URL ile yeniden üretilebilir issue bildir.

## Resmî platform kaynakları

- [Claude Code — skill konumları](https://code.claude.com/docs/en/skills#where-skills-live)
- [OpenAI Codex — skill kaydetme konumları](https://developers.openai.com/codex/skills/#where-to-save-skills)
- [OpenCode — Agent Skills](https://opencode.ai/docs/skills)

Yeniden dağıtmadan önce [LICENSE.md](LICENSE.md) ve [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) dosyalarını oku.
