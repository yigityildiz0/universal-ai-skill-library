# web-animation

[English](web-animation.en.md) · [Türkçe](web-animation.tr.md) · [Library](../../README.tr.md)

**Erişilebilirlik ve mevcut entegrasyonu koruyarak GSAP/Motion örüntüleri uygular.**

## Örnek istek

> Azaltılmış hareket tercihini gözeten sade kaydırma animasyonu ekle.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Scroll and web animation: GSAP ScrollTrigger and Framer Motion/Motion v12 recipes (scroll-triggered reveals, parallax, pinned sections, horizontal scroll, text animations, useScroll/whileInView), plus GSAP timelines/SplitText/Flip/Lenis, 60fps performance, accessible motion, micro-interactions, page transitions, SVG, Lottie. Upstream github/awesome-copilot gsap-framer-scroll-animation + iart-ai/web-animation-skills. Turkish triggers: scroll animasyonu, kaydırınca animasyon, parallax, sabitlenen bölüm, yatay kaydırma, sayfa geçişi, mikro etkileşim, GSAP, Framer Motion, akıcı animasyon.

</details>

## Çalışma mantığı

Kurulu araçları inceler; uygun tarifi seçer; mevcut arayüze entegre eder; hareket tercihi ve performansı değerlendirir.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/web-animation/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [60fps-animation](../../skills/common/web-animation/modules/60fps-animation/MODULE.md) | This skill should be used when the user asks to "fix janky CSS animation", "make animation 60fps", "stop layout thrashing", "animate width/height/top/left smoothly", "convert anima |
| [accessible-animation](../../skills/common/web-animation/modules/accessible-animation/MODULE.md) | This skill should be used when the user asks to "respect prefers-reduced-motion", "honor reduced motion", "make my animations accessible", "fix vestibular / motion-sickness issues" |
| [ascii-animation](../../skills/common/web-animation/modules/ascii-animation/MODULE.md) | This skill should be used when the user asks to "make an ASCII animation", "build a terminal/CLI intro or loader", "convert an image or video to ASCII art", "add an ASCII shader/po |
| [glassmorphism](../../skills/common/web-animation/modules/glassmorphism/MODULE.md) | This skill should be used when the user asks to "add a glassmorphism effect", "frosted glass UI", "Apple liquid glass style", "frosted blur card", "translucent glass panel animatio |
| [gsap-web](../../skills/common/web-animation/modules/gsap-web/MODULE.md) | This skill should be used when the user asks to "build a scroll animation", "add ScrollTrigger", "pin a section while scrolling", "scrub an animation to scroll", "create a hero tim |
| [lottie-animation](../../skills/common/web-animation/modules/lottie-animation/MODULE.md) | This skill should be used when the user asks to "add a Lottie animation", "play a .lottie or .json animation", "integrate a Bodymovin/After Effects animation on web or mobile", "co |
| [micro-interaction](../../skills/common/web-animation/modules/micro-interaction/MODULE.md) | This skill should be used when the user asks to "add a hover/press effect", "animate a toggle or switch", "build an animated like button", "make a toast/snackbar slide in", "animat |
| [page-transition-animation](../../skills/common/web-animation/modules/page-transition-animation/MODULE.md) | This skill should be used when the user asks to "animate page or route transitions", "add a page transition or crossfade between views", "animate route changes in Next.js App Route |
| [svg-animation](../../skills/common/web-animation/modules/svg-animation/MODULE.md) | This skill should be used when the user asks to "animate an SVG", "make a line draw itself on", "do a stroke draw-on / signature animation", "morph one shape into another", "move a |
