"""
generate_asma_audio_elevenlabs.py
==================================
Generates all TTS audio files for Asma's VAK session using ElevenLabs API.
Produces warm, natural Malaysian-accented speech via eleven_multilingual_v2.

Usage:
    pip install elevenlabs
    python generate_asma_audio_elevenlabs.py

    # With explicit credentials:
    ELEVENLABS_API_KEY=sk_... ELEVENLABS_VOICE_ID=... python generate_asma_audio_elevenlabs.py

Configuration:
    Set ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in environment,
    or in ~/.cf-credentials (same file used for Cloudflare), or edit the
    CONFIG block below directly.

After running:
    Script auto-commits audio/ and pushes to current git branch.
    Cloudflare Pages auto-deploys on merge to main.

Voice recommendations (all handle Malay via eleven_multilingual_v2):
    Matilda  — warm, friendly, gentle     : 9BWtsMINqrJLrRacOk9x
    Charlotte — natural, calm             : XB0fDUnXU5powFXDhCwa
    To browse: https://elevenlabs.io/app/voice-library
"""

import os, subprocess, sys
from pathlib import Path

# ── Config — edit here or set environment variables ──────────────────────────
API_KEY   = os.getenv("ELEVENLABS_API_KEY",   "")   # sk_...
VOICE_ID  = os.getenv("ELEVENLABS_VOICE_ID",  "9BWtsMINqrJLrRacOk9x")  # Matilda
MODEL     = "eleven_multilingual_v2"
STABILITY        = 0.5   # 0–1, higher = more consistent
SIMILARITY_BOOST = 0.85  # 0–1, higher = closer to original voice
STYLE            = 0.3   # 0–1, slight expressiveness
OUTPUT_DIR = Path(__file__).parent / "audio"

# ── Source credentials from ~/.cf-credentials if not in env ──────────────────
_creds = Path.home() / ".cf-credentials"
if _creds.exists() and not API_KEY:
    for line in _creds.read_text().splitlines():
        if line.startswith("export ELEVENLABS_API_KEY="):
            API_KEY = line.split("=", 1)[1].strip().strip('"')
        if line.startswith("export ELEVENLABS_VOICE_ID="):
            VOICE_ID = line.split("=", 1)[1].strip().strip('"')

# ── Audio lines ───────────────────────────────────────────────────────────────
LINES = [
    ("asma_welcome",      "Hai Asma! Jom kita main satu permainan yang seronok!"),
    ("asma_g1_intro",     "Tengok gambar-gambar ni. Boleh Asma tolong susun ikut cerita?"),
    ("asma_g1_r0_prompt", "Mana yang jadi dulu — matahari, awan, hujan, atau pelangi?"),
    ("asma_g1_r1_prompt", "Pokok ni macam mana nak tumbuh besar? Mana yang jadi dulu?"),
    ("asma_g1_r2_prompt", "Macam mana nak masak nasi? Mana yang Asma buat dulu sekali?"),
    ("asma_correct",      "Bagus! Pandai Asma!"),
    ("asma_tryagain",     "Cuba lagi! Asma boleh!"),
    ("asma_hint_r0",      "Tengok langit — gelap dulu ke terang dulu?"),
    ("asma_hint_r1",      "Kalau nak tanam pokok, kita letak benih dulu ke siram air dulu?"),
    ("asma_hint_r2",      "Sebelum masak, kita kena ada beras dulu. Beras tu yang mana?"),
    ("asma_next_round",   "Bagus! Jom cuba cerita lain pula!"),
    ("asma_done",         "Siap! Asma hebat! Pergi panggil Abah sekarang ye!"),
    ("asma_call_abah",    "Abah! Abah! Asma dah habis main!"),
]

# ── Main ──────────────────────────────────────────────────────────────────────
def generate():
    if not API_KEY:
        sys.exit("❌  ELEVENLABS_API_KEY not set. See script header for instructions.")

    try:
        from elevenlabs.client import ElevenLabs
        from elevenlabs import VoiceSettings
    except ImportError:
        sys.exit("❌  Run: pip install elevenlabs")

    client = ElevenLabs(api_key=API_KEY)
    OUTPUT_DIR.mkdir(exist_ok=True)

    print(f"\nGenerating {len(LINES)} files → {OUTPUT_DIR}/\n")
    generated = []

    for filename, text in LINES:
        out = OUTPUT_DIR / f"{filename}.mp3"
        if out.exists():
            print(f"  [skip] {filename}.mp3")
            continue

        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            text=text,
            model_id=MODEL,
            voice_settings=VoiceSettings(
                stability=STABILITY,
                similarity_boost=SIMILARITY_BOOST,
                style=STYLE,
                use_speaker_boost=True,
            ),
        )
        out.write_bytes(b"".join(audio))
        size = out.stat().st_size
        print(f"  [done] {filename}.mp3  ({size//1024}KB)")
        generated.append(str(out))

    if not generated:
        print("\n✅ All files already exist — nothing to regenerate.")
        return

    print(f"\n✅ Generated {len(generated)} files.\n")
    _git_push(generated)


def _git_push(new_files: list[str]):
    repo = Path(__file__).parent.parent
    try:
        subprocess.run(["git", "-C", str(repo), "add"] + new_files, check=True)
        subprocess.run(
            ["git", "-C", str(repo), "commit", "-m",
             f"audio: regenerate {len(new_files)} Asma MP3s via ElevenLabs (eleven_multilingual_v2)"],
            check=True,
        )
        branch = subprocess.check_output(
            ["git", "-C", str(repo), "rev-parse", "--abbrev-ref", "HEAD"]
        ).decode().strip()
        subprocess.run(["git", "-C", str(repo), "push", "origin", branch], check=True)
        print(f"🚀 Pushed to {branch} → Cloudflare Pages will auto-deploy.\n")
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Git push failed: {e}\nAudio files are ready in {OUTPUT_DIR} — push manually.")


if __name__ == "__main__":
    generate()
