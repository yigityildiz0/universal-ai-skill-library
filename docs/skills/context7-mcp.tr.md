# context7-mcp

[English](context7-mcp.en.md) · [Türkçe](context7-mcp.tr.md) · [Library](../../README.tr.md)

**Mevcut Context7 entegrasyonuyla güncel kütüphane dokümanına ulaşır.**

## Örnek istek

> Bu React entegrasyonunu değiştirmeden güncel API dokümanını kontrol et.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Context7 MCP compatibility guide for explicit Context7 requests, library-ID resolution, query tuning, or hosts without find-docs. General library/framework/API documentation questions route to find-docs first; do not load both for the same lookup. TR: Context7 kullan, Context7 kütüphane kimliği, doküman sorgusunu iyileştir.

</details>

## Çalışma mantığı

Doğru kütüphane/sürümü bulur; odaklı doküman sorgusu yapar; uygulamayı getirilen örneklerle destekler.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/context7-mcp/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
