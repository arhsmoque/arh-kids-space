# Bandar Ilmu 知识城

Permainan bina bandar untuk Aflah dan Haidar. Bandar hanya membesar bila mereka kira dengan betul:
permainan tidak membuat kira-kira untuk mereka. Soalan ditulis dalam bahasa Cina seperti soalan
peperiksaan SJKC, dengan petunjuk BM satu klik.

**Main:** [kids.arh-urus.com/bandar-ilmu/v1/](https://kids.arh-urus.com/bandar-ilmu/v1/),
atau pasang sebagai aplikasi desktop (luar talian):
`powershell -ExecutionPolicy Bypass -File bandar-ilmu\scripts\install-desktop.ps1`

## Gelung permainan

| Dalam permainan | Kemahiran | Jurang Aflah (kertas 15 Okt 2026) |
|---|---|---|
| Tuai ladang 农场: *setiap jam N guni, sudah H jam* | Darab 乘法 | sifir |
| Pesanan rumah 房子 dalam bahasa Cina (一共, 每, 还要, 已经) | Baca soalan cerita 应用题 | soalan cerita kosong (2/24) |
| Kincir 风车: *mula pukul X, perlu Y, siap pukul?* | 几点结束 | 1 jam = 100 minit |
| Kedai roti 面包店: tempoh bakar, tukar unit masa | 多长时间, 时间单位 | jadual waktu 0/8, unit masa |
| Lori di gudang 仓库: blok ribu/ratus/puluh/sa, 个位…千位, 文字→数字 | 数位 | nilai tempat 1/8, sifar (549 untuk 5409) |
| Beli tanah 土地: luas × harga (Aflah), tambah/tolak (Haidar) | 乘法 / 加减 | pinjam merentasi sifar |

- **Tiada tahap untuk direka.** Setiap soalan dijana dari templat; nombor membesar ikut tahap kemahiran
  (1–5) dan saiz bandar (Kampung → Pekan → Bandar). Kemahiran yang lemah lebih kerap muncul.
- **Dua trek:** *besar* (Aflah, Tahun 3) dan *muda* (Haidar). Tukar dalam panel Abah.
- **Satu PC, giliran:** pilih profil; bandar dikongsi, rekod kemahiran berasingan.
- **Ganjaran:** bandar membesar (penduduk, bangunan baru), duit untuk hiasan, Buku Kata Cina (41 kata
  dengan audio), gelaran ikut penguasaan (Petani Pintar, Tukang Roti, Kerani Gudang, Saudagar, Datuk Bandar).
- **Hari permainan ≈ 15 minit** (7 pagi → 7 malam), ringkasan waktu matahari terbenam, had minit sehari.
- **Panel Abah** (PIN): penguasaan setiap kemahiran, kesilapan terkini dengan jawapan anak, eksport JSON.

## Fail

```
bandar-ilmu/
├── v1/index.html          ← keseluruhan permainan (satu fail, tiada server)
├── v1/audio/*.mp3         ← sebutan kata Cina (zh-CN-XiaoxiaoNeural)
└── scripts/
    ├── generate_audio.py  ← jana audio dari senarai WORDS dalam index.html
    └── install-desktop.ps1← pasang sebagai aplikasi Edge di desktop
```

Kemajuan disimpan dalam pelayar (localStorage) pada mesin itu. Guna **Eksport/Import** dalam panel Abah
untuk sandaran atau pindah mesin.
