# web-ui-design

[English](web-ui-design.en.md) · [Türkçe](web-ui-design.tr.md) · [Library](../../README.tr.md)

**Gerçek görev, hiyerarşi, responsive düzen ve erişilebilirlik etrafında arayüz tasarlar.**

## Örnek istek

> Bu ayar sayfasını küçük ekranda ana eylem açık olacak şekilde yeniden tasarla.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Designs, builds and reviews web and app interfaces: distinctive visual direction (frontend-design), layout, spacing and typography polish per web design guidelines, screenshot-to-code, UX microcopy, accessibility (WCAG) audits, real-browser testing and developer handoff. Styles/palettes/fonts → ui-ux-pro-max; tokens → design-system; Tailwind/shadcn → ui-styling. Turkish triggers: site tasarla, arayüzü güzelleştir, tasarım dengesiz/yamuk, responsive yap, ekran görüntüsünü koda çevir, erişilebilirlik, buton metni, tarayıcıda test et. More triggers: geliştiriciye devret, ölçü ve durumlar, acceptance criteria, UI polish.

</details>

## Çalışma mantığı

Kullanıcı görevini anlar; bilgi/eylemi önceliklendirir; durum/düzen tasarlar; klavye, kontrast ve ekran uyumunu inceler.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/web-ui-design/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [accessibility-review](../../skills/common/web-ui-design/modules/accessibility-review/MODULE.md) | Audit a web, mobile, desktop, document, or product flow for practical accessibility issues using current WCAG 2.2 AA-oriented checks, code, screenshots, and interaction evidence. U |
| [browser-testing-with-devtools](../../skills/common/web-ui-design/modules/browser-testing-with-devtools/MODULE.md) | Test and debug web interfaces in a real browser using whatever browser, DevTools, Playwright, or computer-use capability is already available. Use for DOM, console, network, access |
| [design-handoff](../../skills/common/web-ui-design/modules/design-handoff/MODULE.md) | Create or review a design-to-engineering handoff with intent, responsive behavior, tokens, states, interaction rules, edge cases, assets, acceptance criteria, and open decisions. U |
| [frontend-design](../../skills/common/web-ui-design/modules/frontend-design/MODULE.md) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and making choices that don't rea |
| [ux-copy](../../skills/common/web-ui-design/modules/ux-copy/MODULE.md) | Write or review interface copy for labels, buttons, onboarding, forms, empty states, errors, confirmations, permissions, and help text. Use for UX copy, microcopy, button text, err |
| [visual-reference-to-code](../../skills/common/web-ui-design/modules/visual-reference-to-code/MODULE.md) | Turn a screenshot, generated design reference, or visual brief into a polished responsive interface through measurable visual analysis, implementation, and screenshot comparison. U |
| [web-design-guidelines-workflow](../../skills/common/web-ui-design/modules/web-design-guidelines-workflow/MODULE.md) | Build, improve, or review web and product interfaces as one coherent system across layout and optical balance, accessibility, UX writing, typography, color, surfaces, icons, motion |
