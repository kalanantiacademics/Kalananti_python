import re

with open('/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2C/Python_Program/level3/deck.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_meeting_2 = """    "2": [
        {
            "title": "Welcome to Session 2! 🚀",
            "subtitle": "Labels & Buttons",
            "content": `
                <div class="text-center space-y-6 max-w-3xl mx-auto">
                    <div class="text-6xl">🧩</div>
                    <div class="text-2xl font-bold text-slate-800">Menyusun Kepingan Lego!</div>
                    <p class="text-lg text-slate-600">Di sesi pertama, kita sudah berhasil membangun "ruangan" utama (Root Window). Hari ini, kita akan mengisi ruangan tersebut dengan perabotan: Teks informasi dan Tombol yang bisa diklik.</p>
                </div>
            `
        },
        {
            "title": "Flashback Sesi 1 ⏪",
            "subtitle": "Masih ingat Root Window?",
            "content": `
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🏠</div>
                    <p class="font-semibold text-slate-700 text-lg">Perintah apa yang digunakan untuk membuat pondasi aplikasi utama?</p>
                    <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                        <button onclick="showMiniFeedback('s2fb1-feedback', 'Salah! Itu perintah untuk mengatur ukuran.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all">app.geometry()</button>
                        <button onclick="showMiniFeedback('s2fb1-feedback', 'Tepat! CTk() adalah fondasinya.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all">ctk.CTk()</button>
                        <button onclick="showMiniFeedback('s2fb1-feedback', 'Bukan, itu untuk nama jendela.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all">app.title()</button>
                    </div>
                    <div id="s2fb1-feedback" class="min-h-[48px] mt-4"></div>
                </div>
            `
        },
        {
            "title": "Flashback Sesi 1 ⏪",
            "subtitle": "Menghidupkan Aplikasi",
            "content": `
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">⚡</div>
                    <p class="font-semibold text-slate-700 text-lg">Apa perintah yang <b>wajib</b> ditaruh di paling bawah agar aplikasi tidak langsung tertutup?</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <button onclick="showMiniFeedback('s2fb2-feedback', 'Salah! app.run() biasanya ada di web framework seperti Flask, bukan CustomTkinter.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all">app.run()</button>
                        <button onclick="showMiniFeedback('s2fb2-feedback', 'Benar sekali! mainloop menahan program tetap menyala.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all">app.mainloop()</button>
                    </div>
                    <div id="s2fb2-feedback" class="min-h-[48px] mt-4"></div>
                </div>
            `
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": `
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami konsep <b>Widget</b> sebagai komponen penyusun antarmuka.</li>
                        <li>Menampilkan teks statis di layar menggunakan <code>CTkLabel</code>.</li>
                        <li>Membuat tombol interaktif menggunakan <code>CTkButton</code>.</li>
                        <li>Menggunakan perintah <code>.pack()</code> untuk menyusun perabotan di dalam jendela.</li>
                    </ul>
                </div>
            `
        },
        {
            "title": "Materi 1: Apa itu Widget? 🧩",
            "subtitle": "Komponen Antarmuka",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 border border-slate-700 p-6 rounded-xl shadow-lg">
                        <h4 class="font-bold text-cyan-400 mb-2">Decomposition</h4>
                        <p class="text-slate-300 text-sm">Kita tidak membangun aplikasi sekaligus. Kita memecahnya jadi bagian-bagian kecil (teks, tombol, gambar). Bagian-bagian visual kecil inilah yang disebut <b>Widget</b>.</p>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl">🧱</div>
                        <p class="text-slate-600 text-lg">Sama seperti Lego. Kepingan kecil disatukan untuk membangun pesawat atau istana. Widget disatukan untuk membangun aplikasi!</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Materi 2: CTkLabel 🏷️",
            "subtitle": "Widget untuk Teks",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Poster Informasi</h3>
                        <p class="text-slate-600 text-lg">Label digunakan untuk memberikan instruksi, judul, atau informasi yang hanya untuk <b>dibaca</b>. Pengguna tidak bisa mengetik atau mengeklik ini.</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-6 rounded-xl shadow-lg text-center">
                        <p class="text-slate-800 font-bold mb-4">Contoh CTkLabel di dunia nyata:</p>
                        <div class="bg-slate-100 p-3 rounded">
                            <h2 class="text-2xl font-bold text-blue-600">Pendaftaran Siswa Baru</h2>
                            <p class="text-slate-500 text-sm mt-2">Silakan isi formulir di bawah ini dengan data yang benar.</p>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Materi 3: CTkButton 🔘",
            "subtitle": "Widget untuk Aksi",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-white border border-slate-200 p-6 rounded-xl shadow-lg text-center">
                        <p class="text-slate-800 font-bold mb-4">Contoh CTkButton:</p>
                        <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg shadow transition">SIMPAN DATA</button>
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Saklar Interaktif</h3>
                        <p class="text-slate-600 text-lg">Kalau Label itu poster, Button itu saklar lampu. Sengaja dibuat mencolok agar ditekan oleh pengguna untuk memberikan perintah ke aplikasi.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Materi 4: Perintah .pack() 📦",
            "subtitle": "Proses Penataan Widget",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="text-6xl">🚚</div>
                    <p class="text-lg text-slate-700">Meskipun kamu sudah memesan kursi dan meja, mereka tidak akan muncul di ruang tamu kalau kurirnya belum meletakkannya di sana.</p>
                    <div class="bg-yellow-50 border border-yellow-200 p-5 rounded-xl shadow-sm text-yellow-800 font-medium">
                        Kamu WAJIB memanggil perintah <code>.pack()</code> pada setiap widget agar mereka benar-benar ditempelkan dan muncul di layar secara berurutan!
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Teks Pertamaku 📝",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🏠</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Setup Ruangan</h3>
                        <p class="text-slate-600 text-lg">Buat file baru bernama <code>belajar_widget.py</code> dan siapkan ruangan (jendela) utamanya.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
<span class="text-pink-400">import</span> <span class="text-blue-300">customtkinter</span> <span class="text-pink-400">as</span> <span class="text-blue-300">ctk</span><br><br>
<span class="text-yellow-300">app</span> = ctk.CTk()<br>
<span class="text-yellow-300">app</span>.title(<span class="text-green-300">"Widget Lab"</span>)<br>
<span class="text-yellow-300">app</span>.geometry(<span class="text-green-300">"400x300"</span>)
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Teks Pertamaku 📝",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
<span class="text-slate-400"># Buat teks</span><br>
pesan = ctk.CTkLabel(<span class="text-yellow-300">app</span>, text=<span class="text-green-300">"Daily Task Manager"</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🖋️</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Bikin Label</h3>
                        <p class="text-slate-600 text-lg">Panggil <code>CTkLabel</code>. Kita harus kasih tau dia mau numpang di jendela mana (<code>app</code>), dan isi tulisannya (<code>text="..."</code>).</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Teks Pertamaku 📝",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">📦</div>
                        <h3 class="text-2xl font-bold text-slate-800">3. Pack & Mainloop</h3>
                        <p class="text-slate-600 text-lg">Ingat! Tempelkan labelmu dengan <code>.pack()</code>, lalu tutup kodingan di baris terbawah dengan <code>.mainloop()</code>.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
pesan.pack()<br><br>
<span class="text-yellow-300">app</span>.mainloop()
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Teks Pertamaku 📝",
            "subtitle": "Hasil Akhir (Mockup)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-slate-600 text-lg">Label otomatis muncul di bagian tengah atas jendela.</p>
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-400">
                        <div class="mock-window-header bg-slate-200 border-slate-300">
                            <div class="mock-window-title text-slate-800 font-bold">Widget Lab</div>
                            <div class="mock-window-controls">
                                <div class="win-btn win-min"></div>
                                <div class="win-btn win-max"></div>
                                <div class="win-btn win-close"></div>
                            </div>
                        </div>
                        <div class="mock-window-content bg-[#EBEBEB] h-48 flex flex-col items-center pt-4 justify-start">
                            <p class="text-slate-800 text-sm">Daily Task Manager</p>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Tombol Aksi 🔘",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">👆</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Tambah Tombol</h3>
                        <p class="text-slate-600 text-lg">Taruh kodingan tombol ini <b>di atas</b> <code>mainloop()</code> dan di bawah <code>pesan.pack()</code>.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
<span class="text-slate-400"># Buat tombol</span><br>
tombol1 = ctk.CTkButton(<span class="text-yellow-300">app</span>, text=<span class="text-green-300">"Tambahkan Task"</span>)
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Tombol Aksi 🔘",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
tombol1.pack()
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">📦</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Pack Tombol</h3>
                        <p class="text-slate-600 text-lg">Setiap widget baru harus punya perintah <code>pack()</code>-nya masing-masing.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Tombol Aksi 🔘",
            "subtitle": "Hasil Akhir (Mockup)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-slate-600 text-lg">Sistem <code>.pack()</code> otomatis menumpuk elemen baru di bawah elemen sebelumnya.</p>
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-400">
                        <div class="mock-window-header bg-slate-200 border-slate-300">
                            <div class="mock-window-title text-slate-800 font-bold">Widget Lab</div>
                            <div class="mock-window-controls">
                                <div class="win-btn win-min"></div>
                                <div class="win-btn win-max"></div>
                                <div class="win-btn win-close"></div>
                            </div>
                        </div>
                        <div class="mock-window-content bg-[#EBEBEB] h-48 flex flex-col items-center pt-4 justify-start space-y-1">
                            <p class="text-slate-800 text-sm mb-1">Daily Task Manager</p>
                            <button class="bg-[#1f6aa5] text-white px-4 py-1.5 rounded-md shadow-sm text-sm font-semibold">Tambahkan Task</button>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Gaya & Warna 🎨",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔠</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Ukuran Font</h3>
                        <p class="text-slate-600 text-lg">Tampilan kita masih kekecilan. Yuk perbesar huruf labelnya pakai <code>font=("NamaFont", Ukuran)</code>.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
pesan = ctk.CTkLabel(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text=<span class="text-green-300">"Daily Task Manager"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Arial"</span>, <span class="text-purple-400">20</span>)<br>
)
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Gaya & Warna 🎨",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
tombol1 = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text=<span class="text-green-300">"Tambahkan Task"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;fg_color=<span class="text-green-300">"red"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text_color=<span class="text-green-300">"white"</span><br>
)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🌈</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Ganti Warna</h3>
                        <p class="text-slate-600 text-lg">Kamu bisa ganti warna tombol lewat <code>fg_color</code> (foreground color), dan warna tulisan pakai <code>text_color</code>.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Gaya & Warna 🎨",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">↔️</div>
                        <h3 class="text-2xl font-bold text-slate-800">3. Kasih Jarak (Padding)</h3>
                        <p class="text-slate-600 text-lg">Elemen kita terlalu mepet atas. Tambahkan <code>pady</code> (Padding Y / Vertikal) ke dalam fungsi pack.</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-base text-left shadow-xl border border-slate-700">
pesan.pack(pady=<span class="text-purple-400">20</span>)<br>
tombol1.pack(pady=<span class="text-purple-400">10</span>)
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Gaya & Warna 🎨",
            "subtitle": "Hasil Akhir (Mockup)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-slate-600 text-lg">Sekarang UI kamu terlihat lebih luas dan menarik!</p>
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-400">
                        <div class="mock-window-header bg-slate-200 border-slate-300">
                            <div class="mock-window-title text-slate-800 font-bold">Widget Lab</div>
                            <div class="mock-window-controls">
                                <div class="win-btn win-min"></div>
                                <div class="win-btn win-max"></div>
                                <div class="win-btn win-close"></div>
                            </div>
                        </div>
                        <div class="mock-window-content bg-[#EBEBEB] h-48 flex flex-col items-center pt-8 justify-start space-y-4">
                            <p class="text-slate-800 text-xl font-bold">Daily Task Manager</p>
                            <button class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-md shadow-sm text-sm font-semibold">Tambahkan Task</button>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Tantangan Pro! 🔥",
            "subtitle": "Buktikan kamu programmer sejati",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6 mt-10">
                    <div class="text-8xl animate-bounce">😎</div>
                    <h3 class="text-4xl font-extrabold text-slate-800 tracking-tight">Eksplorasi Fitur Tersembunyi!</h3>
                    <p class="text-slate-600 text-xl max-w-2xl mx-auto">CustomTkinter punya puluhan gaya parameter yang belum kita sentuh. Pecahkan 3 tantangan desain ini!</p>
                </div>
            `
        },
        {
            "title": "Pro Challenge #1 💻",
            "subtitle": "Tombol Hover",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-blue-400 transition-colors">
                        <h4 class="text-3xl font-bold text-cyan-600 mb-6 flex items-center gap-3"><span class="text-4xl">🖱️</span> Misi: Animasi Hover!</h4>
                        <p class="mb-4 text-slate-700 text-lg">Pernah lihat tombol berubah warna pas ditunjuk mouse? Tambahkan parameter <code>hover_color="darkred"</code> di dalam kodingan CTkButton kamu.</p>
                        <p class="text-slate-600 text-lg">Jalankan programnya, lalu gerakkan mouse di atas tombol. Berhasil?</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Pro Challenge #2 🎯",
            "subtitle": "Dashboard Mini",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-fuchsia-400 transition-colors">
                        <h4 class="text-3xl font-bold text-fuchsia-600 mb-6 flex items-center gap-3"><span class="text-4xl">🎛️</span> Misi: Tumpukan Widget!</h4>
                        <p class="mb-4 text-slate-700 text-lg">Buatlah 3 buah <code>CTkLabel</code> (misal: Status Server, Pemain Online, Jam) dan 1 <code>CTkButton</code> (Refresh). Gunakan <code>.pack(pady=10)</code> pada mereka semua.</p>
                        <p class="text-slate-600 text-lg">Lihat bagaimana mereka tersusun rapi dari atas ke bawah!</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Pro Challenge #3 ✅",
            "subtitle": "Tombol Bundar",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-yellow-400 transition-colors">
                        <h4 class="text-3xl font-bold text-yellow-600 mb-6 flex items-center gap-3"><span class="text-4xl">🔴</span> Misi: Corner Radius!</h4>
                        <p class="mb-4 text-slate-700 text-lg">Tombol kotak itu membosankan. Tambahkan parameter <code>corner_radius=20</code> di dalam CTkButton kamu.</p>
                        <p class="text-slate-600 text-lg">Semakin besar angkanya, semakin membulat ujung tombolnya seperti kapsul!</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Summary 📝",
            "subtitle": "Rangkuman Sesi 2",
            "content": `
                <div class="max-w-4xl mx-auto text-left bg-white p-8 rounded-2xl shadow-lg border border-slate-100">
                    <ul class="custom-list list-none text-lg text-slate-700 space-y-6">
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🧩</span>
                            <div><b>Widget:</b> Komponen kecil yang menyusun UI seperti Lego.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🏷️</span>
                            <div><b>CTkLabel:</b> Untuk menampilkan teks, instruksi, atau judul yang tidak bisa diklik.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🔘</span>
                            <div><b>CTkButton:</b> Elemen interaktif untuk memicu aksi saat ditekan.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🎨</span>
                            <div><b>Styling:</b> Widget bisa dipercantik pakai <code>fg_color</code>, <code>font</code>, dan <code>corner_radius</code>.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">📦</span>
                            <div><b>.pack():</b> Perintah wajib agar widget muncul dan tersusun dari atas ke bawah. Jangan lupa <code>pady</code> untuk jarak!</div>
                        </li>
                    </ul>
                </div>
            `
        },
        {
            "title": "Quote of the Day 🌟",
            "subtitle": "Kata-kata Inspirasi",
            "content": `
                <div class="flex flex-col items-center justify-center h-full text-center p-8 max-w-4xl mx-auto">
                    <blockquote class="text-4xl font-serif italic text-blue-800 mb-8 leading-relaxed">
                        "Make it work, make it right, make it fast."
                    </blockquote>
                    <cite class="text-slate-500 font-bold not-italic text-xl uppercase tracking-widest">— Kent Beck</cite>
                    <div class="mt-12 text-7xl animate-bounce">⚡</div>
                    <p class="mt-8 text-slate-600 font-medium text-lg">Sampai jumpa di Sesi 3: Menerima Input Data!</p>
                </div>
            `
        }
    ],
    "3": [
        {
            "title": "Welcome to Session 3! 🚀",
            "subtitle": "Entry Widgets (Input)",
            "content": `
                <div class="text-center space-y-6 max-w-3xl mx-auto">
                    <div class="text-6xl">💬</div>
                    <div class="text-2xl font-bold text-slate-800">Komunikasi Dua Arah!</div>
                    <p class="text-lg text-slate-600">Aplikasi yang cuma ngasih tau info aja itu membosankan. Hari ini kita akan belajar gimana caranya biar aplikasi kita bisa "mendengarkan" ketikan dari pengguna lewat kotak teks input!</p>
                </div>
            `
        },
        {
            "title": "Flashback Sesi 2 ⏪",
            "subtitle": "Ingat Perabotan Kita?",
            "content": `
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🏷️</div>
                    <p class="font-semibold text-slate-700 text-lg">Widget apa yang digunakan untuk memajang poster / instruksi (teks statis)?</p>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        <button onclick="showMiniFeedback('s3fb1-feedback', 'Benar! Label untuk teks biasa.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all">CTkLabel</button>
                        <button onclick="showMiniFeedback('s3fb1-feedback', 'Salah! Tombol itu untuk diklik.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all">CTkButton</button>
                    </div>
                    <div id="s3fb1-feedback" class="min-h-[48px] mt-4"></div>
                </div>
            `
        },
        {
            "title": "Flashback Sesi 2 ⏪",
            "subtitle": "Kurir Penata Layar",
            "content": `
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">📦</div>
                    <p class="font-semibold text-slate-700 text-lg">Jika kita lupa memanggil perintah <code>.pack()</code> pada tombol kita, apa yang terjadi?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('s3fb2-feedback', 'Kurang tepat! Komputer tidak akan rusak hehe.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all">Python langsung crash / error</button>
                        <button onclick="showMiniFeedback('s3fb2-feedback', 'Betul! Program jalan, tapi tombolnya sembunyi/ga diletakkan di layar.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all">Tombolnya tidak muncul di layar sama sekali</button>
                    </div>
                    <div id="s3fb2-feedback" class="min-h-[48px] mt-4"></div>
                </div>
            `
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": `
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami widget <code>CTkEntry</code> untuk menerima input ketikan.</li>
                        <li>Memahami konsep <b>Abstraction</b> (menyimpan kode warna di awal agar praktis).</li>
                        <li>Mengatur posisi perataan (Anchor) teks biar rapi.</li>
                        <li>Membuat antarmuka Login Portal sungguhan yang keren!</li>
                    </ul>
                </div>
            `
        },
        {
            "title": "Materi 1: Hierarchy of Info 👑",
            "subtitle": "Cara mata memindai layar",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 border border-slate-700 p-6 rounded-xl shadow-lg text-center space-y-3">
                        <h1 class="text-4xl text-cyan-400 font-bold">JUDUL BESAR</h1>
                        <p class="text-sm text-slate-400">Instruksi kecil penjelas</p>
                        <input type="text" class="w-full bg-slate-800 border border-slate-600 rounded p-2" disabled>
                        <button class="w-full bg-cyan-600 text-white rounded p-2">AKSI UTAMA</button>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl">👀</div>
                        <p class="text-slate-600 text-lg">Pengguna akan melihat elemen paling besar dan terang duluan. Kita harus memandu mereka: dari Judul -> baca instruksi -> isi form -> pencet tombol.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Materi 2: CTkEntry ⌨️",
            "subtitle": "Kotak Isi Pesan",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Media Komunikasi</h3>
                        <p class="text-slate-600 text-lg">Kalau Label ngomong dari komputer ke manusia, <b>Entry</b> ngomong dari manusia ke komputer. Di sini kita mengetikkan nama, sandi, atau angka!</p>
                    </div>
                    <div class="bg-white border border-slate-200 p-6 rounded-xl shadow-lg text-center">
                        <p class="text-slate-800 font-bold mb-4">Contoh CTkEntry:</p>
                        <input type="text" class="border-2 border-blue-400 p-2 rounded w-full outline-none" placeholder="Ketik namamu di sini...">
                    </div>
                </div>
            `
        },
        {
            "title": "Materi 3: Abstraction 🎨",
            "subtitle": "Kumpulkan Konstanta di Atas!",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-lg text-slate-700">Bayangkan kita bikin aplikasi biru semua. Terus bos minta ganti jadi merah. Capek kan gantiin <code>"blue"</code> satu per satu di 20 baris kode?</p>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-lg text-cyan-300 inline-block w-full max-w-lg">
# Konstanta disimpan di awal<br>
WARNA_UTAMA = "#1f6aa5"<br>
WARNA_TEKS = "#AAAAAA"<br><br>
<span class="text-slate-500"># Tinggal dipanggil pakai nama variabel</span><br>
tombol = ctk.CTkButton(app, fg_color=WARNA_UTAMA)
                    </div>
                    <p class="text-sm text-yellow-600 font-bold">Variabel nilai tetap selalu ditulis dengan HURUF KAPITAL (Konstanta).</p>
                </div>
            `
        },
        {
            "title": "Project 1: Pondasi & Warna 🏢",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🚀</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Setup Portal Login</h3>
                        <p class="text-slate-600 text-lg">Buat file <code>login_portal.py</code>. Siapkan <i>Dark Mode</i> dan simpan Konstanta warna biru keren (<i>Hex code</i>).</p>
                    </div>
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
<span class="text-yellow-300">app</span> = ctk.CTk()<br>
<span class="text-yellow-300">app</span>.geometry(<span class="text-green-300">"400x450"</span>)<br>
ctk.set_appearance_mode(<span class="text-green-300">"dark"</span>)<br><br>
<span class="text-purple-300">WARNA_BIRU</span> = <span class="text-green-300">"#1f6aa5"</span><br>
<span class="text-purple-300">WARNA_ABU</span> = <span class="text-green-300">"#AAAAAA"</span>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Pondasi & Warna 🏢",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
judul = ctk.CTkLabel(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text=<span class="text-green-300">"ARCHIUS"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">30</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;text_color=<span class="text-purple-300">WARNA_BIRU</span><br>
)<br>
judul.pack(pady=(<span class="text-purple-400">30</span>, <span class="text-purple-400">20</span>))
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">👑</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Header Utama</h3>
                        <p class="text-slate-600 text-lg">Panggil variabel warnamu tanpa tanda kutip. Trik jagoan: <code>pady=(30, 20)</code> memberi jarak 30 ke atas dan 20 ke bawah secara spesifik!</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 1: Pondasi & Warna 🏢",
            "subtitle": "Hasil Akhir (Mockup)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-slate-600 text-lg">Warna biru diambil langsung dari konstanta yang kamu set.</p>
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Archius Entry Portal</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-64 flex flex-col items-center pt-8 justify-start space-y-4">
                            <h1 class="text-[#1f6aa5] text-3xl font-bold uppercase tracking-wide">Archius</h1>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Kotak Input ⌨️",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">👉</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Label Rata Kiri</h3>
                        <p class="text-slate-600 text-lg">Instruksi form biasanya nempel di kiri. Gunakan <code>anchor="w"</code> (West/Barat) dan <code>fill="x"</code> biar lebarnya pas.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
lbl_user = ctk.CTkLabel(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>, text=<span class="text-green-300">"Username"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text_color=<span class="text-purple-300">WARNA_ABU</span>, anchor=<span class="text-green-300">"w"</span><br>
)<br>
lbl_user.pack(padx=<span class="text-purple-400">75</span>, fill=<span class="text-green-300">"x"</span>)
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Kotak Input ⌨️",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
input_user = ctk.CTkEntry(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>, width=<span class="text-purple-400">250</span>, height=<span class="text-purple-400">40</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;placeholder_text=<span class="text-green-300">"Enter username"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;border_color=<span class="text-purple-300">WARNA_BIRU</span><br>
)<br>
input_user.pack(pady=(<span class="text-purple-400">5</span>, <span class="text-purple-400">15</span>))
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🖊️</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Kotak Input 1</h3>
                        <p class="text-slate-600 text-lg">Ini <code>CTkEntry</code>-nya! <code>placeholder_text</code> adalah teks bayangan di dalam kotak sebelum diketik.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Kotak Input ⌨️",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🕵️‍♂️</div>
                        <h3 class="text-2xl font-bold text-slate-800">3. Privasi Sandi!</h3>
                        <p class="text-slate-600 text-lg">Buat pasangan Label & Entry buat Password. Biar aman dari lirik-lirik, tambahkan atribut <code>show="*"</code> di Entry-nya!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-slate-500"># Bikin Label password sama kayak atas</span><br>
<span class="text-slate-500">...</span><br><br>
input_pass = ctk.CTkEntry(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>, width=<span class="text-purple-400">250</span>, height=<span class="text-purple-400">40</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;show=<span class="text-green-300">"*"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;border_color=<span class="text-purple-300">WARNA_BIRU</span><br>
)<br>
input_pass.pack(pady=(<span class="text-purple-400">5</span>, <span class="text-purple-400">25</span>))
                    </div>
                </div>
            `
        },
        {
            "title": "Project 2: Kotak Input ⌨️",
            "subtitle": "Hasil Akhir (Mockup)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Archius Entry Portal</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-72 flex flex-col items-center pt-6 justify-start">
                            <h1 class="text-[#1f6aa5] text-2xl font-bold mb-4">ARCHIUS</h1>
                            <div class="w-full px-8 mb-4">
                                <label class="text-[#AAAAAA] text-xs font-bold block mb-1">Username</label>
                                <input type="text" class="w-full bg-[#343638] border border-[#1f6aa5] text-white px-3 py-2 rounded-md outline-none" placeholder="Enter username">
                            </div>
                            <div class="w-full px-8">
                                <label class="text-[#AAAAAA] text-xs font-bold block mb-1">Password</label>
                                <input type="password" class="w-full bg-[#343638] border border-[#1f6aa5] text-white px-3 py-2 rounded-md outline-none" value="12345">
                            </div>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Tombol & Footer 🖱️",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">✅</div>
                        <h3 class="text-2xl font-bold text-slate-800">1. Tombol Sign In</h3>
                        <p class="text-slate-600 text-lg">Samakan lebarnya (<code>width=250</code>) dengan kotak input biar estetik. Setel <code>fg_color</code> dengan konstanta birumu!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
btn = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>, text=<span class="text-green-300">"SIGN IN"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;width=<span class="text-purple-400">250</span>, height=<span class="text-purple-400">45</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;fg_color=<span class="text-purple-300">WARNA_BIRU</span><br>
)<br>
btn.pack()
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Tombol & Footer 🖱️",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": `
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700">
footer = ctk.CTkLabel(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">app</span>, text=<span class="text-green-300">"Secure Portal v1.0"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Arial"</span>, <span class="text-purple-400">10</span>)<br>
)<br>
footer.pack(side=<span class="text-green-300">"bottom"</span>, pady=<span class="text-purple-400">20</span>)<br><br>
<span class="text-yellow-300">app</span>.mainloop()
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">⚓</div>
                        <h3 class="text-2xl font-bold text-slate-800">2. Footer Menempel</h3>
                        <p class="text-slate-600 text-lg">Buat Label keterangan versi. Pakai <code>side="bottom"</code> di pack-nya agar dia turun dan nyangkut di paling bawah jendela. Tutup dengan Mainloop!</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Project 3: Tombol & Footer 🖱️",
            "subtitle": "Hasil Akhir (Mockup Portal)",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-4">
                    <p class="text-slate-600">Selamat! Aplikasi Login pertamamu selesai!</p>
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600 relative">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Archius Entry Portal</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-[340px] flex flex-col items-center pt-6 justify-start relative">
                            <h1 class="text-[#1f6aa5] text-2xl font-bold mb-4">ARCHIUS</h1>
                            <div class="w-full px-8 mb-4">
                                <label class="text-[#AAAAAA] text-xs font-bold block mb-1">Username</label>
                                <input type="text" class="w-full bg-[#343638] border border-[#1f6aa5] text-white px-3 py-2 rounded-md outline-none" placeholder="Enter username">
                            </div>
                            <div class="w-full px-8 mb-5">
                                <label class="text-[#AAAAAA] text-xs font-bold block mb-1">Password</label>
                                <input type="password" class="w-full bg-[#343638] border border-[#1f6aa5] text-white px-3 py-2 rounded-md outline-none" value="12345">
                            </div>
                            <button class="bg-[#1f6aa5] hover:bg-[#144870] text-white font-bold py-2 w-48 rounded-md shadow transition">SIGN IN</button>
                            
                            <p class="text-[#555] text-[10px] absolute bottom-4">Secure Portal v1.0</p>
                        </div>
                    </div>
                </div>
            `
        },
        {
            "title": "Tantangan Pro! 🔥",
            "subtitle": "Tingkatkan Level Form-mu",
            "content": `
                <div class="max-w-4xl mx-auto text-center space-y-6 mt-10">
                    <div class="text-8xl animate-bounce">🔐</div>
                    <h3 class="text-4xl font-extrabold text-slate-800 tracking-tight">Kunci dan Perbaiki Sistem!</h3>
                    <p class="text-slate-600 text-xl max-w-2xl mx-auto">Portal buatanmu masih butuh modifikasi tingkat lanjut. Selesaikan 3 misi rahasia ini!</p>
                </div>
            `
        },
        {
            "title": "Pro Challenge #1 💻",
            "subtitle": "Jendela Anti Tarik",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-blue-400 transition-colors">
                        <h4 class="text-3xl font-bold text-cyan-600 mb-6 flex items-center gap-3"><span class="text-4xl">🛑</span> Misi: Kunci Form!</h4>
                        <p class="mb-4 text-slate-700 text-lg">Di Sesi 1 kamu udah belajar cara nge-lock ukuran. Sekarang terapkan di Portal Login ini agar desainnya ga rusak kalau ditarik user!</p>
                        <p class="text-slate-600 text-lg">Panggil <code>app.resizable()</code> di tempat yang tepat.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Pro Challenge #2 🎯",
            "subtitle": "Input Telepon",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-fuchsia-400 transition-colors">
                        <h4 class="text-3xl font-bold text-fuchsia-600 mb-6 flex items-center gap-3"><span class="text-4xl">📱</span> Misi: Field Tambahan</h4>
                        <p class="mb-4 text-slate-700 text-lg">Wah, ternyata sistem butuh Nomor HP! Tambahkan sepasang Label dan Entry baru di antara Username dan Password.</p>
                        <p class="text-slate-600 text-lg">Pastikan padding (jarak) nya sama persis biar tetap rapi dan tidak timpang.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Pro Challenge #3 ✅",
            "subtitle": "Tombol Batal",
            "content": `
                <div class="max-w-3xl mx-auto text-left space-y-6">
                    <div class="p-8 bg-white border-2 border-slate-200 rounded-2xl shadow-xl hover:border-yellow-400 transition-colors">
                        <h4 class="text-3xl font-bold text-yellow-600 mb-6 flex items-center gap-3"><span class="text-4xl">🔙</span> Misi: Jalan Keluar</h4>
                        <p class="mb-4 text-slate-700 text-lg">Terkadang user salah mencet dan ingin balik. Tambahkan satu CTkButton lagi dengan tulisan "BATAL" di bawah tombol Sign In.</p>
                        <p class="text-slate-600 text-lg">Setel warnanya jadi Merah tua / abu-abu gelap biar jadi tombol sekunder. Beri <code>pady=10</code>.</p>
                    </div>
                </div>
            `
        },
        {
            "title": "Summary 📝",
            "subtitle": "Rangkuman Sesi 3",
            "content": `
                <div class="max-w-4xl mx-auto text-left bg-white p-8 rounded-2xl shadow-lg border border-slate-100">
                    <ul class="custom-list list-none text-lg text-slate-700 space-y-6">
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">⌨️</span>
                            <div><b>CTkEntry:</b> Widget komunikasi dua arah tempat user ngetik data (Textbox).</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🎨</span>
                            <div><b>Konstanta Warna:</b> Taruh hex warna di huruf KAPITAL di awal, biar gampang ubah tema masal.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">🕵️‍♂️</span>
                            <div><b>show="*":</b> Senjata andalan buat kolom password agar tidak diintip.</div>
                        </li>
                        <li class="flex items-start gap-4">
                            <span class="text-3xl">⚓</span>
                            <div><b>Anchor & Side:</b> <code>anchor="w"</code> buat perataan teks kiri, <code>side="bottom"</code> untuk narik komponen ke dasar layar.</div>
                        </li>
                    </ul>
                </div>
            `
        },
        {
            "title": "Quote of the Day 🌟",
            "subtitle": "Kata-kata Inspirasi",
            "content": `
                <div class="flex flex-col items-center justify-center h-full text-center p-8 max-w-4xl mx-auto">
                    <blockquote class="text-4xl font-serif italic text-blue-800 mb-8 leading-relaxed">
                        "First, solve the problem. Then, write the code."
                    </blockquote>
                    <cite class="text-slate-500 font-bold not-italic text-xl uppercase tracking-widest">— John Johnson</cite>
                    <div class="mt-12 text-7xl animate-pulse">🧠</div>
                    <p class="mt-8 text-slate-600 font-medium text-lg">Sampai jumpa di Sesi 4: Mengatur Tata Letak dengan Grid!</p>
                </div>
            `
        }
    ],"""

# Find the start and end of "2": [ ... ],
pattern_s2 = re.compile(r'    "2": \[\n.*?\n    \],\n', re.DOTALL)
content = pattern_s2.sub(new_meeting_2 + '\n', content)

# Find the start and end of "3": [ ... ],
# Wait, "3" ends before "4": [ or at the end. Since the placeholder has "3": [ ... ] but we don't know the exact format, 
# let's look at how "3" ends. In the file viewing, it ended with:
#                 }
#             ],
#             3: [
#                 {
#                     title: "Meeting 3: Intro to Turtle 🐢",
# ...
# wait, my level 3 deck currently doesn't have "4": [ yet? Let me just use a safe regex that replaces up to the next number key, or I'll just do it safely.
