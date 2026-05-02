#!/usr/bin/env bash
# Run from repo root: bash scripts/run-asma-audio.sh
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"

# Load credentials
[ -f "$HOME/.cf-credentials" ] && source "$HOME/.cf-credentials"

: "${ELEVENLABS_API_KEY:?Set ELEVENLABS_API_KEY in ~/.cf-credentials}"

pip install elevenlabs -q

cd "$REPO/artifacts"
python generate_asma_audio_elevenlabs.py
