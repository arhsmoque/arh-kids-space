"""
generate_asma_audio.py
======================
Generates all TTS audio files for Asma's VAK assessment session.
Uses edge-tts (Microsoft Edge Neural TTS) — no API key required.

Voice: ms-MY-YasminNeural (Malaysian Malay, female, warm)

Usage:
    pip install edge-tts
    python generate_asma_audio.py

Output:
    audio/asma_*.mp3  — 13 files, ~200KB total
    
Intended runner: Claude Code (has full network access)
"""

import asyncio
import os
import edge_tts

# ── Config ──────────────────────────────────────────────
VOICE       = "ms-MY-YasminNeural"
RATE        = "+0%"    # normal speed — clear for 5yo
VOLUME      = "+0%"
OUTPUT_DIR  = "audio"

# ── Script: all lines Asma's session needs ───────────────
# Format: (filename_without_ext, text_to_speak)
LINES = [
    # Session flow
    ("asma_welcome",
     "Hai Asma! Jom kita main satu permainan yang seronok!"),

    ("asma_g1_intro",
     "Tengok gambar-gambar ni. Boleh Asma tolong susun ikut cerita?"),

    # Round 0 — Cerita Hujan
    ("asma_g1_r0_prompt",
     "Mana yang jadi dulu — matahari, awan, hujan, atau pelangi?"),

    # Round 1 — Pokok Epal
    ("asma_g1_r1_prompt",
     "Pokok ni macam mana nak tumbuh besar? Mana yang jadi dulu?"),

    # Round 2 — Masak Nasi
    ("asma_g1_r2_prompt",
     "Macam mana nak masak nasi? Mana yang Asma buat dulu sekali?"),

    # Feedback
    ("asma_correct",
     "Bagus! Pandai Asma!"),

    ("asma_tryagain",
     "Cuba lagi! Asma boleh!"),

    # Hints
    ("asma_hint_r0",
     "Tengok langit — gelap dulu ke terang dulu?"),

    ("asma_hint_r1",
     "Kalau nak tanam pokok, kita letak benih dulu ke siram air dulu?"),

    ("asma_hint_r2",
     "Sebelum masak, kita kena ada beras dulu. Beras tu yang mana?"),

    # Transitions
    ("asma_next_round",
     "Bagus! Jom cuba cerita lain pula!"),

    # Completion
    ("asma_done",
     "Siap! Asma hebat! Pergi panggil Abah sekarang ye!"),

    # Abah call — played at session end
    ("asma_call_abah",
     "Abah! Abah! Asma dah habis main!"),
]

# ── Generator ────────────────────────────────────────────
async def generate_one(filename: str, text: str) -> None:
    out_path = os.path.join(OUTPUT_DIR, f"{filename}.mp3")

    if os.path.exists(out_path):
        print(f"  [skip] {filename}.mp3 — already exists")
        return

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE,
        rate=RATE,
        volume=VOLUME,
    )
    await communicate.save(out_path)
    print(f"  [done] {filename}.mp3")


async def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"\nGenerating {len(LINES)} audio files → ./{OUTPUT_DIR}/\n")

    for filename, text in LINES:
        await generate_one(filename, text)
        await asyncio.sleep(0.3)  # polite delay between requests

    print(f"\n✅ All done. {len(LINES)} files in ./{OUTPUT_DIR}/\n")
    print("Next step:")
    print("  1. Copy the audio/ folder next to vak-assessment.html")
    print("  2. Rebuild app with audio playback wired in (next Claude turn)\n")


if __name__ == "__main__":
    asyncio.run(main())
