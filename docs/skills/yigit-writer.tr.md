# yigit-writer

[English](yigit-writer.en.md) · [Türkçe](yigit-writer.tr.md) · [Library](../../README.tr.md)

**Olgusal anlamı değiştirmeden açık mesaj, yazı ve akademik metin üretir/düzenler.**

## Örnek istek

> Bu mesajı teknik terim ve sayıları koruyarak doğal Türkçeyle düzenle.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Writes and rewrites the user's messages and texts: email, WhatsApp, SMS, DM, complaint, request, follow-up, school, teacher, hospital and company messages; prepares difficult conversations; builds a personal writing-style profile; drafts sourced articles, blog posts and long-form content; keeps a brand voice consistent; removes AI-sounding writing patterns. Turkish triggers: ne yazayım, mesajı düzelt, daha kibar/sert yaz, mail yaz, nasıl söyleyeyim, zor konuşma, sınır koy, blog/makale yaz, üslubumu çıkar. More triggers: yapay zeka gibi durmasın, doğal yaz, marka dili, ses tonu, üslup rehberi, kaynaklı içerik yaz, taslağı geliştir, konuşmayı prova yap, mesajın etkisi ne olur.

</details>

## Çalışma mantığı

Kitle ve amacı belirler; verilen bilgi/üslubu korur; yazar/düzenler; anlam, isim, miktar ve desteksiz iddiaları kontrol eder.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/yigit-writer/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [ai-writing-detox](../../skills/common/yigit-writer/modules/ai-writing-detox/MODULE.md) | Eliminates AI-generated writing patterns that erode reader trust. Use when writing or editing articles, docs, or press releases. |
| [brand-voice](../../skills/common/yigit-writer/modules/brand-voice/MODULE.md) | Define, discover, apply, or audit a brand voice across copy, decks, pages, prompts, and product messaging. Use for tone of voice, messaging consistency, editorial rules, brand lang |
| [content-research-writer](../../skills/common/yigit-writer/modules/content-research-writer/MODULE.md) | Automatically help plan, research, draft, cite, and revise a substantial blog post, article, newsletter, tutorial, case study, thought-leadership piece, or sourced long-form conten |
| [difficult-conversation-prep](../../skills/common/yigit-writer/modules/difficult-conversation-prep/MODULE.md) | Prepare a difficult personal or professional conversation: clarify the goal and boundary, map perspectives and likely reactions, choose safe timing/channel, draft an opening and ke |
| [message-writer](../../skills/common/yigit-writer/modules/message-writer/MODULE.md) | Draft, rewrite, shorten, strengthen, or review copy-ready email, WhatsApp, SMS, DM, complaint, request, follow-up, school, healthcare, company, support, or institutional messages.  |
| [setup-writing-style](../../skills/common/yigit-writer/modules/setup-writing-style/MODULE.md) | Build or recalibrate a private, evidence-based writing-style profile from text the user explicitly places in scope. Use when the user asks to analyze/capture their voice across fut |
