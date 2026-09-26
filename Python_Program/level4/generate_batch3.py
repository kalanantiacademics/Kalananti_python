import re

def get_reveal(btn_text, content_html):
    return f'''
    <div class="k-reveal">
        <button class="k-reveal-btn">
            <span>{btn_text}</span>
            <span class="icon">▼</span>
        </button>
        <div class="k-reveal-content">
            {content_html}
        </div>
    </div>
    '''

def get_quiz(question, options, correct_index):
    opts_html = ""
    for i, opt in enumerate(options):
        is_correct = "true" if i == correct_index else "false"
        opts_html += f'<button class="k-quiz-option" data-correct="{is_correct}">{opt}</button>\\n'
    return f'''
    <div class="mb-6">
        <h3 class="text-xl font-bold mb-4">{question}</h3>
        {opts_html}
        <div class="k-quiz-feedback"></div>
    </div>
    '''

def get_code(code_str):
    import html
    return f'<div class="k-code">{html.escape(code_str.strip())}</div>'

def build_slide(meeting, sec_id, sec_label, content_html):
    return f'''
    <div class="raw-slide" data-meeting="{meeting}" data-section-id="{sec_id}" data-section-label="{sec_label}">
        {content_html}
    </div>
    '''

slides = []

# ======================= MEETING 7: Class Interaction =======================
M7 = 7
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 7! 🚀</h2>
    <p class="text-xl mb-4">Hari ini kita akan membuat Objek kita bisa saling ngobrol!</p>
    <p class="text-lg text-muted">Mari kita review Frame Switching.</p>
'''))
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Kenapa kita tidak boleh memanggil <code>ctk.CTk()</code> lebih dari satu kali di kode yang sama?</p>
''' + get_quiz("Pilih jawaban:", ["Karena tampilannya jadi jelek", "Karena bisa crash/hang akibat bentrok sistem jendela", "Karena dilarang oleh Python"], 1)))
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Bagaimana cara memunculkan Pop-up baru yang aman?</p>
''' + get_quiz("Pilih jawaban:", ["Menggunakan ctk.CTkToplevel()", "Menggunakan ctk.CTk()", "Menggunakan ctk.CTkFrame()"], 0)))
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Method apa yang digunakan untuk <b>menyembunyikan</b> frame lama agar kita bisa menampilkan frame baru?</p>
''' + get_quiz("Pilih jawaban:", [".delete()", ".hide()", ".pack_forget()"], 2)))
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Dalam membuat Halaman Custom, kita mewarisi dari Class apa?</p>
''' + get_quiz("Pilih jawaban:", ["ctk.CTkButton", "ctk.CTkFrame", "ctk.CTkWindow"], 1)))
slides.append(build_slide(M7, 'm7-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Untuk memunculkan sebuah Toplevel hanya jika belum muncul, method apa yang kita gunakan untuk mengecek keberadaannya?</p>
''' + get_quiz("Pilih jawaban:", [".winfo_exists()", ".is_open()", ".check()"], 0)))

slides.append(build_slide(M7, 'm7-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menjelaskan bagaimana satu objek dapat memiliki objek lain sebagai atributnya (Composition).</li>
        <li>Mampu menghubungkan <b>Object Data</b> dengan <b>Object GUI</b>.</li>
        <li>Mampu memanipulasi data dari satu class melalui tombol di class lain.</li>
    </ul>
'''))

slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Objek di Dalam Objek?</h2>
    <p class="mb-4 text-lg">Sejauh ini, atribut kita hanyalah Teks (String), Angka (Integer), atau Widget.</p>
    <p class="mb-4 text-lg">Tapi tahukah kamu? Kita bisa memasukkan sebuah <b>Object buatan sendiri</b> ke dalam atribut Object lain!</p>
    <p class="text-lg text-muted">Ini sangat berguna untuk memisahkan antara bagian yang menyimpan Data dan bagian yang mengurus Tampilan Layar (GUI).</p>
'''))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Hubungan Data & GUI</h2>
    <div class="flex gap-6 bg-[#0a1830] p-6 rounded-xl">
        <div class="flex-1 bg-green-900/40 p-4 rounded-xl border border-green-500">
            <h3 class="font-bold text-yellow mb-2">Object 1: AkunUser (Model Data)</h3>
            <p class="text-sm">Menyimpan data "saldo = 50.000"</p>
            <p class="text-sm">Punya kemampuan: tambah_saldo()</p>
        </div>
        <div class="flex items-center text-4xl">↔️</div>
        <div class="flex-1 bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold text-yellow mb-2">Object 2: LayarGUI (View)</h3>
            <p class="text-sm">Menyimpan tombol "Top Up".</p>
            <p class="text-sm">Menyimpan Object 1 sebagai "self.akun" agar tombol bisa memanggil <code>self.akun.tambah_saldo()</code></p>
        </div>
    </div>
'''))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan <b>Mobil (GUI)</b> dan <b>Mesin (Data)</b>.</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Mobil (GUI) memiliki setir dan pedal gas. Dia mengurus interaksi dengan supir.</li>
        <li>Mesin (Data) adalah objek terpisah yang dipasang di dalam mobil.</li>
        <li>Saat supir menginjak gas (GUI diklik), mobil menyuruh mesin bekerja: <code>self.mesin.putar()</code>.</li>
    </ul>
'''))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Objek Menjadi Atribut</h2>
    <p class="mb-4">Mari kita buat Class Data dan panggil dari Class Utama.</p>
''' + get_code('''
class UserData:
    def __init__(self, nama):
        self.nama = nama
        self.skor = 0
    
    def tambah_skor(self):
        self.skor += 10

class GameApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # KUNCI UTAMA: Kita masukkan Object Data ke Atribut GUI!
        self.player_aktif = UserData("Gamer123")
        print("Player siap:", self.player_aktif.nama)
''')))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Berinteraksi Lewat GUI</h2>
    <p class="mb-4">Sekarang GUI kita bisa mengubah data <code>UserData</code> tersebut!</p>
''' + get_code('''
    # Di dalam class GameApp
    def __init__(self):
        super().__init__()
        self.player_aktif = UserData("Gamer123")
        
        self.btn = ctk.CTkButton(self, text="Main", command=self.saat_main)
        self.btn.pack()

    def saat_main(self):
        # 1. Panggil method miliknya Object Data
        self.player_aktif.tambah_skor()
        
        # 2. Gunakan datanya di GUI
        print("Skor sekarang:", self.player_aktif.skor)
''')))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
class Dompet:
    def __init__(self):
        self.uang = 50

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.dompetku = Dompet()
        self.uang += 10
''') + get_quiz("Apa yang terjadi pada kode ini?", [
    "Uang di dompet menjadi 60",
    "Error AttributeError, karena di class App tidak ada atribut self.uang. Harusnya self.dompetku.uang",
    "Aplikasi berjalan normal tapi uang tidak bertambah"
], 1)))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Pisahkan Class yang mengurus data (seperti Hitungan Matematika, Saldo) dari Class GUI. Ini membuat kodemu sangat profesional yang biasa disebut pola <b>Model-View</b>.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan mencampur perhitungan rumit dan penyimpanan ratusan data list di dalam Class GUI (App). Nanti GUI-mu akan lambat dan membingungkan.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M7, 'm7-s3', '3. Class Interaction', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika menemui Error: <code>AttributeError: 'GameApp' object has no attribute 'skor'</code></p>
    <p><b>Solusi:</b> Kamu mencoba mengambil <code>self.skor</code> dari GUI, padahal skor ada di dalam objek datanya. Ganti menjadi <code>self.player_aktif.skor</code>.</p>
'''))

slides.append(build_slide(M7, 'm7-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Bikin Class Data</h2>
    <p class="mb-4">Buat <code>class Inventory:</code>. Punya list kosong <code>self.barang</code>. Punya method <code>tambah(self, item)</code> untuk me-append item ke list.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Inventory:
    def __init__(self):
        self.barang = []
        
    def tambah(self, item):
        self.barang.append(item)
'''))))
slides.append(build_slide(M7, 'm7-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Masukkan ke GUI</h2>
    <p class="mb-4">Buat <code>class App(ctk.CTk):</code>. Di dalam <code>__init__</code>, buat atribut <code>self.tas = Inventory()</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.tas = Inventory()
        
        # Contoh tombol
        self.btn = ctk.CTkButton(self, text="Ambil Pedang", command=self.ambil)
        self.btn.pack()
'''))))
slides.append(build_slide(M7, 'm7-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Menjalankan Interaksi</h2>
    <p class="mb-4">Lengkapi method <code>ambil(self):</code> di GUI agar memanggil method tambah di <code>tas</code>, lalu print isinya!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
    def ambil(self):
        # 1. Mengubah Data
        self.tas.tambah("Pedang Besi")
        
        # 2. Melihat Perubahan
        print("Isi tas sekarang:", self.tas.barang)
'''))))
slides.append(build_slide(M7, 'm7-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class SistemBuku:
    def baca(self):
        print("Membaca...")

class PerpusApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.sistem = SistemBuku

    def mulai(self):
        self.sistem.baca()
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Error! Di <code>__init__</code>, kita menyimpan cetakan class-nya, bukan objeknya: <code>self.sistem = SistemBuku</code>.</p>
<p>Harusnya pakai kurung: <code>self.sistem = SistemBuku()</code> agar objeknya terbentuk!</p>
''')))
slides.append(build_slide(M7, 'm7-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: HP Battery App</h2>
    <p class="mb-4">Buat Class Data <code>Baterai</code> dengan <code>self.persen = 100</code> dan method <code>kurang()</code>.</p>
    <p class="mb-4">Buat GUI <code>PonselApp</code> yang punya tombol "Main Game" dan memanggil method <code>kurang()</code> dari objek baterai.</p>
''' + get_reveal("Hint / Petunjuk", "<p>Instansiasi baterai di ponsel dengan <code>self.batre = Baterai()</code>. Di tombol, lakukan <code>self.batre.kurang()</code> lalu update label!</p>")))

slides.append(build_slide(M7, 'm7-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Akun Bank (Data)</h2>
    <p class="mb-4">Siapkan class <code>AkunBank</code>. Punya saldo, bisa setor(jumlah) dan tarik(jumlah).</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class AkunBank:
    def __init__(self):
        self.saldo = 0
    def setor(self, jumlah):
        self.saldo += jumlah
    def tarik(self, jumlah):
        if self.saldo >= jumlah:
            self.saldo -= jumlah
        else:
            print("Saldo tidak cukup!")
'''))))
slides.append(build_slide(M7, 'm7-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Aplikasi Mesin ATM</h2>
    <p class="mb-4">Hubungkan <code>AkunBank</code> ke GUI <code>ATMApp</code>. Buat entry untuk jumlah uang dan tombol Setor.</p>
''' + get_reveal("Tampilkan Jawaban (Kerangka Utama)", get_code('''
class ATMApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.akun = AkunBank()
        
        self.lbl = ctk.CTkLabel(self, text="Saldo: 0")
        self.lbl.pack()
        
        self.entry_uang = ctk.CTkEntry(self)
        self.entry_uang.pack()
        
        self.btn = ctk.CTkButton(self, text="Setor", command=self.lakukan_setor)
        self.btn.pack()
'''))))
slides.append(build_slide(M7, 'm7-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Menyelesaikan ATM</h2>
    <p class="mb-4">Lengkapi fungsi <code>lakukan_setor()</code>!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
    def lakukan_setor(self):
        # Ambil input dan ubah jadi angka
        nominal = int(self.entry_uang.get())
        
        # Ubah datanya
        self.akun.setor(nominal)
        
        # Perbarui layar
        self.lbl.configure(text=f"Saldo: {self.akun.saldo}")
'''))))
slides.append(build_slide(M7, 'm7-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Sistem Vote Pemilu</h2>
    <p class="mb-4"><b>Misi:</b> Pisahkan Data dan GUI!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Class Data <code>Voting</code> punya atribut suara Kandidat 1 dan Kandidat 2.</li>
        <li>Class GUI punya dua tombol "Vote K1" dan "Vote K2".</li>
        <li>Setiap tombol ditekan, suruh objek Voting mencatat suaranya, lalu perbarui Label di layar!</li>
    </ul>
    <p class="text-muted italic">Uji kodemu di VS Code dan perlihatkan ke instruktur!</p>
'''))

slides.append(build_slide(M7, 'm7-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li><b>Composition</b>: Sebuah Objek bisa memiliki Objek lain di dalamnya (sebagai Atribut).</li>
        <li>Kita harus memisahkan antara Logika Penyimpanan Data dengan Logika Tampilan Layar (GUI).</li>
        <li>GUI akan memanggil method dari Objek Data setiap kali user berinteraksi (misal: klik tombol).</li>
    </ul>
'''))
slides.append(build_slide(M7, 'm7-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Kenapa kita repot-repot memisahkan Class Data dan Class GUI? Kenapa tidak ditaruh di GUI semua saja?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Bayangkan kita ingin membuat Game yang ada di Komputer dan HP. Kalau Data dan GUI dicampur, kita harus menulis ulang seluruh kodenya untuk HP. Kalau dipisah, mesin Datanya bisa kita pakai ulang tanpa ubah sebaris pun!</p>
    </div>
'''))
slides.append(build_slide(M7, 'm7-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Kode kita semakin besar. Kalau 5 Class ditaruh di 1 file <code>.py</code>, kita akan kebingungan mencarinya!</p>
    <p class="text-lg">Besok kita akan belajar <b>Modular Coding</b>. Kita akan memecah file jadi beberapa file <code>.py</code> dan menghubungkannya dengan <code>import</code>!</p>
'''))
slides.append(build_slide(M7, 'm7-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Before software can be reusable it first has to be usable."</p>
        <p class="text-xl">— Ralph Johnson</p>
    </div>
'''))

# ======================= MEETING 8: Modular Coding =======================
M8 = 8
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 8! 🚀</h2>
    <p class="text-xl mb-4">Hari ini kita akan merapikan kode seperti Programmer Senior: Memecah File (Modular)!</p>
    <p class="text-lg text-muted">Mari review interaksi antar class terlebih dahulu!</p>
'''))
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Bolehkah kita memasukkan sebuah Object buatan kita sendiri sebagai nilai atribut (self) di dalam Class GUI?</p>
''' + get_quiz("Pilih jawaban:", ["Boleh", "Tidak boleh, harus string/angka"], 0)))
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Apa keuntungan memisahkan Class Data dan Class GUI?</p>
''' + get_quiz("Pilih jawaban:", ["Kode lebih pendek", "Kode lebih rapi dan bisa dipakai ulang tanpa harus membuat GUI yang sama", "Membuat program lambat"], 1)))
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Bagaimana cara GUI mengambil nilai 'skor' dari objek 'Data' (self.data) yang ada di dalamnya?</p>
''' + get_quiz("Pilih jawaban:", ["self.skor", "self.data.skor", "self.skor.data"], 1)))
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Apakah yang benar untuk membuat objek Data dari class Bank di GUI?</p>
''' + get_quiz("Pilih jawaban:", ["self.uang = Bank", "self.uang = Bank()", "self.uang = ctk.Bank()"], 1)))
slides.append(build_slide(M8, 'm8-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Pola memisahkan penyimpanan data dan urusan tampilan layar sering disebut dengan istilah apa?</p>
''' + get_quiz("Pilih jawaban:", ["Data-Tampil", "Model-View", "Class-Object"], 1)))

slides.append(build_slide(M8, 'm8-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menjelaskan konsep <b>Modularitas</b> dalam penulisan program Python.</li>
        <li>Mampu membuat modul (file `.py` terpisah) untuk menyimpan class tertentu.</li>
        <li>Mampu menggunakan <code>import</code> untuk menghubungkan file `.py` di dalam folder yang sama.</li>
    </ul>
'''))

slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu Modular Coding?</h2>
    <p class="mb-4 text-lg">Sejauh ini, kita menaruh semua Class (Data, Login, Dashboard, Root) di dalam satu file <code>app.py</code>.</p>
    <p class="mb-4 text-lg">Bayangkan aplikasi raksasa seperti Spotify. File kodenya tidak mungkin jutaan baris dalam 1 file! Mereka memecahnya (Modular).</p>
    <p class="text-lg">Setiap file <code>.py</code> disebut <b>Modul</b>.</p>
'''))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Folder Project</h2>
    <div class="flex gap-8 bg-[#0a1830] p-6 rounded-xl">
        <div class="bg-red-900/40 p-4 rounded-xl border border-red-500 w-1/3">
            <h3 class="font-bold text-yellow mb-4 text-center">Spaghetti Code (Lama)</h3>
            <ul class="text-sm space-y-2">
                <li>📄 app.py <span class="text-red-300">(800 baris!)</span></li>
            </ul>
        </div>
        <div class="flex flex-col justify-center text-4xl">➡️</div>
        <div class="bg-green-900/40 p-4 rounded-xl border border-green-500 flex-1">
            <h3 class="font-bold text-yellow mb-4 text-center">Modular (Profesional)</h3>
            <ul class="text-sm space-y-2">
                <li>📂 Folder Proyek</li>
                <li>&nbsp;&nbsp;📄 data.py <span class="text-green-300">(Class Data, 20 baris)</span></li>
                <li>&nbsp;&nbsp;📄 ui.py <span class="text-green-300">(Class GUI, 50 baris)</span></li>
                <li>&nbsp;&nbsp;📄 main.py <span class="text-green-300">(File penjalan, 5 baris)</span></li>
            </ul>
        </div>
    </div>
'''))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan membuat Rakitan PC (Komputer).</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Bukan dicetak jadi 1 balok besi (Susah kalau rusak 1 part).</li>
        <li>Komputer Modular: Ada modul RAM, CPU, VGA yang colok-cabut (Import).</li>
        <li>Jika RAM rusak, kita cukup ganti modul RAM (file <code>data.py</code>), tanpa merusak file lain!</li>
    </ul>
'''))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: File 1 (Modul)</h2>
    <p class="mb-4">Buat file pertama bernama <code>mesin_data.py</code>.</p>
''' + get_code('''
# File: mesin_data.py
class DataGame:
    def __init__(self):
        self.skor = 100
        
    def kurangi(self):
        self.skor -= 5
''') + get_reveal("Penjelasan", "<p>File ini hanya berisi cetakan Class! Tidak ada proses <code>print</code> atau dijalankan di sini. Ini hanya 'gudang part'.</p>")))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: File 2 (Utama)</h2>
    <p class="mb-4">Di file kedua, <code>main.py</code>, kita akan memanggil class yang ada di file <code>mesin_data.py</code>.</p>
''' + get_code('''
# File: main.py
# Format: from nama_file import NamaClass
from mesin_data import DataGame

# Sekarang kita bisa memakainya seperti biasa!
data = DataGame()
data.kurangi()
print("Skor:", data.skor)
''')))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
# File: helper.py
def sapa():
    print("Halo")

# File: main.py
helper.sapa()
''') + get_quiz("Kenapa file main.py ini error NameError 'helper' not defined?", [
    "Karena file helper tidak boleh huruf kecil",
    "Karena belum ada perintah: import helper",
    "Karena fungsi sapa tidak pakai class"
], 1)))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Pastikan semua file <code>.py</code> berada di <b>dalam 1 Folder yang Sama</b>. Jika beda folder, Python tidak akan menemukannya secara otomatis.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan menambahkan akhiran <code>.py</code> saat menulis <code>import</code>. Tulis <code>import helper</code> BUKAN <code>import helper.py</code>!</p>
        </div>
    </div>
'''))
slides.append(build_slide(M8, 'm8-s3', '3. Modular Coding', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika Error: <code>ModuleNotFoundError: No module named 'nama_file'</code></p>
    <p><b>Solusi:</b> Buka File Explorer di VS Code. Pastikan nama file benar (tidak typo) dan letaknya sejajar (1 folder) dengan <code>main.py</code> yang sedang kamu jalankan.</p>
'''))

slides.append(build_slide(M8, 'm8-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Menyiapkan Modul GUI</h2>
    <p class="mb-4">Di VS Code, buat file <code>tampilan.py</code> yang memiliki Class <code>JendelaBaru(ctk.CTkToplevel)</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# File: tampilan.py
import customtkinter as ctk

class JendelaBaru(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("200x200")
        self.lbl = ctk.CTkLabel(self, text="Aku dari file lain!")
        self.lbl.pack()
'''))))
slides.append(build_slide(M8, 'm8-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Menjalankan Main</h2>
    <p class="mb-4">Buat <code>main.py</code>. Import <code>JendelaBaru</code>. Buat class <code>App(ctk.CTk)</code> dan tombol yang memunculkan <code>JendelaBaru</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# File: main.py
import customtkinter as ctk
from tampilan import JendelaBaru  # Import dari file sebelah

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.btn = ctk.CTkButton(self, text="Buka", command=self.buka_jendela)
        self.btn.pack()

    def buka_jendela(self):
        JendelaBaru(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
'''))))
slides.append(build_slide(M8, 'm8-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Menghindari Import Loop</h2>
    <p class="mb-4">Penting! Jika File A meng-import File B, maka File B <b>TIDAK BOLEH</b> meng-import File A balik! (Import Loop / Circular Import). Python akan crash bingung.</p>
''' + get_reveal("Aturan Aman", "<p>Gunakan arsitektur pohon. File 'atas' mengimport dari 'bawah'. Jangan sebaliknya! File <code>main.py</code> mengimport <code>tampilan.py</code>. File <code>tampilan.py</code> tidak boleh mengimport <code>main.py</code>.</p>")))
slides.append(build_slide(M8, 'm8-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
# File: kalkulator.py
class Calc:
    pass

# File: main.py
import Kalkulator
c = Calc()
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Ada dua masalah:</p>
<ol>
    <li>Nama file huruf kecil, import ditulis huruf besar <code>import Kalkulator</code> (Error typo module). Harusnya <code>import kalkulator</code></li>
    <li>Jika <code>import kalkulator</code> dipakai, panggil classnya dengan <code>kalkulator.Calc()</code>. ATAU gunakan cara: <code>from kalkulator import Calc</code></li>
</ol>
''')))
slides.append(build_slide(M8, 'm8-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Import Fungsi Matematika</h2>
    <p class="mb-4">Buat <code>matematika.py</code> dengan fungsi <code>tambah(a,b)</code>. Buat <code>main.py</code>, import fungsi tersebut, dan print <code>tambah(5, 10)</code>.</p>
''' + get_reveal("Hint / Petunjuk", "<p>Pada main.py: <code>from matematika import tambah</code></p>")))

slides.append(build_slide(M8, 'm8-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Arsitektur 3 File (Model)</h2>
    <p class="mb-4">Buat <code>data.py</code>: Class <code>User</code> (username, password).</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# data.py
class User:
    def __init__(self, username, pwd):
        self.username = username
        self.password = pwd
'''))))
slides.append(build_slide(M8, 'm8-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Arsitektur 3 File (View)</h2>
    <p class="mb-4">Buat <code>ui.py</code>: Class <code>LayarLogin(ctk.CTkFrame)</code> yang ada Label dan 2 Entry.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# ui.py
import customtkinter as ctk

class LayarLogin(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        # Bikin widget label dan 2 entry di sini
        self.lbl = ctk.CTkLabel(self, text="Silahkan Login")
        self.lbl.pack()
'''))))
slides.append(build_slide(M8, 'm8-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Arsitektur 3 File (Main)</h2>
    <p class="mb-4">Buat <code>main.py</code>: Mengimpor keduanya dan menyatukannya di Jendela Utama.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# main.py
import customtkinter as ctk
from data import User
from ui import LayarLogin

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user_aktif = User("Admin", "123")
        self.layar = LayarLogin(self)
        self.layar.pack(fill="both", expand=True)

app = App()
app.mainloop()
'''))))
slides.append(build_slide(M8, 'm8-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Menu Makanan Eksternal</h2>
    <p class="mb-4"><b>Misi:</b> Pisahkan Data Makanan ke file berbeda!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Buat <code>menu.py</code> berisi daftar makanan (List of Objects class <code>Menu</code>).</li>
        <li>Buat <code>main.py</code> berisi aplikasi GUI.</li>
        <li>Di <code>main.py</code>, import daftar makanan dari <code>menu.py</code>, lalu cetak ke layar GUI dengan perulangan <code>for</code>.</li>
    </ul>
    <p class="text-muted italic">Persiapan yang bagus sebelum final project!</p>
'''))

slides.append(build_slide(M8, 'm8-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Modular coding artinya memecah kode menjadi beberapa file <code>.py</code> agar rapi.</li>
        <li>Gunakan <code>from nama_file import NamaClass</code> untuk mengambil data dari file lain.</li>
        <li>Jangan gunakan akhiran <code>.py</code> di sintaks import.</li>
        <li>File harus berada di dalam folder yang sama agar mudah terhubung.</li>
    </ul>
'''))
slides.append(build_slide(M8, 'm8-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Dalam membuat game raksasa dengan tim 10 orang, mengapa Modular Coding menjadi solusi terbaik dibanding mengetik 1 file bersama-sama?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Setiap orang bisa mengerjakan 1 File/Modul secara terpisah tanpa bertabrakan atau merusak kode orang lain. Nanti tinggal disatukan di main.py!</p>
    </div>
'''))
slides.append(build_slide(M8, 'm8-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Selamat! Kamu telah menyelesaikan SELURUH materi konsep dasar Level 4! 🎉</p>
    <p class="text-lg">Di 4 pertemuan terakhir (Meeting 9-12), kita akan fokus penuh merancang dan membangun Aplikasi OOP canggih buatanmu sendiri!</p>
'''))
slides.append(build_slide(M8, 'm8-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Clean code always looks like it was written by someone who cares."</p>
        <p class="text-xl">— Michael Feathers</p>
    </div>
'''))


# ======================= MEETING 9: Ideation & Planning =======================
M9 = 9
slides.append(build_slide(M9, 'm9-s1', '1. Opening', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 9! 🚀</h2>
    <p class="text-xl mb-4">Hari ini adalah langkah awal dari pembuatan Karya Akhirmu!</p>
    <p class="text-lg text-muted">Bukan lagi belajar teori, tapi bagaimana menyusun IDE aplikasi menjadi kenyataan.</p>
'''))
slides.append(build_slide(M9, 'm9-s1', '1. Flashback', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Senjata Rahasiamu (Level 4 Toolkit)</h2>
    <div class="grid grid-cols-2 gap-4">
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">1. OOP Base</h3>
            <p class="text-sm">Class, Object, Attributes, Methods.</p>
        </div>
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">2. Constructor</h3>
            <p class="text-sm"><code>__init__</code> untuk start awal.</p>
        </div>
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">3. OOP GUI</h3>
            <p class="text-sm">Menyusun widget dengan <code>self.</code></p>
        </div>
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">4. Inheritance & Multi-Window</h3>
            <p class="text-sm">Pop-up dan Halaman canggih.</p>
        </div>
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">5. Class Interaction</h3>
            <p class="text-sm">Memisahkan Data & Tampilan.</p>
        </div>
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500">
            <h3 class="font-bold">6. Modular Coding</h3>
            <p class="text-sm">Memecah aplikasi jadi banyak file <code>.py</code>.</p>
        </div>
    </div>
'''))

slides.append(build_slide(M9, 'm9-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu mengidentifikasi permasalahan pengguna dan merancang solusi aplikasinya.</li>
        <li>Mampu menyusun kerangka MVP (Minimum Viable Product) yang realistis.</li>
        <li>Mampu merancang diagram alur (Class Diagram / Flow) untuk arsitektur OOP.</li>
    </ul>
'''))

slides.append(build_slide(M9, 'm9-s3', '3. Ideation: Menemukan Masalah', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Semua Dimulai dari Masalah</h2>
    <p class="mb-4 text-lg">Aplikasi terbaik di dunia tidak dibuat dari ide acak. Mereka dibuat untuk menyelesaikan <b>masalah (Problem)</b> orang lain.</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Gojek: Orang susah cari ojek saat butuh cepat.</li>
        <li>Tokopedia: Orang takut ditipu saat beli barang online jarak jauh.</li>
    </ul>
'''))
slides.append(build_slide(M9, 'm9-s3', '3. Ideation: Menemukan Masalah', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Contoh Ide & Masalah (Inspirasi Level 4)</h2>
    <div class="space-y-4">
        <div class="bg-[#0f172a] p-4 rounded border border-[#334155]">
            <p class="font-bold text-yellow">1. Sistem Kasir Toko Kopi</p>
            <p class="text-sm">Masalah: Toko masih hitung manual, sering salah kembalian.</p>
        </div>
        <div class="bg-[#0f172a] p-4 rounded border border-[#334155]">
            <p class="font-bold text-yellow">2. To-Do List Belajar</p>
            <p class="text-sm">Masalah: Siswa sering lupa PR apa yang besok dikumpulkan.</p>
        </div>
        <div class="bg-[#0f172a] p-4 rounded border border-[#334155]">
            <p class="font-bold text-yellow">3. Sistem Absensi Ekskul</p>
            <p class="text-sm">Masalah: Absensi pakai kertas sering hilang atau lecek.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M9, 'm9-s4', '4. Konsep MVP (Minimum Viable Product)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Fokus pada Inti (MVP)!</h2>
    <p class="mb-4 text-lg"><b>MVP (Minimum Viable Product)</b> adalah versi aplikasi paling dasar, tapi fitur utamanya BERJALAN.</p>
    <div class="flex gap-4">
        <div class="flex-1 bg-red-900/40 p-4 border border-red-500 rounded-xl">
            <h3 class="font-bold">Ekspektasi Lebay</h3>
            <p class="text-sm">Kasir pakai AI Scanner, Face Recognition, Kirim Email Nota otomatis. (Gagal di tengah jalan karena waktu habis).</p>
        </div>
        <div class="flex-1 bg-green-900/40 p-4 border border-green-500 rounded-xl">
            <h3 class="font-bold">Ekspektasi MVP (Fokus)</h3>
            <p class="text-sm">Ada tombol menu kopi, ada daftar keranjang, ada fitur hitung total dan cetak kembalian di layar. (Selesai dan jalan mulus!).</p>
        </div>
    </div>
'''))

slides.append(build_slide(M9, 'm9-s5', '5. Framework Perencanaan (Copy-Ready)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Salin Framework Ini ke Google Docs/Notion-mu!</h2>
    <div class="bg-black/30 p-4 rounded font-mono text-sm overflow-y-auto max-h-[400px]">
        <p class="text-yellow font-bold">--- PROJECT BLUEPRINT ---</p>
        <p>1. NAMA APLIKASI: [Isi...]</p>
        <p>2. PROBLEM YANG DISELESAIKAN: [Isi...]</p>
        <p>3. TARGET USER (Siapa yg pakai): [Isi...]</p>
        <p><br>4. FITUR MVP (3 Syarat Utama):</p>
        <p>- Fitur 1: (misal: Tambah Barang)</p>
        <p>- Fitur 2: (misal: Hapus Barang)</p>
        <p>- Fitur 3: (misal: Hitung Total)</p>
        <p><br>5. FITUR BONUS (Kerjakan jika waktu sisa):</p>
        <p>- Bonus: (misal: Warna UI berganti Dark Mode)</p>
        <p><br>6. TEKNOLOGI YANG DIPAKAI:</p>
        <p>- Class Data, Class GUI, CTkFrame, CTkToplevel.</p>
    </div>
'''))

slides.append(build_slide(M9, 'm9-s6', '6. Merancang Class Diagram', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Siapkan Cetak Biru (Class Diagram)</h2>
    <p class="mb-4 text-lg">Sebelum koding, rancang dulu di kertas! Apa nama Class Datanya, apa nama Class GUI-nya?</p>
    <div class="flex justify-center my-4">
        <table class="border-collapse border border-blue-500 w-3/4">
            <tr>
                <th class="border border-blue-500 p-2 bg-blue-900/40">Data (model.py)</th>
                <th class="border border-blue-500 p-2 bg-green-900/40">GUI (main.py)</th>
            </tr>
            <tr>
                <td class="border border-blue-500 p-2">class Item<br>class Keranjang</td>
                <td class="border border-blue-500 p-2">class App(ctk.CTk)<br>class FrameMenu(ctk.CTkFrame)</td>
            </tr>
        </table>
    </div>
'''))

slides.append(build_slide(M9, 'm9-s7', '7. Milestone M9-M11', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Timeline Proyekmu</h2>
    <ul class="list-none space-y-4 text-lg">
        <li>🚀 <b>Meeting 9 (Hari Ini):</b> Ide disetujui, Dokumen Perencanaan (Blueprint) selesai, Buat file project kosong.</li>
        <li>⚙️ <b>Meeting 10 (Minggu Depan):</b> Koding fitur utama (MVP) sampai selesai dan tidak error. Draft Elevator Pitch.</li>
        <li>🎨 <b>Meeting 11:</b> Testing aplikasi, perbaiki bug, percantik UI warna, kerjakan bonus jika sempat, latihan presentasi.</li>
        <li>🎤 <b>Meeting 12:</b> Showtime! Presentasi di depan teman-teman.</li>
    </ul>
'''))

slides.append(build_slide(M9, 'm9-s8', '8. Workshop Time', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6 text-center">Let's Work! 🛠️</h2>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155]">
        <p class="text-xl mb-4 font-bold text-center">Tugas Hari Ini:</p>
        <ol class="list-decimal list-inside space-y-2 text-lg">
            <li>Pikirkan Ide Aplikasimu.</li>
            <li>Buat salinan "Project Blueprint" di Docs.</li>
            <li>Tulis fitur MVP (jangan muluk-muluk!).</li>
            <li>Konsultasikan dan minta Tanda Tangan/Persetujuan Guru.</li>
            <li>Buka VS Code, buat folder project, dan buat kerangka <code>main.py</code>, <code>data.py</code> yang kosong (pass).</li>
        </ol>
    </div>
'''))

slides.append(build_slide(M9, 'm9-s9', '9. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket</h2>
    <p class="text-xl mb-4">Pastikan Gurumu telah menyetujui ide MVP-mu!</p>
    <p class="text-lg">Ide yang tidak di-acc guru biasanya: terlalu susah (AI/Cloud) untuk 2 pertemuan, atau kebalikannya: tidak menggunakan materi OOP sama sekali.</p>
'''))
slides.append(build_slide(M9, 'm9-s9', '9. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"A goal without a plan is just a wish."</p>
        <p class="text-xl">— Antoine de Saint-Exupéry</p>
    </div>
'''))


# Inject slides into existing deck.html
import re
import sys

try:
    with open("level4/deck.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    match = re.search(r'</div>\s*<script>', html)
    if match:
        parts = html.split(match.group(0))
        new_html = parts[0] + "\\n" + "\\n".join(slides) + "\\n" + match.group(0) + parts[1]
        with open("level4/deck.html", "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Deck HTML successfully updated with Batch 3 (Meetings 7-9) content via regex!")
    else:
        print("ERROR: Could not find insertion point.")
except Exception as e:
    print("Error:", e)
