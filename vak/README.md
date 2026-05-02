# VAK Assessment

Alat penilaian gaya belajar Visual–Auditori–Kinestetik untuk anak-anak keluarga ARH.

**Dibina sebab:** Aflah dan Haidar sering lupa ejaan walaupun sudah belajar. Ingin tahu sama ada gaya belajar mereka lebih visual, auditori, atau kinestetik supaya Abah boleh pilih cara mengajar yang lebih berkesan.

---

## Anak-anak

| Nama | Umur | Versi | Tema warna |
|------|------|-------|------------|
| Aflah | 10 | v2 | Merah jambu (pink) |
| Haidar | 8 | v2 | Merah (red) |
| Asma | 5 | v2 (Asma Mode) | Biru (blue) |

---

## Cara Abah Jalankan Sesi

1. Buka `v2/` (atau [arh-kids-space.pages.dev/vak/v2/](https://arh-kids-space.pages.dev/vak/v2/))
2. Pilih nama anak dari dropdown
3. Uruskan 3 permainan mengikut turutan:
   - **G1 — Susun Gambar** (urutan logik): anak susun 4 gambar ikut cerita
   - **G2 — Ingat Nombor** (ingatan auditori): Abah baca nombor, anak taip balik
   - **G3 — Teka Huruf** (sentuhan/kinestetik): anak teka huruf yang dilukis di belakang tangan
4. Klik **Eksport Laporan** → salin teks → tampal ke Claude untuk analisis

**Asma Mode:** Butang audio muncul di G1 apabila "Asma" dipilih. Tekan ▶ untuk Asma dengar arahan dalam Bahasa Melayu (suara YasminNeural).

---

## Versi

| Versi | Tarikh | Ringkasan |
|-------|--------|-----------|
| v1 | 2026-04-28 | Binaan pertama — 3 permainan, skor asas VAK |
| v2 | 2026-05-02 | Tema pastel per-anak, drag Pointer Events, skor median G3, ramp linear, tambah anak baru, skor bar animasi, rumusan wawasan |

v1 diarkib di `v1/` — tidak digunakan tetapi disimpan sebagai rujukan.

---

## Audio Asma

13 fail MP3 tersimpan di `v2/audio/`. Dijana menggunakan Microsoft Edge TTS (ms-MY-YasminNeural).

**Jana semula jika perlu:**
```bash
pip install edge-tts
python vak/scripts/generate_asma_audio.py
```

Skrip akan skip fail yang sudah ada — selamat dijalankan berulang kali.

---

## Nota Pembangun

- Satu fail HTML sahaja — tiada build step, tiada dependency
- Buka terus dalam pelayar web
- Semua data sesi disimpan dalam memori sahaja (tiada server, tiada database)
- Untuk tambah anak baru: edit bahagian `CHILDREN` dalam HTML
