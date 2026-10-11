# ai-image-video-studio

[English](ai-image-video-studio.en.md) · [Türkçe](ai-image-video-studio.tr.md) · [Library](../../README.tr.md)

**Yerel ComfyUI dahil görsel/video üretimini planlar ve sorun giderir.**

## Örnek istek

> Bu ComfyUI akışındaki hatayı bul ve tekrarlanabilir çözüm öner.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

AI image and video production: ComfyUI workflow design and repair (FLUX, SDXL, SD3, Wan, Hunyuan, LTXV, LoRA, ControlNet, IPAdapter, PuLID, inpaint, upscale, img2vid; missing nodes or models, Failed to fetch, VRAM, identity drift), AI product photography, source-preserving image edits and rendered-video QA. Turkish triggers: ComfyUI workflow yap, iş akışını düzelt, node eksik, model bulunamadı, VRAM hatası, ürün fotoğrafı, görseli düzenle, arka planı değiştir, rötuş ve varyasyon, videoyu kontrol et. More triggers: güvenli onarım, workflow'u bozmadan modül ekle, ışık ve kompozisyon, çekim listesi, çözünürlük/ses/kare kontrolü.

</details>

## Çalışma mantığı

Medya hedefi ve ortamı belirler; akış/model uyumunu inceler; planlar veya onarır; gerçek çıktıyı kontrol eder.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/ai-image-video-studio/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [comfyui-workflow](../../skills/common/ai-image-video-studio/modules/comfyui-workflow/MODULE.md) | Automatically design or substantially modify a ComfyUI workflow when the user wants a new image/video pipeline or capability for FLUX, SDXL, SD3, Wan, Hunyuan, LTXV, Mochi, Cosmos, |
| [comfyui-workflow-guardian](../../skills/common/ai-image-video-studio/modules/comfyui-workflow-guardian/MODULE.md) | Automatically audit, repair, refactor, and stabilize an existing ComfyUI workflow or Windows runtime when the user shares workflow JSON, an error/screenshot, or reports startup/que |
| [image-editing-workflow](../../skills/common/ai-image-video-studio/modules/image-editing-workflow/MODULE.md) | Apply a source-preserving workflow to plan, execute, and verify image edits with the active host's approved image-editing capability. Use when the user asks for this workflow or ne |
| [product-photography](../../skills/common/ai-image-video-studio/modules/product-photography/MODULE.md) | Plan, generate, edit, or review AI product photography for e-commerce, packaging, ads, catalogs, and product launches. Use for product photos, packshots, hero images, lifestyle sce |
| [video-delivery-qa](../../skills/common/ai-image-video-studio/modules/video-delivery-qa/MODULE.md) | Inspect, validate, and prepare video deliverables for export or handoff using available local tools such as ffprobe, frame sampling, waveform/audio inspection, captions, and visual |
