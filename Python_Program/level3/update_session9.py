import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_9 = """    "9": [
        {
            "title": "Meeting 9: Task Manager Pintar 📝",
            "subtitle": "Archius Task Flow",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">✅</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Membangun Aplikasi To-Do List</p>
                <p class="text-lg text-slate-600">Selama ini kita membuat elemen UI (tombol, teks) di awal program. Bagaimana jika kita ingin menambahkan elemen UI <b>secara dinamis</b> hanya ketika *user* mengetik sesuatu? Hari ini kita akan belajar menciptakan dan menghancurkan elemen UI!</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-indigo-50 border border-indigo-100 p-4 text-indigo-700">Dynamic UI Creation</div>
                    <div class="rounded-xl bg-red-50 border border-red-100 p-4 text-red-700">.destroy() Method</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 8 ⏪",
            "subtitle": "Review Kalkulator",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🥷</div><h4 class="font-bold text-slate-800">Lambda</h4><p class="text-sm text-slate-500 mt-2">Menahan fungsi agar tak langsung tereksekusi</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">✨</div><h4 class="font-bold text-slate-800">eval()</h4><p class="text-sm text-slate-500 mt-2">Mesin hitung ajaib pembedah string</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🎨</div><h4 class="font-bold text-slate-800">**kwargs</h4><p class="text-sm text-slate-500 mt-2">Menyuntik gaya ke puluhan tombol sekaligus</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Kenapa kita butuh <code>lambda</code> saat menyambungkan tombol ke fungsi <code>tambah_angka(7)</code>?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb9', 'Salah! Tombol tidak menolak parameter, tapi parameter bikin fungsinya langsung jalan duluan.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Karena tombol CustomTkinter tidak menerima fungsi yang punya parameter.</button>
                        <button onclick="showMiniFeedback('fb1-fb9', 'Tepat! Tanpa lambda, python akan langsung menjalankan tambah_angka(7) saat aplikasi baru dibuka, bukan menunggu diklik.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Karena tanpa lambda, fungsinya akan langsung tereksekusi tanpa menunggu tombol diklik.</button>
                        <button onclick="showMiniFeedback('fb1-fb9', 'Salah! Lambda tidak merubah tipe data jadi string.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Supaya angka 7 diubah jadi huruf terlebih dahulu.</button>
                    </div>
                    <div id="fb1-fb9" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memecah kerumitan aplikasi menggunakan teknik <span class="font-bold text-blue-600">Dekomposisi UI</span>.</li>
                        <li>Membuat komponen *user interface* secara gaib ketika kode sedang berjalan (<span class="font-bold text-indigo-600">Dynamic Widget Creation</span>).</li>
                        <li>Menghapus jejak komponen dari memori komputer dengan <span class="font-mono text-red-600 bg-red-50 px-2 py-1 rounded">.destroy()</span>.</li>
                        <li>Menyelamatkan <code>lambda</code> dari kutukan <i>Variable Capture</i> pakai jurus <b>Default Argument</b>.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Seni Merencanakan (Dekomposisi) 🧩",
            "subtitle": "Pecah Jadi Bagian Kecil",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Jangan Koding Buta!</h3>
                        <p class="text-slate-600 text-lg">Programmer hebat tidak langsung ngetik kode. Mereka membelah masalah besar jadi kepingan kecil (<b>Decomposition</b>).</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li><span class="font-bold">Header:</span> Judul & Subjudul.</li>
                            <li><span class="font-bold">Input Area:</span> Kotak ketik (Entry) & Tombol Add.</li>
                            <li><span class="font-bold">List Area:</span> Tempat hasil tugas ditumpuk (Scrollable Frame).</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center shadow-inner">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/d0ca33ff-5a02-4041-8838-27ab2cee4739.jpg" class="mx-auto rounded-lg h-48 object-contain">
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Memanggil UI Secara Gaib 🪄",
            "subtitle": "Dynamic Widget Creation",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-indigo-50 p-5 rounded-xl border border-indigo-200 shadow-md">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/21362db9-d089-4251-ae5f-f14964e35523.jpg" class="mx-auto rounded-lg h-36 object-contain mb-4">
                        <p class="text-indigo-800 text-sm font-bold">Saat tombol tambah diklik, UI tugas baru TERCIPTA!</p>
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kapan UI Muncul?</h3>
                        <p class="text-slate-600 text-lg">Biasanya kita menulis <code>CTkButton()</code> di baris luar sehingga dia selalu ada saat aplikasi dibuka (<i>Static</i>).</p>
                        <p class="text-slate-600 text-lg">Kali ini, kita memasukkan pembuatan UI <b>di dalam fungsi</b>! Artinya, UI itu belum ada sampai si *user* menekan sebuah tombol tertentu.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Menghancurkan UI 💥",
            "subtitle": "Metode .destroy()",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menghapus Selamanya</h3>
                        <p class="text-slate-600 text-lg">Kalau kita punya tugas yang sudah beres, UI-nya harus dilenyapkan agar layar tidak penuh.</p>
                        <p class="text-slate-600 text-lg">Gunakan metode <code>.destroy()</code> pada Frame tugas tersebut. Ini akan menghapus frame sekaligus tulisan dan tombol di dalamnya ke <b>alam gaib</b> (dihapus bersih dari memori RAM).</p>
                    </div>
                    <div class="bg-red-50 p-5 rounded-xl border border-red-200 shadow-md">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/e33c4af1-67a4-46d5-9ffb-4761561d6755.jpg" class="mx-auto rounded-lg h-36 object-contain mb-4">
                        <p class="text-red-800 text-sm font-bold">Frame di-destroy() = Musnah tak tersisa.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Kutukan Variable Capture 🧟",
            "subtitle": "Lambda Default Argument",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-red-500 font-bold"># SALAH (Semua tombol akan menghapus tugas paling baru!):</span><br>
command=lambda: hapus_tugas(kotak_tugas)<br><br><br>
<span class="text-green-400 font-bold"># BENAR (Kunci nilai 'kotak_tugas' pakai 'f='):</span><br>
command=lambda f=kotak_tugas: hapus_tugas(f)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kunci Targetnya!</h3>
                        <p class="text-slate-600 text-lg">Kalau kamu bikin UI Dinamis berkali-kali pakai loop atau fungsi, <code>lambda</code> akan "pikun" dan selalu mengingat benda yang <b>terakhir kali</b> dibuat.</p>
                        <p class="text-slate-600 text-lg">Untuk mencegahnya, buat variabel bayangan (Default Argument) <code>f=kotak_tugas</code>. Ini menyuruh Python memfoto memori pada saat itu juga!</p>
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
                    <p class="font-semibold text-slate-700 text-xl">Apa yang terjadi jika kita me-<code>.destroy()</code> sebuah <b>Frame</b> yang di dalamnya berisi Label Judul dan Tombol Close?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb9', 'Salah! Frame tidak menyembunyikan isi, destroy akan memusnahkan semuanya.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Frame-nya hancur, tapi tulisan label dan tombol close-nya akan melayang di layar.</button>
                        <button onclick="showMiniFeedback('fb2-fb9', 'Tepat! Semua \"anak\" di dalam Frame tersebut (Label dan Tombol) akan ikut musnah dihapus dari memori bersama dengan Frame induknya.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Seluruh Frame beserta label dan tombol di dalamnya akan ikut musnah.</button>
                        <button onclick="showMiniFeedback('fb2-fb9', 'Salah! Error tidak terjadi kalau destroy digunakan pada Frame yang benar.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Error sistem terjadi karena tombolnya harus dihapus satu per satu dulu.</button>
                    </div>
                    <div id="fb2-fb9" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Task Manager 📝 (Step 1)",
            "subtitle": "Header & Input Area",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.title(<span class="text-green-300">"Archius Task Flow"</span>)<br>
app.geometry(<span class="text-green-300">"420x600"</span>)<br>
ctk.set_appearance_mode(<span class="text-green-300">"light"</span>)<br><br>
<span class="text-emerald-400"># Header App</span><br>
ctk.CTkLabel(app, text=<span class="text-green-300">"ARCHIUS TASK FLOW"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">24</span>, <span class="text-green-300">"bold"</span>), text_color=<span class="text-green-300">"#2563EB"</span>).pack(pady=(<span class="text-purple-400">30</span>, <span class="text-purple-400">5</span>))<br><br>
<span class="text-emerald-400"># Frame khusus untuk Box Ketik & Tombol Tambah</span><br>
input_frame = ctk.CTkFrame(app, fg_color=<span class="text-green-300">"transparent"</span>)<br>
input_frame.pack(pady=<span class="text-purple-400">10</span>, padx=<span class="text-purple-400">20</span>, fill=<span class="text-green-300">"x"</span>)<br><br>
box_ketik = ctk.CTkEntry(input_frame, placeholder_text=<span class="text-green-300">"Ada jadwal apa hari ini?"</span>, height=<span class="text-purple-400">45</span>)<br>
box_ketik.pack(side=<span class="text-green-300">"left"</span>, fill=<span class="text-green-300">"x"</span>, expand=<span class="text-orange-400 font-bold">True</span>, padx=(<span class="text-purple-400">0</span>, <span class="text-purple-400">10</span>))<br><br>
<span class="text-emerald-400"># Tombol Tambah (Fungsinya nanti kita buat!)</span><br>
btn_tambah = ctk.CTkButton(input_frame, text=<span class="text-green-300">"+"</span>, width=<span class="text-purple-400">50</span>, height=<span class="text-purple-400">45</span>)<br>
btn_tambah.pack(side=<span class="text-green-300">"right"</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Kerangka Bagian Atas</h3>
                        <p class="text-slate-600 text-lg">Buat Judul, lalu buat <code>input_frame</code> secara mendatar (horizontal) yang berisi kotak <b>Entry</b> (untuk ketik) dan <b>Button +</b>.</p>
                        <p class="text-slate-600 text-sm">Gunakan kombinasi <code>side="left"</code> dan <code>side="right"</code> di dalam <code>.pack()</code> agar mereka berjejer menyamping.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Task Manager 📝 (Step 2)",
            "subtitle": "Keranjang Tugas (Scrollable)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menampung Jutaan Tugas</h3>
                        <p class="text-slate-600 text-lg">Di bawah kotak ketik, letakkan <code>CTkScrollableFrame</code>. Nanti, setiap tugas baru akan "ditempelkan" ke dalam keranjang gulung ini!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Area Daftar Tugas yang bisa di-scroll</span><br>
daftar_frame = ctk.CTkScrollableFrame(<br>
&nbsp;&nbsp;&nbsp;&nbsp;app,<br>
&nbsp;&nbsp;&nbsp;&nbsp;fg_color=<span class="text-green-300">"#F8FAFC"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;label_text=<span class="text-green-300">"Tasks To-Do"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;label_text_color=<span class="text-green-300">"#1E3A8A"</span><br>
)<br>
daftar_frame.pack(pady=<span class="text-purple-400">20</span>, padx=<span class="text-purple-400">20</span>, fill=<span class="text-green-300">"both"</span>, expand=<span class="text-orange-400 font-bold">True</span>)<br><br>
<span class="text-emerald-400"># app.mainloop() - (Taruh ini di garis terbawah kodinganmu ya!)</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Task Manager 📝 (Step 3)",
            "subtitle": "UI Dinamis (Fungsi Tambah)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Buat fungsi ini TEPAT DI BAWAH ctk.set_appearance_mode!</span><br>
def tambah_tugas():<br>
&nbsp;&nbsp;&nbsp;&nbsp;teks_tugas = box_ketik.get()<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Cek jika tidak kosong</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">if</span> teks_tugas != <span class="text-green-300">""</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Bikin Kotak UI (Baru!)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kotak = ctk.CTkFrame(daftar_frame, fg_color=<span class="text-green-300">"white"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kotak.pack(pady=<span class="text-purple-400">5</span>, padx=<span class="text-purple-400">10</span>, fill=<span class="text-green-300">"x"</span>)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Bikin Tulisan di dalam Kotaknya</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl = ctk.CTkLabel(kotak, text=teks_tugas)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl.pack(side=<span class="text-green-300">"left"</span>, padx=<span class="text-purple-400">15</span>, pady=<span class="text-purple-400">10</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyulap Frame Baru</h3>
                        <p class="text-slate-600 text-lg">Fungsi <code>tambah_tugas</code> ini akan membaca isi <code>box_ketik.get()</code>.</p>
                        <p class="text-slate-600 text-lg">Jika teksnya ada, dia akan menciptakan 1 Frame (kotak putih) di dalam <code>daftar_frame</code>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Task Manager 📝 (Step 4)",
            "subtitle": "Tombol Penghancur Tugas",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Delete Button</h3>
                        <p class="text-slate-600 text-lg">Tugas yang sudah selesai harus bisa dihapus. Bikin tombol silang merah "X", dan letakkan di sebelah kanan.</p>
                        <p class="text-slate-600 text-lg text-red-600 font-bold">AWAS! Gunakan pelindung <code>lambda f=kotak</code> agar aman dari kebocoran memori!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Bikin Fungsi Menghapus DULU (Taruh di atas tambah_tugas)</span><br>
def hapus_tugas(frame_target):<br>
&nbsp;&nbsp;&nbsp;&nbsp;frame_target.destroy()<br><br>
<span class="text-emerald-400"># Lanjutkan di dalam fungsi tambah_tugas(), setelah lbl.pack()</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_hapus = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kotak, text=<span class="text-green-300">"x"</span>, width=<span class="text-purple-400">30</span>, fg_color=<span class="text-green-300">"red"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command=lambda f=kotak: hapus_tugas(f)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;btn_hapus.pack(side=<span class="text-green-300">"right"</span>, padx=<span class="text-purple-400">10</span>)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Kosongkan Box Ketik!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;box_ketik.delete(<span class="text-purple-400">0</span>, <span class="text-green-300">"end"</span>)<br><br>
<span class="text-emerald-400"># TERAKHIR! Jangan lupa pasang command=tambah_tugas di btn_tambah (Langkah 1).</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Task Flow 📋",
            "subtitle": "Karya Canggihmu!",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-300 rounded-2xl overflow-hidden bg-[#F8FAFC]">
                        <div class="bg-white p-6 border-b border-slate-200">
                            <h2 class="text-xl font-bold text-blue-600 mb-1">ARCHIUS TASK FLOW</h2>
                            <div class="flex gap-2">
                                <div class="bg-slate-100 flex-grow rounded-xl p-2 text-slate-400 text-sm text-left">Ada jadwal apa hari ini?</div>
                                <div class="bg-blue-600 rounded-xl px-4 py-2 text-white font-bold">+</div>
                            </div>
                        </div>
                        <div class="p-4 space-y-2 h-64 overflow-hidden relative">
                            <!-- Task 1 -->
                            <div class="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex justify-between items-center">
                                <span class="text-slate-800">Kerjakan PR Coding</span>
                                <div class="bg-red-500 rounded-lg w-8 h-8 flex items-center justify-center text-white font-bold">x</div>
                            </div>
                            <!-- Task 2 -->
                            <div class="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex justify-between items-center">
                                <span class="text-slate-800">Beli Makan Siang</span>
                                <div class="bg-red-500 rounded-lg w-8 h-8 flex items-center justify-center text-white font-bold">x</div>
                            </div>
                            <!-- Task 3 -->
                            <div class="bg-white rounded-xl p-3 shadow-sm border border-slate-200 flex justify-between items-center">
                                <span class="text-slate-800">Main Valorant Bareng Tim</span>
                                <div class="bg-red-500 rounded-lg w-8 h-8 flex items-center justify-center text-white font-bold">x</div>
                            </div>
                        </div>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Tandai Selesai ✅",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Warna Abu-Abu Tanda Usai</h3>
                        <p class="text-slate-600 text-lg">Kadang kita malas menghapus, kita cuma mau melihat kalau itu "Sudah Selesai". Tambahkan tombol <code>[ v ]</code> di sebelah kiri nama tugas.</p>
                    </div>
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat fungsi: <br><code>def selesai(frame): frame.configure(fg_color="gray")</code></li>
                            <li>Buat Tombol centang (warna hijau) tepat di sebelah kiri label teks tugas.</li>
                            <li>Gunakan ilmu lambda pengaman: <br><code>command=lambda f=kotak: selesai(f)</code>.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Total Tugas Aktif 📊",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
                        <h4 class="font-bold text-indigo-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat label `total_label` di bawah header dengan teks "0 Tugas Tersisa".</li>
                            <li>Gunakan fitur ajaib: <code>daftar_frame.winfo_children()</code> yang otomatis menghitung ada berapa jumlah kotak(anak) di dalam *Scrollable Frame*.</li>
                            <li>Update `total_label.configure(text=...)` di dalam fungsi Tambah dan Hapus.</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Sub Header Dinamis</h3>
                        <p class="text-slate-600 text-lg">Alangkah serunya kalau di atas keranjang, ada peringatan: <b>"Kamu punya 5 tugas belum selesai!"</b> yang angkanya naik/turun setiap kali kamu menghapus atau menambah tugas.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Tombol Sapu Jagat 🧹",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Clear All Tasks</h3>
                        <p class="text-slate-600 text-lg">Akhir minggu tiba! Saatnya menghapus 20 tugas yang ada di layar sekaligus pakai 1 tombol: <b>Clear All</b>.</p>
                    </div>
                    <div class="bg-red-50 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-red-900 border border-red-200">
<span class="text-red-500 font-bold"># Clue:</span><br>
Pakai perulangan (For Loop) untuk membedah `winfo_children()`.<br><br>
for anak in daftar_frame.winfo_children():<br>
&nbsp;&nbsp;&nbsp;&nbsp;anak.destroy()
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Info: Kelemahan Sistem Kita 💡",
            "subtitle": "Konsep Persistence",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 text-green-300">
<span class="text-emerald-400"># Menulis data (Menyimpan):</span><br>
with open(<span class="text-green-300">"data.txt"</span>, <span class="text-green-300">"w"</span>) as file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;file.write(teks_tugas + <span class="text-green-300">"\\n"</span>)<br><br>
<span class="text-emerald-400"># Membaca saat aplikasi baru dibuka:</span><br>
with open(<span class="text-green-300">"data.txt"</span>, <span class="text-green-300">"r"</span>) as file:<br>
&nbsp;&nbsp;&nbsp;&nbsp;semua = file.readlines()
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Amnesia Digital</h3>
                        <p class="text-slate-600 text-lg">Jika kamu tutup aplikasi Task Manager ini dan buka lagi, <b>semua tugasmu hilang!</b> Kenapa? Karena data cuma disimpan di RAM (sementara).</p>
                        <p class="text-slate-600 text-lg">Aplikasi beneran (seperti WhatsApp) menyimpan data secara <b>Persistent</b> (permanen) ke dalam Hard Disk menggunakan Database atau sekadar file teks (<code>.txt</code> / <code>.json</code>).</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Summary 📝",
            "subtitle": "Ringkasan Pembelajaran",
            "content": \`
                <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                    <div class="bg-indigo-50 border border-indigo-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-indigo-700 mb-3 text-xl">Dinamis Itu Keren</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-indigo-600">Dynamic UI:</span> Membuat frame dan label di dalam sebuah fungsi untuk mendatangkan komponen layar secara *"on-demand"*.</li>
                            <li><span class="font-bold text-indigo-600">.destroy():</span> Alat penghancur. Menghapus frame secara permanen (bersama anak-anaknya).</li>
                        </ul>
                    </div>
                    <div class="bg-green-50 border border-green-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-green-700 mb-3 text-xl">Jurus Bertahan Hidup</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-green-600">Lambda Target Kunci:</span> <code>lambda f=target: hapus(f)</code> memastikan tombol tidak amnesia dan salah sasaran saat menghapus objek.</li>
                            <li><span class="font-bold text-green-600">Dekomposisi:</span> Pecahkan aplikasi besar menjadi bagian kecil (Header, Input, List) sebelum menulis 1 baris pun kodingan.</li>
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
                        The secret of getting ahead is getting started. The secret of getting started is breaking your complex tasks into small manageable tasks.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— Mark Twain (Writer)</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "9": \[\s*\{.*?\}\s*\],\s*"10": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_9.replace("\\\\`", "`") + '\\n    ],\\n    "10": [', content, count=1)

# Escape JS template literal bugs
new_content = new_content.replace("winfo_children()`.", "<code>winfo_children()</code>.")
new_content = new_content.replace("`total_label.configure(text=...)`", "<code>total_label.configure(text=...)</code>")
new_content = new_content.replace("`winfo_children()`.", "<code>winfo_children()</code>.")

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 9 successfully.")
