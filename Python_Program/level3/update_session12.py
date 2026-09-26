import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_12 = """    "12": [
        {
            "title": "Meeting 12: The Grand Showcase 🚀",
            "subtitle": "Presentasi Final & Portofolio",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🎓</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Garis Finish Ada di Depan Mata!</p>
                <p class="text-lg text-slate-600">Selamat! Kalian sudah berhasil menyihir layar hitam terminal menjadi sebuah Aplikasi Desktop Visual (GUI) sungguhan yang tersambung ke Internet.</p>
                <p class="text-lg text-slate-600 mt-2">Hari ini bukan tentang menulis baris kode baru, melainkan tentang <b>Showcase</b> (memamerkan) hasil karyamu, memolesnya, dan belajar cara mempresentasikan mahakaryamu layaknya seorang Profesional Developer!</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-blue-50 border border-blue-100 p-4 text-blue-700">Improvement Sprint</div>
                    <div class="rounded-xl bg-purple-50 border border-purple-100 p-4 text-purple-700">Digital Portfolio</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 11 ⏪",
            "subtitle": "Review API & Back-End",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🍽️</div><h4 class="font-bold text-slate-800">API (Pelayan)</h4><p class="text-sm text-slate-500 mt-2">Jembatan pengantar pesan antara Aplikasimu dan Server BMKG.</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">📦</div><h4 class="font-bold text-slate-800">Requests</h4><p class="text-sm text-slate-500 mt-2">Library (Kendaraan Ekspedisi) untuk meminta data (HTTP GET).</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">📜</div><h4 class="font-bold text-slate-800">JSON</h4><p class="text-sm text-slate-500 mt-2">Format data balasan dari Internet yang dibaca seperti Dictionary Python.</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Mengapa kita WAJIB meletakkan kode pemanggilan API (seperti <code>requests.get()</code>) di dalam blok <b>try-except</b>?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb12', 'Salah! Try-except tidak mengubah bahasa pemrograman.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Untuk menerjemahkan JSON ke bahasa Indonesia.</button>
                        <button onclick="showMiniFeedback('fb1-fb12', 'Tepat! Kalau internet mati/putus, aplikasi tidak akan mendadak Crash/Force Close.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Mencegah aplikasi tertutup paksa (Crash) jika tidak ada koneksi internet.</button>
                        <button onclick="showMiniFeedback('fb1-fb12', 'Salah! Try-except bukan untuk validasi input string kosong.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Untuk mengecek apakah input nama kota dari user itu kosong.</button>
                    </div>
                    <div id="fb1-fb12" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Melakukan <b>Improvement Sprint</b> (Sesi polesan terakhir) untuk memperbaiki / merapikan aplikasimu.</li>
                        <li>Mampu <b>mempresentasikan</b> aplikasi buatan sendiri secara percaya diri (Demo & Cerita Teknis).</li>
                        <li>Mengevaluasi kelebihan dan kelemahan proyek yang telah dibuat.</li>
                        <li>Memahami cara menyusun <b>Portofolio Digital</b> (seperti GitHub & README) sebagai bekal karya digital seumur hidup.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Improvement Sprint 🛠️",
            "subtitle": "Sentuhan Akhir",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menyapu Debu Terakhir</h3>
                        <p class="text-slate-600 text-lg">Sebelum dipamerkan, <i>developer</i> profesional biasanya melakukan <b>Sprint</b> (Lari cepat) perbaikan. Luangkan 15-20 menit pertama hari ini untuk:</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li>Merapikan letak tombol yang agak miring (Ubah padding/margin).</li>
                            <li>Mengganti kombinasi warna yang terlalu silau.</li>
                            <li>Mengetes apakah <b>Semua Tantangan (Pro Challenge)</b> dari sesi-sesi sebelumnya sudah berfungsi sempurna.</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center shadow-inner">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/0fc434d8-0326-4153-996b-733bbfe7afcd.jpg" class="mx-auto rounded-lg h-48 object-contain">
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Struktur Presentasi 🎤",
            "subtitle": "Kerangka 5 Menit",
            "content": \`
                <div class="max-w-4xl mx-auto text-left space-y-5">
                    <h3 class="text-2xl font-bold text-slate-800 text-center mb-6">Bagaimana Cara Pamer yang Keren?</h3>
                    <div class="grid md:grid-cols-2 gap-4">
                        <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                            <h4 class="font-bold text-blue-600">1. Perkenalan (1 Menit)</h4>
                            <p class="text-slate-600 mt-2 text-sm">Sebutkan nama aplikasimu dan apa kegunaan utamanya. "Halo, ini Archius Weather. Gunanya untuk melihat cuaca asli di belahan bumi manapun secara Real-Time!"</p>
                        </div>
                        <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                            <h4 class="font-bold text-purple-600">2. Demo Langsung (2 Menit)</h4>
                            <p class="text-slate-600 mt-2 text-sm">Jalankan aplikasinya di depan layar (Share Screen). Coba cari kota yang aneh, atau uji coba mengetik asal untuk membuktikan aplikasimu aman dari Crash!</p>
                        </div>
                        <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                            <h4 class="font-bold text-orange-600">3. Cerita Teknis (1 Menit)</h4>
                            <p class="text-slate-600 mt-2 text-sm">Tunjukkan sepotong kode kebanggaanmu. Jelaskan satu fitur tersulit yang berhasil kamu taklukkan (Contoh: "Bagian tergila itu saat nyambungin API JSON...").</p>
                        </div>
                        <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                            <h4 class="font-bold text-green-600">4. Refleksi & QnA (1 Menit)</h4>
                            <p class="text-slate-600 mt-2 text-sm">Ceritakan 1 hal yang belum sempat kamu buat, lalu buka sesi pertanyaan untuk teman-teman dan instruktur.</p>
                        </div>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Portofolio Digital 📂",
            "subtitle": "Warisan Digitalmu",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menyimpan Aset</h3>
                        <p class="text-slate-600 text-lg">Proyek ini bukan cuma "tugas les". Ini adalah <b>Aset Portofolio</b>.</p>
                        <p class="text-slate-600 text-lg">Di dunia IT, ijazah itu nomor dua. Bukti nyata berupa karya yang bisa di-klik dan kode yang bisa dibaca adalah <b>Nomor Satu</b>. Platform standar seluruh dunia untuk menyimpan kode disebut <b>GitHub</b>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl text-left shadow-xl border border-slate-700">
                        <img src="https://brand.github.com/_next/static/media/logo-03.cc5e5332.png" class="mx-auto rounded-lg object-contain w-full h-32 invert mb-4">
                        <p class="text-slate-300 text-sm text-center">GitHub: Sosial medianya para Programmer di seluruh dunia.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: File README.md 📝",
            "subtitle": "Buku Panduan Karyamu",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-indigo-50 p-5 rounded-xl font-mono text-sm text-left shadow-md border border-indigo-200 h-64 overflow-y-auto">
<span class="text-indigo-800 font-bold"># Archius Live Weather App</span><br><br>
Aplikasi cuaca desktop yang dibuat dengan Python dan CustomTkinter.<br><br>
<span class="text-indigo-800 font-bold">## Fitur:</span><br>
- Real-Time data via OpenWeatherMap API<br>
- Dynamic Background Colors<br><br>
<span class="text-indigo-800 font-bold">## Cara Menjalankan:</span><br>
1. pip install customtkinter requests Pillow<br>
2. Masukkan API Key di baris 45<br>
3. python main.py
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Manual Book</h3>
                        <p class="text-slate-600 text-lg">Jika kamu menaruh proyekmu di internet, kamu WAJIB membuat file teks bernama <code>README.md</code>.</p>
                        <p class="text-slate-600 text-lg">README adalah halaman pertama yang dibaca orang. Isinya: Judul, Kegunaan, dan Cara Meng-<i>install</i> proyekmu.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Mini Quiz: Konsep 🧠",
            "subtitle": "Cek Pemahaman!",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Dalam presentasi teknis, mengapa kita harus jujur menyebutkan "Fitur yang belum selesai" di sesi Refleksi?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb12', 'Salah! Instruktur tidak akan mengurangi nilai karena kamu jujur.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Agar teman-teman bisa merendahkan karya kita.</button>
                        <button onclick="showMiniFeedback('fb2-fb12', 'Tepat! Jujur menunjukkan bahwa kamu paham batasan dan punya rencana perbaikan.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Karena menyadari kelemahan dan merencanakan fitur masa depan adalah tanda pola pikir developer sejati.</button>
                        <button onclick="showMiniFeedback('fb2-fb12', 'Salah! Bukan soal kode ditutup-tutupi.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Agar kita tidak disuruh membagikan source code ke orang lain.</button>
                    </div>
                    <div id="fb2-fb12" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Must Do 1: Improvement Sprint 🏃",
            "subtitle": "Tugas Wajib",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="text-7xl">⏱️</div>
                    <h3 class="text-3xl font-bold text-slate-800">Sprint 15 Menit Dimulai!</h3>
                    <p class="text-xl text-slate-600">Pastikan Aplikasimu (baik Task Manager / Archius Weather) dalam kondisi <b>Sempurna</b>.</p>
                    <ul class="text-left max-w-lg mx-auto list-disc text-lg text-slate-700 bg-white p-6 rounded-xl shadow-sm border border-slate-200">
                        <li>Cek <i>Typo</i> (salah ketik) pada Label.</li>
                        <li>Pastikan gambar cuaca/ikon tidak <i>Error</i> (lokasi file Path benar).</li>
                        <li>Coba salahkan input celah aplikasimu. Pastikan tidak Crash!</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Must Do 2: Latihan Presentasi 🗣️",
            "subtitle": "Tugas Wajib",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Gladi Resik</h3>
                        <p class="text-slate-600 text-lg">Pilih satu Aplikasi terbaikmu (Task Manager / Weather). Buka layar kameramu (di Zoom/GMeet).</p>
                        <p class="text-slate-600 text-lg font-bold text-blue-600">Latih ucapanmu sendiri selama 3 menit tanpa teks. Gunakan rumus 4 tahap: Intro, Demo, Coding, Refleksi.</p>
                    </div>
                    <div class="bg-indigo-50 p-5 rounded-xl shadow-md border border-indigo-200 text-center">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/49e09a85-6b3b-4c98-8839-b8fe476d58ee.jpg" class="mx-auto rounded-lg object-cover w-full h-40">
                    </div>
                </div>
            \`
        },
        {
            "title": "Must Do 3: Panggung Utama! 🌟",
            "subtitle": "Tugas Wajib",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="text-7xl">🎙️</div>
                    <h3 class="text-3xl font-bold text-slate-800">Tunjukkan Pesonamu!</h3>
                    <p class="text-xl text-slate-600">Saat namamu dipanggil, <b>Share Screen</b> seluruh layarmu.</p>
                    <div class="bg-yellow-50 border border-yellow-200 p-6 rounded-xl max-w-2xl mx-auto">
                        <p class="text-yellow-800 font-bold text-lg">Jangan cuma baca teks PPT! Ceritakan selayaknya kamu sedang menunjukkan mainan barumu ke teman terdekat.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Must Do 4: Menjawab Pertanyaan ❓",
            "subtitle": "Tugas Wajib",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl border border-slate-700 shadow-xl">
                        <p class="text-emerald-400 font-bold mb-2">Pertanyaan Juri (Instruktur/Teman):</p>
                        <p class="text-slate-300 italic">"Gimana caranya gambar hujannya bisa muncul otomatis pas datanya 'Rain'?"</p>
                        <hr class="border-slate-600 my-4">
                        <p class="text-blue-400 font-bold mb-2">Jawabanmu:</p>
                        <p class="text-slate-300">"Saya membedah dictionary pakai .items() Kak, lalu merubah gambarnya dengan perintah .configure(image=...)"</p>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Buktikan Kepemilikan</h3>
                        <p class="text-slate-600 text-lg">Jawab <b>Minimal 1 Pertanyaan</b> terkait teknis kodinganmu dengan santai. Kalau tidak tahu, jawab jujur: "Bagian itu saya juga masih bingung Kak, butuh belajar lagi."</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Must Do 5: Memberi Feedback 💬",
            "subtitle": "Tugas Wajib",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="text-7xl">🤝</div>
                    <h3 class="text-3xl font-bold text-slate-800">Menjadi Apresiator yang Baik</h3>
                    <p class="text-xl text-slate-600">Saat temanmu presentasi, perhatikan baik-baik. Berikan apresiasi (Pujian) dan masukkan saran (Kritik Membangun).</p>
                    <div class="bg-green-50 border border-green-200 p-6 rounded-xl max-w-2xl mx-auto">
                        <p class="text-green-800 font-bold text-lg">"Keren banget warnanya Budi! Tapi mungkin font suhunya bisa dibesarin sedikit biar lebih gampang dibaca."</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Buat README.txt 📓",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Tulis Dokumentasimu!</h3>
                        <p class="text-slate-600 text-lg">Buka VS Code, buat file baru bernama <code>README.txt</code> di dalam folder proyek akhirmu. Tulis 3 hal:</p>
                        <ul class="list-disc pl-5 text-slate-600 font-bold">
                            <li>Nama Aplikasi & Versi</li>
                            <li>Fitur Utama</li>
                            <li>Library yang harus di-install.</li>
                        </ul>
                    </div>
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200 text-center shadow-inner">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/a8a80b0f-3ea8-4604-b56b-50e47b00b86e.png" class="mx-auto rounded-lg h-40 object-contain">
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Unggah ke GitHub 🐙",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
                        <h4 class="font-bold text-indigo-800 mb-3">Tugas Khusus:</h4>
                        <ol class="list-decimal pl-5 text-slate-700 space-y-2">
                            <li>Buat akun di GitHub.com.</li>
                            <li>Klik tombol <b>New Repository</b>.</li>
                            <li>Beri nama `Archius-Weather-App`.</li>
                            <li><i>Drag & Drop</i> (Seret) semua file `.py` dan gambarmu ke sana.</li>
                            <li>Selamat! Karyamu sekarang resmi ada di Internet!</li>
                        </ol>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Mulai Jejak Digitalmu</h3>
                        <p class="text-slate-600 text-lg">Hapus (atau sembunyikan) <i>API Key</i> kamu di kodingan, gantikan dengan tulisan "KODE_RAHASIAMU", lalu <i>upload</i> ke GitHub!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Rilis .exe (PyInstaller) 💿",
            "subtitle": "Tantangan Level 3 (Super Hard)",
            "content": \`
                <div class="max-w-4xl mx-auto text-left space-y-6">
                    <div class="flex items-center gap-4">
                        <div class="text-5xl">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Ubah Python Jadi Aplikasi Betulan (.exe)</h3>
                    </div>
                    <p class="text-slate-600 text-lg">Apakah kamu mau mengirim aplikasimu ke temanmu yang laptopnya TIDAK MENGINSTALL PYTHON? Kamu bisa mengubah `.py` menjadi `.exe`!</p>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm shadow-xl border border-slate-700 text-green-300">
<span class="text-emerald-400"># Buka terminal dan ketik (Eksplorasi Mandiri):</span><br>
pip install pyinstaller<br><br>
<span class="text-emerald-400"># Lalu ketik ini untuk mengubah file main.py mu:</span><br>
pyinstaller --onefile --windowed main.py
                    </div>
                    <p class="text-red-500 font-bold text-sm">Peringatan: Proses ini cukup rumit dan sering terjadi error lokasi gambar. Lakukan hanya jika kamu suka tantangan tingkat tinggi!</p>
                </div>
            \`
        },
        {
            "title": "Bonus Info: Transparansi Digital 🔍",
            "subtitle": "Etika Programmer",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Jujur pada Pengguna</h3>
                        <p class="text-slate-600 text-lg">Di dunia profesional, mencuri data atau berbohong asal usul data itu melanggar etika.</p>
                        <p class="text-slate-600 text-lg">Selalu tuliskan dari mana aplikasimu mengambil data. Misal: <i>"Powered by OpenWeatherMap API"</i> di aplikasimu atau README-mu. Ini disebut <b>Transparansi Digital</b>.</p>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center">
                        <div class="text-6xl mb-4">⚖️</div>
                        <h4 class="font-bold text-blue-800">Kode Etik</h4>
                        <p class="text-slate-600 text-sm mt-2">Jangan mengumpulkan data tanpa izin, jangan membajak karya orang tanpa memberi kredit (Credit Title).</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Summary Level 3 🏆",
            "subtitle": "Ringkasan Perjalanan",
            "content": \`
                <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                    <div class="bg-purple-50 border border-purple-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-purple-700 mb-3 text-xl">Skill Teknis Baru</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-purple-600">CustomTkinter:</span> Menguasai Framework GUI Modern.</li>
                            <li><span class="font-bold text-purple-600">Layouting:</span> Mahir menggunakan <code>.pack()</code>, <code>.grid()</code>, dan <i>Mixed Layout</i>.</li>
                            <li><span class="font-bold text-purple-600">Event & API:</span> Menghidupkan tombol (Event) dan menarik data langsung dari Internet (Requests/JSON).</li>
                        </ul>
                    </div>
                    <div class="bg-emerald-50 border border-emerald-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-emerald-700 mb-3 text-xl">Skill Profesional</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-emerald-600">Defensive Coding:</span> Menggunakan <code>try-except</code> agar tidak memalukan (Crash) saat Demo.</li>
                            <li><span class="font-bold text-emerald-600">Showcase:</span> Mempresentasikan proyek dengan metode <i>Pitching</i> 4 langkah.</li>
                            <li><span class="font-bold text-emerald-600">Portofolio:</span> Mulai sadar akan jejak rekam karya via README dan GitHub.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Farewell Quote 💭",
            "subtitle": "Sampai Jumpa di Level 4!",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-8 mt-10">
                    <div class="text-6xl text-purple-500 opacity-50">"</div>
                    <blockquote class="text-3xl font-bold text-slate-800 italic leading-snug">
                        First, solve the problem. Then, write the code.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— John Johnson (Pioneer of Software Engineering)</p>
                    <p class="text-md text-slate-500 mt-6 font-bold uppercase tracking-widest border-t border-slate-200 pt-6">PYTHON LEVEL 3 - COMPLETED</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "12": \[\s*\{.*?\}\s*\]\s*\}\;', re.DOTALL)
new_content = re.sub(pattern, new_session_12.replace("\\\\`", "`") + '\\n    ]\\n};', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 12 successfully.")
