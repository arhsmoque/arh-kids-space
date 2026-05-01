# ARH Kids — VAK Behavioural Assessment
## Project Record & Design Memory
*Written for future-Rahman, so you remember why things are the way they are.*

---

## What This Project Is

A behavioural assessment tool disguised as three short games, built to determine how each of your children — Aflah, Haidar, and Asma — naturally processes and retains information. The output is a structured report you send to Claude for VAK analysis and SJKC-specific learning recommendations.

This is **not** a quiz where children answer "what kind of learner are you?" That approach fails at this age because children answer what they think sounds right, not what they actually do. Instead, the games observe *how* they play — and that behavioural trace is the real data.

---

## Your Children at the Time of This Project

| Child | Age | School | Notes |
|---|---|---|---|
| **Aflah** | 8 years | SJKC Chung Hwa (P), Jalan Damai, KL — Darjah 2 | Reads and types independently. Game-oriented. |
| **Haidar** | 7 years | Same school — Darjah 1 | Enthusiastic. Still building reading confidence. |
| **Asma** | 5 years | Tadika Amal | Cannot read yet. Abah must be present throughout. |
| **Huda** | 2 years | — | Too young. Not part of this project. |

All three attend KAFA Integrasi Taman Keramat Permai in the afternoon (except Huda). Aflah and Haidar are doing 听写 (ting xie / mo xie) — Chinese character dictation — which was the original motivation for wanting to understand their learning styles.

---

## Why This Was Built

The immediate trigger was ting xie. Both Aflah and Haidar struggle with memorising Chinese characters for weekly dictation tests. The question was: are they struggling because of the *method* being used, or because of genuine difficulty?

VAK theory says: a kinesthetic learner forced to study by reading silently will always underperform relative to their actual ability. The same child given movement-based or hands-on study techniques may perform significantly better — not because they got smarter, but because the method finally matched how their brain actually processes information.

The goal: identify each child's dominant learning style, then redesign their ting xie revision approach accordingly.

---

## The VAK Model — Quick Reference

| Style | Core trait | Learns best by |
|---|---|---|
| **Visual (V)** | Thinks in images and spatial relationships | Seeing — diagrams, colour, charts, written words, watching |
| **Auditory (A)** | Thinks in sound and language | Hearing — explanation, discussion, reading aloud, rhythm |
| **Kinesthetic (K)** | Thinks through physical experience | Doing — touching, building, movement, trial and error |

**VARK** adds a fourth — Reading/Writing (R) — but for primary school age this is rarely the dominant style and was excluded from this assessment.

**Important limitation:** VAK is a tendency spectrum, not a fixed category. Results should read as "leans strongly toward K with A secondary" — not "this child is K." The spectrum also shifts with age, subject matter, and context.

---

## The Assessment Design

### Method: Behavioural Observation via Games
Three games, each designed so that Visual, Auditory, and Kinesthetic learners naturally gravitate toward different strategies — without being asked which they prefer.

### The Six Behavioral Signals Captured

| Signal | How captured | What it indicates |
|---|---|---|
| **First-action latency** | `Date.now()` on first tap vs session start | Long pause = observer (V/A). Fast dive = doer (K) |
| **Hint type preference** | Which hint button they tap: 👁️ Visual or 🔊 Audio | Direct V vs A discriminator |
| **Error recovery method** | Undo usage pattern — immediate vs delayed vs never | Reflective (V/A) vs committed (K) |
| **Attempt-accuracy curve** | Errors per round tracked with timestamps | Improves with reps (K) vs careful first attempt (V/A) |
| **Audio replay behavior** | How many times they replay word in Game 2 | Strong A signal if >1 replay |
| **Hesitation time** | Time from round display to first action in Game 3 | Studies whole pattern first (V) vs dives in (K) |

Signal 6 — verbal behaviour (does the child talk aloud during play?) — cannot be captured by the app. This requires Abah present in the room. For Asma, this is mandatory. For Aflah and Haidar, it's optional but adds confidence to the result.

### The Three Games

**Game 1 — Susun Gambar (Story Sequencer)**
Four scrambled scene cards, child arranges them into correct story order via drag-and-drop. Three rounds with different stories (rain, apple tree, cooking rice). Captures: latency, spatial reasoning approach, undo/redo pattern, hint preference.

*Why this game:* Story sequencing has no single "correct path" — a visual learner will scan all four cards before placing any, an auditory learner may narrate the story aloud, a kinesthetic learner will start placing immediately and adjust after.

**Game 2 — Padanan Bunyi (Sound-Image Matching)**
A word is shown and spoken via TTS. Child picks the matching image from four choices. Four rounds. Captures: audio replay count, first-action latency, hint preference, error pattern.

*Why this game:* The word is spoken automatically — but a Visual learner will rely on the written word, an Auditory learner will replay the audio, a Kinesthetic learner will just start tapping choices.

**Game 3 — Bina Corak (Pattern Completion)**
A visual sequence with one missing element (❓). Child picks the correct answer from four options. Four rounds, increasing complexity. Captures: hesitation time per round, hint preference, undo/redo, error pattern.

*Why this game:* Pattern recognition can be approached visually (study the whole sequence), auditorily (count or verbalise the pattern), or kinesthetically (tap options until one feels right).

### Asma's Session (Modified)
Asma plays Game 1 only. All instructions are read aloud by Abah. Hint buttons are available but Abah decides when to use them. Abah's verbal observations are added manually to the report before analysis.

---

## Technical Decisions & Why

**Single HTML file, no dependencies**
Works offline. No npm, no CDN failures, no API keys. Load once on POCO F7, works anywhere. This was a deliberate choice over a React/Vue app — durability over developer convenience.

**Timestamp logging, not stopwatch**
Every meaningful action logs `Date.now()`. Time deltas are calculated post-hoc during analysis, not during the session. This means: no polling, no drift, full action sequence reconstruction, and the app never needs to "know" how much time has passed.

**Undo/Redo included deliberately**
The availability of undo does not mask learning style — a kinesthetic child will still dive in fast even knowing they can undo, a visual child will still pause and plan. But the *pattern* of undo usage is itself a signal: immediate undo after wrong (reflective = V/A) vs never undoing (committed = K) vs undoing everything at once after seeing the full result (pattern-thinker = V).

**TTS via Web Speech API**
`speechSynthesis` with `ms-MY` locale, fallback to `ms`. No external TTS API needed. Audio unlocked on first user tap (required by Chrome Android). Quality is adequate for single words and short phrases. If ms-MY voice is not available on device, the app continues — audio hints fall back to Abah-read text.

**Why Whisper/Groq was considered but deferred**
Whisper would add value for transcribing Abah's spoken observations (especially for Asma) and for a future verbal response task for Aflah. Deferred because: mic permission UX is disruptive for young children, background noise in home environment degrades accuracy, and the current touch-based signals are sufficient for a first assessment. Groq STT is the right add-on when verbal tasks are introduced in v2.

**Device: POCO F7 (Snapdragon 8 Elite, Chrome/Thorium)**
Touch targets set at minimum 56px. Right-edge 40px avoided (physical button zone). Portrait locked. Pinch-zoom disabled. All hover states have active-state equivalents for touch.

---

## Report Format

Each session produces a dual-format export:

**Readable text** — human-readable summary for Abah to review, with signal breakdown and full action log in plain English timestamp format.

**JSON** — structured data with `meta`, `result`, `signals`, and `action_log` arrays. Paste to Claude for VAK analysis.

Both are in the same exported file, separated by `---JSON---`.

---

## What Happens After the Session

1. Run each child's session separately (one child per session, app resets between)
2. Export the report for each child
3. Paste all three reports to Claude in one message
4. Add your verbal observations for Asma (and any others you noticed)
5. Claude cross-references against VAK signal standards and returns:
   - Confident VAK profile per child
   - Primary + secondary style
   - SJKC-specific revision strategies for ting xie, Mathematics, and general study
   - Comparison across siblings (useful — often one child's strength is another's gap)

---

## Planned Future Work (Not Yet Built)

### Modular Architecture Refactor
Current code is monolithic — functional, but all in one block. When new games are added after the first session, the code should be restructured into three clearly separated modules within the same HTML file:

- `CONTENT` — all question data, stories, words, patterns. Edit here to add rounds.
- `GAMES` — render + interaction logic per game. Add new game types here.
- `ENGINE` — scoring weights, signal computation, export formatter.
- `SHELL` — navigation, screen management, logging, toast. Never touch this.

This refactor costs ~2 hours and should happen *after* the first session reveals what's missing — not before.

### Potential New Games (Post-Session Additions)
These emerged during design discussions as strong candidates for v2:

| Game idea | Primary signal |
|---|---|
| **Hafazan helper** — hear a doa, tap which line comes next | Strong A discriminator |
| **Trace the stroke** — draw Chinese character strokes in order | K + V discriminator |
| **Colour the story** — given a story, colour-code which scene came first | V discriminator |
| **Explain to me** — child describes an image in their own words (requires Groq STT) | A discriminator for Aflah |

### Groq STT Integration (v2)
Single use case: Abah observation notes during Asma's session. One button, one API call, transcribed text appended to log with timestamp. Keeps Abah's hands free during the session. Requires a Groq API key — slot is already identified in the architecture.

### Multi-session Tracking
Currently the app has no memory between sessions. Future version should store results in `localStorage` keyed by child name and session date, allowing Abah to compare results across sessions over time (e.g., does Haidar's profile shift as he gets older?).

---

## Open Questions for Future-Rahman

- After the first session: did the games feel too long, too short, or right for each child's attention span?
- Did Asma engage with Game 1, or was it too abstract for 5 years old? If too abstract, a simpler colour-matching game may be needed.
- Was the drag-and-drop in Game 1 smooth on POCO F7 touch, or did the touch-drag fallback feel clunky?
- Did any child ask to replay Game 2's audio repeatedly? That's your strongest A signal — note it even if the counter didn't catch it.
- After getting the VAK profiles — did changing the ting xie revision method actually improve results? This is the real test.

---

## Key People in This Project

- **Rahman (Abah)** — you. Initiated this because ting xie was a recurring struggle.
- **Claude** — designed and built the assessment. Project lives in the ARH Kids project context on claude.ai. All prior conversations are searchable.
- **Aflah, Haidar, Asma** — the subjects. They don't need to know this is an assessment. To them it's just three games.

---

*Document written: May 2026*
*App version: v1.0 — first session build*
*Next action: Run sessions, collect reports, paste to Claude.*
