# VAK Assessment — As-Built

## Mengapa Dibina

Aflah (10) dan Haidar (8) kerap lupa ejaan Mandarin (ting xie) walaupun belajar berulang kali.
Abah ingin tahu gaya belajar dominan mereka — visual, auditori, atau kinestetik — supaya
teknik mengajar boleh disesuaikan.

Asma (5) masih prasekolah; penilaiannya lebih santai, dengan panduan audio supaya dia boleh
bermain sendiri sementara menunggu Abah.

---

## Model VAK

Tiga dimensi yang dinilai:

| Dimensi | Maksud | Permainan |
|---------|--------|-----------|
| **V — Visual** | Belajar melalui gambar, urutan, corak | G1 Susun Gambar |
| **A — Auditori** | Belajar melalui bunyi, perkataan, hafalan | G2 Ingat Nombor |
| **K — Kinestetik** | Belajar melalui sentuhan, pergerakan, tangan | G3 Teka Huruf |

---

## Tiga Permainan

### G1 — Susun Gambar (Visual)
Anak menyusun 4 gambar mengikut urutan cerita yang betul.
- 3 pusingan (Hujan, Pokok Epal, Masak Nasi)
- Skor: 10 (susunan pertama betul) → 1 (banyak cubaan)
- Mekanisme drag: Pointer Events API (menyokong touch dan mouse)

### G2 — Ingat Nombor (Auditori)
Abah membaca jujukan nombor dengan kuat; anak menaip semula dari ingatan.
- 3 pusingan (panjang nombor meningkat)
- Skor: 10 → 1 berdasarkan bilangan digit yang betul

### G3 — Teka Huruf (Kinestetik)
Abah melukis huruf di belakang tangan anak; anak meneka.
- 3 pusingan
- Skor: median 3 percubaan menggunakan skema linear ramp

---

## Sistem Skor

Setiap permainan menghasilkan skor 1–10 untuk dimensi berkaitan.
Skor akhir dipaparkan sebagai bar animasi.
Laporan teks (eksport) merangkumi skor mentah + rumusan wawasan untuk Claude.

---

## Asma Mode

Diaktifkan apabila "Asma" dipilih dalam dropdown.
Butang ▶ muncul di G1; menekannya memainkan fail MP3 dari `v2/audio/`.

| Fail | Kandungan |
|------|-----------|
| `asma_welcome.mp3` | Salam pembuka sesi |
| `asma_g1_intro.mp3` | Pengenalan G1 |
| `asma_g1_r0_prompt.mp3` | Soalan Pusingan 0 (Hujan) |
| `asma_g1_r1_prompt.mp3` | Soalan Pusingan 1 (Pokok) |
| `asma_g1_r2_prompt.mp3` | Soalan Pusingan 2 (Masak Nasi) |
| `asma_correct.mp3` | Maklum balas betul |
| `asma_tryagain.mp3` | Maklum balas salah |
| `asma_hint_r0/r1/r2.mp3` | Petunjuk setiap pusingan |
| `asma_next_round.mp3` | Peralihan pusingan |
| `asma_done.mp3` | Sesi selesai |
| `asma_call_abah.mp3` | Panggil Abah |

**Suara:** ms-MY-YasminNeural (Microsoft Edge TTS, percuma, tanpa API key)
**Jana semula:** `python vak/scripts/generate_asma_audio.py`

---

## Keputusan Teknikal

- **Satu fail HTML** — tiada build step, tiada CDN dependency (kecuali Google Fonts)
- **Pointer Events** untuk drag (bukan Touch Events) — menyokong semua peranti
- **Median untuk G3** — lebih robust berbanding min untuk 3 percubaan
- **Tema per-anak dalam CSS variables** — mudah ditambah anak baru
- **Tiada penyimpanan data** — sesi bersih selepas tutup tab; laporan dieksport secara manual

---

## Format Laporan (Eksport)

```
=== VAK Assessment Report ===
Child: [Nama]
Date: [Tarikh]

G1 Visual Score: X/10
G2 Auditory Score: X/10
G3 Kinaesthetic Score: X/10

Dominant Style: [V/A/K]

[Wawasan ringkas]
```

---

## KIV / Kerja Masa Hadapan

- G2 (Auditori): auto-TTS untuk baca nombor (kini Abah baca sendiri)
- G3 (Kinestetik): tambah pusingan abjad Mandarin atau Jawi
- Simpan sejarah sesi (localStorage)
- Sokongan bahasa: BM penuh (kini sebahagian BM, sebahagian BI)
