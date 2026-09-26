import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_6 = """    "6": [
        {
            "title": "Meeting 6: Try-Except & Timer ⏱️",
            "subtitle": "Membuat Aplikasi yang Tangguh",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🛡️</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Jangan Biarkan Aplikasimu Mudah Hancur!</p>
                <p class="text-lg text-slate-600">Hari ini kita akan belajar menghadapi "User yang Bandel" (salah isi form) dan membuat aplikasi penghitung waktu mundur yang berjalan mulus tanpa macet.</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-red-50 border border-red-100 p-4 text-red-700">try ... except</div>
                    <div class="rounded-xl bg-blue-50 border border-blue-100 p-4 text-blue-700">app.after()</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 5 ⏪",
            "subtitle": "Review Materi Kemarin",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">⚡</div><h4 class="font-bold text-slate-800">Event-Driven</h4><p class="text-sm text-slate-500 mt-2">Menunggu reaksi user, tidak jalan lurus</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🔗</div><h4 class="font-bold text-slate-800">command=</h4><p class="text-sm text-slate-500 mt-2">Menyambungkan tombol dengan fungsi</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🔄</div><h4 class="font-bold text-slate-800">.configure()</h4><p class="text-sm text-slate-500 mt-2">Ubah teks di UI secara instan</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">👀</div>
                    <p class="font-semibold text-slate-700 text-xl">Keyword apa yang harus ditambahkan di dalam fungsi jika fungsi tersebut mau memodifikasi nilai variabel yang ada di luar fungsi?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb6', 'Salah! Tidak ada keyword var di Python.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. var</button>
                        <button onclick="showMiniFeedback('fb1-fb6', 'Salah! local malah membuat variabel itu terbatas di dalam fungsi.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. local</button>
                        <button onclick="showMiniFeedback('fb1-fb6', 'Tepat sekali! global mengizinkan fungsi mengedit data di luar.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">C. global</button>
                    </div>
                    <div id="fb1-fb6" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami <span class="font-bold text-blue-600">Robustness</span> (Kestabilan Aplikasi).</li>
                        <li>Menggunakan <span class="font-mono text-red-600 bg-red-50 px-2 py-1 rounded">try</span> dan <span class="font-mono text-red-600 bg-red-50 px-2 py-1 rounded">except ValueError</span> untuk menangani user yang iseng.</li>
                        <li>Membuat <i>timer/countdown</i> tanpa membuat aplikasi nge-<i>freeze</i> dengan <span class="font-mono text-blue-600 bg-blue-50 px-2 py-1 rounded">app.after()</span>.</li>
                        <li>Menggunakan variabel <b>boolean</b> sebagai <i>flag</i> (penanda) aktif/tidaknya timer.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Aplikasi Sempurna Hancur Seketika 💥",
            "subtitle": "Realita Dunia Software",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">User Tidak Selalu Patuh</h3>
                        <p class="text-slate-600 text-lg">Bayangkan aplikasimu meminta "Masukkan Umur". Kodenya sudah benar pakai <code class="font-mono text-blue-600">int()</code>.</p>
                        <p class="text-slate-600 text-lg">Tapi, ada user iseng yang mengetik "Dua Belas". Apa yang terjadi? <b>BUM! Aplikasi langsung crash (menutup paksa) 💥</b>.</p>
                        <p class="text-slate-600 text-lg">Aplikasi yang gampang <i>crash</i> disebut rentan. Kita butuh aplikasi yang <b>Robust</b> (Tangguh).</p>
                    </div>
                    <div class="bg-red-50 p-6 rounded-xl border border-red-200 text-center">
                        <div class="text-5xl mb-4">😱</div>
                        <p class="text-red-700 font-bold font-mono">ValueError: invalid literal for int() with base 10: 'Dua Belas'</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Analogi Mesin ATM 🏧",
            "subtitle": "Menangkap Kesalahan",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-100 p-6 rounded-xl border border-slate-300 text-center">
                        <div class="text-6xl mb-4">🏧 ❌</div>
                        <p class="text-slate-700 font-bold">ATM tidak pernah meledak kalau PIN salah.</p>
                    </div>
                    <div class="text-left space-y-4">
                        <p class="text-slate-600 text-lg">Saat kamu salah masukkan PIN, apakah mesin ATM mati/error? Tentu tidak. Mesin hanya memunculkan tulisan: <i>"PIN Salah, Coba Lagi."</i></p>
                        <p class="text-slate-600 text-lg">Itulah Error Handling! Program menangkap kesalahan <b>sebelum</b> error itu menghancurkan aplikasi, lalu merespons dengan cara yang baik.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Try-Except 🛡️",
            "subtitle": "Perisai Kode Kita",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menjebak Error</h3>
                        <p class="text-slate-600 text-lg">Gunakan blok <span class="font-bold text-red-600">try</span> (Mencoba menjalankan kode) dan <span class="font-bold text-red-600">except</span> (Jika gagal, lakukan ini).</p>
                        <p class="text-slate-600 text-lg">Jika <code>try</code> sukses, kode lanjut seperti biasa. Jika <code>try</code> error, ia akan loncat ke <code>except</code>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Minta input user</span><br>
<span class="text-orange-400 font-bold">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;umur = int( input_umur.get() )<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="text-green-300">"Sukses, angkanya:"</span>, umur)<br>
<span class="text-orange-400 font-bold">except</span> ValueError:<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Kalau masukin teks (bukan angka), lari kesini!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="text-green-300">"Tolong masukkan angka, bukan huruf!"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Bahaya while True di GUI ⏳",
            "subtitle": "Jangan Bikin Aplikasimu Beku!",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-100 p-5 rounded-xl font-mono text-sm text-left shadow-md border border-slate-300 text-slate-800">
<span class="text-red-500 font-bold"># JANGAN GUNAKAN INI DI GUI! ❌</span><br>
import time<br><br>
waktu = 10<br>
while waktu > 0:<br>
&nbsp;&nbsp;&nbsp;&nbsp;label.configure(text=str(waktu))<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-red-500 font-bold">time.sleep(1) # BIKIN MACET!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;waktu -= 1
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kenapa Macet / Freeze?</h3>
                        <p class="text-slate-600 text-lg">Di aplikasi CLI/Terminal, <code>time.sleep(1)</code> adalah sahabat kita. Di CustomTkinter? Ia adalah <span class="font-bold text-red-500">Mimpi Buruk!</span></p>
                        <p class="text-slate-600 text-lg">Saat Python sedang "tidur" (sleep), jendela aplikasimu juga ikut mati suri. Tombol tidak bisa diklik, tulisan tidak terganti, dan tertulis <i>Not Responding</i>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 5: app.after() ⏰",
            "subtitle": "Timer Tanpa Freeze",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Timer Pintar</h3>
                        <p class="text-slate-600 text-lg">Solusinya adalah <span class="font-bold text-blue-600">app.after(1000, fungsi)</span>.</p>
                        <p class="text-slate-600 text-lg">Ini artinya: <i>"Hai sistem, tolong diam-diam panggil fungsi ini 1000 milidetik (1 detik) lagi. Saya mau layani layar UI dulu."</i> Layar tetap hidup!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
def jalan_lagi():<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(<span class="text-green-300">"Satu detik sudah berlalu!"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Panggil dirinya sendiri lagi nanti</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;app.after(<span class="text-purple-400">1000</span>, jalan_lagi)<br><br>
<span class="text-emerald-400"># Pemicu awal</span><br>
app.after(<span class="text-purple-400">1000</span>, jalan_lagi)
                    </div>
                </div>
            \`
        },
        {
            "title": "Mini Quiz: Error Handling 🧠",
            "subtitle": "Cek Pemahaman!",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🛡️</div>
                    <p class="font-semibold text-slate-700 text-xl">Jika kita mau menampung error khusus konversi tulisan ke angka, error apa yang kita targetkan?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb6', 'Salah! TypeError adalah error jika salah cara pakai, misalnya integer ditambah string.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. TypeError</button>
                        <button onclick="showMiniFeedback('fb2-fb6', 'Salah! SyntaxError adalah error dari kode yang penulisannya salah (kurang titik dua, dll).', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. SyntaxError</button>
                        <button onclick="showMiniFeedback('fb2-fb6', 'Tepat! ValueError dipicu saat int(\"halo\") karena isinya tidak valid untuk jadi angka.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">C. ValueError</button>
                    </div>
                    <div id="fb2-fb6" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Countdown Timer ⏱️",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># 1. Setup UI (Buat UI-nya dulu)</span><br>
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.geometry(<span class="text-green-300">"400x300"</span>)<br>
app.title(<span class="text-green-300">"Countdown"</span>)<br><br>
<span class="text-emerald-400"># Komponen UI</span><br>
lbl_judul = ctk.CTkLabel(app, text=<span class="text-green-300">"TIMER BOM"</span>, font=(<span class="text-green-300">"Arial"</span>, <span class="text-purple-400">20</span>))<br>
lbl_judul.pack(pady=<span class="text-purple-400">10</span>)<br><br>
entry_waktu = ctk.CTkEntry(app, placeholder_text=<span class="text-green-300">"Masukan Detik..."</span>)<br>
entry_waktu.pack(pady=<span class="text-purple-400">10</span>)<br><br>
lbl_angka = ctk.CTkLabel(app, text=<span class="text-green-300">"0"</span>, font=(<span class="text-green-300">"Arial"</span>, <span class="text-purple-400">60</span>, <span class="text-green-300">"bold"</span>))<br>
lbl_angka.pack(pady=<span class="text-purple-400">10</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Kerangka Visual (UI)</h3>
                        <p class="text-slate-600 text-lg">Buat file <code>timer.py</code>. Siapkan label judul, <b>Entry</b> untuk menginput detik, dan Label Besar (<code>lbl_angka</code>) untuk menampilkan waktu berjalannya.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Countdown Timer ⏱️",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">State Variabel & Tombol</h3>
                        <p class="text-slate-600 text-lg">Di bawah kode inisialisasi tadi, kita buat state: <code>sisa_waktu</code> dan <code>is_running</code>.</p>
                        <p class="text-slate-600 text-lg">Juga sediakan kerangka fungsi <code>klik_start()</code> yang memakai <span class="font-bold text-red-600">Try Except</span>!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># 2. State Variables</span><br>
sisa_waktu = <span class="text-purple-400">0</span><br>
is_running = <span class="text-orange-400 font-bold">False</span><br><br>
<span class="text-emerald-400"># 3. Fungsi Start (Dengan Proteksi)</span><br>
def klik_start():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> sisa_waktu, is_running<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;angka = int(entry_waktu.get())<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sisa_waktu = angka<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_running = <span class="text-orange-400 font-bold">True</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_angka.configure(text=str(sisa_waktu), text_color=<span class="text-green-300">"white"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Nanti kita panggil jalankan_timer() disini</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">except</span> ValueError:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_angka.configure(text=<span class="text-green-300">"Input Angka!"</span>, text_color=<span class="text-green-300">"red"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Countdown Timer ⏱️",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># 4. Fungsi Timer Mundur (Cerdas Tanpa Freeze)</span><br>
def jalankan_timer():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> sisa_waktu, is_running<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">if</span> is_running <span class="text-orange-400 font-bold">and</span> sisa_waktu > <span class="text-purple-400">0</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sisa_waktu -= <span class="text-purple-400">1</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_angka.configure(text=str(sisa_waktu))<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;app.after(<span class="text-purple-400">1000</span>, jalankan_timer) <span class="text-emerald-400"># Panggil ulang!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">elif</span> sisa_waktu == <span class="text-purple-400">0</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_running = <span class="text-orange-400 font-bold">False</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_angka.configure(text=<span class="text-green-300">"TIME'S UP!"</span>, text_color=<span class="text-green-300">"red"</span>)<br><br>
<span class="text-emerald-400"># TADI: Jangan lupa tambahkan jalankan_timer() di dalam blok try milik klik_start()</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menghitung Mundur</h3>
                        <p class="text-slate-600 text-lg">Ini adalah kuncinya! Fungsi <code>jalankan_timer</code> akan memanggil dirinya sendiri setiap detik <i>hanya jika</i> waktu masih ada dan statusnya <code>True</code>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Countdown Timer ⏱️",
            "subtitle": "Ayo kita koding! (Step 4)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Sambungkan Tombol</h3>
                        <p class="text-slate-600 text-lg">Pasang tombol Start dan jalankan aplikasimu!</p>
                        <p class="text-slate-600 text-lg">Coba masukkan teks "halo" dan klik Start, lihat apa yang terjadi. (Pasti tidak crash!)</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># 5. Tombol Pemicu</span><br>
btn_start = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app, text=<span class="text-green-300">"START TIMER"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">16</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-yellow-300">command=klik_start</span><br>
)<br>
btn_start.pack(pady=<span class="text-purple-400">10</span>)<br><br>
<span class="text-emerald-400"># Start Aplikasi</span><br>
app.mainloop()
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Countdown Timer 🎯",
            "subtitle": "Hitung Mundur",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Countdown Timer</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-80 flex flex-col items-center justify-center p-6 space-y-4">
                            <p class="text-slate-300 text-lg">Masukkan Detik:</p>
                            <div class="w-full bg-[#1e1e1e] border border-[#555] rounded-md px-3 py-2 text-left text-slate-400 text-sm">Contoh: 10</div>
                            <h1 class="text-white text-[60px] font-bold my-2">5</h1>
                            <button class="w-full h-10 rounded-md bg-[#1f6aa5] text-white text-md font-bold hover:bg-blue-600 transition-colors shadow-lg active:scale-95">START TIMER</button>
                        </div>
                    </div>
                    <p class="text-slate-500 italic mt-4 text-sm">Dengan begini kita punya timer yang berjalan asinkron dan elegan.</p>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Tombol STOP 🛑",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyetop Timer</h3>
                        <p class="text-slate-600 text-lg">Bagaimana kalau aku mau membatalkan timer di tengah jalan?</p>
                        <p class="text-slate-600 text-lg">Buatlah tombol STOP warna merah (<i>fg_color</i>), dan buat fungsi baru untuk mematikan status <code>is_running</code>!</p>
                    </div>
                    <div class="bg-red-50 p-6 rounded-xl border border-red-200">
                        <h4 class="font-bold text-red-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat fungsi <code>def klik_stop():</code></li>
                            <li>Gunakan keyword <code>global is_running</code></li>
                            <li>Set <code>is_running = False</code>.</li>
                            <li>Buat CTkButton "STOP TIMER" dan pasang <i>command</i>-nya.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Cegah Angka Negatif ➖",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Modifikasi blok <code>try</code> di dalam fungsi <code>klik_start()</code>.</li>
                            <li>Tambahkan <span class="font-bold text-orange-600">If angka <= 0:</span></li>
                            <li>Jika iya, suruh label memunculkan "Harus Lebih dari 0!".</li>
                            <li>Gunakan <code>return</code> agar fungsi langsung berhenti.</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">User iseng lagi...</h3>
                        <p class="text-slate-600 text-lg">User menginputkan angka <code>-10</code>. Memang tidak Error karena -10 itu <i>Integer</i>. Tapi timer jadi aneh!</p>
                        <p class="text-slate-600 text-lg">Validasi pakai "IF" agar tidak memulai timer kalau inputnya aneh.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Peringatan Kritis! 🚨",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Waktu Hampir Habis</h3>
                        <p class="text-slate-600 text-lg">Ubah warna <code>label_angka</code> menjadi <b>kuning</b> ("#f39c12") saat sisa_waktu berada di angka <b>1, 2, atau 3</b> (kurang dari 4 detik) sebagai peringatan visual bahwa waktu hampir habis!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Clue: Di dalam fungsi jalankan_timer()</span><br>
<span class="text-orange-400 font-bold">if</span> sisa_waktu < <span class="text-purple-400">4</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_angka.configure(<span class="text-purple-300">text_color</span>=<span class="text-green-300">"yellow"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Project: Menit & Detik ⏰",
            "subtitle": "Latihan Ekstra",
            "content": \`
                <div class="max-w-5xl mx-auto">
                    <p class="text-slate-600 text-lg mb-4 text-center">Bosan hanya lihat detik? Coba pakai modulo untuk membuat format <code>MM:SS</code> (Menit:Detik)</p>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Ganti bagian configure di update_timer() jadi seperti ini:</span><br>
menit = sisa_waktu // <span class="text-purple-400">60</span>   <span class="text-emerald-400"># Pembagian Bulat (Division)</span><br>
detik = sisa_waktu % <span class="text-purple-400">60</span>    <span class="text-emerald-400"># Modulo (Sisa Bagi)</span><br><br>
<span class="text-emerald-400"># Menggunakan f-string dengan zfill (zero fill) agar formatnya 05:09 bukan 5:9</span><br>
format_waktu = f<span class="text-green-300">"{str(menit).zfill(2)}:{str(detik).zfill(2)}"</span><br><br>
lbl_angka.configure(text=format_waktu)
                    </div>
                </div>
            \`
        },
        {
            "title": "Info Tambahan: Literasi Digital 🌐",
            "subtitle": "Keamanan Data",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200">
                        <h4 class="font-bold text-blue-800 mb-3 text-xl">Tahukah Kamu?</h4>
                        <p class="text-slate-700">Error handling (Try-Except) yang buruk bisa menjadi <b>celah keamanan (Hack)</b>. Pesan error teknis yang langsung muncul di layar sering kali mengungkapkan isi struktur sistem, atau <i>database password</i> kepada <i>hacker</i>.</p>
                    </div>
                    <div class="text-left space-y-4">
                        <p class="text-slate-600 text-lg">Oleh sebab itu, developer profesional selalu menangkap error (<b>Try-Except</b>) dan memberikan pesan ramah ke pengguna (Contoh: "Mohon ulangi lagi"), sedangkan kode asli error-nya disembunyikan dalam file rahasia.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Summary 📝",
            "subtitle": "Ringkasan Pembelajaran",
            "content": \`
                <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                    <div class="bg-red-50 border border-red-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-red-700 mb-3 text-xl">Robustness & Try-Except</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-red-600">try:</span> Baris kode yang ingin dijalankan dan dilindungi dari error (misal Input Konversi).</li>
                            <li><span class="font-bold text-red-600">except ValueError:</span> Jalankan ini kalau pengguna memasukkan format teks yang salah (Bukan angka).</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 border border-blue-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-blue-700 mb-3 text-xl">Smart Timer</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-blue-600">app.after(1000, func):</span> Menyuruh GUI untuk memanggil fungsi ini dalam 1000 milidetik (1 detik), UI tidak akan membeku.</li>
                            <li><span class="font-bold">Boolean Flag:</span> Variabel True/False penting mengatur status nyala/mati Timer.</li>
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
                        Programs must be written for people to read, and only incidentally for machines to execute. So, expect people to make mistakes and handle them gracefully.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— Developer Wisdom</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "6": \[\s*\{.*?\}\s*\],\s*"7": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_6.replace("\\`", "`") + '\n    ],\n    "7": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 6 successfully.")
