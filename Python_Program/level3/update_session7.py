import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_7 = """    "7": [
        {
            "title": "Meeting 7: Bermain Gambar 🖼️",
            "subtitle": "Memasukkan Visual ke dalam UI",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🎨</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Tinggalkan Aplikasi Membosankan!</p>
                <p class="text-lg text-slate-600">Aplikasi yang kita buat selama ini hanya pakai tulisan. Sekarang, kita akan bikin antarmuka kita "hidup" dengan menambahkan gambar, foto, dan belajar bikin komponen berulang (Abstraction).</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-orange-50 border border-orange-100 p-4 text-orange-700">Pillow (PIL)</div>
                    <div class="rounded-xl bg-purple-50 border border-purple-100 p-4 text-purple-700">CTkImage & CTkScrollableFrame</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 6 ⏪",
            "subtitle": "Review Materi Kemarin",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🛡️</div><h4 class="font-bold text-slate-800">Robustness</h4><p class="text-sm text-slate-500 mt-2">Ketangguhan aplikasi terhadap error</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🪤</div><h4 class="font-bold text-slate-800">try - except</h4><p class="text-sm text-slate-500 mt-2">Menangkap error sebelum sistem crash</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">⏱️</div><h4 class="font-bold text-slate-800">app.after()</h4><p class="text-sm text-slate-500 mt-2">Timer pintar tanpa bikin layar beku</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">👀</div>
                    <p class="font-semibold text-slate-700 text-xl">Kenapa kita pakai <code>app.after()</code> untuk membikin Timer dan sangat menghindari <code>time.sleep(1)</code>?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb7', 'Salah! Tidak ada pengaruh langsung dengan baterai laptop.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Karena time.sleep() akan membuat baterai laptop habis.</button>
                        <button onclick="showMiniFeedback('fb1-fb7', 'Tepat sekali! time.sleep() menghentikan seluruh program (termasuk UI) sehingga layar \"Not Responding\".', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">B. Karena time.sleep() memblokir aplikasi (freeze), sehingga tombol tak bisa diklik.</button>
                        <button onclick="showMiniFeedback('fb1-fb7', 'Salah! after() tidak lebih cepat, hanya berbeda cara eksekusinya (asinkron).', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Karena time.sleep() itu terlalu lambat.</button>
                    </div>
                    <div id="fb1-fb7" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami cara menggunakan <b>Pillow</b> (PIL) untuk memproses gambar.</li>
                        <li>Memahami <span class="font-mono text-blue-600 bg-blue-50 px-2 py-1 rounded">os.path</span> agar gambar tidak hilang ("File Not Found").</li>
                        <li>Menampilkan gambar ke UI dengan <span class="font-mono text-orange-600 bg-orange-50 px-2 py-1 rounded">CTkImage</span>.</li>
                        <li>Menerapkan <b>Abstraction</b> (Fungsi Helper) untuk membuat kartu resep yang bisa dipakai ulang berkali-kali!</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Aplikasi Bukan Cuma Teks 📰",
            "subtitle": "Zaman Sudah Modern",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kenapa Gambar Penting?</h3>
                        <p class="text-slate-600 text-lg">Coba bayangkan <i>Instagram</i> atau <i>Gojek</i> tanpa gambar. Pasti bosan!</p>
                        <p class="text-slate-600 text-lg">Aplikasi modern menggunakan elemen visual (foto, ikon) untuk memikat <i>user</i>. Hari ini kita akan buat aplikasi "Katalog Resep Kue" bernama <b>Cake Bliss</b>!</p>
                    </div>
                    <div class="bg-pink-50 p-6 rounded-xl border border-pink-200 text-center">
                        <div class="text-5xl mb-4">🍰</div>
                        <p class="text-pink-700 font-bold">"Sebuah gambar bernilai ribuan kata-kata."</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Cara Python Melihat Gambar 🔎",
            "subtitle": "Butuh Library Ekstra",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-100 p-6 rounded-xl border border-slate-300 text-center">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/44e7b398-a31d-4d4d-a863-3b306b58b434.png" class="mx-auto h-32 rounded-lg">
                        <p class="text-slate-700 font-bold mt-4">Pillow (PIL)</p>
                    </div>
                    <div class="text-left space-y-4">
                        <p class="text-slate-600 text-lg">Secara bawaan, Python tidak tahu cara membaca format <code>.jpg</code> atau <code>.png</code>.</p>
                        <p class="text-slate-600 text-lg">Kita butuh "kacamata" tambahan bernama <b>Pillow</b> (Library terpopuler di Python untuk memproses gambar). Setelah dibaca Pillow, barulah <b>CustomTkinter</b> bisa menyulapnya jadi UI.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: os.path (Pencarian File Aman) 📁",
            "subtitle": "Jangan Sampai File Not Found",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Menghindari Error</h3>
                        <p class="text-slate-600 text-lg">Terkadang Python kebingungan mencari file gambarmu jika dijalankan dari Terminal di <i>folder</i> yang berbeda.</p>
                        <p class="text-slate-600 text-lg">Modul <code>os</code> akan memaksa Python: <b>"Cari gambarnya persis di folder tempat file kodemu berada!"</b></p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300 text-sm">
import os<br><br>
<span class="text-emerald-400"># Dapatkan path folder saat ini:</span><br>
folder = os.path.dirname(__file__)<br><br>
<span class="text-emerald-400"># Gabung dengan nama file gambarnya:</span><br>
path_asli = os.path.join(folder, <span class="text-green-300">"kue.png"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: Abstraction / Fungsi Helper ⚙️",
            "subtitle": "Jangan Koding Berulang-ulang!",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-5 rounded-xl font-mono text-sm text-left shadow-md border border-blue-200 text-blue-900">
def buat_kartu(nama, harga):<br>
&nbsp;&nbsp;&nbsp;&nbsp;kotak = ctk.CTkFrame(app)<br>
&nbsp;&nbsp;&nbsp;&nbsp;kotak.pack()<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl = ctk.CTkLabel(kotak, text=nama)<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl.pack()<br><br>
<span class="text-blue-600 font-bold"># Tinggal panggil berkali-kali!</span><br>
buat_kartu("Mie Ayam", 15000)<br>
buat_kartu("Bakso", 20000)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Reusable Component</h3>
                        <p class="text-slate-600 text-lg">Bayangkan ada 10 kue. Masak kamu mau ketik <code>CTkLabel</code> 10 kali? Cukup buat <b>1 Fungsi (Helper)</b> yang otomatis membuat kotaknya beserta gambar dan tulisan.</p>
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
                    <p class="font-semibold text-slate-700 text-xl">Apa untungnya kita membuat "Fungsi Helper" untuk membuat komponen UI (seperti Kartu Kue)?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb7', 'Tepat! Kita mencegah nulis kode CTkFrame dan CTkLabel yang sama berulang-ulang ratusan baris.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">A. Kode lebih pendek, tidak perlu nulis berulang-ulang untuk komponen yang mirip bentuknya.</button>
                        <button onclick="showMiniFeedback('fb2-fb7', 'Salah! Fungsi helper tidak membuat warna layar berubah, dia hanya mempermudah penulisan.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. Karena tanpa fungsi helper layarnya akan berwarna hitam putih.</button>
                        <button onclick="showMiniFeedback('fb2-fb7', 'Salah! Malah error kalau fungsi belum dipanggil sama sekali.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. Supaya tombol start bisa dihapus.</button>
                    </div>
                    <div id="fb2-fb7" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 1)",
            "subtitle": "Instalasi Pillow",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Buka Terminal di VS Code:</span><br>
<span class="text-green-300">$ pip install Pillow</span><br><br>
<span class="text-emerald-400"># Tunggu "Successfully installed"</span><br><br>
<span class="text-emerald-400"># Bikin file main.py:</span><br>
import customtkinter as ctk<br>
from PIL import Image <span class="text-emerald-400"># Import Pillow</span><br>
import os
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Download Library</h3>
                        <p class="text-slate-600 text-lg">Sebelum coding, kita wajib mengunduh Pillow via terminal: <code>pip install Pillow</code>.</p>
                        <p class="text-slate-600 text-lg">Note: Gambar (e.g. <code>kue1.png</code>) HARUS ada satu folder dengan file python mu!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 2)",
            "subtitle": "Bikin Layout Utama",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Layout & Warna</h3>
                        <p class="text-slate-600 text-lg">Siapkan konstanta warna favoritmu. Jangan lupa pakai <code>CTkScrollableFrame</code> agar aplikasinya bisa digulir ke bawah saat kuenya banyak!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
app = ctk.CTk()<br>
app.title(<span class="text-green-300">"Cake Bliss"</span>)<br>
app.geometry(<span class="text-green-300">"450x650"</span>)<br><br>
PINK = <span class="text-green-300">"#FF85A1"</span><br>
CREAM = <span class="text-green-300">"#FFF5F5"</span><br><br>
<span class="text-emerald-400"># Frame yang bisa di-scroll</span><br>
main_frame = ctk.CTkScrollableFrame(app, fg_color=CREAM)<br>
main_frame.pack(fill=<span class="text-green-300">"both"</span>, expand=<span class="text-orange-400 font-bold">True</span>)<br><br>
<span class="text-emerald-400"># Judul App</span><br>
lbl_judul = ctk.CTkLabel(main_frame, text=<span class="text-green-300">"CAKE BLISS 🍰"</span>, font=(<span class="text-green-300">"Georgia"</span>, <span class="text-purple-400">30</span>, <span class="text-green-300">"bold"</span>), text_color=PINK)<br>
lbl_judul.pack(pady=<span class="text-purple-400">20</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 3)",
            "subtitle": "Fungsi Helper Kartu (Belum Berisi)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Fungsi Pencetak Kartu Kue (Abstraction)</span><br>
def buat_kartu_kue(judul, resep, nama_gambar):<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># 1. Kotak Dasarnya</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;card = ctk.CTkFrame(main_frame, fg_color=<span class="text-green-300">"white"</span>, corner_radius=<span class="text-purple-400">15</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;card.pack(pady=<span class="text-purple-400">15</span>, padx=<span class="text-purple-400">20</span>, fill=<span class="text-green-300">"x"</span>)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># (Nanti kita tambah Label Text & Gambar disini!)</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Kerangka Fungsi Helper</h3>
                        <p class="text-slate-600 text-lg">Fungsi ini butuh 3 variabel/parameter: judul, resep, dan gambar. Ia membungkus semuanya dalam 1 Frame bernama <code>card</code>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 4)",
            "subtitle": "Menambah Teks ke Kartu",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Isi Kartunya (Bagian Teks)</h3>
                        <p class="text-slate-600 text-lg">Tambahkan Label Judul Kue dan Deskripsi Resep <b>di dalam fungsi</b> tadi! (Gunakan <code>card</code> sebagai parent, jangan <code>main_frame</code>!).</p>
                        <p class="text-slate-600 text-lg"><code>wraplength=300</code> memaksa teks turun jika terlalu panjang (Mencegah meluber).</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># ...Lanjutan di dalam Fungsi buat_kartu_kue...</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_nama = ctk.CTkLabel(card, text=judul, font=(<span class="text-green-300">"Arial"</span>, <span class="text-purple-400">20</span>, <span class="text-green-300">"bold"</span>))<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_nama.pack(pady=<span class="text-purple-400">5</span>)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_desc = ctk.CTkLabel(card, text=resep, text_color=<span class="text-green-300">"gray"</span>, wraplength=<span class="text-purple-400">300</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_desc.pack(pady=<span class="text-purple-400">10</span>, padx=<span class="text-purple-400">10</span>)<br>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 5)",
            "subtitle": "Keajaiban Gambar (Pillow)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># ...Lanjutan di dalam Fungsi buat_kartu_kue... (Taruh DI ATAS lbl_nama)</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># 1. Cari file fotonya dengan os.path</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;folder = os.path.dirname(__file__)<br>
&nbsp;&nbsp;&nbsp;&nbsp;path_foto = os.path.join(folder, nama_gambar)<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># 2. Buka dgn Pillow, lalu rubah jadi CTkImage</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;foto_mentah = Image.open(path_foto)<br>
&nbsp;&nbsp;&nbsp;&nbsp;foto_ctk = ctk.CTkImage(foto_mentah, size=(<span class="text-purple-400">350</span>, <span class="text-purple-400">200</span>))<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># 3. Tempel di CTkLabel! (text harus dikosongkan)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_foto = ctk.CTkLabel(card, text=<span class="text-green-300">""</span>, image=foto_ctk)<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_foto.pack(pady=<span class="text-purple-400">10</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">5️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Memasang Gambar!</h3>
                        <p class="text-slate-600 text-lg">Inilah rahasianya: <b>os.path</b> &rarr; <b>Image.open()</b> &rarr; <b>CTkImage()</b>.</p>
                        <p class="text-slate-600 text-lg">Gambar "ditempelkan" ke dalam sebuah Label biasa menggunakan parameter <code>image=</code>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Cake Bliss 🍰 (Step 6)",
            "subtitle": "The Magic of Reusability",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">6️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Panggil Fungsinya!</h3>
                        <p class="text-slate-600 text-lg">Di luar blok fungsi (di bagian paling bawah kodemu, tepat sebelum <code>app.mainloop()</code>), cukup panggil fungsi tersebut berkali-kali dengan data berbeda!</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700">
<span class="text-emerald-400"># Panggil fungsinya untuk mencetak kue!</span><br>
buat_kartu_kue(<span class="text-green-300">"Coklat Lava"</span>, <span class="text-green-300">"Lelehan coklat hangat manis"</span>, <span class="text-green-300">"coklat.png"</span>)<br><br>
buat_kartu_kue(<span class="text-green-300">"Strawberry Dream"</span>, <span class="text-green-300">"Krim strawberry segar..."</span>, <span class="text-green-300">"straw.png"</span>)<br><br>
buat_kartu_kue(<span class="text-green-300">"Lemon Cheese"</span>, <span class="text-green-300">"Asam manis lumer"</span>, <span class="text-green-300">"lemon.png"</span>)<br><br>
<span class="text-emerald-400"># (Ingat: Pastikan file coklat.png dll ada di folder!)</span><br>
app.mainloop()
                    </div>
                </div>
            \`
        },
        {
            "title": "Demo Final Cake Bliss 🧁",
            "subtitle": "Katalog Interaktif",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-600">
                        <div class="mock-window-header bg-[#FFF5F5] border-[#FFD1DC]">
                            <div class="mock-window-title text-[#FF85A1] font-bold">Cake Bliss</div>
                        </div>
                        <div class="mock-window-content bg-[#FFF5F5] h-96 flex flex-col items-center justify-start p-4 overflow-y-auto space-y-4">
                            <h2 class="text-2xl font-bold text-[#FF85A1]">CAKE BLISS 🍰</h2>
                            
                            <!-- Mock Card 1 -->
                            <div class="bg-white w-full rounded-2xl p-3 shadow-md border border-pink-100 flex flex-col items-center text-center">
                                <div class="w-full h-32 bg-slate-200 rounded-lg flex items-center justify-center text-5xl mb-2">🍫</div>
                                <h3 class="font-bold text-slate-800 text-lg">Coklat Lava</h3>
                                <p class="text-xs text-slate-500 mt-1">Lelehan coklat hangat manis berpadu dengan taburan gula halus.</p>
                            </div>
                            
                            <!-- Mock Card 2 -->
                            <div class="bg-white w-full rounded-2xl p-3 shadow-md border border-pink-100 flex flex-col items-center text-center">
                                <div class="w-full h-32 bg-slate-200 rounded-lg flex items-center justify-center text-5xl mb-2">🍓</div>
                                <h3 class="font-bold text-slate-800 text-lg">Strawberry Dream</h3>
                                <p class="text-xs text-slate-500 mt-1">Krim tebal dengan buah strawberry organik pilihan dari kebun.</p>
                            </div>
                        </div>
                    </div>
                    <p class="text-slate-500 italic mt-4 text-sm">Berkat ScrollableFrame, kamu bisa scroll tak terbatas jika kue ditambahkan lagi!</p>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Border Warna-Warni 🌈",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyesuaikan Warna Border</h3>
                        <p class="text-slate-600 text-lg">Akan sangat keren jika kartu Strawberry punya border pink, dan kartu Lemon punya border kuning.</p>
                    </div>
                    <div class="bg-purple-50 p-6 rounded-xl border border-purple-200">
                        <h4 class="font-bold text-purple-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Ubah definisi fungsi: <br><code>def buat_kartu_kue(judul, resep, nama_gambar, <span class="font-bold text-purple-600">warna_border</span>):</code></li>
                            <li>Pada <code>CTkFrame</code>, set <code>border_color=warna_border, border_width=2</code>.</li>
                            <li>Saat memanggil fungsi, masukkan warna: <br><code>buat_kartu_kue(..., "yellow")</code></li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Tambah Koleksi 🍰",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200">
                        <h4 class="font-bold text-orange-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Cari 2 gambar kue/makanan favoritmu dari internet, simpan jadi PNG/JPG.</li>
                            <li>Taruh file di folder yang sama.</li>
                            <li>Panggil <code>buat_kartu_kue</code> 2x lagi dengan data barumu.</li>
                            <li>Buktikan bahwa fungsi <i>helper</i> ini benar-benar membuat hidup jadi gampang!</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menu Baru!</h3>
                        <p class="text-slate-600 text-lg">Sekarang toko ini baru punya 3 kue. Mari kita jadikan minimal 5 Kue!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Sub-Header Dinamis 📝",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Penghitung Resep</h3>
                        <p class="text-slate-600 text-lg">Bikin Label baru di bawah Judul "CAKE BLISS". Label itu bertuliskan: <br><b>"Ada 5 kue lezat menantimu hari ini!"</b></p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl text-green-300">
<span class="text-emerald-400"># Clue:</span><br>
Bikin variabel `jumlah_kue = 5`.<br>
Masukkan variabel itu pakai <b>f-string</b> ke dalam teks CTkLabel baru yang di-pack tepat di bawah judul.<br><br>
<span class="text-emerald-400">Coba ubah angkanya kalau kamu menambah kue baru!</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Project: Galeri Wisata ✈️",
            "subtitle": "Latihan Ekstra",
            "content": \`
                <div class="max-w-5xl mx-auto text-center space-y-5">
                    <div class="text-6xl mb-2">🏝️</div>
                    <h3 class="text-3xl font-bold text-slate-800">Galeri Destinasi Wisata Indonesia</h3>
                    <p class="text-slate-600 text-lg max-w-2xl mx-auto">Coba ubah total aplikasi ini. Bukan lagi jualan kue, tapi "Travel App"!</p>
                    <ul class="list-disc pl-5 text-slate-700 max-w-lg mx-auto text-left space-y-2">
                        <li>Set <code>appearance_mode</code> ke "dark".</li>
                        <li>Ganti gambar dengan foto Danau Toba, Bali, Raja Ampat, dll.</li>
                        <li>Ubah fungsi helpernya jadi <code>buat_kartu_wisata(lokasi, provinsi, gambar)</code>.</li>
                        <li>Rasakan betapa mudahnya mendesain ulang aplikasi karena kamu sudah pakai fungsi Helper!</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Info Tambahan: Hak Cipta Gambar 🌐",
            "subtitle": "Digital Literacy",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-blue-50 p-6 rounded-xl border border-blue-200">
                        <h4 class="font-bold text-blue-800 mb-3 text-xl">Tahukah Kamu?</h4>
                        <p class="text-slate-700">Gambar di Google tidak semuanya boleh dipakai! Sebagian besar dilindungi <b>Hak Cipta (Copyright)</b>. Menggunakan gambar orang lain untuk aplikasimu bisa dituntut secara hukum (didenda jutaan rupiah).</p>
                    </div>
                    <div class="text-left space-y-4">
                        <p class="text-slate-600 text-lg">Solusinya? Carilah gambar berlisensi <b>CC0</b> (<i>Creative Commons Zero</i> / Bebas Hak Cipta).</p>
                        <p class="text-slate-600 text-lg">Situs seperti <span class="font-bold">Unsplash</span>, <span class="font-bold">Pexels</span>, dan <span class="font-bold">Pixabay</span> menyediakan jutaan gambar indah yang 100% legal dan gratis untuk digunakan di kodemu!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Summary 📝",
            "subtitle": "Ringkasan Pembelajaran",
            "content": \`
                <div class="grid md:grid-cols-2 gap-6 max-w-5xl mx-auto">
                    <div class="bg-orange-50 border border-orange-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-orange-700 mb-3 text-xl">Mengelola Gambar</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-orange-600">Pillow (PIL):</span> Library pengolah gambar (seperti kacamata bagi Python).</li>
                            <li><span class="font-bold text-orange-600">os.path:</span> Agar Python tidak buta lokasi file, wajib pakai os.path.dirname(__file__).</li>
                            <li><span class="font-bold text-orange-600">CTkImage:</span> Jembatan antara gambar PIL agar bisa dipajang di GUI.</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 border border-blue-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-blue-700 mb-3 text-xl">Abstraction & Scroll</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-blue-600">Fungsi Helper:</span> Komponen Reusable yang membungkus kode UI agar tidak diketik ulang. Pemanggilan berulang jadi super rapi.</li>
                            <li><span class="font-bold text-blue-600">CTkScrollableFrame:</span> Layar ajaib yang bisa digulung saat isi (kartu) sangat banyak.</li>
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
                        Simplicity is about subtracting the obvious and adding the meaningful. Good code is like a good design—don't repeat yourself.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— John Maeda (Designer & Engineer)</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "7": \[\s*\{.*?\}\s*\],\s*"8": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_7.replace("\\\\`", "`") + '\\n    ],\\n    "8": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 7 successfully.")
