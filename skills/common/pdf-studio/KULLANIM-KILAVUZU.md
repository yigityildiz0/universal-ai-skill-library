# PDF Studio — Kullanım Kılavuzu

## Ne işe yarar?
Herhangi bir konuda PDF hazırlarken yapay zekânın sık yaptığı hataları önler:
- tablo, görsel veya kutunun iki sayfaya bölünmesi,
- başlığın sayfa sonunda tek kalması,
- yazının kenardan taşması veya üst üste binmesi,
- Türkçe harflerin (ı, ğ, ş, İ) kareye dönmesi,
- bulanık görsel, çok küçük yazı, boş sayfa, eksik sayfa numarası.

İçeriği kısaltmaz, tasarımı sıkıştırmaz: önce sorar, sonra kurallı şablonla üretir, sayfa sayfa denetler.

## Nasıl istenir?
Sadece "… için PDF hazırla" yaz. Skill önce tek mesajda şunları sorar (cevapladığın soruyu tekrar sormaz):
1. Ne için? (kendi çalışmam, gönderilecek, yazdırılacak, ekran…)
2. Dikey mi yatay mı? (A4 varsayılan)
3. Tasarım dili: konuya uygun 3–4 seçenek (Akademik sade, Klinik temiz, Editoryal, Teknik rapor, Modern kartlı, Minimal).
4. İçerik nereden gelecek? (dosyalarım / araştırarak / ikisi)
5. Uzunluk ve yapı: sayfa sayısı, kapak, içindekiler, kaynakça.
"Sen karar ver" dersen en uygununu seçer ve tek satırda söyler.

Hızlı kalıp: `A4 dikey, Klinik temiz, 6 sayfa, kaynaklı, kapak yok: <konu> özeti PDF`.

## Ne olur?
1. HTML/CSS ile belge yazılır (`print.css` + seçtiğin tema).
2. `html_lint.py` kuralları kontrol eder.
3. `build_pdf.py` Edge/Chrome ile PDF üretir.
4. `pdf_audit.py --render` sayfaları PNG'ye çevirir; taşma, bölünen tablo, yalnız kalan başlık, bozuk harf, gömülmeyen font bakar.
5. Her sayfa görüntüsü okunur, hata varsa kaynağı düzeltilir (puntoyu küçültmek yerine).
6. Teslimde sayfa sayısı, yön, yazı tipleri ve kontrol edilemeyenler yazılır.

## Kurala ters istek
"6 puntoyla tek sayfaya sığdır" gibi bir istek skill kuralıyla çelişirse kısa soru gelir: kural mı, istek mi; bu belge için mi, kalıcı mı.

## Kurulum notu
Geometri denetimi için bir kez: `python -m pip install pymupdf`. Yoksa denetim kısıtlı çalışır ve bunu söyler.

## Dosyalar
`SKILL.md`, `references/` (sorular, tasarım dilleri, düzen kuralları, yapay zekâ hata listesi, motorlar), `assets/pdf-kit/` (print.css, themes.css, template.html), `scripts/` (build_pdf.py, pdf_audit.py, html_lint.py).
