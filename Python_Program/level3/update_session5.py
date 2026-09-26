import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new JSON part for "5": [...]
new_session_5 = """    "5": [
        {
            "title": "Meeting 5: Event & Interaktivitas ⚡",
            "subtitle": "Menghidupkan Aplikasi",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">⚡</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Aplikasimu Sekarang Bisa Merespons!</p>
                <p class="text-lg text-slate-600">Selama ini aplikasi kita cuma "diam" dipandang. Hari ini, kita akan membuatnya bereaksi setiap kali diklik!</p>
                <div class="mt-8 grid sm:grid-cols-3 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-purple-50 border border-purple-100 p-4 text-purple-700">def (Fungsi)</div>
                    <div class="rounded-xl bg-orange-50 border border-orange-100 p-4 text-orange-700">global</div>
                    <div class="rounded-xl bg-pink-50 border border-pink-100 p-4 text-pink-700">.configure()</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 4 ⏪",
            "subtitle": "Review Materi Kemarin",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🗄️</div><h4 class="font-bold text-slate-800">.grid()</h4><p class="text-sm text-slate-500 mt-2">Menata elemen layaknya tabel</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">📍</div><h4 class="font-bold text-slate-800">row &amp; column</h4><p class="text-sm text-slate-500 mt-2">Koordinat, indeks dimulai dari 0</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">↔️</div><h4 class="font-bold text-slate-800">columnspan</h4><p class="text-sm text-slate-500 mt-2">Menggabungkan ukuran beberapa sel</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">👀</div>
                    <p class="font-semibold text-slate-700 text-xl">Parameter apa yang dipakai supaya tombol menempel atau melar ke kiri (West) dan kanan (East) secara bersamaan?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb5', 'Salah! weight untuk responsivitas/melar layar penuh.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. weight="ew"</button>
                        <button onclick="showMiniFeedback('fb1-fb5', 'Betul! sticky="ew" bikin elemen nempel ke timur dan barat.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. sticky="ew"</button>
                        <button onclick="showMiniFeedback('fb1-fb5', 'Kurang tepat! merapat bukan syntax yang benar.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. align="center"</button>
                    </div>
                    <div id="fb1-fb5" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami <span class="font-bold text-blue-600">Event-Driven Programming</span> (Kodingan berbasis kejadian).</li>
                        <li>Memasukkan <span class="font-mono text-purple-600 bg-purple-50 px-2 py-1 rounded">command</span> pada tombol agar bisa merespons saat diklik.</li>
                        <li>Menggunakan <span class="font-mono text-orange-600 bg-orange-50 px-2 py-1 rounded">global</span> untuk memodifikasi skor dan data.</li>
                        <li>Menggunakan <span class="font-mono text-pink-600 bg-pink-50 px-2 py-1 rounded">.configure()</span> untuk mengubah teks di UI tanpa nge-<i>restart</i> aplikasi.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Kode Linear vs Event-Driven ⚠️",
            "subtitle": "Cara Baru Berpikir",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menunggu Reaksi (Event)</h3>
                        <p class="text-slate-600 text-lg">Dulu, kode Python jalan lurus dari atas ke bawah. Sekarang, aplikasimu harus seperti Spotify: <b>menunggu</b> user menekan tombol <i>Play</i>, baru kodenya bekerja.</p>
                        <p class="text-slate-600 text-lg">Kejadian atau <i>Event</i> bisa berupa klik mouse, tekan <i>Enter</i>, atau menggeser kursor. Program yang bereaksi karena hal tersebut dinamakan <b>Event-Driven</b>.</p>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center">
                        <div class="text-5xl mb-4">🎶</div>
                        <p class="text-blue-700 font-bold">Lagu tidak akan terputar kalau "Tombol Play" tidak diklik!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Analogi Resepsionis 🛎️",
            "subtitle": "Bagaimana Tombol Bekerja?",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-100 p-6 rounded-xl border border-slate-300 text-center">
                        <div class="text-6xl mb-4">🛎️ 🏃‍♂️</div>
                        <p class="text-slate-700 font-bold">Tombol (Bel) memanggil Fungsi (Petugas)</p>
                    </div>
                    <div class="text-left space-y-4">
                        <p class="text-slate-600 text-lg">Bayangkan <b>Bel</b> di meja hotel. Kalau ditekan, <b>Petugas</b> datang melayani.</p>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold">Tombol:</span> Bel-nya.</li>
                            <li><span class="font-bold">Fungsi (def):</span> Petugasnya (tugas apa yang harus dilakukan).</li>
                            <li><span class="font-bold">command=:</span> Tali yang menghubungkan bel dan ruangan petugas.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Fungsi &amp; Command 🛠️",
            "subtitle": "Kode yang Dipanggil",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menyambungkan Tali</h3>
                        <p class="text-slate-600 text-lg">Untuk menyambungkan bel dan tugasnya, pakai atribut <code>command=nama_fungsi</code> (<b>TIDAK</b> pakai tanda kurung <span class="text-red-500">()</span> di akhirnya!).</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300">
<span class="text-emerald-400"># 1. Bikin petugasnya (Fungsi)</span><br>
def sapa_user():<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="text-green-300">"Halo semuanya!"</span>)<br><br>
<span class="text-emerald-400"># 2. Bikin tombol &amp; sambungkan talinya</span><br>
btn = ctk.CTkButton(app, text=<span class="text-green-300">"Sapa"</span>, <span class="text-yellow-300">command=sapa_user</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Keyword \"global\" 🌍",
            "subtitle": "Mengingat Skor Keluar Fungsi",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
skor = <span class="text-purple-400">0</span><br><br>
def tambah_skor():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> skor<br>
&nbsp;&nbsp;&nbsp;&nbsp;skor += <span class="text-purple-400">1</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;print(skor)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Izin Mengubah Data</h3>
                        <p class="text-slate-600 text-lg">Variabel <code>skor</code> ada di luar fungsi (di luar ruangan). Supaya petugas (fungsi) boleh memodifikasinya, ia butuh izin masuk pakai kata kunci <span class="font-bold text-orange-600">global</span>.</p>
                        <p class="text-slate-600 text-lg">Tanpa <span class="font-bold text-orange-600">global</span>, fungsi akan membuat <code>skor</code> sementara dan error.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Mini Quiz: Event &amp; Global 🧠",
            "subtitle": "Cek Pemahaman!",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">⚡</div>
                    <p class="font-semibold text-slate-700 text-xl">Bagaimana cara menyambungkan fungsi <code>login()</code> ke dalam tombol CTkButton?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb5', 'Salah! Kalau pakai kurung (), fungsinya akan langsung kepanggil tanpa diklik tombolnya!', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. command=login()</button>
                        <button onclick="showMiniFeedback('fb2-fb5', 'Tepat! Kita hanya memberi nama fungsinya, tanpa tanda kurung eksekusi.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. command=login</button>
                        <button onclick="showMiniFeedback('fb2-fb5', 'Salah! action= bukan bagian dari syntax CustomTkinter.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. action=login</button>
                    </div>
                    <div id="fb2-fb5" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Materi 5: .configure() 🔄",
            "subtitle": "Update UI secara instan",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menyulap Teks</h3>
                        <p class="text-slate-600 text-lg">Kita sudah bisa print angka ke terminal, tapi bagaimana cara mengubah Label angka di dalam aplikasinya sendiri?</p>
                        <p class="text-slate-600 text-lg">Gunakan metode <span class="font-mono text-pink-600">.configure()</span> pada widget yang mau diubah!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Bikin label tulisan "0"</span><br>
label_skor = ctk.CTkLabel(app, text=<span class="text-green-300">"0"</span>)<br><br>
<span class="text-emerald-400"># Di dalam fungsi, kita ubah isi teksnya:</span><br>
label_skor.configure(text=<span class="text-green-300">"99"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Clicker Counter 🕹️",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># 1. Setup Awal</span><br>
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.geometry(<span class="text-green-300">"350x400"</span>)<br>
app.title(<span class="text-green-300">"Clicker Game"</span>)<br><br>
<span class="text-emerald-400"># 2. Variabel Skor (State)</span><br>
skor = <span class="text-purple-400">0</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">State Preparation</h3>
                        <p class="text-slate-600 text-lg">Buat file <code>clicker.py</code>. Siapkan jendela aplikasi dan satu variabel yang bertugas menyimpan berapa kali tombol ditekan.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Clicker Counter 🕹️",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Fungsi Penambah Skor</h3>
                        <p class="text-slate-600 text-lg">Buat fungsi (petugas) yang bertugas menambah variabel <code>skor</code> sebesar 1 setiap kali ia dipanggil.</p>
                        <p class="text-slate-600 text-lg text-orange-600 font-bold">Wajib pakai global!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># 3. Fungsi Logika Game</span><br>
def klik_tombol():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> skor<br>
&nbsp;&nbsp;&nbsp;&nbsp;skor += <span class="text-purple-400">1</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Jangan lupa ganti angka dari variabel skor menjadi string</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;label_angka.configure(text=str(skor))
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Clicker Counter 🕹️",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># 4. Membuat UI Label (Papan Skor)</span><br>
label_judul = ctk.CTkLabel(app, text=<span class="text-green-300">"Total Klik:"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">20</span>))<br>
label_judul.pack(pady=(<span class="text-purple-400">40</span>, <span class="text-purple-400">10</span>))<br><br>
label_angka = ctk.CTkLabel(app, text=<span class="text-green-300">"0"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">70</span>, <span class="text-green-300">"bold"</span>))<br>
label_angka.pack(pady=<span class="text-purple-400">10</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyusun Layar (UI)</h3>
                        <p class="text-slate-600 text-lg">Buat UI-nya pakai pack saja biar gampang di tengah. Variabel Label-nya bebas, di sini kita pakai nama <code>label_angka</code> (yang tadi dipakai di step 2 pakai configure).</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Clicker Counter 🕹️",
            "subtitle": "Ayo kita koding! (Step 4)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Sambungkan Tombol</h3>
                        <p class="text-slate-600 text-lg">Terakhir, buat Tombol Klik. Nah, rahasianya ada di parameter <span class="font-mono text-blue-600 font-bold">command=klik_tombol</span>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># 5. Tombol Pemicu</span><br>
btn_tambah = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app, text=<span class="text-green-300">"TAP ME!"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;width=<span class="text-purple-400">200</span>, height=<span class="text-purple-400">60</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">24</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">command=klik_tombol</span><br>
)<br>
btn_tambah.pack(pady=<span class="text-purple-400">40</span>)<br><br>
<span class="text-emerald-400"># Start Aplikasi</span><br>
app.mainloop()
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Clicker Counter 🎯",
            "subtitle": "Tap Tap Game!",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Clicker Game</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-80 flex flex-col items-center justify-center p-6">
                            <p class="text-slate-300 text-xl mb-2">Total Klik:</p>
                            <h1 class="text-white text-[70px] font-bold mb-8">17</h1>
                            <button class="w-48 h-16 rounded-lg bg-[#1f6aa5] text-white text-2xl font-bold hover:bg-blue-600 transition-colors shadow-lg active:scale-95">TAP ME!</button>
                        </div>
                    </div>
                    <p class="text-slate-500 italic mt-4 text-sm">Cobalah klik tombolnya, angkanya akan terus naik secara otomatis. Keren kan?</p>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Tombol Reset 🔄",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Mulai dari Nol</h3>
                        <p class="text-slate-600 text-lg">Aplikasi clicker kurang lengkap kalau tidak bisa kembali ke angka 0.</p>
                        <p class="text-slate-600 text-lg">Buatlah tombol baru berwarna merah (<i>fg_color</i>), dan buat fungsi baru khusus untuk tombol tersebut!</p>
                    </div>
                    <div class="bg-red-50 p-6 rounded-xl border border-red-200">
                        <h4 class="font-bold text-red-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat fungsi <code>def reset_skor():</code></li>
                            <li>Set skor kembali jadi 0.</li>
                            <li>Configure label_angka jadi "0" lagi.</li>
                            <li>Buat CTkButton "RESET" dan pasang <i>command</i>-nya.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Tombol Kurang ➖",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat fungsi <code>def kurang_skor():</code></li>
                            <li>Kurangi skor (-= 1).</li>
                            <li>Cegah angkanya jadi negatif! (Gunakan <code>if skor > 0:</code>).</li>
                            <li>Buat tombol baru "Minus".</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menghindari Minus</h3>
                        <p class="text-slate-600 text-lg">Selain tambah, kamu ditantang bikin tombol untuk mengurang skor. Tapi jangan sampai angkanya jadi -1, -2, dll.</p>
                        <p class="text-slate-600 text-sm font-semibold text-orange-600 mt-2">Clue: Gunakan If Conditional sebelum mengurangi variabel skor!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Peringatan 100! 🚨",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Perubahan Tema Warna</h3>
                        <p class="text-slate-600 text-lg">Pernah lihat speedometer mobil kalau ngebut jadi warna merah peringatan?</p>
                        <p class="text-slate-600 text-lg">Tambahkan If Conditional di dalam <code>klik_tombol</code>: Kalau skor sudah mencapai >= 50, ubah warna angka menjadi merah (<i>text_color</i>)!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Clue: .configure() bukan cuma bisa ganti text, tapi warna juga!</span><br>
label_angka.configure(<br>
&nbsp;&nbsp;&nbsp;&nbsp;text=str(skor),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-purple-300">text_color</span>=<span class="text-green-300">"red"</span><br>
)
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Project: Tema Siang Malam 🌗",
            "subtitle": "Latihan Ekstra",
            "content": \`
                <div class="max-w-5xl mx-auto">
                    <p class="text-slate-600 text-lg mb-4 text-center">Fungsi tidak hanya untuk mengubah Label lho, tapi juga hal sistematis seperti Tema Aplikasi!</p>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl text-green-300 h-64 overflow-y-auto">
<span class="text-emerald-400"># Buat tombol khusus ubah tema "Dark" ke "Light" dan sebaliknya!</span><br>
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.geometry("300x200")<br>
ctk.set_appearance_mode("dark")<br>
tema_sekarang = "dark"<br><br>
def ubah_tema():<br>
&nbsp;&nbsp;&nbsp;&nbsp;global tema_sekarang<br>
&nbsp;&nbsp;&nbsp;&nbsp;if tema_sekarang == "dark":<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctk.set_appearance_mode("light")<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tema_sekarang = "light"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_tema.configure(text="Jadi Gelap")<br>
&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctk.set_appearance_mode("dark")<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tema_sekarang = "dark"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_tema.configure(text="Jadi Terang")<br><br>
btn_tema = ctk.CTkButton(app, text="Jadi Terang", command=ubah_tema)<br>
btn_tema.pack(pady=70)<br>
app.mainloop()
                    </div>
                </div>
            \`
        },
        {
            "title": "Summary 📝",
            "subtitle": "Ringkasan Pembelajaran",
            "content": \`
                <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                    <div class="bg-blue-50 border border-blue-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-blue-700 mb-3 text-xl">Event &amp; Fungsi</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold">Event-Driven:</span> Aplikasi bereaksi terhadap aksi pengguna (klik).</li>
                            <li><span class="font-bold">command=:</span> Parameter untuk memanggil nama fungsi (Tanpa tanda kurung ()).</li>
                        </ul>
                    </div>
                    <div class="bg-orange-50 border border-orange-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-orange-700 mb-3 text-xl">State &amp; UI Update</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-orange-600">global:</span> Izin agar fungsi bisa mengubah data variabel luaran.</li>
                            <li><span class="font-bold text-pink-600">.configure():</span> Cara cepat untuk meng-update properti widget tanpa menggambarnya ulang.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Quote of the Day 💭",
            "subtitle": "Motivasi",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-8 mt-10">
                    <div class="text-6xl text-blue-500 opacity-50">"</div>
                    <blockquote class="text-3xl font-bold text-slate-800 italic leading-snug">
                        Code that listens is better than code that just talks. Give your users the power to trigger actions.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— Interactive UI Mantra</p>
                </div>
            \`
        }"""

pattern = re.compile(r'    "5": \[\s*\{.*?\}\s*\],\s*"6": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_5 + '\n    ],\n    "6": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 5 successfully.")
