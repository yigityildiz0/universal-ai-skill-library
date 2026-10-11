# primary-source-research

[English](primary-source-research.en.md) · [Türkçe](primary-source-research.tr.md) · [Library](../../README.tr.md)

**Resmî belge, spesifikasyon, kaynak kodu ve birincil kayıtlardan yanıt üretir.**

## Örnek istek

> Bu API davranışını resmî doküman ve kaynaktan doğrula.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Answer research questions from primary sources: official docs, specifications, source code and first-party records. Return cited findings in chat; create a repository memo only when requested. TR: resmi dokümandan araştır, API nasıl çalışıyor, birincil kaynaktan doğrula, kaynaklı not dosyası çıkar.

</details>

## Çalışma mantığı

İddiayı taşıyan birincil kaynağı bulur; ilgili bölüm/sürümü inceler; çelişkileri karşılaştırır; kaynaklı yanıt veya istenen notu üretir.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/primary-source-research/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
