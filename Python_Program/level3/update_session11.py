import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

new_session_11 = """    "11": [
        {
            "title": "Meeting 11: Archius Live Weather 🌦️ (Part 2)",
            "subtitle": "Membangun Otak Aplikasi (Back-end & API)",
            "content": `<div class="text-center max-w-4xl mx-auto">
                <div class="text-6xl mb-5">🧠</div>
                <p class="text-2xl font-bold text-slate-800 mb-3">Back-End Developer Mode!</p>
                <p class="text-lg text-slate-600">Sesi lalu kita sudah membuat tampilan visual yang sangat cantik. Tapi sayangnya, suhunya selamanya menunjuk pada "--°C". Hari ini, kita akan menyihir aplikasi itu menjadi hidup dengan mengambil data cuaca asli dari internet secara Real-Time!</p>
                <div class="mt-8 grid sm:grid-cols-2 gap-3 text-sm font-bold">
                    <div class="rounded-xl bg-orange-50 border border-orange-100 p-4 text-orange-700">API (Internet)</div>
                    <div class="rounded-xl bg-yellow-50 border border-yellow-100 p-4 text-yellow-700">JSON Data Parsing</div>
                </div>
            </div>`
        },
        {
            "title": "Flashback Sesi 10 ⏪",
            "subtitle": "Review Front-End",
            "content": `<div class="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto text-center">
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🌌</div><h4 class="font-bold text-slate-800">app.configure</h4><p class="text-sm text-slate-500 mt-2">Mewarnai latar belakang (Background) aplikasi secara menyeluruh</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">✒️</div><h4 class="font-bold text-slate-800">Styling Entry</h4><p class="text-sm text-slate-500 mt-2">Mengganti warna kotak, border, dan huruf pada input</p></div>
                <div class="rounded-xl bg-white border border-slate-200 p-6 shadow-sm"><div class="text-5xl mb-4">🔀</div><h4 class="font-bold text-slate-800">Mixed Layout</h4><p class="text-sm text-slate-500 mt-2">Mencampur .pack() & .grid() dengan aman lewat Frame terpisah</p></div>
            </div>`
        },
        {
            "title": "Mini Quiz: Flashback 🧠",
            "subtitle": "Pemanasan",
            "content": \`
                <div class="max-w-2xl mx-auto text-center space-y-5">
                    <div class="text-5xl">🧐</div>
                    <p class="font-semibold text-slate-700 text-xl">Di CustomTkinter, bagaimana cara termudah mengganti warna <i>border</i> (garis batas pinggir) dari sebuah kotak ketik (<code>CTkEntry</code>)?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb1-fb11', 'Salah! fg_color mengubah warna isi kotaknya (foreground), bukan border.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">A. Mengisi parameter fg_color="red".</button>
                        <button onclick="showMiniFeedback('fb1-fb11', 'Salah! Parameter color saja tidak akan dikenali oleh CTkEntry.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. Mengisi parameter color="red".</button>
                        <button onclick="showMiniFeedback('fb1-fb11', 'Tepat! Parameter border_color secara spesifik akan mengubah warna garis yang mengelilingi kotak.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">C. Mengisi parameter border_color="red".</button>
                    </div>
                    <div id="fb1-fb11" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Objectives 🎯",
            "subtitle": "Target Kita Hari Ini",
            "content": \`
                <div class="max-w-4xl mx-auto">
                    <ul class="custom-list list-disc text-xl text-slate-700 space-y-4 text-left">
                        <li>Memahami konsep <b>API (Application Programming Interface)</b> sebagai jembatan komunikasi data antar aplikasi.</li>
                        <li>Menggunakan <i>library</i> <code>requests</code> untuk meminta (GET) data dari internet.</li>
                        <li>Membedah dan menerjemahkan data mentah berbentuk <b>JSON</b> menjadi <i>Dictionary Python</i>.</li>
                        <li>Menyelamatkan aplikasi dari *Crash* pakai blok <code>try-except</code> ketika internet mati.</li>
                    </ul>
                </div>
            \`
        },
        {
            "title": "Materi 1: Berkenalan dengan API 🍽️",
            "subtitle": "Pelayan Restoran Digital",
            "content": \`
                <div class="grid md:grid-cols-2 gap-8 items-center max-w-5xl mx-auto">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Analogi Restoran</h3>
                        <p class="text-slate-600 text-lg">Bagaimana cara kita (Aplikasi) tahu cuaca di London hari ini tanpa pergi ke sana?</p>
                        <p class="text-slate-600 text-lg">Kita "memesan" datanya ke <b>API</b> (Application Programming Interface). API bekerja persis seperti <b>Pelayan Restoran</b>:</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li><span class="font-bold">Kamu (Aplikasi):</span> Pelanggan yang memesan menu.</li>
                            <li><span class="font-bold text-orange-500">API (Pelayan):</span> Tukang antar pesanan ke dapur (Server).</li>
                            <li><span class="font-bold">Dapur (Server BMKG):</span> Pemasak data yang membalas dengan makanan (Data Cuaca).</li>
                        </ul>
                    </div>
                    <div class="bg-orange-50 p-6 rounded-xl border border-orange-200 text-center shadow-inner">
                        <img src="https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg" class="mx-auto rounded-lg h-48 object-contain">
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 2: Library Requests 🌐",
            "subtitle": "Kurir Pribadi Python",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300 text-sm">
import requests<br><br>
<span class="text-emerald-400"># URL = Alamat Server BMKG/Cuaca</span><br>
url = <span class="text-green-300">"http://api.weather.com..."</span><br><br>
<span class="text-emerald-400"># Minta (GET) data dari alamat itu</span><br>
balasan = requests.get(url)
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Paket Ekspedisi Datamu</h3>
                        <p class="text-slate-600 text-lg">Untuk memanggil pelayan (API), Python butuh kendaraan. Kendaraannya bernama <code>requests</code>.</p>
                        <p class="text-slate-600 text-lg">Perintah <code>requests.get(url)</code> artinya kita mengetuk pintu (HTTP GET) alamat web tersebut dan menunggu balasan dari <i>server</i> mereka.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 3: Bedah URL & API Key 🔑",
            "subtitle": "Surat Rahasia",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Alamat Terenkripsi</h3>
                        <p class="text-slate-600 text-lg">Server cuaca tidak akan melayani sembarang orang. Kita butuh <b>API Key</b> (Karcis izin khusus).</p>
                        <p class="text-slate-600 text-lg text-blue-600 font-bold">Query Parameters (?):</p>
                        <ul class="list-disc pl-5 text-slate-600 space-y-1">
                            <li><code>q={kota}</code> = Tolong carikan data untuk Kota ini.</li>
                            <li><code>appid={kunci}</code> = Ini karcis izinku.</li>
                            <li><code>units=metric</code> = Tolong hitung pakai Celcius (Bukan Fahrenheit).</li>
                        </ul>
                    </div>
                    <div class="bg-blue-50 p-5 rounded-xl font-mono text-xs text-left shadow-md border border-blue-200 text-blue-900">
kota = <span class="text-blue-700">"Jakarta"</span><br>
kunci = <span class="text-blue-700">"RAHASIA_123"</span><br><br>
<span class="text-gray-500"># Format String (f) sangat penting di sini!</span><br>
url = f<span class="text-blue-700">"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={kunci}&units=metric"</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 4: JSON, Sang Dictionary 📜",
            "subtitle": "JavaScript Object Notation",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-xs text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Ini bentuk data JSON dari Internet:</span><br>
{<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"weather"</span>: [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<span class="text-green-300">"main"</span>: <span class="text-green-300">"Rain"</span>, <span class="text-green-300">"description"</span>: <span class="text-green-300">"light rain"</span>}<br>
&nbsp;&nbsp;&nbsp;&nbsp;],<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"main"</span>: {<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"temp"</span>: <span class="text-purple-400">29.5</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-green-300">"humidity"</span>: <span class="text-purple-400">80</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;}<br>
}<br><br>
<span class="text-emerald-400"># Cara ambil suhunya:</span><br>
data_mentah = response.json()<br>
suhu = data_mentah[<span class="text-green-300">"main"</span>][<span class="text-green-300">"temp"</span>]
                    </div>
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kotak di dalam Kotak</h3>
                        <p class="text-slate-600 text-lg">Server akan membalas pakai bahasa <b>JSON</b>. JSON itu ibarat <i>Dictionary Python</i> raksasa (Kotak di dalam Kotak).</p>
                        <p class="text-slate-600 text-lg">Untuk mengambil data suhu, kita panggil <code>response.json()</code>, lalu buka kamusnya perlahan: <i>"Buka laci main, ambil temp"</i>.</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Materi 5: Iterasi Kamus 📖",
            "subtitle": "Metode .items()",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Bedah Dictionary!</h3>
                        <p class="text-slate-600 text-lg">Gimana cara mengecek isi kamus <code>ICON_MAP</code> yang kita buat di Sesi 10 kemarin?</p>
                        <p class="text-slate-600 text-lg">Gunakan <code>.items()</code> pada <i>for-loop</i>. Fitur ini akan memecah kamus menjadi dua bagian sekaligus: Kata Kunci (<code>key</code>) dan Nilainya (<code>value/filename</code>).</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-left shadow-xl text-green-300 text-sm border border-slate-700">
<span class="text-emerald-400"># ICON_MAP = {"rain": "hujan.png"}</span><br><br>
for kunci, nama_file in ICON_MAP.items():<br>
&nbsp;&nbsp;&nbsp;&nbsp;if kunci in kondisi_cuaca:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pakai_gambar = nama_file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">break</span>
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
                    <p class="font-semibold text-slate-700 text-xl">Jika server membalas data seperti ini: <code>{"wind": {"speed": 5, "deg": 180}}</code>, bagaimana cara Python mengambil angka <b>5</b> dari dalam dictionary bernama `data`?</p>
                    <div class="grid grid-cols-1 gap-3">
                        <button onclick="showMiniFeedback('fb2-fb11', 'Tepat! Susunannya harus masuk ke laci wind dulu, baru buka kotak speed.', 'success')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-green-300 transition-all text-left">A. data["wind"]["speed"]</button>
                        <button onclick="showMiniFeedback('fb2-fb11', 'Salah! Kalau kamu ambil data[speed], programnya error karena speed ada di dalam laci wind.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">B. data["speed"]</button>
                        <button onclick="showMiniFeedback('fb2-fb11', 'Salah! Terbalik. Python membacanya dari luar ke dalam.', 'warn')" class="px-4 py-3 bg-white border border-slate-200 rounded-xl hover:border-blue-300 transition-all text-left">C. data["speed"]["wind"]</button>
                    </div>
                    <div id="fb2-fb11" class="min-h-[48px] mt-4"></div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 1)",
            "subtitle": "Instalasi Kurir Pribadi",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-sm text-left shadow-xl border border-slate-700 text-gray-300">
<span class="text-green-500 font-bold">Yazids-MacBook-Pro:</span>WeatherApp yazid$ <br>
> pip install requests<br><br>
<span class="text-gray-400">Collecting requests<br>
Successfully installed requests-2.31.0</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">1️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Siapkan Komunikasi Web</h3>
                        <p class="text-slate-600 text-lg">Buka <b>Terminal</b> di VS Code (<code>Ctrl</code> + <code>`</code>).</p>
                        <p class="text-slate-600 text-lg">Ketik <code>pip install requests</code>. Setelah beres, tambahkan <code>import requests</code> di baris paling atas kodingan Sesi 10 kemarin!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 2)",
            "subtitle": "Kunci Rahasia API",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">2️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Dapatkan Kartu Akses!</h3>
                        <p class="text-slate-600 text-lg">Daftar akun gratis di <a href="https://openweathermap.org/" target="_blank" class="text-blue-500 font-bold underline">OpenWeatherMap.org</a>.</p>
                        <p class="text-slate-600 text-lg">Klik profilmu, pilih <b>My API Keys</b>, lalu copy kode unik (kombinasi huruf & angka acak panjang) milikmu.</p>
                    </div>
                    <div class="bg-indigo-50 p-5 rounded-xl text-left shadow-md border border-indigo-200">
                        <img src="https://uob-1328237036.cos.ap-singapore.myqcloud.com//file-uploader/images/97fd428a-526b-4a2c-b3c9-c4750ea9a468.png" class="mx-auto rounded-lg object-cover w-full h-40">
                        <p class="text-xs text-indigo-700 mt-2 font-bold text-center">Jangan bocorkan kuncimu ke publik (misal: TikTok/GitHub)!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 3)",
            "subtitle": "Fungsi Tukang Ganti Gambar",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[11px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto">
<span class="text-emerald-400"># Buat fungsi ini sebelum fungsi pencarian utama!</span><br>
def update_icon(kondisi):<br>
&nbsp;&nbsp;&nbsp;&nbsp;kondisi = kondisi.lower() <span class="text-blue-400"># Ubah huruf kecil semua</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;file_gambar = <span class="text-green-300">"sunny.png"</span> <span class="text-blue-400"># Nilai awal cadangan</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Cek kamus ICON_MAP dari Sesi 10</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">for</span> kunci, nama_file <span class="text-orange-400 font-bold">in</span> ICON_MAP.items():<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">if</span> kunci <span class="text-orange-400 font-bold">in</span> kondisi:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_gambar = nama_file<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">break</span> <span class="text-blue-400"># Stop nyari jika udah ketemu!</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Ganti gambar pada Label!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lokasi = os.path.join(os.path.dirname(__file__), file_gambar)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gambar_baru = ctk.CTkImage(Image.open(lokasi), size=(<span class="text-purple-400">220</span>, <span class="text-purple-400">220</span>))<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_icon.configure(image=gambar_baru)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">except</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-blue-400">print("Gambar hilang bos!")</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">3️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Pencocokan Gambar</h3>
                        <p class="text-slate-600 text-lg">Fungsi <code>update_icon</code> akan menerima kata kunci kondisi (contoh: "Rain"). Lalu ia akan mengecek di <code>ICON_MAP</code>, oh ternyata harus me-<i>load</i> <code>rain.png</code>!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 4)",
            "subtitle": "Menarik Data (fetch_weather)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">4️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Mengetuk Pintu BMKG Internasional</h3>
                        <p class="text-slate-600 text-lg">Ini <b>Jantung Utama</b> aplikasinya! Bikin fungsi <code>fetch_weather()</code>. Ambil tulisan dari kotak Entry, satukan dalam URL (<code>f-string</code>), lalu kirim pakai <code>requests.get()</code>.</p>
                    </div>
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto text-green-300">
def fetch_weather():<br>
&nbsp;&nbsp;&nbsp;&nbsp;kota = entry_search.get()<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># TARUH KUNCI RAHASIAMU DISINI!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;api_key = <span class="text-green-300">"c6e3b..."</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;url = f<span class="text-green-300">"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={api_key}&units=metric"</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">try</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Panggil Server (Internet)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;response = requests.get(url)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data = response.json() <span class="text-emerald-400"># Ubah ke Dictionary</span><br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Lanjut ke Step 5 (Membedah isi json)</span>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 5)",
            "subtitle": "Membedah Kamus JSON (Parsing)",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-slate-900 p-5 rounded-xl font-mono text-[10px] text-left shadow-xl border border-slate-700 h-64 overflow-y-auto text-green-300">
<span class="text-emerald-400"># (Lanjutan di dalam try fungsi fetch_weather)</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">if</span> data[<span class="text-green-300">"cod"</span>] == <span class="text-purple-400">200</span>: <span class="text-blue-400"># 200 = Sukses Nemu Kota</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main_cuaca = data[<span class="text-green-300">"weather"</span>][<span class="text-purple-400">0</span>][<span class="text-green-300">"main"</span>]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;suhu = data[<span class="text-green-300">"main"</span>][<span class="text-green-300">"temp"</span>]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;deskripsi = data[<span class="text-green-300">"weather"</span>][<span class="text-purple-400">0</span>][<span class="text-green-300">"description"</span>]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lembap = data[<span class="text-green-300">"main"</span>][<span class="text-green-300">"humidity"</span>]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;angin = data[<span class="text-green-300">"wind"</span>][<span class="text-green-300">"speed"</span>]<br><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-emerald-400"># Timpa isi layar visual!</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_city.configure(text=data[<span class="text-green-300">"name"</span>].upper())<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_temp.configure(text=f<span class="text-green-300">"{round(suhu)}°C"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_desc.configure(text=deskripsi.upper())<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_hum_val.configure(text=f<span class="text-green-300">"{lembap}%"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_wind_val.configure(text=f<span class="text-green-300">"{angin} m/s"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_icon(main_cuaca)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_city.configure(text=<span class="text-green-300">"CITY NOT FOUND"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-orange-400 font-bold">except</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lbl_city.configure(text=<span class="text-green-300">"NO INTERNET"</span>)
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">5️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menyuntikkan Nyawa!</h3>
                        <p class="text-slate-600 text-lg">Jika <code>data["cod"] == 200</code> (Sukses), kita "rampok" semua data JSON-nya (suhu, kelembapan), lalu panggil perintah <code>.configure()</code> untuk mengubah semua Label "dummy/palsu" yang kita buat minggu lalu menjadi angka ASLI!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Project: Weather App 🌦️ (Step 6)",
            "subtitle": "Konektor Akhir",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">6️⃣</div>
                        <h3 class="text-2xl font-bold text-slate-800">Menghidupkan Tombol SEARCH</h3>
                        <p class="text-slate-600 text-lg">Scroll jauh ke atas, cari tempat kamu membuat tombol SEARCH (di Sesi 10).</p>
                        <p class="text-slate-600 text-lg text-blue-600 font-bold">Tambahkan <code>command=fetch_weather</code> pada saat kamu mencetak <code>CTkButton</code>.</p>
                    </div>
                    <div class="bg-blue-50 p-5 rounded-xl font-mono text-sm text-left shadow-md border border-blue-200 text-blue-900">
btn_search = ctk.CTkButton(<br>
&nbsp;&nbsp;&nbsp;&nbsp;search_frame,<br>
&nbsp;&nbsp;&nbsp;&nbsp;text=<span class="text-blue-700">"SEARCH"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;height=<span class="text-purple-700">45</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;fg_color=<span class="text-blue-700">"#3b82f6"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span class="text-red-500 font-bold">command=fetch_weather</span><br>
)<br>
btn_search.pack(side=<span class="text-blue-700">"right"</span>)
                    </div>
                </div>
            \`
        },
        {
            "title": "Jalankan Sekarang! 🚀",
            "subtitle": "Testing Archius Weather",
            "content": \`
                <div class="max-w-4xl mx-auto text-center space-y-6">
                    <div class="mock-window w-full max-w-sm mx-auto shadow-2xl border-slate-700 rounded-2xl overflow-hidden bg-[#1e3a8a]">
                        <div class="p-6 h-[500px] flex flex-col justify-between items-center text-white space-y-4">
                            <!-- Search -->
                            <div class="flex w-full gap-2 mt-4">
                                <div class="bg-[#1e40af] border border-[#3b82f6] flex-grow rounded-lg p-2 text-white text-sm text-left">London</div>
                                <div class="bg-[#3b82f6] rounded-lg px-3 py-2 font-bold text-sm shadow-md cursor-pointer hover:bg-blue-400">SEARCH</div>
                            </div>
                            
                            <!-- Main Display -->
                            <div class="flex flex-col items-center mt-2">
                                <h3 class="font-bold text-lg tracking-widest text-yellow-300">LONDON</h3>
                                <div class="text-[100px] my-2">🌧️</div>
                                <h1 class="font-bold text-6xl">9°C</h1>
                                <p class="text-[#bfdbfe] italic mt-2 text-sm">LIGHT RAIN</p>
                            </div>
                            
                            <!-- Stats Grid -->
                            <div class="bg-[#1e40af] border border-[#3b82f6] rounded-2xl w-full p-4 flex justify-around mt-4 shadow-xl">
                                <div class="text-center">
                                    <p class="text-[9px] text-[#93c5fd] font-bold">HUMIDITY</p>
                                    <p class="text-xl font-bold text-white">82%</p>
                                </div>
                                <div class="text-center">
                                    <p class="text-[9px] text-[#93c5fd] font-bold">WIND SPEED</p>
                                    <p class="text-xl font-bold text-white">4.1 m/s</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <p class="text-slate-600 font-bold animate-pulse">Coba cari kota: Tokyo, Jakarta, New York!</p>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 1: Validasi Input Kosong 🚫",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-red-50 p-6 rounded-xl border border-red-200">
                        <h4 class="font-bold text-red-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li>Di dalam awal fungsi <code>fetch_weather()</code>, cek apakah variabel <code>kota</code> bernilai kosong (<code>""</code>).</li>
                            <li>Jika ya, jangan panggil requests (hemat kuota API), langsung ubah <code>lbl_city</code> jadi "PLEASE ENTER CITY".</li>
                            <li>Jika tidak kosong, baru lakukan <code>requests.get()</code>.</li>
                        </ul>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Cegah Pemborosan API</h3>
                        <p class="text-slate-600 text-lg">Jika <i>user</i> lupa mengetik nama kota dan langsung klik SEARCH, aplikasi akan mengirim API Kosong, dan sistem BMKG bisa marah (API Key-mu kena ban). Cegah ini!</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 2: Fitur \"Feels Like\" 🌡️",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Suhu Asli vs Terasa</h3>
                        <p class="text-slate-600 text-lg">Terkadang suhu 30 derajat terasa seperti 35 derajat karena panas terik. API menyediakan data itu di <code>data["main"]["feels_like"]</code>.</p>
                    </div>
                    <div class="bg-indigo-50 p-6 rounded-xl border border-indigo-200">
                        <h4 class="font-bold text-indigo-800 mb-3">Tugas Khusus:</h4>
                        <ul class="list-disc pl-5 text-slate-700">
                            <li>Buat <code>CTkLabel</code> baru di bawah label Suhu Raksasa (di Sesi 10).</li>
                            <li>Di dalam fungsi <code>fetch_weather()</code>, "sedot" datanya: <code>rasa = data["main"]["feels_like"]</code>.</li>
                            <li>Tampilkan pada label tersebut dengan format: <i>"Feels like: 35°C"</i>.</li>
                        </ul>
                    </div>
                </div>
            \`
        },
        {
            "title": "Pro Challenge 3: Termometer Cerdas 🌡️🎨",
            "subtitle": "Tantangan Level 3",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="bg-orange-50 p-6 rounded-xl font-mono text-sm text-left shadow-xl text-orange-900 border border-orange-200">
<span class="text-orange-600 font-bold"># Logika If/Else:</span><br>
if suhu < 20:<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_temp.configure(text_color="#3b82f6") <span class="text-blue-500"># Biru</span><br>
elif suhu > 30:<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_temp.configure(text_color="#f97316") <span class="text-orange-500"># Oranye Panas</span><br>
else:<br>
&nbsp;&nbsp;&nbsp;&nbsp;lbl_temp.configure(text_color="white") <span class="text-gray-500"># Normal</span>
                    </div>
                    <div class="text-left space-y-4">
                        <div class="text-5xl mb-2">🔥</div>
                        <h3 class="text-2xl font-bold text-slate-800">Warna Suhu Dinamis</h3>
                        <p class="text-slate-600 text-lg">Buat aplikasi ini lebih estetik! Tulisan suhu Raksasa (90 font) akan otomatis berubah warna: Biru kalau dingin, Putih kalau biasa saja, Oranye/Merah kalau suhu terlalu panas (> 30C).</p>
                    </div>
                </div>
            \`
        },
        {
            "title": "Bonus Info: Bahaya Bocornya API Key ⚠️",
            "subtitle": "Literasi Keamanan Cyber",
            "content": \`
                <div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
                    <div class="text-left space-y-4">
                        <h3 class="text-2xl font-bold text-slate-800">Kenapa Disembunyikan?</h3>
                        <p class="text-slate-600 text-lg">Di dunia nyata (Proyek GitHub), kamu tidak boleh menulis <code>api_key = "KODE"</code> langsung di dalam file Python (Hardcoding).</p>
                        <p class="text-slate-600 text-lg">Hacker memakai *Bot* 24 jam untuk men-*scan* GitHub mencari API Key yang bocor, lalu memakainya untuk mencuri layanan berbayarmu (Tagihan kartu kreditmu bisa bengkak!). Gunakan file <code>.env</code> untuk mengamankannya.</p>
                    </div>
                    <div class="bg-red-50 p-6 rounded-xl font-mono text-sm text-left shadow-xl border border-red-200 text-red-700">
<span class="text-red-500 font-bold">Kasus Nyata:</span><br>
Seorang programmer lupa menghapus API Key Amazon Web Service di GitHub. Keesokan harinya dia ditagih <br><b>$60,000 (Rp 900 Juta)</b> karena Hackernya menyedot <i>database server</i> berbayar.
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
                        <h4 class="font-bold text-orange-700 mb-3 text-xl">Komunikasi Web</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-orange-600">API:</span> Jembatan ajaib (Pelayan) yang menghubungkan Python-mu dengan Super Komputer di internet (Server).</li>
                            <li><span class="font-bold text-orange-600">Requests:</span> Kendaraan yang digunakan untuk metode pengiriman surat (HTTP GET).</li>
                        </ul>
                    </div>
                    <div class="bg-yellow-50 border border-yellow-200 p-6 rounded-xl shadow-sm text-left">
                        <h4 class="font-bold text-yellow-700 mb-3 text-xl">Pengolahan Data (Parsing)</h4>
                        <ul class="list-disc pl-5 text-slate-700 space-y-2">
                            <li><span class="font-bold text-yellow-600">JSON:</span> Data mentah balasan API (Formatnya mirip banget sama Python Dictionary).</li>
                            <li><span class="font-bold text-yellow-600">Error Handling:</span> Penggunaan <code>try-except</code> super penting agar kalau internetnya *down* (mati), layar hanya berubah tulisan, bukan Aplikasinya tiba-tiba ketutup (Crash).</li>
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
                    <div class="text-6xl text-orange-500 opacity-50">"</div>
                    <blockquote class="text-3xl font-bold text-slate-800 italic leading-snug">
                        Information is the oil of the 21st century, and analytics is the combustion engine.
                    </blockquote>
                    <p class="text-xl text-slate-600 font-medium">— Peter Sondergaard (Gartner Research)</p>
                </div>
            \`
        }
"""

pattern = re.compile(r'    "11": \[\s*\{.*?\}\s*\],\s*"12": \[', re.DOTALL)
new_content = re.sub(pattern, new_session_11.replace("\\\\`", "`") + '\\n    ],\\n    "12": [', content, count=1)

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated session 11 successfully.")
