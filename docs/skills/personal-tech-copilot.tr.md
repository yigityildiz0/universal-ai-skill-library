# personal-tech-copilot

[English](personal-tech-copilot.en.md) · [Türkçe](personal-tech-copilot.tr.md) · [Library](../../README.tr.md)

**Günlük cihaz, uygulama ve kurulum sorunlarını mevcut araçlarla giderir.**

## Örnek istek

> Bu Windows uygulamasının neden açılmadığını teşhis et.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Personal technology help: diagnoses and fixes Windows, macOS, Android and iPhone problems, apps, device setup, compatibility, networking, displays, peripherals, storage, backups and cross-device workflows; read-only PC health checks for slow computers (disk, RAM, CPU, startup); tech purchase compatibility; read-only Harness/DSH GUI health checks. Turkish triggers: nasıl yaparım, neden çalışmıyor, hata veriyor, bilgisayar yavaş, kurulum, ayar, uyumlu mu, telefon veya PC sorunu. More triggers: disk dolu, RAM, başlangıç programları, Wi-Fi, yazıcı, yedekleme, Harness sağlık kontrolü, DSH araç eksik.

</details>

## Çalışma mantığı

Belirti ve ortamı inceler; nedenleri daraltır; kapsamlı olmayan hedefli onarım yapar/önerir; sonucu doğrular.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/personal-tech-copilot/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [computer-health-check](../../skills/common/personal-tech-copilot/modules/computer-health-check/MODULE.md) | Perform a bounded, read-only health check of a Windows, macOS, or Linux computer, covering storage, memory pressure, CPU activity, startup load, battery where available, updates, a |
| [harness-health-check](../../skills/common/personal-tech-copilot/modules/harness-health-check/MODULE.md) | harness health check |
