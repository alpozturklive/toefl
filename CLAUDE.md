# TOEFL 2026 — Listen & Repeat Çalışma Paketi

Bu repo, TOEFL iBT 2026 sınavındaki **Listen & Repeat** bölümü için
AI destekli çalışma materyali üretir.

## Projenin Amacı

Kullanıcı (Alp), ChatGPT / Gemini / Claude ile konuşarak
TOEFL cümlelerini dinleyip tekrar ediyor. Her `.md` dosyası bir
ders — dosyayı AI'ya yükleyip başlangıç komutunu çalıştırıyor.

## Mevcut Dosyalar

| Dosya | İçerik |
|---|---|
| `ders001.md` | Ders 1 — Cafeteria, Campus Store, Lecture Hall (45 cümle) |
| `toefl-listen-repeat-sentences.md` | 1608 cümle, 105 video, tema bazlı |
| `listen-and-repair-english-study.md` | Kapsamlı çalışma rehberi (tema + prompt) |
| `extract_toefl.py` | YouTube transcript çekme scripti |

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
3. Yeni cümleleri tema bazlı `ders002.md`, `ders003.md`... olarak böl
4. Her ders dosyası yapısı `ders001.md` ile aynı olsun (prompt + bölümler + rubrik)

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

1. ders001 ✅ — Cafeteria, Campus Store, Lecture Hall
2. ders002 — Library, Career Forum, MBA Open House
3. ders003 — Travel & Airport, Shopping, Restaurant
4. ders004 — Daily Conversations, Health, Technology
5. ders005+ — Playlist'ten çıkan yeni temalar
