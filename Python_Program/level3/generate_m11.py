# -*- coding: utf-8 -*-
"""Generate Meeting 11 for level3/deck.html"""

m11_slides = [
    {
        "title": "Meeting 11: Menghidupkan Aplikasi (App Logic) ⚡",
        "subtitle": "Event Handling, Validasi & Debugging",
        "content": """<div class="text-center max-w-4xl mx-auto space-y-6">
    <div class="text-6xl animate-pulse">⚡</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-green-100 text-green-800 dark:bg-green-900/50 dark:text-green-300 font-bold text-xs uppercase tracking-widest border border-green-200 dark:border-green-700">Proyek Akhir • Tahap 2 dari 2</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Saatnya Memberi "Otak" pada Aplikasi!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Di Sesi 10 kemarin, kita sudah berhasil merancang wajah visual aplikasi. Hari ini, seluruh tombol yang tadinya masih diam membisu akan kita beri "nyawa" agar dapat merespons klik mouse, memproses data, dan memperbarui hasil di layar!
    </p>
    <div class="grid sm:grid-cols-3 gap-4 pt-4 max-w-3xl mx-auto text-left text-xs">
        <div class="p-4 bg-white/5 border border-white/10 rounded-2xl">
            <b class="text-blue-400 block mb-1">1. Event Handling</b>
            <span class="text-slate-400">Menghubungkan tombol ke fungsi Python via <code>command=</code></span>
        </div>
        <div class="p-4 bg-white/5 border border-white/10 rounded-2xl">
            <b class="text-indigo-400 block mb-1">2. Core Processing</b>
            <span class="text-slate-400">Membaca input <code>.get()</code> & update teks <code>.configure()</code></span>
        </div>
        <div class="p-4 bg-white/5 border border-white/10 rounded-2xl">
            <b class="text-green-400 block mb-1">3. Robust Testing</b>
            <span class="text-slate-400">Validasi input kosong & pencegahan crash dengan <code>try-except</code></span>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Flashback Sesi 10 ⏪",
        "subtitle": "Menyambungkan Tombol ke Fungsi",
        "content": """<div class="max-w-3xl mx-auto space-y-5 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm">Ingat kembali aturan sakti saat menyambungkan tombol ke fungsi Python:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        <span class="text-slate-500"># Definisikan fungsinya terlebih dahulu di bagian atas</span><br>
        def aksi_tombol():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print("Tombol berhasil diklik!")<br><br>
        <span class="text-slate-500"># Sambungkan ke tombol tanpa tanda kurung ()</span><br>
        btn = ctk.CTkButton(app, text="Klik Aku", <span class="text-yellow-400 font-bold">command=aksi_tombol</span>)
    </div>
    <div class="p-4 bg-amber-50 dark:bg-amber-950/40 border border-amber-300 dark:border-amber-800/50 rounded-2xl text-xs space-y-1">
        <b class="text-amber-800 dark:text-amber-300">⚠️ JANGAN TULIS <code>command=aksi_tombol()</code>!</b>
        <p class="text-slate-600 dark:text-slate-400">Jika memakai tanda kurung <code>()</code>, fungsi akan langsung dieksekusi begitu aplikasi baru dibuka, bukan menunggu tombol diklik pengguna!</p>
    </div>
</div>"""
    },
    {
        "title": "Mini Quiz Flashback 🧠",
        "subtitle": "Pemanasan Event Handling",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-5xl">🧐</div>
    <p class="font-semibold text-slate-800 dark:text-white text-xl">Bagaimana cara mengambil teks yang sedang diketik oleh user di dalam <code>CTkEntry</code> bernama <code>entry_nama</code>?</p>
    <div class="grid grid-cols-1 gap-3">
        <button onclick="showMiniFeedback('fb-m11-quiz', 'Salah! .text bukan method bawaan CTkEntry untuk mengambil data.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">A. Menggunakan perintah entry_nama.text()</button>
        <button onclick="showMiniFeedback('fb-m11-quiz', 'Tepat Sekali! Method .get() akan membaca dan mengembalikan teks yang ada di kotak input sebagai tipe data String.', 'success')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-green-400 transition-all text-left text-sm">B. Menggunakan method entry_nama.get()</button>
        <button onclick="showMiniFeedback('fb-m11-quiz', 'Salah! .read() biasanya untuk membaca file eksternal, bukan kotak GUI.', 'warn')" class="px-5 py-4 bg-white/5 border border-white/10 rounded-2xl hover:border-blue-400 transition-all text-left text-sm">C. Menggunakan perintah entry_nama.read()</button>
    </div>
    <div id="fb-m11-quiz" class="min-h-[48px] mt-4"></div>
</div>"""
    },
    {
        "title": "Objectives Misi 11 🎯",
        "subtitle": "Target Kita Hari Ini",
        "content": """<div class="max-w-3xl mx-auto space-y-6">
    <ul class="space-y-4 text-left">
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menguasai Tiga Langkah Emas Logika GUI</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Alur standar: Ambil Input (<code>.get()</code>) ➔ Proses Rumus/Verifikasi ➔ Update Layar (<code>.configure()</code>).</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menuliskan Logika Inti Sesuai Track Proyek Masing-Masing</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Mengimplementasikan rumus converter / logika verifikasi login / manajemen list tugas.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menerapkan Proteksi Error dengan try-except</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Mencegah aplikasi force close saat user memasukkan huruf di kolom angka atau membiarkan form kosong.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-4 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Menuntaskan 3 Test Case Pengujian Mandiri</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-1">Memastikan aplikasi lolos uji coba normal, uji coba input kosong, dan uji coba input salah.</p>
            </div>
        </li>
    </ul>
</div>"""
    },
    {
        "title": "Tiga Langkah Emas Logika GUI 🏆",
        "subtitle": "Alur Wajib Setiap Fungsi Tombol",
        "content": """<div class="max-w-4xl mx-auto space-y-5 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-base">Hampir 100% fungsi tombol di aplikasi GUI modern mengikuti 3 langkah ini:</p>
    <div class="grid md:grid-cols-3 gap-4 text-xs">
        <div class="p-5 rounded-2xl bg-blue-50 dark:bg-slate-800 border-2 border-blue-300 dark:border-blue-700 space-y-2">
            <div class="text-2xl mb-1">📥</div>
            <b class="text-blue-800 dark:text-blue-300 text-sm">Langkah 1: Tarik Data</b>
            <p class="text-slate-600 dark:text-slate-400">Ambil apa yang sedang diketik user ke dalam variabel lokal:</p>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-300">teks = entry.get()</div>
        </div>
        <div class="p-5 rounded-2xl bg-indigo-50 dark:bg-slate-800 border-2 border-indigo-300 dark:border-indigo-700 space-y-2">
            <div class="text-2xl mb-1">⚙️</div>
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">Langkah 2: Proses Otak</b>
            <p class="text-slate-600 dark:text-slate-400">Lakukan perhitungan matematika, cek kata sandi, atau format teks:</p>
            <div class="bg-black/30 p-2 rounded font-mono text-indigo-300">hasil = float(teks) * 2</div>
        </div>
        <div class="p-5 rounded-2xl bg-green-50 dark:bg-slate-800 border-2 border-green-300 dark:border-green-700 space-y-2">
            <div class="text-2xl mb-1">🖥️</div>
            <b class="text-green-800 dark:text-green-300 text-sm">Langkah 3: Tembak Layar</b>
            <p class="text-slate-600 dark:text-slate-400">Perbarui teks label di layar dengan hasil yang baru:</p>
            <div class="bg-black/30 p-2 rounded font-mono text-green-300">label.configure(text=hasil)</div>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Logika Track 1: Unit Converter 🔄",
        "subtitle": "Koding Fungsi Hitung Konversi",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">App Logic Track 1</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Pasang fungsi ini di atas dan sambungkan ke <code>command=hitung_konversi</code> pada tombol:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        def hitung_konversi():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;try:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># 1. Ambil nilai input dan ubah jadi angka desimal (float)</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;celcius = float(entry_nilai.get())<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># 2. Hitung rumus Fahrenheit</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fahrenheit = (celcius * 9/5) + 32<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># 3. Update tampilan hasil ke layar</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text=f"Hasil: {fahrenheit:.1f} °F", text_color="#38BDF8")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;except ValueError:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># Jika user mengetik huruf, cegah crash & beri peringatan ramah</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text="⚠️ Harap masukkan angka!", text_color="#F87171")
    </div>
</div>"""
    },
    {
        "title": "Logika Track 2: Login System 🔐",
        "subtitle": "Koding Fungsi Autentikasi Pengguna",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">App Logic Track 2</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Pasang fungsi verifikasi kredensial ini dan sambungkan ke <code>command=proses_login</code>:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        def proses_login():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;user = entry_user.get().strip()<br>
        &nbsp;&nbsp;&nbsp;&nbsp;pwd = entry_pass.get().strip()<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># 1. Cek jika form masih kosong</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;if not user or not pwd:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_status.configure(text="⚠️ Username & Password wajib diisi!", text_color="#FBBF24")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># 2. Cocokkan dengan akun contoh yang diizinkan</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;if user == "agent_kalananti" and pwd == "rahasia123":<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_status.configure(text=f"✅ Akses Diterima! Selamat datang, {user}.", text_color="#4ADE80")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_status.configure(text="❌ Akses Ditolak: Password salah!", text_color="#F87171")
    </div>
</div>"""
    },
    {
        "title": "Logika Track 3: To-Do List Lite 📋",
        "subtitle": "Koding Fungsi Tambah & Reset Tugas",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">App Logic Track 3</span>
    <p class="text-sm text-slate-600 dark:text-slate-300">Kelola daftar tugas menggunakan List Python dan update label papan tugas:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        daftar_tugas = []&nbsp;&nbsp;<span class="text-slate-500"># List penyimpanan data tugas</span><br><br>
        def tambah_misi():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;tugas_baru = entry_tugas.get().strip()<br>
        &nbsp;&nbsp;&nbsp;&nbsp;if tugas_baru:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;daftar_tugas.append(tugas_baru)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;entry_tugas.delete(0, 'end')&nbsp;&nbsp;<span class="text-slate-500"># Kosongkan kotak ketik</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># Susun kembali tampilan teks berurutan</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;teks_tampil = "\\n".join([f"{i+1}. {t}" for i, t in enumerate(daftar_tugas)])<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_daftar.configure(text=teks_tampil, text_color="white")<br><br>
        def reset_misi():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;daftar_tugas.clear()<br>
        &nbsp;&nbsp;&nbsp;&nbsp;label_daftar.configure(text="Daftar Misi Kosong...", text_color="gray")
    </div>
</div>"""
    },
    {
        "title": "Penyelamat Aplikasi: try-except 🛡️",
        "subtitle": "Mencegah Aplikasi Crash di Depan Penonton",
        "content": """<div class="grid md:grid-cols-2 gap-6 items-center max-w-4xl mx-auto text-left">
    <div class="space-y-4">
        <h4 class="text-xl font-bold text-slate-800 dark:text-white">Mengapa Wajib try-except?</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Bayangkan saat presentasi, penguji tidak sengaja mengetik huruf <code>"abc"</code> di kotak suhu. Tanpa <code>try-except</code>, Python akan memuntahkan error merah di terminal dan aplikasimu mati seketika!
        </p>
        <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">
            Dengan <code>try-except</code>, kamu menjadi programmer tangguh yang bisa menangani kesalahan dengan anggun.
        </p>
    </div>
    <div class="p-5 rounded-2xl bg-slate-900 border border-slate-700 font-mono text-xs space-y-2">
        <span class="text-blue-400 font-bold">Pola Penanganan:</span>
        <p class="text-green-400">try:<br>&nbsp;&nbsp;&nbsp;&nbsp;angka = float(entry.get())</p>
        <p class="text-red-400">except ValueError:<br>&nbsp;&nbsp;&nbsp;&nbsp;label.configure(text="Input salah!")</p>
    </div>
</div>"""
    },
    {
        "title": "Creative Sandbox: Power-Up 1 🧹",
        "subtitle": "Tombol Reset / Bersihkan Form",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Power-Up Fitur 1</span>
    <h4 class="text-lg font-bold text-slate-800 dark:text-white">Membersihkan Kotak Input Sekali Klik</h4>
    <p class="text-sm text-slate-600 dark:text-slate-300">Pengguna sangat senang jika tidak perlu repot-repot memblok dan menekan tombol Backspace berulang kali. Buat fungsi pembersih form ini:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        def bersihkan_form():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;entry_input.delete(0, 'end')&nbsp;&nbsp;<span class="text-slate-500"># Kosongkan dari huruf index 0 sampai akhir</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text="Hasil: ---", text_color="gray")<br><br>
        <span class="text-slate-500"># Sambungkan ke tombol:</span><br>
        btn_reset = ctk.CTkButton(app, text="Clear Form 🧹", command=bersihkan_form, fg_color="#475569")
    </div>
</div>"""
    },
    {
        "title": "Creative Sandbox: Power-Up 2 🌈",
        "subtitle": "Feedback Warna Dinamis",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Power-Up Fitur 2</span>
    <h4 class="text-lg font-bold text-slate-800 dark:text-white">Warna Layar yang Merespons Nilai Hasil</h4>
    <p class="text-sm text-slate-600 dark:text-slate-300">Gunakan logika <code>if / elif / else</code> untuk mengubah warna teks atau tombol sesuai kondisi hasil perhitungan:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        if nilai_suhu > 35:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># Suhu panas: teks warna merah membara</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text=f"Panas Terik: {nilai_suhu}°C 🔥", text_color="#EF4444")<br>
        elif nilai_suhu < 15:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># Suhu dingin: teks warna biru es</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text=f"Dingin Sejuk: {nilai_suhu}°C ❄️", text_color="#38BDF8")<br>
        else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;label_hasil.configure(text=f"Nyaman: {nilai_suhu}°C 🌿", text_color="#22C55E")
    </div>
</div>"""
    },
    {
        "title": "Creative Sandbox: Power-Up 3 🌗",
        "subtitle": "Tombol Ganti Dark / Light Mode",
        "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <span class="mock-window-badge">Power-Up Fitur 3</span>
    <h4 class="text-lg font-bold text-slate-800 dark:text-white">Beralih Tema Saat Aplikasi Berjalan</h4>
    <p class="text-sm text-slate-600 dark:text-slate-300">Kalian bisa memasang tombol saklar yang memungkinkan pengguna mengganti nuansa gelap ke terang secara instan:</p>
    <div class="bg-slate-900 p-5 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-2">
        mode_gelap = True<br><br>
        def ganti_tema():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;global mode_gelap<br>
        &nbsp;&nbsp;&nbsp;&nbsp;if mode_gelap:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctk.set_appearance_mode("Light")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_tema.configure(text="Mode Gelap 🌙")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_gelap = False<br>
        &nbsp;&nbsp;&nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctk.set_appearance_mode("Dark")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_tema.configure(text="Mode Terang ☀️")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode_gelap = True
    </div>
</div>"""
    },
    {
        "title": "Optional Track: Weather App & API 🌦️",
        "subtitle": "Konsep Pelayan Data Web",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <div class="inline-block px-3 py-1 bg-purple-100 text-purple-800 dark:bg-purple-900/50 dark:text-purple-300 rounded-full font-bold text-[10px] uppercase tracking-widest">Optional Advanced Track</div>
    <h4 class="text-xl font-bold text-slate-800 dark:text-white">Apa itu API (Application Programming Interface)?</h4>
    <p class="text-sm text-slate-600 dark:text-slate-300">
        Bayangkan kamu makan di restoran. Kamu (Aplikasi) tidak boleh masuk ke dapur (Server BMKG). Kamu memesan lewat <b>Pelayan (API)</b>. Pelayan membawakan hidangan (Data Cuaca) dalam piring khusus bernama <b>JSON</b>.
    </p>
    <div class="grid md:grid-cols-3 gap-3 text-center text-xs pt-2">
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>1. Request</b>
            <p class="text-slate-400 mt-1">Aplikasimu minta: "Cuaca Jakarta?"</p>
        </div>
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>2. Server Cuaca</b>
            <p class="text-slate-400 mt-1">Mengecek sensor satelit</p>
        </div>
        <div class="p-3 bg-white/5 border border-white/10 rounded-xl">
            <b>3. Response JSON</b>
            <p class="text-slate-400 mt-1">Balasan data: Suhu 31.5°C</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Weather API: Keamanan & Offline Fallback 🛡️",
        "subtitle": "Kunci Kelas yang Anti-Gagal",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-red-50 dark:bg-red-950/40 border border-red-300 dark:border-red-800/50 rounded-2xl text-xs space-y-1">
        <b class="text-red-800 dark:text-red-300">⚠️ GUARDRAIL KEAMANAN PENTING:</b>
        <p class="text-slate-600 dark:text-slate-400">JANGAN PERNAH menuliskan API Key rahasia di file publik atau presentasi! Jika internet sekolah lambat atau API Key belum aktif, aplikasimu BISA TETAP JALAN dengan <b>Mode Simulasi Offline (Mock Data)</b>!</p>
    </div>
    <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 text-xs font-mono text-cyan-300 space-y-1">
        <span class="text-slate-500"># Data Simulasi Cadangan (Jalan 100% Walau Tanpa Internet)</span><br>
        DATA_CUACA_OFFLINE = {<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"jakarta": {"suhu": 32.0, "kondisi": "Cerah Berawan ☀️"},<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"bandung": {"suhu": 22.5, "kondisi": "Hujan Ringan 🌧️"},<br>
        &nbsp;&nbsp;&nbsp;&nbsp;"surabaya": {"suhu": 34.0, "kondisi": "Panas Terik 🌤️"}<br>
        }
    </div>
</div>"""
    },
    {
        "title": "Weather API: Fungsi Eksekusi Cuaca 🌦️",
        "subtitle": "Menghubungkan Data ke Antarmuka",
        "content": """<div class="max-w-4xl mx-auto space-y-3 text-left">
    <span class="mock-window-badge">Logika Weather App</span>
    <div class="bg-slate-900 p-4 rounded-2xl border border-slate-700 text-xs font-mono text-green-400 space-y-1">
        def cari_cuaca():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;kota = entry_kota.get().strip().lower()<br>
        &nbsp;&nbsp;&nbsp;&nbsp;if not kota:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_kondisi.configure(text="⚠️ Ketik nama kota dulu!", text_color="yellow")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return<br><br>
        &nbsp;&nbsp;&nbsp;&nbsp;<span class="text-slate-500"># Cek dari data offline terlebih dahulu (Aman & Cepat)</span><br>
        &nbsp;&nbsp;&nbsp;&nbsp;if kota in DATA_CUACA_OFFLINE:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;info = DATA_CUACA_OFFLINE[kota]<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_suhu.configure(text=f"{info['suhu']} °C")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_kondisi.configure(text=f"{info['kondisi']} • {kota.title()}", text_color="white")<br>
        &nbsp;&nbsp;&nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_kondisi.configure(text="Kota tidak ditemukan di radar!", text_color="#F87171")
    </div>
</div>"""
    },
    {
        "title": "QA & Testing Clinic: 3 Uji Coba Wajib 🧪",
        "subtitle": "Uji Ketahanan Aplikasimu",
        "content": """<div class="max-w-4xl mx-auto space-y-4 text-left">
    <p class="text-slate-600 dark:text-slate-300 text-sm">Sebelum proyek dinyatakan selesai, kamu wajib lulus 3 Uji Coba Kritis ini:</p>
    <div class="grid md:grid-cols-3 gap-4 text-xs">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-green-400">1. Happy Path Test</b>
            <p class="text-slate-400">Ketik data yang benar dan wajar. Apakah hasil muncul sesuai perhitungan?</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-amber-400">2. Empty Form Test</b>
            <p class="text-slate-400">Kosongkan kolom input, lalu klik tombol aksi. Apakah aplikasi memberi peringatan tanpa Force Close?</p>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-red-400">3. Invalid Data Test</b>
            <p class="text-slate-400">Ketik huruf di kotak angka atau simbol aneh. Apakah <code>try-except</code> berhasil menyelamatkan aplikasi?</p>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Debugging Routine: Membaca Pesan Error 🔍",
        "subtitle": "Jangan Takut Pesan Merah di Terminal!",
        "content": """<div class="max-w-3xl mx-auto space-y-3 text-left text-xs">
    <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 text-slate-300 font-mono space-y-1">
        <b class="text-amber-400 font-sans">1. TypeError: 'NoneType' object is not callable</b>
        <p class="text-slate-400">Penyebab: Kamu tidak sengaja menulis <code>command=fungsi()</code> dengan tanda kurung. Hapus tanda kurungnya!</p>
    </div>
    <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 text-slate-300 font-mono space-y-1">
        <b class="text-red-400 font-sans">2. ValueError: could not convert string to float</b>
        <p class="text-slate-400">Penyebab: User mengosongkan input atau mengetik huruf. Bungkus dengan <code>try: ... except ValueError:</code></p>
    </div>
    <div class="p-3 rounded-xl bg-slate-900 border border-slate-700 text-slate-300 font-mono space-y-1">
        <b class="text-blue-400 font-sans">3. NameError: name 'entry_data' is not defined</b>
        <p class="text-slate-400">Penyebab: Ada salah ketik (typo) nama variabel, atau variabel baru dibuat setelah tombol dipanggil.</p>
    </div>
</div>"""
    },
    {
        "title": "Independent Coding Milestone: Sambungkan Otak! 💻",
        "subtitle": "Fokus Hands-on 25 Menit",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-5">
    <div class="text-6xl animate-bounce">⚡</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Saatnya Menuntaskan Logika di VS Code!</h3>
    <p class="text-sm text-slate-600 dark:text-slate-300">Buka file <code>app.py</code>, tuliskan fungsi logikamu, sambungkan ke tombol, dan jalankan 3 test case!</p>
    <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 text-left text-xs font-mono text-green-300 space-y-1 max-w-lg mx-auto">
        <p>1. [ ] Fungsi callback tombol sudah dibuat</p>
        <p>2. [ ] Method .get() berhasil menarik input user</p>
        <p>3. [ ] Rumus matematika / verifikasi berjalan benar</p>
        <p>4. [ ] Label hasil terupdate via .configure()</p>
        <p>5. [ ] try-except aktif melindungi dari input rusak</p>
    </div>
    <p class="text-xs text-slate-400">Captain ada di samping kalian untuk membantu membasmi bug!</p>
</div>"""
    },
    {
        "title": "Checklist Kesiapan Sesi 11 ✅",
        "subtitle": "Syarat Lolos ke Grand Showcase",
        "content": """<div class="max-w-xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <h4 class="font-bold text-slate-800 dark:text-white text-sm">Checklist Kesiapan Showcase:</h4>
        <div class="space-y-2 text-xs">
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Aplikasi berjalan mulus dari awal hingga akhir tanpa crash.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">3 Fitur Core MVP bekerja 100% saat diuji coba.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Validasi input aktif memberikan pesan ramah saat salah ketik.</span>
            </div>
            <div class="flex items-center gap-2">
                <span class="text-green-500 font-bold">✓</span>
                <span class="text-slate-700 dark:text-slate-300">Terdapat minimal 1 sentuhan personal dari menu Creative Sandbox.</span>
            </div>
        </div>
    </div>
    <p class="text-center text-xs text-green-600 dark:text-green-400 font-semibold">Selamat! Mahakarya aplikasimu siap dipamerkan di panggung Sesi 12!</p>
</div>"""
    },
    {
        "title": "Summary Misi 11 📝",
        "subtitle": "Aplikasi Telah Bernyawa Penuh",
        "content": """<div class="max-w-3xl mx-auto space-y-5">
    <div class="grid sm:grid-cols-2 gap-4 text-left text-xs">
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">✅ Yang Telah Kita Capai Hari Ini:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Menguasai pola <code>Input -> Process -> Output</code> di GUI.</li>
                <li>Menghubungkan event klik tombol dengan fungsi koding Python.</li>
                <li>Menerapkan pertahanan <code>try-except</code> dari bahaya crash.</li>
                <li>Menguji ketahanan aplikasi lewat 3 skenario pengujian ketat.</li>
            </ul>
        </div>
        <div class="p-4 rounded-xl bg-white/5 border border-white/10 space-y-2">
            <b class="text-slate-800 dark:text-white text-sm">🌟 Panggung Besar Menanti di Sesi 12:</b>
            <ul class="space-y-1 list-disc pl-4 text-slate-600 dark:text-slate-300">
                <li>Showcase Day: Pamerkan aplikasi buatanmu di depan kelas!</li>
                <li>Belajar teknik presentasi 3 menit layaknya Developer Profesional.</li>
                <li>Mendemonstrasikan fitur unggulan dan cara kamu membasmi bug.</li>
                <li>Menerima feedback positif dari teman-teman dan perayaan kelulusan!</li>
            </ul>
        </div>
    </div>
</div>"""
    },
    {
        "title": "Quote of the Day 💭",
        "subtitle": "Inspirasi Hari Ini",
        "content": """<div class="max-w-2xl mx-auto text-center space-y-6">
    <div class="text-6xl">🚀</div>
    <blockquote class="text-xl md:text-2xl font-bold text-slate-800 dark:text-white italic leading-relaxed">
        "Kode terbaik bukanlah kode yang paling panjang atau paling rumit, melainkan kode yang bekerja andal dan membawa manfaat nyata bagi penggunanya."
    </blockquote>
    <p class="text-sm font-semibold text-blue-600 dark:text-blue-400">— Developer Principle</p>
    <div class="pt-6 border-t border-white/10">
        <p class="text-xs text-slate-400 uppercase tracking-widest font-bold">Sampai Jumpa di Sesi 12: The Grand Showcase!</p>
    </div>
</div>"""
    }
]

print(f"Generated Meeting 11 with {len(m11_slides)} slides successfully.")
