# ARH Kids Space — As-Built

## Gambaran Keseluruhan

Monorepo yang mengandungi aplikasi web interaktif untuk anak-anak keluarga ARH.
Semua aplikasi adalah fail HTML tunggal — tiada build step, tiada framework, tiada server.

---

## Profil Anak-anak

| Nama | Umur | Sekolah | Keperluan |
|------|------|---------|-----------|
| Aflah | 10 | SJKC + KAFA | VAK assessment, kuiz Islam, hafazan, Mandarin |
| Haidar | 8 | SJKC + KAFA | VAK assessment, kuiz Islam, hafazan, Mandarin |
| Asma | 5 | Prasekolah | VAK assessment (Asma Mode dengan audio BM) |

---

## Seni Bina

```
Browser
  └── Cloudflare Pages (CDN global)
        └── GitHub repo root (.)
              ├── index.html
              ├── vak/v2/index.html  +  audio/
              └── kawan-belajar/v1/index.html
```

- **Tiada backend** — semua logik dalam HTML+JS
- **Tiada database** — data sesi dalam memori sahaja
- **Tiada CDN dependency** — Google Fonts sahaja (boleh dikeluarkan jika offline)

---

## CI/CD

| Perkara | Nilai |
|---------|-------|
| Platform deploy | Cloudflare Pages |
| Trigger | Push ke branch `main` |
| Workflow | `.github/workflows/deploy-pages.yml` |
| Deploy directory | `.` (root repo) |
| Project name CF | `arh-kids-space` |
| Live URL | https://arh-kids-space.pages.dev |

Workflow boleh guna semula tersedia di `reusable-cf-pages-deploy.yml` untuk bootstrap projek CF Pages baru.

---

## Skrip

| Skrip | Tujuan |
|-------|--------|
| `scripts/new-cf-project.sh` | Bootstrap projek Cloudflare Pages baru dari repo ini |
| `scripts/cf-credentials.example` | Contoh format credentials CF |
| `vak/scripts/generate_asma_audio.py` | Jana semula 13 fail MP3 untuk Asma Mode |

---

## KIV

- Pindah repo ke GitHub org keluarga (kini di akaun peribadi)
- ElevenLabs untuk audio berkualiti lebih tinggi (kini edge-tts percuma)
- Branch protection pada `main`
- Tambah subprojek baru: jadual solat, latihan matematik
