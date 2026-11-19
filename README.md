# ARH Kids Space

Ruang belajar interaktif untuk anak-anak keluarga ARH — Aflah, Haidar, Asma.

**Live:** [kids.arh-urus.com](https://kids.arh-urus.com) (Cloudflare Worker `arh-kids-space`; Pages project lama `arh-kids-space.pages.dev` sudah tiada)

---

## Subprojek

| Folder | Aplikasi | Versi | Untuk |
|--------|----------|-------|-------|
| [`vak/`](vak/) | Penilaian gaya belajar VAK | v2 | Aflah, Haidar, Asma |
| [`kawan-belajar/`](kawan-belajar/) | Kuiz Islam · Hafazan · Mandarin | v1 | Aflah, Haidar |
| [`bandar-ilmu/`](bandar-ilmu/) | Permainan bina bandar: matematik + Mandarin | v1 | Aflah, Haidar |

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

1. Buka [kids.arh-urus.com](https://kids.arh-urus.com)
2. Pilih aplikasi
3. Jalankan sesi, eksport laporan, tampal ke Claude untuk analisis

Atau muat turun mana-mana fail `.html` dan buka terus dalam pelayar — tiada internet diperlukan selepas itu.

---

## Deploy

**Semasa (2026-11-20):** `g4-secrets-cli inject --env CLOUDFLARE_API_TOKEN=arh-cloudflare-workers-local/api_token -- npx wrangler@4 deploy`, kemudian `python scripts/attach-domain.py` (dengan inject yang sama) untuk kids.arh-urus.com. Fail dalam `.assetsignore` (skrip, `.md`, session-logs) tidak diterbitkan.

Lama (rosak sejak Julai 2026; projek Pages sudah tiada):

Push ke `main` → GitHub Actions → Cloudflare Pages auto-deploy.
Lihat [`.github/workflows/deploy-pages.yml`](.github/workflows/deploy-pages.yml).
