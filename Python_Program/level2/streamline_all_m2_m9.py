# -*- coding: utf-8 -*-
"""
Streamline Meetings 2 through 9 in level2/deck.html
Reduces bloated 45 slides per meeting down to 16-24 high-impact slides.
Adheres strictly to the pedagogical time-budget:
- 30% Concept / Introduction
- 60% Hands-on Coding (Guided, Independent, Bug Hunt, Challenge)
- 10% Reflection & Closing
"""

import re
import json

def build_meeting_2():
    return [
        {
            "title": "Meeting 2: Dictionary (Key-Value Pairs) 📖",
            "subtitle": "Struktur Data Cerdas Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">📚</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 2</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Selamat Datang di Dunia Dictionary!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Di Sesi 1, kita sudah mahir menggunakan List dengan nomor urut (index 0, 1, 2). Hari ini kita akan menguasai struktur data yang jauh lebih cerdas: <b>Dictionary</b>, di mana data disimpan menggunakan label nama (<b>Key</b>) berpasangan dengan nilainya (<b>Value</b>)!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <b>Key-Value Pairs</b>, Akses Aman <code>.get()</code>, Modifikasi Data, dan Ekstrak Data (<code>keys</code>, <code>values</code>, <code>items</code>)!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 2 🎯",
            "subtitle": "Target Penguasaan Dictionary Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Konsep Key-Value & Anatomi Dictionary</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami cara menyimpan data dengan label deskriptif seperti kontak HP atau kamus kata.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Akses Cepat & Penanganan Bahaya KeyError</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mengambil data secara instan dan menggunakan method penyelamat <code>.get()</code> agar program tidak crash.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Metode Ekstraksi Data: .keys(), .values(), .items()</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Membongkar isi kamus secara menyeluruh dan mengulanginya (looping) dengan for loop.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Sistem Pokedex & Kasir Supermarket</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Membangun aplikasi data mini interaktif berbasis data kamus nyata.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 1 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Materi List & Slicing",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak output dari kode List berikut sebelum lanjut ke materi baru:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. Slicing Terpotong</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">hewan = ["Cat", "Dog", "Fox"]<br>print(hewan[0:2])</div>
            <p class="text-slate-500">Output: <code>['Cat', 'Dog']</code> (Stop index tidak ikut terbawa!)</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. append() vs insert()</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">skor = [10, 20]<br>skor.append(30)</div>
            <p class="text-slate-500"><code>.append()</code> selalu masuk ke antrian paling belakang.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. pop() Mengambil Data</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">item = skor.pop()<br>print(item)</div>
            <p class="text-slate-500"><code>.pop()</code> mencabut item dan mengembalikannya ke variabel.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Masalah List vs Solusi Dictionary 🗂️",
            "subtitle": "Mencari Berdasarkan Nomor vs Berdasarkan Nama",
            "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">❌</span>
            <b class="text-red-800 dark:text-red-300 text-sm">List: Sulit Diingat Angkanya</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-red-400">
            kontak = ["0812345", "0899999", "0877777"]<br><br>
            # Siapa nomor telepon milik Budi?<br>
            # Index 0? 1? Atau 2? Kita harus menebak!
        </div>
        <p class="text-xs text-slate-500">Jika ada 100 kontak, mustahil kita menghafal nomor urut index setiap orang.</p>
    </div>
    <div class="p-5 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">✅</span>
            <b class="text-green-800 dark:text-green-300 text-sm">Dictionary: Langsung Panggil Namanya!</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-green-400">
            kontak = {<br>
            &nbsp;&nbsp;"Andi": "0812345",<br>
            &nbsp;&nbsp;"Budi": "0899999"<br>
            }<br>
            print(kontak["Budi"]) # Langsung tepat!
        </div>
        <p class="text-xs text-slate-500">Cepat dan tepat! Komputer langsung melompat ke kunci yang dituju tanpa harus mencari satu per satu.</p>
    </div>
</div>"""
        },
        {
            "title": "Syntax & Anatomi Dictionary 🛠️",
            "subtitle": "Kurung Kurawal {}, Titik Dua :, dan Koma ,",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-sm leading-relaxed border border-slate-700 shadow-xl">
        <span class="text-slate-400"># Anatomi Pembuatan Dictionary:</span><br>
        <span class="text-yellow-400">biodata</span> = {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">"nama"</span>: <span class="text-green-400">"Archius"</span>,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">"level"</span>: <span class="text-purple-400">2</span>,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">"role"</span>: <span class="text-green-400">"Cyber Cadet"</span>,<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">"aktif"</span>: <span class="text-amber-400">True</span><br>
        }
    </div>
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 bg-cyan-50 dark:bg-slate-800 rounded-xl border border-cyan-200 dark:border-slate-700">
            <b class="text-cyan-700 dark:text-cyan-300">🔑 KEY (Kunci):</b>
            <p class="text-slate-500 mt-1">Label pengenal unik. Biasanya berupa <code>String</code>. Tidak boleh ada 2 Key yang kembar dalam satu kamus!</p>
        </div>
        <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700">
            <b class="text-green-700 dark:text-green-300">📦 VALUE (Nilai):</b>
            <p class="text-slate-500 mt-1">Isi datanya. Bebas tipe data apa saja: teks, angka, desimal, boolean, bahkan List lain!</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Akses & Modifikasi Data Kamus 🎯",
            "subtitle": "Membaca, Mengubah, dan Menambah Pasangan Data",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. Mengakses Data</b>
            <div class="text-slate-400">hero = {"nama": "Axe", "hp": 500}</div>
            <div class="text-green-400">print(hero["nama"]) # Output: Axe</div>
            <div class="text-green-400">print(hero["hp"])   # Output: 500</div>
            <p class="text-slate-400 text-[11px] mt-2">Gunakan tanda kurung siku <code>[ ]</code> dan masukkan nama Key-nya.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. Update & Tambah Data</b>
            <div class="text-slate-400"># Jika key sudah ada -> Mengubah isi</div>
            <div class="text-yellow-400">hero["hp"] = 450</div>
            <div class="text-slate-400"># Jika key belum ada -> Menambah baru</div>
            <div class="text-yellow-400">hero["senjata"] = "Kapak Petir"</div>
            <p class="text-slate-400 text-[11px] mt-2">Sintaksnya persis sama: Python otomatis memeriksa apakah Key sudah ada atau belum.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Kamus Terjemahan Cyber 👨‍🏫",
            "subtitle": "Mari Bedah dan Ketik Kode Bersama Guru",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-sm text-slate-600 dark:text-slate-300 font-medium">Ketik script berikut di VS Code / Replit:</p>
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># 1. Inisialisasi Dictionary Terjemahan</span><br>
        kamus = {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"cat": "kucing",<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"dog": "anjing",<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"bird": "burung"<br>
        }<br><br>
        <span class="text-slate-500"># 2. Ambil input dari user</span><br>
        kata = input("Masukkan kata bahasa Inggris: ")<br>
        if kata in kamus:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print(f"Artinya adalah: {kamus[kata]}")<br>
        else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print("Maaf, kata tidak ditemukan dalam kamus!")
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        💡 <b>Tips Guru:</b> Operator <code>kata in kamus</code> sangat berguna untuk mengecek apakah sebuah Key ada di dalam Dictionary sebelum kita memanggilnya.
    </div>
</div>"""
        },
        {
            "title": "Bahaya KeyError vs Senjata get() 🛡️",
            "subtitle": "Mengamankan Program dari Crash yang Tak Terduga",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-300 text-sm">🚨 Cara Rawan (Crash):</b>
            <div class="bg-black/30 p-2.5 rounded font-mono text-red-400">
                skor = {"Andi": 90}<br>
                print(skor["Budi"])
            </div>
            <p class="text-slate-600 dark:text-slate-400">Program langsung meledak dengan <code>KeyError: 'Budi'</code> dan berhenti total!</p>
        </div>
        <div class="p-4 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 text-xs space-y-2">
            <b class="text-green-700 dark:text-green-300 text-sm">🛡️ Senjata Aman: .get()</b>
            <div class="bg-black/30 p-2.5 rounded font-mono text-green-400">
                skor = {"Andi": 90}<br>
                hasil = skor.get("Budi", 0)<br>
                print(hasil) # Output: 0
            </div>
            <p class="text-slate-600 dark:text-slate-400">Jika Key tidak ada, <code>.get()</code> memberikan nilai default tanpa bikin program error!</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Menghapus Data: del vs pop() 🗑️",
            "subtitle": "Membuang Pasangan Key-Value yang Tidak Dibutuhkan",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700 text-xs text-white space-y-2 font-mono">
            <b class="text-cyan-300 block">1. Kata Kunci: del</b>
            <div class="text-slate-400">tas = {"pedang": 1, "potion": 5}</div>
            <div class="text-yellow-400">del tas["potion"]</div>
            <div class="text-slate-400">print(tas) # {"pedang": 1}</div>
            <p class="text-slate-400 text-[11px] mt-2">Menghapus langsung dari memori tanpa menyimpan nilai yang dihapus.</p>
        </div>
        <div class="p-4 rounded-2xl bg-slate-900 border border-slate-700 text-xs text-white space-y-2 font-mono">
            <b class="text-amber-300 block">2. Method: .pop()</b>
            <div class="text-slate-400">tas = {"pedang": 1, "potion": 5}</div>
            <div class="text-yellow-400">dibuang = tas.pop("potion")</div>
            <div class="text-slate-400">print(dibuang) # 5</div>
            <p class="text-slate-400 text-[11px] mt-2">Menghapus Key dan mengembalikan Valuenya agar bisa disimpan di variabel lain.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Ekstraksi Data: .keys(), .values(), .items() 💎",
            "subtitle": "Membongkar Isi Kamus Menjadi Koleksi Terpisah",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">nilai = {"Math": 90, "Coding": 100, "English": 85}</div>
        <div class="mt-2 text-slate-300">1. print(nilai.keys())   <span class="text-green-400"># ['Math', 'Coding', 'English']</span></div>
        <div class="text-slate-300">2. print(nilai.values()) <span class="text-green-400"># [90, 100, 85]</span></div>
        <div class="text-slate-300">3. print(nilai.items())  <span class="text-green-400"># [('Math', 90), ('Coding', 100), ...]</span></div>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center text-xs">
        <div class="p-2.5 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 font-semibold text-blue-700 dark:text-blue-300">
            .keys()<br><span class="text-[10px] text-slate-500 font-normal">Hanya daftar label kunci</span>
        </div>
        <div class="p-2.5 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 font-semibold text-green-700 dark:text-green-300">
            .values()<br><span class="text-[10px] text-slate-500 font-normal">Hanya daftar isi nilai</span>
        </div>
        <div class="p-2.5 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 font-semibold text-purple-700 dark:text-purple-300">
            .items()<br><span class="text-[10px] text-slate-500 font-normal">Pasangan (Key, Value)</span>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Looping Dictionary: Membaca Semua Isi 🔄",
            "subtitle": "Mengulang Pasangan Data Menggunakan for loop",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. Looping Standar (Hanya Key)</b>
            <div class="text-yellow-400">for k in menu:</div>
            <div class="text-green-400 pl-4">print(k, "->", menu[k])</div>
            <p class="text-slate-400 text-[11px] mt-2">Komputer membaca setiap Key satu per satu, lalu kita memanggil valuenya secara manual.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. Looping Pasangan (.items())</b>
            <div class="text-yellow-400">for k, v in menu.items():</div>
            <div class="text-green-400 pl-4">print(f"Menu {k} harganya {v}")</div>
            <p class="text-slate-400 text-[11px] mt-2">Cara paling elegan! Langsung membongkar Key ke variabel <code>k</code> dan Value ke <code>v</code>.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Konsep Lanjutan: Nested Dictionary 🪆",
            "subtitle": "Kamus di dalam Kamus (Struktur Data Profil Game)",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-cyan-300 border border-slate-700 leading-relaxed">
        players = {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"player1": {"nama": "Axe", "role": "Warrior", "hp": 500},<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"player2": {"nama": "Lina", "role": "Mage", "hp": 300}<br>
        }<br><br>
        <span class="text-slate-400"># Cara mengakses HP milik player2:</span><br>
        <span class="text-green-400">print(players["player2"]["hp"]) # Output: 300</span>
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        💡 <b>Dunia Nyata:</b> Hampir semua sistem game online, profil akun media sosial, dan data internet (JSON) menggunakan struktur Nested Dictionary seperti ini!
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Mengatasi Error Dictionary 🐛",
            "subtitle": "Dua Kesalahan Paling Sering Terjadi di Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug 1: KeyError Huruf Kapital</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                data = {"nama": "Budi"}<br>
                print(data["Nama"]) # ERROR!
            </div>
            <p class="text-slate-500">Key di Python itu <b>case-sensitive</b>! <code>"nama"</code> tidak sama dengan <code>"Nama"</code>.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-amber-700 dark:text-amber-400 text-sm">🐛 Bug 2: Unhashable Type (Key berupa List)</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-400">
                kamus = {[1, 2]: "nilai"} # ERROR!
            </div>
            <p class="text-slate-500">Key tidak boleh berupa List karena List bisa berubah (mutable). Gunakan String atau Angka untuk Key.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Ambil Data Raport) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Aplikasi Nilai Raport Siswa</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Buatlah sebuah dictionary berisi 4 mata pelajaran favoritmu beserta nilainya (misal: Matematika, IPA, Bahasa Inggris, Seni).
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Tampilkan nilai mata pelajaran tertinggi dengan format rapi.</li>
            <li>Ubah salah satu nilai mata pelajaran menjadi 100 karena kamu baru saja remedial.</li>
            <li>Hitung rata-rata nilai menggunakan <code>sum(raport.values()) / len(raport)</code>!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "Exercise 3: Independent (Update Kontak) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Menengah",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-indigo-500/20 text-indigo-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Sistem Buku Kontak Cyber</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Buat program yang menerima input nama teman dan nomor telepon dari user, lalu simpan ke dalam dictionary.
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Gunakan loop agar user bisa memasukkan 3 kontak sekaligus.</li>
            <li>Setelah selesai, tampilkan semua kontak dengan looping <code>.items()</code> dalam bentuk tabel terminal.</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ CHALLENGE MODE: Ujian Kelayakan 2 ⚠️",
            "subtitle": "Pilih 1 dari 3 Tantangan Kode Nyata Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🏆</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Saatnya Membuktikan Keahlianmu!</h3>
    <p class="text-slate-600 dark:text-slate-400 text-sm">Pilih misi yang sesuai dengan level kepercayaan dirimu hari ini:</p>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700">
            <span class="text-xl">🐉</span>
            <b class="block mt-1 text-green-700 dark:text-green-300 font-bold">Challenge 1: Pokedex</b>
            <p class="text-slate-500 mt-1">Cari tipe dan skill Pokemon favorit dari dictionary database.</p>
        </div>
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700">
            <span class="text-xl">🛒</span>
            <b class="block mt-1 text-blue-700 dark:text-blue-300 font-bold">Challenge 2: Kasir Minimarket</b>
            <p class="text-slate-500 mt-1">Hitung total belanjaan berdasarkan daftar harga barang dan quantity.</p>
        </div>
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🎓</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 3: Rapor Bintang</b>
            <p class="text-slate-500 mt-1">Kelola data murid bertingkat (Nested Dict) lengkap dengan ranking.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Pokedex Pokemon 🐉",
            "subtitle": "Mencari Informasi Elemen & Status Monster",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">pokedex = {</div>
        <div class="pl-4 text-slate-300">"Pikachu": {"tipe": "Electric", "power": 55},</div>
        <div class="pl-4 text-slate-300">"Charizard": {"tipe": "Fire/Flying", "power": 84},</div>
        <div class="pl-4 text-slate-300">"Blastoise": {"tipe": "Water", "power": 79}</div>
        <div class="text-cyan-300">}</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Minta user memasukkan nama Pokemon via <code>input()</code>.</li>
            <li>Gunakan <code>.get()</code> untuk mengecek apakah monster ada di dalam pokedex.</li>
            <li>Jika ada, cetak Tipe dan Power-nya secara menarik! Jika tidak ada, beri pesan ramah.</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Kasir Supermarket 🛒",
            "subtitle": "Simulasi Hitung Belanja Otomatis dengan Looping",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">harga = {"roti": 15000, "susu": 20000, "apel": 8000, "keju": 25000}</div>
        <div class="text-yellow-300">keranjang = ["roti", "susu", "susu", "apel"]</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Buat variabel <code>total_belanja = 0</code>.</li>
            <li>Gunakan for loop untuk mengulang setiap item di dalam <code>keranjang</code>.</li>
            <li>Ambil harganya dari dictionary <code>harga</code> lalu tambahkan ke <code>total_belanja</code>.</li>
            <li>Cetak struk belanjaan dan total yang harus dibayar user!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Rapor Kelas Bintang 🎓",
            "subtitle": "Tantangan Pro: Nested Dictionary & Nilai Rata-rata",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">kelas = {</div>
        <div class="pl-4 text-slate-300">"Andi": {"math": 80, "english": 85},</div>
        <div class="pl-4 text-slate-300">"Budi": {"math": 95, "english": 90}</div>
        <div class="text-cyan-300">}</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Gunakan <code>for nama, nilai in kelas.items():</code></li>
            <li>Hitung rata-rata setiap siswa: <code>(nilai["math"] + nilai["english"]) / 2</code>.</li>
            <li>Tampilkan status: jika rata-rata >= 85 beri gelar "Cadet Berprestasi ⭐"!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 2 📝",
            "subtitle": "Rangkuman Senjata Dictionary Planet Modula",
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
                    <td class="py-1.5 text-cyan-400">d = {"a": 1}</td>
                    <td>Membuat kamus Key-Value</td>
                    <td><code>kontak = {"Budi": "081"}</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-cyan-400">d["a"]</td>
                    <td>Akses value via Key (rawan KeyError)</td>
                    <td><code>print(d["Budi"])</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">d.get("b", 0)</td>
                    <td>Akses aman dengan nilai default</td>
                    <td><code>d.get("Cici", "Tidak ada")</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">d["c"] = 99</td>
                    <td>Update atau tambah Key baru</td>
                    <td><code>d["skor"] = 100</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">d.items()</td>
                    <td>Pasangan (Key, Value) untuk loop</td>
                    <td><code>for k, v in d.items():</code></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai Dictionary!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Data tanpa label adalah kekacauan. Dengan Dictionary, kita memberi arti dan tujuan pada setiap informasi."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 3: <b>String Manipulation & Text Processing</b>!
    </div>
</div>"""
        }
    ]

print("Script template ready for building Meetings 2-9.")
