# caveman

[English](caveman.en.md) · [Türkçe](caveman.tr.md) · [Library](../../README.tr.md)

**Kısa iletişim için resmî Caveman, Ultracave ve Megacave modlarını kullanır.**

## Örnek istek

> /caveman ultra

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

Caveman açık etkinleştirme ister; Ultra, Ultracave modülünü yükler. Durum sorgusu etkinleştirme değildir.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Official Caveman voice and companions: Caveman, Ultra/Ultracave, Wenyan/Megacave, commit, review, compress and code-work patterns. Activate on /caveman, /ultracave, /megacave or explicit Caveman mode request. TR: Caveman modunu aç, Caveman Ultra. Status/audit mentions do not activate it.

</details>

## Çalışma mantığı

Açık mod isteğiyle etkinleşir; yalnız ilgili modu yükler; bilgi/kodu korur; durum ve kapatma davranışını doğru bildirir.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/caveman/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [cavecrew](../../skills/common/caveman/modules/cavecrew/MODULE.md) | cavecrew |
| [caveman](../../skills/common/caveman/modules/caveman/MODULE.md) | caveman |
| [caveman-commit](../../skills/common/caveman/modules/caveman-commit/MODULE.md) | caveman commit |
| [caveman-compress](../../skills/common/caveman/modules/caveman-compress/MODULE.md) | caveman compress |
| [caveman-discover](../../skills/common/caveman/modules/caveman-discover/MODULE.md) | caveman discover |
| [caveman-evidence-review](../../skills/common/caveman/modules/caveman-evidence-review/MODULE.md) | caveman evidence review |
| [caveman-explore](../../skills/common/caveman/modules/caveman-explore/MODULE.md) | caveman explore |
| [caveman-help](../../skills/common/caveman/modules/caveman-help/MODULE.md) | caveman help |
| [caveman-learn](../../skills/common/caveman/modules/caveman-learn/MODULE.md) | caveman learn |
| [caveman-manage](../../skills/common/caveman/modules/caveman-manage/MODULE.md) | caveman manage |
| [caveman-optimize](../../skills/common/caveman/modules/caveman-optimize/MODULE.md) | caveman optimize |
| [caveman-review](../../skills/common/caveman/modules/caveman-review/MODULE.md) | caveman review |
| [caveman-setup](../../skills/common/caveman/modules/caveman-setup/MODULE.md) | caveman setup |
| [caveman-stats](../../skills/common/caveman/modules/caveman-stats/MODULE.md) | caveman stats |
| [investigate-first](../../skills/common/caveman/modules/investigate-first/MODULE.md) | investigate first |
| [lean-build](../../skills/common/caveman/modules/lean-build/MODULE.md) | lean build |
| [megacave](../../skills/common/caveman/modules/megacave/MODULE.md) | megacave |
| [migration](../../skills/common/caveman/modules/migration/MODULE.md) | migration |
| [safe-refactor](../../skills/common/caveman/modules/safe-refactor/MODULE.md) | safe refactor |
| [surgical-patch](../../skills/common/caveman/modules/surgical-patch/MODULE.md) | surgical patch |
| [ultracave](../../skills/common/caveman/modules/ultracave/MODULE.md) | ultracave |
| [verify-and-stop](../../skills/common/caveman/modules/verify-and-stop/MODULE.md) | verify and stop |
