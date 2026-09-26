# -*- coding: utf-8 -*-
"""Generate Meeting 9 for level3/deck.html"""

m9_slides = [
    {
        "title": "Meeting 9: Rancang Aplikasi Impianmu 🎨",
        "subtitle": "Flashback, Ideasi & Wireframe Proyek Akhir",
        "content": """<div class="text-center max-w-4xl mx-auto space-y-6">
    <div class="text-6xl animate-bounce">🚀</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Tahap Akhir Level 3 • Sesi 9-12</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Selamat Datang di Fase Proyek Akhir!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Selama 8 pertemuan, kalian sudah menguasai fondasi pembuatan aplikasi desktop dengan <b>CustomTkinter</b>. Mulai hari ini, kalian bukan lagi sekadar menyalin kode guru, melainkan menjadi <b>Software Creator</b> yang merancang, membangun, dan memamerkan aplikasi buatan kalian sendiri!
    </p>
    <div class="grid sm:grid-cols-3 gap-4 pt-4">
        <div class="bg-blue-50 dark:bg-slate-800/80 p-4 rounded-2xl border border-blue-200 dark:border-slate-700 text-center">
            <div class="text-3xl mb-2">💡</div>
            <div class="font-bold text-slate-800 dark:text-white text-sm">Sesi 9: Ideasi & Wireframe</div>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Rancang ide, tema, dan sketsa antarmuka</p>
        </div>
        <div class="bg-indigo-50 dark:bg-slate-800/80 p-4 rounded-2xl border border-indigo-200 dark:border-slate-700 text-center">
            <div class="text-3xl mb-2">📐</div>
            <div class="font-bold text-slate-800 dark:text-white text-sm">Sesi 10: UI Layouting</div>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Bangun seluruh tampilan visual (Front-End)</p>
        </div>
        <div class="bg-green-50 dark:bg-slate-800/80 p-4 rounded-2xl border border-green-200 dark:border-slate-700 text-center">
            <div class="text-3xl mb-2">⚡</div>
            <div class="font-bold text-slate-800 dark:text-white text-sm">Sesi 11-12: Logic & Showcase</div>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1">Hubungkan fungsi logika dan presentasi karya</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Flashback Materi GUI (Sesi 1–8) ⏪",
        "subtitle": "Peralatan Tempur yang Sudah Kita Kuasai",
        "content": """<div class="max-w-4xl mx-auto space-y-6">
    <p class="text-center text-slate-600 dark:text-slate-300 text-lg">Sebelum memilih proyek, mari ingat kembali "senjata" koding yang sudah ada di inventaris kita:</p>
    <div class="grid sm:grid-cols-2 md:grid-cols-4 gap-4 text-center">
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl shadow-sm">
            <div class="text-4xl mb-3">🪟</div>
            <h4 class="font-bold text-slate-800 dark:text-white">Window & Theme</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1"><code>app = ctk.CTk()</code>, title, geometry, dark/light mode</p>
        </div>
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl shadow-sm">
            <div class="text-4xl mb-3">🔤</div>
            <h4 class="font-bold text-slate-800 dark:text-white">Widget Dasar</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1"><code>CTkLabel</code> (teks), <code>CTkButton</code> (tombol), <code>CTkEntry</code> (input teks)</p>
        </div>
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl shadow-sm">
            <div class="text-4xl mb-3">📊</div>
            <h4 class="font-bold text-slate-800 dark:text-white">Tata Letak</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1"><code>.pack()</code> untuk tumpukan rapi & <code>.grid()</code> untuk baris-kolom teratur</p>
        </div>
        <div class="bg-white/5 border border-white/10 p-5 rounded-2xl shadow-sm">
            <div class="text-4xl mb-3">⚡</div>
            <h4 class="font-bold text-slate-800 dark:text-white">Event & Logic</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1"><code>command=fungsi</code>, <code>.get()</code>, <code>.configure()</code>, dan <code>try-except</code></p>
        </div>
    </div>
    <div class="bg-blue-50 dark:bg-blue-900/30 p-4 rounded-xl border border-blue-200 dark:border-blue-700/50 text-center">
        <p class="text-sm text-blue-900 dark:text-blue-200 font-semibold">💡 Semua proyek akhir yang hebat dibangun hanya dari kombinasi 4 pilar di atas!</p>
    </div>
</div>"""
    },
    {
        "title": "Mini Quiz Flashback 🧠",
        "subtitle": "Pemanasan Ideasi",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-5xl">🧐</div>
    <p class="font-semibold text-slate-800 dark:text-white text-xl">Mengapa seorang programmer profesional selalu membuat <b>Wireframe (Sketsa Layar)</b> sebelum mulai mengetik baris kode?</p>
    <div class="grid grid-cols-1 gap-3">
        <button onclick="showMiniFeedback('fb-m9-quiz', 'Kurang tepat! Komputer tidak butuh gambar kertas untuk membaca syntax Python.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">A. Agar komputer otomatis membaca gambar kertas menjadi kode Python.</button>
        <button onclick="showMiniFeedback('fb-m9-quiz', 'Tepat Sekali! Wireframe memandu kita mengetahui komponen apa saja yang dibutuhkan dan tata letaknya, sehingga koding menjadi terarah dan bebas revisi bongkar-pasang.', 'success')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-green-400 transition-all text-left text-sm">B. Mengetahui posisi widget dan alur tombol terlebih dahulu, sehingga koding lebih terarah dan tidak buang waktu bongkar-pasang.</button>
        <button onclick="showMiniFeedback('fb-m9-quiz', 'Salah! Wireframe bukan untuk memilih warna background saja.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">C. Hanya sebagai formalitas agar buku catatan terlihat rapi.</button>
    </div>
    <div id="fb-m9-quiz" class="min-h-[48px] mt-4"></div>
</div>"""
    },
    {
        "title": "Objectives Misi 9 🎯",
        "subtitle": "Target Kita Hari Ini",
        "content": """<div class="max-w-3xl mx-auto space-y-6">
    <ul class="space-y-4 text-left">
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Memilih 1 Track Proyek Resmi (SSOT1)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Memilih di antara Unit Converter, Login System, atau To-Do List Lite (atau Weather App bagi yang siap tantangan lanjutan).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menentukan Target Pengguna & Solusi Aplikasi</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Menjelaskan aplikasi ini dibuat untuk siapa dan membantu memecahkan masalah apa.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Merancang Sketsa Antarmuka (Wireframe UI)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Memetakan 3 zona utama antarmuka: Header, Form Input, dan Hasil/Aksi.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menyusun 3 Fitur Core MVP (Minimum Viable Product)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Menentukan 3 fungsi wajib yang harus berhasil berjalan sebelum menambah fitur bonus.</p>
            </div>
        </li>
    </ul>
</div>"""
    },
    {
        "title": "Mindset Software Creator 💡",
        "subtitle": "Bukan Sekadar Menjiplak Kode",
        "content": """<div class="grid md:grid-cols-2 gap-8 items-center max-w-4xl mx-auto">
    <div class="space-y-4 text-left">
        <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Kamu yang Pegang Kendali!</h3>
        <p class="text-slate-600 dark:text-slate-300">
            Di sesi latihan sebelumnya, semua orang membuat tombol dan warna yang sama sesuai instruksi guru. Namun di Proyek Akhir ini:
        </p>
        <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-300 list-disc pl-5">
            <li><b>Nama aplikasi</b> kamu yang tentukan sendiri.</li>
            <li><b>Palet warna & tema</b> (Dark / Light / Blue / Green) bebas kamu pilih.</li>
            <li><b>Kata-kata pesan dan tombol</b> bisa disesuaikan dengan gaya pribadimu.</li>
            <li><b>Fitur unik</b> bisa kamu tambahkan lewat menu <i>Creative Sandbox</i>.</li>
        </ul>
    </div>
    <div class="bg-gradient-to-br from-blue-500/10 to-indigo-500/10 border border-blue-500/20 p-6 rounded-3xl text-center">
        <div class="text-6xl mb-3">🎨</div>
        <h4 class="font-bold text-blue-600 dark:text-blue-400 text-lg">Karya Orisinil</h4>
        <p class="text-xs text-slate-500 dark:text-slate-400 mt-2">Dua murid yang memilih tema sama bisa menghasilkan aplikasi dengan wajah dan rasa yang sama sekali berbeda!</p>
    </div>
</div>"""
    },
    {
        "title": "Tiga Pilihan Core Project Track 🚀",
        "subtitle": "Pilih Sesuai Minat & Imu",
        "content": """<div class="max-w-4xl mx-auto space-y-4">
    <p class="text-center text-slate-600 dark:text-slate-300">Silabus resmi Kalananti menyediakan 3 Track Proyek Inti yang 100% bisa diselesaikan offline tanpa koneksi internet:</p>
    <div class="grid md:grid-cols-3 gap-4 text-left">
        <div class="bg-blue-50/50 dark:bg-slate-800/80 border border-blue-200 dark:border-blue-900/40 p-5 rounded-2xl flex flex-col justify-between">
            <div>
                <div class="text-3xl mb-2">🔄</div>
                <div class="font-extrabold text-blue-800 dark:text-blue-300 text-base">Track 1: Unit Converter</div>
                <p class="text-xs text-slate-600 dark:text-slate-400 mt-2">Aplikasi pengubah satuan: Suhu (C ke F), Jarak (Km ke Meter), atau Mata Uang (IDR ke USD).</p>
                <div class="mt-3 text-[11px] font-mono text-blue-600 dark:text-blue-400">Entry • Math Formula • Result Label</div>
            </div>
            <div class="mt-4 pt-3 border-t border-blue-200/60 dark:border-slate-700 text-xs font-semibold text-blue-700 dark:text-blue-300">Cocok untuk: Suka angka & sains</div>
        </div>
        <div class="bg-amber-50/50 dark:bg-slate-800/80 border border-amber-200 dark:border-amber-900/40 p-5 rounded-2xl flex flex-col justify-between">
            <div>
                <div class="text-3xl mb-2">🔐</div>
                <div class="font-extrabold text-amber-800 dark:text-amber-300 text-base">Track 2: Login System</div>
                <p class="text-xs text-slate-600 dark:text-slate-400 mt-2">Sistem autentikasi gerbang rahasia dengan username, password berbintang (*), dan verifikasi status.</p>
                <div class="mt-3 text-[11px] font-mono text-amber-600 dark:text-amber-400">2x Entry • show="*" • If-Else Dict</div>
            </div>
            <div class="mt-4 pt-3 border-t border-amber-200/60 dark:border-slate-700 text-xs font-semibold text-amber-700 dark:text-amber-300">Cocok untuk: Suka game vault & security</div>
        </div>
        <div class="bg-green-50/50 dark:bg-slate-800/80 border border-green-200 dark:border-green-900/40 p-5 rounded-2xl flex flex-col justify-between">
            <div>
                <div class="text-3xl mb-2">📋</div>
                <div class="font-extrabold text-green-800 dark:text-green-300 text-base">Track 3: To-Do List Lite</div>
                <p class="text-xs text-slate-600 dark:text-slate-400 mt-2">Aplikasi pencatat misi harian/tugas sekolah: ketik tugas, klik simpan, dan tampilkan ke layar.</p>
                <div class="mt-3 text-[11px] font-mono text-green-600 dark:text-green-400">Entry • List Display • Reset Button</div>
            </div>
            <div class="mt-4 pt-3 border-t border-green-200/60 dark:border-slate-700 text-xs font-semibold text-green-700 dark:text-green-300">Cocok untuk: Suka produktivitas & checklist</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Track 1 Spotlight: Unit Converter 🔄",
        "subtitle": "Kalkulator Konversi Cerdas",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Preview Target Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Cara Kerja Unit Converter</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Pengguna memasukkan nilai di kotak input, memilih jenis konversi, menekan tombol, dan aplikasi langsung menghitung serta menampilkan hasil yang rapi.</p>
        <div class="bg-slate-100 dark:bg-slate-800 p-3 rounded-xl text-xs space-y-1">
            <p><b>Fitur MVP 1:</b> Menerima angka dari <code>CTkEntry</code></p>
            <p><b>Fitur MVP 2:</b> Menghitung rumus: <code>(C * 9/5) + 32</code></p>
            <p><b>Fitur MVP 3:</b> Validasi: cegah error jika user mengetik huruf</p>
        </div>
    </div>
    <div class="mock-window w-full max-w-sm">
        <div class="mock-window-header">
            <div class="mock-window-title">ThermoConvert Pro</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content space-y-3">
            <div class="text-center font-bold text-cyan-400 text-sm">🌡️ Konverter Celcius ke Fahrenheit</div>
            <div>
                <label class="text-[10px] text-slate-400 block mb-1">Derajat Celcius:</label>
                <div class="p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-sm text-white font-mono">100</div>
            </div>
            <div class="w-full py-2 bg-blue-600 rounded-lg text-center text-white font-bold text-xs">Hitung Fahrenheit ⚡</div>
            <div class="p-3 bg-[#172554] rounded-lg border border-blue-500/40 text-center">
                <div class="text-[10px] text-blue-300">Hasil:</div>
                <div class="text-xl font-extrabold text-white font-mono">212.0 °F</div>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Track 2 Spotlight: Login System 🔐",
        "subtitle": "Gerbang Keamanan Rahasia",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Preview Target Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Cara Kerja Login System</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Pengguna memasukkan username dan password. Password terlindungi dengan sensor bintang <code>*</code>. Aplikasi mengecek apakah kredensial cocok dengan database contoh.</p>
        <div class="bg-slate-100 dark:bg-slate-800 p-3 rounded-xl text-xs space-y-1">
            <p><b>Fitur MVP 1:</b> Input User & Password masked (<code>show="*"</code>)</p>
            <p><b>Fitur MVP 2:</b> Pengecekan data benar/salah via <code>if/else</code></p>
            <p><b>Fitur MVP 3:</b> Label status feedback warna (Hijau/Merah) + Tombol Reset</p>
        </div>
    </div>
    <div class="mock-window w-full max-w-sm">
        <div class="mock-window-header">
            <div class="mock-window-title">CyberVault Guardian</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content space-y-3">
            <div class="text-center font-bold text-amber-400 text-sm">🛡️ Security Gateway</div>
            <div class="space-y-2">
                <div class="p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-white">Username: agent_kalananti</div>
                <div class="p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-white">Password: ••••••••</div>
            </div>
            <div class="flex gap-2">
                <div class="flex-1 py-2 bg-green-600 rounded-lg text-center text-white font-bold text-xs">Masuk Portal 🔓</div>
                <div class="px-3 py-2 bg-slate-700 rounded-lg text-center text-slate-300 font-bold text-xs">Clear</div>
            </div>
            <div class="p-2 bg-green-950/60 rounded-lg border border-green-500/40 text-center text-green-300 text-xs font-bold">
                ✅ Akses Diterima! Selamat Datang, Agent.
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Track 3 Spotlight: To-Do List Lite 📋",
        "subtitle": "Pengingat Misi Harian",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Preview Target Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Cara Kerja To-Do List Lite</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Ketik nama misi atau tugas baru, tekan tombol Tambah, dan teks tugas akan otomatis masuk ke papan daftar. Dilengkapi tombol reset untuk membersihkan papan.</p>
        <div class="bg-slate-100 dark:bg-slate-800 p-3 rounded-xl text-xs space-y-1">
            <p><b>Fitur MVP 1:</b> Kotak input teks tugas baru</p>
            <p><b>Fitur MVP 2:</b> Menampilkan daftar tugas yang bertambah</p>
            <p><b>Fitur MVP 3:</b> Validasi cegah input kosong & Tombol Reset</p>
        </div>
    </div>
    <div class="mock-window w-full max-w-sm">
        <div class="mock-window-header">
            <div class="mock-window-title">DailyQuest Manager</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content space-y-3">
            <div class="text-center font-bold text-indigo-400 text-sm">📝 Daftar Misi Hari Ini</div>
            <div class="flex gap-2">
                <div class="flex-1 p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-300">Belajar Python GUI...</div>
                <div class="px-3 py-2 bg-indigo-600 rounded-lg text-white font-bold text-xs">+ Tambah</div>
            </div>
            <div class="p-3 bg-[#1e293b] rounded-lg border border-slate-700 space-y-1 text-xs">
                <div class="text-slate-200">1. 🚀 Selesaikan latihan Tkinter</div>
                <div class="text-slate-200">2. 💻 Bikin wireframe proyek</div>
                <div class="text-slate-400">3. 📖 Baca materi Sesi 10</div>
            </div>
            <div class="w-full py-1.5 bg-red-600/30 border border-red-500/40 rounded-lg text-center text-red-300 text-xs font-semibold">
                Reset Semua Misi 🧹
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Optional Advanced Track: Weather App 🌦️",
        "subtitle": "Tantangan Integrasi Data Eksternal",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="inline-block px-3 py-1 bg-purple-100 text-purple-800 dark:bg-purple-900/50 dark:text-purple-300 rounded-full font-bold text-[10px] uppercase tracking-widest border border-purple-300 dark:border-purple-700">Optional Advanced Track</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Bagi yang Ingin Tantangan Lebih!</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Jika kamu merasa cepat menguasai materi dan ingin mencoba mengambil data dari internet (API) atau data simulasi cuaca kota-kota di dunia.</p>
        <div class="bg-purple-50 dark:bg-purple-950/40 p-3 rounded-xl border border-purple-200 dark:border-purple-800/40 text-xs space-y-1">
            <p><b>Syarat:</b> Core UI sudah selesai dan paham dictionary.</p>
            <p><b>Catatan Aman:</b> Tersedia mode offline (data tiruan) jika tidak ada koneksi internet!</p>
        </div>
    </div>
    <div class="mock-window w-full max-w-sm">
        <div class="mock-window-header">
            <div class="mock-window-title">Live Weather Radar</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content space-y-3 text-center">
            <div class="flex gap-2">
                <div class="flex-1 p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-white text-left">Jakarta</div>
                <div class="px-3 py-2 bg-blue-600 rounded-lg text-white font-bold text-xs">Cari 🔍</div>
            </div>
            <div class="p-3 bg-[#1e3a8a]/60 rounded-xl border border-blue-400/30">
                <div class="text-4xl mb-1">⛅</div>
                <div class="text-2xl font-black text-white font-mono">31.5 °C</div>
                <div class="text-xs text-blue-200 font-semibold mt-1">Berawan Sebagian • Jakarta</div>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Konsep 1: Dekomposisi UI (3 Zona Kunci) 🧩",
        "subtitle": "Memecah Kerumitan Layar Menjadi 3 Blok",
        "content": """<div class="max-w-4xl mx-auto space-y-6">
    <p class="text-center text-slate-600 dark:text-slate-300 text-base">Semua aplikasi desktop di dunia dibangun dengan membagi layar menjadi 3 Zona Utama:</p>
    <div class="grid md:grid-cols-3 gap-4 text-center">
        <div class="bg-blue-50 dark:bg-slate-800 p-5 rounded-2xl border-2 border-blue-300 dark:border-blue-700">
            <div class="text-3xl mb-2">🏷️</div>
            <h4 class="font-bold text-blue-700 dark:text-blue-300">1. Zona Header</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-2">Berisi judul aplikasi, icon/logo, dan instruksi singkat untuk pengguna.</p>
            <div class="mt-3 text-[11px] font-mono text-slate-600 dark:text-slate-300 bg-white dark:bg-black/30 p-2 rounded">CTkLabel (Title)</div>
        </div>
        <div class="bg-indigo-50 dark:bg-slate-800 p-5 rounded-2xl border-2 border-indigo-300 dark:border-indigo-700">
            <div class="text-3xl mb-2">⌨️</div>
            <h4 class="font-bold text-indigo-700 dark:text-indigo-300">2. Zona Input</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-2">Tempat user memasukkan teks, angka, password, atau memilih opsi.</p>
            <div class="mt-3 text-[11px] font-mono text-slate-600 dark:text-slate-300 bg-white dark:bg-black/30 p-2 rounded">CTkEntry / CTkOptionMenu</div>
        </div>
        <div class="bg-green-50 dark:bg-slate-800 p-5 rounded-2xl border-2 border-green-300 dark:border-green-700">
            <div class="text-3xl mb-2">🎯</div>
            <h4 class="font-bold text-green-700 dark:text-green-300">3. Zona Aksi & Hasil</h4>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-2">Tombol pemicu eksekusi dan label penampil output/feedback hasil kerja.</p>
            <div class="mt-3 text-[11px] font-mono text-slate-600 dark:text-slate-300 bg-white dark:bg-black/30 p-2 rounded">CTkButton + CTkLabel (Result)</div>
        </div>
    </div>
    <p class="text-center text-xs text-slate-400">Teknik dekomposisi ini membuat layouting di Sesi 10 menjadi sangat mudah dan terstruktur!</p>
</div>"""
    },
    {
        "title": "Konsep 2: Apa itu Core MVP? 🧱",
        "subtitle": "Minimum Viable Product",
        "content": """<div class="grid md:grid-cols-2 gap-8 items-center max-w-4xl mx-auto">
    <div class="space-y-4 text-left">
        <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Aturan Emas: MVP Dulu!</h3>
        <p class="text-slate-600 dark:text-slate-300">
            <b>MVP</b> adalah versi paling sederhana dari aplikasimu yang <b>sudah bisa berfungsi 100%</b> tanpa error.
        </p>
        <div class="p-4 bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/40 rounded-2xl text-xs space-y-2">
            <p class="font-bold text-amber-800 dark:text-amber-300">⚠️ Kesalahan Terbesar Pemula:</p>
            <p class="text-slate-600 dark:text-slate-400">Ingin membuat 10 fitur sekaligus, memasang puluhan gambar, tapi tombol utamanya malah tidak berfungsi atau aplikasi sering crash!</p>
        </div>
        <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">
            Kuncinya: Selesaikan 3 Fitur Core MVP terlebih dahulu. Jika waktu masih ada, baru tambahkan fitur bonus!
        </p>
    </div>
    <div class="bg-white/5 border border-white/10 p-6 rounded-3xl text-center space-y-4">
        <div class="text-5xl">🎯</div>
        <h4 class="font-bold text-slate-800 dark:text-white">Target 3 Fitur Core MVP</h4>
        <div class="space-y-2 text-xs text-left">
            <div class="p-2.5 bg-green-500/10 border border-green-500/30 rounded-xl text-green-700 dark:text-green-300 font-semibold">1. Input: Bisa menerima ketikan pengguna</div>
            <div class="p-2.5 bg-blue-500/10 border border-blue-500/30 rounded-xl text-blue-700 dark:text-blue-300 font-semibold">2. Process: Tombol memicu fungsi perhitungan/logika</div>
            <div class="p-2.5 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-indigo-700 dark:text-indigo-300 font-semibold">3. Output: Layar memperbarui hasil secara dinamis</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Menu Creative Sandbox 🎨",
        "subtitle": "Katalog Fitur Tambahan Personal",
        "content": """<div class="max-w-4xl mx-auto space-y-5">
    <p class="text-center text-slate-600 dark:text-slate-300">Setelah 3 fitur Core MVP selesai, kalian bebas memilih 1–2 fitur ekspansi dari menu sandbox ini:</p>
    <div class="grid sm:grid-cols-2 md:grid-cols-4 gap-3 text-center">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-1">🌗</div>
            <b class="text-xs text-slate-800 dark:text-white">Theme Switcher</b>
            <p class="text-[11px] text-slate-400 mt-1">Tombol toggle ganti Dark / Light mode saat aplikasi jalan</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-1">🧹</div>
            <b class="text-xs text-slate-800 dark:text-white">One-Click Reset</b>
            <p class="text-[11px] text-slate-400 mt-1">Tombol reset instan yang mengosongkan semua kolom input</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-1">🌈</div>
            <b class="text-xs text-slate-800 dark:text-white">Dynamic Color</b>
            <p class="text-[11px] text-slate-400 mt-1">Warna hasil berubah (Merah jika panas, Hijau jika berhasil)</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-1">🛡️</div>
            <b class="text-xs text-slate-800 dark:text-white">Smart Validator</b>
            <p class="text-[11px] text-slate-400 mt-1">Pesan peringatan ramah jika user memasukkan data aneh</p>
        </div>
    </div>
    <div class="text-center text-xs text-slate-400 italic">Pilihlah fitur yang membuat aplikasimu paling unik dan menyenangkan untuk dipresentasikan!</div>
</div>"""
    },
    {
        "title": "Dari Sketsa ke Kode (Wireframe to UI) ✏️",
        "subtitle": "Bagaimana Gambar Menjadi Kode CustomTkinter",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="p-5 rounded-2xl bg-amber-50 dark:bg-slate-800 border-2 border-dashed border-amber-300 dark:border-amber-700 text-center space-y-3">
        <span class="text-xs font-bold text-amber-700 dark:text-amber-300 uppercase tracking-widest">Sketsa Wireframe Kertas</span>
        <div class="p-3 bg-white dark:bg-slate-900 rounded-xl border border-slate-300 text-left font-mono text-xs space-y-2">
            <div class="p-2 border border-slate-400 text-center font-bold">[ JUDUL APLIKASI ]</div>
            <div class="p-2 border border-slate-400 text-slate-500">[ Kotak Input Data ... ]</div>
            <div class="p-2 bg-slate-200 dark:bg-slate-800 text-center font-bold">[ TOMBOL AKSI ]</div>
            <div class="p-3 border border-slate-400 text-center font-bold text-blue-500">[ HASIL AKAN MUNCUL DI SINI ]</div>
        </div>
        <p class="text-xs text-slate-500">Gambar kotak sederhana di buku tulismu!</p>
    </div>
    <div class="p-5 rounded-2xl bg-slate-900 border border-slate-700 text-left font-mono text-xs text-green-400 space-y-2">
        <span class="text-xs font-bold text-blue-400 uppercase tracking-widest block font-sans">Kode Python CustomTkinter</span>
        <p><span class="text-slate-500"># 1. Judul</span><br>label_judul = ctk.CTkLabel(app, text="Judul")</p>
        <p><span class="text-slate-500"># 2. Kotak Input</span><br>entry_data = ctk.CTkEntry(app)</p>
        <p><span class="text-slate-500"># 3. Tombol</span><br>btn_aksi = ctk.CTkButton(app, text="Hitung")</p>
        <p><span class="text-slate-500"># 4. Label Hasil</span><br>label_hasil = ctk.CTkLabel(app, text="---")</p>
    </div>
</div>"""
    },
    {
        "title": "Workshop Tahap 1: Identitas Proyek 🏷️",
        "subtitle": "Nama Aplikasi & Target Pengguna",
        "content": """<div class="max-w-2xl mx-auto space-y-5 text-left">
    <div class="bg-white/5 border border-white/10 p-6 rounded-2xl space-y-4">
        <h4 class="font-bold text-lg text-slate-800 dark:text-white">Lembar Kerja 1: Identitas Aplikasi</h4>
        <div class="space-y-3 text-sm">
            <div>
                <label class="block font-semibold text-slate-700 dark:text-slate-300 mb-1">1. Track yang Dipilih:</label>
                <div class="text-xs text-slate-500">Pilih: [Unit Converter] / [Login System] / [To-Do List Lite] / [Weather App]</div>
            </div>
            <div>
                <label class="block font-semibold text-slate-700 dark:text-slate-300 mb-1">2. Nama Keren Aplikasimu:</label>
                <div class="text-xs text-slate-500">Contoh: <i>ThermoMaster</i>, <i>RobloxVault</i>, <i>MisiJuara 2026</i></div>
            </div>
            <div>
                <label class="block font-semibold text-slate-700 dark:text-slate-300 mb-1">3. Siapa Penggunanya & Masalah Apa yang Diselesaikan?</label>
                <div class="text-xs text-slate-500">Contoh: "Membantu adik kelas mengonversi suhu PR Fisika tanpa ribet hitung manual."</div>
            </div>
        </div>
    </div>
    <p class="text-center text-xs text-slate-400">Tulis jawabanmu di buku catatan atau Google Doc proyekmu sekarang!</p>
</div>"""
    },
    {
        "title": "Workshop Tahap 2: Gambar Wireframe 📐",
        "subtitle": "Waktunya Menggambar di Kertas!",
        "content": """<div class="max-w-3xl mx-auto space-y-5 text-center">
    <div class="text-5xl">✏️</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Buka Buku Catatan & Pensilmu!</h3>
    <p class="text-slate-600 dark:text-slate-300 text-sm max-w-xl mx-auto">
        Gambarkan satu persegi panjang besar (mewakili jendela CustomTkinter aplikasimu), lalu bagi menjadi 3 blok:
    </p>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs text-left max-w-2xl mx-auto">
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>Blok Atas:</b>
            <p class="text-slate-400 mt-1">Judul aplikasi & icon</p>
        </div>
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>Blok Tengah:</b>
            <p class="text-slate-400 mt-1">Kotak input data & petunjuk</p>
        </div>
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>Blok Bawah:</b>
            <p class="text-slate-400 mt-1">Tombol aksi & area teks hasil</p>
        </div>
    </div>
    <div class="inline-block p-3 bg-green-500/10 border border-green-500/30 rounded-xl text-green-700 dark:text-green-300 text-xs font-semibold">
        ⏱️ Waktu menggambar: 10 Menit. Jangan takut gambarnya jelek, yang penting jelas posisinya!
    </div>
</div>"""
    },
    {
        "title": "Workshop Tahap 3: Tentukan 3 Fitur Core MVP 🎯",
        "subtitle": "Kunci Keberhasilan Proyek",
        "content": """<div class="max-w-2xl mx-auto space-y-4 text-left">
    <div class="bg-white/5 border border-white/10 p-6 rounded-2xl space-y-3">
        <h4 class="font-bold text-slate-800 dark:text-white">Lembar Kerja 2: Tiga Fitur Wajib (Core MVP)</h4>
        <p class="text-xs text-slate-400">Tentukan 3 fitur yang PASTI akan kamu selesaikan di Sesi 10 & 11:</p>
        <div class="space-y-3 text-xs">
            <div class="p-3 bg-slate-900 rounded-xl text-white space-y-1">
                <span class="text-blue-400 font-bold">Fitur 1 (Input Handling):</span>
                <p class="text-slate-300">Contoh: "Menerima input angka derajat dari user"</p>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl text-white space-y-1">
                <span class="text-indigo-400 font-bold">Fitur 2 (Processing):</span>
                <p class="text-slate-300">Contoh: "Menghitung rumus konversi saat tombol ditekan"</p>
            </div>
            <div class="p-3 bg-slate-900 rounded-xl text-white space-y-1">
                <span class="text-green-400 font-bold">Fitur 3 (Display & Validation):</span>
                <p class="text-slate-300">Contoh: "Menampilkan hasil berformat & cegah error jika input kosong"</p>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Workshop Tahap 4: Ringkasan Proposal 📝",
        "subtitle": "Checklist Kesiapan Sebelum Mulai Koding",
        "content": """<div class="max-w-2xl mx-auto space-y-4 text-left">
    <div class="p-6 bg-slate-900 text-white rounded-2xl border border-slate-700 font-mono text-xs space-y-2">
        <div class="text-center font-sans font-bold text-amber-400 text-sm pb-2 border-b border-slate-700">=== PROPOSAL PROYEK LEVEL 3 KALANANTI ===</div>
        <p><span class="text-slate-400">Nama Developer:</span> [Nama Kamu]</p>
        <p><span class="text-slate-400">Track Pilihan:</span> [Track 1 / 2 / 3 / Advanced]</p>
        <p><span class="text-slate-400">Nama Aplikasi:</span> [Nama Keren Aplikasi]</p>
        <p><span class="text-slate-400">Target Warna:</span> [Dark Mode + Aksen Biru/Hijau]</p>
        <p><span class="text-slate-400">Fitur MVP 1:</span> [Input data user]</p>
        <p><span class="text-slate-400">Fitur MVP 2:</span> [Fungsi perhitungan / validasi]</p>
        <p><span class="text-slate-400">Fitur MVP 3:</span> [Display hasil dinamis]</p>
        <p><span class="text-slate-400">Ide Fitur Sandbox:</span> [Reset Button / Dynamic Color]</p>
    </div>
</div>"""
    },
    {
        "title": "Bonus Sneak Peek: Dynamic UI & .destroy() 💥",
        "subtitle": "Tantangan To-Do Pro (Opsional)",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="inline-block px-3 py-1 bg-indigo-100 text-indigo-800 dark:bg-indigo-900/50 dark:text-indigo-300 rounded-full font-bold text-[10px] uppercase tracking-widest">Sneak Peek Opsional</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Menghapus Widget dari Layar</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Bagi yang ingin mengembangkan To-Do List Pro di mana setiap baris tugas bisa dihapus dengan tanda silang, CustomTkinter memiliki perintah bernama <code>.destroy()</code>.</p>
        <div class="bg-slate-900 p-3 rounded-xl font-mono text-xs text-red-400 text-left">
            kotak_tugas.destroy()
        </div>
        <p class="text-xs text-slate-500">Perintah ini akan melepas widget dari tampilan layar aplikasi. Fitur ini opsional dan bisa dieksplorasi di Sesi 11!</p>
    </div>
    <div class="bg-indigo-50 dark:bg-slate-800 p-6 rounded-3xl text-center space-y-3 border border-indigo-200 dark:border-indigo-800">
        <div class="text-5xl">🪄</div>
        <h5 class="font-bold text-slate-800 dark:text-white text-sm">Dynamic Widget Creation</h5>
        <p class="text-xs text-slate-600 dark:text-slate-300">Widget bisa diciptakan di dalam fungsi saat tombol diklik, bukan cuma di awal program. Keren banget kan?</p>
    </div>
</div>"""
    },
    {
        "title": "Checkpoint Persetujuan Guru ✅",
        "subtitle": "Konsultasikan Sketsamu!",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-pulse">📋</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Waktunya Konsultasi dengan Guru!</h3>
    <p class="text-sm text-slate-600 dark:text-slate-300">Tunjukkan sketsa wireframe dan 3 fitur MVP yang sudah kamu tulis kepada Captain / Miss Pengajar.</p>
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs text-left max-w-xl mx-auto">
        <div class="p-3 bg-green-500/10 border border-green-500/30 rounded-xl text-green-700 dark:text-green-300">
            <b>1. Scope Masuk Akal</b>
            <p class="text-[11px] mt-1">Bisa selesai dalam 2 pertemuan</p>
        </div>
        <div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl text-blue-700 dark:text-blue-300">
            <b>2. Wireframe Jelas</b>
            <p class="text-[11px] mt-1">Posisi widget terlihat rapi</p>
        </div>
        <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl text-purple-700 dark:text-purple-300">
            <b>3. MVP Terukur</b>
            <p class="text-[11px] mt-1">Tiga fungsi utama jelas</p>
        </div>
    </div>
    <p class="text-xs font-bold text-blue-600 dark:text-blue-400">Jika sudah di-ACC, simpan wireframe-mu baik-baik untuk Sesi 10 minggu depan!</p>
</div>"""
    },
    {
        "title": "Summary Misi 9 📝",
        "subtitle": "Fondasi Kuat Telah Dibangun",
        "content": """<div class="max-w-3xl mx-auto space-y-5">
    <div class="grid sm:grid-cols-2 gap-4 text-left text-xs">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">✅ Yang Telah Kita Selesaikan Hari Ini:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Memilih 1 Track Proyek (Converter / Login / To-Do / Weather).</li>
                <li>Membagi layar jadi 3 Zona (Header, Input, Display).</li>
                <li>Menetapkan 3 Fitur Core MVP yang realistis.</li>
                <li>Menyelesaikan wireframe sketsa antarmuka.</li>
            </ul>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">🎯 Apa yang Akan Kita Lakukan di Sesi 10:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Buka VS Code dan buat file proyek utama (<code>app.py</code>).</li>
                <li>Koding layout UI lengkap sesuai wireframe masing-masing.</li>
                <li>Menerapkan styling warna, frame, padding, dan font.</li>
                <li>Menghasilkan antarmuka visual utuh yang siap diberi logika!</li>
            </ul>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Quote of the Day 💭",
        "subtitle": "Inspirasi Hari Ini",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-6">
    <div class="text-6xl">🌟</div>
    <blockquote class="text-xl md:text-2xl font-bold text-slate-800 dark:text-white italic leading-relaxed">
        "Sebelum menulis baris kode pertama, seorang developer hebat selalu menggambar rencananya terlebih dahulu."
    </blockquote>
    <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">— Kalananti Coding Academy</p>
    <div class="pt-6 border-t border-white/10">
        <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">Sampai Jumpa di Sesi 10: Koding Antarmuka!</p>
    </div>
</div>"""
    }
]

print(f"Generated Meeting 9 with {len(m9_slides)} slides successfully.")
