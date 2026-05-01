# Asma Audio Generation — Claude Code Runbook

## What This Does
Generates 13 MP3 audio files using Microsoft Edge Neural TTS (ms-MY-YasminNeural).
No API key needed. No Azure account needed.

## Run Order

### Step 1 — Install dependency
```bash
pip install edge-tts
```

### Step 2 — Run from this directory
```bash
python generate_asma_audio.py
```

### Step 3 — Verify output
```bash
ls -lh audio/
```
Expected: 13 x asma_*.mp3 files, ~10–20KB each

### Step 4 — Commit to repo
```bash
git add audio/
git commit -m "feat: add Asma TTS audio files (ms-MY-YasminNeural)"
git push
```

## Output Files
| File | Content |
|---|---|
| asma_welcome.mp3 | Session greeting |
| asma_g1_intro.mp3 | Game 1 introduction |
| asma_g1_r0_prompt.mp3 | Round 0 question (Hujan) |
| asma_g1_r1_prompt.mp3 | Round 1 question (Pokok) |
| asma_g1_r2_prompt.mp3 | Round 2 question (Nasi) |
| asma_correct.mp3 | Correct answer feedback |
| asma_tryagain.mp3 | Wrong answer feedback |
| asma_hint_r0.mp3 | Hint for Round 0 |
| asma_hint_r1.mp3 | Hint for Round 1 |
| asma_hint_r2.mp3 | Hint for Round 2 |
| asma_next_round.mp3 | Round transition |
| asma_done.mp3 | Session complete |
| asma_call_abah.mp3 | Calls Abah at end |

## If a File Fails
Script skips already-generated files — safe to re-run.
If one file fails, delete it and re-run — only missing files regenerate.

## Next Step After Audio is Generated
Tell Claude: "Audio files generated — wire them into vak-assessment.html for Asma"
Claude will update the app to play correct file at each moment in Asma's session.

## Voice Details
- Voice: ms-MY-YasminNeural
- Language: Malay (Malaysia)
- Rate: normal (+0%)
- Provider: Microsoft Edge TTS (free, no auth)
