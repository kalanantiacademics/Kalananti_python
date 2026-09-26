# -*- coding: utf-8 -*-
"""Streamlined Meetings 8 and 9 for Level 2"""

def get_m8_slides():
    return [
        {
            "title": "Meeting 8: Advanced Nested Loops & Grid 🏁",
            "subtitle": "Dari Geometri Menuju Pixel Art 2D di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">👾</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 8</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Dunia Komputer Adalah Susunan Grid!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Layar HP, monitor TV, papan catur, dan dunia game seperti Minecraft tersusun dari susunan kotak-kotak piksel 2D. Hari ini kita akan menjadi <b>Game Artist & Grid Engineer</b>: memetakan koordinat Baris & Kolom menggunakan Nested Loop untuk membuat Pixel Art!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <b>Grid Baris x Kolom</b>, Transformasi <code>(Row, Col) -> (X, Y)</code>, <b>Logika Papan Catur</b>, dan <b>Matrix List 2D</b>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 8 🎯",
            "subtitle": "Target Penguasaan Grid & Matriks Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Konsep Baris (Row) dan Kolom (Column)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami cara dua loop bersarang (nested loop) memindai seluruh petak layar secara sistematis.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Rumus Transformasi Matematika: (Row, Col) ke (X, Y)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menghitung posisi pixel kanvas: <code>x = col * ukuran</code> dan <code>y = -row * ukuran</code>.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Logika Selang-Seling Papan Catur (Ganjil / Genap)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memanfaatkan operator sisa bagi modulo <code>(row + col) % 2 == 0</code> untuk warna hitam-putih berselang.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Pixel Art Karakter Game (Minecraft Creeper)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Membaca data list 2D (Matrix blueprint) dan mencetaknya menjadi sprite game retro.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 7 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Nested Loop",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak total putaran dari kode loop berikut sebelum mulai:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. Total Putaran Nested</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">for r in range(4):<br>&nbsp;&nbsp;for c in range(5):</div>
            <p class="text-slate-500">Total putaran: <code>4 x 5 = 20 kali</code>!</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. Rumus Poligon</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">sudut = 360 / 6</div>
            <p class="text-slate-500">60 derajat untuk Segi Enam (Hexagon).</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. Variabel Counter</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">for i in range(10):</div>
            <p class="text-slate-500">Nilai <code>i</code> berjalan dari 0 sampai 9.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Dunia Adalah Grid: Baris x Kolom 📊",
            "subtitle": "Bagaimana Layar Komputer Menampilkan Gambar",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">for row in range(3):       # Baris: 0, 1, 2 (Atas ke Bawah)</div>
        <div class="text-yellow-400 pl-4">for col in range(3):   # Kolom: 0, 1, 2 (Kiri ke Kanan)</div>
        <div class="text-green-400 pl-8">print(f"Kotak ({row}, {col})")</div>
    </div>
    <div class="grid grid-cols-3 gap-2 text-center text-xs">
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 font-mono">(0, 0) | (0, 1) | (0, 2)</div>
        <div class="p-3 bg-indigo-50 dark:bg-slate-800 rounded-xl border border-indigo-200 dark:border-slate-700 font-mono">(1, 0) | (1, 1) | (1, 2)</div>
        <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 font-mono">(2, 0) | (2, 1) | (2, 2)</div>
    </div>
</div>"""
        },
        {
            "title": "Rumus Matematika: (Row, Col) ke (X, Y) 📐",
            "subtitle": "Mengubah Posisi Petak Menjadi Piksel Layar Turtle",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-xs leading-relaxed border border-slate-700 shadow-xl">
        <span class="text-yellow-400">UKURAN_KOTAK</span> = <span class="text-purple-300">40</span> <span class="text-slate-400"># Lebar setiap sel pixel</span><br><br>
        <span class="text-slate-400"># Rumus Konversi Koordinat Layar:</span><br>
        <span class="text-cyan-300">x</span> = <span class="text-yellow-400">col</span> * <span class="text-yellow-400">UKURAN_KOTAK</span> - <span class="text-purple-300">100</span><br>
        <span class="text-cyan-300">y</span> = <span class="text-purple-300">100</span> - (<span class="text-yellow-400">row</span> * <span class="text-yellow-400">UKURAN_KOTAK</span>)<br><br>
        <span class="text-yellow-400">t</span>.<span class="text-blue-400">penup</span>()<br>
        <span class="text-yellow-400">t</span>.<span class="text-blue-400">goto</span>(<span class="text-cyan-300">x</span>, <span class="text-cyan-300">y</span>)
    </div>
    <div class="p-3 bg-amber-50 dark:bg-slate-800 rounded-xl border border-amber-200 dark:border-slate-700 text-xs">
        💡 <b>Kenapa Y Bernilai Minus?</b> Karena di layar komputer, semakin ke bawah baris bertambah (Row 0, 1, 2), sedangkan di koordinat Kartesius nilai Y yang semakin ke bawah bernilai negatif!
    </div>
</div>"""
        },
        {
            "title": "Cetak Cepat dengan t.stamp() 🖨️",
            "subtitle": "Kotak Sempurna Tanpa Harus Menggambar 4 Sisi",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">t.shape("square")  # Gunakan bentuk kotak bawaan</div>
        <div class="text-yellow-400">t.shapesize(2)     # Ukuran 2 = 40x40 piksel</div>
        <div class="text-green-400">t.stamp()          # Cetak kotak instan dalam 0.001 detik!</div>
    </div>
    <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 text-xs">
        ⚡ <b>Rahasia Developer:</b> Menggunakan <code>stamp()</code> untuk Grid 100 kali lebih cepat daripada menggambar 4 garis manual di setiap petak!
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Papan Catur Hitam-Putih ♟️",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Papan Catur 4x4 Otomatis</span><br>
        import turtle<br>
        t = turtle.Turtle()<br>
        t.speed(0); t.shape("square"); t.shapesize(2); t.penup()<br><br>
        for row in range(4):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;for col in range(4):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = col * 42 - 80<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y = 80 - row * 42<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.goto(x, y)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">if (row + col) % 2 == 0:</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.color("black")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.color("lightgray")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t.stamp()<br><br>
        turtle.done()
    </div>
</div>"""
        },
        {
            "title": "Data Matrix 2D: List di dalam List 🗺️",
            "subtitle": "Menyimpan Desain Karakter Pixel Art dalam Kode",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-cyan-300 border border-slate-700 leading-relaxed">
        <span class="text-slate-400"># 0 = Hijau Rumput, 1 = Hitam Creeper</span><br>
        blueprint = [<br>
        &nbsp;&nbsp;&nbsp;&nbsp;[0, 1, 1, 0],<br>
        &nbsp;&nbsp;&nbsp;&nbsp;[1, 0, 0, 1],<br>
        &nbsp;&nbsp;&nbsp;&nbsp;[1, 1, 1, 1],<br>
        &nbsp;&nbsp;&nbsp;&nbsp;[1, 0, 0, 1]<br>
        ]<br><br>
        <span class="text-yellow-400">warna = blueprint[row][col]</span>
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        👾 <b>Inilah Asal Mula Game Retro:</b> Game legendaris seperti Mario Bros, Space Invaders, dan Pacman dibangun menggunakan Matrix 2D persis seperti ini!
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: Salah Indeks Grid Matrix 🐛",
            "subtitle": "Dua Kesalahan Paling Sering Terjadi di Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🐛 Bug 1: IndexError Matrix</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                blueprint[col][row] # TERBALIK!
            </div>
            <p class="text-slate-500">Urutan pemanggilan Matrix 2D selalu <b>[Baris][Kolom]</b>, bukan sebaliknya.</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-amber-700 dark:text-amber-400 text-sm">🐛 Bug 2: Gambar Tertumpuk di Satu Titik</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-400">
                t.goto(row, col) # Ukuran cuma 1 pixel!
            </div>
            <p class="text-slate-500">Wajib dikalikan dengan konstanta <code>UKURAN_KOTAK</code> agar setiap petak memiliki jarak.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Minecraft Creeper Face) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-green-500/20 text-green-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Pixel Art Wajah Creeper</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Rancanglah matrix 4x4 berisi wajah ikonik monster Creeper Minecraft menggunakan warna hijau cerah dan hitam.
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Tentukan petak mana yang berwarna hitam untuk mata dan mulut.</li>
            <li>Gunakan <code>t.shapesize(2)</code> dan <code>t.stamp()</code> untuk mencetak setiap blok piksel.</li>
            <li>Atur background hitam gelap agar karaktermu menyala!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ FINAL ART CHALLENGE: Grid Master ⚠️",
            "subtitle": "Pilih 1 dari 3 Karya Pixel Art Tingkat Tinggi Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🏁</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Tunjukkan Bakat Game Artist Kamu!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700">
            <span class="text-xl">🪜</span>
            <b class="block mt-1 text-blue-700 dark:text-blue-300 font-bold">Challenge 1: Tangga Langit</b>
            <p class="text-slate-500 mt-1">Grid segitiga di mana jumlah kolom bertambah per baris (row >= col).</p>
        </div>
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🕺</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 2: Lantai Disko</b>
            <p class="text-slate-500 mt-1">Papan grid 6x6 di mana setiap petak memiliki warna RGB acak.</p>
        </div>
        <div class="p-4 rounded-xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700">
            <span class="text-xl">👾</span>
            <b class="block mt-1 text-red-700 dark:text-red-300 font-bold">Challenge 3: Sprite Karakter</b>
            <p class="text-slate-500 mt-1">Desain monster alien 8x8 piksel penuh warna.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Tangga Menuju Langit 🪜",
            "subtitle": "Kondisi Logika: Hanya Cetak Petak Jika row >= col",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Buat nested loop <code>row in range(6)</code> dan <code>col in range(6)</code>.</li>
            <li>Gunakan kondisi <code>if col <= row:</code> untuk mencetak balok tangga warna biru terang.</li>
            <li>Hasilnya adalah tangga bertingkat piramida yang sangat rapi!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Lantai Dansa Disko 🕺",
            "subtitle": "Papan 6x6 Penuh Gemerlap Warna Cahaya RGB Acak",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Set <code>turtle.colormode(255)</code> dan background hitam.</li>
            <li>Di setiap petak grid 6x6, acak 3 nilai <code>r, g, b</code> antara 50 sampai 255.</li>
            <li>Beri warna petak tersebut dengan <code>t.color(r, g, b)</code> lalu cetak via <code>t.stamp()</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Game Sprite Karakter 8x8 👾",
            "subtitle": "Tantangan Pro: Membangun Karakter Game Retro",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Buat matrix <code>8x8</code> di mana angka 0 = transparan, 1 = tubuh alien, 2 = mata putih.</li>
            <li>Gunakan <code>t.shapesize(1.5)</code> agar ukuran karakter pas di tengah layar.</li>
            <li>Jalankan program dan saksikan kura-kura memindai dan mencetak karakter game retro buatanmu!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 8 📝",
            "subtitle": "Rangkuman Grid, Matriks, dan Koordinat",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="overflow-x-auto">
        <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
            <thead>
                <tr class="border-b border-slate-200 dark:border-slate-700 font-bold text-slate-800 dark:text-white">
                    <th class="py-2">Konsep</th>
                    <th class="py-2">Sintaks Kode</th>
                    <th class="py-2">Fungsi Utama</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-[11px]">
                <tr>
                    <td class="py-1.5 text-cyan-400">Scan Baris x Kolom</td>
                    <td><code>for r in range(H): for c in range(W):</code></td>
                    <td>Mengunjungi setiap sel grid</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">Hitung Piksel X, Y</td>
                    <td><code>x = c * size; y = -r * size</code></td>
                    <td>Transformasi koordinat layar</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">Logika Papan Catur</td>
                    <td><code>(row + col) % 2 == 0</code></td>
                    <td>Pola selang-seling genap-ganjil</td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">Akses Matrix 2D</td>
                    <td><code>matrix[row][col]</code></td>
                    <td>Ambil nilai sel pada baris & kolom</td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai Grid System!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Dari piksel-piksel sederhana, lahirlah dunia game yang tak terbatas. Kamu baru saja membuka pintu menuju game development sejati."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 9: <b>Brainstorming & Planning: Memulai Proyek Akhir Level 2!</b>!
    </div>
</div>"""
        }
    ]

def get_m9_slides():
    return [
        {
            "title": "Meeting 9: Brainstorming & Planning 🧠",
            "subtitle": "Merancang Capstone Project Final Level 2 di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🏰</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 9</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Saatnya Menjadi Arsitek Software Sejati!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Selamat! Kamu telah menguasai 8 kekuatan besar di Planet Modula: List, Dictionary, String Processing, File Handling, serta Turtle Graphics & Grid Art. Sekarang saatnya menggabungkan seluruh keahlianmu ke dalam <b>Karya Proyek Akhir Mandiri (Capstone Project)</b>!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Memilih <b>Jalur Proyek</b>, Menyusun <b>Game Design Document (GDD)</b>, Merancang <b>Flowchart</b> & <b>Pseudocode</b>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 9 🎯",
            "subtitle": "Target Perencanaan & Ideasi Proyek Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Mega-Flashback: Mengumpulkan Semua Senjata Modula</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memetakan kapan harus menggunakan List, Dict, String, File I/O, atau Turtle pada aplikasi nyata.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">3 Pilihan Jalur Proyek Akhir Sesuai Minat Siswa</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Track A: Turtle Art Gallery, Track B: Text RPG Adventure, atau Track C: Kasir Cafe & Student DB.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Teknik Rekayasa: Flowchart & Pseudocode</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Merancang alur logika program sebelum membuka editor kode agar tidak tersesat saat coding.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Hands-on: Menyelesaikan Proposal & Desain GDD</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Mendapatkan persetujuan guru untuk mulai coding di Sesi 10 & 11.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Mega-Flashback: 5 Senjata Utama Level 2 ⚔️",
            "subtitle": "Katalog Keahlian yang Bisa Kamu Gunakan di Proyekmu",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="grid grid-cols-2 gap-3">
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 space-y-1">
            <b class="text-blue-700 dark:text-blue-300 font-bold">1. List & Slicing</b>
            <p class="text-slate-500">Koleksi urutan: inventory tas, daftar nama skor, antrian antarmuka.</p>
        </div>
        <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 space-y-1">
            <b class="text-green-700 dark:text-green-300 font-bold">2. Dictionary Key-Value</b>
            <p class="text-slate-500">Database berlabel: biodata player, daftar harga menu, status monster RPG.</p>
        </div>
        <div class="p-3 bg-yellow-50 dark:bg-slate-800 rounded-xl border border-yellow-200 dark:border-slate-700 space-y-1">
            <b class="text-yellow-700 dark:text-yellow-300 font-bold">3. String Processing</b>
            <p class="text-slate-500">Filter input user, pembersih spasi, sensor chat, format teks rapi.</p>
        </div>
        <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 space-y-1">
            <b class="text-purple-700 dark:text-purple-300 font-bold">4. File Handling (.txt)</b>
            <p class="text-slate-500">Save & Load permanen: rekor highscore, catatan diary, riwayat transaksi.</p>
        </div>
    </div>
    <div class="p-3 bg-indigo-50 dark:bg-slate-800 rounded-xl border border-indigo-200 dark:border-slate-700 space-y-1">
        <b class="text-indigo-700 dark:text-indigo-300 font-bold">5. Turtle Graphics & Grid Art</b>
        <p class="text-slate-500">Visualisasi seni geometri, mandala, animasi warna RGB, dan peta pixel art 2D.</p>
    </div>
</div>"""
        },
        {
            "title": "3 Menu Pilihan Jalur Proyek Akhir 📜",
            "subtitle": "Pilih 1 Jalur yang Paling Sesuai Minat & Bakatmu",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left text-xs">
    <div class="p-4 rounded-2xl bg-cyan-50 dark:bg-slate-800 border border-cyan-200 dark:border-slate-700 space-y-1.5">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🎨</span>
            <b class="text-cyan-800 dark:text-cyan-300 text-sm">JALUR 1: Turtle Art Gallery & Interactive Visual</b>
        </div>
        <p class="text-slate-600 dark:text-slate-300">Pameran lukisan digital interaktif. User bisa memilih lukisan (Mandala, Pemandangan, atau Pixel Sprite) lewat input menu terminal.</p>
    </div>
    <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-1.5">
        <div class="flex items-center gap-2">
            <span class="text-2xl">⚔️</span>
            <b class="text-amber-800 dark:text-amber-300 text-sm">JALUR 2: Text RPG Dungeon Adventure</b>
        </div>
        <p class="text-slate-600 dark:text-slate-300">Game petualangan teks! Memiliki sistem pertarungan, inventory tas (List), status pemain (Dictionary), dan Save Game ke file teks.</p>
    </div>
    <div class="p-4 rounded-2xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 space-y-1.5">
        <div class="flex items-center gap-2">
            <span class="text-2xl">💼</span>
            <b class="text-green-800 dark:text-green-300 text-sm">JALUR 3: Smart Cafe Cashier & Student Database</b>
        </div>
        <p class="text-slate-600 dark:text-slate-300">Aplikasi manajemen kasir cafe atau database nilai murid dengan menu tambah data, hitung total otomatis, dan cetak struk ke file .txt!</p>
    </div>
</div>"""
        },
        {
            "title": "Mengapa Programmer Wajib Merencanakan? 📐",
            "subtitle": "Arsitek vs Kuli Bangunan Tanpa Gambar Kerja",
            "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="p-5 rounded-2xl bg-red-50 dark:bg-red-950/30 border border-red-200 dark:border-red-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">💥</span>
            <b class="text-red-800 dark:text-red-300 text-sm">Langsung Coding Tanpa Rencana</b>
        </div>
        <p class="text-xs text-slate-500">
            Di tengah jalan bingung variabelnya untuk apa, logika tabrakan, banyak bug, dan akhirnya malas melanjutkan karena kodenya berantakan!
        </p>
    </div>
    <div class="p-5 rounded-2xl bg-green-50 dark:bg-green-950/30 border border-green-200 dark:border-green-900/40 space-y-2">
        <div class="flex items-center gap-2">
            <span class="text-2xl">🏛️</span>
            <b class="text-green-800 dark:text-green-300 text-sm">Bikin Blueprint GDD Dulu</b>
        </div>
        <p class="text-xs text-slate-500">
            Semua alur input, variabel, dan fitur sudah jelas di atas kertas. Saat coding di Sesi 10-11, tinggal mengetik lancar tanpa rasa pusing!
        </p>
    </div>
</div>"""
        },
        {
            "title": "Merancang Alur dengan Flowchart 🔄",
            "subtitle": "Peta Diagram Jalan dari Awal Hingga Akhir",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid grid-cols-3 gap-3 text-center text-xs">
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700">
            <b class="text-blue-700 dark:text-blue-300">Oval (Terminator)</b><br>
            <span class="text-slate-500">Mulai (Start) & Selesai (End)</span>
        </div>
        <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700">
            <b class="text-green-700 dark:text-green-300">Jajargenjang (I/O)</b><br>
            <span class="text-slate-500">Input user & Print output</span>
        </div>
        <div class="p-3 bg-amber-50 dark:bg-slate-800 rounded-xl border border-amber-200 dark:border-slate-700">
            <b class="text-amber-700 dark:text-amber-300">Belah Ketupat (Decision)</b><br>
            <span class="text-slate-500">Percabangan <code>if-else</code> (Ya/Tidak)</span>
        </div>
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        💡 <b>Tips Guru:</b> Siswa bisa menggambar flowchart di kertas HVS atau Google Docs sebelum menulis kode program.
    </div>
</div>"""
        },
        {
            "title": "Pseudocode: Kode Versi Bahasa Manusia 👻",
            "subtitle": "Menulis Logika Tanpa Takut Salah Titik Koma",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 bg-slate-900 rounded-2xl font-mono text-xs leading-relaxed border border-slate-700 text-green-400">
        MULAI PROGRAM KASIR<br>
        1. Buat menu_harga dengan Dictionary {"Kopi": 15000, "Donat": 8000}<br>
        2. Tampilkan daftar menu ke layar<br>
        3. TANYA user: "Mau pesan apa?"<br>
        4. JIKA pesanan ada di menu_harga:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;Tambahkan ke keranjang<br>
        &nbsp;&nbsp;&nbsp;&nbsp;Simpan catatan ke file "struk.txt"<br>
        5. SELAIN ITU:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;Tampilkan pesan "Menu tidak tersedia"<br>
        SELESAI
    </div>
</div>"""
        },
        {
            "title": "Checklist Game Design Document (GDD) ✅",
            "subtitle": "Dokumen Sakti yang Harus Kamu Tuntaskan Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 space-y-2">
        <b class="text-sm text-slate-800 dark:text-white block font-bold">📋 Komponen Wajib GDD Siswa:</b>
        <ul class="space-y-1.5 text-slate-400 list-disc list-inside">
            <li><b>Nama Aplikasi / Game:</b> Judul karya yang keren dan unik.</li>
            <li><b>Jalur Terpilih:</b> Art Gallery / Text RPG / Kasir DB.</li>
            <li><b>Struktur Data Utama:</b> List apa saja dan Dictionary apa saja yang akan dipakai?</li>
            <li><b>3 Fitur Utama (Core MVP):</b> Fitur wajib yang harus jalan di Sesi 10.</li>
            <li><b>1 Fitur Ekstensi (Bonus Sandbox):</b> Ide kreatif tambahan jika waktu masih tersisa.</li>
            <li><b>File Storage:</b> Data apa yang akan disimpan ke dalam file <code>.txt</code>?</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "Exercise: Menyusun Proposal Desain Siswa 📝",
            "subtitle": "Waktu Diskusi & Konsultasi dengan Guru Kelas",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-3">
        <h4 class="text-base font-bold text-blue-900 dark:text-blue-300">Waktunya Curah Gagasan (Brainstorming)!</h4>
        <p class="text-xs text-slate-600 dark:text-slate-300 leading-relaxed">
            Ambil selembar kertas atau buka catatan digital. Tuliskan jawaban dari 6 pertanyaan checklist GDD. Guru akan berkeliling untuk mereview dan memberikan masukan teknis agar proyekmu realistis untuk diselesaikan dalam 2 sesi ke depan!
        </p>
        <div class="p-3 bg-white/50 dark:bg-black/30 rounded-xl text-xs text-slate-500 font-semibold">
            ⏳ Alokasi Waktu: 30 Menit Ideasi Mandiri + 15 Menit Review & Approval Guru.
        </div>
    </div>
</div>"""
        },
        {
            "title": "Persiapan Tempur Coding Sesi 10 🛠️",
            "subtitle": "Roadmap Pengerjaan 3 Sesi ke Depan",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700">
        <b class="text-blue-700 dark:text-blue-300 block text-sm">Sesi 10: Coding Phase 1 (Mekanik Inti)</b>
        <p class="text-slate-500 mt-1">Fokus membuat struktur data (List/Dict) dan logika utama jalan. Belum perlu memikirkan dekorasi yang rumit.</p>
    </div>
    <div class="p-3 bg-indigo-50 dark:bg-slate-800 rounded-xl border border-indigo-200 dark:border-slate-700">
        <b class="text-indigo-700 dark:text-indigo-300 block text-sm">Sesi 11: Coding Phase 2 (Polesan & Debugging)</b>
        <p class="text-slate-500 mt-1">Menyelesaikan fitur penyimpanan file, membasmi bug, dan mempercantik antarmuka program.</p>
    </div>
    <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700">
        <b class="text-green-700 dark:text-green-300 block text-sm">Sesi 12: The Grand Showcase & Graduation</b>
        <p class="text-slate-500 mt-1">Mempresentasikan hasil karya hebatmu di depan teman-teman kelas dan pelatih!</p>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 9 📝",
            "subtitle": "Rangkuman Fase Perencanaan Proyek",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">TAHAPAN SOFTWARE ENGINEERING:</div>
        <div class="text-slate-300">1. Ideation   -> Cari ide masalah & solusi</div>
        <div class="text-slate-300">2. Planning   -> GDD, Flowchart, Pseudocode</div>
        <div class="text-green-400">3. Coding     -> Mulai ketik kode di Sesi 10</div>
        <div class="text-yellow-400">4. Testing    -> Debugging & perbaikan di Sesi 11</div>
        <div class="text-purple-400">5. Showcase   -> Presentasi karya di Sesi 12</div>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Proposalmu Siap, Petualangan Capstone Dimulai!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Jika kamu gagal merencanakan, kamu sedang merencanakan kegagalan. Cetak birumu sudah selesai, saatnya mewujudkan karya impianmu!"
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 10: <b>Coding Phase 1 (Membangun Pondasi Mekanik Inti)</b>!
    </div>
</div>"""
        }
    ]
