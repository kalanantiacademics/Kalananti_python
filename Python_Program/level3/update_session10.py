import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_10 = """    "10": [
        {
            "title": "Meeting 10: Archius Live Weather 🌦️ (Part 1)",
            "subtitle": "Membangun Wajah Aplikasi (Front-end)",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🎨</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Front-End Developer Mode!</p>
                <p class="text-lg text-slate-600">Pernah buka aplikasi cuaca seperti BMKG atau AccuWeather? Tampilannya sangat rapi, suhu ada di tengah, dan detail lain ada di bawah. Hari ini, kita akan murni merancang <b>wajah visual</b> dari aplikasi cuaca kita, tanpa koneksi internet (offline dulu)!</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-blue-50 border border-blue-100 p-4 text-blue-700">app.configure() & Styling</div>
                    <div class="rounded-xl bg-cyan-50 border border-cyan-100 p-4 text-cyan-700">Mixed Layout (Pack + Grid)</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 9 ⏪",
            "subtitle": "Review Task Manager",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🪄</div><h4 class="font-bold text-slate-800">Dynamic UI</h4><p class="text-sm text-slate-500 mt-2">Menciptakan komponen layar secara gaib di dalam fungsi</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">💥</div><h4 class="font-bold text-slate-800">.destroy()</h4><p class="text-sm text-slate-500 mt-2">Menghapus komponen secara total dari memori RAM</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🧩</div><h4 class="font-bold text-slate-800">Decomposition</h4><p class="text-sm text-slate-500 mt-2">Memecah aplikasi besar jadi beberapa Frame/Bagian</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Apa fungsi dari perintah <code>kotak_tugas.destroy()</code>?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb10', 'Salah! Membunyikan alarm tidak ada hubungannya dengan destroy.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Membunyikan suara ledakan saat kotak dihapus.</button>
                        <button onclick="showMiniFeedback('fb1-fb10', 'Tepat! Perintah ini akan menghancurkan Frame kotak_tugas secara permanen dari layar dan memori komputer, termasuk semua isinya.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Menghapus frame kotak_tugas (beserta semua widget di dalamnya) secara permanen dari aplikasi.</button>
                        <button onclick="showMiniFeedback('fb1-fb10', 'Salah! destroy() itu menghancurkan, bukan menyembunyikan sementara.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Menyembunyikan kotak_tugas sementara waktu agar bisa dimunculkan lagi nanti.</button>
                    </div>
                    <div id="fb1-fb10" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami konsep <b>Front-End</b> (Lapisan Visual) pada pembangunan software.</li>
                        <li>Mengubah warna latar keseluruhan jendela dengan <code>app.configure(fg_color=...)</code>.</li>
                        <li>Membedah dan mengatur warna spesifik pada <code>CTkEntry</code> (Mewarnai *border* dan kotak isi).</li>
                        <li>Menerapkan <b>Mixed Layout</b>: Bebas menggabungkan `.pack()` dan `.grid()` secara cerdas di tempat yang tepat.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Apa itu Front-End? 🖥️",
            "subtitle": "Wajah Aplikasi",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Dua Sisi Mata Uang</h3>
                        <p class="text-slate-600 text-lg">Dalam dunia programming, aplikasi dibagi dua:</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li><b>Front-End:</b> Wajah aplikasi (Warna, Tombol, Animasi). Tugasnya memanjakan mata pengguna.</li>
                            <li><b>Back-End:</b> Otak aplikasi (Database, Jaringan Internet, Server).</li>
                        </ul>
                        <p class="text-slate-600 font-bold text-blue-600">Hari ini, kita akan full menjadi Front-End Designer!</p>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center shadow-inner">
                        <div class="text-7xl mb-4">🎨</div>
                        <p class="text-blue-800 font-bold">Semua tombol hari ini masih palsu (Dummy), belum bisa jalan.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Membedah Tampilan Cuaca 🔍",
            "subtitle": "Rencana Layout",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl text-left shadow-xl h-64 overflow-y-auto">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/f69c2651-114d-4309-866b-d48e941d2033.png" class="mx-auto rounded-lg object-contain w-full h-full">
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">3 Bagian Utama</h3>
                        <p class="text-slate-600 text-lg">Mari kita dekomposisi layarnya:</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-2">
                            <li><span class="font-bold text-blue-600">Search Section:</span> Paling atas, kotak pencarian kota.</li>
                            <li><span class="font-bold text-orange-600">Main Display:</span> Tengah, nama kota & Suhu 90°C!</li>
                            <li><span class="font-bold text-green-600">Stats Grid:</span> Bawah, detail kelembapan & angin.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Latar Belakang Biru Navy 🌌",
            "subtitle": "Mengubah Background Penuh",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">app.configure()</h3>
                        <p class="text-slate-600 text-lg">Selama ini kita hanya memakai tema "dark" atau "light" (Abu-abu/Hitam).</p>
                        <p class="text-slate-600 text-lg">Untuk mengubah seluruh warna latar aplikasi jadi Biru Navy secara paksa, kita gunakan perintah rahasia: <br><code>app.configure(fg_color="#1e3a8a")</code></p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300 text-sm">
app = ctk.CTk()<br>
app.geometry(<span class="text-green-300">"500x750"</span>)<br><br>
<span class="text-emerald-400"># Mewarnai seluruh Background!</span><br>
app.configure(fg_color=<span class="text-green-300">"#1e3a8a"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Menghias Kotak Input (Entry) ✒️",
            "subtitle": "Entry Custom Color",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-5 rounded-xl font-mono text-xs text-left shadow-md border border-blue-200 text-blue-900">
box_ketik = ctk.CTkEntry(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app,<br>
&nbsp;&nbsp;&nbsp;&nbsp;fg_color=<span class="text-blue-700">"#1e40af"</span>, <span class="text-blue-500"># Warna di dalam kotak</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;border_color=<span class="text-blue-700">"#3b82f6"</span>, <span class="text-blue-500"># Warna garis pinggir</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;text_color=<span class="text-blue-700">"white"</span> <span class="text-blue-500"># Warna tulisan yang diketik</span><br>
)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Desain Detail</h3>
                        <p class="text-slate-600 text-lg">Biar tampilannya nyatu sama warna biru, <code>CTkEntry</code> harus kita poles.</p>
                        <p class="text-slate-600 text-lg">Kamu bisa mengatur 3 elemen warna di dalam Entry: *Foreground* (isi kotak), *Border* (garis pembatas), dan *Text Color*.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 5: Rahasia Mixed Layout 🔀",
            "subtitle": "Campur Pack & Grid",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Boleh Dicampur!</h3>
                        <p class="text-slate-600 text-lg">"Kata Guru gak boleh nyampur Pack sama Grid di 1 program!"</p>
                        <p class="text-slate-600 text-lg">Faktanya: Kamu <b>TIDAK BOLEH</b> mencampur di dalam satu Frame/Area yang sama. TAPI, kamu boleh menaruh Frame utama pakai <code>.pack()</code>, lalu di dalam Frame itu isinya diatur pakai <code>.grid()</code>. Ini kuncinya membuat aplikasi kompleks!</p>
                    </div>
                    <div class="bg-indigo-50 p-5 rounded-xl border border-indigo-200 shadow-md">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/adff2764-841b-4af8-999d-82bbe2ded725.png" class="mx-auto rounded-lg h-36 object-contain mb-4">
                        <p class="text-indigo-800 text-sm font-bold text-center">Kotak luar di-pack(). Label di dalamnya di-grid().</p>
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
                    <p class="font-semibold text-slate-700 text-xl">Kenapa kita pakai <code>app.configure(fg_color="#warna")</code> daripada <code>ctk.set_appearance_mode()</code>?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb10', 'Salah! Bukan tentang kecepatan komputer.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Karena configure itu prosesnya lebih cepat untuk memori RAM.</button>
                        <button onclick="showMiniFeedback('fb2-fb10', 'Tepat! appearance_mode hanya memberi warna gelap/terang bawaan (abu-abu/putih/hitam). Kalau mau warna kustom spesifik (seperti biru laut), kita wajib timpa pakai configure.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Karena appearance_mode cuma ada dark/light. Kalau mau warna spesifik (misal Biru Navy), harus pakai configure.</button>
                        <button onclick="showMiniFeedback('fb2-fb10', 'Salah! Justru configure mengganti warna keseluruhan layar.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Karena configure cuma mengganti warna teksnya saja, bukan latarnya.</button>
                    </div>
                    <div id="fb2-fb10" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 1)",
            "subtitle": "Setup & Asset",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
import customtkinter as ctk<br>
from PIL import Image<br>
import os<br><br>
app = ctk.CTk()<br>
app.title(<span class="text-green-300">"Archius Live Weather"</span>)<br>
app.geometry(<span class="text-green-300">"500x750"</span>)<br>
app.configure(fg_color=<span class="text-green-300">"#1e3a8a"</span>) <span class="text-blue-500"># Biru Navy!</span><br><br>
<span class="text-emerald-400"># DOWNLOAD ASET DULU!</span><br>
<span class="text-emerald-400"># Pastikan kamu punya gambar: sunny.png, rain.png, dll</span><br>
<span class="text-emerald-400"># Taruh 1 folder dengan file python ini.</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Bikin Fondasinya!</h3>
                        <p class="text-slate-600 text-lg">Mulai dengan file <code>main.py</code> baru. <i>Download</i> dan kumpulkan semua aset gambar cuaca (Awan, Hujan, Matahari) ke dalam satu folder yang sama.</p>
                        <a href="https://bit.ly/weather-img" target="_blank" class="inline-block bg-blue-600 text-white font-bold py-2 px-4 rounded-xl hover:bg-blue-700 transition">Download Gambar ⬇️</a>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 2)",
            "subtitle": "Kamus Ikon Cuaca",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyambungkan Kode & Gambar</h3>
                        <p class="text-slate-600 text-lg">Buat sebuah Dictionary besar bernama <code>ICON_MAP</code>. Ini jadi "buku panduan" buat Python untuk mencari file gambar yang tepat berdasarkan cuacanya nanti.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto text-green-300">
<span class="text-emerald-400"># Kamus Pemetaan Cuaca -> Gambar (Dictionary)</span><br>
ICON_MAP = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"clear"</span>: <span class="text-green-300">"sunny.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"clouds"</span>: <span class="text-green-300">"clouds.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"rain"</span>: <span class="text-green-300">"rain.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"drizzle"</span>: <span class="text-green-300">"rain.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"thunderstorm"</span>: <span class="text-green-300">"thunderstorm.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"snow"</span>: <span class="text-green-300">"snow.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"mist"</span>: <span class="text-green-300">"haze.png"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"haze"</span>: <span class="text-green-300">"haze.png"</span><br>
}
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 3)",
            "subtitle": "Bagian Pencarian (Search Area)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># 1. Kotak Panjang (Search Frame)</span><br>
search_frame = ctk.CTkFrame(app, fg_color=<span class="text-green-300">"transparent"</span>)<br>
search_frame.pack(pady=<span class="text-purple-400">40</span>, padx=<span class="text-purple-400">30</span>, fill=<span class="text-green-300">"x"</span>)<br><br>
<span class="text-emerald-400"># 2. Input Teks di Sebelah Kiri</span><br>
entry_search = ctk.CTkEntry(<br>
&nbsp;&nbsp;&nbsp;&nbsp;search_frame, placeholder_text=<span class="text-green-300">"Enter city..."</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;height=<span class="text-purple-400">45</span>, fg_color=<span class="text-green-300">"#1e40af"</span>, <br>
&nbsp;&nbsp;&nbsp;&nbsp;border_color=<span class="text-green-300">"#3b82f6"</span>, text_color=<span class="text-green-300">"white"</span><br>
)<br>
entry_search.pack(side=<span class="text-green-300">"left"</span>, fill=<span class="text-green-300">"x"</span>, expand=<span class="text-orange-400 font-bold">True</span>, padx=(<span class="text-purple-400">0</span>, <span class="text-purple-400">10</span>))<br><br>
<span class="text-emerald-400"># 3. Tombol Cari di Kanan</span><br>
btn_search = ctk.CTkButton(search_frame, text=<span class="text-green-300">"SEARCH"</span>, height=<span class="text-purple-400">45</span>, fg_color=<span class="text-green-300">"#3b82f6"</span>)<br>
btn_search.pack(side=<span class="text-green-300">"right"</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menu Navigasi Atas</h3>
                        <p class="text-slate-600 text-lg">Rakit kolom pencariannya. Perhatikan bahwa <code>command=...</code> di tombol SEARCH kita kosongkan dulu karena fungsinya baru dibuat di Sesi 11 nanti!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 4)",
            "subtitle": "Display Suhu Utama (Palsu/Dummy)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyusun Visual Pusat</h3>
                        <p class="text-slate-600 text-lg">Buat Label untuk Nama Kota, Label berisi Gambar Matahari dari Pillow, dan Label Raksasa (<code>font 90</code>) untuk menunjukkan Suhu!</p>
                        <p class="text-slate-600 text-sm italic">Note: Semua teks kita isi dengan teks *dummy* "--C" dulu.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># A. Label Nama Kota</span><br>
lbl_city = ctk.CTkLabel(app, text=<span class="text-green-300">"WEATHER DASHBOARD"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">18</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"white"</span>)<br>
lbl_city.pack()<br><br>
<span class="text-emerald-400"># B. Gambar Matahari (Default) Pakai OS Path!</span><br>
path_awal = os.path.join(os.path.dirname(__file__), <span class="text-green-300">"sunny.png"</span>)<br>
gambar_awal = ctk.CTkImage(Image.open(path_awal), size=(<span class="text-purple-400">220</span>, <span class="text-purple-400">220</span>))<br>
lbl_icon = ctk.CTkLabel(app, text=<span class="text-green-300">""</span>, image=gambar_awal)<br>
lbl_icon.pack(pady=<span class="text-purple-400">20</span>)<br><br>
<span class="text-emerald-400"># C. Teks Suhu Raksasa</span><br>
lbl_temp = ctk.CTkLabel(app, text=<span class="text-green-300">"--°C"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">90</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"white"</span>)<br>
lbl_temp.pack()<br><br>
<span class="text-emerald-400"># D. Teks Deskripsi (Hujan Rintik/Cerah)</span><br>
lbl_desc = ctk.CTkLabel(app, text=<span class="text-green-300">"Search for a city..."</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">14</span>), text_color=<span class="text-green-300">"#bfdbfe"</span>)<br>
lbl_desc.pack(pady=(<span class="text-purple-400">0</span>, <span class="text-purple-400">30</span>))
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 5)",
            "subtitle": "Kotak Stats Bawah (Mixed Layout)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Kotak Dasar di-PACK()</span><br>
stats = ctk.CTkFrame(app, fg_color=<span class="text-green-300">"#1e40af"</span>, corner_radius=<span class="text-purple-400">20</span>, border_width=<span class="text-purple-400">1</span>, border_color=<span class="text-green-300">"#3b82f6"</span>)<br>
stats.pack(pady=<span class="text-purple-400">10</span>, padx=<span class="text-purple-400">40</span>, fill=<span class="text-green-300">"x"</span>)<br>
stats.grid_columnconfigure((<span class="text-purple-400">0</span>, <span class="text-purple-400">1</span>), weight=<span class="text-purple-400">1</span>) <span class="text-blue-500"># Rahasia Lebar Sama Rata!</span><br><br>
<span class="text-emerald-400"># Anak-anaknya di-GRID() semua di dalam Stats!</span><br>
<span class="text-emerald-400"># Kelembapan (Kiri)</span><br>
ctk.CTkLabel(stats, text=<span class="text-green-300">"HUMIDITY"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">10</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"#93c5fd"</span>).grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">0</span>, pady=(<span class="text-purple-400">15</span>, <span class="text-purple-400">0</span>))<br>
lbl_hum_val = ctk.CTkLabel(stats, text=<span class="text-green-300">"--"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">24</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"white"</span>)<br>
lbl_hum_val.grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">0</span>, pady=(<span class="text-purple-400">0</span>, <span class="text-purple-400">15</span>))<br><br>
<span class="text-emerald-400"># Kecepatan Angin (Kanan)</span><br>
ctk.CTkLabel(stats, text=<span class="text-green-300">"WIND SPEED"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">10</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"#93c5fd"</span>).grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">1</span>, pady=(<span class="text-purple-400">15</span>, <span class="text-purple-400">0</span>))<br>
lbl_wind_val = ctk.CTkLabel(stats, text=<span class="text-green-300">"--"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">24</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"white"</span>)<br>
lbl_wind_val.grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">1</span>, pady=(<span class="text-purple-400">0</span>, <span class="text-purple-400">15</span>))<br><br>
<span class="text-emerald-400"># app.mainloop() - taruh di bawah!</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">5️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Panel Tambahan di Bawah</h3>
                        <p class="text-slate-600 text-lg">Buatlah kotak statistik <code>stats</code>, masukkan ke layar pakai <code>.pack()</code>. Lalu, isi kotak itu dengan Label Kelembapan dan Kecepatan Angin menggunakan sistem koordinat <code>.grid()</code>.</p>
                        <p class="text-slate-600 font-bold text-sm">Ingat Tuple: <code>(0, 1)</code> bisa langsung mengatur 2 kolom sekaligus!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Weather App 🌦️",
            "subtitle": "Karya Masterpiece-mu",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-700 rounded-2xl overflow-hidden bg-[#1e3a8a]">
                        <div class="p-6 h-[500px] flex flex-col justify-between items-center text-white space-y-4">
                            <!-- Search -->
                            <div class="flex w-full gap-2 mt-4">
                                <div class="bg-[#1e40af] border border-[#3b82f6] flex-grow rounded-lg p-2 text-slate-300 text-sm text-left">Enter city...</div>
                                <div class="bg-[#3b82f6] rounded-lg px-3 py-2 font-bold text-sm">SEARCH</div>
                            </div>
                            
                            <!-- Main Display -->
                            <div class="flex flex-col items-center mt-2">
                                <h3 class="font-bold text-lg">WEATHER DASHBOARD</h3>
                                <div class="text-[100px] my-2">☀️</div>
                                <h1 class="font-bold text-6xl">--°C</h1>
                                <p class="text-[#bfdbfe] italic mt-2 text-sm">Search for a city...</p>
                            </div>
                            
                            <!-- Stats Grid -->
                            <div class="bg-[#1e40af] border border-[#3b82f6] rounded-2xl w-full p-4 flex justify-around mt-4">
                                <div class="text-center">
                                    <p class="text-[9px] text-[#93c5fd] font-bold">HUMIDITY</p>
                                    <p class="text-xl font-bold">--</p>
                                </div>
                                <div class="text-center">
                                    <p class="text-[9px] text-[#93c5fd] font-bold">WIND SPEED</p>
                                    <p class="text-xl font-bold">--</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Tambah Footer Merek 🏢",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Powered by OpenWeather</h3>
                        <p class="text-slate-600 text-lg">Aplikasi profesional selalu mencantumkan sumber datanya di bagian paling bawah layar agar terlihat resmi.</p>
                    </div>
                    <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
                        <h4 class="font-bold text-indigo-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat satu buah <code>CTkLabel</code> tepat di bawah (setelah kode kotak Stats).</li>
                            <li>Beri teks: <i>"Data provided by OpenWeatherMap"</i>.</li>
                            <li>Gunakan ukuran font kecil (Misal: 10) dan warna samar seperti <code>#93c5fd</code> agar tidak mengganggu fokus utama layar.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Uji Ketahanan Layar 📱",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Ubah baris <code>app.geometry("500x750")</code> menjadi ukuran yang sangat gepeng: <code>"350x550"</code>.</li>
                            <li>Jalankan aplikasi! Apakah desainmu berantakan? Atau matahari jadi terpotong?</li>
                            <li>Coba perbaiki dengan menurunkan nilai <code>pady</code> pada *pack* dari masing-masing kotak agar mereka lebih merapat!</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Responsive UI Test</h3>
                        <p class="text-slate-600 text-lg">Setiap HP punya layar berbeda. Aplikasi yang bagus tidak akan pecah saat dijalankan di layar sempit!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Rombak Tema Visual 🖌️",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Bebaskan Kreativitasmu</h3>
                        <p class="text-slate-600 text-lg">Kenapa harus warna Biru Navy? Bagaimana kalau kamu membuat Aplikasi "Forest Weather" dengan dominasi Hijau Tua, atau "Midnight Weather" dominan Ungu?</p>
                    </div>
                    <div class="bg-green-50 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-900 border border-green-200">
<span class="text-green-700 font-bold"># Ganti kombinasi Hex Color di kode (Cari di Google):</span><br>
1. app.configure(fg_color="#064e3b") <span class="text-gray-500"># Dark Green</span><br>
2. border_color="#10b981" <span class="text-gray-500"># Emerald</span><br>
3. text_color="#d1fae5" <span class="text-gray-500"># Light Green</span><br>
<span class="text-green-600">Pastikan 3 komponen ini selaras agar desainmu nampak premium!</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Info: Psikologi Warna Biru 🌍",
            "subtitle": "Literasi UI/UX",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700 text-blue-300">
<span class="text-blue-400 font-bold"># Aplikasi yang dominan BIRU:</span><br>
- Facebook<br>
- Twitter / X (Sebelum ganti logo)<br>
- PayPal<br>
- IBM / Intel<br>
- 99% Aplikasi Cuaca
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kenapa Semuanya Biru?</h3>
                        <p class="text-slate-600 text-lg">Bukan kebetulan aplikasi kita berwarna Biru Navy. Dalam ilmu UI/UX (Desain Aplikasi Profesional), <b>Warna Biru memancarkan aura Kepercayaan, Kestabilan, dan Rasa Aman.</b></p>
                        <p class="text-slate-600 text-lg">Orang melihat ramalan cuaca untuk mencari keamanan (apakah aman pergi ke luar). Sama seperti orang membuka aplikasi Bank! Itulah kekuatan Psikologi Visual.</p>
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
                        <h4 class="font-bold text-blue-700 mb-3 text-xl">Senjata Front-End</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-blue-600">app.configure(fg_color=):</span> Mantra paksa mengubah total warna latar belakang aplikasi di luar tema bawaan.</li>
                            <li><span class="font-bold text-blue-600">Custom Entry:</span> Kotak teks (Entry) tidak boleh kaku. Kita bisa ubah isi <code>fg_color</code>, warna garis (<code>border_color</code>), dan warna huruf (<code>text_color</code>).</li>
                        </ul>
                    </div>
                    <div class="bg-cyan-50 border border-cyan-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-cyan-700 mb-3 text-xl">Sistem Layout Cerdas</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-cyan-600">Mixed Layout:</span> Jangan mencampur pack dan grid SEJAJAR. Bungkus dengan Frame (pakai pack), lalu isi frame tersebut pakai grid!</li>
                            <li><span class="font-bold text-cyan-600">Tuple Configure:</span> Tulis <code>(0,1)</code> di grid configure agar kamu nggak usah koding loop *for* atau nulis kodingan lebar kolom 2 kali lipat. Praktis!</li>
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
                        Design is not just what it looks like and feels like. Design is how it works.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— Steve Jobs (Co-founder of Apple)</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "10": \[\s*\{.*?\}\s*\],\s*"11": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_10.replace("\\\\`", "`") + '\\n    ],\\n    "11": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 10 successfully.")
