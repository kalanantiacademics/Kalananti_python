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

# ======================= MEETING 4: OOP in CustomTkinter =======================
M4 = 4
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 4! 🚀</h2>
    <p class="text-xl mb-4">Hari ini kita akan menghubungkan dua kekuatan besar: OOP dan GUI (CustomTkinter)!</p>
    <p class="text-lg text-muted">Mari kita review Constructor <code>__init__</code> terlebih dahulu.</p>
'''))
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Kapan Method <code>__init__</code> otomatis dijalankan?</p>
''' + get_quiz("Pilih jawaban:", ["Saat program ditutup", "Saat objek pertama kali dibuat", "Saat kita memanggilnya dengan objek.__init__()"], 1)))
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Berapa jumlah underscore yang digunakan pada <code>__init__</code>?</p>
''' + get_quiz("Pilih jawaban:", ["Satu di depan, satu di belakang", "Dua di depan, dua di belakang (Dunder)", "Tiga di depan"], 1)))
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Apa fungsi dari parameter <code>self</code> pada Constructor?</p>
''' + get_quiz("Pilih jawaban:", ["Menghapus data", "Merujuk pada objek itu sendiri agar bisa menyimpan atribut", "Menutup jendela aplikasi"], 1)))
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Perhatikan: <code>class A: def __init__(self, nama): self.nama = nama</code>. Bagaimana membuat objeknya?</p>
''' + get_quiz("Pilih jawaban:", ["obj = A()", "obj = A(\"Budi\")", "obj = A.nama(\"Budi\")"], 1)))
slides.append(build_slide(M4, 'm4-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Apa error yang terjadi jika kita tidak memasukkan nilai wajib ke <code>__init__</code>?</p>
''' + get_quiz("Pilih jawaban:", ["NameError", "TypeError: missing required positional argument", "ValueError"], 1)))

slides.append(build_slide(M4, 'm4-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menerapkan struktur OOP untuk membangun aplikasi GUI dengan CustomTkinter (Standar Industri).</li>
        <li>Mampu mengatur widget dan layout di dalam Class.</li>
        <li>Mampu menghubungkan <code>command</code> tombol dengan Method (Event Handling berbasis Class).</li>
    </ul>
'''))

slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Kenapa pakai OOP untuk GUI?</h2>
    <p class="mb-4 text-lg">Di Level 3, kita membuat aplikasi dengan banyak variabel global (berantakan!).</p>
    <p class="mb-4 text-lg">Dengan OOP, sebuah <b>Aplikasi</b> adalah sebuah <b>Object</b>. Widget-widget (Tombol, Label, Input) adalah <b>Attributes</b>-nya, dan fungsi klik tombol adalah <b>Methods</b>-nya!</p>
    <p class="text-lg">Ini adalah standar industri yang digunakan oleh programmer profesional.</p>
'''))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Arsitektur GUI</h2>
    <div class="bg-[#0a1830] p-6 rounded-xl flex items-center justify-between text-center gap-6">
        <div class="flex-1 bg-red-900/40 p-4 rounded-xl">
            <h3 class="font-bold mb-2">Level 3 (Prosedural)</h3>
            <p class="text-sm">root = CTk()<br>btn = CTkButton()<br>lbl = CTkLabel()<br>def fungsi(): ...<br>btn.configure(command=fungsi)</p>
            <p class="text-xs text-muted mt-2 text-red-300">Variabel bercampur di mana-mana.</p>
        </div>
        <div class="flex-1 bg-green-900/40 p-4 rounded-xl">
            <h3 class="font-bold mb-2">Level 4 (OOP)</h3>
            <p class="text-sm">class App(ctk.CTk):<br>&nbsp;&nbsp;def __init__(self):<br>&nbsp;&nbsp;&nbsp;&nbsp;self.btn = CTkButton()<br>&nbsp;&nbsp;def fungsi(self): ...</p>
            <p class="text-xs text-muted mt-2 text-green-300">Semua rapi terbungkus dalam "App".</p>
        </div>
    </div>
'''))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan membangun sebuah <b>Rumah</b> (Aplikasi GUI).</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li><b>Tanpa OOP:</b> Material berserakan di jalan. Siapapun bisa tersandung paku.</li>
        <li><b>Dengan OOP:</b> Semua material dimasukkan ke kotak <code>self</code>. Tukang kayu (Method) bisa mengambil alat (Atribut) dari kotak <code>self</code> dengan mudah tanpa mengganggu tetangga.</li>
    </ul>
'''))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Kerangka Dasar OOP CustomTkinter</h2>
    <p class="mb-4">Kita akan mewarisi (inherit) kemampuan <code>ctk.CTk</code> ke dalam Class kita sendiri.</p>
''' + get_code('''
import customtkinter as ctk

class AplikasiSaya(ctk.CTk):
    def __init__(self):
        super().__init__() # Memanggil constructor CTk
        self.title("Aplikasi OOP Pertama")
        self.geometry("400x300")
        
        # Simpan widget di self
        self.label = ctk.CTkLabel(self, text="Halo, OOP!")
        self.label.pack(pady=20)

# Jalankan aplikasi
if __name__ == "__main__":
    app = AplikasiSaya()
    app.mainloop()
''') + get_reveal("Penjelasan", "<p>Dengan <code>super().__init__()</code>, Class kita mendapatkan semua fungsi jendela CustomTkinter secara instan! <code>self</code> sekarang bertindak sebagai Jendela Utama (root).</p>")))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Menghubungkan Tombol</h2>
    <p class="mb-4">Bagaimana cara kita memasang <code>command</code> pada tombol?</p>
''' + get_code('''
class Aplikasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # command memanggil method menggunakan self
        self.btn = ctk.CTkButton(self, text="Klik Aku", command=self.saat_diklik)
        self.btn.pack(pady=20)

    # Ini adalah method-nya
    def saat_diklik(self):
        print("Tombol berhasil ditekan!")
''') + get_reveal("Kenapa pakai self.saat_diklik?", "<p>Karena fungsi <code>saat_diklik</code> sekarang menempel pada objek <code>self</code>. Tanpa <code>self.</code>, Python tidak akan menemukannya!</p>")))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.label = ctk.CTkLabel(self, text="Halo")
        self.btn = ctk.CTkButton(self, text="Ubah", command=ubah_teks)

    def ubah_teks(self):
        self.label.configure(text="Berhasil")
''') + get_quiz("Apa yang terjadi saat dijalankan?", [
    "Akan error 'ubah_teks' is not defined karena kurang self. di parameter command",
    "Berjalan normal",
    "Akan langsung mengubah teks sebelum tombol ditekan"
], 0)))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Selalu gunakan <code>self.nama_widget</code> agar widget bisa diakses/diubah dari method manapun di dalam class.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan menambahkan kurung <code>()</code> pada command: <code>command=self.fungsi()</code>. Itu akan membuat fungsi langsung dijalankan tanpa menunggu tombol ditekan!</p>
        </div>
    </div>
'''))
slides.append(build_slide(M4, 'm4-s3', '3. OOP in GUI', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika menemui Error GUI di OOP:</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li><code>NameError: name '...' is not defined</code>: Biasanya kamu lupa menambahkan <code>self.</code> pada atribut atau method.</li>
        <li><code>AttributeError: 'App' object has no attribute '...'</code>: Kamu mungkin mendefinisikan widget di <code>__init__</code> tanpa <code>self.</code> (misal: <code>btn = ...</code>).</li>
    </ul>
'''))

slides.append(build_slide(M4, 'm4-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Kerangka App</h2>
    <p class="mb-4">Buka <b>VS Code</b>! Buat Class <code>KalanantiApp</code> yang mewarisi <code>ctk.CTk</code>, beri judul "Belajar OOP GUI", ukuran "400x300". Jangan lupa <code>super().__init__()</code>!</p>
''' + get_reveal("Tampilkan Jawaban (Jalankan di VS Code)", get_code('''
import customtkinter as ctk

class KalanantiApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Belajar OOP GUI")
        self.geometry("400x300")

if __name__ == "__main__":
    app = KalanantiApp()
    app.mainloop()
'''))))
slides.append(build_slide(M4, 'm4-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Tambah Widget</h2>
    <p class="mb-4">Tambahkan <code>self.label</code> dan <code>self.entry</code> di dalam <code>__init__</code>. Gunakan <code>.pack()</code> agar tampil.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# Di dalam __init__ di bawah geometry:
        self.label = ctk.CTkLabel(self, text="Masukkan Nama:")
        self.label.pack(pady=10)
        
        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)
'''))))
slides.append(build_slide(M4, 'm4-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Menambahkan Aksi</h2>
    <p class="mb-4">Buat method <code>def sapa_user(self):</code> yang mengubah text label menjadi isi dari entry. Tambahkan tombol yang mengeksekusi method tersebut.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# Di dalam __init__:
        self.btn = ctk.CTkButton(self, text="Sapa", command=self.sapa_user)
        self.btn.pack(pady=10)

    # Sejajar dengan def __init__ (Method baru)
    def sapa_user(self):
        nama = self.entry.get()
        self.label.configure(text=f"Halo, {nama}!")
'''))))
slides.append(build_slide(M4, 'm4-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class Aplikasi(ctk.CTk):
    def __init__(self):
        super().__init__()
        teks_judul = ctk.CTkLabel(self, text="Aplikasi")
        teks_judul.pack()

    def ganti(self):
        teks_judul.configure(text="Berhasil")
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Error <code>NameError</code>! Method <code>ganti</code> tidak mengenali variabel <code>teks_judul</code> karena variabel tersebut dibuat tanpa <code>self.</code> dan terjebak di dalam <code>__init__</code>.</p>
<p>Solusi: Ubah menjadi <code>self.teks_judul = ...</code> di kedua tempat.</p>
''')))
slides.append(build_slide(M4, 'm4-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Penghitung Klik (Counter)</h2>
    <p class="mb-4">Buat aplikasi dengan OOP. Aplikasi punya Label yang menampilkan angka 0. Ada tombol "Tambah 1". Setiap tombol diklik, angka di label bertambah 1.</p>
    <p class="text-muted">Gunakan VS Code. Buat atribut <code>self.angka = 0</code> di dalam <code>__init__</code> untuk menyimpan datanya.</p>
''' + get_reveal("Hint / Petunjuk", "<p>Di dalam method <code>tambah()</code>, kamu cukup menulis <code>self.angka += 1</code> lalu <code>self.label.configure(text=str(self.angka))</code></p>")))

slides.append(build_slide(M4, 'm4-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Login Palsu (OOP)</h2>
    <p class="mb-4">Buat aplikasi yang meminta Username dan Password. Jika admin/1234, ubah label jadi "Sukses", jika salah jadi "Gagal".</p>
''' + get_reveal("Tampilkan Jawaban (Hanya kerangka class)", get_code('''
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # ... setup widgets (2 Entry, 1 Button, 1 Label) ...

    def cek_login(self):
        if self.entry_user.get() == "admin" and self.entry_pass.get() == "1234":
            self.label_status.configure(text="Sukses!", text_color="green")
        else:
            self.label_status.configure(text="Gagal!", text_color="red")
'''))))
slides.append(build_slide(M4, 'm4-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Merapikan Fungsi</h2>
    <p class="mb-4">Seringkali <code>__init__</code> jadi penuh sesak dengan puluhan widget. Mari kita pecah jadi method <code>self.buat_widget()</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.buat_widget() # Panggil fungsinya di sini!
        
    def buat_widget(self):
        # Letakkan semua kode pembuatan widget di sini
        self.label = ctk.CTkLabel(self, text="Lebih Rapi!")
        self.label.pack()
'''))))
slides.append(build_slide(M4, 'm4-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Interaksi 2 Object GUI</h2>
    <p class="mb-4">Dalam OOP, kita bisa membuat objek dari class kita sendiri sebagai penyimpan data. Contoh: class Akun (non-GUI) dan KalanantiApp (GUI).</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Akun:
    def __init__(self):
        self.saldo = 50000

class BankApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.akun_user = Akun() # Instansiasi Object Data di dalam GUI!
        self.label = ctk.CTkLabel(self, text=f"Saldo: {self.akun_user.saldo}")
        self.label.pack()
'''))))
slides.append(build_slide(M4, 'm4-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: ToDo List OOP</h2>
    <p class="mb-4"><b>Misi:</b> Buat Aplikasi Catatan Sederhana dengan OOP!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Sediakan <code>CTkEntry</code> untuk input tugas.</li>
        <li>Sediakan <code>CTkButton</code> "Tambah".</li>
        <li>Sediakan <code>CTkTextbox</code> untuk menampilkan daftar tugas.</li>
        <li>Saat diklik, masukkan tugas ke Textbox.</li>
    </ul>
    <p class="text-muted italic">Tidak ada jawaban yang disediakan. Uji aplikasimu di VS Code!</p>
'''))

slides.append(build_slide(M4, 'm4-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>OOP di CustomTkinter membuat kode aplikasi kita sangat rapi dan tertata.</li>
        <li>Kita mewarisi kemampuan window GUI menggunakan <code>class Aplikasi(ctk.CTk):</code> dan memanggil <code>super().__init__()</code>.</li>
        <li>Semua widget harus disimpan dengan <code>self.</code> agar bisa diakses oleh method (fungsi logika) di tempat lain.</li>
        <li>Gunakan <code>self.nama_method</code> pada <code>command=</code> tombol.</li>
    </ul>
'''))
slides.append(build_slide(M4, 'm4-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Kenapa menggunakan OOP dianggap "Standar Industri" untuk membuat GUI dibanding cara yang kita pelajari di Level 3?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Karena aplikasi besar bisa memiliki ratusan tombol dan fungsi. Jika tidak pakai OOP, variabel akan bertabrakan. OOP membungkusnya dalam kapsul <code>self</code> yang aman.</p>
    </div>
'''))
slides.append(build_slide(M4, 'm4-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Pernah dengar tentang "Pewarisan Harta"? Di pemrograman OOP juga ada lho!</p>
    <p class="text-lg">Di pertemuan berikutnya, kita akan belajar <b>Inheritance</b>, cara mewariskan atribut dan method ke Class baru agar kita tidak perlu menulis ulang kode dari nol!</p>
'''))
slides.append(build_slide(M4, 'm4-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Good design adds value faster than it adds cost."</p>
        <p class="text-xl">— Thomas C. Gale</p>
    </div>
'''))


# ======================= MEETING 5: Inheritance =======================
M5 = 5
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 5! 🚀</h2>
    <p class="text-xl mb-4">Siap untuk jurus pamungkas OOP: Inheritance (Pewarisan)?</p>
    <p class="text-lg text-muted">Mari kita review OOP di CustomTkinter terlebih dahulu!</p>
'''))
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Untuk membuat class Aplikasi, kita melakukan pewarisan dari Class apa di CustomTkinter?</p>
''' + get_quiz("Pilih jawaban:", ["ctk.App", "ctk.Window", "ctk.CTk"], 2)))
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Kenapa kita WAJIB menggunakan awalan <code>self.</code> saat membuat tombol di <code>__init__</code>?</p>
''' + get_quiz("Pilih jawaban:", ["Agar tombol punya warna bagus", "Agar tombol menjadi atribut yang bisa dipanggil oleh fungsi/method lain", "Agar tombol jadi lebih besar"], 1)))
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Fungsi ajaib apa yang digunakan untuk memastikan Class Induk (CTk) bekerja pada constructor kita?</p>
''' + get_quiz("Pilih jawaban:", ["super().__init__()", "self.init()", "ctk.start()"], 0)))
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Bentuk <code>command</code> yang BENAR saat menghubungkan tombol ke method di dalam class OOP adalah?</p>
''' + get_quiz("Pilih jawaban:", ["command=fungsi", "command=self.fungsi", "command=self.fungsi()"], 1)))
slides.append(build_slide(M5, 'm5-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Bagaimana cara kita mengakses widget yang sudah kita beri nama <code>self.label</code> di method yang berbeda?</p>
''' + get_quiz("Pilih jawaban:", ["Memanggil label", "Memanggil self.label", "Membuat ulang label"], 1)))

slides.append(build_slide(M5, 'm5-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menjelaskan konsep <b>Inheritance (Pewarisan)</b> dalam Object-Oriented Programming.</li>
        <li>Mampu membuat <b>Child Class</b> yang mewarisi Attribute dan Method dari <b>Parent Class</b>.</li>
        <li>Mampu menggunakan <code>super()</code> untuk memperluas fungsi parent di child class.</li>
    </ul>
'''))

slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu Inheritance?</h2>
    <p class="mb-4 text-lg"><b>Inheritance (Pewarisan)</b> memungkinkan kita membuat Class Baru berdasarkan Class yang sudah ada.</p>
    <p class="text-lg">Class yang ditiru disebut <b>Parent Class</b> (Induk). Class yang baru disebut <b>Child Class</b> (Anak).</p>
    <p class="text-lg mt-4">Sang anak akan secara otomatis mewarisi SEMUA atribut dan method sang induk tanpa kita harus mengetik ulang!</p>
'''))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Pohon Keluarga (Hirarki)</h2>
    <div class="flex flex-col items-center gap-4 bg-[#0a1830] p-6 rounded-xl text-center">
        <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500 w-64">
            <h3 class="font-bold text-yellow">Kendaraan (Parent)</h3>
            <p class="text-sm">Method: maju(), rem()</p>
        </div>
        <div class="text-4xl">⬇️</div>
        <div class="flex gap-6 w-full justify-center">
            <div class="bg-green-900/40 p-4 rounded-xl border border-green-500 w-64">
                <h3 class="font-bold text-yellow">Mobil (Child)</h3>
                <p class="text-sm">+ Atribut: jumlah_ban=4</p>
                <p class="text-xs mt-2 italic text-muted">Otomatis bisa maju() & rem()</p>
            </div>
            <div class="bg-red-900/40 p-4 rounded-xl border border-red-500 w-64">
                <h3 class="font-bold text-yellow">Pesawat (Child)</h3>
                <p class="text-sm">+ Method: terbang()</p>
                <p class="text-xs mt-2 italic text-muted">Otomatis bisa maju() & rem()</p>
            </div>
        </div>
    </div>
'''))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Menu Kalananti Cafe!</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Semua menu pasti punya <b>Nama</b> dan <b>Harga</b> (Parent: <code>MenuUtama</code>).</li>
        <li>Kopi Susu punya tambahan <b>Ukuran Gelas</b> (Child: <code>Minuman</code>).</li>
        <li>Nasi Goreng punya tambahan <b>Level Pedas</b> (Child: <code>Makanan</code>).</li>
    </ul>
    <p class="mt-4 italic text-muted">Daripada menulis Nama & Harga berulang kali, kita cukup wariskan!</p>
'''))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Sintaks Inheritance</h2>
    <p class="mb-4">Cara mewariskan class adalah dengan memasukkan nama Parent Class di dalam kurung setelah nama Child Class.</p>
''' + get_code('''
# Parent Class
class Hewan:
    def makan(self):
        print("Nyam nyam!")

# Child Class: Kucing (Mewarisi Hewan)
class Kucing(Hewan):
    def mengeong(self):
        print("Meow!")

kucing_oren = Kucing()
kucing_oren.makan()    # Method warisan dari Hewan
kucing_oren.mengeong() # Method miliknya sendiri
''')))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Memanggil super()</h2>
    <p class="mb-4">Saat kita butuh mengambil Constructor (<code>__init__</code>) milik parent, kita wajib menggunakan fungsi <code>super().__init__()</code>.</p>
''' + get_code('''
class Karyawan:
    def __init__(self, nama):
        self.nama = nama

class Programmer(Karyawan):
    def __init__(self, nama, bahasa_koding):
        super().__init__(nama) # Serahkan ke Parent
        self.bahasa = bahasa_koding # Khusus Child

p = Programmer("Budi", "Python")
print(p.nama, "ahli", p.bahasa)
''')))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
class Bapak:
    def info(self):
        print("Ini dari Bapak")

class Anak(Bapak):
    pass

a = Anak()
a.info()
''') + get_quiz("Apa yang tercetak di layar?", [
    "Error, karena Anak menggunakan pass",
    "Ini dari Bapak",
    "Kosong, tidak mencetak apa-apa"
], 1)))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Gunakan konsep <b>DRY (Don't Repeat Yourself)</b>. Jika dua class punya banyak atribut sama, buatkan Parent Class.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Lupa memanggil <code>super().__init__()</code> di dalam Child Class jika Child Class tersebut membuat method <code>__init__</code> sendiri.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M5, 'm5-s3', '3. Inheritance (Pewarisan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika menemui Error: <code>AttributeError: 'Child' object has no attribute 'nama'</code></p>
    <p><b>Solusi:</b> Periksa apakah kamu lupa menulis <code>super().__init__()</code> di dalam Child! Tanpa perintah itu, Constructor Parent yang menyematkan atribut <code>nama</code> tidak pernah berjalan.</p>
'''))

slides.append(build_slide(M5, 'm5-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Hewan Keturunan</h2>
    <p class="mb-4">Buat Parent Class <code>Burung</code> dengan method <code>terbang</code>. Buat Child Class <code>Elang</code> yang mewarisi <code>Burung</code> dan tambahkan method <code>buru_mangsa</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Burung:
    def terbang(self):
        print("Melayang di udara...")

class Elang(Burung):
    def buru_mangsa(self):
        print("Menukik menangkap mangsa!")

e = Elang()
e.terbang()     # Warisan
e.buru_mangsa() # Miliknya sendiri
'''))))
slides.append(build_slide(M5, 'm5-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Parent Konstruktor</h2>
    <p class="mb-4">Buat Parent Class <code>Kendaraan</code> yang menerima argumen <code>roda</code>. Buat Child Class <code>SepedaMotor</code> yang punya <code>roda=2</code> tapi memanggil <code>super()</code> ke Kendaraan.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Kendaraan:
    def __init__(self, roda):
        self.roda = roda

class SepedaMotor(Kendaraan):
    def __init__(self):
        # Mengirim angka 2 ke Parent!
        super().__init__(2)
        
motor = SepedaMotor()
print("Jumlah Roda:", motor.roda)
'''))))
slides.append(build_slide(M5, 'm5-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Menimpa Method (Polymorphism/Override)</h2>
    <p class="mb-4">Jika Anak punya nama Method yang SAMA dengan Induk, Method Anak yang akan menang! (Override). Coba buat class Kucing yang menimpa method <code>suara()</code> dari class Hewan.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Hewan:
    def suara(self):
        print("Suara random...")

class Kucing(Hewan):
    def suara(self):
        print("Meow!")

kucing = Kucing()
kucing.suara() # Output: Meow!
'''))))
slides.append(build_slide(M5, 'm5-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class Makanan:
    def __init__(self, nama):
        self.nama = nama

class MakananPedas(Makanan):
    def __init__(self, nama, pedas):
        self.pedas = pedas

mie = MakananPedas("Mie", 5)
print(mie.nama)
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Error AttributeError! <code>MakananPedas</code> lupa memanggil <code>super().__init__(nama)</code> sehingga atribut <code>self.nama</code> tidak pernah terbentuk.</p>
''')))
slides.append(build_slide(M5, 'm5-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Karakter RPG</h2>
    <p class="mb-4">Buat Parent Class <code>Character</code> dengan method <code>jalan()</code>. Buat Child <code>Mage</code> yang punya method khusus <code>cast_spell()</code>. Panggil keduanya melalui objek Mage.</p>
''' + get_reveal("Hint / Petunjuk", "<p><code>class Mage(Character):</code>. Pastikan membuat objek Mage(), lalu panggil <code>.jalan()</code> dan <code>.cast_spell()</code>.</p>")))

slides.append(build_slide(M5, 'm5-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Akun Premium</h2>
    <p class="mb-4">Buat Parent <code>AkunBank</code> (saldo 100k). Buat Child <code>AkunPremium</code> yang menambah atribut <code>cashback = 5000</code> menggunakan <code>super()</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class AkunBank:
    def __init__(self):
        self.saldo = 100000

class AkunPremium(AkunBank):
    def __init__(self):
        super().__init__() # Dapatkan saldo 100k
        self.cashback = 5000

vip = AkunPremium()
print(vip.saldo, vip.cashback)
'''))))
slides.append(build_slide(M5, 'm5-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Tombol Khusus (OOP di GUI)</h2>
    <p class="mb-4">Kita bisa mewarisi widget! Buat <code>TombolBahaya(ctk.CTkButton)</code> yang otomatis selalu berwarna merah dan punya teks "AWAS".</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
# Contoh kerangka kodenya saja
class TombolBahaya(ctk.CTkButton):
    def __init__(self, parent_window):
        # Meneruskan ke CTkButton asli
        super().__init__(parent_window, text="AWAS", fg_color="red")
        
# Di aplikasi utama
# btn = TombolBahaya(self)
# btn.pack()
'''))))
slides.append(build_slide(M5, 'm5-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Menu Cafe</h2>
    <p class="mb-4">Parent <code>Menu(nama, harga)</code>. Child <code>Minuman(nama, harga, ukuran)</code>. Print info minumannya!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Minuman(Menu):
    def __init__(self, nama, harga, ukuran):
        super().__init__(nama, harga)
        self.ukuran = ukuran

kopi = Minuman("Kopi Susu", 25000, "Besar")
print(f"{kopi.nama} ukuran {kopi.ukuran} - Rp{kopi.harga}")
'''))))
slides.append(build_slide(M5, 'm5-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Alat Musik</h2>
    <p class="mb-4"><b>Misi:</b> Bangun hierarki alat musik!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Parent: <code>AlatMusik</code> dengan method <code>mainkan()</code> (Cetak: Bunyi nada...).</li>
        <li>Child 1: <code>Gitar</code>. Method khusus: <code>petik()</code>.</li>
        <li>Child 2: <code>Drum</code>. Method khusus: <code>pukul()</code>.</li>
        <li>Buat objek Gitar dan Drum, lalu panggil semua kemampuan mereka (baik yang diwarisi maupun kemampuan sendiri).</li>
    </ul>
    <p class="text-muted italic">Tidak ada jawaban yang disediakan. Ayo tunjukkan kodemu ke gurumu!</p>
'''))

slides.append(build_slide(M5, 'm5-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li><b>Inheritance</b> menghindari pengetikan ulang kode (DRY).</li>
        <li><b>Child Class</b> mewarisi semua sifat dan kemampuan <b>Parent Class</b>.</li>
        <li>Untuk memanggil <code>__init__</code> milik parent dari dalam child, gunakan <code>super().__init__()</code>.</li>
        <li>Method di Parent bisa ditimpa (override) oleh method bernama sama di Child.</li>
    </ul>
'''))
slides.append(build_slide(M5, 'm5-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Ingat class Aplikasi yang kita buat di materi sebelumnya? <code>class App(ctk.CTk):</code></p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Sebenarnya kita diam-diam SUDAH menggunakan Inheritance lho! Kita membuat Child Class (App) yang mewarisi kekuatan Jendela GUI dari Parent Class (ctk.CTk)! Keren kan?</p>
    </div>
'''))
slides.append(build_slide(M5, 'm5-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Aplikasi nyata jarang sekali hanya menggunakan satu jendela. Pasti ada jendela login, lalu dashboard utama.</p>
    <p class="text-lg">Di pertemuan berikutnya, kita akan menggunakan <code>CTkToplevel</code> dan Frame Switching untuk Multi-window Navigation ala aplikasi profesional!</p>
'''))
slides.append(build_slide(M5, 'm5-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"If I have seen further it is by standing on the shoulders of Giants."</p>
        <p class="text-xl">— Isaac Newton (Sempurna untuk Inheritance!)</p>
    </div>
'''))


# ======================= MEETING 6: Multi-window Navigation =======================
M6 = 6
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 6! 🚀</h2>
    <p class="text-xl mb-4">Hari ini kita akan membuat aplikasi dengan banyak halaman (Navigation)!</p>
    <p class="text-lg text-muted">Mari kita ingat lagi tentang Pewarisan OOP.</p>
'''))
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Dalam <code>class B(A):</code>, manakah yang merupakan Parent Class?</p>
''' + get_quiz("Pilih jawaban:", ["Class A", "Class B", "Keduanya"], 0)))
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Apakah Child Class wajib menulis ulang (copy-paste) isi dari Parent Class?</p>
''' + get_quiz("Pilih jawaban:", ["Ya, agar tidak error", "Tidak, Child otomatis mewarisi tanpa harus diketik ulang"], 1)))
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Apa kepanjangan dari prinsip DRY dalam koding?</p>
''' + get_quiz("Pilih jawaban:", ["Do Run Yourself", "Don't Repeat Yourself", "Draw Reality Yearly"], 1)))
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Apa sintaks yang digunakan untuk memanggil constructor Parent dari dalam constructor Child?</p>
''' + get_quiz("Pilih jawaban:", ["parent()", "super().__init__()", "self.__init__()"], 1)))
slides.append(build_slide(M6, 'm6-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Jika sebuah method di Child namanya SAMA PERSIS dengan di Parent (misal: method suara). Mana yang akan dijalankan oleh si Anak?</p>
''' + get_quiz("Pilih jawaban:", ["Method milik Parent", "Method milik Anak (ditimpa/override)", "Dua-duanya"], 1)))

slides.append(build_slide(M6, 'm6-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu memahami arsitektur <b>Satu Root</b> dalam CustomTkinter.</li>
        <li>Mampu menggunakan <b>CTkFrame</b> untuk berpindah "halaman" di dalam jendela yang sama.</li>
        <li>Mampu menggunakan <b>CTkToplevel</b> untuk memunculkan jendela baru (Pop-up/Dialog) secara OOP.</li>
    </ul>
'''))

slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Aturan Emas: Hanya Satu Jendela Utama!</h2>
    <p class="mb-4 text-lg">Dalam membuat aplikasi dengan Tkinter/CustomTkinter, <b>JANGAN PERNAH</b> memanggil <code>ctk.CTk()</code> atau menggunakan <code>mainloop()</code> lebih dari satu kali secara bersamaan.</p>
    <p class="text-lg">Mengapa? Karena sistem grafis (GUI) bisa crash atau hang akibat bentrok memori.</p>
'''))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Lalu, bagaimana cara ganti halaman?</h2>
    <div class="grid grid-cols-2 gap-6 bg-[#0a1830] p-6 rounded-xl">
        <div>
            <h3 class="font-bold text-blue-400 mb-2">1. Frame Switching (Ganti Layar)</h3>
            <p>Jendela utamanya (Root) tetap satu, tapi kita menghapus "Kertas (Frame)" lama dan memasang "Kertas (Frame)" baru ke dalam Root. Sangat mulus seperti aplikasi di HP.</p>
        </div>
        <div>
            <h3 class="font-bold text-yellow mb-2">2. CTkToplevel (Jendela Tambahan)</h3>
            <p>Memunculkan jendela pop-up di atas jendela utama. Cocok untuk dialog informasi, pengaturan, atau peringatan.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li><b>Frame Switching:</b> Seperti buku tulis. Bukunya (Window) tetap satu, tapi kamu membalik kertas/halamannya (Frame).</li>
        <li><b>CTkToplevel:</b> Seperti menempelkan Sticky Note / Post-It tambahan di atas buku tersebut.</li>
    </ul>
'''))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: CTkToplevel</h2>
    <p class="mb-4">Kita bisa membuat class untuk jendela sekunder dengan mewarisi <code>ctk.CTkToplevel</code>.</p>
''' + get_code('''
class JendelaPopup(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Jendela Tambahan")
        self.geometry("300x200")
        
        self.lbl = ctk.CTkLabel(self, text="Halo, saya Pop Up!")
        self.lbl.pack(pady=20)
''') + get_reveal("Penjelasan", "<p>Sangat mirip dengan membuat Root, tapi kita gunakan Toplevel agar dia tidak crash dengan Window Utama!</p>")))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Memanggil Toplevel dari Utama</h2>
    <p class="mb-4">Di jendela utama, kita cukup instansiasi objek dari Class Popup tersebut di dalam Method.</p>
''' + get_code('''
class AplikasiUtama(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.btn = ctk.CTkButton(self, text="Buka Pop-up", command=self.buka_popup)
        self.btn.pack()
        # Simpan state popup
        self.popup = None 

    def buka_popup(self):
        # Mencegah terbukanya banyak popup berulang kali
        if self.popup is None or not self.popup.winfo_exists():
            self.popup = JendelaPopup(self)
        else:
            self.popup.focus()
''')))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
def salah_cara():
    app1 = ctk.CTk()
    app2 = ctk.CTk()
    app1.mainloop()
    app2.mainloop()
''') + get_quiz("Apa yang terjadi pada kode di atas?", [
    "Dua jendela akan muncul berdampingan dengan lancar.",
    "Akan error atau program 'hang' (macet) karena ada dua jendela utama dan dua mainloop bersaing.",
    "Jendela kedua akan menimpa jendela pertama."
], 1)))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Jadikan halaman-halaman aplikasimu (Login, Dashboard) sebagai <b>Frame (ctk.CTkFrame)</b> dan gonta-ganti menggunakan <code>.pack_forget()</code> lalu di-<code>.pack()</code> ulang yang baru.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan pernah membuat dua Class yang keduanya mewarisi <code>ctk.CTk</code> di aplikasi yang sama.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M6, 'm6-s3', '3. Multi-Window Navigation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika menekan tombol berulang kali dan memunculkan 10 jendela popup yang sama tanpa sengaja:</p>
    <p><b>Solusi:</b> Tambahkan logika pengecekan <code>if self.toplevel is None or not self.toplevel.winfo_exists():</code> seperti kode sebelumnya! Ini menjaga agar hanya ada 1 popup aktif.</p>
'''))

slides.append(build_slide(M6, 'm6-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Bikin Pop-up Kosong</h2>
    <p class="mb-4">Buat Class <code>InfoApp(ctk.CTkToplevel)</code> yang mengatur ukurannya jadi "200x150".</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class InfoApp(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Info")
        self.geometry("200x150")
'''))))
slides.append(build_slide(M6, 'm6-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Trigger Pop-up</h2>
    <p class="mb-4">Di <code>AplikasiUtama(ctk.CTk)</code>, buat method <code>show_info(self)</code> yang langsung memanggil <code>InfoApp(self)</code> tanpa pengecekan ganda dulu.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class AplikasiUtama(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.btn = ctk.CTkButton(self, text="Klik!", command=self.show_info)
        self.btn.pack(pady=20)

    def show_info(self):
        InfoApp(self)  # Memunculkan jendela!
'''))))
slides.append(build_slide(M6, 'm6-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Frame Switching Dasar</h2>
    <p class="mb-4">Siapkan dua frame <code>self.frame_A</code> dan <code>self.frame_B</code>. Buat method <code>ke_B(self)</code> yang menghapus A dari layar dan mem-pack B.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
    def ke_B(self):
        # Sembunyikan Frame A
        self.frame_A.pack_forget()
        # Munculkan Frame B
        self.frame_B.pack(fill="both", expand=True)
'''))))
slides.append(build_slide(M6, 'm6-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class Pop(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pop up")

class Utama(ctk.CTk):
    def buka(self):
        p = Pop()
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Class <code>Pop</code> harusnya mewarisi <code>ctk.CTkToplevel</code>, BUKAN <code>ctk.CTk</code>. Aplikasi akan crash karena ada dua jendela utama.</p>
''')))
slides.append(build_slide(M6, 'm6-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Warning Pop-up</h2>
    <p class="mb-4">Buat aplikasi dengan tombol "Hapus Data". Saat ditekan, akan muncul `CTkToplevel` dengan pesan "Apakah kamu yakin?"</p>
    <p class="text-muted">Gunakan VS Code!</p>
''' + get_reveal("Hint / Petunjuk", "<p>Buat Class khusus `PeringatanToplevel` dan panggil dari <code>command</code> tombol di Class Utama.</p>")))

slides.append(build_slide(M6, 'm6-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Setup Frame OOP</h2>
    <p class="mb-4">Mari kita bangun kerangka "Halaman" (Frame) menggunakan OOP. Buat Class <code>HalamanHome</code> yang mewarisi <code>ctk.CTkFrame</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class HalamanHome(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # Widget isi halaman
        self.label = ctk.CTkLabel(self, text="Ini Halaman Home!")
        self.label.pack(pady=50)
'''))))
slides.append(build_slide(M6, 'm6-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Hubungkan Frame ke App</h2>
    <p class="mb-4">Di <code>AplikasiUtama</code>, panggil `HalamanHome` dan pack ke dalam layar utama.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class AplikasiUtama(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        
        # Memasang Frame ke dalam Jendela Utama
        self.home = HalamanHome(self)
        self.home.pack(fill="both", expand=True)
'''))))
slides.append(build_slide(M6, 'm6-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Menu Navigasi</h2>
    <p class="mb-4">Tambahkan frame untuk tombol di sebelah kiri (Sidebar), dan ganti-ganti konten di sebelah kanan.</p>
''' + get_reveal("Tampilkan Jawaban (Konsep)", get_code('''
# Sidebar ditaruh menggunakan .pack(side="left")
# Frame Halaman ditaruh menggunakan .pack(side="right")
# Saat tombol ditekan, frame_lama.pack_forget(), frame_baru.pack(side="right")
'''))))
slides.append(build_slide(M6, 'm6-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Simulasi Login ke Dashboard</h2>
    <p class="mb-4"><b>Misi:</b> Bangun sistem Login dengan ganti halaman!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Buat Frame Login (Entry Username + Tombol Login).</li>
        <li>Buat Frame Dashboard (Label "Selamat Datang" + Tombol Logout).</li>
        <li>Jika user klik Login, <code>pack_forget()</code> Frame Login, dan tampilkan Frame Dashboard. Sebaliknya untuk Logout!</li>
    </ul>
    <p class="text-muted italic">Aplikasi ini adalah cikal bakal Final Project-mu! Tunjukkan ke instruktur.</p>
'''))

slides.append(build_slide(M6, 'm6-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Satu Aplikasi = <b>SATU ROOT (ctk.CTk)</b>.</li>
        <li>Untuk memunculkan halaman atau jendela baru, JANGAN gunakan <code>CTk()</code> lagi.</li>
        <li>Gunakan <b>Frame Switching</b> (sembunyikan & munculkan) untuk navigasi halaman yang mulus.</li>
        <li>Gunakan <b>CTkToplevel</b> untuk memunculkan pop-up / dialog peringatan terpisah.</li>
    </ul>
'''))
slides.append(build_slide(M6, 'm6-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Apa keuntungan menggunakan Frame (CTkFrame) yang dirubah menjadi Class sendiri?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Aplikasi kita jadi sangat rapi (Modular). Frame Login mengurus kodenya sendiri, Frame Dashboard mengurus kodenya sendiri. Jendela utama tugasnya cuma gonta-ganti layar!</p>
    </div>
'''))
slides.append(build_slide(M6, 'm6-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Bicara tentang Modular, kalau kode kita sudah mencapai ratusan baris, pasti satu file <code>.py</code> akan sangat penuh!</p>
    <p class="text-lg">Di pertemuan ke-8 kita akan belajar cara memecah file, tapi di pertemuan ke-7 besok kita pelajari dulu <b>Class Interaction</b> (bagaimana dua Object ngobrol satu sama lain)!</p>
'''))
slides.append(build_slide(M6, 'm6-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."</p>
        <p class="text-xl">— Martin Fowler</p>
    </div>
'''))

# Inject slides into existing deck.html
import sys
import os

try:
    with open("level4/deck.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # We find the insertion point: <!-- INJECT_SLIDES_HERE -->
    # Or append before closing </div> of #slide-data
    if "<!-- INJECT_SLIDES_HERE -->" in html:
        new_html = html.replace("<!-- INJECT_SLIDES_HERE -->", "\\n".join(slides) + "\\n        <!-- INJECT_SLIDES_HERE -->")
        with open("level4/deck.html", "w", encoding="utf-8") as f:
            f.write(new_html)
        print("Deck HTML successfully updated with Batch 2 (Meetings 4-6) content!")
    else:
        # Fallback if I removed the comment
        import re
        match = re.search(r'</div>\s*<script>', html)
        if match:
            parts = html.split(match.group(0))
            new_html = parts[0] + "\\n" + "\\n".join(slides) + "\\n" + match.group(0) + parts[1]
            with open("level4/deck.html", "w", encoding="utf-8") as f:
                f.write(new_html)
            print("Deck HTML successfully updated with Batch 2 (Meetings 4-6) content via regex!")
        else:
            print("ERROR: Could not find insertion point.")
except Exception as e:
    print("Error:", e)
