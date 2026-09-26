# -*- coding: utf-8 -*-
"""Streamlined Meetings 6 and 7 for Level 2"""

def get_m6_slides():
    return [
        {
            "title": "Meeting 6: Colors & Pen Control 🎨",
            "subtitle": "Kuas Ajaib RGB & Efek Acak di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🌈</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 6</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Menguasai 16 Juta Warna Spektrum Cahaya!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Di Sesi 5, kita hanya menggunakan nama warna bahasa Inggris biasa (<code>"red"</code>, <code>"blue"</code>). Hari ini kita akan membuka laboratorium warna sejati: <b>Sistem RGB (Red, Green, Blue)</b>, efek stempel kilat (<code>stamp</code>), dan generator warna acak (<code>random</code>)!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <code>turtle.colormode(255)</code>, <code>bgcolor()</code>, <code>stamp()</code>, dan Pewarnaan Acak <code>random.randint()</code>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 6 🎯",
            "subtitle": "Target Penguasaan Warna & Kuas Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Sistem Spektrum Cahaya RGB (0–255)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami cara mencampur warna primer Red, Green, dan Blue untuk menghasilkan jutaan warna kustom.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Atmosfer Kanvas & Penataan Pena</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mewarnai latar belakang layar (<code>bgcolor</code>) dan membedakan warna garis vs warna isi (<code>color(pen, fill)</code>).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Kloning Instan dengan 'stamp()' & Teks Layar 'write()'</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mencetak jejak bentuk kura-kura secara instan tanpa harus menggambar ulang garis per garis.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Lukisan Hujan Bintang & Jam Dinding Modern</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mengombinasikan modul <code>random</code> untuk menghasilkan karya seni generatif yang unik.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 5 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Dasar Turtle",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak fungsi perintah Turtle berikut sebelum mulai:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. penup() vs pendown()</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">t.penup()<br>t.goto(100, 100)</div>
            <p class="text-slate-500">Angkat pena agar perpindahan tidak mencoret layar.</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. Ember Warna</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">t.begin_fill()<br>...<br>t.end_fill()</div>
            <p class="text-slate-500">Kunci pewarna bidang tertutup.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. Jendela Tetap Terbuka</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">turtle.done()</div>
            <p class="text-slate-500">Menjaga kanvas tidak langsung menghilang.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Laboratorium Warna: Sistem Spektrum RGB 🧪",
            "subtitle": "Tiga Angka Pengatur Cahaya: Red (0-255), Green (0-255), Blue (0-255)",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-yellow-400">import turtle</div>
        <div class="text-green-400">turtle.colormode(255) # WAJIB dipanggil agar bisa pakai angka 0-255!</div>
        <div class="text-cyan-300">t = turtle.Turtle()</div>
        <div class="text-purple-300">t.color(255, 105, 180) # Warna Pink Hot!</div>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center text-xs">
        <div class="p-2.5 bg-red-50 dark:bg-slate-800 rounded-xl border border-red-200 dark:border-slate-700 font-semibold text-red-700 dark:text-red-300">
            Merah Murni<br><span class="text-[10px] text-slate-500 font-mono">(255, 0, 0)</span>
        </div>
        <div class="p-2.5 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 font-semibold text-green-700 dark:text-green-300">
            Hijau Neon<br><span class="text-[10px] text-slate-500 font-mono">(0, 255, 0)</span>
        </div>
        <div class="p-2.5 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 font-semibold text-blue-700 dark:text-blue-300">
            Biru Laut<br><span class="text-[10px] text-slate-500 font-mono">(0, 150, 255)</span>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Atmosfer Kanvas & Dua Warna Berbeda 🌆",
            "subtitle": "bgcolor() dan color(garis, isi)",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. Latar Belakang (bgcolor)</b>
            <div class="text-yellow-400">turtle.bgcolor("midnightblue")</div>
            <p class="text-slate-400 text-[11px] mt-2">Mengubah seluruh warna kanvas layar, sangat cocok untuk suasana malam atau antariksa.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. Garis & Isi Berbeda</b>
            <div class="text-green-400">t.color("yellow", "red")</div>
            <p class="text-slate-400 text-[11px] mt-2">Argumen 1 adalah warna garis pena (kuning), argumen 2 adalah warna isi bidang (merah)!</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Jurus Kloning Kilat: t.stamp() 🥷",
            "subtitle": "Mencetak Cap Kura-kura Tanpa Mengetik Ulang Garis",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">t.shape("circle")</div>
        <div class="text-yellow-400">t.stamp() # Mencetak lingkaran di posisi ini!</div>
        <div class="text-slate-400">t.forward(50)</div>
        <div class="text-yellow-400">t.stamp() # Mencetak lingkaran kedua!</div>
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        💡 <b>Super Cepat:</b> Method <code>stamp()</code> mencetak bentuk kura-kura saat itu juga ke kanvas. Sangat efisien untuk membuat pola titik, bunga, jejak kaki, atau confetti!
    </div>
</div>"""
        },
        {
            "title": "Chaos Magic: Warna Acak dengan random 🎲",
            "subtitle": "Mengacak Tiga Nilai R, G, B Secara Otomatis",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-purple-400">import</span> <span class="text-cyan-400">turtle</span><br>
        <span class="text-purple-400">import</span> <span class="text-cyan-400">random</span><br><br>
        <span class="text-cyan-400">turtle</span>.<span class="text-yellow-400">colormode</span>(<span class="text-purple-300">255</span>)<br>
        <span class="text-yellow-400">t</span> = <span class="text-cyan-400">turtle</span>.<span class="text-green-400">Turtle</span>()<br><br>
        <span class="text-slate-400"># Gacha 3 angka dari 0 sampai 255</span><br>
        <span class="text-cyan-300">r</span> = <span class="text-cyan-400">random</span>.<span class="text-yellow-400">randint</span>(<span class="text-purple-300">0</span>, <span class="text-purple-300">255</span>)<br>
        <span class="text-cyan-300">g</span> = <span class="text-cyan-400">random</span>.<span class="text-yellow-400">randint</span>(<span class="text-purple-300">0</span>, <span class="text-purple-300">255</span>)<br>
        <span class="text-cyan-300">b</span> = <span class="text-cyan-400">random</span>.<span class="text-yellow-400">randint</span>(<span class="text-purple-300">0</span>, <span class="text-purple-300">255</span>)<br><br>
        <span class="text-yellow-400">t</span>.<span class="text-blue-400">color</span>(<span class="text-cyan-300">r</span>, <span class="text-cyan-300">g</span>, <span class="text-cyan-300">b</span>)
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Langit Malam Berbintang 🌌",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Langit Malam Bertabur Bintang Acak</span><br>
        import turtle, random<br>
        turtle.bgcolor("black")<br>
        t = turtle.Turtle()<br>
        t.speed(0)<br>
        t.hideturtle() # Sembunyikan badan turtle<br><br>
        for _ in range(20):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;x = random.randint(-200, 200)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;y = random.randint(-200, 200)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.penup()<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.goto(x, y)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.color("gold")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.dot(random.randint(5, 15))<br><br>
        turtle.done()
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Mengatasi Error Warna RGB 🐛",
            "subtitle": "Dua Kesalahan Paling Sering Terjadi di Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug 1: Lupa colormode(255)</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                t.color(255, 0, 0)<br>
                # TurtleGraphicsError: bad color sequence
            </div>
            <p class="text-slate-500">Secara default, turtle mengharapkan desimal 0.0 - 1.0. Wajib panggil <code>turtle.colormode(255)</code> terlebih dahulu!</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-amber-700 dark:text-amber-400 text-sm">🐛 Bug 2: Angka Melebihi 255</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-400">
                t.color(300, 100, 50) # ERROR!
            </div>
            <p class="text-slate-500">Nilai spektrum RGB hanya valid dari angka <b>0 hingga 255</b>.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Cahaya Bulan) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Bulan Sabit Bersinar</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Buatlah bulan purnama kuning di tengah layar dengan background hitam pekat, lalu buat ilusi bulan sabit dengan menumpuk lingkaran hitam di atasnya!
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Gunakan <code>turtle.bgcolor("#0a0a23")</code> untuk langit malam.</li>
            <li>Gambar lingkaran kuning terang dengan radius 70.</li>
            <li>Geser sedikit ke kanan, gambar lingkaran hitam kedua untuk menutupi sebagian badan bulan.</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ FINAL ART CHALLENGE: Galeri Warna ⚠️",
            "subtitle": "Pilih 1 dari 3 Karya Seni Modern Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🎨</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Uji Kemampuan Desain Visualmu!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-cyan-50 dark:bg-slate-800 border border-cyan-200 dark:border-slate-700">
            <span class="text-xl">💧</span>
            <b class="block mt-1 text-cyan-700 dark:text-cyan-300 font-bold">Challenge 1: Hujan Pelangi</b>
            <p class="text-slate-500 mt-1">Garis hujan vertikal dengan warna RGB acak berkilauan.</p>
        </div>
        <div class="p-4 rounded-xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700">
            <span class="text-xl">⏰</span>
            <b class="block mt-1 text-amber-700 dark:text-amber-300 font-bold">Challenge 2: Jam Modern</b>
            <p class="text-slate-500 mt-1">12 titik jam melingkar rapi menggunakan putaran stamp.</p>
        </div>
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🏙️</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 3: Siluet Kota</b>
            <p class="text-slate-500 mt-1">Gedung bertingkat warna-warni di bawah langit malam ungu.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Hujan Pelangi Vertikal 💧",
            "subtitle": "Mengombinasikan Loop, Random Position, dan Random RGB",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set background warna abu-abu gelap <code>"#111827"</code>.</li>
            <li>Gunakan looping 30 kali. Pada setiap putaran:</li>
            <li>Acak posisi X dan Y, acak nilai RGB <code>(r, g, b)</code>, lalu buat garis vertikal pendek sepanjang 30-50 pixel ke bawah!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Jam Dinding Modern ⏰",
            "subtitle": "Menggunakan stamp() dan Putaran 30 Derajat (360 / 12)",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set bentuk turtle <code>t.shape("circle")</code> dan beri warna emas.</li>
            <li>Ulangi 12 kali (untuk 12 angka jam):</li>
            <li>Maju 120 langkah (ke tepi), cetak stempel <code>t.stamp()</code>, mundur kembali ke tengah (0,0), lalu putar 30 derajat: <code>t.right(30)</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Siluet Kota Malam 🏙️",
            "subtitle": "Tantangan Pro: Gedung Bertingkat dengan Jendela Berpendar",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set background ungu tua malam hari <code>"#2e1065"</code>.</li>
            <li>Gambar 5 gedung berjajar dengan tinggi berbeda-beda menggunakan kotak hitam pekat.</li>
            <li>Beri titik-titik stempel kuning kecil di setiap gedung sebagai jendela lampu yang menyala!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 6 📝",
            "subtitle": "Rangkuman Senjata Warna & Kuas",
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
                    <td class="py-1.5 text-cyan-400">turtle.colormode(255)</td>
                    <td>Aktifkan mode angka RGB 0–255</td>
                    <td>Wajib sebelum memakai RGB</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">turtle.bgcolor(c)</td>
                    <td>Ubah warna latar kanvas</td>
                    <td><code>turtle.bgcolor("black")</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">t.color(pen, fill)</td>
                    <td>Warna garis dan warna isi berbeda</td>
                    <td><code>t.color("cyan", "navy")</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">t.stamp()</td>
                    <td>Cetak cap bentuk kura-kura di layar</td>
                    <td>Kloning instan tanpa garis</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai Palet Spektrum!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Dunia digital tersusun dari kombinasi Merah, Hijau, dan Biru. Sekarang kamu bisa menciptakan warna apa pun dari ketiadaan."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 7: <b>Turtle & Loops: Otomatisasi Poligon & Seni Geometri!</b>!
    </div>
</div>"""
        }
    ]

def get_m7_slides():
    return [
        {
            "title": "Meeting 7: Turtle & Loops 🔄",
            "subtitle": "Otomatisasi Pola & Seni Geometri di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🌀</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 7</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Menghentikan Capek Ngetik Copas!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Saat menggambar persegi, kita mengetik <code>forward</code> dan <code>right</code> sebanyak 4 kali. Bagaimana jika kita ingin menggambar segi-100 atau lingkaran raksasa? Apakah harus copy-paste 100 baris? Tentu tidak! Hari ini kita akan menggunakan kekuatan <b>For Loop</b> untuk menggambar pola kompleks dalam sekejap!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <b>For Loop</b> di Turtle, <b>Rumus Poligon 360 / N</b>, Variabel Counter <code>i</code>, dan <b>Nested Loop Spirograph</b>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 7 🎯",
            "subtitle": "Target Penguasaan Loop Visual Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Anatomi For Loop & Aturan Indentasi</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami cara komputer mengeksekusi blok kode berulang menggunakan <code>for _ in range(n):</code>.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Rumus Rahasia Poligon: 360° / Sisi</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menggambar segitiga, segi lima, segi enam, hingga lingkaran dengan rumus sudut matematis.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Pola Spiral Dinamis dengan Variabel Counter 'i'</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memanfaatkan nilai angka yang terus bertambah (0, 1, 2, ...) untuk membuat ilusi pusaran spiral membesar.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Spirograph Bunga & Mandala Art Otomatis</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menggabungkan Nested Loop untuk menciptakan ilusi optik geometris tingkat tinggi.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 6 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Warna & Kuas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak output kode visual berikut sebelum mulai:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. RGB Kuning</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">t.color(255, 255, 0)</div>
            <p class="text-slate-500">Campuran Merah + Hijau menghasilkan Kuning.</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. stamp() Cetak Cap</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">t.stamp()</div>
            <p class="text-slate-500">Meninggalkan stempel kura-kura di layar instan.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. Warna Background</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">turtle.bgcolor("black")</div>
            <p class="text-slate-500">Mengubah atmosfer layar jadi gelap.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Kuli vs Mesin: Kekuatan For Loop 🤖",
            "subtitle": "4 Baris Kode Menggantikan 100 Baris Manual",
            "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">😫</span>
            <b class="text-red-800 dark:text-red-300 text-sm">Manual (Bosan & Lelah)</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-red-400">
            t.forward(100)<br>t.right(90)<br>
            t.forward(100)<br>t.right(90)<br>
            t.forward(100)<br>t.right(90)<br>
            t.forward(100)<br>t.right(90)
        </div>
        <p class="text-xs text-slate-500">Bagaimana kalau mau gambar segi-36? Capek ngetik ratusan baris!</p>
    </div>
    <div class="p-5 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">⚡</span>
            <b class="text-green-800 dark:text-green-300 text-sm">For Loop (Elegan & Otomatis)</b>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-[11px] text-green-400">
            for _ in range(4):<br>
            &nbsp;&nbsp;&nbsp;&nbsp;t.forward(100)<br>
            &nbsp;&nbsp;&nbsp;&nbsp;t.right(90)
        </div>
        <p class="text-xs text-slate-500">Cukup 3 baris! Mau diulang 4 kali atau 1000 kali kodenya tetap seringkas ini.</p>
    </div>
</div>"""
        },
        {
            "title": "Rumus Rahasia Poligon: 360° / Sisi 📐",
            "subtitle": "Kunci Matematika Semua Bentuk Beraturan di Dunia",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">sisi = int(input("Mau segi berapa? "))</div>
        <div class="text-yellow-400">sudut = 360 / sisi # Rumus emas!</div>
        <div class="text-purple-300">for _ in range(sisi):</div>
        <div class="text-green-400 pl-4">t.forward(80)</div>
        <div class="text-green-400 pl-4">t.right(sudut)</div>
    </div>
    <div class="grid grid-cols-4 gap-2 text-center text-xs">
        <div class="p-2.5 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700">
            Segi-3 (Segitiga)<br><span class="text-blue-600 font-bold">360 / 3 = 120°</span>
        </div>
        <div class="p-2.5 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700">
            Segi-5 (Pentagon)<br><span class="text-green-600 font-bold">360 / 5 = 72°</span>
        </div>
        <div class="p-2.5 bg-amber-50 dark:bg-slate-800 rounded-xl border border-amber-200 dark:border-slate-700">
            Segi-6 (Hexagon)<br><span class="text-amber-600 font-bold">360 / 6 = 60°</span>
        </div>
        <div class="p-2.5 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700">
            Segi-36 (Lingkaran)<br><span class="text-purple-600 font-bold">360 / 36 = 10°</span>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Misteri Variabel Counter 'i': Pola Spiral 🌀",
            "subtitle": "Menggambar Garis yang Semakin Lama Semakin Panjang",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-yellow-400">for i in range(50):</div>
        <div class="text-green-400 pl-4">t.forward(i * 4) # Langkah bertambah: 0, 4, 8, 12, 16...</div>
        <div class="text-cyan-400 pl-4">t.right(91)     # Sudut sedikit miring dari 90°!</div>
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        🌀 <b>Efek Magis:</b> Karena sudut beloknya <code>91°</code> (bukan pas 90°), kotaknya tidak menutup sempurna melainkan berputar membentuk pusaran spiral hipnotis yang spektakuler!
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Jaring Laba-Laba Spiral 🕷️",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Spiral Jaring Laba-laba Cyber</span><br>
        import turtle<br>
        turtle.bgcolor("black")<br>
        t = turtle.Turtle()<br>
        t.speed(0)<br>
        t.color("cyan")<br><br>
        for i in range(60):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.forward(i * 3)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;t.left(59) # Belok hampir 60 derajat!<br><br>
        turtle.done()
    </div>
</div>"""
        },
        {
            "title": "Inception: Nested Loop (Loop di dalam Loop) 🪆",
            "subtitle": "Mengulang Gambar yang Berulang untuk Membuat Bunga",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-xs leading-relaxed border border-slate-700 shadow-xl">
        <span class="text-yellow-400">for kelopak in range(36):</span> <span class="text-slate-400"># Loop Luar: 36 Kelopak Bunga</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-purple-400">for sisi in range(4):</span> <span class="text-slate-400"># Loop Dalam: 1 Persegi Utuh</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-400">t.forward(100)</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-400">t.right(90)</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-cyan-400">t.right(10)</span> <span class="text-slate-400"># Putar sedikit kura-kura sebelum buat kelopak berikutnya!</span>
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        🌸 <b>Hasil Visual:</b> 36 persegi yang saling tumpang tindih berputar membentuk <b>Spirograph Bunga Geometri</b> yang sangat memukau!
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Indentasi For Loop Rusak 🐛",
            "subtitle": "Mengapa Gambarku Berantakan?",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug Indentasi:</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                for _ in range(4):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;t.forward(100)<br>
                t.right(90) # OOPS! Tidak menjorok!
            </div>
            <p class="text-slate-500">Karena <code>t.right(90)</code> ada di luar loop, turtle maju 400 langkah dulu, baru belok sekali!</p>
        </div>
        <div class="p-4 rounded-2xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-green-700 dark:text-green-400 text-sm">✅ Solusi Benar:</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">
                for _ in range(4):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;t.forward(100)<br>
                &nbsp;&nbsp;&nbsp;&nbsp;t.right(90) # Menjorok rapi
            </div>
            <p class="text-slate-500">Semua baris aksi yang ingin diulang wajib memiliki indentasi 4 spasi yang sama.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Bunga Kelopak Banyak) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Spirograph Lingkaran Emas</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Buatlah bunga spirograph menggunakan lingkaran (<code>circle</code>) yang berputar 360 derajat mengelilingi titik pusat.
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Set kecepatan maksimum: <code>t.speed(0)</code>.</li>
            <li>Buat for loop 24 kali putaran.</li>
            <li>Di setiap putaran: gambar lingkaran radius 60 dengan <code>t.circle(60)</code> lalu belokkan kura-kura sebesar 15 derajat (<code>360 / 24 = 15°</code>)!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ FINAL ART CHALLENGE: The Master Illusionist ⚠️",
            "subtitle": "Pilih 1 dari 3 Karya Geometri Spektakuler Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🌀</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Saatnya Membuat Ilusi Optik Spektakuler!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🌌</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 1: Blackhole</b>
            <p class="text-slate-500 mt-1">Pusaran spiral warna pelangi acak yang menghisap pandangan.</p>
        </div>
        <div class="p-4 rounded-xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700">
            <span class="text-xl">🏵️</span>
            <b class="block mt-1 text-amber-700 dark:text-amber-300 font-bold">Challenge 2: Mandala</b>
            <p class="text-slate-500 mt-1">Seni simetri suci India menggunakan kombinasi lingkaran & poligon.</p>
        </div>
        <div class="p-4 rounded-xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700">
            <span class="text-xl">🎆</span>
            <b class="block mt-1 text-green-700 dark:text-green-300 font-bold">Challenge 3: Kembang Api</b>
            <p class="text-slate-500 mt-1">Ledakan garis memancar 360 derajat lengkap dengan stamp bintang.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Pusaran Lubang Hitam (Blackhole) 🌌",
            "subtitle": "Kombinasi Variabel Counter 'i' dan Palet Warna Berganti",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set background hitam dan daftar warna: <code>warna = ["red", "purple", "blue", "green", "orange", "yellow"]</code>.</li>
            <li>Gunakan loop 120 kali dengan counter <code>i</code>:</li>
            <li>Pilih warna berdasarkan urutan: <code>t.color(warna[i % 6])</code>.</li>
            <li>Maju <code>t.forward(i * 2)</code> dan belok <code>t.left(59)</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Mandala Art Geometri 🏵️",
            "subtitle": "Nested Loop Segi Enam (Hexagon) Berputar",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set <code>t.speed(0)</code> dan <code>t.pensize(2)</code>.</li>
            <li>Loop luar 18 kali. Di dalam loop luar:</li>
            <li>Gunakan loop dalam 6 kali untuk menggambar 1 Hexagon (maju 80, belok 60°).</li>
            <li>Setelah hexagon selesai, putar kura-kura sebesar 20° (<code>360 / 18 = 20°</code>) untuk membuat kelopak berikutnya!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Ledakan Pesta Kembang Api 🎆",
            "subtitle": "Tantangan Pro: Garis Memancar Radian dengan Stamp Bintang",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set <code>turtle.bgcolor("black")</code> dan <code>t.shape("circle")</code>.</li>
            <li>Ulangi 36 kali:</li>
            <li>Maju 150 langkah dengan pena menempel (garis warna acak), cetak cap <code>t.stamp()</code> di ujung ledakan, angkat pena, kembali ke tengah <code>(0,0)</code>, lalu belok 10 derajat!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 7 📝",
            "subtitle": "Rangkuman For Loop & Rumus Geometri",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="overflow-x-auto">
        <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
            <thead>
                <tr class="border-b border-slate-200 dark:border-slate-700 font-bold text-slate-800 dark:text-white">
                    <th class="py-2">Pola / Konsep</th>
                    <th class="py-2">Rumus Kode</th>
                    <th class="py-2">Hasil Visual</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-[11px]">
                <tr>
                    <td class="py-1.5 text-cyan-400">Poligon Segi-N</td>
                    <td><code>sudut = 360 / N</code></td>
                    <td>Bentuk geometri teratur</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">Spiral Dinamis</td>
                    <td><code>t.forward(i * faktor)</code></td>
                    <td>Garis membesar seiring nilai i</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">Spirograph Bunga</td>
                    <td>Nested Loop (Luar kelopak, Dalam bentuk)</td>
                    <td>Bunga simetris multi kelopak</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">Rotasi Warna</td>
                    <td><code>list_warna[i % len(list_warna)]</code></td>
                    <td>Warna berputar tanpa index error</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai Otomatisasi Loop!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Komputer diciptakan bukan untuk menggantikan manusia, melainkan untuk membebaskan manusia dari pekerjaan berulang yang membosankan."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 8: <b>Advanced Nested Loops & Grid: Menuju Pixel Art 2D!</b>!
    </div>
</div>"""
        }
    ]
