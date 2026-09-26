# -*- coding: utf-8 -*-
"""Generate Meeting 10 for level3/deck.html"""

m10_slides = [
    {
        "title": "Meeting 10: Membangun Antarmuka (UI Layout) 📐",
        "subtitle": "Front-End Blueprint & Visual Styling",
        "content": """<div class="text-center max-w-4xl mx-auto space-y-6">
    <div class="text-6xl animate-pulse">📐</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-indigo-100 text-indigo-800 dark:bg-indigo-900/50 dark:text-indigo-300 font-bold text-xs uppercase tracking-widest border border-indigo-200 dark:border-indigo-700">Proyek Akhir • Tahap 1 dari 2</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Saatnya Menjadi Front-End Designer!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Hari ini kita akan menerjemahkan sketsa kertas (Wireframe) dari Sesi 9 menjadi <b>antarmuka jendela aplikasi sungguhan</b> di CustomTkinter. Seluruh tombol, kotak input, dan label akan dipasang rapi di posisinya!
    </p>
    <div class="bg-blue-50 dark:bg-slate-800/80 p-4 rounded-2xl border border-blue-200 dark:border-slate-700 max-w-xl mx-auto text-sm text-blue-900 dark:text-blue-200 font-semibold">
        💡 Catatan Penting: Hari ini kita murni fokus pada <b>tampilan visual</b>. Tombol masih berupa tombol dummy (belum dihubungkan ke logika hitung). Logika tombol akan kita berikan di Sesi 11!
    </div>
</div>"""
    },
    {
        "title": "Flashback Sesi 9 ⏪",
        "subtitle": "Review Wireframe & 3 Zona",
        "content": """<div class="max-w-4xl mx-auto space-y-6 text-center">
    <p class="text-slate-600 dark:text-slate-300 text-base">Ambil kertas wireframemu! Ingat kembali 3 zona yang akan kita wujudkan hari ini:</p>
    <div class="grid md:grid-cols-3 gap-4">
        <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-2">🏷️</div>
            <h4 class="font-bold text-slate-800 dark:text-white text-sm">1. Zona Header</h4>
            <p class="text-xs text-slate-400 mt-1">Judul aplikasi & icon pengenal</p>
        </div>
        <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-2">⌨️</div>
            <h4 class="font-bold text-slate-800 dark:text-white text-sm">2. Zona Form Input</h4>
            <p class="text-xs text-slate-400 mt-1">Kotak ketik teks / angka user</p>
        </div>
        <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
            <div class="text-3xl mb-2">🔘</div>
            <h4 class="font-bold text-slate-800 dark:text-white text-sm">3. Zona Aksi & Display</h4>
            <p class="text-xs text-slate-400 mt-1">Tombol utama & label hasil</p>
        </div>
    </div>
    <p class="text-xs text-slate-400">Semua track (Converter, Login, To-Do, Weather) menggunakan struktur 3 zona ini!</p>
</div>"""
    },
    {
        "title": "Mini Quiz Flashback 🧠",
        "subtitle": "Pemanasan Front-End",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-5xl">🧐</div>
    <p class="font-semibold text-slate-800 dark:text-white text-xl">Dalam siklus pembuatan software, apa tugas utama seorang <b>Front-End Developer</b>?</p>
    <div class="grid grid-cols-1 gap-3">
        <button onclick="showMiniFeedback('fb-m10-quiz', 'Kurang tepat! Database dan server adalah tugas Back-End Developer.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">A. Merancang kabel server internet dan database pusat.</button>
        <button onclick="showMiniFeedback('fb-m10-quiz', 'Tepat Sekali! Front-End Developer merancang antarmuka visual yang dilihat dan disentuh langsung oleh pengguna agar nyaman, indah, dan intuitif.', 'success')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-green-400 transition-all text-left text-sm">B. Membangun wajah aplikasi (tata letak, tombol, warna, dan keterbacaan teks) agar nyaman digunakan oleh user.</button>
        <button onclick="showMiniFeedback('fb-m10-quiz', 'Salah! Memperbaiki listrik monitor bukan tugas programmer.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">C. Memperbaiki kerusakan kabel daya monitor komputer.</button>
    </div>
    <div id="fb-m10-quiz" class="min-h-[48px] mt-4"></div>
</div>"""
    },
    {
        "title": "Objectives Misi 10 🎯",
        "subtitle": "Target Kita Hari Ini",
        "content": """<div class="max-w-3xl mx-auto space-y-6">
    <ul class="space-y-4 text-left">
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Setup Root Window & Visual Identity</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Mengatur ukuran jendela (geometry), judul window, dan tema warna (Dark/Light).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Membangun Container Frame (Wadah Bersih)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Menggunakan <code>CTkFrame</code> dengan sudut membulat (*corner_radius*) untuk mengelompokkan elemen.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Memasang Widget Sesuai Blueprint Track Masing-Masing</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Menempatkan seluruh Label, Entry input, dan Button sesuai wireframe yang sudah di-ACC.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menerapkan Mixed Layouting & Polishing Padding</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Mengatur jarak renggang (*padx*, *pady*) agar antarmuka tidak sesak dan enak dilihat.</p>
            </div>
        </li>
    </ul>
</div>"""
    },
    {
        "title": "Pondasi: Setup Root Window 🪟",
        "subtitle": "Membuat Jendela Pertama Aplikasimu",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Buka VS Code, buat file baru bernama <code>app.py</code>, dan tuliskan pondasi jendela awal ini:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 leading-relaxed">
        <span class="text-slate-500"># 1. Import library CustomTkinter</span><br>
        import customtkinter as ctk<br><br>
        <span class="text-slate-500"># 2. Pengaturan Tema Warna Global</span><br>
        ctk.set_appearance_mode("Dark")&nbsp;&nbsp;<span class="text-slate-500"># Bisa "Light" atau "Dark"</span><br>
        ctk.set_default_color_theme("blue")&nbsp;&nbsp;<span class="text-slate-500"># Tema: "blue", "green", atau "dark-blue"</span><br><br>
        <span class="text-slate-500"># 3. Inisialisasi Jendela Utama</span><br>
        app = ctk.CTk()<br>
        app.title("Nama Aplikasimu 🚀")<br>
        app.geometry("400x520")&nbsp;&nbsp;<span class="text-slate-500"># Lebar x Tinggi (dalam pixel)</span><br><br>
        <span class="text-slate-500"># --- Tempat Kita Memasang Widget Nanti ---</span><br><br>
        <span class="text-slate-500"># 4. Loop Utama Aplikasi (Wajib di Paling Bawah)</span><br>
        app.mainloop()
    </div>
</div>"""
    },
    {
        "title": "Visual Preview: Dark vs Light Mode 🌗",
        "subtitle": "Pilih Nuansa yang Mewakili Karakter Aplikasimu",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div>
        <div class="text-center font-bold text-xs text-blue-400 mb-2 uppercase tracking-widest">Tema 1: Dark Mode</div>
        <div class="mock-window w-full max-w-xs">
            <div class="mock-window-header">
                <div class="mock-window-title">Dark Mode App</div>
                <div class="mock-window-controls">
                    <span class="win-btn win-min"></span>
                    <span class="win-btn win-max"></span>
                    <span class="win-btn win-close"></span>
                </div>
            </div>
            <div class="mock-window-content text-center py-8 space-y-3">
                <div class="text-2xl">🌌</div>
                <div class="text-xs font-bold text-white">Elegan & Ramah Mata</div>
                <div class="px-4 py-2 bg-blue-600 rounded-lg text-white font-bold text-xs mx-auto inline-block">Tombol Biru</div>
            </div>
        </div>
    </div>
    <div>
        <div class="text-center font-bold text-xs text-slate-600 dark:text-slate-300 mb-2 uppercase tracking-widest">Tema 2: Light Mode</div>
        <div class="mock-window light-mode w-full max-w-xs">
            <div class="mock-window-header">
                <div class="mock-window-title">Light Mode App</div>
                <div class="mock-window-controls">
                    <span class="win-btn win-min"></span>
                    <span class="win-btn win-max"></span>
                    <span class="win-btn win-close"></span>
                </div>
            </div>
            <div class="mock-window-content text-center py-8 space-y-3">
                <div class="text-2xl">☀️</div>
                <div class="text-xs font-bold text-slate-800">Bersih & Minimalis</div>
                <div class="px-4 py-2 bg-blue-600 rounded-lg text-white font-bold text-xs mx-auto inline-block">Tombol Biru</div>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Membangun Wadah: CTkFrame Container 📦",
        "subtitle": "Membuat Kartu Pembungkus yang Rapi",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="space-y-4">
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Mengapa Butuh Frame?</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Tanpa <code>CTkFrame</code>, semua widget akan menempel langsung di background jendela dan terlihat berantakan. Frame bekerja seperti <b>kartu pembungkus</b> dengan sudut lengkung yang modern.
        </p>
        <div class="bg-slate-900 p-4 rounded-xl font-mono text-xs text-green-400 space-y-1">
            frame_utama = ctk.CTkFrame(<br>
            &nbsp;&nbsp;&nbsp;&nbsp;master=app,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;corner_radius=15<br>
            )<br>
            frame_utama.pack(pady=20, padx=20, fill="both", expand=True)
        </div>
    </div>
    <div class="mock-window w-full max-w-xs">
        <div class="mock-window-header">
            <div class="mock-window-title">App Window</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content p-4">
            <div class="p-6 bg-[#2a2a2a] rounded-xl border border-dashed border-cyan-400 text-center space-y-2">
                <span class="text-xs font-mono text-cyan-300 font-bold">CTkFrame (corner_radius=15)</span>
                <p class="text-[11px] text-slate-400">Seluruh widget nanti dipasang di dalam wadah ini!</p>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Rahasia Tata Letak: Mixed Layouting 🔀",
        "subtitle": "Kombinasi Cerdas .pack() dan .grid()",
        "content": """<div class="max-w-4xl mx-auto space-y-5 text-left">
    <div class="bg-blue-50 dark:bg-slate-800/80 p-5 rounded-2xl border border-blue-200 dark:border-slate-700">
        <h4 class="font-bold text-blue-900 dark:text-blue-300 text-base mb-2">Aturan Emas Mixed Layout:</h4>
        <p class="text-sm text-slate-700 dark:text-slate-300">
            1. Gunakan <b>.pack()</b> untuk menumpuk bagian-bagian besar secara vertikal (Header di atas, Frame Form di tengah, Display di bawah).<br>
            2. Gunakan <b>.grid(row, column)</b> di dalam Frame kecil jika ingin menaruh dua elemen berdampingan (misal tombol Login dan Clear bersisian).
        </p>
    </div>
    <div class="p-4 bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800/50 rounded-2xl text-xs space-y-1">
        <b class="text-amber-800 dark:text-amber-300">⚠️ PERINGATAN KERAS:</b>
        <p class="text-slate-600 dark:text-slate-400">JANGAN PERNAH mencampur <code>.pack()</code> dan <code>.grid()</code> pada <b>wadah yang persis sama</b>! Python akan bingung dan aplikasimu akan Freeze/Hanging.</p>
    </div>
</div>"""
    },
    {
        "title": "Mini Quiz Konsep Layout 🧠",
        "subtitle": "Uji Pemahaman Tata Letak",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-5xl">🧐</div>
    <p class="font-semibold text-slate-800 dark:text-white text-xl">Jika kita ingin menaruh tombol <b>"Hitung"</b> dan tombol <b>"Reset"</b> sejajar ke samping (horizontal), cara mana yang paling tepat?</p>
    <div class="grid grid-cols-1 gap-3">
        <button onclick="showMiniFeedback('fb-m10-layout', 'Kurang tepat! .pack() secara default menumpuk tombol atas-bawah, bukan samping-menyamping yang rapi.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">A. Langsung memanggil .pack() pada kedua tombol di jendela utama.</button>
        <button onclick="showMiniFeedback('fb-m10-layout', 'Tepat Sekali! Membuat frame wadah khusus tombol, lalu memakai .grid(row=0, column=0) dan .grid(row=0, column=1) menghasilkan penataan horizontal yang sangat presisi.', 'success')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-green-400 transition-all text-left text-sm">B. Membuat frame_tombol khusus, lalu menggunakan .grid(row=0, column=0) dan .grid(row=0, column=1) di dalamnya.</button>
        <button onclick="showMiniFeedback('fb-m10-layout', 'Salah! Tombol tidak boleh ditumpuk di koordinat yang sama karena tombol kedua akan menutupi tombol pertama.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">C. Memberi row=0 dan column=0 pada kedua tombol di frame yang sama.</button>
    </div>
    <div id="fb-m10-layout" class="min-h-[48px] mt-4"></div>
</div>"""
    },
    {
        "title": "Memasang Header: CTkLabel Judul 🏷️",
        "subtitle": "Memberi Identitas dan Icon pada Aplikasi",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="space-y-4">
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Di dalam frame pembungkus, kita letakkan judul aplikasi menggunakan <code>CTkLabel</code> dengan font tebal dan emoji icon:
        </p>
        <div class="bg-slate-900 p-4 rounded-xl font-mono text-xs text-green-400 space-y-1">
            label_judul = ctk.CTkLabel(<br>
            &nbsp;&nbsp;&nbsp;&nbsp;master=frame_utama,<br>
            &nbsp;&nbsp;&nbsp;&nbsp;text="✨ Nama Keren Aplikasi ✨",<br>
            &nbsp;&nbsp;&nbsp;&nbsp;font=("Arial", 20, "bold")<br>
            )<br>
            label_judul.pack(pady=(20, 10))
        </div>
        <p class="text-xs text-slate-500">Tips: Gunakan <code>pady=(20, 10)</code> untuk memberi jarak 20px di atas dan 10px di bawah!</p>
    </div>
    <div class="mock-window w-full max-w-xs">
        <div class="mock-window-header">
            <div class="mock-window-title">App Window</div>
            <div class="mock-window-controls">
                <span class="win-btn win-min"></span>
                <span class="win-btn win-max"></span>
                <span class="win-btn win-close"></span>
            </div>
        </div>
        <div class="mock-window-content text-center py-6">
            <div class="text-base font-bold text-white">✨ Nama Keren Aplikasi ✨</div>
            <div class="text-[11px] text-slate-400 mt-1">Siap menerima instruksi</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Blueprint Track 1: Unit Converter 🔄",
        "subtitle": "Susunan Widget Konverter Satuan",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Blueprint Track 1</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Bagi yang memilih <b>Unit Converter</b>, pasanglah 4 komponen ini secara berurutan:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># 1. Kotak Input Angka</span><br>
        entry_nilai = ctk.CTkEntry(frame_utama, placeholder_text="Masukkan angka...", width=250, height=38)<br>
        entry_nilai.pack(pady=10)<br><br>
        <span class="text-slate-500"># 2. Tombol Konversi (Command dummy dulu)</span><br>
        btn_hitung = ctk.CTkButton(frame_utama, text="Konversi Sekarang ⚡", width=250, height=40)<br>
        btn_hitung.pack(pady=10)<br><br>
        <span class="text-slate-500"># 3. Label Wadah Penampil Hasil</span><br>
        label_hasil = ctk.CTkLabel(frame_utama, text="Hasil: ---", font=("Arial", 16, "bold"), text_color="#38BDF8")<br>
        label_hasil.pack(pady=15)
    </div>
</div>"""
    },
    {
        "title": "Visual Output: Track 1 (Unit Converter) 🔄",
        "subtitle": "Ekspektasi Tampilan Sesi 10",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Expected Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Target Tampilan Hari Ini</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Setelah kode di sebelah dijalankan, jendela aplikasimu akan muncul rapi seperti ini. Kotak input sudah bisa diketik, tetapi tombol belum menghitung.</p>
        <div class="p-3 bg-blue-500/10 border border-blue-500/30 rounded-xl text-xs text-blue-700 dark:text-blue-300">
            ✅ Checklist Sesi 10: Window muncul, kotak entry aktif, tombol terpasang rapi di tengah!
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
        <div class="mock-window-content space-y-3 py-6">
            <div class="text-center font-bold text-white text-base">🌡️ ThermoConvert Pro</div>
            <div class="text-center text-[11px] text-slate-400">Konversi Celcius ke Fahrenheit</div>
            <div class="w-4/5 mx-auto p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-400 text-center">Masukkan nilai suhu...</div>
            <div class="w-4/5 mx-auto py-2.5 bg-blue-600 rounded-lg text-center text-white font-bold text-xs">Konversi Sekarang ⚡</div>
            <div class="w-4/5 mx-auto p-3 bg-[#172554] rounded-lg border border-blue-500/40 text-center text-cyan-300 text-sm font-bold">
                Hasil: ---
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Blueprint Track 2: Login System 🔐",
        "subtitle": "Susunan Widget Gerbang Keamanan",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Blueprint Track 2</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Bagi yang memilih <b>Login System</b>, pasanglah komponen autentikasi ini:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># 1. Input Username</span><br>
        entry_user = ctk.CTkEntry(frame_utama, placeholder_text="Username...", width=250)<br>
        entry_user.pack(pady=8)<br><br>
        <span class="text-slate-500"># 2. Input Password (Masked dengan Bintang)</span><br>
        entry_pass = ctk.CTkEntry(frame_utama, placeholder_text="Password...", show="*", width=250)<br>
        entry_pass.pack(pady=8)<br><br>
        <span class="text-slate-500"># 3. Tombol Login</span><br>
        btn_login = ctk.CTkButton(frame_utama, text="Masuk Portal 🔓", fg_color="#16a34a", width=250)<br>
        btn_login.pack(pady=10)<br><br>
        <span class="text-slate-500"># 4. Status Pesan</span><br>
        label_status = ctk.CTkLabel(frame_utama, text="Silakan masukkan akun", text_color="gray")<br>
        label_status.pack(pady=8)
    </div>
</div>"""
    },
    {
        "title": "Visual Output: Track 2 (Login System) 🔐",
        "subtitle": "Ekspektasi Tampilan Sesi 10",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Expected Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Target Tampilan Hari Ini</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Jendela portal keamanan siap dengan sensor bintang pada input password. Kolom sudah bisa diketik secara aman.</p>
        <div class="p-3 bg-green-500/10 border border-green-500/30 rounded-xl text-xs text-green-700 dark:text-green-300">
            ✅ Checklist Sesi 10: Kolom password menyamarkan ketikan dengan bulatan/bintang (<code>show="*"</code>)!
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
        <div class="mock-window-content space-y-3 py-6">
            <div class="text-center font-bold text-amber-400 text-base">🛡️ CyberVault Guardian</div>
            <div class="text-center text-[11px] text-slate-400">Portal Keamanan Rahasia</div>
            <div class="w-4/5 mx-auto p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-400">Username...</div>
            <div class="w-4/5 mx-auto p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-400">••••••••</div>
            <div class="w-4/5 mx-auto py-2 bg-green-600 rounded-lg text-center text-white font-bold text-xs">Masuk Portal 🔓</div>
            <div class="text-center text-xs text-slate-500">Silakan masukkan akun</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Blueprint Track 3: To-Do List Lite 📋",
        "subtitle": "Susunan Widget Pencatat Misi",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Blueprint Track 3</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Bagi yang memilih <b>To-Do List Lite</b>, pasanglah komponen pencatat misi ini:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># 1. Baris Input + Tombol Tambah</span><br>
        entry_tugas = ctk.CTkEntry(frame_utama, placeholder_text="Tulis misi baru...", width=200)<br>
        entry_tugas.pack(pady=8)<br><br>
        btn_tambah = ctk.CTkButton(frame_utama, text="+ Tambah Misi", width=200)<br>
        btn_tambah.pack(pady=5)<br><br>
        <span class="text-slate-500"># 2. Wadah Area Display Teks Tugas</span><br>
        label_daftar = ctk.CTkLabel(frame_utama, text="Daftar Misi Kosong...", justify="left")<br>
        label_daftar.pack(pady=15, fill="both", expand=True)<br><br>
        <span class="text-slate-500"># 3. Tombol Reset / Clear</span><br>
        btn_reset = ctk.CTkButton(frame_utama, text="Reset Semua 🧹", fg_color="#b91c1c", width=200)<br>
        btn_reset.pack(pady=10)
    </div>
</div>"""
    },
    {
        "title": "Visual Output: Track 3 (To-Do Lite) 📋",
        "subtitle": "Ekspektasi Tampilan Sesi 10",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Expected Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Target Tampilan Hari Ini</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Antarmuka pencatat tugas dengan area display siap menampung misi-misi yang akan ditambahkan lewat koding logika minggu depan.</p>
        <div class="p-3 bg-indigo-500/10 border border-indigo-500/30 rounded-xl text-xs text-indigo-700 dark:text-indigo-300">
            ✅ Checklist Sesi 10: Input tugas, tombol simpan, area display daftar, dan tombol reset sudah terpasang rapi!
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
        <div class="mock-window-content space-y-3 py-6">
            <div class="text-center font-bold text-indigo-400 text-base">📝 DailyQuest Manager</div>
            <div class="w-4/5 mx-auto p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-400">Tulis misi baru...</div>
            <div class="w-4/5 mx-auto py-2 bg-indigo-600 rounded-lg text-center text-white font-bold text-xs">+ Tambah Misi</div>
            <div class="w-4/5 mx-auto p-4 bg-[#1e293b] rounded-xl border border-slate-700 text-xs text-slate-400 text-center">
                (Daftar Misi Masih Kosong)
            </div>
            <div class="w-4/5 mx-auto py-1.5 bg-red-600/30 border border-red-500/40 rounded-lg text-center text-red-300 text-xs font-semibold">
                Reset Semua 🧹
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Blueprint Optional Track: Weather App 🌦️",
        "subtitle": "Susunan Widget Tampilan Cuaca (Dummy)",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Blueprint Optional Track</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Bagi yang memilih <b>Weather App</b>, pasanglah tampilan kartu cuaca statis ini:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># 1. Search Bar (Entry Kota + Tombol Cari)</span><br>
        entry_kota = ctk.CTkEntry(frame_utama, placeholder_text="Ketik kota (misal: Jakarta)...", width=220)<br>
        entry_kota.pack(pady=10)<br><br>
        btn_cari = ctk.CTkButton(frame_utama, text="Cari Cuaca 🔍", width=220)<br>
        btn_cari.pack(pady=5)<br><br>
        <span class="text-slate-500"># 2. Kartu Display Cuaca (Card Frame)</span><br>
        card_cuaca = ctk.CTkFrame(frame_utama, fg_color="#1e3a8a", corner_radius=15)<br>
        card_cuaca.pack(pady=15, padx=20, fill="both")<br><br>
        label_suhu = ctk.CTkLabel(card_cuaca, text="-- °C", font=("Arial", 32, "bold"))<br>
        label_suhu.pack(pady=10)<br>
        label_kondisi = ctk.CTkLabel(card_cuaca, text="Siap Mencari...", font=("Arial", 14))<br>
        label_kondisi.pack(pady=5)
    </div>
</div>"""
    },
    {
        "title": "Visual Output: Weather App (Dummy UI) 🌦️",
        "subtitle": "Ekspektasi Tampilan Sesi 10",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto">
    <div class="space-y-3 text-left">
        <span class="mock-window-badge">Expected Output</span>
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Target Tampilan Hari Ini</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">Tampilan front-end cuaca sudah terpasang megah dengan warna latar biru laut. Hari ini data masih dummy; koneksi logika/data akan dipasang di Sesi 11!</p>
        <div class="p-3 bg-purple-500/10 border border-purple-500/30 rounded-xl text-xs text-purple-700 dark:text-purple-300">
            ✅ Checklist Sesi 10: Input kota, tombol search, dan kartu cuaca statis sudah terpasang presisi!
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
        <div class="mock-window-content space-y-3 py-6">
            <div class="text-center font-bold text-cyan-400 text-base">🌦️ Live Weather Radar</div>
            <div class="w-4/5 mx-auto p-2 bg-[#2d2d2d] rounded-lg border border-slate-700 text-xs text-slate-400 text-center">Ketik nama kota...</div>
            <div class="w-4/5 mx-auto py-2 bg-blue-600 rounded-lg text-center text-white font-bold text-xs">Cari Cuaca 🔍</div>
            <div class="w-4/5 mx-auto p-4 bg-[#1e3a8a]/70 rounded-xl border border-blue-400/30 text-center space-y-1">
                <div class="text-2xl font-black text-white font-mono">-- °C</div>
                <div class="text-xs text-blue-200">Siap Mencari Kota...</div>
            </div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Polishing UI: Jarak & Warna (Padding) 💅",
        "subtitle": "Kunci Tampilan Antarmuka Profesional",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Aplikasi yang terlihat murahan biasanya karena elemen-elemennya saling bertubrukan. Gunakan 3 rahasia polesan ini:</p>
    <div class="grid md:grid-cols-3 gap-4 text-xs">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-blue-400">1. Padding Luar (pady & padx)</b>
            <p class="text-slate-400">Beri ruang bernafas antar widget: <code>pady=10</code> atau <code>pady=(15, 5)</code> agar tidak mepet.</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-indigo-400">2. Sudut Membulat (corner_radius)</b>
            <p class="text-slate-400">Ubah sudut kotak tombol dan frame: <code>corner_radius=12</code> untuk kesan gadget modern.</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-green-400">3. Warna Interaksi (hover_color)</b>
            <p class="text-slate-400">Tentukan warna tombol saat cursor mouse diarahkan ke atasnya: <code>hover_color="#1d4ed8"</code>.</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Troubleshooting Umum Front-End 🔧",
        "subtitle": "Solusi Cepat Kendala Layout",
        "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="p-3 rounded-xl bg-red-500/10 border border-red-500/30 space-y-1">
        <b class="text-red-700 dark:text-red-300">Kendala 1: Widget tidak muncul sama sekali di layar!</b>
        <p class="text-slate-600 dark:text-slate-400">Solusi: Pastikan kamu sudah memanggil <code>.pack()</code> atau <code>.grid()</code>. Widget yang cuma dibuat tanpa di-pack tidak akan pernah dirender oleh Tkinter!</p>
    </div>
    <div class="p-3 rounded-xl bg-amber-500/10 border border-amber-500/30 space-y-1">
        <b class="text-amber-700 dark:text-amber-300">Kendala 2: Tulisan terpotong atau jendela kekecilan!</b>
        <p class="text-slate-600 dark:text-slate-400">Solusi: Perbesar dimensi pada <code>app.geometry("450x550")</code> agar cukup menampung semua komponen.</p>
    </div>
    <div class="p-3 rounded-xl bg-blue-500/10 border border-blue-500/30 space-y-1">
        <b class="text-blue-700 dark:text-blue-300">Kendala 3: Muncul error TclError: cannot use geometry manager!</b>
        <p class="text-slate-600 dark:text-slate-400">Solusi: Kamu tidak sengaja mencampur <code>.pack()</code> dan <code>.grid()</code> di dalam master frame yang sama. Pisahkan wadahnya!</p>
    </div>
</div>"""
    },
    {
        "title": "Independent Coding Milestone: Bangun UI-mu! 💻",
        "subtitle": "Fokus Hands-on 25 Menit",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-bounce">⚡</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Saatnya Mengoding di VS Code!</h3>
    <p class="text-sm text-slate-600 dark:text-slate-300">Buka file <code>app.py</code> kalian, lihat sketsa wireframe Sesi 9, dan bangun seluruh komponen visualnya sekarang.</p>
    <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 text-left text-xs font-mono text-cyan-300 space-y-1 max-w-lg mx-auto">
        <p>1. [ ] Window setup (title & geometry)</p>
        <p>2. [ ] CTkFrame container pembungkus</p>
        <p>3. [ ] Label Judul & Icon</p>
        <p>4. [ ] Kolom Input (CTkEntry)</p>
        <p>5. [ ] Tombol Aksi (CTkButton)</p>
        <p>6. [ ] Area Display Hasil</p>
    </div>
    <p class="text-xs text-slate-400">Angkat tangan jika menemui error layout, Captain siap mendampingi!</p>
</div>"""
    },
    {
        "title": "Checklist Kesiapan Sesi 10 ✅",
        "subtitle": "Syarat Lolos ke Tahap Logika",
        "content": """<div class="max-w-xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <h4 class="font-bold text-slate-800 dark:text-white text-sm">Checklist Kesiapan Hari Ini:</h4>
        <div class="space-y-2 text-xs">
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">File <code>app.py</code> bisa dijalankan tanpa pesan error merah di terminal.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Jendela aplikasi memiliki judul personal dan tema warna rapi.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Semua kotak input sudah bisa diketik dengan keyboard.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Semua tombol sudah muncul di posisi yang tepat sesuai sketsa.</span>
            </div>
        </div>
    </div>
    <p class="text-center text-xs text-blue-600 dark:text-blue-400 font-semibold">Hebat! Separuh perjalanan proyek akhir sudah berhasil kamu tuntaskan!</p>
</div>"""
    },
    {
        "title": "Summary Misi 10 📝",
        "subtitle": "Wajah Aplikasi Telah Terwujud",
        "content": """<div class="max-w-3xl mx-auto space-y-5">
    <div class="grid sm:grid-cols-2 gap-4 text-left text-xs">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">✅ Pencapaian Hari Ini:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Menguasai arsitektur <code>CTkFrame</code> sebagai container.</li>
                <li>Menata komponen dengan teknik Mixed Layouting yang bersih.</li>
                <li>Membangun layout lengkap sesuai track proyek pilihan.</li>
                <li>Menghasilkan UI yang nyaman dipandang dan siap diberi fungsi.</li>
            </ul>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">⚡ Misi Selanjutnya di Sesi 11:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Membuat fungsi logika di Python untuk merespons tombol.</li>
                <li>Membaca data ketikan user dengan method <code>.get()</code>.</li>
                <li>Menghitung rumus / memverifikasi data login / mengelola tugas.</li>
                <li>Memperbarui teks hasil secara dinamis dengan <code>.configure()</code>!</li>
            </ul>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Quote of the Day 💭",
        "subtitle": "Inspirasi Hari Ini",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-6">
    <div class="text-6xl">🎨</div>
    <blockquote class="text-xl md:text-2xl font-bold text-slate-800 dark:text-white italic leading-relaxed">
        "Desain bukan hanya tentang bagaimana sesuatu terlihat, tetapi bagaimana sesuatu itu bekerja dan dirasakan oleh pengguna."
    </blockquote>
    <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">— Steve Jobs</p>
    <div class="pt-6 border-t border-white/10">
        <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">Sampai Jumpa di Sesi 11: Menghidupkan Aplikasi!</p>
    </div>
</div>"""
    }
]

print(f"Generated Meeting 10 with {len(m10_slides)} slides successfully.")
