# Python Program

> Orientasi folder `B2C/Python_Program`. Dibuat otomatis pada 2026-08-30; isi kode/aset tetap menjadi sumber kebenaran.

Program pembelajaran Python: syllabus, deck per level, source code contoh, lesson plan, dan script generator.

## Posisi dalam katalog
- [Katalog Academic_Content](../../CATALOG.md)
- [Index folder induk](../index.md)

## File langsung

| File | Fungsi | Hubungan umum |
|---|---|---|
| [`.gitignore`](.gitignore) | Metadata/konfigurasi lokal. | Baca import/reference dari file entry point untuk detail dependency. |
| [`add_animation.py`](add_animation.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`AGENTS.md`](AGENTS.md) | Panduan kerja/aturan khusus untuk contributor atau agent. | Baca import/reference dari file entry point untuk detail dependency. |
| [`fix_css.py`](fix_css.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`fix_deck_css.py`](fix_deck_css.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`fix_js_anim.py`](fix_js_anim.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`fix_scroll_and_code.py`](fix_scroll_and_code.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`fix_styles.py`](fix_styles.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`illustrate_deck.py`](illustrate_deck.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`level4_styles.txt`](level4_styles.txt) | Dokumentasi, spesifikasi, catatan, atau panduan. | Baca import/reference dari file entry point untuk detail dependency. |
| [`parse_syllabus.py`](parse_syllabus.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`port_level3_ui.py`](port_level3_ui.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`syllabus_python_kalananti.md`](syllabus_python_kalananti.md) | Dokumentasi, spesifikasi, catatan, atau panduan. | Baca import/reference dari file entry point untuk detail dependency. |
| [`template_lesson_plan_python.html`](template_lesson_plan_python.html) | Halaman materi, deck, assessment, report, atau panduan yang dibuka di browser. | Entry point yang menggabungkan markup, style inline, aset, dan/atau script sibling. |
| [`update_deck.py`](update_deck.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_html_animations.py`](update_html_animations.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |
| [`update_light_mode.py`](update_light_mode.py) | Script Python untuk generator, otomasi, migrasi, validasi, atau server lokal. | Dipakai oleh entry point atau workflow build/QC pada folder ini. |

## Subfolder

| Folder | Isi dan hubungan |
|---|---|
| [`level/`](level/index.md) | Index turunan |
| [`level1/`](level1/index.md) | Index turunan |
| [`level2/`](level2/index.md) | Index turunan |
| [`level3/`](level3/index.md) | Index turunan |
| [`level4/`](level4/index.md) | Index turunan |
| [`marketing/`](marketing/index.md) | Index turunan |

## Cara membaca
1. Mulai dari entry point (biasanya `index.html`, `deck.html`, atau file bernama `main_*`).
2. Ikuti file `.js`, `.css`, dan aset yang dirujuk oleh entry point.
3. Untuk backend/deployment, baca `.gs`, `README.md`, `PRD.md`, atau `docs/` sebelum mengubah source.
4. Folder `assets/`, `dist/`, `node_modules/`, virtualenv, dan output QC bersifat pendukung; bukan source utama.

## Hubungan utama program Python

```text
syllabus_python_kalananti.md
        └─ level1/ … level4/ (deck dan lesson plan)
             └─ level/source-code/ (contoh proyek sebagai inspirasi)
                  └─ script *.py (parse/generate/fix/illustrate)
```

Gunakan `AGENTS.md` sebagai aturan kerja, syllabus sebagai sumber kurikulum, lalu deck level terkait sebagai artefak siswa. Script perbaikan/generator adalah tooling; jangan menganggapnya sebagai materi yang dibuka siswa.
