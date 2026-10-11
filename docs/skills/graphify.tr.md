# graphify

[English](graphify.en.md) · [Türkçe](graphify.tr.md) · [Library](../../README.tr.md)

**Bilgi grafıyla kod, belge ve araştırma arasındaki ilişkileri anlamaya yardımcı olur.**

## Örnek istek

> Mevcut grafı kullanarak bu modül değişikliğinin etkisini açıkla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Build, update, query or explain a persistent knowledge graph when graphify is requested explicitly, or consult an existing graphify-out/graph.json for relevant codebase, architecture and file-relationship questions. Ordinary code review or read-only audits do not require installation or graph generation. Supports code, docs, papers, images and videos, community detection, query/path/explain tools. TR: graphify kullan, bilgi grafiği oluştur, mevcut grafiği sorgula.

</details>

## Çalışma mantığı

Mevcut graf/ortamı inceler; ilgili ilişkileri sorgular; çıkarılan olguyla tahmini ayırır; görev kapsamındaki güncellemeyi yapar.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/graphify/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
