# -*- coding: utf-8 -*-
"""Generate official Lesson Plan HTML for Level 2 (Planet Modula - Data Manipulation & Visual Art)"""

import sys

def build_lesson_plan():
    html = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Official Lesson Plan Kalananti B2C Python Level 2 — Planet Modula, Data Manipulation & Visual Art">
    <title>Lesson Plan Python Level 2 — Planet Modula</title>
    <style>
        :root {
            --blue: #265e9b;
            --blue-dark: #173f70;
            --blue-pale: #f0f6fc;
            --blue-light: #e2eef9;
            --yellow: #f9c013;
            --yellow-pale: #fffde6;
            --teal: #339d9d;
            --teal-pale: #e6f5f5;
            --ink: #1e293b;
            --muted: #64748b;
            --line: #cbd5e1;
            --paper: #ffffff;
            --screen: #e2e8f0;
        }

        * { box-sizing: border-box; }
        html { scroll-behavior: smooth; }

        body {
            margin: 0;
            background: var(--screen);
            color: var(--ink);
            font-family: "Avenir Next", Avenir, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 8.5pt;
            line-height: 1.35;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }

        #document {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10mm;
            padding: 10mm 0 20mm;
        }

        .page {
            position: relative;
            width: 210mm;
            min-height: 297mm;
            height: auto;
            padding: 18mm 16mm 14mm;
            background: var(--paper);
            border: 1px solid rgba(38, 94, 155, .15);
            box-shadow: 0 8px 25px rgba(15, 23, 42, .12);
            break-after: page;
            page-break-after: always;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .page:last-child {
            break-after: auto;
            page-break-after: auto;
        }

        .page-body {
            flex: 1 0 auto;
            display: flex;
            flex-direction: column;
        }

        .page-header {
            position: absolute;
            top: 5mm;
            left: 14mm;
            right: 14mm;
            height: 12mm;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 2px solid var(--blue-pale);
            padding-bottom: 1.5mm;
        }

        .page-header img {
            height: 9.5mm;
            width: auto;
            object-fit: contain;
        }

        .brand-ribbons {
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 1mm;
        }

        .brand-ribbons .top-stripe {
            width: 60mm;
            height: 3mm;
            background: var(--blue);
            border-radius: 3px 0 0 3px;
            position: relative;
        }

        .brand-ribbons .top-stripe::before {
            content: "";
            position: absolute;
            top: 0;
            left: -8mm;
            width: 8mm;
            height: 3mm;
            background: var(--yellow);
            clip-path: polygon(100% 0, 0 50%, 100% 100%);
        }

        .brand-ribbons .dots {
            width: 50mm;
            height: 2mm;
            background-image: radial-gradient(circle, var(--yellow) 1mm, transparent 1.1mm);
            background-size: 4.5mm 2mm;
            background-repeat: repeat-x;
        }

        .page-footer {
            margin-top: 5mm;
            flex-shrink: 0;
            display: flex;
            flex-direction: column;
        }

        .footer-meta {
            display: flex;
            justify-content: space-between;
            color: var(--muted);
            font-size: 7.5pt;
            font-weight: 600;
            padding-bottom: 1mm;
            border-bottom: 1px solid var(--line);
        }

        .footer-stripes {
            height: 2mm;
            display: flex;
            width: 100%;
            margin-top: 1mm;
        }

        .footer-stripes .st-blue { flex: 4; background: var(--blue); }
        .footer-stripes .st-yellow { flex: 2; background: var(--yellow); }
        .footer-stripes .st-teal { flex: 2; background: var(--teal); }

        h1, h2, h3, h4 {
            color: var(--blue-dark);
            margin: 0 0 1.5mm 0;
            font-weight: 700;
        }

        h1 { font-size: 16pt; letter-spacing: -0.3px; }
        h2 { font-size: 12pt; border-bottom: 1.5px solid var(--blue-light); padding-bottom: 1mm; margin-top: 1mm; }
        h3 { font-size: 9.5pt; color: var(--blue); margin-top: 2.5mm; }
        p { margin: 0 0 2mm 0; color: #334155; }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 7.8pt;
            margin: 2mm 0;
        }

        th, td {
            border: 1px solid var(--line);
            padding: 1.8mm 2.2mm;
            text-align: left;
            vertical-align: top;
        }

        th {
            background: var(--blue-pale);
            color: var(--blue-dark);
            font-weight: 700;
        }

        .badge {
            display: inline-block;
            padding: 0.8mm 2.5mm;
            border-radius: 3px;
            font-size: 7pt;
            font-weight: 700;
            background: var(--blue-light);
            color: var(--blue-dark);
        }

        .badge-green { background: #dcfce7; color: #15803d; }
        .badge-yellow { background: var(--yellow-pale); color: #854d0e; }
        .badge-purple { background: #f3e8ff; color: #6b21a8; }

        .callout {
            padding: 2.5mm 3.5mm;
            border-radius: 4px;
            border-left: 3.5px solid var(--blue);
            background: var(--blue-pale);
            margin: 2mm 0;
            font-size: 8pt;
        }

        .callout-warn { border-left-color: #f59e0b; background: var(--yellow-pale); }
        .callout-success { border-left-color: #10b981; background: #ecfdf5; }

        .terminal-box {
            background: #1e1e1e;
            color: #38bdf8;
            font-family: "Consolas", "Courier New", monospace;
            font-size: 7.5pt;
            padding: 3mm 4mm;
            border-radius: 6px;
            border: 1px solid #334155;
            margin: 2mm 0;
            line-height: 1.3;
        }

        /* Cover Specific */
        .cover-page {
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 40mm 20mm;
            background: radial-gradient(circle at 50% 20%, #e2eef9 0%, #ffffff 70%);
        }

        .cover-logo { height: 18mm; width: auto; margin-bottom: 12mm; }
        .cover-title { font-size: 26pt; color: var(--blue-dark); font-weight: 800; letter-spacing: -0.5px; }
        .cover-subtitle { font-size: 13pt; color: var(--blue); font-weight: 600; margin-top: 3mm; }
        .cover-planet { font-size: 11pt; color: var(--yellow); background: var(--blue-dark); padding: 1.5mm 6mm; border-radius: 20px; display: inline-block; font-weight: 700; margin-top: 6mm; letter-spacing: 1px; }
        .cover-meta { margin-top: 25mm; border-top: 2px solid var(--blue-light); padding-top: 6mm; font-size: 8.5pt; color: var(--muted); }

        @media print {
            body { background: white; }
            #document { padding: 0; gap: 0; }
            .page { box-shadow: none; border: none; min-height: 297mm; height: 297mm; page-break-after: always; break-after: page; }
        }
    </style>
</head>
<body>
    <div id="document">
"""

    logo_url = "https://cdn-web-2.ruangguru.com/landing-pages/assets/545c0426-169c-406f-8775-93afcacef50a.png"

    def page_header(meet_str):
        return f"""
        <div class="page-header">
            <img src="{logo_url}" alt="Kalananti Logo">
            <div class="brand-ribbons">
                <div class="top-stripe"></div>
                <div class="dots"></div>
            </div>
        </div>
        """

    def page_footer(page_num, total_pages=15):
        return f"""
        <div class="page-footer">
            <div class="footer-meta">
                <span>Kalananti B2C Python — Level 2: Planet Modula (Data Manipulation & Visual Art)</span>
                <span>Halaman {page_num} dari {total_pages}</span>
            </div>
            <div class="footer-stripes">
                <div class="st-blue"></div>
                <div class="st-yellow"></div>
                <div class="st-teal"></div>
            </div>
        </div>
        """

    # --- PAGE 1: COVER ---
    html += f"""
        <div class="page cover-page">
            <img class="cover-logo" src="{logo_url}" alt="Kalananti Logo">
            <h1 class="cover-title">OFFICIAL LESSON PLAN</h1>
            <div class="cover-subtitle">Python Level 2 — Data Manipulation & Visual Art</div>
            <div class="cover-planet">🪐 PLANET MODULA</div>

            <div style="max-width: 140mm; margin: 15mm auto 0; text-align: left; font-size: 8.5pt; background: rgba(255,255,255,0.85); padding: 5mm 8mm; border-radius: 8px; border: 1px solid var(--blue-light);">
                <p><b>Target Siswa:</b> Usia 9–14 Tahun (SD Akhir / SMP - Lulusan Level 1)</p>
                <p><b>Alokasi Waktu Pedagogis:</b> 60–90 Menit per Pertemuan (30% Teori / 60% Hands-on / 10% Refleksi)</p>
                <p><b>Rasio Slide Efektif:</b> 16–24 Slide per Pertemuan (Bebas Duplikasi & Analogi Berulang)</p>
                <p><b>Kurikulum Acuan:</b> Silabus Resmi B2C Kalananti (SSOT1 B2C_Python Tab - Level 2)</p>
                <p><b>Teknologi Utama:</b> Python 3.10+, Struktur Data (List, Dict), String I/O, Modul Turtle Graphics</p>
                <p><b>Fokus Capstone:</b> 3 Pilihan Proyek (Turtle Art Gallery, Text RPG Adventure, Smart Cafe / Student DB)</p>
            </div>

            <div class="cover-meta">
                <p><b>Kalananti Academic & Curriculum Development Team</b></p>
                <p>Dokumen Pegangan Guru — Dilengkapi Panduan Waktu, Diagnostik Bug Hunt, dan Kunci Jawaban</p>
            </div>
            {page_footer(1)}
        </div>
    """

    # --- PAGE 2: PROGRAM OVERVIEW & RESTRUCTURING RATIONALE ---
    html += f"""
        <div class="page">
            {page_header("Overview")}
            <div class="page-body">
                <h2>1. Program Overview & Restructuring Rationale</h2>
                <p>Level 2 (Planet Modula) merupakan fase transisi krusial di mana siswa beralih dari sekadar mengeksekusi variabel tunggal menjadi <b>pengendali koleksi data terstruktur</b> dan <b>seniman komputasi visual</b>. Siswa menguasai manipulasi struktur data (List Methods, Dictionary Key-Value), pengolahan teks (String Manipulation), penyimpanan permanen (File Handling .txt), hingga pemrograman visual (Turtle Graphics & Pixel Art Grid).</p>

                <h3>1.1 Resolusi Feedback Pengajar: Rasionalisasi Beban Slide</h3>
                <div class="callout callout-warn">
                    <b>Evaluasi Guru Sebelumnya:</b> Deck Level 2 sebelumnya memiliki rata-rata 45 slide per pertemuan yang padat dengan analogi berulang, 5 slide flashback terpisah, dan placeholder materi tambahan kosong. Hal ini menyebabkan waktu kelas habis untuk ceramah slide dan memotong waktu praktik mengetik kode siswa.
                </div>
                <p>Dalam kurikulum terevisi ini, materi disederhanakan menjadi <b>16–24 slide berbobot tinggi</b> dengan menerapkan aturan alokasi waktu:</p>
                <ul>
                    <li><b>Maksimal 30% Waktu Kelas (15–25 Menit):</b> Pengantar konsep inti, visual mental model, dan Active-Recall Speed Review.</li>
                    <li><b>Minimal 60% Waktu Kelas (40–55 Menit):</b> Hands-on coding murni! Siswa mengetik langsung di IDE melalui Guided Coding, Bug Hunt Diagnostic, Independent Exercise, dan Challenge Mode bertingkat (Bronze, Silver, Gold).</li>
                    <li><b>Sekitar 10% Waktu Kelas (5–10 Menit):</b> Refleksi, Cheat Sheet summary, dan persiapan misi selanjutnya.</li>
                </ul>

                <h3>1.2 Pedoman Mengajar Guru di Kelas</h3>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">Aktivitas Deck</th>
                            <th style="width: 45%;">Peran & Tindakan Guru</th>
                            <th style="width: 30%;">Target Siswa</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Speed Review</b></td>
                            <td>Tampilkan kode di layar, minta siswa menebak output serentak dalam 30 detik. Jangan ceramah ulang teori Sesi lalu.</td>
                            <td>Active recall & kesiapan mental</td>
                        </tr>
                        <tr>
                            <td><b>Guided Exercise</b></td>
                            <td>Ketik kode bersama siswa baris per baris. Jelaskan fungsi operator dan method kunci saat sedang mengetik.</td>
                            <td>Semua siswa memiliki script dasar yang berjalan</td>
                        </tr>
                        <tr>
                            <td><b>Detektif Bug</b></td>
                            <td>Tantang siswa menemukan baris yang menyebabkan error (misal: KeyError, IndexError, FileNotFoundError).</td>
                            <td>Melatih ketajaman debugging mandiri</td>
                        </tr>
                        <tr>
                            <td><b>Challenge Mode</b></td>
                            <td>Berikan kebebasan memilih Challenge 1 (Mudah), Challenge 2 (Sedang), atau Challenge 3 (Sulit). Guru berkeliling memberi asistensi.</td>
                            <td>Diferensiasi kemampuan siswa</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            {page_footer(2)}
        </div>
    """

    # --- PAGE 3: SCOPE & SEQUENCE MATRIX ---
    html += f"""
        <div class="page">
            {page_header("Matrix")}
            <div class="page-body">
                <h2>2. Scope & Sequence Matrix (12 Pertemuan)</h2>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 7%;">Sesi</th>
                            <th style="width: 22%;">Topik Utama</th>
                            <th style="width: 35%;">Kompetensi & Sintaks Inti</th>
                            <th style="width: 36%;">Aktivitas Hands-on & Output</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Sesi 1</b></td>
                            <td><b>Advanced Lists & Slicing</b></td>
                            <td>Zero-based index, slicing <code>[start:stop]</code>, method <code>.append()</code>, <code>.insert()</code>, <code>.pop()</code>, <code>.remove()</code>, <code>.sort()</code>.</td>
                            <td>Sistem Inventaris Cyber: Menambah, mengiris, dan mengurutkan item game.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 2</b></td>
                            <td><b>Dictionary (Key-Value)</b></td>
                            <td>Sintaks <code>{{key: value}}</code>, akses aman <code>.get()</code>, update data, <code>.keys()</code>, <code>.values()</code>, <code>.items()</code>.</td>
                            <td>Pokedex Database & Sistem Kasir Supermarket dengan looping kamus.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 3</b></td>
                            <td><b>String Manipulation</b></td>
                            <td>Slicing teks, casing (<code>.upper()</code>, <code>.lower()</code>), <code>.split()</code>, <code>.join()</code>, <code>.strip()</code>, <code>.replace()</code>.</td>
                            <td>Bot Sensor Chat Otomatis & Pembersih Nomor Kontak Internasional.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 4</b></td>
                            <td><b>File Handling Dasar</b></td>
                            <td>RAM vs Harddisk, mode <code>'r'</code>, <code>'w'</code>, <code>'a'</code>, <code>with open()</code>, <code>\\n</code>, <code>.read()</code>, <code>.readlines()</code>.</td>
                            <td>Buku Tamu Digital (Log Append) & Game Highscore Saver permanen (.txt).</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 5</b></td>
                            <td><b>Intro to Turtle Graphics</b></td>
                            <td>Modul <code>turtle</code>, <code>forward()</code>, <code>left()</code>, <code>right()</code>, <code>penup()</code>, <code>pendown()</code>, <code>begin/end_fill()</code>.</td>
                            <td>Bendera Merah Putih, Bintang Bersudut 5, dan Rumah Geometri.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 6</b></td>
                            <td><b>Colors & Pen Control</b></td>
                            <td>Sistem RGB 0-255, <code>colormode(255)</code>, <code>bgcolor()</code>, <code>color(p, f)</code>, <code>stamp()</code>, <code>random.randint()</code>.</td>
                            <td>Langit Malam Berbintang, Jam Dinding Modern, dan Hujan Pelangi RGB.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 7</b></td>
                            <td><b>Turtle & Loops</b></td>
                            <td>Otomatisasi loop, rumus poligon <code>360 / N</code>, variabel <code>i</code> spiral dinamis, nested loop spirograph.</td>
                            <td>Jaring Laba-laba Spiral, Spirograph Bunga, dan Mandala Art Geometri.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 8</b></td>
                            <td><b>Nested Loops & Grid</b></td>
                            <td>Pemindaian Baris x Kolom, konversi <code>(row, col) -> (x, y)</code>, papan catur modulo 2, matrix 2D list.</td>
                            <td>Papan Catur Hitam-Putih & Pixel Art Karakter Minecraft Creeper 2D.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 9</b></td>
                            <td><b>Brainstorming & Planning</b></td>
                            <td>Siklus SDLC, pemilihan 3 jalur Capstone, Game Design Document (GDD), Flowchart & Pseudocode.</td>
                            <td>Penyusunan proposal proyek siswa dan konsultasi desain dengan guru.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 10</b></td>
                            <td><b>Coding Phase 1 (Core)</b></td>
                            <td>Implementasi struktur data utama (List/Dict), alur input-proses-output dasar (Functional First).</td>
                            <td>Membangun pondasi mekanik inti proyek sesuai blueprint GDD.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 11</b></td>
                            <td><b>Coding Phase 2 (Polesan)</b></td>
                            <td>Penyimpanan file permanen (.txt), sanitasi input string, debugging error, dekorasi UI/output.</td>
                            <td>Finishing proyek, membasmi bug, dan latihan demo kelancaran program.</td>
                        </tr>
                        <tr>
                            <td><b>Sesi 12</b></td>
                            <td><b>Showcase & Graduation</b></td>
                            <td>Pitching 3 menit, demonstrasi live code, evaluasi rubrik adil (UI, Logika, Kreativitas, Presentasi).</td>
                            <td>Presentasi akbar proyek akhir dan penyerahan sertifikat kelulusan Level 2.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            {page_footer(3)}
        </div>
    """

    meetings_data = [
        {
            "num": 1,
            "title": "Advanced Lists & Slicing",
            "unit": "Unit 1: Data & Visual Foundations",
            "obj": "Membuat List data, mengakses elemen dengan zero-based indexing, memotong sebagian data (slicing), serta memanipulasi list dengan method bawaan.",
            "vocab": "List, Index, Zero-based, Slicing [start:stop:step], .append(), .insert(), .pop(), .remove(), .sort().",
            "tech": "<b>Memory Model:</b> List menyimpan alamat memori terurut. Slicing <code>[a:b]</code> mengambil data mulai indeks <code>a</code> hingga <code>b-1</code>. <code>.append()</code> memasukkan ke ujung belakang, <code>.insert(idx, val)</code> menyisipkan di tengah, <code>.pop()</code> mencabut elemen dan mengembalikan nilainya.",
            "output": """=== SISTEM INVENTARIS CYBER ===
Isi Tas: ['Health Potion', 'Laser Pistol', 'Shield']
Senjata Baru Disisipkan: ['Health Potion', 'Plasma Sword', 'Laser Pistol', 'Shield']
Item yang Digunakan: Shield
Urutan Alfabet: ['Health Potion', 'Laser Pistol', 'Plasma Sword']""",
            "err": "<b>IndexError: list index out of range:</b> Siswa memanggil index yang sama dengan <code>len(list)</code>. Ingat bahwa pada list berisi 3 item, index maksimal adalah 2.",
            "diff": "<b>Min:</b> List 4 item, tambah 1 item dengan append, hapus dengan pop.<br><b>Bonus:</b> Buat sistem antrian skor terurut dengan <code>.sort(reverse=True)</code>."
        },
        {
            "num": 2,
            "title": "Dictionary (Key-Value Pairs)",
            "unit": "Unit 1: Data & Visual Foundations",
            "obj": "Menyimpan data berpasangan label-nilai (Key-Value), mengakses data secara instan, mencegah KeyError dengan method .get(), dan mengekstrak data kamus.",
            "vocab": "Dictionary, Key (Kunci Unik), Value (Nilai Bebas), KeyError, .get(), .keys(), .values(), .items(), Nested Dictionary.",
            "tech": "<b>Hash Map Lookup:</b> Tidak seperti List yang mencari O(N) berurutan, Dictionary menggunakan Hash Table O(1) langsung menuju sasaran Key. Method <code>.get(k, default)</code> aman dari crash jika Key belum terdaftar. Looping <code>for k, v in d.items():</code> membongkar pasangan data sekaligus.",
            "output": """=== POKEDEX DATABASE ===
Masukkan Pokemon: Pikachu
Nama   : Pikachu
Tipe   : Electric
Power  : 55 HP
Status : Siap Bertarung! ⚡""",
            "err": "<b>KeyError & Case Sensitivity:</b> Siswa memanggil <code>data['nama']</code> padahal key-nya adalah <code>'Nama'</code>. Gunakan <code>.get()</code> dan samakan ukuran huruf.",
            "diff": "<b>Min:</b> Dictionary biodata 4 atribut, ubah 1 nilai, dan panggil via .get().<br><b>Bonus:</b> Simulasi kasir supermarket hitung total belanja dengan looping <code>.items()</code>."
        },
        {
            "num": 3,
            "title": "String Manipulation & Methods",
            "unit": "Unit 1: Data & Visual Foundations",
            "obj": "Memperlakukan string sebagai sekuens karakter, menyeragamkan format teks, memecah kalimat (split), menyatukan kata (join), serta menyaring teks terlarang.",
            "vocab": "String Immutability, Text Casing, .upper(), .lower(), .title(), .split(), .join(), .strip(), .replace(), Method Chaining.",
            "tech": "<b>String Immutability:</b> Teks di Python tidak dapat diubah sebagian (<code>s[0]='x'</code> menghasilkan TypeError). Untuk mengubahnya, buat string baru menggunakan method string atau rekombinasi potongan slicing. <code>.strip()</code> memangkas whitespace ujung, <code>.split(sep)</code> menghasilkan List, dan <code>glue.join(list)</code> menyatukan list menjadi String.",
            "output": """=== CHAT FILTER BOT ===
Input User   : '  DASAR kamu curang dan bodoh!  '
Setelah Strip: 'DASAR kamu curang dan bodoh!'
Hasil Sensor : 'DASAR kamu ****** dan *****!'
Status       : Pesan Aman Terkirim ✅""",
            "err": "<b>TypeError: 'str' does not support item assignment:</b> Guru mengingatkan bahwa string bersifat immutable; hasil operasi harus disimpan kembali ke variabel baru.",
            "diff": "<b>Min:</b> Sanitasi input teks dengan <code>.strip().lower()</code> dan validasi if-else.<br><b>Bonus:</b> Buat generator URL Web Slug menggunakan <code>.lower().replace().split()</code> dan <code>'-'.join()</code>."
        },
        {
            "num": 4,
            "title": "File Handling Dasar (I/O File)",
            "unit": "Unit 1: Data & Visual Foundations",
            "obj": "Memahami perbedaan RAM dan Harddisk, membuka file teks dengan mode 'r', 'w', 'a', serta mengamankan pembacaan berkas dengan 'with open()'.",
            "vocab": "File Handling, Persistence, Harddisk, RAM, Mode 'r', Mode 'w', Mode 'a', Context Manager (with open), Karakter Newline (\\n).",
            "tech": "<b>Persistence & I/O Streams:</b> Mode <code>'w'</code> menimpa file dari awal (truncate), mode <code>'a'</code> menulis di baris akhir tanpa menghapus data lama. Konstruksi <code>with open() as f:</code> adalah Context Manager Python yang menjamin pemanggilan <code>.close()</code> secara otomatis meskipun terjadi crash logika di dalam blok.",
            "output": """=== CATATAN LOG BUKU TAMU ===
Masukkan Nama : Budi
Pesan Singkat : Senang belajar Python di Kalananti!
Menyimpan ke file 'buku_tamu.txt'... Berhasil!
Isi file saat ini:
1. Andi: Halo semua!
2. Budi: Senang belajar Python di Kalananti!""",
            "err": "<b>FileNotFoundError pada Mode 'r':</b> Guru memandu siswa untuk memastikan file sudah dibuat terlebih dahulu atau menggunakan mode 'a' yang otomatis membuat file jika belum ada.",
            "diff": "<b>Min:</b> Menulis 2 baris ke file dengan mode 'w' dan membaca isinya dengan mode 'r'.<br><b>Bonus:</b> Sistem Game Highscore yang hanya mengupdate skor jika skor baru lebih tinggi dari file lama."
        },
        {
            "num": 5,
            "title": "Intro to Turtle Graphics",
            "unit": "Unit 2: Logic & Automation",
            "obj": "Menginisialisasi modul turtle, menavigasi gerakan kura-kura dengan koordinat dan sudut derajat, mengontrol pena, serta mewarnai bidang tertutup.",
            "vocab": "Turtle Graphics, Kanvas Layar, forward(), backward(), left(), right(), penup(), pendown(), goto(x, y), begin_fill(), end_fill(), turtle.done().",
            "tech": "<b>Turtle State Machine:</b> Objek kura-kura bertindak seperti state machine yang memiliki posisi (x,y), orientasi heading (0° = Timur), status pena (up/down), dan warna. Setiap belokan memutar heading relatif terhadap arah saat ini. Pola fill mewajibkan jalur garis tertutup agar warna tidak bocor.",
            "output": """[ Jendela Kanvas Turtle 600x600 ]
- Latar Belakang: Putih
- Gambar: Bendera Merah Putih
  * Kotak 1: Merah Terang (Lebar 200, Tinggi 60)
  * Kotak 2: Putih Bergaris Abu (Lebar 200, Tinggi 60)
- Posisi Akhir Kura-Kura: Tersembunyi (hideturtle)""",
            "err": "<b>Coretan Garis Hantu saat Pindah:</b> Siswa lupa memanggil <code>t.penup()</code> sebelum berpindah koordinat dengan <code>goto()</code>.",
            "diff": "<b>Min:</b> Menggambar persegi 4 sisi dengan warna pena dan warna isi berbeda.<br><b>Bonus:</b> Menggambar bintang bersudut lima emas menggunakan sudut putar 144 derajat."
        },
        {
            "num": 6,
            "title": "Colors & Pen Control",
            "unit": "Unit 2: Logic & Automation",
            "obj": "Mengaktifkan spektrum 16 juta warna RGB, mengatur latar kanvas, memanfaatkan stamp() untuk kloning instan, serta menghasilkan warna acak dengan modul random.",
            "vocab": "RGB (Red, Green, Blue 0–255), colormode(255), bgcolor(), color(pen, fill), stamp(), dot(), random.randint().",
            "tech": "<b>Addictive Color Model (RGB):</b> Setiap kanal warna direpresentasikan oleh integer 8-bit (0 hingga 255). Pemanggilan <code>turtle.colormode(255)</code> wajib dilakukan sebelum memasukkan angka RGB integer. <code>t.stamp()</code> menduplikasi bentuk turtle ke canvas buffer tanpa beban kalkulasi garis.",
            "output": """[ Jendela Kanvas Turtle Malam ]
- Background: Black (#000000)
- Objek: Jam Dinding Modern 12 Angka
  * 12 Titik Stempel Emas Melingkar Rapi
  * Jarak Radius: 120 piksel
  * Sudut Belok Antar Titik: 30 derajat (360 / 12)""",
            "err": "<b>TurtleGraphicsError: bad color sequence:</b> Siswa memasukkan angka RGB (misal 255, 0, 0) tanpa menuliskan <code>turtle.colormode(255)</code> di awal script.",
            "diff": "<b>Min:</b> Mengubah latar belakang hitam dan menggambar 10 titik stempel berwarna.<br><b>Bonus:</b> Hujan pelangi vertikal dengan posisi X, Y dan warna RGB acak berkilauan."
        },
        {
            "num": 7,
            "title": "Turtle & Loops (Seni Geometri)",
            "unit": "Unit 2: Logic & Automation",
            "obj": "Mengotomatisasi gambar geometri dengan For Loop, menerapkan rumus poligon 360/N, membuat pola spiral dinamis dengan counter i, dan membangun spirograph.",
            "vocab": "For Loop, range(n), Rumus Poligon (360 / N), Indentasi Blok, Counter Variable 'i', Spiral Dinamis, Spirograph, Nested Loop.",
            "tech": "<b>Mathematical Iteration:</b> Untuk poligon teratur dengan $N$ sisi, sudut belok luar selalu bernilai $360^\circ / N$. Dengan counter $i$, fungsi <code>forward(i * faktor)</code> menghasilkan garis spiral Archimedes. Pada Nested Loop, loop luar menentukan jumlah kelopak dan loop dalam menggambar bentuk individual.",
            "output": """[ Jendela Kanvas Turtle Seni Geometri ]
- Background: Black
- Pola: Spirograph Bunga 36 Kelopak Persegi
  * Loop Luar: 36 kali rotasi (belok 10 derajat)
  * Loop Dalam: 4 sisi persegi panjang 100 piksel
  * Palet Warna: Rotasi 6 warna pelangi secara dinamis""",
            "err": "<b>IndentationError / Bentuk Tidak Berputar:</b> Siswa meletakkan perintah putar sudut di dalam loop terdalam sehingga kura-kura hanya berputar di tempat.",
            "diff": "<b>Min:</b> Menggambar poligon segi-6 (Hexagon) menggunakan For Loop dan rumus 360/6.<br><b>Bonus:</b> Spirograph Mandala bertingkat dengan variasi warna RGB pada setiap kelopak."
        },
        {
            "num": 8,
            "title": "Advanced Nested Loops & Grid 2D",
            "unit": "Unit 2: Logic & Automation",
            "obj": "Memetakan petak koordinat baris dan kolom 2D, mentransformasikan (row, col) ke koordinat piksel layar, menerapkan pola papan catur, dan membaca data matrix.",
            "vocab": "Grid System, Row (Baris), Col (Kolom), Matrix 2D, Modulo Genap-Ganjil (row + col) % 2, Pixel Art, Retro Game Sprite.",
            "tech": "<b>2D Grid Coordinate Mapping:</b> Komputer memetakan sel baris $r$ dan kolom $c$ menjadi koordinat kanvas melalui transformasi linier: $x = c \\times size - offset_x$ dan $y = offset_y - (r \\times size)$. Matriks 2D berupa list of lists diakses dengan sintaks <code>grid[row][col]</code>.",
            "output": """[ Jendela Kanvas Turtle Grid ]
- Background: Dark Gray
- Pola: Papan Catur 4x4
  * Petak Genap  : Hitam
  * Petak Ganjil : Abu-abu Terang
- Ukuran Sel: 40x40 piksel via t.stamp() instan""",
            "err": "<b>IndexError pada Matriks 2D:</b> Siswa menukar urutan indeks <code>matrix[col][row]</code>. Ingat prinsip matriks: Baris dulu, baru Kolom.",
            "diff": "<b>Min:</b> Membangun grid 3x3 selang-seling warna menggunakan nested loop.<br><b>Bonus:</b> Merancang Matrix 4x4 Wajah Creeper Minecraft dan mencetaknya menjadi Pixel Art."
        },
        {
            "num": 9,
            "title": "Capstone Project: Brainstorming & Planning",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Memilih 1 dari 3 jalur proyek akhir, menyusun Game Design Document (GDD), menggambar Flowchart logika alur, dan menuliskan Pseudocode program.",
            "vocab": "Software Development Life Cycle (SDLC), Ideation, Planning, GDD (Game Design Document), Flowchart, Pseudocode, Core MVP, Bonus Feature.",
            "tech": "<b>Engineering Blueprinting:</b> Tahap perancangan mencegah kegagalan teknis (logic deadlock). Siswa membedah program menjadi 3 komponen: Data Model (List/Dict apa yang dibutuhkan), Process Logic (Rumus & if-else yang berjalan), dan Storage (File teks apa yang dicatat).",
            "output": """=== PROPOSAL CAPSTONE LEVEL 2 ===
Nama Siswa   : Alex
Jalur Proyek : Track B - Text RPG Dungeon
Nama Game    : 'Escape from Modula Cave'
Fitur MVP    : 1. Status Player (Dict) | 2. Battle System (If-Else) | 3. Highscore (.txt)
Status Guru  : APPROVED ✅ (Siap Masuk Coding Sesi 10)""",
            "err": "<b>Scope Creep (Fitur Terlalu Rumit):</b> Siswa ingin membuat game multiplayer online di Level 2. Guru mengarahkan kembali ke 3 fitur Core MVP yang realistis selesai dalam 2 sesi.",
            "diff": "<b>Semua Siswa:</b> Menyelesaikan GDD 6 poin, Flowchart alur utama, dan Pseudocode sebelum membuka IDE."
        },
        {
            "num": 10,
            "title": "Capstone Project: Coding Phase 1 (Core)",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Mengimplementasikan struktur data utama (List / Dictionary), membangun loop program utama, dan memastikan mekanik dasar berfungsi (Functional First).",
            "vocab": "Functional First, Core Mechanics, Main Game Loop, Input Sanitization, Test Cases, Modular Functions.",
            "tech": "<b>Iterative Prototyping:</b> Siswa dilarang mempercantik tampilan sebelum logika intinya berjalan lancar. Fokus sesi ini adalah mengamankan input user, manipulasi dictionary data, dan pengujian alur percabangan utama tanpa crash.",
            "output": """=== CODING PHASE 1 CHECKLIST ===
[x] Struktur data Dictionary / List terdefinisi
[x] Loop menu utama berjalan lancar
[x] Input user berhasil diproses tanpa error
[ ] Penyimpanan file .txt (Dijadwalkan Sesi 11)
[ ] Dekorasi tampilan akhir (Dijadwalkan Sesi 11)""",
            "err": "<b>Infinite Loop pada Menu Utama:</b> Siswa lupa memberikan opsi 'Exit' yang mengubah flag kondisi while loop menjadi False.",
            "diff": "<b>Min:</b> 3 Fitur Core MVP dapat dijalankan dan diuji langsung di terminal / turtle.<br><b>Bonus:</b> Menambahkan menu bantuan (Help) dan validasi input yang sangat ketat."
        },
        {
            "num": 11,
            "title": "Capstone Project: Coding Phase 2 (Polesan & Debug)",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Menyelesaikan fitur penyimpanan file permanen (.txt), membasmi seluruh bug yang tersisa, mempercantik antarmuka program, dan gladi resik presentasi.",
            "vocab": "Debugging, Persistence Integration, File I/O Append, Edge Case Handling, Polish & Aesthetics, Rehearsal.",
            "tech": "<b>Defensive Programming:</b> Integrasi penyimpanan berkas eksternal dengan <code>with open()</code>. Memastikan semua kasus batas (edge cases: input kosong, angka negatif, huruf tak dikenal) ditangani dengan pesan ramah pengguna.",
            "output": """=== FINAL TESTING VERIFICATION ===
Test Case 1: Input valid   -> SUKSES ✅
Test Case 2: Input kosong  -> Pesan ramah muncul ✅
Test Case 3: Save file     -> Data tercatat di highscore.txt ✅
Bug Terdeteksi: 1 (IndexError saat inventory kosong - SUDAH DIPERBAIKI)
Status: SIAP SHOWCASE SESI 12 🏆""",
            "err": "<b>File Korup / Tertimpa:</b> Siswa keliru menggunakan mode 'w' bukannya mode 'a' saat mencatat riwayat transaksi/skor. Guru mereview kembali perbedaan mode.",
            "diff": "<b>Min:</b> Seluruh alur program bebas dari error crash dan data tersimpan ke file.<br><b>Bonus:</b> Menambahkan fitur rahasia (Easter Egg) atau variasi warna visual Turtle."
        },
        {
            "num": 12,
            "title": "The Grand Showcase & Portofolio Day",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Mempresentasikan pitch 3 menit, mendemonstrasikan program di depan kelas, menjelaskan 1 bug tersulit yang berhasil diatasi, dan refleksi kelulusan.",
            "vocab": "Developer Pitch, Live Demo, Peer Review, Rubrik Penilaian Adil, Portofolio Digital, Sertifikat Kelulusan.",
            "tech": "<b>Rubrik Penilaian 4 Pilar:</b> Penilaian kelulusan didasarkan secara setara pada: Struktur Data & Logika (35%), Fungsionalitas & Bebas Bug (25%), Kreativitas Personal (20%), dan Kejelasan Pitching & Jawaban Tanya Jawab (20%).",
            "output": """=== THE GRAND SHOWCASE STAGE ===
1. Perkenalan & Masalah yang Diselesaikan (30 Detik)
2. Live Demo Aplikasi & Fitur Utama (60 Detik)
3. Bedah Bug & Cara Mengatasinya (45 Detik)
4. Rencana Fitur Versi Selanjutnya (45 Detik)
Hasil Evaluasi: LULUS DENGAN PREDIKAT MASTER CADET ⭐""",
            "err": "<b>Gugup di Panggung Presentasi:</b> Guru memandu siswa dengan lembar contekan urutan presentasi 4 poin.",
            "diff": "<b>Semua Siswa:</b> Melakukan demo langsung, menjawab pertanyaan pelatih, dan menerima sertifikat resmi Level 2!"
        }
    ]

    # Generate Page 4 to Page 15 (1 meeting per page)
    current_page = 4
    for m in meetings_data:
        diff_parts = m['diff'].split('<br>')
        min_diff = diff_parts[0]
        bonus_diff = diff_parts[1] if len(diff_parts) > 1 else min_diff

        html += f"""
        <div class="page">
            {page_header(f"Sesi {m['num']}: {m['title']}")}
            <div class="page-body">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2mm;">
                    <span class="badge">Sesi {m['num']} • {m['unit']}</span>
                    <span class="badge badge-yellow">Alokasi: 30% Teori / 60% Hands-on / 10% Penutup</span>
                </div>
                <h2>Misi {m['num']}: {m['title']}</h2>
                
                <p><b>🎯 Observable Learning Objectives:</b><br>{m['obj']}</p>

                <h3>1. Key Vocabulary & Istilah Teknis</h3>
                <p style="font-size: 8pt; color: var(--ink);"><b>Istilah Kunci:</b> {m['vocab']}</p>

                <h3>2. Technical Brief & Arsitektur Kode</h3>
                <div style="font-size: 8pt; color: var(--ink); line-height: 1.35;">{m['tech']}</div>

                <h3>3. Expected Program Output</h3>
                <div class="terminal-box"><pre style="margin: 0; font-family: inherit;">{m['output']}</pre></div>

                <h3>4. Common Misconceptions & Diagnostik Error Guru</h3>
                <div class="callout callout-warn" style="font-size: 8pt;">{m['err']}</div>

                <h3>5. Diferensiasi & Target Keberhasilan Kelas</h3>
                <table style="margin-top: 1mm;">
                    <tr>
                        <td style="width: 50%;"><b>Target Minimum (Core Goal):</b><br>{min_diff}</td>
                        <td style="width: 50%;"><b>Tantangan Ekstensi (Bonus Challenge):</b><br>{bonus_diff}</td>
                    </tr>
                </table>
            </div>
            {page_footer(current_page, 15)}
        </div>
        """
        current_page += 1

    # Close document
    html += """
    </div>
</body>
</html>
"""
    return html

content = build_lesson_plan()
with open("lesson_plan_level2.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated level2/lesson_plan_level2.html successfully with size: {len(content)} bytes.")
