# -*- coding: utf-8 -*-
"""Streamlined Meetings 4 and 5 for Level 2"""

def get_m4_slides():
    return [
        {
            "title": "Meeting 4: File Handling Dasar 💾",
            "subtitle": "Menyimpan & Membaca Data Permanen di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">📁</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 4</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Menyelamatkan Data dari Amnesia Komputer!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Selama ini, setiap kali script Python ditutup atau komputer dimatikan, semua variabel (List, Dict, Angka) lenyap seketika dari RAM. Hari ini kita akan belajar <b>File Handling</b>: menulis dan membaca file <code>.txt</code> agar datamu tersimpan abadi di Harddisk!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai Mode <b>'r'</b>, <b>'w'</b>, <b>'a'</b>, dan sintaks sakti anti-bocor <code>with open()</code>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 4 🎯",
            "subtitle": "Target Penguasaan File I/O Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Memori Sementara (RAM) vs Memori Abadi (Harddisk)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami mengapa program butuh menulis data ke media penyimpanan fisik.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Tiga Mode Hak Akses Utama ('r', 'w', 'a')</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Membedakan mode Baca (Read), Tulis Timpa (Write), dan Tulis Tambah (Append).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">SOP Aman: Konstruksi 'with open()' Context Manager</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mencegah kebocoran memori (memory leak) dan file korup dengan penutupan file otomatis.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Sistem Buku Tamu & Game Highscore Saver</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mencatat aktivitas user dan menyimpan rekor skor game ke file teks.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 3 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Manipulasi Teks",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak output kode String berikut sebelum mulai:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. .strip() & .upper()</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">"  halo  ".strip().upper()</div>
            <p class="text-slate-500">Output: <code>"HALO"</code> (Bersih spasi lalu kapital).</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. .split() Menjadi List</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">"a-b-c".split("-")</div>
            <p class="text-slate-500">Output: <code>['a', 'b', 'c']</code> (Dipotong tanda strip).</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. .replace() Tukar Teks</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">"kucing".replace("c", "k")</div>
            <p class="text-slate-500">Output: <code>"kukin"</code> (Mengganti huruf 'c').</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "RAM (Sementara) vs Harddisk (Abadi) ⚡",
            "subtitle": "Mengapa Data di Variabel Biasa Bisa Hilang?",
            "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🧠</span>
            <b class="text-red-800 dark:text-red-300 text-sm">RAM: Memori Super Cepat tapi 'Amnesia'</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-red-400">
            skor = 9999<br>
            # Jika program di-stop atau laptop mati,<br>
            # nilai variabel skor LENYAP selamanya!
        </div>
        <p class="text-xs text-slate-500">RAM butuh aliran listrik untuk mengingat data. Listrik mati = data hilang.</p>
    </div>
    <div class="p-5 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">💽</span>
            <b class="text-green-800 dark:text-green-300 text-sm">Harddisk: Memori Permanen & Tersimpan</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-green-400">
            with open("skor.txt", "w") as f:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;f.write("9999")<br>
            # Besok dibuka lagi, skor masih utuh di file!
        </div>
        <p class="text-xs text-slate-500">Disimpan dalam bentuk file fisik di media penyimpanan komputer.</p>
    </div>
</div>"""
        },
        {
            "title": "Tiga Mode Hak Akses File: 'r', 'w', 'a' 🚦",
            "subtitle": "Pilih Kacamata Akses yang Tepat!",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="grid grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-700 dark:text-blue-300 text-sm block">1. Mode 'r' (Read) 👓</b>
            <p class="text-slate-600 dark:text-slate-400">Hanya membaca isi file. Jika file belum ada, Python akan <b>ERROR (FileNotFoundError)</b>.</p>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">open("data.txt", "r")</div>
        </div>
        <div class="p-4 rounded-xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 space-y-2">
            <b class="text-red-700 dark:text-red-300 text-sm block">2. Mode 'w' (Write) ⚠️</b>
            <p class="text-slate-600 dark:text-slate-400">Menulis baru. <b>Hati-hati!</b> Jika file sudah ada, isinya akan <b>DIHAPUS BERSIH</b> lalu ditimpa!</p>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">open("data.txt", "w")</div>
        </div>
        <div class="p-4 rounded-xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 space-y-2">
            <b class="text-green-700 dark:text-green-300 text-sm block">3. Mode 'a' (Append) ➕</b>
            <p class="text-slate-600 dark:text-slate-400">Mode aman! Menambahkan data baru di baris paling bawah tanpa menghapus data lama.</p>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">open("data.txt", "a")</div>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Membaca File: .read() vs .readlines() 📖",
            "subtitle": "Menyedot Semua Teks vs Menjadikannya List Baris",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. .read() -> Satu Teks Utuh</b>
            <div class="text-slate-400">with open("cerita.txt", "r") as f:</div>
            <div class="text-yellow-400 pl-4">isi = f.read()</div>
            <div class="text-green-400">print(isi) # Semua paragraf dicetak</div>
            <p class="text-slate-400 text-[11px] mt-2">Cocok untuk membaca artikel atau naskah utuh.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. .readlines() -> List Baris</b>
            <div class="text-slate-400">with open("daftar.txt", "r") as f:</div>
            <div class="text-yellow-400 pl-4">baris = f.readlines()</div>
            <div class="text-green-400">print(baris[0]) # Baris pertama!</div>
            <p class="text-slate-400 text-[11px] mt-2">Cocok jika ingin memproses data per baris dengan for loop.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Senjata Rahasia: Sintaks with open() 🛡️",
            "subtitle": "Cara Modern Python Menutup File Otomatis",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-xs leading-relaxed border border-slate-700 shadow-xl">
        <span class="text-slate-400"># Standar Industri Python:</span><br>
        <span class="text-purple-400">with</span> <span class="text-yellow-400">open</span>(<span class="text-green-400">"biodata.txt"</span>, <span class="text-green-400">"w"</span>) <span class="text-purple-400">as</span> <span class="text-cyan-400">file</span>:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">file</span>.<span class="text-yellow-400">write</span>(<span class="text-green-400">"Nama: Archius\\n"</span>)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">file</span>.<span class="text-yellow-400">write</span>(<span class="text-green-400">"Planet: Modula\\n"</span>)<br><br>
        <span class="text-slate-400"># Begitu indentasi selesai, file OTOMATIS tertutup rapat & aman!</span>
    </div>
    <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 text-xs">
        💡 <b>Kenapa tidak pakai file.close() biasa?</b> Jika program error di tengah jalan saat file terbuka, memori komputer bisa bocor (memory leak). Dengan <code>with open()</code>, file dijamin 100% selalu tertutup apa pun yang terjadi!
    </div>
</div>"""
        },
        {
            "title": "Rahasia Baris Baru: Karakter \\n ↵",
            "subtitle": "Jangan Lupa Tekan Enter di Dalam File Teks!",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">❌ Tanpa \\n (Menumpuk Rapat):</b>
            <div class="bg-black/30 p-2.5 rounded font-mono text-red-400">
                f.write("Baris 1")<br>
                f.write("Baris 2")<br>
                # Hasil di file: "Baris 1Baris 2"
            </div>
            <p class="text-slate-500">Method <code>.write()</code> tidak otomatis memberi spasi atau enter!</p>
        </div>
        <div class="p-4 rounded-2xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-green-700 dark:text-green-400 text-sm">✅ Dengan \\n (Rapi Berbaris):</b>
            <div class="bg-black/30 p-2.5 rounded font-mono text-green-400">
                f.write("Baris 1\\n")<br>
                f.write("Baris 2\\n")<br>
                # Hasil di file:<br>
                # Baris 1<br># Baris 2
            </div>
            <p class="text-slate-500">Gunakan <code>\\n</code> setiap kali ingin membuat baris baru.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Buku Tamu Digital (Log) 👨‍🏫",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Aplikasi Buku Tamu Cyber</span><br>
        nama = input("Masukkan nama pengunjung: ")<br>
        pesan = input("Tulis pesan singkat: ")<br><br>
        <span class="text-slate-500"># Gunakan mode 'a' agar pengunjung lama tidak terhapus!</span><br>
        with open("buku_tamu.txt", "a") as f:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;f.write(f"{nama}: {pesan}\\n")<br><br>
        print("Data berhasil disimpan ke buku_tamu.txt! ✅")
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        🔍 <b>Cek File:</b> Buka tab file di VS Code atau folder komputermu, cari file <code>buku_tamu.txt</code> dan lihat isinya bertambah setiap kali kamu menjalankan program!
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Mengatasi Error File I/O 🐛",
            "subtitle": "Dua Kesalahan Paling Sering Terjadi di Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug 1: FileNotFoundError</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                open("rahasia.txt", "r")<br>
                # FileNotFoundError: No such file
            </div>
            <p class="text-slate-500">Membaca file dengan mode <code>'r'</code> padahal filenya belum pernah dibuat.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-amber-700 dark:text-amber-400 text-sm">🐛 Bug 2: Data Terhapus Bersih</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-400">
                open("nilai.txt", "w") # OOPS!
            </div>
            <p class="text-slate-500">Salah memilih mode <code>'w'</code> saat berniat menambah data. Seharusnya gunakan mode <code>'a'</code> (append).</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Baca File Misteri) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Pembaca Pesan Tersembunyi</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Buatlah file teks manual bernama <code>pesan.txt</code> berisi 3 baris teka-teki rahasia.
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Buat program Python yang membuka <code>pesan.txt</code> dengan mode <code>'r'</code>.</li>
            <li>Gunakan <code>.readlines()</code> untuk mendapatkan daftar barisnya.</li>
            <li>Cetak baris demi baris menggunakan looping <code>for nomor, baris in enumerate(daftar):</code>!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ CHALLENGE MODE: Ujian Akhir File System ⚠️",
            "subtitle": "Pilih 1 dari 3 Tantangan Kode Nyata Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🏆</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Uji Nyali Pengendali Berkas!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700">
            <span class="text-xl">🎮</span>
            <b class="block mt-1 text-green-700 dark:text-green-300 font-bold">Challenge 1: Highscore</b>
            <p class="text-slate-500 mt-1">Sistem penyimpan rekor nilai game pemain secara permanen.</p>
        </div>
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700">
            <span class="text-xl">📝</span>
            <b class="block mt-1 text-blue-700 dark:text-blue-300 font-bold">Challenge 2: Buku Diary</b>
            <p class="text-slate-500 mt-1">Catat curhatan harian otomatis dengan tanggal & waktu.</p>
        </div>
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🧹</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 3: Pembersih Log</b>
            <p class="text-slate-500 mt-1">Filter baris file log yang mengandung kata ERROR saja.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Game Highscore Keeper 🎮",
            "subtitle": "Menyimpan dan Membaca Skor Tertinggi Pemain",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300"># Simulasi Selesai Main Game:</div>
        <div class="text-yellow-400">skor_baru = int(input("Masukkan skor kamu hari ini: "))</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Buka file <code>highscore.txt</code> dengan mode <code>'r'</code> (jika ada) dan baca skor lama.</li>
            <li>Jika <code>skor_baru > skor_lama</code>, cetak "Rekor Baru Tercipta! 🏆".</li>
            <li>Buka kembali dengan mode <code>'w'</code> dan simpan <code>skor_baru</code> ke file tersebut!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Buku Diary Cyber 📝",
            "subtitle": "Mencatat Jurnal Petualangan dengan Timestamp",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Import modul waktu: <code>from datetime import datetime</code>.</li>
            <li>Minta user memasukkan catatan diary via <code>input()</code>.</li>
            <li>Simpan dengan format: <code>f"[{datetime.now()}] {catatan}\\n"</code> menggunakan mode <code>'a'</code> ke <code>diary.txt</code>!</li>
            <li>Cek file untuk memastikan riwayat catatan tersimpan urut.</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Mesin Pembersih Log Error 🧹",
            "subtitle": "Menyaring Baris Tertentu dan Menyimpan ke File Baru",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Baca file <code>server.log</code> yang berisi campuran status INFO dan ERROR.</li>
            <li>Gunakan loop untuk menyaring baris yang memiliki kata <code>"ERROR"</code>.</li>
            <li>Tulis hanya baris-baris error tersebut ke dalam file baru <code>hanya_error.txt</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 4 📝",
            "subtitle": "Rangkuman Senjata File Handling",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="overflow-x-auto">
        <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
            <thead>
                <tr class="border-b border-slate-200 dark:border-slate-700 font-bold text-slate-800 dark:text-white">
                    <th class="py-2">Kode</th>
                    <th class="py-2">Fungsi</th>
                    <th class="py-2">Catatan Kritis</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-[11px]">
                <tr>
                    <td class="py-1.5 text-cyan-400">open("f.txt", "r")</td>
                    <td>Membaca file yang sudah ada</td>
                    <td>Error jika file tidak ditemukan</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-red-400">open("f.txt", "w")</td>
                    <td>Menulis baru / menimpa total</td>
                    <td>Menghapus seluruh isi file lama!</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">open("f.txt", "a")</td>
                    <td>Menambah baris baru di bawah</td>
                    <td>Paling aman untuk pencatatan log</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">with open(...) as f:</td>
                    <td>Context manager penutup otomatis</td>
                    <td>Mencegah memory leak & file korup</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai Data Persistence!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Program yang hebat adalah program yang tidak pernah lupa. File Handling adalah memori abadi aplikasimu."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 5: <b>Selamat Datang di Dunia Visual: Intro to Turtle Graphics</b>!
    </div>
</div>"""
        }
    ]

def get_m5_slides():
    return [
        {
            "title": "Meeting 5: Intro to Turtle Graphics 🐢",
            "subtitle": "Selamat Datang di Dunia Visual & Grafis Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🎨</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 5</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Selamat Tinggal Layar Terminal Hitam-Putih!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Hari ini kita memasuki babak baru yang sangat menyenangkan: <b>Turtle Graphics</b>! Kita akan mengendalikan seekor kura-kura robotik digital yang membawa pena untuk menggambar bentuk geometri, lukisan seni, dan animasi di layar komputermu!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <code>import turtle</code>, Gerakan Dasar (<code>forward</code>, <code>left</code>, <code>right</code>), Kontrol Pena (<code>penup</code>, <code>pendown</code>), dan Pewarnaan (<code>fill</code>)!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 5 🎯",
            "subtitle": "Target Penguasaan Turtle Graphics Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Kanvas Layar & Gerakan Dasar Kura-Kura</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami sistem koordinat kanvas dan menggerakkan turtle maju (forward), mundur (backward), serta belok (left, right).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Kustomisasi Tampilan: Bentuk, Warna Garis, & Kecepatan</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mengubah bentuk kura-kura, ketebalan kuas (pensize), warna tinta, dan kecepatan animasi (speed).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Kontrol Pena: Angkat, Tempel, & Teleportasi (goto)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Berpindah tempat tanpa mencoret layar menggunakan <code>penup()</code> dan <code>pendown()</code>.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Bendera Merah Putih & Rumah Geometri</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mengisi bidang warna dengan <code>begin_fill()</code> dan <code>end_fill()</code>.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 4 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat File Handling",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak mode file yang tepat untuk kasus berikut:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. Baca Artikel</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">open("naskah.txt", "r")</div>
            <p class="text-slate-500">Mode <code>'r'</code> (Read) hanya melihat data.</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. Tambah Catatan Log</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">open("log.txt", "a")</div>
            <p class="text-slate-500">Mode <code>'a'</code> (Append) tidak menghapus isi lama.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. Penutup Otomatis</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">with open(...) as f:</div>
            <p class="text-slate-500">Kunci keselamatan agar bebas bocor.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Setup Pertama: Memanggil Modul Turtle 🚀",
            "subtitle": "Import Modul Bawaan Resmi Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-xs leading-relaxed border border-slate-700 shadow-xl">
        <span class="text-purple-400">import</span> <span class="text-cyan-400">turtle</span><br><br>
        <span class="text-slate-400"># 1. Siapkan Kura-kura Penulis</span><br>
        <span class="text-yellow-400">t</span> = <span class="text-cyan-400">turtle</span>.<span class="text-green-400">Turtle</span>()<br>
        <span class="text-yellow-400">t</span>.<span class="text-blue-400">shape</span>(<span class="text-green-400">"turtle"</span>) <span class="text-slate-400"># Bentuk kura-kura</span><br><br>
        <span class="text-slate-400"># 2. Perintah wajib di baris paling akhir agar jendela tidak langsung menutup</span><br>
        <span class="text-cyan-400">turtle</span>.<span class="text-blue-400">done</span>()
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        💡 <b>Info Menarik:</b> Modul Turtle sudah terpasang otomatis di setiap instalasi Python di seluruh dunia sejak era 1960-an (bahasa Logo)!
    </div>
</div>"""
        },
        {
            "title": "Gerakan Dasar: Maju, Mundur, & Belok 🧭",
            "subtitle": "forward(pixel), backward(pixel), left(derajat), right(derajat)",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. Jarak (Pixel)</b>
            <div class="text-yellow-400">t.forward(100)  # Maju 100 langkah</div>
            <div class="text-yellow-400">t.backward(50)  # Mundur 50 langkah</div>
            <p class="text-slate-400 text-[11px] mt-2">Ukuran langkah turtle dihitung dalam satuan piksel layar komputer.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. Sudut Putar (Derajat)</b>
            <div class="text-green-400">t.right(90)  # Belok kanan 90 derajat</div>
            <div class="text-green-400">t.left(90)   # Belok kiri 90 derajat</div>
            <p class="text-slate-400 text-[11px] mt-2">Belok hanya memutar arah kepala kura-kura, belum berjalan maju!</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Menggambar Persegi Sempurna 👨‍🏫",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Menggambar Persegi 4 Sisi Sama Panjang</span><br>
        import turtle<br>
        t = turtle.Turtle()<br><br>
        t.forward(100) # Sisi 1<br>
        t.right(90)<br>
        t.forward(100) # Sisi 2<br>
        t.right(90)<br>
        t.forward(100) # Sisi 3<br>
        t.right(90)<br>
        t.forward(100) # Sisi 4<br><br>
        turtle.done()
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        📐 <b>Matematika Visual:</b> Persegi memiliki 4 sudut siku-siku masing-masing 90°. Total putaran: <code>4 x 90° = 360°</code> (kembali menghadap posisi semula)!
    </div>
</div>"""
        },
        {
            "title": "Kostumisasi Turtle: Kuas & Kecepatan 🎨",
            "subtitle": "color(), pensize(), speed()",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">t.color("blue")       <span class="text-slate-400"># Warna kuas: 'red', 'green', 'gold', dll</span></div>
        <div class="text-yellow-400">t.pensize(5)          <span class="text-slate-400"># Ketebalan garis (default: 1)</span></div>
        <div class="text-green-400">t.speed(10)           <span class="text-slate-400"># Kecepatan gerak (1 lambat, 10 cepat, 0 instan!)</span></div>
    </div>
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700">
            <b class="text-blue-700 dark:text-blue-300">speed(0) = Ultra Fast!</b>
            <p class="text-slate-500 mt-1">Gunakan angka 0 jika gambarmu sangat kompleks dan ingin langsung selesai tanpa menunggu animasi.</p>
        </div>
        <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700">
            <b class="text-green-700 dark:text-green-300">pensize(pixel)</b>
            <p class="text-slate-500 mt-1">Semakin besar angka pensize, semakin tebal goresan garis yang dihasilkan kura-kura.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Kontrol Pena: penup(), pendown(), & goto() 🪂",
            "subtitle": "Berpindah Tempat Tanpa Meninggalkan Coretan",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-yellow-400">t.penup()          <span class="text-slate-400"># Angkat pena dari kertas</span></div>
        <div class="text-cyan-400">t.goto(150, 100)    <span class="text-slate-400"># Teleportasi ke koordinat X=150, Y=100</span></div>
        <div class="text-green-400">t.pendown()        <span class="text-slate-400"># Tempelkan kembali pena ke kertas</span></div>
        <div class="text-purple-400">t.forward(50)      <span class="text-slate-400"># Mulai menggambar di tempat baru!</span></div>
    </div>
    <div class="p-3 bg-amber-50 dark:bg-slate-800 rounded-xl border border-amber-200 dark:border-slate-700 text-xs">
        🎯 <b>Aturan Emas:</b> Selalu ingat untuk <code>pendown()</code> setelah melakukan perpindahan! Jika lupa, kura-kura akan bergerak hantu tanpa mencoret apa pun di layar.
    </div>
</div>"""
        },
        {
            "title": "Mewarnai Bidang: begin_fill() & end_fill() 🪣",
            "subtitle": "Menumpahkan Ember Cat ke Dalam Bentuk Tertutup",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">t.fillcolor("crimson") # Tentukan warna isi</div>
        <div class="text-yellow-400">t.begin_fill()        # 1. Buka keran cat</div>
        <div class="text-slate-300 pl-4">t.circle(60)         # Gambar lingkaran radius 60</div>
        <div class="text-green-400">t.end_fill()          # 2. Kunci & isi seluruh bidang</div>
    </div>
    <div class="p-3 bg-red-50 dark:bg-slate-800 rounded-xl border border-red-200 dark:border-slate-700 text-xs">
        ⚠️ <b>Syarat Wajib Fill:</b> Bentuk harus tertutup (ujung garis bertemu dengan titik awal). Jika terbuka, warna bisa bocor atau tidak rata.
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Mengatasi Kesalahan Gambar Turtle 🐛",
            "subtitle": "Dua Kesalahan Paling Sering Terjadi di Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug 1: Layar Langsung Menutup</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                # Lupa menulis:<br>
                turtle.done()
            </div>
            <p class="text-slate-500">Tanpa <code>turtle.done()</code>, Python langsung mengakhiri proses OS begitu kode selesai.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-amber-700 dark:text-amber-400 text-sm">🐛 Bug 2: Garis 'Coretan Hantu'</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-400">
                t.goto(100, 100) # Tanpa penup()!
            </div>
            <p class="text-slate-500">Garis liar akan tergores dari titik asal (0,0) menuju tujuan. Angkat pena dulu sebelum berpindah!</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 1: Independent (Segitiga Sama Sisi) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Segitiga Sama Sisi Emas</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Gambarlah segitiga sama sisi dengan panjang sisi 120 pixel dan warna kuas emas (<code>"gold"</code>).
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Tebak berapa sudut belok luar segitiga? (Petunjuk: <code>360° / 3 = 120°</code>).</li>
            <li>Gunakan <code>t.pensize(4)</code> agar garis tampak gagah.</li>
            <li>Beri warna isi hijau (<code>"forestgreen"</code>) menggunakan <code>begin_fill()</code> dan <code>end_fill()</code>!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ ART CHALLENGE MODE: Galeri Kura-Kura ⚠️",
            "subtitle": "Pilih 1 dari 3 Karya Seni Berikut untuk Kamu Buat",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🎨</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Saatnya Melukis dengan Kode!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700">
            <span class="text-xl">🇮🇩</span>
            <b class="block mt-1 text-red-700 dark:text-red-300 font-bold">Challenge 1: Bendera</b>
            <p class="text-slate-500 mt-1">Dua persegi panjang bertumpuk: Merah di atas, Putih di bawah.</p>
        </div>
        <div class="p-4 rounded-xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700">
            <span class="text-xl">⭐</span>
            <b class="block mt-1 text-amber-700 dark:text-amber-300 font-bold">Challenge 2: Bintang</b>
            <p class="text-slate-500 mt-1">Bintang bersudut 5 dengan rumus belok 144 derajat.</p>
        </div>
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700">
            <span class="text-xl">🏡</span>
            <b class="block mt-1 text-blue-700 dark:text-blue-300 font-bold">Challenge 3: Rumah</b>
            <p class="text-slate-500 mt-1">Kombinasi dinding kotak, atap segitiga, dan matahari bundar.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Bendera Merah Putih 🇮🇩",
            "subtitle": "Menggabungkan Dua Kotak Berwarna Berbeda",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Gambar persegi panjang atas ukuran <code>lebar 200, tinggi 60</code>, warnai merah (<code>"red"</code>).</li>
            <li>Pindahkan kura-kura ke posisi bawah menggunakan <code>penup()</code> dan <code>goto(0, -60)</code>.</li>
            <li>Turunkan pena dengan <code>pendown()</code> dan gambar persegi panjang bawah bergaris abu-abu/putih!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Bintang Bersudut Lima ⭐",
            "subtitle": "Sudut Emas 144 Derajat Geometri Seni",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Atur <code>t.color("gold")</code> dan <code>t.pensize(3)</code>.</li>
            <li>Mulai isi dengan <code>t.begin_fill()</code>.</li>
            <li>Ulangi langkah ini 5 kali: <code>t.forward(150)</code> lalu <code>t.right(144)</code>!</li>
            <li>Tutup dengan <code>t.end_fill()</code> dan lihat bintang menyala sempurna!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Rumah Idaman & Matahari 🏡",
            "subtitle": "Tantangan Pro: Memadukan Berbagai Bentuk Geometri",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Gambar dinding rumah berbentuk kotak besar (warna oranye/biru).</li>
            <li>Gunakan <code>penup()</code> naik ke atas dinding dan gambar atap segitiga (warna merah/cokelat).</li>
            <li>Teleportasi ke langit pojok kanan atas, gambar lingkaran matahari kuning dengan <code>t.circle(30)</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 5 📝",
            "subtitle": "Rangkuman Senjata Perintah Dasar Turtle",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="overflow-x-auto">
        <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
            <thead>
                <tr class="border-b border-slate-200 dark:border-slate-700 font-bold text-slate-800 dark:text-white">
                    <th class="py-2">Perintah</th>
                    <th class="py-2">Fungsi</th>
                    <th class="py-2">Contoh</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-[11px]">
                <tr>
                    <td class="py-1.5 text-cyan-400">forward(x) / backward(x)</td>
                    <td>Maju / Mundur sejauh x piksel</td>
                    <td><code>t.forward(100)</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">left(deg) / right(deg)</td>
                    <td>Putar arah kepala kura-kura</td>
                    <td><code>t.right(90)</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">penup() / pendown()</td>
                    <td>Angkat pena (bebas gores) / tempelkan</td>
                    <td><code>t.penup(); t.goto(0,50)</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">begin_fill() / end_fill()</td>
                    <td>Buka & kunci ember pewarna bidang</td>
                    <td><code>t.begin_fill() ...</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-pink-400">turtle.done()</td>
                    <td>Tahan jendela kanvas tetap terbuka</td>
                    <td>Baris paling akhir script</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menjadi Digital Artist!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Seni dan logika bukan dua hal yang berlawanan. Dengan kode, komputermu adalah kanvas dan imajinasimu adalah kuasnya."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 6: <b>Colors & Pen Control: Palet Warna RGB & Efek Acak!</b>!
    </div>
</div>"""
        }
    ]
