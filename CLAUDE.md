# TOEFL 2026 — Listen & Repeat Çalışma Paketi

Bu repo, TOEFL iBT 2026 sınavındaki **Listen & Repeat** bölümü için
AI destekli çalışma materyali üretir.

## Projenin Amacı

Kullanıcı (Alp), ChatGPT / Gemini / Claude ile konuşarak
TOEFL cümlelerini dinleyip tekrar ediyor. Her `.md` dosyası bir
ders — dosyayı AI'ya yükleyip başlangıç komutunu çalıştırıyor.

## Mevcut Dosyalar

| Dosya | İçerik | TOEFL Önceliği |
|---|---|---|
| `lesson1.md` | Cafeteria, Campus Store, Lecture Hall (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson2.md` | Library, Career Forum, MBA Open House (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson3.md` | Airport, Restaurant, Hotel (45 cümle) | ⚠️ Düşük — iBT'de nadiren çıkar |
| `lesson4.md` | Health Center, Gym, Dorm Life (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson5.md` | Science Lecture, Lab, Research (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson6.md` | Student Organizations, Campus Events, Study Abroad (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson7.md` | Technology, Online Classes, Financial Aid (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson8.md` | Registrar, Academic Advising, Tutoring Center (45 cümle) | ⭐⭐⭐ Çok yüksek |
| `lesson9.md` | Campus Housing Office, Campus Safety, Campus Transit (45 cümle) | ⭐⭐ Yüksek |
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
3. Yeni cümleleri tema bazlı `lesson002.md`, `lesson003.md`... olarak böl
4. Her ders dosyası yapısı `lesson001.md` ile aynı olsun (prompt + bölümler + rubrik)

## Ders Dosyası Yapısı (şablon)

```markdown
# TOEFL 2026 — Ders 00X: [Tema Adları]

> Kaynak: Inspire SpeakEasy TOEFL 2026

## Başlangıç Komutu (AI'ya yapıştır)
[prompt buraya]

## Tema X: [Ad]
1. Cümle
2. Cümle
...

## Puanlama
[rubrik]
```

## Önemli Kural

**TOEFL 2026 Listen & Repeat ≠ Speaking Task.**
Speaking bölümünde 2 mülakat sorusu var — bunlar bu repo'ya girmez.
Sadece kısa kampüs/akademik cümleler: cafeteria, bookstore,
lecture, library, career forum, airport, restaurant senaryoları.

## Tema Sırası (ders planı)

1. ders1 ✅ — Cafeteria, Campus Store, Lecture Hall
2. ders2 ✅ — Library, Career Forum, MBA Open House
3. ders3 ✅ — Airport, Restaurant, Hotel ⚠️ (genel İngilizce; iBT'de nadiren çıkar)
4. ders4 ✅ — Health Center, Gym, Dorm Life
5. ders5 ✅ — Science Lecture, Lab, Research
6. ders6 ✅ — Student Organizations, Campus Events, Study Abroad
7. ders7 ✅ — Technology, Online Classes, Financial Aid
8. ders8 ✅ — Registrar's Office, Academic Advising, Tutoring Center
9. ders9 ✅ — Campus Housing Office, Campus Safety, Campus Transit
10. ders10+ — YouTube'dan yeni temalar (internet search + transcript ile genişlet)
