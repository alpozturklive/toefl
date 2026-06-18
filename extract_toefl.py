#!/usr/bin/env python3
"""
TOEFL 2026 Listen & Repeat — YouTube Transcript Extractor
Mac'te çalıştır: python3 extract_toefl.py
Gerekli: pip install youtube-transcript-api
"""

from youtube_transcript_api import YouTubeTranscriptApi
import re
import sys

# ─── Hedef videolar ───────────────────────────────────────────────────────────
SINGLE_VIDEOS = [
    "I46DN4NW5Bg",   # https://www.youtube.com/watch?v=I46DN4NW5Bg
]

PLAYLIST_ID = "PLDysj-2jpdTtsniblszfWEGsfHbFOFBYD"

# ─── Speaking görevi filtresi (bunları ATLA) ─────────────────────────────────
SKIP_PATTERNS = [
    r"some people prefer",
    r"do you agree or disagree",
    r"what do you think",
    r"explain why",
    r"give reasons",
    r"your opinion",
    r"task \d",
    r"speaking task",
    r"take an interview",
    r"^\s*question\s*\d",
    r"^\s*prompt",
]
SKIP_RE = re.compile("|".join(SKIP_PATTERNS), re.IGNORECASE)


def get_playlist_video_ids(playlist_id: str) -> list[str]:
    """yt-dlp ile playlist video ID'lerini çeker."""
    import subprocess, json
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "-j",
         f"https://www.youtube.com/playlist?list={playlist_id}"],
        capture_output=True, text=True
    )
    ids = []
    for line in result.stdout.strip().splitlines():
        try:
            data = json.loads(line)
            ids.append(data["id"])
        except Exception:
            pass
    return ids


def fetch_transcript(video_id: str) -> list[str]:
    """Bir video için İngilizce transcript çeker, filtreler."""
    try:
        api = YouTubeTranscriptApi()
        snippets = api.fetch(video_id)
        sentences = []
        for s in snippets:
            text = s.text.strip()
            text = re.sub(r"\[.*?\]", "", text).strip()  # [Music] vb. kaldır
            if len(text) < 4:
                continue
            if SKIP_RE.search(text):
                continue
            # Küçük harf veya tek kelime ise birleştirme adayı — büyük harfle başlayanları al
            if text[0].isupper() or text[0].isdigit():
                sentences.append(text)
        return sentences
    except Exception as e:
        print(f"  ⚠ {video_id}: {e}", file=sys.stderr)
        return []


def main():
    all_sentences = set()

    # Tekil videolar
    print("Tekil videolar işleniyor...")
    for vid in SINGLE_VIDEOS:
        print(f"  → {vid}")
        sentences = fetch_transcript(vid)
        all_sentences.update(sentences)
        print(f"     {len(sentences)} cümle bulundu")

    # Playlist
    print(f"\nPlaylist işleniyor: {PLAYLIST_ID}")
    try:
        video_ids = get_playlist_video_ids(PLAYLIST_ID)
        print(f"  {len(video_ids)} video bulundu")
        for vid in video_ids:
            print(f"  → {vid}")
            sentences = fetch_transcript(vid)
            all_sentences.update(sentences)
            print(f"     {len(sentences)} cümle")
    except Exception as e:
        print(f"  ⚠ Playlist alınamadı: {e}", file=sys.stderr)
        print("  yt-dlp kurulu değilse: pip install yt-dlp", file=sys.stderr)

    # Çıktı
    sorted_sentences = sorted(all_sentences, key=len)
    output = "# TOEFL 2026 Listen & Repeat — Yeni Cümleler\n\n"
    output += f"_Toplam: {len(sorted_sentences)} cümle_\n\n"
    for s in sorted_sentences:
        output += f"- {s}\n"

    with open("new_sentences.md", "w") as f:
        f.write(output)

    print(f"\n✅ Tamamlandı: {len(sorted_sentences)} cümle → new_sentences.md")


if __name__ == "__main__":
    main()
