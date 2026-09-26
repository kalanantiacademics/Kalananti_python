# level2

> Orientasi folder `B2C/level2`. Dibuat otomatis pada 2026-08-30; isi kode/aset tetap menjadi sumber kebenaran.

Folder proyek/artefak level2. Gunakan tabel di bawah untuk melihat fungsi setiap file dan hubungan dengan subfolder.

## Posisi dalam katalog
- [Katalog Academic_Content](../../CATALOG.md)
- [Index folder induk](../index.md)

## File langsung

| File | Fungsi | Hubungan umum |
|---|---|---|
| [`deck.html`](deck.html) | Halaman materi, deck, assessment, report, atau panduan yang dibuka di browser. | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |

## Subfolder

| Folder | Isi dan hubungan |
|---|---|
| *(tidak ada)* | Semua artefak berada langsung di folder ini. |

## Cara membaca
1. Mulai dari entry point (biasanya `index.html`, `deck.html`, atau file bernama `main_*`).
2. Ikuti file `.js`, `.css`, dan aset yang dirujuk oleh entry point.
3. Untuk backend/deployment, baca `.gs`, `README.md`, `PRD.md`, atau `docs/` sebelum mengubah source.
4. Folder `assets/`, `dist/`, `node_modules/`, virtualenv, dan output QC bersifat pendukung; bukan source utama.
