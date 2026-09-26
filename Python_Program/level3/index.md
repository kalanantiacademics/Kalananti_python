# level3

> Orientasi folder `B2C/Python_Program/level3`. Dibuat otomatis pada 2026-08-30; isi kode/aset tetap menjadi sumber kebenaran.

Folder proyek/artefak level3. Gunakan tabel di bawah untuk melihat fungsi setiap file dan hubungan dengan subfolder.

## Posisi dalam katalog
- [Katalog Academic_Content](../../../CATALOG.md)
- [Index folder induk](../index.md)

## File langsung

| File | Fungsi | Hubungan umum |
|---|---|---|
| [`deck.html`](deck.html) | Halaman materi, deck, assessment, report, atau panduan yang dibuka di browser. | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`deck.html.merged`](deck.html.merged) | File pendukung proyek; cek referensi/import dari source utama. | Baca import/reference dari file entry point untuk detail dependency. |
| [`merge_deck.py`](merge_deck.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_deck_s2_s3.py`](update_deck_s2_s3.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session10.py`](update_session10.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session11.py`](update_session11.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session12.py`](update_session12.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session4.py`](update_session4.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session5.py`](update_session5.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session6.py`](update_session6.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session7.py`](update_session7.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session8.py`](update_session8.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_session9.py`](update_session9.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |

## Subfolder

| Folder | Isi dan hubungan |
|---|---|
| *(tidak ada)* | Semua artefak berada langsung di folder ini. |

## Cara membaca
1. Mulai dari entry point (biasanya `index.html`, `deck.html`, atau file bernama `main_*`).
2. Ikuti file `.js`, `.css`, dan aset yang dirujuk oleh entry point.
3. Untuk backend/deployment, baca `.gs`, `README.md`, `PRD.md`, atau `docs/` sebelum mengubah source.
4. Folder `assets/`, `dist/`, `node_modules/`, virtualenv, dan output QC bersifat pendukung; bukan source utama.
