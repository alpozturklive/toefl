# TOEFL 2026 — Listen & Repeat Çalışma Paketi

Bu repo, TOEFL iBT 2026 sınavındaki **Listen & Repeat** bölümü için
AI destekli çalışma materyali üretir.

## Projenin Amacı

Kullanıcı (Alp), ChatGPT / Gemini / Claude ile konuşarak
TOEFL cümlelerini dinleyip tekrar ediyor. Her `.md` dosyası bir
ders — dosyayı AI'ya yükleyip başlangıç komutunu çalıştırıyor.

**Yeni format (2026-06-24):** Her ders 3 sahne içerir; her sahne bir
**🎯 Sınav Seti** (7 cümle, kısa→uzun, gerçek sınav süreleri 8/8/10/10/10/12/12 sn)
+ **📚 Ekstra Pratik** (8 cümle) olarak ikiye bölünür. Bu yapı, gerçek TOEFL
Listen & Repeat görevinin 7 cümlelik artan zorluk akışını birebir taklit eder.

## Mevcut Dosyalar

| Dosya | İçerik | TOEFL Önceliği |
|---|---|---|
| `lesson1.md` | Cafeteria, Campus Store, Lecture Hall (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson2.md` | Library, Career Forum, MBA Open House (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson3.md` | Art Museum, International Student Office, IT Help Desk (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson4.md` | Health Center, Gym, Dorm Life (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson5.md` | Science Lecture, Lab, Research (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson6.md` | Student Organizations, Campus Events, Study Abroad (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson7.md` | Technology, Online Classes, Financial Aid (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson8.md` | Registrar, Academic Advising, Tutoring Center (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson9.md` | Campus Housing Office, Campus Safety, Campus Transit (45 cümle) | ⭐⭐ Yüksek |
| `lesson10.md` | Orientation Week, Graduate Admissions, Campus Sustainability (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `toefl-listen-repeat-sentences.md` | ~1608 cümle — ⚠️ HAM VERİ, doğrudan kullanma | — |
| `extract_toefl.py` | YouTube transcript çekme scripti | — |

## Mac'te Yapılacak Görev — YouTube Transcript Çıkarımı

**Hedef videolar:**
- `https://www.youtube.com/watch?v=I46DN4NW5Bg`
- Playlist: `https://www.youtube.com/playlist?list=PLDysj-2jpdTtsniblszfWEGsfHbFOFBYD`

**Adımlar:**

```bash
pip install youtube-transcript-api yt-dlp
python3 extract_toefl.py
```

Script çalışınca `new_sentences.md` oluşur.

**Sonra ne yapılacak:**
1. `new_sentences.md` içindeki cümleleri temizle (tekrar, köşeli parantez, kısa olanlar)
2. `toefl-listen-repeat-sentences.md` ile çakışanları çıkar (dedup)
3. Yeni cümleleri tema bazlı `lesson11.md`, `lesson12.md`... olarak böl
4. Her ders dosyası yapısı `lesson1.md` ile aynı olsun (yeni Sınav Seti formatı)
5. Toplu yeniden biçimlendirme için `reformat.py` mantığını kullan: her temanın
   15 cümlesini kelime sayısına göre sırala, 7'lik Sınav Seti (kısa→uzun) + 8 Ekstra'ya böl.

## Ders Dosyası Yapısı (şablon)

```markdown
# TOEFL 2026 — Ders N: [Tema Adları]

> Kaynak: Inspire SpeakEasy TOEFL 2026

## Başlangıç Komutu (AI'ya yapıştır)
[prompt — önce Sınav Seti, süreyle, teker teker]

## Tema X: [Ad]
> 🖼️ **Sahne:** [tek resimli sahne açıklaması]

### 🎯 Sınav Seti — kısa→uzun (süreyle çalış)
1. (8 sn) ...   2. (8 sn) ...
3-5. (10 sn) ...   6-7. (12 sn) ...

### 📚 Ekstra Pratik
8-15. ...

## Puanlama
[rubrik + süre sınırları]
```

## Önemli Kural

**TOEFL 2026 Listen & Repeat ≠ Speaking Task.**
Speaking bölümünde 2 mülakat sorusu var — bunlar bu repo'ya girmez.
Sadece kısa kampüs/akademik cümleler: cafeteria, bookstore,
lecture, library, career forum, airport, restaurant senaryoları.

## Tema Sırası (ders planı)

1. ders1 ✅ — Cafeteria, Campus Store, Lecture Hall
2. ders2 ✅ — Library, Career Forum, MBA Open House
3. ders3 ✅ — Art Museum, International Student Office, IT Help Desk (eski Airport/Restaurant/Hotel yerine)
4. ders4 ✅ — Health Center, Gym, Dorm Life
5. ders5 ✅ — Science Lecture, Lab, Research
6. ders6 ✅ — Student Organizations, Campus Events, Study Abroad
7. ders7 ✅ — Technology, Online Classes, Financial Aid
8. ders8 ✅ — Registrar's Office, Academic Advising, Tutoring Center
9. ders9 ✅ — Campus Housing Office, Campus Safety, Campus Transit
10. ders10 ✅ — Orientation Week, Graduate Admissions, Campus Sustainability
11. ders11+ — YouTube'dan yeni temalar (internet search + transcript ile genişlet)
