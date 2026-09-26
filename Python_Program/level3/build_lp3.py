# -*- coding: utf-8 -*-
"""Generate official Lesson Plan HTML for Level 3 (Planet Archius - GUI with CustomTkinter)"""

import sys

def build_lesson_plan():
    # Load CSS and template parts from template or level4
    html = """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Official Lesson Plan Kalananti B2C Python Level 3 — Planet Archius, GUI Application Development">
    <title>Lesson Plan Python Level 3 — Planet Archius</title>
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
            height: 3.5mm;
            display: flex;
            margin-top: 1mm;
        }

        .footer-stripes .st-blue { flex: 7; background: var(--blue); }
        .footer-stripes .st-yellow { flex: 2; background: var(--yellow); }
        .footer-stripes .st-teal { flex: 1; background: var(--teal); }

        /* Typography & Components */
        h1, h2, h3, h4 { color: var(--blue-dark); margin: 0; font-weight: 700; }
        h1 { font-size: 16pt; line-height: 1.2; }
        h2 { font-size: 12pt; border-bottom: 2px solid var(--blue-light); padding-bottom: 1mm; margin-bottom: 2mm; }
        h3 { font-size: 10pt; color: var(--blue); margin-top: 2mm; margin-bottom: 1mm; }

        .badge {
            display: inline-block;
            font-size: 7pt;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 1mm 2.5mm;
            border-radius: 3px;
            background: var(--blue-pale);
            color: var(--blue-dark);
            border: 1px solid var(--blue-light);
        }

        .badge-yellow { background: var(--yellow-pale); color: #854d0e; border-color: #fde047; }
        .badge-green { background: #ecfdf5; color: #065f46; border-color: #a7f3d0; }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 8pt;
            margin: 2mm 0 3mm;
        }

        th, td {
            padding: 1.8mm 2.5mm;
            border: 1px solid var(--line);
            text-align: left;
            vertical-align: top;
        }

        th { background: var(--blue-pale); color: var(--blue-dark); font-weight: 700; }
        tr:nth-child(even) td { background: #f8fafc; }

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

        .wireframe-box {
            background: #1e1e1e;
            color: #e2e8f0;
            font-family: monospace;
            font-size: 7.5pt;
            padding: 3mm 4mm;
            border-radius: 6px;
            border: 1px solid #334155;
            margin: 2mm 0;
            line-height: 1.3;
        }

        .code-box {
            background: #0f172a;
            color: #38bdf8;
            font-family: "Consolas", "Courier New", monospace;
            font-size: 7.5pt;
            padding: 2.5mm 3.5mm;
            border-radius: 4px;
            border-left: 3px solid var(--teal);
            margin: 2mm 0;
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
                <span>Kalananti B2C Python — Level 3: Planet Archius (GUI Development)</span>
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
            <div class="cover-subtitle">Python Level 3 — GUI Application Development</div>
            <div class="cover-planet">🪐 PLANET ARCHIUS</div>

            <div style="max-width: 140mm; margin: 15mm auto 0; text-align: left; font-size: 8.5pt; background: rgba(255,255,255,0.85); padding: 5mm 8mm; border-radius: 8px; border: 1px solid var(--blue-light);">
                <p><b>Target Siswa:</b> Usia 10–15 Tahun (SMP / Intermediate Beginner)</p>
                <p><b>Durasi Sesi:</b> 60–90 Menit per Pertemuan (Proporsi: 30% Konsep, 60% Hands-on, 10% Penutup)</p>
                <p><b>Kurikulum Acuan:</b> Silabus Resmi B2C Kalananti (SSOT1 B2C_Python Tab)</p>
                <p><b>Teknologi Utama:</b> Python 3.10+, Tkinter, CustomTkinter (Modern GUI Framework)</p>
                <p><b>Arsitektur Proyek:</b> 3 Core Tracks (Unit Converter, Login System, To-Do Lite) + Optional Advanced Track (Weather App & API)</p>
            </div>

            <div class="cover-meta">
                <p><b>Kalananti Academic & Curriculum Development Team</b></p>
                <p>Dokumen Pegangan Pengajar — Dilengkapi Panduan Visual, Hierarki Widget, dan Diagnostik Error</p>
            </div>
            {page_footer(1)}
        </div>
    """

    # --- PAGE 2: PROGRAM OVERVIEW & LEARNING JOURNEY ---
    html += f"""
        <div class="page">
            {page_header("Overview")}
            <div class="page-body">
                <h2>1. Program Overview & Learning Journey</h2>
                <p>Level 3 merupakan jembatan emas bagi siswa dari pemrograman berbasis terminal hitam-putih (CLI) menuju <b>pengembangan perangkat lunak nyata berantarmuka grafis (GUI)</b>. Siswa belajar bahwa tombol, kotak input, dan jendela aplikasi dibangun dengan kode terstruktur dan pola <i>Event-Driven Programming</i>.</p>
                
                <div class="callout callout-success">
                    <b>🎯 End-of-Level Mastery Outcome:</b><br>
                    Siswa mampu mendekomposisi kebutuhan aplikasi ke dalam layout antarmuka (Grid/Pack), membangun jendela CustomTkinter modern, memproses input pengguna secara aman dengan <code>try-except</code>, dan mempresentasikan karya aplikasinya secara percaya diri.
                </div>

                <h3>Tabel Perjalanan 12 Pertemuan (Syllabus SSOT1)</h3>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 10%;">Sesi</th>
                            <th style="width: 25%;">Topik & Modul</th>
                            <th style="width: 45%;">Tujuan Pembelajaran & Penguasaan</th>
                            <th style="width: 20%;">Artefak / Output</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Misi 1</b></td>
                            <td>Intro to CustomTkinter</td>
                            <td>Membuat jendela utama (Root Window), title, geometry, dark/light mode</td>
                            <td>Window Dasar</td>
                        </tr>
                        <tr>
                            <td><b>Misi 2</b></td>
                            <td>Labels & Buttons</td>
                            <td>Menampilkan teks (Label) dan tombol membulat dengan event klik</td>
                            <td>Kartu Profil Interaktif</td>
                        </tr>
                        <tr>
                            <td><b>Misi 3</b></td>
                            <td>Entry Widgets (Input)</td>
                            <td>Menerima data teks pengguna via <code>CTkEntry</code> dan method <code>.get()</code></td>
                            <td>Form Biodata</td>
                        </tr>
                        <tr>
                            <td><b>Misi 4</b></td>
                            <td>Layout Management</td>
                            <td>Menata posisi dengan sistem matriks baris-kolom (<code>.grid()</code>) & <code>.pack()</code></td>
                            <td>Formulir Grid 2x2</td>
                        </tr>
                        <tr>
                            <td><b>Misi 5</b></td>
                            <td>Event Handling</td>
                            <td>Menghubungkan tombol ke fungsi callback dinamis (<code>command=fungsi</code>)</td>
                            <td>Click Counter Game</td>
                        </tr>
                        <tr>
                            <td><b>Misi 6</b></td>
                            <td>Error Handling</td>
                            <td>Mencegah crash aplikasi akibat input salah menggunakan <code>try-except</code></td>
                            <td>Validator Angka</td>
                        </tr>
                        <tr>
                            <td><b>Misi 7</b></td>
                            <td>Image in GUI</td>
                            <td>Menyisipkan ikon dan gambar grafis dengan <code>CTkImage</code></td>
                            <td>Kartu Karakter Bergambar</td>
                        </tr>
                        <tr>
                            <td><b>Misi 8</b></td>
                            <td>Mini Project: Calculator</td>
                            <td>Integrasi tombol matriks angka, rumus matematika, dan display hasil</td>
                            <td>Kalkulator Mini</td>
                        </tr>
                        <tr>
                            <td><b>Misi 9</b></td>
                            <td>Ideasi & Wireframing</td>
                            <td>Memilih 1 dari 3 Track Silabus, menyusun 3 fitur Core MVP, dan sketsa wireframe</td>
                            <td>Proposal & Wireframe</td>
                        </tr>
                        <tr>
                            <td><b>Misi 10</b></td>
                            <td>UI Layouting</td>
                            <td>Implementasi Front-End lengkap: Container Frame, Input, Display, dan Button</td>
                            <td>UI Proyek (Dummy)</td>
                        </tr>
                        <tr>
                            <td><b>Misi 11</b></td>
                            <td>App Logic & Testing</td>
                            <td>Koding fungsi callback, validasi input, 3 skenario testing, optional API mock</td>
                            <td>Aplikasi Fungsional</td>
                        </tr>
                        <tr>
                            <td><b>Misi 12</b></td>
                            <td>The Grand Showcase</td>
                            <td>Presentasi pitch 3 menit, demonstrasi karya, peer review, dan wisuda level</td>
                            <td>Presentasi & Portofolio</td>
                        </tr>
                    </tbody>
                </table>

                <div class="callout callout-warn">
                    <b>⚠️ Model Proyek Akhir SSOT1 (Sesi 9–12):</b><br>
                    Siswa memilih salah satu dari <b>3 Core Tracks</b>: (1) <i>Unit Converter</i>, (2) <i>Login System</i>, atau (3) <i>To-Do List Lite</i>. Proyek <i>Weather App dengan API</i> diposisikan sebagai <b>Optional Advanced Extension</b> dan <b>Teacher Reference</b> (100% opsional, dilengkapi mode offline fallback agar tidak bergantung pada internet/API key).
                </div>
            </div>
            {page_footer(2)}
        </div>
    """

    # --- PAGE 3: TECH SETUP & OFFLINE CONTINGENCY ---
    html += f"""
        <div class="page">
            {page_header("Persiapan Teknis")}
            <div class="page-body">
                <h2>2. Persiapan Teknis & Offline Contingency</h2>
                
                <h3>A. Kebutuhan Perangkat Lunak</h3>
                <ul>
                    <li><b>Python:</b> Versi 3.10 atau lebih baru (Pastikan opsi <i>Add Python to PATH</i> dicentang saat instalasi).</li>
                    <li><b>Editor Kode:</b> Visual Studio Code dengan ekstensi resmi Python (Microsoft).</li>
                    <li><b>Library GUI:</b> <code>customtkinter</code> versi 5.2.0+.</li>
                </ul>

                <div class="code-box">
                    # Perintah Instalasi Library di Terminal (Hanya 1x di awal level):<br>
                    pip install customtkinter<br><br>
                    # Verifikasi Berhasil:<br>
                    python -c "import customtkinter as ctk; print(ctk.__version__)"
                </div>

                <h3>B. Protokol Keamanan & Anti-Crash Offline (Zero Secrets Guardrail)</h3>
                <p>Untuk memastikan proses belajar di kelas berjalan lancar tanpa kendala sinyal internet:</p>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 30%;">Skenario Risiko</th>
                            <th style="width: 35%;">Dampak Jika Terjadi</th>
                            <th style="width: 35%;">Solusi & Protokol Pengajar</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>Internet Sekolah Putus / Lambat</b></td>
                            <td>Aplikasi tidak bisa fetch data eksternal (API)</td>
                            <td>Gunakan <b>MOCK DATA OFFLINE</b> (Dictionary lokal) yang sudah disiapkan. Seluruh Core Mission berjalan 100% offline tanpa internet.</td>
                        </tr>
                        <tr>
                            <td><b>API Key Belum Aktif / Error</b></td>
                            <td>Error HTTP 401 Unauthorized</td>
                            <td>Jangan paksa siswa mendaftar API Key baru saat jam kelas. Arahkan menggunakan data simulasi lokal atau pilih Core Track (Converter/Login/To-Do).</td>
                        </tr>
                        <tr>
                            <td><b>Kebocoran Kredensial</b></td>
                            <td>API Key pribadi disalin orang lain</td>
                            <td><b>Dilarang keras</b> menuliskan API Key pribadi pada slide/repo publik. Semua contoh di slide wajib memakai placeholder <code>"{'{api_key}'}"</code>.</td>
                        </tr>
                    </tbody>
                </table>

                <h3>C. Rumus Manajemen Waktu Kelas (Time Budget Rule)</h3>
                <div class="callout">
                    <b>Proporsi Alokasi Waktu Sesi (Durasi 60–90 Menit):</b><br>
                    • <b>25–30% Waktu (15–25 Menit):</b> Review flashback, pemaparan konsep baru, demonstrasi visual, dan Bug Hunt.<br>
                    • <b>60% Waktu (35–55 Menit):</b> Hands-on koding aktif di VS Code (Guided Practice & Independent Mission).<br>
                    • <b>10–15% Waktu (5–10 Menit):</b> Pengujian mandiri, refleksi pemahaman, dan exit ticket.
                </div>
            </div>
            {page_footer(3)}
        </div>
    """

    # --- FUNCTION FOR MEETING CARDS ---
    meetings_data = [
        {
            "num": 1,
            "title": "Intro to CustomTkinter & Root Window",
            "unit": "Unit 1: UI Foundations",
            "obj": "Membuat jendela utama aplikasi (Root Window), mengatur judul, ukuran (geometry), dan tema warna Dark/Light mode.",
            "vocab": "Root Window (jendela induk), geometry (lebar x tinggi pixel), appearance_mode (tema tampilan), mainloop (siklus hidup aplikasi).",
            "tech": "<b>Event Loop (mainloop()):</b> Jendela GUI tidak langsung menutup seperti script CLI karena berada di dalam infinite loop yang mendengarkan event OS (klik, gerak mouse). `app.mainloop()` wajib diletakkan di baris paling akhir.",
            "wireframe": """+--------------------------------------+
| [O O O]  Archius Command Center   - X|
|--------------------------------------|
|                                      |
|            [ Dark Window ]           |
|                                      |
|    "Selamat Datang di Level 3!"      |
|                                      |
+--------------------------------------+""",
            "err": "<b>Window langsung menutup sendiri:</b> Guru memeriksa apakah baris `app.mainloop()` terlupa atau berada di dalam indentasi yang salah.",
            "diff": "<b>Min:</b> Window 400x400 dengan title.<br><b>Bonus:</b> Coba ganti tema `set_default_color_theme('green')`."
        },
        {
            "num": 2,
            "title": "Labels & Buttons (Komponen Dasar)",
            "unit": "Unit 1: UI Foundations",
            "obj": "Menampilkan teks dengan CTkLabel dan memasang tombol membulat interaktif dengan CTkButton.",
            "vocab": "Widget (komponen UI), corner_radius (kelengkungan sudut), fg_color (warna latar depan), hover_color (warna saat kursor di atas tombol).",
            "tech": "<b>Hierarki Master-Child:</b> Setiap widget membutuhkan argumen pertama `master` (menentukan di wadah mana widget tersebut menempel). Jika lupa di-pack/grid, widget dibuat di memori tetapi tidak tampak di layar.",
            "wireframe": """+--------------------------------------+
| [O O O]  Widget Lab               - X|
|--------------------------------------|
|                                      |
|       [ Label: Halo Dunia! ]         |
|                                      |
|        ( Tombol Membulat )           |
|                                      |
+--------------------------------------+""",
            "err": "<b>Widget tidak muncul:</b> Lupa memanggil `.pack()` setelah membuat objek widget.",
            "diff": "<b>Min:</b> 1 Label + 1 Button.<br><b>Bonus:</b> Buat tombol dengan font kustom dan hover_color unik."
        },
        {
            "num": 3,
            "title": "Entry Widgets (Form Input Pengguna)",
            "unit": "Unit 1: UI Foundations",
            "obj": "Menerima input teks dari pengguna menggunakan CTkEntry dan membaca isinya dengan method .get().",
            "vocab": "Entry (kotak input teks), placeholder_text (teks petunjuk abu-abu), .get() (menarik teks isian), show='*' (sensor sandi).",
            "tech": "<b>Retrival Tipe Data String:</b> Method `.get()` SELALU mengembalikan data bertipe String. Jika nilai input akan dihitung secara matematis, wajib dikonversi dengan `int()` atau `float()`.",
            "wireframe": """+--------------------------------------+
| [O O O]  Entry Portal             - X|
|--------------------------------------|
|   Nama:   [ Ketik nama kamu...     ] |
|   Sandi:  [ ••••••••               ] |
|                                      |
|           [ Kirim Data ]             |
+--------------------------------------+""",
            "err": "<b>TypeError saat hitung:</b> Siswa langsung menjumlahkan `entry.get() + 5` tanpa casting `int()`.",
            "diff": "<b>Min:</b> 1 Kotak input + tombol print ke console.<br><b>Bonus:</b> Kotak password bersensor `show='*'`."
        },
        {
            "num": 4,
            "title": "Layout Management (Pack vs Grid)",
            "unit": "Unit 1: UI Foundations",
            "obj": "Menyusun widget secara teratur menggunakan matriks baris-kolom (.grid()) dan container CTkFrame.",
            "vocab": "Frame (wadah pengelompok), row (baris horizontal), column (kolom vertikal), sticky (penjajaran arah mata angin), padx/pady.",
            "tech": "<b>Larangan Mencampur Manager:</b> Jangan pernah memanggil `.pack()` dan `.grid()` pada wadah master yang sama. Pisahkan menjadi Frame berbeda jika ingin mengombinasikan layout.",
            "wireframe": """+--------------------------------------+
| [O O O]  Grid Form                - X|
|--------------------------------------|
|  [CTkFrame Pembungkus]               |
|  Row 0:  [Label 1]     [Entry 1]     |
|  Row 1:  [Label 2]     [Entry 2]     |
|  Row 2:  [Tombol A]    [Tombol B]    |
+--------------------------------------+""",
            "err": "<b>TclError: cannot use geometry manager:</b> Siswa mencampur pack dan grid di container yang sama.",
            "diff": "<b>Min:</b> Grid 2 baris x 2 kolom.<br><b>Bonus:</b> Form login rapi dengan alignment `sticky='w'`."
        },
        {
            "num": 5,
            "title": "Event Handling & Functions in GUI",
            "unit": "Unit 2: App Logic",
            "obj": "Menghubungkan klik tombol dengan fungsi Python melalui parameter command= dan memperbarui tampilan via .configure().",
            "vocab": "Event (kejadian/klik), Callback (fungsi yang dipanggil sistem saat event terjadi), .configure() (mengubah properti widget saat runtime).",
            "tech": "<b>Aturan Callback Tanpa Kurung:</b> Parameter `command=nama_fungsi` menerima referensi objek fungsi, BUKAN hasil panggilannya. Menulis `command=nama_fungsi()` akan mengeksekusi fungsi di awal dan tombol menjadi mati.",
            "wireframe": """+--------------------------------------+
| [O O O]  Clicker Counter          - X|
|--------------------------------------|
|                                      |
|             Skor:  [ 5 ]             |
|                                      |
|        [ + Tambah Angka ]            |
|                                      |
+--------------------------------------+""",
            "err": "<b>Fungsi jalan otomatis sebelum diklik:</b> Ada tanda kurung `()` pada parameter `command=`.",
            "diff": "<b>Min:</b> Counter bertambah 1 saat tombol diklik.<br><b>Bonus:</b> Tambahkan tombol reset angka 0."
        },
        {
            "num": 6,
            "title": "Error Handling (Try & Except) in GUI",
            "unit": "Unit 2: App Logic",
            "obj": "Melindungi aplikasi dari crash akibat kesalahan input user (huruf di kotak angka/form kosong) dengan try-except.",
            "vocab": "Crash (aplikasi tertutup paksa), Exception (kondisi error saat runtime), ValueError (error ketidakcocokan tipe data), fallback.",
            "tech": "<b>Robustness Standard:</b> Aplikasi profesional tidak boleh crash di depan pengguna. Blok `try:` mencoba konversi `float()`, dan `except ValueError:` menangkap kegagalan untuk menampilkan pesan peringatan ramah.",
            "wireframe": """+--------------------------------------+
| [O O O]  Input Validator          - X|
|--------------------------------------|
|  Masukkan Umur: [ abc ]              |
|  [ Cek Kelayakan ]                   |
|                                      |
|  ⚠️ Harap masukkan angka bulat valid!|
+--------------------------------------+""",
            "err": "<b>Except terlalu luas:</b> Menulis `except:` tanpa tipe error spesifik menyembunyikan bug typo syntax.",
            "diff": "<b>Min:</b> Validasi angka dengan try-except.<br><b>Bonus:</b> Warna label berubah merah jika error."
        },
        {
            "num": 7,
            "title": "Images & Assets Integration in GUI",
            "unit": "Unit 2: App Logic",
            "obj": "Memasukkan gambar atau ikon grafis ke dalam tombol dan label menggunakan CTkImage.",
            "vocab": "Asset (berkas gambar/suara pendukung), CTkImage (pembungkus gambar CustomTkinter), size (dimensi lebar x tinggi).",
            "tech": "<b>Pillow Integration:</b> CustomTkinter menggunakan Pillow (`PIL.Image`) di latar belakang untuk me-render gambar dengan DPI scaling yang tajam di layar Retina/High-DPI.",
            "wireframe": """+--------------------------------------+
| [O O O]  Card Profile             - X|
|--------------------------------------|
|           [ 🖼️ Foto/Ikon ]           |
|                                      |
|            Captain Budi              |
|        Rank: Lead Architect          |
+--------------------------------------+""",
            "err": "<b>FileNotFoundError:</b> Berkas gambar tidak berada di folder yang sama dengan script Python.",
            "diff": "<b>Min:</b> 1 Gambar berhasil tampil di label.<br><b>Bonus:</b> Tombol bergambar dengan teks di sampingnya."
        },
        {
            "num": 8,
            "title": "Mini Project: Scientific Calculator",
            "unit": "Unit 2: App Logic",
            "obj": "Membangun kalkulator visual lengkap: display angka, keypad tombol grid 4x4, dan kalkulasi matematika.",
            "vocab": "Display Frame, Keypad Matrix, String Concatenation, State Accumulator.",
            "tech": "<b>Pola Akumulasi Input:</b> Angka yang diklik user digabungkan sebagai string (misal `'1' + '5' = '15'`). Saat operator ditekan, ekspresi dihitung dan hasilnya dikonfigurasi ke layar display.",
            "wireframe": """+--------------------------------------+
| [O O O]  Archius Calculator       - X|
|--------------------------------------|
|  [ Display: 125                     ]|
|  ----------------------------------- |
|  [ 7 ]  [ 8 ]  [ 9 ]  [ / ]          |
|  [ 4 ]  [ 5 ]  [ 6 ]  [ * ]          |
|  [ 1 ]  [ 2 ]  [ 3 ]  [ - ]          |
|  [ C ]  [ 0 ]  [ = ]  [ + ]          |
+--------------------------------------+""",
            "err": "<b>Syntax error saat hitung:</b> Operasi dua simbol berdampingan (misal `5++3`).",
            "diff": "<b>Min:</b> Tombol tambah dan kurang berfungsi.<br><b>Bonus:</b> Keypad 16 tombol lengkap + clear."
        },
        {
            "num": 9,
            "title": "Final Project Ideation & Wireframing",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Memilih 1 dari 3 Core Track Silabus, merancang sketsa wireframe 3 zona, dan menetapkan 3 fitur Core MVP.",
            "vocab": "Wireframe (sketsa blueprint visual), Core MVP (3 fungsi minimum wajib), Scope Creep (kelebihan beban rencana yang tidak realistis).",
            "tech": "<b>Scaffolding Pedagogis:</b> Siswa memilih salah satu dari 3 Track resmi: (1) Unit Converter, (2) Login System, (3) To-Do List Lite. Track Weather App menjadi pilihan tantangan lanjutan. Proposal wajib di-ACC guru sebelum koding.",
            "wireframe": """+--------------------------------------+
| [O O O]  PILIHAN TRACK SISWA      - X|
|--------------------------------------|
|  [Track 1: Unit Converter          ] |
|  [Track 2: Login & Security Vault  ] |
|  [Track 3: To-Do List Lite        ] |
|  *(Opsional: Live Weather App)       |
+--------------------------------------+""",
            "err": "<b>Scope terlalu besar:</b> Siswa ingin membuat game RPG raksasa di Tkinter. Guru mengarahkan kembali ke Core MVP 3 fitur.",
            "diff": "<b>Min:</b> Sketsa kertas 3 zona + 3 MVP.<br><b>Bonus:</b> Memilih 2 fitur Creative Sandbox."
        },
        {
            "num": 10,
            "title": "Final Project: Front-End UI Layouting",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Menerjemahkan wireframe menjadi antarmuka visual CustomTkinter lengkap: Frame container, Input, Display, dan Tombol dummy.",
            "vocab": "Front-End Blueprint, UI Container, Dummy Button, Visual Hierarchy, Padding Polish.",
            "tech": "<b>Isolasi Pekerjaan Visual:</b> Di Sesi 10 siswa dilarang memikirkan logika rumus. Fokus 100% pada tampilan agar rapi, tidak bertubrukan, dan memenuhi wireframe.",
            "wireframe": """+--------------------------------------+
| [O O O]  Aplikasi Karya Siswa     - X|
|--------------------------------------|
|  [Header]: Judul & Ikon              |
|  [Form Input]: Entry / Option Menu   |
|  [Action]: Tombol (Masih Dummy)      |
|  [Display]: Wadah Hasil Siap Pakai   |
+--------------------------------------+""",
            "err": "<b>Layout bergeser saat di-resize:</b> Ukuran geometry terlalu sempit untuk menampung widget.",
            "diff": "<b>Min:</b> Seluruh widget wireframe terpasang rapi.<br><b>Bonus:</b> Palet warna harmonis dan custom fonts."
        },
        {
            "num": 11,
            "title": "Final Project: App Logic & Testing Clinic",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Menghubungkan tombol ke logika fungsi (Input -> Process -> Output), proteksi error, dan 3 pengujian testing.",
            "vocab": "App Logic, Input Sanitation (.strip()), 3 Test Cases (Happy Path, Empty, Edge Case), Mock Fallback.",
            "tech": "<b>Robust Event Handling:</b> Setiap track mengimplementasikan alur: `teks = entry.get() -> proses -> label.configure()`. Siswa jalur Weather dilengkapi data simulasi offline agar 100% anti-crash.",
            "wireframe": """+--------------------------------------+
| [O O O]  Aplikasi Siap Diuji      - X|
|--------------------------------------|
|  Input:   [ 100 ]                    |
|  Aksi:    [ Konversi Sekarang ⚡ ]   |
|  Hasil:   212.0 °F (Berhasil!)       |
|  Status:  ✅ Lolos 3 Test Cases      |
+--------------------------------------+""",
            "err": "<b>Crash saat input kosong:</b> Siswa lupa memberi validasi `if not data:` di awal fungsi callback.",
            "diff": "<b>Min:</b> 3 Fitur Core MVP jalan sempurna.<br><b>Bonus:</b> Fitur Creative Sandbox (Reset / Dynamic Color)."
        },
        {
            "num": 12,
            "title": "The Grand Showcase & Portofolio Day",
            "unit": "Unit 3: Final Project Phase",
            "obj": "Mempresentasikan pitch 3 menit, mendemonstrasikan fitur aplikasi, menjawab tanya jawab, dan refleksi kelulusan.",
            "vocab": "Developer Pitch (presentasi produk), Peer Review, Rubrik Adil, Portofolio Digital, PyInstaller (.exe).",
            "tech": "<b>Standarisasi Rubrik Setara:</b> Penilaian tidak didasarkan pada ada/tidaknya API, melainkan 4 pilar: UI Layout (25%), Core Logic (35%), Kreativitas Personal (20%), dan Kejelasan Presentasi (20%).",
            "wireframe": """+--------------------------------------+
| [O O O]  GRAND SHOWCASE STAGE     - X|
|--------------------------------------|
|  1. Masalah & Solusi (30 Detik)      |
|  2. Live Demo Aplikasi (60 Detik)    |
|  3. Bug & Cara Mengatasinya (45 Dtk) |
|  4. Rencana Fitur Masa Depan (45 Dtk)|
+--------------------------------------+""",
            "err": "<b>Gugup di panggung:</b> Guru membimbing siswa dengan checklist 4 poin di layar.",
            "diff": "<b>Min:</b> Demo live 3 menit & jawab 1 pertanyaan teknis.<br><b>Bonus:</b> Bundle file .exe mandiri dengan PyInstaller & export GitHub portofolio."
        }
    ]

    # Generate Page 4 to Page 15 (1 meeting per page)
    current_page = 4
    for m in meetings_data:
        html += f"""
        <div class="page">
            {page_header(f"Sesi {m['num']}: {m['title']}")}
            <div class="page-body">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2mm;">
                    <span class="badge">Sesi {m['num']} • {m['unit']}</span>
                    <span class="badge badge-yellow">Assumed: 60–90 Menit (30% Teori / 60% Hands-on / 10% Penutup)</span>
                </div>
                <h2>Misi {m['num']}: {m['title']}</h2>
                
                <p><b>🎯 Observable Learning Objectives:</b><br>{m['obj']}</p>

                <h3>1. Key Vocabulary & Istilah Teknis</h3>
                <p style="font-size: 8pt; color: var(--ink);"><b>Istilah Kunci:</b> {m['vocab']}</p>

                <h3>2. Technical Brief & Arsitektur Kode</h3>
                <div style="font-size: 8pt; color: var(--ink); line-height: 1.35;">{m['tech']}</div>

                <h3>3. Wireframe & Expected GUI Output</h3>
                <div class="wireframe-box">{m['wireframe']}</div>

                <h3>4. Common Misconceptions & Diagnostik Error Guru</h3>
                <div class="callout callout-warn" style="font-size: 8pt;">{m['err']}</div>

                <h3>5. Diferensiasi & Target Keberhasilan Kelas</h3>
                <table style="margin-top: 1mm;">
                    <tr>
                        <td style="width: 50%;"><b>Target Minimum (Core Goal):</b><br>{m['diff'].split('<br>')[0]}</td>
                        <td style="width: 50%;"><b>Tantangan Ekstensi (Bonus Challenge):</b><br>{m['diff'].split('<br>')[1]}</td>
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
with open("lesson_plan_level3.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated level3/lesson_plan_level3.html successfully with size: {len(content)} bytes.")
