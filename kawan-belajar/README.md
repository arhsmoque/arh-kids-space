# Kawan Belajar

Alat belajar interaktif untuk Aflah dan Haidar — tiga modul dalam satu aplikasi.

**Dibina sebab:** Aflah (SJKC + KAFA) dan Haidar memerlukan latihan hafazan surah, kuiz Islam asas,
dan ulangkaji karakter Mandarin dalam satu tempat yang mudah dibuka.

---

## Tiga Modul

| Modul | Kandungan | Siapa |
|-------|-----------|-------|
| **Kuiz Islam** | 13 soalan pilihan berganda (aqidah, ibadah, akhlak) | Aflah, Haidar |
| **Hafazan Tracker** | 10 surah (Al-Fatihah → Al-Asr) — tandakan hafal/belum | Aflah, Haidar |
| **Karakter Mandarin** | 16 kad imbas aksara asas dengan sebutan Pinyin | Aflah, Haidar |

---

## Cara Guna

Buka `v1/` atau [arh-kids-space.pages.dev/kawan-belajar/v1/](https://arh-kids-space.pages.dev/kawan-belajar/v1/) dalam pelayar web.
Tiada internet diperlukan selepas dimuat naik.

---

## Cara Tambah Kandungan

Semua data dalam satu fail HTML. Cari dan edit bahagian berikut:

- **Kuiz:** cari array `quizData` → tambah objek `{ q, options, answer }`
- **Hafazan:** cari array `surahs` → tambah nama surah
- **Mandarin:** cari array `characters` → tambah `{ char, pinyin, meaning }`

---

## Nota Pembangun

- Satu fail HTML — buka terus dalam pelayar, tiada build step
- Keadaan tidak disimpan antara sesi (tiada localStorage pada v1)
