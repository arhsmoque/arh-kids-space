# ARH Kids Space

Ruang belajar interaktif untuk anak-anak keluarga ARH — Aflah, Haidar, Asma.

**Live:** [arh-kids-space.pages.dev](https://arh-kids-space.pages.dev)

---

## Subprojek

| Folder | Aplikasi | Versi | Untuk |
|--------|----------|-------|-------|
| [`vak/`](vak/) | Penilaian gaya belajar VAK | v2 | Aflah, Haidar, Asma |
| [`kawan-belajar/`](kawan-belajar/) | Kuiz Islam · Hafazan · Mandarin | v1 | Aflah, Haidar |

Setiap subprojek mempunyai `README.md`, `CHANGELOG.md`, dan folder versi tersendiri.

---

## Struktur Repo

```
arh-kids-space/
├── index.html              ← Landing page (arh-kids-space.pages.dev)
├── vak/                    ← VAK Assessment subprojek
│   ├── v1/                 ← Versi asal (arkib)
│   ├── v2/                 ← Versi semasa + audio Asma
│   ├── scripts/            ← Jana audio TTS
│   └── session-logs/       ← Log sesi yang dieksport
├── kawan-belajar/          ← Kawan Belajar subprojek
│   └── v1/                 ← Versi semasa
├── instruction/            ← Custom instruction Claude.ai Kids Project
├── scripts/                ← Skrip CI/CD repo-level
└── worksheets/             ← Lembaran kerja boleh cetak
```

---

## Cara Guna (Abah)

1. Buka [arh-kids-space.pages.dev](https://arh-kids-space.pages.dev)
2. Pilih aplikasi
3. Jalankan sesi, eksport laporan, tampal ke Claude untuk analisis

Atau muat turun mana-mana fail `.html` dan buka terus dalam pelayar — tiada internet diperlukan selepas itu.

---

## Deploy

Push ke `main` → GitHub Actions → Cloudflare Pages auto-deploy.
Lihat [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).
