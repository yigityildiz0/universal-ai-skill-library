# physio-clinical-copilot

[English](physio-clinical-copilot.en.md) · [Türkçe](physio-clinical-copilot.tr.md) · [Library](../../README.tr.md)

**Klinisyen kontrolündeki rehabilitasyon akıl yürütmesi, değerlendirme ve taslak planlamayı destekler.**

## Örnek istek

> Bu rehabilitasyon vakası için değerlendirme çerçevesi hazırla ve eksik bilgileri bul.

## Tetikleme ve yönlendirme

İstek, hostun skill açıklamasıyla eşleştirilir. Host destekliyorsa kanonik adla açık seçim de yapılabilir. Sohbete /ad yazmak tek başına kayıtlı bir komut yaratmaz.

<details>
<summary>Kaynak açıklamasının tam metni</summary>

Physiotherapy/FTR clinical copilot for patient cases: triage and red flags, clinical reasoning and ICF, differential hypotheses, goals and prognosis, rehabilitation exercise and home programs (dose, progression, stop rules), outcome measures and special tests (reliability, MCID), patient education, SOAP/progress/discharge documentation and professional development. Turkish triggers: vakayı analiz et, fizyoterapi/FTR vakası, rehabilitasyon veya egzersiz programı yaz, hangi test/ölçek, hastaya anlat, SOAP notu, epikriz, değerlendirme formu. More triggers: klinik akıl yürütme, kırmızı bayrak, ev programı, hedef ve prognoz. Short TR/EN requests: fizyo / physio; fizyoterapi / physiotherapy. Fizyo: vakayı analiz et; physio: assess case; rehabilitasyon / rehabilitation.

</details>

## Çalışma mantığı

Vakayı düzenler; kırmızı bayrakları kontrol eder; değerlendirme/ölçüt seçer; kanıtı taslağa bağlayıp belirsizliği kaydeder.

Kök giriş dosyası görevi karşılar; yalnız gereken modül ve referanslar yüklenir. Betik içermesi çalıştırıldığı anlamına gelmez. Mevcut araç, veri ve kapsam doğrulandıktan sonra görev yürütülür.

## Girdi, çıktı ve doğrulama

- Girdi: örnek istekteki hedef, ilgili dosya/URL/veri ve sonucu değiştiren kısıtlar.
- Çıktı: isteğe uygun yanıt, plan, taslak veya yetkili dosya değişikliği; dayanak ve belirsizlik açık.
- Doğrulama: yapılan kontrol ile önerilen kontrol ayrı belirtilir; erişilmeyen kaynak veya çalıştırılmayan araç kullanılmış sayılmaz.

## Ortam ve sınırlar

Paket model ağırlığı, izin, hesap veya API kredisi sağlamaz. Bu sürüm mevcut host araçları, açık erişim ve yerel işlemi kullanır; ücretli servis otomatik alternatif değildir. Klinik/yatırım çıktıları profesyonel kararın veya emir işleminin yerine geçmez.

## Modüller ve kaynak

[SKILL.md](../../skills/common/physio-clinical-copilot/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Modül | Kaynak kapsamı |
|---|---|
| [physio-clinical-reasoning](../../skills/common/physio-clinical-copilot/modules/physio-clinical-reasoning/MODULE.md) | Structure safety-first, evidence-based physiotherapy reasoning for a patient case. Use for vaka/case prompts involving symptoms, examination findings, surgery or injury, triage, di |
| [physio-documentation](../../skills/common/physio-clinical-copilot/modules/physio-documentation/MODULE.md) | Draft accurate, traceable physiotherapy documentation from supplied facts. Use for initial evaluation, visit/daily note, re-examination/progress report, discharge or episode summar |
| [physio-outcome-measures](../../skills/common/physio-clinical-copilot/modules/physio-outcome-measures/MODULE.md) | Select and compare physiotherapy PROMs, ClinROMs, performance tests, and diagnostic special tests using population-specific evidence. Use for test/ölçek selection, baseline or chan |
| [physio-patient-education](../../skills/common/physio-clinical-copilot/modules/physio-patient-education/MODULE.md) | Create safe, accessible, evidence-aligned physiotherapy patient education and shared-decision materials. Use for plain-language explanations, diagnosis/rehabilitation expectations, |
| [physio-professional-development](../../skills/common/physio-clinical-copilot/modules/physio-professional-development/MODULE.md) | Build evidence-based physiotherapy professional development, research, and practice-improvement plans. Use for competency self-audit, CPD portfolio, learning goals, literature watc |
| [physio-program-design](../../skills/common/physio-clinical-copilot/modules/physio-program-design/MODULE.md) | Convert a safe physiotherapy case formulation and evidence summary into a reproducible rehabilitation program. Use for exercise prescription, FITT-VP, treatment phase/session desig |
