# pdf-studio

[English](pdf-studio.en.md) · [Türkçe](pdf-studio.tr.md) · [Library](../../README.tr.md)

**Güvenilir PDF hazırlar: önce sorular, baskıya uygun HTML/CSS ve tasarım dilleri, sayfa sayfa denetim: bölünen tablo, yalnız kalan başlık, taşma ve bozuk harf.**

## Örnek istek

> Bu notlardan A4 dikey, temiz klinik tasarımlı, kaynakçalı bir PDF çalışma kılavuzu hazırla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Make clean, reliable PDFs (study guides, reports, handouts, summaries, CVs, brochures, forms of any topic): asks the right questions first (orientation, purpose, design language, sources), builds from HTML/CSS with print rules so tables, headings and figures never split badly and nothing overflows, then renders and audits every page. Turkish triggers: PDF hazırla, PDF yap, PDF oluştur, rapor PDF, çalışma kılavuzu, el notu, özet PDF, PDF düzenle, sayfa bölünüyor, tablo ikiye bölündü.

</details>

## Çalışma mantığı

Yön, amaç, tasarım dili ve kaynakları sorar; baskı kitiyle kurar; HTML'yi denetler; Edge/Chrome ile çıkarır; sayfaları okuyup denetler; kontrolleri listeleyerek teslim eder.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/pdf-studio/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
