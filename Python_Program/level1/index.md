# level1

> Orientasi folder `B2C/Python_Program/level1`. Dibuat otomatis pada 2026-08-30; isi kode/aset tetap menjadi sumber kebenaran.

Folder proyek/artefak level1. Gunakan tabel di bawah untuk melihat fungsi setiap file dan hubungan dengan subfolder.

## Posisi dalam katalog
- [Katalog Academic_Content](../../../CATALOG.md)
- [Index folder induk](../index.md)

## File langsung

| File | Fungsi | Hubungan umum |
|---|---|---|
| [`debug_meet6.js`](debug_meet6.js) | Logika frontend, sinkronisasi, data interaksi, atau skrip tooling. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`main_deck.html`](main_deck.html) | Halaman materi, deck, assessment, report, atau panduan yang dibuka di browser. | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`main_deck.js`](main_deck.js) | Logika frontend, sinkronisasi, data interaksi, atau skrip tooling. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`meet1.html`](meet1.html) | Halaman web/interaktif (UI dan logika biasanya berada di file .js/.gs terkait). | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`meet2.html`](meet2.html) | Halaman web/interaktif (UI dan logika biasanya berada di file .js/.gs terkait). | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`meet3.html`](meet3.html) | Halaman web/interaktif (UI dan logika biasanya berada di file .js/.gs terkait). | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`meet4.html`](meet4.html) | Halaman web/interaktif (UI dan logika biasanya berada di file .js/.gs terkait). | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`meet5.html`](meet5.html) | Halaman web/interaktif (UI dan logika biasanya berada di file .js/.gs terkait). | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`temp_block.txt`](temp_block.txt) | Dokumentasi, spesifikasi, catatan, atau panduan. | Baca import/reference dari file entry point untuk detail dependency. |

## Subfolder

| Folder | Isi dan hubungan |
|---|---|
| *(tidak ada)* | Semua artefak berada langsung di folder ini. |

## Cara membaca
1. Mulai dari entry point (biasanya `index.html`, `deck.html`, atau file bernama `main_*`).
2. Ikuti file `.js`, `.css`, dan aset yang dirujuk oleh entry point.
3. Untuk backend/deployment, baca `.gs`, `README.md`, `PRD.md`, atau `docs/` sebelum mengubah source.
4. Folder `assets/`, `dist/`, `node_modules/`, virtualenv, dan output QC bersifat pendukung; bukan source utama.
