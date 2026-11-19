"""Generate the Chinese word audio for Bandar Ilmu.

Reads the WORDS list between the /*WORDS-START*/ and /*WORDS-END*/ markers in
v1/index.html (one source for game and audio) and writes v1/audio/<id>.mp3 with
the same voice the tutoring desk uses (zh-CN-XiaoxiaoNeural, a little slower).
Existing files are kept; pass --force to redo them.

    uv run --with edge-tts python bandar-ilmu/scripts/generate_audio.py [--force]
"""
import asyncio
import json
import re
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent / "v1"
VOICE, RATE = "zh-CN-XiaoxiaoNeural", "-15%"


def words():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    m = re.search(r"/\*WORDS-START\*/(.*?)/\*WORDS-END\*/", html, re.S)
    if not m:
        sys.exit("WORDS markers not found in v1/index.html")
    return json.loads(m.group(1))


async def main(force: bool) -> None:
    out = ROOT / "audio"
    out.mkdir(exist_ok=True)
    made = kept = 0
    for w in words():
        f = out / f"{w['id']}.mp3"
        if f.exists() and not force:
            kept += 1
            continue
        await edge_tts.Communicate(w["zh"], VOICE, rate=RATE).save(str(f))
        made += 1
    print(f"audio: {made} made, {kept} kept, in {out}")


if __name__ == "__main__":
    asyncio.run(main("--force" in sys.argv))
