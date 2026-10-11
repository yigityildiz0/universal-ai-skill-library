# mental-health-crisis-support

[English](mental-health-crisis-support.en.md) · [Türkçe](mental-health-crisis-support.tr.md) · [Library](../../README.tr.md)

**Ruh sağlığı kriz işaretlerine sakin ve güvenlik odaklı yanıt vermeyi destekler.**

## Örnek istek

> Acil tehlikede olabilecek birine destekleyici biçimde nasıl yanıt verebilirim?

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Immediate, supportive, safety-first response when the user or someone else may be at risk of suicide or serious self-harm: wanting to die, a plan or means, or how to help someone in crisis. Turkish triggers: kendimi öldürmek, yaşamak istemiyorum, canıma kıymak, intihar düşüncesi/planı, kendine zarar, arkadaşım intihar edecek. Checks imminent danger and connects to local emergency and crisis help (Türkiye: 112).

</details>

## Çalışma mantığı

Önce acil güvenliği ve açık iletişimi gözetir; yerel kaynaklar için konumu netleştirir; tanı koymuş gibi yapmadan insan desteğine yönlendirir.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/mental-health-crisis-support/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

Bağımsız kök akışı; referanslar giriş dosyasında listelenir.
