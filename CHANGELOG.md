# ARH Kids Space — Repo Changelog

Rekod perubahan infrastruktur dan CI/CD peringkat repo.
Perubahan aplikasi dicatatkan dalam CHANGELOG.md masing-masing subprojek.

---

## 2026-05-02

- Susun semula repo kepada struktur monorepo subprojek (vak/ dan kawan-belajar/)
- Setiap subprojek kini mempunyai README, CHANGELOG, folder versi, dan docs tersendiri
- Tukar CF Pages deploy directory dari `artifacts/` ke `.` (repo root)
- Tambah landing page (`index.html`) di root
- Pindah log sesi ke `vak/session-logs/`
- Pindah skrip audio ke `vak/scripts/`
- Jana dan commit audio Asma (13 × asma_*.mp3, ms-MY-YasminNeural)
- Tambah `reusable-cf-pages-deploy.yml` (workflow boleh guna semula untuk projek lain)

## 2026-04-20

- Commit pertama — `artifacts/`, `instruction/`, `worksheets/`, `scripts/`
- Setup Cloudflare Pages deploy via GitHub Actions (wrangler)
- Tambah `scripts/new-cf-project.sh` untuk bootstrap projek CF Pages baru
