# Presentation Studio — Ayrıntılı Kullanım Kılavuzu

Bu kılavuz, herhangi bir yapay zekâ uygulamasında (Claude, ChatGPT/Codex, Gemini, OpenCode,
DeepSeek Harness) bu skill ile sunum hazırlatırken ne yazacağını, yapay zekânın hangi sırayla ne
yapacağını, nerede durup ne kontrol edeceğini ve nasıl düzeltme isteyeceğini anlatır.

---

## 1. Kısa özet: ne yapar?

1. Konunu, dersini ve süreyi anlar; hocanın kurallarını varsayılan olarak uygular.
2. Kaynakları doğrular, her sayıyı bir "iddia kartına" bağlar.
3. Slayt slayt plan çıkarır: her slaytın başlığı, öğretim amacı, yerleşim türü ve görseli.
4. Gerçek fotoğrafları lisanslarıyla bulur, konuya göre kırpar. Bulamazsa "şematik" diye etiketli çizim yapar.
5. Hazır tasarım kitiyle düzenlenebilir PPTX üretir. Yazı tipi Calibri; yazılar en az 36 pt
   (kaynak satırı, kaynakça, slayt numarası ve görsel kredisi hariç).
6. Her slayta konuşmacı notu yazar: kısaltmaların okunuşu ve açılımı, araştırmanın yorumu,
   terimler, geçiş cümlesi, süre.
7. Slaytları PowerPoint'te görüntüye çevirip tek tek kontrol eder, hataları düzeltir.
8. Betikle denetler: punto, taşma, yasak ifade, kaynak satırı, süre.
9. Üç dosya teslim eder: Sunum.pptx, Sunum.pdf, Sunum öncesi okuma.pdf.

---

## 2. Hangi uygulamada nasıl?

| Uygulama | Nasıl kurulur | Nasıl çalışır |
|---|---|---|
| **Claude Code / Claude masaüstü** | `sync_skills.py` ile kendiliğinden kurulur | En iyi sonuç. PPTX üretir, PowerPoint'te render alıp kontrol eder. |
| **claude.ai (web)** | Ayarlar → Capabilities/Skills → `presentation-studio.zip` yükle, aç | PPTX üretir; kontrol LibreOffice ile yapılır. Calibri/Arial dışında font kullanma. |
| **ChatGPT / Codex masaüstü** | Codex: `sync_skills.py` kurar. ChatGPT: `ChatGPT/yigit-skills-plugin.zip` eklenti olarak yüklenir | Codex PPTX üretir. ChatGPT web'de Python kiti (`deck_kit.py`) kod aracında çalışır. |
| **Gemini** | Gemini CLI: `~/.gemini/skills/presentation-studio/`. Gemini web: Skills bölümüne klasörü yükle | CLI dosya üretir. Web'de genelde plan + `deck.json` hazırlar, PPTX'i kitle yerelde üretirsin. |
| **OpenCode / DeepSeek Harness** | Masaüstü paket klasöründeki talimat | Kabuk erişimi olduğu için kitlerle PPTX üretir. |

**Codex için önemli:** Çok fazla eklenti açıksa Codex skill listesi kesiliyor ve bu skill görünmeyebilir.
Yeni bir sohbette "Skill listende presentation-studio var mı?" diye sor. Yoksa kullanmadığın
eklentileri kapat (Ayarlar → Eklentiler).

---

## 3. İstek nasıl yazılır? (kopyala, düzenle, gönder)

Slash komutu gerekmez. "sunum hazırla", "slayt hazırla", "PowerPoint yap" demen yeterli.

### 3.1 Ders sunumu (konu anlatımı)
```
Ölçme Değerlendirme dersi için "Kas kuvvetinin nicel değerlendirilmesi" konulu PPTX sunum hazırla.
Süre 30–45 dk. Ders klasörü: <yol>. Hocanın kuralları ve önceki sunum dosyaları orada.
Konuşmacı notlarını, PDF'i ve sunum öncesi okuma PDF'ini de hazırla.
```

### 3.2 Makale sunumu (seminer)
```
Seminer dersi için deri sisteminde son araştırmalar sunumu hazırla (PPTX).
En az 8 makale, 2020 sonrası, uluslararası klinik çalışma; derleme olmasın.
Her makalenin ilk sayfasını göster; amaç–yöntem–değerlendirme–bulgular–tartışma sırasıyla anlat.
```

### 3.3 Vaka sunumu (grup)
```
Klinik problem çözme dersi için spor yaralanması vaka sunumu hazırla (PPTX, 60 dk).
Kısa teori, ICF temelli değerlendirme, iki tarafı karşılaştır, tedaviyi gerekçesiyle anlat.
Görev dağılımını anonim yap (A kişisi, B kişisi). Hasta fotoğrafları klasörde, izinleri alındı.
```

### 3.4 Akademik olmayan sunum
```
Proje ilerleme raporu için 10–12 slaytlık PPTX hazırla. Dinleyici yöneticiler, süre 15 dk.
Veriler ekteki Excel'de. Kurum şablonu: <dosya>.
```

### 3.5 Var olan sunumu iyileştirme
```
Ekteki sunumu bu skill'in kurallarına göre yeniden tasarla. İçeriği koru, tasarımı ve notları iyileştir.
```

---

## 4. Süreç adım adım: ne görürsün, sen ne yaparsın?

| Aşama | Yapay zekâ ne yapar | Senin işin |
|---|---|---|
| 1. Brief | Ders profilini seçer, kuralları yazar, eksik ve sonucu değiştiren bilgiyi bir kez sorar | Süre, ders ya da şablon gibi sorulursa kısaca cevapla |
| 2. Kaynak | PubMed/DOI ile doğrular, sayıları iddia kartına yazar | Gerek yok (istersen claims.json'a bak) |
| 3. Plan | Slayt planı tablosu çıkarır | İstersen göz at; açık bir sorun yoksa devam eder |
| 4. Görseller | Gerçek fotoğraf arar, lisans kaydeder, kırpar | Elinde kendi fotoğrafın varsa ver |
| 5. Örnek 4 slayt | Kapak, protokol, karşılaştırma ve yoğun slaytı üretir, kontrol eder | Beğenmediğin tarz varsa şimdi söyle |
| 6. Tam deste | Tüm slaytları ve notları üretir | — |
| 7. Kontrol | Render → kontrol → düzelt döngüsü, sonra denetim betiği | — |
| 8. Teslim | 3 dosya + kısa rapor: kullanılan istisnalar, varsayımlar, kontrol edilemeyenler | Dosyaları aç, sunucu görünümünde notlara bak, bir kez saat tutarak prova et |

---

## 5. Varsayılan kurallar

Sen aksini söylemedikçe bunlar uygulanır:

- **Yazı tipi:** Calibri; başlık ve metin aynı aile. Yedeği Arial. Segoe UI, Aptos ve indirilen fontlar
  kullanılmaz; başka bilgisayarda ya da Google Slaytlar'da bozulurlar.
- **Punto:**
  - Bütün metin en az 36 pt. Başlık 40–44 pt, büyük sayılar 60–96 pt.
  - Yalnız şunlar küçük olabilir: kaynak satırı (16 pt, sol alt), kaynakça slaytı (14–16 pt),
    slayt numarası ve görsel kredisi (14 pt).
  - Bölüm etiketi gibi 20 pt'lik küçük yazılar varsayılan olarak yok.
- **Yoğunluk:** slaytta en fazla 6 satır, paragraf yok, slayt başına tek mesaj. Sığmazsa slayt
  bölünür ya da ayrıntı nota taşınır; punto küçültülmez.
- **Tasarım:**
  - Her slaytta görsel olur.
  - Yerleşim çeşitlidir; aynı tür arka arkaya en fazla 2 kez gelir.
  - Koyu bölüm geçişleri kullanılır.
  - Şerit, başlık altı çizgi ve animasyon yok.
- **Görsel:** önce gerçek fotoğraf; bulunamazsa "şematik" etiketli çizim. Yapay zekâ görseli klinik
  fotoğraf gibi gösterilmez.
- **Kaynak:**
  - Bilimsel bilgi içeren slaytın sol altında kısa künye; sonda APA 7 kaynakça.
  - Blog ve YouTube kaynak olarak kullanılmaz.
  - Ders notu sayfa numarasıyla kaynak gösterilmez.
- **Slaytta yasak:**
  - "Bu akşam", "bugün" gibi zaman ifadeleri.
  - Arkadaş adları.
  - "Tartışalım" ya da "Sorular?" slaytı.
  - "Öğretim örneği" etiketi.
  - Çeviri ya da yapay zekâ kokan cümleler.
- **Notlar:** aşağıdaki 6. bölüm.
- **Süre:** 112 kelime/dk ve slayt başına 7 sn ile hesaplanır. Slayt sayısı süreye göre belirlenir,
  zorla sayı tutturulmaz.
- **Teslim:** PPTX + PDF + sunum öncesi okuma PDF'i ders klasörüne; çalışma dosyaları ayrı bir
  "Yapay zeka çalışmaları" klasörüne.

---

## 6. Konuşmacı notları nasıl olur?

Sunucu görünümünde (Alt+F5) okunacak şekilde yazılır:

```
[7/55]  Hedef ≈ 0:55 · Bitişte ≈ 6:10 / 38:48

Kendi ağzından 2–5 kısa cümle. HHD (eyç-eyç-di; el dinamometresi) ile ölçtüğümüzde…

ÖZETLE: Bu slayttan anlamamız gereken tek şey…

ARAŞTIRMA — Pinto-Ramos ve ark., 2022
• Neden burada: …
• Ne yapılmış, ne bulunmuş: 29 hasta; ICC (ay-si-si; sınıf içi korelasyon katsayısı) 0,978
• Nasıl yorumlanır: 0,90 üstü mükemmel kabul edilir; yani…

TERİMLER:
• ICC (ay-si-si): sınıf içi korelasyon katsayısı (intraclass correlation coefficient): …

→ Geçiş: Peki bu ölçümü hangi pozisyonda yapıyoruz?
```

- **Kısaltmalar:** her geçtiği yerde (okunuş; açılım) yazılır; araştırma bloğunun içinde de.
  İstersen "ilk geçişte tam, sonra yalnız okunuş" moduna çevrilebilir.
- **Birimler:** kelimeyle yazılır ("60 newton", "5 santimetre").
- **Sayılar:** her sayı yorumlanır: eşik, anlamı, sınırlılığı. Ham sayı bırakılmaz.
- **Arkadaş sunumlarıyla bağlantı:** yalnız notta, göreli zamanla ("Geçen hafta [arkadaşın adı] anlatmıştı…").
- **Uzunluk:** okunan kısım slayt başına yaklaşık 80–100 kelime; en fazla 160.

---

## 7. Kurala ters bir şey istersen ne olur?

Yapay zekâ önce sorar, sonra yapar:

> Skill kuralı: «36 pt altı yazı yok». Senin isteğin: «maddeler 28 pt». Hangisini uygulayayım?
> 1) Kural  2) Senin isteğin, yalnız bu sunumda  3) Senin isteğin, kalıcı

Cevabın brief'e yazılır ve bütün sunuma uygulanır. Kuralla çelişmeyen isteklerde soru sorulmaz.

Örnek çatışmalar: puntoyu küçültmek, başka bir yazı tipi istemek, kaynak satırını kaldırmak,
animasyon eklemek, yapay zekâ görseli kullanmak, not biçimini değiştirmek.

---

## 8. Düzeltme isterken en etkili yazım

- Slayt numarası + sorun + istenen: "12. slayt: başlık iki satır, kısalt; görseli temas noktasına kırp."
- Genel tarz: "Tüm teknik slaytlara Özetle kutusu koy." / "Notları %20 kısalt."
- Kural değişikliği: "Bundan sonra kaynakça 14 pt olsun (kalıcı)."
- Toplu geri bildirimi tek mesajda ver; yapay zekâ maddeleri ledger'a yazar ve tek tek işaretler.

---

## 9. Uzun işler ve model değiştirme

- Yapay zekâ `ledger.md` dosyasını günceller: nerede kaldı, son dosya hangisi, ne eksik.
- Yeni sohbete ya da başka bir modele geçerken ham sohbet kaydını değil, şu dosyaları ver:
  `brief.md`, `claims.json`, `deck-plan.md`, `deck.json`, `ledger.md`.
- Araştırmayı bir sohbette, üretimi temiz bir sohbette yaptırmak hem hızlı hem ucuzdur.

---

## 10. Sorun giderme

| Sorun | Çözüm |
|---|---|
| "pptxgenjs bulunamadı" | Çalışma klasöründe `npm install pptxgenjs@4` |
| "python-pptx bulunamadı" | `python -m pip install python-pptx` |
| Render alınamıyor | PowerPoint kurulu mu? `render_pptx.ps1` yolunu kontrol et; yoksa PDF üzerinden kontrol |
| Yazı başka bilgisayarda kaydı | Font Calibri/Arial mi? Denetim çıktısındaki "fonts" satırına bak |
| Drive'da sunum bozuldu | Drive "yüklemeleri dönüştür" açık olabilir; PPTX Google Slaytlar'a dönüşür. Birebir kopya PDF'tir |
| Skill tetiklenmiyor | İstekte "PPTX" ve "sunum" geçsin; Codex'te skill listesini kontrol et |
| Not çok uzun | Denetim uyarısındaki slaytlarda notu kısalttır ya da slaytı böldür |

---

## 11. Dosyalar (skill içinde)

- `SKILL.md`: yapay zekânın ana talimatı.
- `references/`: kurallar, ders profilleri, tasarım sistemi, görseller, notlar, akademik içerik,
  uygulamaya göre üretim, kontrol ve teslim.
- `assets/deck-kit/`: JavaScript kiti (`kit.js`, `build.js`, `deck.example.json`).
- `assets/deck-kit-py/`: Python kiti (`deck_kit.py`).
- `scripts/`:
  - `pptx_audit.py`: denetim.
  - `render_pptx.ps1`: PowerPoint ile görüntü alma.
  - `contact_sheet.py`: görüntüleri tek sayfada toplama.
  - `find_images.py`: lisanslı görsel arama.
  - `make_reading_guide.py`: okuma PDF'i.
- `templates/`: brief, slayt planı, iddia kartları, çalışma kaydı.
