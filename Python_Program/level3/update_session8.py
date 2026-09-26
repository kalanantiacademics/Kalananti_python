import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_8 = """    "8": [
        {
            "title": "Meeting 8: Finalisasi Proyek Kalkulator 🧮",
            "subtitle": "Menggabungkan Semua Ilmu Menjadi Satu",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🚀</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Ujian Sebenarnya Dimulai!</p>
                <p class="text-lg text-slate-600">Dari Sesi 1 sampai Sesi 7, kita sudah mempelajari banyak hal keren: tombol, input, grid layout, variabel, fungsi, event, try-except. Hari ini, kita satukan semuanya untuk membuat aplikasi Kalkulator Asli!</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-blue-50 border border-blue-100 p-4 text-blue-700">Lambda & Eval()</div>
                    <div class="rounded-xl bg-green-50 border border-green-100 p-4 text-green-700">Dictionary Styling (**kwargs)</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 7 ⏪",
            "subtitle": "Review Materi Kemarin",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🖼️</div><h4 class="font-bold text-slate-800">Pillow (PIL)</h4><p class="text-sm text-slate-500 mt-2">Membaca file gambar agar bisa diproses Python</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">📁</div><h4 class="font-bold text-slate-800">os.path</h4><p class="text-sm text-slate-500 mt-2">Mencari letak file secara otomatis dan aman</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">⚙️</div><h4 class="font-bold text-slate-800">Abstraction</h4><p class="text-sm text-slate-500 mt-2">Membuat komponen UI dengan fungsi pembungkus (Helper)</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Apa fungsi utama dari <code>CTkImage</code> saat kita mau menampilkan gambar dari Pillow?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb8', 'Tepat! CTkImage menjembatani gambar dari format Pillow agar dimengerti dan bisa ditampilkan oleh label/tombol di CustomTkinter.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">A. Mengonversi gambar Pillow ke format yang bisa dipahami UI.</button>
                        <button onclick="showMiniFeedback('fb1-fb8', 'Salah! Tidak ada hubungannya dengan suara.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. Menambahkan efek suara saat gambar ditekan.</button>
                        <button onclick="showMiniFeedback('fb1-fb8', 'Salah! CTkImage bukan untuk membuat gambar baru dari nol.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Menggambar bentuk bulat atau kotak pakai kursor.</button>
                    </div>
                    <div id="fb1-fb8" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami <span class="font-bold text-blue-600">Lambda Function</span> untuk menyisipkan argumen/data ke dalam tombol.</li>
                        <li>Memakai keajaiban <span class="font-mono text-purple-600 bg-purple-50 px-2 py-1 rounded">eval()</span> untuk menghitung rumus matematika dari teks string seketika.</li>
                        <li>Menggunakan <b>Dictionary</b> (<code>**style</code>) agar tidak pegal mengetik konfigurasi warna yang sama berulang-ulang di puluhan tombol.</li>
                        <li>Menggabungkan <i>Grid System</i> tingkat lanjut (<code>sticky="nsew"</code>).</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Merancang Struktur Kalkulator 📐",
            "subtitle": "Rencana Induk",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Apa Saja Bagiannya?</h3>
                        <p class="text-slate-600 text-lg">Sebelum koding, kita harus merancang bagian aplikasinya:</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li><b>Layar Atas:</b> Sebuah Label penyimpan string, misal <code>"3+5*2"</code>.</li>
                            <li><b>Keyboard/Grid:</b> 4 kolom dan 5 baris tombol angka & simbol.</li>
                            <li><b>Mesin (Logika):</b> 3 Fungsi (Tambah angka, Hapus/Clear, Hitung/Sama-Dengan).</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200 text-center shadow-inner">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/58bad2ed-f676-47a3-9da6-4916ce11f61b.png" class="mx-auto rounded-lg h-40 object-contain">
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Fungsi Lambda (Penyelundup Data) 🥷",
            "subtitle": "Kelemahan Command=",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-red-50 p-5 rounded-xl font-mono text-xs text-left shadow-md border border-red-200">
<span class="text-red-500 font-bold"># SALAH:</span><br>
command=tambah_angka(7)<br><br>
<span class="text-red-600">Kalau begini, angka 7 otomatis terpanggil SAAT APLIKASI BARU DIBUKA (Belum diklik).</span>
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Lambda Function</h3>
                        <p class="text-slate-600 text-lg">Bagaimana kalau kita mau bikin banyak tombol (1, 2, 3...) pakai 1 fungsi yang sama? Kita butuh membawa "nilai" saat diklik.</p>
                        <p class="text-slate-600 text-lg">Solusinya adalah Lambda: <code>command=lambda: tambah_angka(7)</code>. Lambda membuat fungsi "tak bernama" yang hanya bekerja <b>saat tombol ditekan</b>!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Keajaiban Fungsi eval() ✨",
            "subtitle": "Mesin Hitung Bawaan Python",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Ubah String Jadi Hasil!</h3>
                        <p class="text-slate-600 text-lg">Menghitung <code>3+5*2</code> itu gampang buat kita, tapi bagaimana cara menyuruh komputer menghitung <b>string tulisan</b> "3+5*2"?</p>
                        <p class="text-slate-600 text-lg">Gunakan <code>eval()</code>. Ia otomatis membedah tulisan string, menghitung secara matematika (perkalian didahulukan), dan mengeluarkan hasil aslinya (13)!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300 text-sm">
tulisan_matematika = <span class="text-green-300">"3+5*2"</span><br><br>
hasil = eval(tulisan_matematika)<br>
print(hasil)<br><br>
<span class="text-emerald-400"># Output: 13</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Dictionary Styling & **kwargs 🎨",
            "subtitle": "Menghemat Ratusan Baris Kode",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-5 rounded-xl font-mono text-xs text-left shadow-md border border-blue-200 text-blue-900">
<span class="text-blue-700 font-bold"># Simpan gaya dalam 1 variabel Dictionary:</span><br>
gaya_ku = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;"fg_color": "#333333",<br>
&nbsp;&nbsp;&nbsp;&nbsp;"font": ("Arial", 18),<br>
&nbsp;&nbsp;&nbsp;&nbsp;"width": 60<br>
}<br><br>
<span class="text-blue-700 font-bold"># Gunakan ** untuk "Membongkar" isinya</span><br>
CTkButton(app, text="1", **gaya_ku)<br>
CTkButton(app, text="2", **gaya_ku)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Males Ngetik?</h3>
                        <p class="text-slate-600 text-lg">Kalkulator punya hampir 20 tombol! Kalau kamu mengetik <code>fg_color="#333", width=60, font=("Arial", 18)</code> di setiap tombol, jarimu akan keriting.</p>
                        <p class="text-slate-600 text-lg">Gunakan Dictionary yang dibongkar dengan bintang dua (<code>**</code>). Ini jurus Ninja Python!</p>
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
                    <p class="font-semibold text-slate-700 text-xl">Jika kita menjalankan kode <code>eval("10/2 + 3")</code>, apa hasilnya?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb8', 'Tepat sekali! Pembagian didahulukan 10/2=5, lalu 5+3=8. (Hasil float di Python biasa bernilai 8.0).', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">A. 8</button>
                        <button onclick="showMiniFeedback('fb2-fb8', 'Salah! eval() menghitung matematika, bukan menggabungkan teks.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. \"10/2 + 3\" (Tetap jadi teks string)</button>
                        <button onclick="showMiniFeedback('fb2-fb8', 'Salah! eval() paham hierarki matematika (kali bagi tambah kurang). Dia nggak mungkin ngitung 2+3 dulu.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. 2 (Karena 2+3 dihitung dulu jadi 5, terus 10/5=2)</button>
                    </div>
                    <div id="fb2-fb8" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Kalkulator 🧮 (Step 1)",
            "subtitle": "Setup Layout",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
import customtkinter as ctk<br><br>
app = ctk.CTk()<br>
app.title(<span class="text-green-300">"Archius Calc"</span>)<br>
app.geometry(<span class="text-green-300">"350x500"</span>)<br>
ctk.set_appearance_mode(<span class="text-green-300">"dark"</span>)<br><br>
<span class="text-emerald-400"># String Penyimpan Hitungan (State)</span><br>
persamaan = <span class="text-green-300">""</span><br><br>
<span class="text-emerald-400"># Layar Atas</span><br>
label_layar = ctk.CTkLabel(app, text=<span class="text-green-300">"0"</span>, font=(<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">50</span>, <span class="text-green-300">"bold"</span>), anchor=<span class="text-green-300">"e"</span>)<br>
label_layar.pack(pady=(<span class="text-purple-400">40</span>, <span class="text-purple-400">20</span>), padx=<span class="text-purple-400">20</span>, fill=<span class="text-green-300">"x"</span>)<br><br>
<span class="text-emerald-400"># Frame Grid untuk Tempat Tombol</span><br>
frame_tombol = ctk.CTkFrame(app, fg_color=<span class="text-green-300">"transparent"</span>)<br>
frame_tombol.pack(expand=<span class="text-orange-400 font-bold">True</span>, padx=<span class="text-purple-400">20</span>, pady=<span class="text-purple-400">20</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Kerangka Dasar</h3>
                        <p class="text-slate-600 text-lg">Buat jendela ukuran 350x500. Sediakan sebuah variabel global <code>persamaan</code>.</p>
                        <p class="text-slate-600 text-lg">Buat Layar Hitung pakai Label, lalu siapkan Frame Kosong <code>frame_tombol</code> untuk Grid tombol di bawahnya.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Kalkulator 🧮 (Step 2)",
            "subtitle": "Otak Logikanya!",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Fungsi Mesin Hitung</h3>
                        <p class="text-slate-600 text-lg">Tiga fungsi yang akan membuat kalkulator ini hidup: nambah angka, hapus angka (tombol C), dan ngehitung pakai <code>eval()</code> lengkap dengan pengaman <b>Try Except</b>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
def tambah_angka(angka):<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> persamaan<br>
&nbsp;&nbsp;&nbsp;&nbsp;persamaan += str(angka)<br>
&nbsp;&nbsp;&nbsp;&nbsp;label_layar.configure(text=persamaan)<br><br>
def hapus_layar():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> persamaan<br>
&nbsp;&nbsp;&nbsp;&nbsp;persamaan = <span class="text-green-300">""</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;label_layar.configure(text=<span class="text-green-300">"0"</span>)<br><br>
def hitung_hasil():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">global</span> persamaan<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hasil = str(eval(persamaan))<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_layar.configure(text=hasil)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;persamaan = hasil<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">except</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_layar.configure(text=<span class="text-green-300">"Error"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;persamaan = <span class="text-green-300">""</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Kalkulator 🧮 (Step 3)",
            "subtitle": "Kekuatan Styling Dictionary",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Bikin Gaya Tombol!</span><br>
style_angka = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"fg_color"</span>: <span class="text-green-300">"#333333"</span>, <span class="text-green-300">"hover_color"</span>: <span class="text-green-300">"#444444"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"text_color"</span>: <span class="text-green-300">"white"</span>, <span class="text-green-300">"font"</span>: (<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">18</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"height"</span>: <span class="text-purple-400">60</span>, <span class="text-green-300">"width"</span>: <span class="text-purple-400">60</span><br>
}<br><br>
style_ops = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"fg_color"</span>: <span class="text-green-300">"#FF9500"</span>, <span class="text-green-300">"hover_color"</span>: <span class="text-green-300">"#FFaa33"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"text_color"</span>: <span class="text-green-300">"white"</span>, <span class="text-green-300">"font"</span>: (<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">18</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"height"</span>: <span class="text-purple-400">60</span>, <span class="text-green-300">"width"</span>: <span class="text-purple-400">60</span><br>
}<br><br>
style_special = {<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"fg_color"</span>: <span class="text-green-300">"#A5A5A5"</span>, <span class="text-green-300">"hover_color"</span>: <span class="text-green-300">"#C5C5C5"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"text_color"</span>: <span class="text-green-300">"black"</span>, <span class="text-green-300">"font"</span>: (<span class="text-green-300">"Inter"</span>, <span class="text-purple-400">18</span>, <span class="text-green-300">"bold"</span>),<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"height"</span>: <span class="text-purple-400">60</span>, <span class="text-green-300">"width"</span>: <span class="text-purple-400">60</span><br>
}
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Gaya Tombol</h3>
                        <p class="text-slate-600 text-lg">Buat 3 gaya: Gaya Angka (Gelap), Gaya Operasi (+-*/ warna Oranye), dan Gaya Spesial (Tombol Clear/Persen warna abu terang).</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Kalkulator 🧮 (Step 4)",
            "subtitle": "Menggambar Grid Tombol",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyebar Tombolnya</h3>
                        <p class="text-slate-600 text-lg">Sekarang, tebar 20 tombol ke dalam Grid dengan koordinat baris (<code>row</code>) dan kolom (<code>column</code>)! Gunakan `**style_angka` dan `lambda`!</p>
                        <p class="text-slate-600 text-sm">Contoh baris 1 & 2:</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># BARIS 0 (C, %, /)</span><br>
ctk.CTkButton(frame_tombol, text=<span class="text-green-300">"C"</span>, command=hapus_layar, **style_special).grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">0</span>, columnspan=<span class="text-purple-400">2</span>, padx=<span class="text-purple-400">5</span>, pady=<span class="text-purple-400">5</span>, sticky=<span class="text-green-300">"nsew"</span>)<br>
ctk.CTkButton(frame_tombol, text=<span class="text-green-300">"%"</span>, command=lambda: tambah_angka(<span class="text-green-300">"%"</span>), **style_special).grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">2</span>, padx=<span class="text-purple-400">5</span>, pady=<span class="text-purple-400">5</span>, sticky=<span class="text-green-300">"nsew"</span>)<br>
ctk.CTkButton(frame_tombol, text=<span class="text-green-300">"/"</span>, command=lambda: tambah_angka(<span class="text-green-300">"/"</span>), **style_ops).grid(row=<span class="text-purple-400">0</span>, column=<span class="text-purple-400">3</span>, padx=<span class="text-purple-400">5</span>, pady=<span class="text-purple-400">5</span>, sticky=<span class="text-green-300">"nsew"</span>)<br><br>
<span class="text-emerald-400"># BARIS 1 (7, 8, 9, x)</span><br>
ctk.CTkButton(frame_tombol, text=<span class="text-green-300">"7"</span>, command=lambda: tambah_angka(<span class="text-purple-400">7</span>), **style_angka).grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">0</span>, padx=<span class="text-purple-400">5</span>, pady=<span class="text-purple-400">5</span>, sticky=<span class="text-green-300">"nsew"</span>)<br>
ctk.CTkButton(frame_tombol, text=<span class="text-green-300">"8"</span>, command=lambda: tambah_angka(<span class="text-purple-400">8</span>), **style_angka).grid(row=<span class="text-purple-400">1</span>, column=<span class="text-purple-400">1</span>, padx=<span class="text-purple-400">5</span>, pady=<span class="text-purple-400">5</span>, sticky=<span class="text-green-300">"nsew"</span>)<br>
<span class="text-emerald-400">... Lengkapi Sampai Baris 4 (Tombol 0, Titik, dan =) ...</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Kalkulator 🧮 (Step 5)",
            "subtitle": "Merapikan Bobot Grid & Start",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Loop Mengatur Kekenyalan/Bobot Tiap Sel Grid</span><br>
<span class="text-orange-400 font-bold">for</span> i <span class="text-orange-400 font-bold">in</span> range(<span class="text-purple-400">4</span>):<br>
&nbsp;&nbsp;&nbsp;&nbsp;frame_tombol.grid_columnconfigure(i, weight=<span class="text-purple-400">1</span>)<br><br>
<span class="text-orange-400 font-bold">for</span> i <span class="text-orange-400 font-bold">in</span> range(<span class="text-purple-400">5</span>):<br>
&nbsp;&nbsp;&nbsp;&nbsp;frame_tombol.grid_rowconfigure(i, weight=<span class="text-purple-400">1</span>)<br><br>
<span class="text-emerald-400"># Jalankan Aplikasi!</span><br>
app.mainloop()
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">5️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Proporsional Grid</h3>
                        <p class="text-slate-600 text-lg">Sebelum <code>app.mainloop()</code>, set <code>weight=1</code> untuk 4 kolom dan 5 barismu agar semuanya bisa melar serasi tanpa ada celah berantakan ketika jendela dibesarkan!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Kalkulator 🎯",
            "subtitle": "Apple Style Calculator",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-xs mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#212121] border-[#333]">
                            <div class="mock-window-title text-slate-200">Archius Calc</div>
                        </div>
                        <div class="mock-window-content bg-black h-96 flex flex-col p-4 space-y-2">
                            <!-- Layar -->
                            <div class="w-full text-right text-white text-5xl font-bold pt-8 pb-4">120</div>
                            <!-- Tombol (Mockup) -->
                            <div class="grid grid-cols-4 gap-2 flex-grow pb-2">
                                <div class="bg-gray-300 rounded-full flex items-center justify-center text-black font-bold col-span-2">C</div>
                                <div class="bg-gray-300 rounded-full flex items-center justify-center text-black font-bold">%</div>
                                <div class="bg-orange-500 rounded-full flex items-center justify-center text-white font-bold">/</div>
                                
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">7</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">8</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">9</div>
                                <div class="bg-orange-500 rounded-full flex items-center justify-center text-white font-bold text-xl">x</div>
                                
                                <!-- Dan seterusnya (Tidak perlu lengkap semua, ini visualisasi saja) -->
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">4</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">5</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">6</div>
                                <div class="bg-orange-500 rounded-full flex items-center justify-center text-white font-bold text-xl">-</div>
                                
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">1</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">2</div>
                                <div class="bg-gray-700 rounded-full flex items-center justify-center text-white font-bold text-xl">3</div>
                                <div class="bg-orange-500 rounded-full flex items-center justify-center text-white font-bold text-xl">+</div>
                            </div>
                        </div>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Angka Terlalu Panjang? 📉",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Batasi Desimal</h3>
                        <p class="text-slate-600 text-lg">Coba ketik <code>1/3</code>, hasilnya <code>0.3333333333</code> yang pasti akan meluber ke luar layarmu.</p>
                        <p class="text-slate-600 text-lg">Mari perbaiki pakai fungsi <code>round(hasil, 8)</code> di dalam fungsi <code>hitung_hasil()</code>.</p>
                    </div>
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Di dalam fungsi <code>hitung_hasil</code>, cek tipe datanya dulu:<br><code>if isinstance(hasil, float):</code></li>
                            <li>Lalu bulatkan:<br><code>hasil = round(hasil, 8)</code></li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Tombol Backspace 🔙",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200">
                        <h4 class="font-bold text-blue-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat fungsi baru: <code>def hapus_satu():</code></li>
                            <li>Potong string dari belakang (slicing):<br><code>persamaan = persamaan[:-1]</code></li>
                            <li>Sisipkan tombol backspace (Mungkin tombol 'DEL') di baris paling atas grid!</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menghapus 1 Angka</h3>
                        <p class="text-slate-600 text-lg">Gimana kalau salah ketik 1 angka saja? Kalau klik "C", semua terhapus. Buatlah fitur <i>Backspace</i>!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Ganti Tema Custom 🎨",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Desain Light Mode</h3>
                        <p class="text-slate-600 text-lg">Kalkulator Apple memang dominan gelap, sekarang buat jadi bergaya Android Material Light (Terang).</p>
                    </div>
                    <div class="bg-pink-50 p-6 rounded-xl border border-pink-200">
                        <h4 class="font-bold text-pink-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Ubah <code>set_appearance_mode</code> jadi "light".</li>
                            <li>Ganti isi <code>style_angka</code>, <code>style_ops</code>, dan <code>style_special</code> dengan paduan warna pastel yang keren (Misal: Pink, Biru Muda, Tosca).</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Info: Bahaya eval() ☢️",
            "subtitle": "Literasi Keamanan Cyber",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-6 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 text-green-300 h-64 overflow-y-auto">
<span class="text-red-500 font-bold"># Hacker memasukkan tulisan:</span><br>
<span class="text-emerald-400">__import__('os').system('rm -rf /')</span><br><br>
<span class="text-emerald-400"># Jika dimasukkan ke dalam eval()...</span><br>
eval(input_user)<br><br>
<span class="text-red-500 font-bold"># MAKA SELURUH SISTEM KOMPUTER AKAN TERHAPUS!</span>
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Amankan Kodemu!</h3>
                        <p class="text-slate-600 text-lg">Fungsi <code>eval()</code> bisa mengeksekusi script mematikan! Kalkulator kita "aman" karena user hanya bisa nge-klik tombol angka bawaan, bukan mengetik teks bebas.</p>
                        <p class="text-slate-600 text-lg">Di perusahaan besar, <i>programmer</i> jarang memakai <code>eval()</code>, tapi membuat mesin penghitung logika mandiri (<i>parsing</i>) yang jauh lebih aman.</p>
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
                        <h4 class="font-bold text-blue-700 mb-3 text-xl">Sihir Baru</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-blue-600">Lambda:</span> Fungsi misterius satu baris yang menunda eksekusi tombol sampai benar-benar diklik. (<code>command=lambda: halo("a")</code>).</li>
                            <li><span class="font-bold text-blue-600">eval():</span> Menghitung operasi matematika dari tulisan <i>string</i> menjadi hasil angka.</li>
                        </ul>
                    </div>
                    <div class="bg-green-50 border border-green-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-green-700 mb-3 text-xl">Senjata Styling</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-green-600">**kwargs (Dictionary):</span> Membongkar bungkus gaya desain UI (font, color) dan melemparnya ke puluhan tombol sekaligus (Koding efisien).</li>
                            <li><span class="font-bold text-green-600">Grid Configure:</span> <code>grid_columnconfigure(weight=1)</code> bikin tombol melebar proporsional.</li>
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
                        First, solve the problem. Then, write the code. (Pertama, pecahkan dulu masalahnya dalam kepalamu, baru kemudian tulis kodenya).
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— John Johnson</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "8": \[\s*\{.*?\}\s*\],\s*"9": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_8.replace("\\\\`", "`") + '\\n    ],\\n    "9": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 8 successfully.")
