import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

# Define the new JSON part for "4": [...]
new_session_4 = """    "4": [
        {
            "title": "Meeting 4: Grid System 📊",
            "subtitle": "Mengatur Tata Letak seperti Pro",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🗂️</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Selamat tinggal tumpukan bata!</p>
                <p class="text-lg text-slate-600">Hari ini kita akan menyusun antarmuka dengan sistem <b>Grid</b>, seperti lemari atau rak laci yang rapi.</p>
                <div class="mt-8 grid sm:grid-cols-4 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-blue-50 border border-blue-100 p-4 text-blue-700">row & column</div>
                    <div class="rounded-xl bg-green-50 border border-green-100 p-4 text-green-700">sticky</div>
                    <div class="rounded-xl bg-yellow-50 border border-yellow-100 p-4 text-yellow-700">columnspan</div>
                    <div class="rounded-xl bg-slate-50 border border-slate-200 p-4 text-slate-700">weight</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 3 ⏪",
            "subtitle": "Review Materi Kemarin",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🎨</div><h4 class="font-bold text-slate-800">Hex Colors</h4><p class="text-sm text-slate-500 mt-2">Kode warna seperti #1f6aa5</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🕵️</div><h4 class="font-bold text-slate-800">show="*"</h4><p class="text-sm text-slate-500 mt-2">Menyembunyikan teks password</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">📐</div><h4 class="font-bold text-slate-800">Constants</h4><p class="text-sm text-slate-500 mt-2">Menyimpan warna di awal file</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">👀</div>
                    <p class="font-semibold text-slate-700 text-xl">Bagaimana cara mengubah warna teks pada CTkLabel?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb', 'Kurang tepat! font_color tidak ada di CustomTkinter.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. font_color="red"</button>
                        <button onclick="showMiniFeedback('fb1-fb', 'Tepat! text_color adalah parameter yang benar.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. text_color="red"</button>
                        <button onclick="showMiniFeedback('fb1-fb', 'Salah! fg_color digunakan untuk warna background.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. fg_color="red"</button>
                    </div>
                    <div id="fb1-fb" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami perbedaan <span class="font-mono text-blue-600 bg-blue-50 px-2 py-1 rounded">pack()</span> vs <span class="font-mono text-green-600 bg-green-50 px-2 py-1 rounded">grid()</span>.</li>
                        <li>Membuat antarmuka layaknya tabel (baris &amp; kolom).</li>
                        <li>Membuat elemen memanjang dengan <span class="font-mono text-slate-600 bg-slate-100 px-2 py-1 rounded">columnspan</span>.</li>
                        <li>Merapatkan posisi elemen dengan <span class="font-mono text-slate-600 bg-slate-100 px-2 py-1 rounded">sticky</span>.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Kelemahan pack() ⚠️",
            "subtitle": "Kenapa pack() tidak cukup?",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Tumpukan Barang</h3>
                        <p class="text-slate-600 text-lg"><span class="font-mono font-bold">.pack()</span> itu seperti menyusun barang di dalam kardus dari atas ke bawah. Sangat mudah jika hanya satu baris lurus.</p>
                        <p class="text-slate-600 text-lg">Tapi, bayangkan jika kamu ingin meletakkan Label di "kiri" dan Entry di "kanan" pada satu baris yang sama. <span class="font-mono">pack()</span> akan sangat kesulitan mengatur ini tanpa kode tambahan yang rumit!</p>
                    </div>
                    <div class="bg-red-50 p-6 rounded-xl border border-red-200 text-center">
                        <div class="text-5xl mb-4">📦</div>
                        <p class="text-red-700 font-bold">pack() = Tumpukan Atas-Bawah</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Halo grid()! 📏",
            "subtitle": "Kerapian adalah Kunci",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="bg-green-50 p-6 rounded-xl border border-green-200 text-center">
                        <div class="text-5xl mb-4">🗄️</div>
                        <p class="text-green-700 font-bold">grid() = Rak Lemari Tersusun</p>
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Sistem Koordinat</h3>
                        <p class="text-slate-600 text-lg"><span class="font-mono font-bold">.grid()</span> membagi jendela menjadi <b>Baris (row)</b> dan <b>Kolom (column)</b>.</p>
                        <p class="text-slate-600 text-lg">Mirip seperti papan catur atau Microsoft Excel! Kita tinggal menentukan widget diletakkan di kotak sebelah mana.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Row &amp; Column 📍",
            "subtitle": "Indeks dimulai dari 0",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <p class="text-lg text-slate-700">Di dunia programming, perhitungan selalu dimulai dari <b>Nol (0)</b>.</p>
                    <table class="w-full text-center border-collapse text-lg font-bold">
                        <tr>
                            <td class="border border-slate-300 p-4 bg-slate-100">(row=0, column=0)</td>
                            <td class="border border-slate-300 p-4 bg-slate-200">(row=0, column=1)</td>
                        </tr>
                        <tr>
                            <td class="border border-slate-300 p-4 bg-slate-200">(row=1, column=0)</td>
                            <td class="border border-slate-300 p-4 bg-slate-100">(row=1, column=1)</td>
                        </tr>
                    </table>
                    <p class="text-slate-600 text-sm mt-4 italic">Baris bertambah ke bawah, Kolom bertambah ke kanan.</p>
                </div>
            \`
        },
        {
            "title": "Mini Quiz: Row &amp; Column 🧠",
            "subtitle": "Cek Pemahaman!",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">📍</div>
                    <p class="font-semibold text-slate-700 text-xl">Jika saya ingin meletakkan tombol di <b>baris kedua</b> dan <b>kolom ketiga</b>, berapa nilai yang harus ditulis?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb', 'Ingat, indeks selalu dikurangi 1 karena mulai dari 0!', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. row=2, column=3</button>
                        <button onclick="showMiniFeedback('fb2-fb', 'Tepat sekali! Baris kedua adalah 1, dan kolom ketiga adalah 2.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. row=1, column=2</button>
                        <button onclick="showMiniFeedback('fb2-fb', 'Terbalik! Row untuk baris, Column untuk kolom.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. row=3, column=2</button>
                    </div>
                    <div id="fb2-fb" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Sticky (Menempel) 🧲",
            "subtitle": "Atur perataan (Alignment)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menempel ke Sisi</h3>
                        <p class="text-slate-600 text-lg">Gunakan arah mata angin untuk menempelkan widget di dalam kotaknya:</p>
                        <ul class="list-disc pl-5 text-slate-600">
                            <li><span class="font-mono font-bold text-blue-600">"n"</span>: North (Tengah-Atas)</li>
                            <li><span class="font-mono font-bold text-blue-600">"s"</span>: South (Tengah-Bawah)</li>
                            <li><span class="font-mono font-bold text-blue-600">"w"</span>: West (Kiri)</li>
                            <li><span class="font-mono font-bold text-blue-600">"e"</span>: East (Kanan)</li>
                            <li><span class="font-mono font-bold text-blue-600">"ew"</span>: Memanjang penuh Kiri-Kanan</li>
                        </ul>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Tombol ini rata ke kiri (West)</span><br>
btn.grid(row=0, column=1, sticky=<span class="text-yellow-300">"w"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 5: Columnspan ↔️",
            "subtitle": "Menggabungkan Sel",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Judul yang berada di tengah 2 kolom</span><br>
judul.grid(<br>
&nbsp;&nbsp;&nbsp;&nbsp;row=0,<br>
&nbsp;&nbsp;&nbsp;&nbsp;column=0,<br>
&nbsp;&nbsp;&nbsp;&nbsp;columnspan=2<br>
)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menguasai Ruang</h3>
                        <p class="text-slate-600 text-lg">Bila kamu ingin satu elemen menempati luas dua kolom (seperti fitur Merge &amp; Center di Excel), gunakan <span class="font-mono font-bold text-blue-600">columnspan</span>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Form Login Grid 🏗️",
            "subtitle": "Ayo kita koding! (Step 1)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Setup Jendela Baru</h3>
                        <p class="text-slate-600 text-lg">Buat file <code>login_grid.py</code>. Kita atur <i>padding</i> jendela luar agar isi form tidak nempel ke ujung layar.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Import dll</span><br>
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.geometry(<span class="text-green-300">"400x350"</span>)<br>
app.title(<span class="text-green-300">"Grid Form"</span>)<br><br>
<span class="text-emerald-400"># Memberi jarak internal untuk seluruh window</span><br>
app.grid_container = ctk.CTkFrame(app)<br>
app.grid_container.pack(pady=<span class="text-purple-400">30</span>, padx=<span class="text-purple-400">30</span>, fill=<span class="text-green-300">"both"</span>, expand=<span class="text-yellow-300">True</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Form Login Grid 🏗️",
            "subtitle": "Ayo kita koding! (Step 2)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Judul di Baris 0</span><br>
lbl_judul = ctk.CTkLabel(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app.grid_container, text=<span class="text-green-300">"Login Portal"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">24</span>, <span class="text-green-300">"bold"</span>)<br>
)<br>
<span class="text-emerald-400"># Karena form butuh 2 kolom, judul akan memakan ke 2 kolom</span><br>
lbl_judul.grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">0</span>, columnspan=<span class="text-purple-400">2</span>, pady=(<span class="text-purple-400">0</span>,<span class="text-purple-400">20</span>))
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyisipkan Judul (Row 0)</h3>
                        <p class="text-slate-600 text-lg">Judul selalu ditaruh di paling atas (<span class="font-mono">row=0</span>). Gunakan <span class="font-mono">columnspan=2</span> agar judul berada persis di tengah form kita yang punya dua lajur.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Form Login Grid 🏗️",
            "subtitle": "Ayo kita koding! (Step 3)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyisipkan Baris Pertama (Row 1)</h3>
                        <p class="text-slate-600 text-lg">Sisi kiri (<span class="font-mono">column=0</span>) untuk <b>Label</b>. Sisi kanan (<span class="font-mono">column=1</span>) untuk <b>Kotak Input</b>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Label Kiri (Row 1, Col 0)</span><br>
lbl_user = ctk.CTkLabel(app.grid_container, text=<span class="text-green-300">"Username:"</span>)<br>
lbl_user.grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">0</span>, sticky=<span class="text-green-300">"w"</span>, padx=<span class="text-purple-400">10</span>, pady=<span class="text-purple-400">10</span>)<br><br>
<span class="text-emerald-400"># Entry Kanan (Row 1, Col 1)</span><br>
entry_user = ctk.CTkEntry(app.grid_container, width=<span class="text-purple-400">200</span>)<br>
entry_user.grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">1</span>, padx=<span class="text-purple-400">10</span>, pady=<span class="text-purple-400">10</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Form Login Grid 🏗️",
            "subtitle": "Ayo kita koding! (Step 4)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Label Kiri (Row 2, Col 0)</span><br>
lbl_pass = ctk.CTkLabel(app.grid_container, text=<span class="text-green-300">"Password:"</span>)<br>
lbl_pass.grid(row=<span class="text-purple-400">2</span>, column=<span class="text-purple-400">0</span>, sticky=<span class="text-green-300">"w"</span>, padx=<span class="text-purple-400">10</span>, pady=<span class="text-purple-400">10</span>)<br><br>
<span class="text-emerald-400"># Entry Kanan (Row 2, Col 1)</span><br>
entry_pass = ctk.CTkEntry(app.grid_container, width=<span class="text-purple-400">200</span>, show=<span class="text-green-300">"*"</span>)<br>
entry_pass.grid(row=<span class="text-purple-400">2</span>, column=<span class="text-purple-400">1</span>, padx=<span class="text-purple-400">10</span>, pady=<span class="text-purple-400">10</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyisipkan Baris Kedua (Row 2)</h3>
                        <p class="text-slate-600 text-lg">Ulangi struktur yang sama tapi di baris berikutnya. Jangan lupa <span class="font-mono">show="*"</span> untuk password!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project 1: Form Login Grid 🏗️",
            "subtitle": "Ayo kita koding! (Step 5)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">5️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Akhiri dengan Tombol</h3>
                        <p class="text-slate-600 text-lg">Tombol login ditaruh di <span class="font-mono">row=3</span>, dan bisa memanjang memakai <span class="font-mono">columnspan=2</span>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Tombol Bawah (Row 3, Col 0 &amp; 1)</span><br>
btn_login = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app.grid_container, text=<span class="text-green-300">"Masuk"</span><br>
)<br>
btn_login.grid(<br>
&nbsp;&nbsp;&nbsp;&nbsp;row=<span class="text-purple-400">3</span>, column=<span class="text-purple-400">0</span>, columnspan=<span class="text-purple-400">2</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;pady=(<span class="text-purple-400">20</span>, <span class="text-purple-400">0</span>)<br>
)<br><br>
app.mainloop()
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Form Rapi 🎯",
            "subtitle": "Kerapian yang Hakiki",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Grid Form</div>
                        </div>
                        <div class="mock-window-content bg-[#242424] h-72 flex flex-col items-center justify-center p-6">
                            <h1 class="text-white text-xl font-bold mb-6">Login Portal</h1>
                            
                            <table class="w-full text-slate-300 text-sm">
                                <tr>
                                    <td class="pb-4 pr-4 font-semibold text-left">Username:</td>
                                    <td class="pb-4"><input type="text" class="w-full bg-[#343638] text-white px-3 py-2 rounded-md outline-none" placeholder=""></td>
                                </tr>
                                <tr>
                                    <td class="pb-6 pr-4 font-semibold text-left">Password:</td>
                                    <td class="pb-6"><input type="password" class="w-full bg-[#343638] text-white px-3 py-2 rounded-md outline-none" value="12345"></td>
                                </tr>
                                <tr>
                                    <td colspan="2">
                                        <button class="w-full py-2 rounded-md bg-[#1f6aa5] text-white font-bold hover:bg-blue-600 transition-colors">Masuk</button>
                                    </td>
                                </tr>
                            </table>
                        </div>
                    </div>
                    <p class="text-slate-500 italic mt-4 text-sm">Berkat Grid, baris dan jarak label terlihat sangat rapi dan presisi, berbeda jika hanya ditumpuk pakai pack!</p>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Kolom Email 💌",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Tambah Data</h3>
                        <p class="text-slate-600 text-lg">Form-mu masih kurang data Email. Tugasmu adalah <b>menyisipkan</b> sebaris form khusus Email <b>di antara</b> Username dan Password.</p>
                        <p class="text-slate-600 text-sm font-semibold text-blue-600 mt-2">Clue: Kamu harus menggeser <code>row</code> Password dan Tombol Login ke bawah (+1).</p>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200">
                        <h4 class="font-bold text-blue-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat CTkLabel "Email:".</li>
                            <li>Buat CTkEntry email.</li>
                            <li>Atur .grid() pada baris yang tepat.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Sticky Power 🧲",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-green-50 p-6 rounded-xl border border-green-200">
                        <h4 class="font-bold text-green-800 mb-3">Tugas:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Cari kode .grid() milik tombol Login.</li>
                            <li>Tambahkan parameter <span class="font-mono bg-white px-1">sticky="ew"</span>.</li>
                            <li>Jalankan dan lihat perubahan pada tombol!</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyebar Ke Samping</h3>
                        <p class="text-slate-600 text-lg">Tombol Login kamu sebelumnya ada di tengah karena menempati 2 kolom, tapi ukurannya tidak memanjang.</p>
                        <p class="text-slate-600 text-lg">Buat tombolmu "menempel" ke batas East (kanan) dan West (kiri) secara bersamaan!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Responsive Form 📱",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Fleksibel</h3>
                        <p class="text-slate-600 text-lg">Coba perbesar jendelamu perlahan pakai mouse. Kotak input-nya diam saja dan tidak ikut membesar, kan?</p>
                        <p class="text-slate-600 text-lg">Tambahkan <code>app.grid_container.grid_columnconfigure(1, weight=1)</code> sebelum baris <code>app.mainloop()</code> agar Kolom 1 (kolom input) melar secara otomatis.</p>
                    </div>
                    <div class="bg-purple-50 p-6 rounded-xl border border-purple-200 text-center">
                        <div class="text-6xl mb-4">⚖️</div>
                        <p class="text-purple-700 font-bold text-lg">weight = Bobot Pelebaran Kolom</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Project: Numpad Calculator 🔢",
            "subtitle": "Latihan Ekstra Grid",
            "content": \`
                <div class="max-w-5xl mx-auto">
                    <p class="text-slate-600 text-lg mb-4 text-center">Kapan kita butuh Grid yang sangat rapi? Saat membuat kalkulator!</p>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300 h-64 overflow-y-auto">
<span class="text-emerald-400"># Tombol-tombol bisa dibuat dengan cepat menggunakan perulangan (Loop)!</span><br>
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.geometry("300x400")<br><br>
tombol_angka = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "C", "0", "="]<br>
baris = 0<br>
kolom = 0<br><br>
for angka in tombol_angka:<br>
&nbsp;&nbsp;&nbsp;&nbsp;btn = ctk.CTkButton(app, text=angka, width=70, height=70)<br>
&nbsp;&nbsp;&nbsp;&nbsp;btn.grid(row=baris, column=kolom, padx=5, pady=5)<br>
&nbsp;&nbsp;&nbsp;&nbsp;kolom += 1<br>
&nbsp;&nbsp;&nbsp;&nbsp;if kolom > 2:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kolom = 0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;baris += 1<br><br>
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
                    <div class="bg-red-50 border border-red-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-red-700 mb-3 text-xl">❌ pack()</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li>Cepat dan sederhana.</li>
                            <li>Elemen saling bertumpuk (atas ke bawah / kiri ke kanan).</li>
                            <li>Kesulitan membuat layout form 2 kolom.</li>
                            <li>Tidak boleh dicampur dengan grid.</li>
                        </ul>
                    </div>
                    <div class="bg-green-50 border border-green-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-green-700 mb-3 text-xl">✅ grid()</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li>Lebih presisi layaknya Microsoft Excel.</li>
                            <li>Menggunakan <span class="font-mono font-bold text-blue-600">row</span> dan <span class="font-mono font-bold text-blue-600">column</span>.</li>
                            <li>Dapat menggabung baris/kolom (<span class="font-mono font-bold text-blue-600">columnspan</span>).</li>
                            <li>Bisa diatur kelenturannya (<span class="font-mono font-bold text-blue-600">weight</span>).</li>
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
                        A good layout is the difference between an app that looks like a prototype and one that looks professional.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— UI/UX Principle</p>
                </div>
            \`
        }"""

pattern = re.compile(r'    "4": \[\s*\{.*?\}\s*\],\s*"5": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_4 + '\n    ],\n    "5": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 4 successfully.")
