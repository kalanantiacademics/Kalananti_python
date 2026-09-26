# -*- coding: utf-8 -*-
"""Generate streamlined Meeting 1 for level2/deck.html (Pilot: 24 slides)"""

m1_streamlined_slides = [
    {
        "title": "Meeting 1: Advanced Lists & Slicing 📋",
        "subtitle": "Misi Baru di Planet Modula Dimulai",
        "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🚀</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Planet Modula</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Selamat Datang di Level 2!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Di Level 1, kita sudah menguasai logika dasar dan variabel tunggal. Sekarang di Planet Modula, kita akan naik tingkat menjadi <b>Master Pengendali Data</b>: mengelola ratusan data sekaligus menggunakan struktur data modern!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <b>List</b>, <b>Zero-Based Indexing</b>, <b>Slicing</b>, dan <b>5 Method Sakti</b>!
    </div>
</div>"""
    },
    {
        "title": "Objectives & Roadmap Misi 1 🎯",
        "subtitle": "Target Penguasaan Data Hari Ini",
        "content": """<div class="max-w-3xl mx-auto space-y-4">
    <ul class="space-y-3 text-left">
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Konsep List & Zero-Based Indexing</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami cara komputer menyimpan banyak data berurutan mulai dari index 0.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Teknik Slicing Data [start : stop]</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mengiris dan mengambil sebagian data spesifik secara instan dengan rumus sakti.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">5 Method Bawaan List (Built-in Methods)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menambah (<code>append</code>, <code>insert</code>), menghapus (<code>pop</code>, <code>remove</code>), dan mengurutkan (<code>sort</code>, <code>len</code>).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Sistem Inventaris Cyber</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menerapkan seluruh keahlian dalam latihan terbimbing dan tantangan mandiri.</p>
            </div>
        </li>
    </ul>
</div>"""
    },
    {
        "title": "Speed Review Challenge ⚡",
        "subtitle": "Uji Ingatan Kilat Materi Level 1",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tiga pilar Level 1 yang wajib kamu ingat:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. Variabel & Print</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">hero = "Iron Man"<br>print("Hero:", hero)</div>
            <p class="text-slate-500">Variabel adalah kotak penyimpan 1 nilai.</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. Input & Casting</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">skor = int(input())<br>total = skor + 10</div>
            <p class="text-slate-500">Input selalu menghasilkan String, ubah dengan <code>int()</code> jika ingin dihitung.</p>
        </div>
        <div class="p-4 rounded-2xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 space-y-2">
            <b class="text-green-800 dark:text-green-300 text-sm">3. If-Else Indentasi</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">if skor >= 80:<br>&nbsp;&nbsp;&nbsp;&nbsp;print("Lulus!")</div>
            <p class="text-slate-500">Indentasi (spasi menjorok) wajib agar tidak syntax error.</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Konsep 1: Mengapa Butuh List? 📦",
        "subtitle": "Kamar Berantakan vs Laci Terorganisir",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🌪️</span>
            <b class="text-red-800 dark:text-red-300 text-sm">Tanpa List: Chaos di Memori</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-red-400">
            murid1 = "Andi"<br>
            murid2 = "Budi"<br>
            murid3 = "Cici"<br>
            ...<br>
            murid100 = "Zeta"
        </div>
        <p class="text-xs text-slate-500">Bayangkan jika ada 1000 murid! Memori komputer berantakan dan sulit dikelola.</p>
    </div>
    <div class="p-5 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🗄️</span>
            <b class="text-green-800 dark:text-green-300 text-sm">Dengan List: Satu Lemari Rapi</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-green-400">
            murid = ["Andi", "Budi", "Cici", ..., "Zeta"]
        </div>
        <p class="text-xs text-slate-500">Cukup <b>1 variabel</b> untuk menampung ribuan data berurutan dengan aman dan rapi!</p>
    </div>
</div>"""
    },
    {
        "title": "Syntax & Anatomi List 🛠️",
        "subtitle": "Kurung Siku [], Koma, dan Tipe Data Campuran",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Di Python, List dibuat menggunakan kurung siku <code>[ ]</code> dan setiap data dipisahkan dengan koma <code>,</code> :</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 font-mono text-xs text-green-400 space-y-2">
        <span class="text-slate-500"># 1. List Teks (String)</span><br>
        buah = ["Apel", "Jeruk", "Mangga"]<br><br>
        <span class="text-slate-500"># 2. List Angka (Integer / Float)</span><br>
        nilai = [95, 80, 88, 100]<br><br>
        <span class="text-slate-500"># 3. List Campuran (Fleksibel!)</span><br>
        profil = ["Andi", 14, True, 165.5]&nbsp;&nbsp;<span class="text-slate-500"># String, Int, Bool, Float</span>
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800/80 rounded-xl border border-blue-200 dark:border-slate-700 text-xs text-blue-900 dark:text-blue-200">
        💡 List di Python sangat hebat karena bisa menyimpan berbagai tipe data sekaligus di dalam satu wadah!
    </div>
</div>"""
    },
    {
        "title": "Konsep 2: Zero-Based Indexing 🔢",
        "subtitle": "Mengapa Komputer Memulai dari Angka 0?",
        "content": """<div class="max-w-4xl mx-auto space-y-5 text-center">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Setiap elemen di dalam list memiliki nomor urut alamat yang disebut <b>Index</b>:</p>
    <div class="flex justify-center gap-3 py-3">
        <div class="bg-slate-900 text-white p-4 rounded-xl border-2 border-blue-500 w-24 text-center">
            <div class="text-base font-bold font-mono">"Apel"</div>
            <div class="text-xs text-cyan-400 mt-2 font-bold font-mono">Index [0]</div>
        </div>
        <div class="bg-slate-900 text-white p-4 rounded-xl border-2 border-blue-500 w-24 text-center">
            <div class="text-base font-bold font-mono">"Jeruk"</div>
            <div class="text-xs text-cyan-400 mt-2 font-bold font-mono">Index [1]</div>
        </div>
        <div class="bg-slate-900 text-white p-4 rounded-xl border-2 border-blue-500 w-24 text-center">
            <div class="text-base font-bold font-mono">"Mangga"</div>
            <div class="text-xs text-cyan-400 mt-2 font-bold font-mono">Index [2]</div>
        </div>
        <div class="bg-slate-900 text-white p-4 rounded-xl border-2 border-blue-500 w-24 text-center">
            <div class="text-base font-bold font-mono">"Pisang"</div>
            <div class="text-xs text-cyan-400 mt-2 font-bold font-mono">Index [3]</div>
        </div>
    </div>
    <div class="p-4 bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800/50 rounded-2xl text-xs max-w-2xl mx-auto text-left space-y-1">
        <b class="text-amber-800 dark:text-amber-300">Kenapa mulai dari 0?</b>
        <p class="text-slate-600 dark:text-slate-400">Dalam arsitektur komputer, index adalah <i>jarak lompatan (offset)</i> dari pintu gerbang memori. Elemen pertama berada tepat di pintu gerbang, sehingga jarak lompatannya adalah <b>0 lompatan</b>!</p>
    </div>
</div>"""
    },
    {
        "title": "Quiz Kilat: Tebak Index Laci 🧠",
        "subtitle": "Uji Kejelian Zero-Based Indexing",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-5xl">🧐</div>
    <div class="bg-slate-900 p-4 rounded-xl font-mono text-sm text-green-400 text-left">
        hero = ["Iron Man", "Thor", "Hulk", "Spider-Man"]
    </div>
    <p class="font-semibold text-slate-800 dark:text-white text-lg">Jika kita ingin memanggil <b>"Hulk"</b>, index berapakah yang harus kita tulis?</p>
    <div class="grid grid-cols-3 gap-3">
        <button onclick="showMiniFeedback('fb-m1-quiz', 'Salah! hero[1] adalah Thor.', 'warn')" class="p-3 bg-white/5 border border-white/10 rounded-xl hover:border-blue-400 font-mono text-sm">hero[1]</button>
        <button onclick="showMiniFeedback('fb-m1-quiz', 'Tepat Sekali! Iron Man [0], Thor [1], Hulk [2].', 'success')" class="p-3 bg-white/5 border border-white/10 rounded-xl hover:border-green-400 font-mono text-sm">hero[2]</button>
        <button onclick="showMiniFeedback('fb-m1-quiz', 'Salah! hero[3] adalah Spider-Man.', 'warn')" class="p-3 bg-white/5 border border-white/10 rounded-xl hover:border-blue-400 font-mono text-sm">hero[3]</button>
    </div>
    <div id="fb-m1-quiz" class="min-h-[40px] mt-2"></div>
</div>"""
    },
    {
        "title": "Guided Practice 1: Buat & Panggil List 👨‍🏫",
        "subtitle": "Koding Bersama Guru di VS Code",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Buka VS Code, buat file <code>latihan1.py</code> dan ketik kode berikut bersama guru:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># 1. Deklarasi list hewan</span><br>
        hewan = ["Kucing", "Anjing", "Kelinci", "Panda"]<br><br>
        <span class="text-slate-500"># 2. Cetak elemen pertama</span><br>
        print("Elemen pertama:", hewan[0])&nbsp;&nbsp;<span class="text-slate-500"># Output: Kucing</span><br><br>
        <span class="text-slate-500"># 3. Trik Sakti: Index Negatif mengambil dari belakang!</span><br>
        print("Elemen terakhir:", hewan[-1])&nbsp;&nbsp;<span class="text-slate-500"># Output: Panda</span>
    </div>
    <p class="text-xs text-blue-600 dark:text-blue-400 font-semibold">💡 Tips Pro: <code>[-1]</code> adalah cara tercepat mengambil elemen paling ujung tanpa perlu menghitung panjang list!</p>
</div>"""
    },
    {
        "title": "Konsep 3: List Bersifat Mutable (Bisa Diubah) 🔄",
        "subtitle": "Mengubah Nilai Tertentu Secara Langsung",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="space-y-4">
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">List Bersifat "Bisa Diedit"</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Berbeda dengan teks String yang paten, item di dalam List bisa kita ganti sewaktu-waktu hanya dengan menyebutkan nomor indexnya:
        </p>
        <div class="bg-slate-900 p-4 rounded-xl font-mono text-xs text-green-400 space-y-1">
            skor = [10, 20, 30]<br>
            skor[1] = 99&nbsp;&nbsp;<span class="text-slate-500"># Ganti index 1 jadi 99</span><br>
            print(skor)&nbsp;&nbsp;<span class="text-cyan-400"># [10, 99, 30]</span>
        </div>
    </div>
    <div class="p-6 bg-slate-100 dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 text-center space-y-2">
        <div class="text-5xl">✏️</div>
        <div class="font-bold text-slate-800 dark:text-white text-sm">Operasi Timpa Data</div>
        <p class="text-xs text-slate-500">Nilai lama pada laci tersebut otomatis digantikan dengan nilai baru seketika!</p>
    </div>
</div>"""
    },
    {
        "title": "Bug Hunt 1: Jebakan IndexError! 🐞",
        "subtitle": "Mendiagnosis Kesalahan Umum Programmer",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left text-xs">
    <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 font-mono text-red-400 space-y-1">
        buah = ["Apel", "Jeruk", "Mangga"]<br>
        print(buah[3])&nbsp;&nbsp;<span class="text-amber-400"># 💥 ERROR: IndexError: list index out of range</span>
    </div>
    <div class="p-4 bg-red-50 dark:bg-red-950/40 border border-red-300 dark:border-red-800/50 rounded-2xl space-y-2">
        <b class="text-red-800 dark:text-red-300 text-sm">Mengapa Muncul Error Ini?</b>
        <p class="text-slate-600 dark:text-slate-400">
            Jumlah buah ada 3, tapi indexnya adalah <b>0, 1, dan 2</b>. Memanggil index <code>[3]</code> artinya mencari laci ke-4 yang sama sekali tidak ada!
        </p>
        <p class="text-green-700 dark:text-green-300 font-bold">Solusi: Index tertinggi selalu bernilai (Jumlah Elemen - 1).</p>
    </div>
</div>"""
    },
    {
        "title": "Independent Mission 1: Inventaris Hero 💻",
        "subtitle": "Praktik Mandiri 8 Menit",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-pulse">⚔️</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Misi Mandiri 1: Bikin List Hero</h3>
    <div class="p-5 bg-slate-900 text-left rounded-2xl border border-slate-700 font-mono text-xs text-cyan-300 space-y-2 max-w-lg mx-auto">
        <p>1. Buat list <code>hero = ["Batman", "Superman", "Flash", "Aquaman"]</code></p>
        <p>2. Ganti hero pada index 1 ("Superman") menjadi "Wonder Woman"</p>
        <p>3. Cetak hero pertama dan hero terakhir menggunakan index negatif!</p>
        <p>4. Tampilkan seluruh list <code>hero</code> ke layar.</p>
    </div>
    <p class="text-xs text-slate-400">Waktu koding: 8 menit di VS Code. Buktikan kamu paham index!</p>
</div>"""
    },
    {
        "title": "Konsep 4: Seni Memotong Data (Slicing) 🗡️",
        "subtitle": "Formula Sakti [start : stop]",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="space-y-4">
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Apa itu Slicing?</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Jika index hanya mengambil <b>1 data</b>, maka <b>Slicing</b> mengambil <b>sebagian potongan list</b> sekaligus!
        </p>
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 font-mono text-xs">
            <b>Rumus:</b> data[start : stop]
        </div>
        <div class="p-3 bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800/50 rounded-xl text-xs space-y-1">
            <b class="text-amber-800 dark:text-amber-300">⚠️ ATURAN STOP - 1:</b>
            <p class="text-slate-600 dark:text-slate-400">Angka <code>stop</code> tidak diikutkan! Jika menulis <code>[1:4]</code>, data yang diambil adalah index <b>1, 2, dan 3</b>.</p>
        </div>
    </div>
    <div class="p-6 bg-slate-100 dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 text-center space-y-2">
        <div class="text-5xl">🍞</div>
        <div class="font-bold text-slate-800 dark:text-white text-sm">Analogi Pisau Roti</div>
        <p class="text-xs text-slate-500">Kita memotong tepat di batas garis pisau, bukan di tengah rotinya!</p>
    </div>
</div>"""
    },
    {
        "title": "Shortcut Slicing Sakti ⚡",
        "subtitle": "Trik Cepat Menyingkat Kode",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Programmer profesional jarang menuliskan angka start jika mulai dari awal:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-3">
        <div>
            <span class="text-slate-500"># List contoh:</span><br>
            huruf = ["A", "B", "C", "D", "E"]
        </div>
        <div>
            <span class="text-blue-400">print(huruf[:3])</span>&nbsp;&nbsp;<span class="text-slate-500"># Dari AWAL sampai sebelum 3 -> ['A', 'B', 'C']</span>
        </div>
        <div>
            <span class="text-indigo-400">print(huruf[2:])</span>&nbsp;&nbsp;<span class="text-slate-500"># Dari index 2 sampai AKHIR -> ['C', 'D', 'E']</span>
        </div>
        <div>
            <span class="text-amber-400">print(huruf[:])</span>&nbsp;&nbsp;<span class="text-slate-500"># Duplikasi/Salin SELURUH list secara instan!</span>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Guided Practice 2: Bedah Slicing Data 👨‍🏫",
        "subtitle": "Hands-on Slicing Bersama Guru",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Coba ketik kode filter skor ranking ini di VS Code:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        pemain = ["Zeta", "Alpha", "Omega", "Beta", "Sigma"]<br><br>
        <span class="text-slate-500"># Ambil Top 3 Juara (index 0, 1, 2)</span><br>
        top_3 = pemain[:3]<br>
        print("Pemenang Podium:", top_3)&nbsp;&nbsp;<span class="text-slate-500"># ['Zeta', 'Alpha', 'Omega']</span><br><br>
        <span class="text-slate-500"># Ambil 2 pemain cadangan terakhir</span><br>
        cadangan = pemain[3:]<br>
        print("Pemain Cadangan:", cadangan)&nbsp;&nbsp;<span class="text-slate-500"># ['Beta', 'Sigma']</span>
    </div>
</div>"""
    },
    {
        "title": "Independent Mission 2: Potong Data Rahasia 💻",
        "subtitle": "Praktik Mandiri 8 Menit",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-pulse">✂️</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Misi Mandiri 2: Irisan Data Agen</h3>
    <div class="p-5 bg-slate-900 text-left rounded-2xl border border-slate-700 font-mono text-xs text-cyan-300 space-y-2 max-w-lg mx-auto">
        <p>1. Buat list <code>angka = [10, 20, 30, 40, 50, 60, 70]</code></p>
        <p>2. Gunakan slicing untuk mengambil <code>[20, 30, 40]</code></p>
        <p>3. Gunakan shortcut untuk mengambil 4 angka pertama</p>
        <p>4. Gunakan shortcut untuk mengambil 3 angka terakhir</p>
    </div>
    <p class="text-xs text-slate-400">Jalankan di terminal dan periksa hasilnya!</p>
</div>"""
    },
    {
        "title": "List Methods: Menambah Data ➕",
        "subtitle": ".append() vs .insert()",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🚪</span>
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. .append(nilai)</b>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-400">Menaruh data baru di <b>antrean paling belakang</b>:</p>
        <div class="bg-black/30 p-2.5 rounded font-mono text-xs text-cyan-300">
            hewan = ["Kucing"]<br>
            hewan.append("Anjing")<br>
            <span class="text-slate-500"># Hasil: ["Kucing", "Anjing"]</span>
        </div>
    </div>
    <div class="p-5 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🥷</span>
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. .insert(index, nilai)</b>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-400">Menyusupkan data baru di <b>posisi index spesifik</b>:</p>
        <div class="bg-black/30 p-2.5 rounded font-mono text-xs text-indigo-300">
            hewan = ["Kucing", "Anjing"]<br>
            hewan.insert(1, "Kelinci")<br>
            <span class="text-slate-500"># Hasil: ["Kucing", "Kelinci", "Anjing"]</span>
        </div>
    </div>
</div>"""
    },
    {
        "title": "List Methods: Menghapus Data 🗑️",
        "subtitle": ".pop() vs .remove()",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🎈</span>
            <b class="text-red-800 dark:text-red-300 text-sm">1. .pop(index)</b>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-400">Menghapus berdasarkan <b>nomor index</b> (bisa disimpan hasilnya):</p>
        <div class="bg-black/30 p-2.5 rounded font-mono text-xs text-red-300">
            item_dibuang = hewan.pop(0)<br>
            <span class="text-slate-500"># Menghapus index 0 ("Kucing")</span>
        </div>
    </div>
    <div class="p-5 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🎯</span>
            <b class="text-amber-800 dark:text-amber-300 text-sm">2. .remove(nilai)</b>
        </div>
        <p class="text-xs text-slate-600 dark:text-slate-400">Menghapus berdasarkan <b>nama nilainya</b>:</p>
        <div class="bg-black/30 p-2.5 rounded font-mono text-xs text-amber-300">
            hewan.remove("Anjing")<br>
            <span class="text-slate-500"># Mencari nama "Anjing" lalu dihapus</span>
        </div>
    </div>
</div>"""
    },
    {
        "title": "List Methods: Urutkan & Hitung 📊",
        "subtitle": ".sort() dan len()",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Dua alat pamungkas untuk merapikan dan menginspeksi data:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-3">
        <div>
            <span class="text-slate-500"># Mengurutkan otomatis (A-Z atau Angka Kecil ke Besar):</span><br>
            nilai = [40, 100, 25, 80]<br>
            nilai.sort()<br>
            print(nilai)&nbsp;&nbsp;<span class="text-cyan-400"># Output: [25, 40, 80, 100]</span>
        </div>
        <div>
            <span class="text-slate-500"># Menghitung panjang/total isi list:</span><br>
            total_siswa = len(nilai)<br>
            print("Jumlah data:", total_siswa)&nbsp;&nbsp;<span class="text-cyan-400"># Output: 4</span>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Guided Practice 3: Simulasi Gudang Cyber 👨‍🏫",
        "subtitle": "Kombinasi Seluruh Method dalam 1 Kasus Nyata",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Ketik simulasi inventaris game ini di VS Code:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        inv = ["Pedang", "Perisai", "Ramuan"]<br><br>
        <span class="text-slate-500"># 1. Tambah panah di belakang</span><br>
        inv.append("Panah")<br><br>
        <span class="text-slate-500"># 2. Sisipkan baju zirah di posisi index 1</span><br>
        inv.insert(1, "Baju Zirah")<br><br>
        <span class="text-slate-500"># 3. Ramuan diminum (dihapus)</span><br>
        inv.remove("Ramuan")<br><br>
        <span class="text-slate-500"># 4. Urutkan abjad alfabet</span><br>
        inv.sort()<br>
        print(f"Isi Inventaris ({len(inv)} item):", inv)
    </div>
</div>"""
    },
    {
        "title": "Bug Hunt 2: Error Method Populer 🐞",
        "subtitle": "Mencegah Crash Saat Mengolah List",
        "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="p-4 rounded-xl bg-red-50 dark:bg-red-950/40 border border-red-300 dark:border-red-800/50 space-y-1">
        <b class="text-red-800 dark:text-red-300">Jebakan: ValueError: list.remove(x): x not in list</b>
        <div class="bg-black/30 p-2 rounded font-mono text-red-400">
            inv = ["Pedang", "Panah"]<br>
            inv.remove("Bom")&nbsp;&nbsp;<span class="text-amber-400"># 💥 ERROR: Bom tidak ada di list!</span>
        </div>
        <p class="text-green-700 dark:text-green-300 font-bold mt-1">Solusi Cerdas: Selalu cek keberadaan item terlebih dahulu:</p>
        <div class="bg-black/30 p-2 rounded font-mono text-green-300">
            if "Bom" in inv:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;inv.remove("Bom")
        </div>
    </div>
</div>"""
    },
    {
        "title": "Final Boss Challenge: Cyber Store 🏆",
        "subtitle": "Tantangan Mandiri Integratif 12 Menit",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-bounce">🏪</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Final Boss: Toko Senjata Cyber</h3>
    <div class="p-5 bg-slate-900 text-left rounded-2xl border border-slate-700 font-mono text-xs text-green-300 space-y-2 max-w-lg mx-auto">
        <p>1. Buat list <code>toko = ["Potion", "Shield", "Sword", "Armor"]</code></p>
        <p>2. Pelanggan membeli item pertama: gunakan <code>.pop(0)</code></p>
        <p>3. Stok baru datang: tambahkan "Helmet" dan "Bow" pakai <code>.append()</code></p>
        <p>4. Urutkan toko secara alfabet dengan <code>.sort()</code></p>
        <p>5. Cetak: "Total stok sekarang ada [len] item: [isi list]"</p>
    </div>
    <p class="text-xs text-slate-400">Kerjakan sendiri di VS Code dan tunjukkan ke gurumu!</p>
</div>"""
    },
    {
        "title": "Cheat Sheet & Rangkuman Esensial 📋",
        "subtitle": "Koleksi Jurus Sakti List dalam 1 Layar",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left text-xs">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <h4 class="font-bold text-slate-800 dark:text-white text-sm">Tabel Rangkuman Operasi List:</h4>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-2 font-mono text-[11px]">
            <div class="p-2.5 bg-slate-900 rounded-lg text-blue-300">data[0] ➔ Item pertama</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-blue-300">data[-1] ➔ Item terakhir</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-indigo-300">data[:3] ➔ Ambil 3 data awal</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-indigo-300">data[2:] ➔ Ambil index 2 ke atas</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-green-300">.append(x) ➔ Tambah belakang</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-green-300">.insert(i, x) ➔ Sisip di index</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-red-300">.pop(i) ➔ Hapus nomor index</div>
            <div class="p-2.5 bg-slate-900 rounded-lg text-amber-300">.sort() ➔ Urutkan abjad</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Refleksi & Exit Ticket 🎟️",
        "subtitle": "Check Pemahaman Misi Hari Ini",
        "content": """<div class="max-w-2xl mx-auto space-y-5 text-center">
    <div class="text-5xl">🎟️</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Tiket Keluar Lab Modula</h3>
    <p class="text-sm text-slate-600 dark:text-slate-300">Sebelum mengakhiri sesi, jawablah 2 pertanyaan ini dalam hatimu:</p>
    <div class="grid sm:grid-cols-2 gap-3 text-xs text-left max-w-lg mx-auto">
        <div class="p-4 bg-white/5 border border-white/10 rounded-xl">
            <b>1. Apa beda .append() dan .insert()?</b>
            <p class="text-slate-400 mt-1">Kapan kita harus memilih salah satunya?</p>
        </div>
        <div class="p-4 bg-white/5 border border-white/10 rounded-xl">
            <b>2. Mengapa slicing [:3] berhenti di index 2?</b>
            <p class="text-slate-400 mt-1">Ingat selalu rumus (stop - 1)!</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Quote of the Day 🌟",
        "subtitle": "Penutup Misi 1",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-6">
    <div class="text-6xl">🚀</div>
    <blockquote class="text-xl md:text-2xl font-bold text-slate-800 dark:text-white italic leading-relaxed">
        "Data adalah kekuatan. Menguasai cara mengaturnya adalah langkah awal menjadi arsitek dunia digital."
    </blockquote>
    <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">— Modula Mission Log</p>
    <div class="pt-6 border-t border-white/10">
        <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">Sampai Jumpa di Misi 2: Dictionary & Key-Value Pairs!</p>
    </div>
</div>"""
    }
]

print(f"Generated Pilot Meeting 1 with {len(m1_streamlined_slides)} slides successfully.")
