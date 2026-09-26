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

# ======================= MEETING 10: Core Build & Pitch Draft =======================
M10 = 10
slides.append(build_slide(M10, 'm10-s1', '1. Opening & Project Status', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 10! 🚀</h2>
    <p class="text-xl mb-4">Hari ini adalah Hari Koding! Waktunya membangun MVP aplikasimu.</p>
'''))
slides.append(build_slide(M10, 'm10-s1', '1. Opening & Project Status', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Status Check</h2>
    <p class="mb-4">Pastikan kamu sudah memiliki:</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Folder proyek khusus.</li>
        <li>Buku catatan / dokumen Blueprint dari minggu lalu.</li>
        <li>Tahu apa 3 Fitur Utama (MVP) yang akan dikerjakan hari ini.</li>
    </ul>
'''))
slides.append(build_slide(M10, 'm10-s2', '2. Build Plan & Checkpoints', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Strategi Membangun Aplikasi OOP</h2>
    <p class="mb-4 text-lg">Jangan menulis ratusan baris baru mencoba menjalankannya. Lakukan secara bertahap:</p>
    <ol class="list-decimal list-inside space-y-4 text-lg">
        <li><b>Checkpoint 1:</b> Kerangka Jendela Utama bisa terbuka (Tanpa error).</li>
        <li><b>Checkpoint 2:</b> Widget tampil di layar (Label, Tombol).</li>
        <li><b>Checkpoint 3:</b> Class Data (Model) terhubung dan bisa mem-print hasil di terminal.</li>
        <li><b>Checkpoint 4:</b> Hasil Data tampil kembali di Layar GUI!</li>
    </ol>
'''))
slides.append(build_slide(M10, 'm10-s2', '2. Build Plan & Checkpoints', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Starter Architecture (Modular)</h2>
    <p class="mb-4 text-lg">Buatlah struktur file ini di VS Code-mu:</p>
    <div class="bg-black/30 p-4 rounded font-mono text-sm border border-blue-500">
        <p>📁 MyProject_Namamu/</p>
        <p> ┣ 📄 model.py (Class untuk menyimpan & menghitung Data)</p>
        <p> ┣ 📄 view.py (Class untuk Frame/Toplevel CustomTkinter)</p>
        <p> ┗ 📄 main.py (File pusat yang menyatukan segalanya!)</p>
    </div>
'''))
slides.append(build_slide(M10, 'm10-s3', '3. Debugging Clinic', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Klinik Debugging (Level 4 Edition)</h2>
    <p class="mb-4 text-lg">Error adalah teman yang memberi petunjuk. Jangan panik!</p>
    <ul class="list-disc list-inside space-y-4 text-lg">
        <li><b>Error NameError/AttributeError:</b> Lupa <code>self.</code>? Atau lupa <code>import</code>?</li>
        <li><b>Error TypeError (takes 0 positional arguments):</b> Lupa <code>self</code> di dalam tanda kurung <code>def fungsi(self):</code>?</li>
        <li><b>GUI Hang / Crash:</b> Pastikan tidak ada <code>ctk.CTk()</code> ganda. Gunakan Frame atau Toplevel!</li>
    </ul>
'''))
slides.append(build_slide(M10, 'm10-s4', '4. Hands-on Core Build', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6 text-center">Fokus Koding! 💻</h2>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] text-center">
        <p class="text-xl mb-4 font-bold text-green-400">Target Hari Ini:</p>
        <p class="text-lg">Selesaikan Checkpoint 1 sampai 4.</p>
        <p class="text-md text-muted mt-4">Jangan pikirkan warna (UI) dulu. Fokus agar tombol bisa dipencet dan logikanya jalan (MVP)!</p>
    </div>
'''))
slides.append(build_slide(M10, 'm10-s5', '5. Elevator Pitch Draft', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Siapkan Katamu (Elevator Pitch)</h2>
    <p class="mb-4 text-lg">Setelah koding inti selesai, mari kita rancang kalimat pembukamu untuk presentasi nanti. (45-60 Detik!)</p>
    <p class="text-lg">Tulis draft ini di buku catatanmu:</p>
    <div class="bg-blue-900/40 p-4 rounded-xl border border-blue-500 mt-4 text-md italic">
        <p>"Halo semuanya! Pernahkah kalian merasa kesulitan saat [Sebutkan Masalah]? Saya juga! Oleh karena itu saya membuat [Nama Aplikasi], sebuah aplikasi yang bisa [Sebutkan 1 Fungsi Utama]."</p>
    </div>
'''))
slides.append(build_slide(M10, 'm10-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket</h2>
    <p class="text-xl mb-4">Tunjukkan hasil kerjamu (MVP) kepada instruktur, meskipun masih jelek atau belum diwarnai!</p>
'''))
slides.append(build_slide(M10, 'm10-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Make it work, make it right, make it fast."</p>
        <p class="text-xl">— Kent Beck</p>
    </div>
'''))


# ======================= MEETING 11: Integration & Testing =======================
M11 = 11
slides.append(build_slide(M11, 'm11-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 11! 🚀</h2>
    <p class="text-xl mb-4">Aplikasi kalian sudah bisa berjalan. Hari ini kita akan membuatnya <b>Sempurna</b>!</p>
'''))
slides.append(build_slide(M11, 'm11-s2', '2. UI Polish (Mempercantik Tampilan)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Waktunya Menghias! 🎨</h2>
    <p class="mb-4 text-lg">Karena fitur inti (MVP) sudah jadi, kamu boleh mulai mewarnai dan mengatur letak widget agar aplikasi terlihat profesional.</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Gunakan <code>fg_color</code>, <code>text_color</code>, atau <code>corner_radius</code> di CustomTkinter.</li>
        <li>Rapikan jarak menggunakan <code>pady</code> dan <code>padx</code> di dalam <code>.pack()</code> atau <code>.grid()</code>.</li>
    </ul>
'''))
slides.append(build_slide(M11, 'm11-s3', '3. Test Cases & QA', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">QA (Quality Assurance) Checklist</h2>
    <p class="mb-4 text-lg">Jadilah penguji (tester) untuk aplikasimu sendiri. Uji dengan cara seekstrim mungkin!</p>
    <ul class="list-disc list-inside space-y-4 text-lg">
        <li><b>Test 1:</b> Apa yang terjadi jika User tidak mengisi apa-apa di Entry tapi menekan tombol "Submit"? (Apakah Error atau muncul Pop-up peringatan?)</li>
        <li><b>Test 2:</b> Klik tombol secara beruntun 10 kali cepat. Apakah aplikasi hang?</li>
        <li><b>Test 3:</b> Coba ganti halaman lalu kembali lagi. Apakah data sebelumnya hilang?</li>
    </ul>
'''))
slides.append(build_slide(M11, 'm11-s4', '4. Presentation Preparation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Struktur Presentasi (PPT)</h2>
    <p class="mb-4 text-lg">Sambil menunggu teman yang belum selesai, siapkan slide presentasimu (Max 5-7 Slide):</p>
    <ol class="list-decimal list-inside space-y-2 text-lg">
        <li><b>Slide 1:</b> Judul & Perkenalan</li>
        <li><b>Slide 2:</b> Masalah (Problem)</li>
        <li><b>Slide 3:</b> Solusi (Demonstrasi Aplikasimu)</li>
        <li><b>Slide 4:</b> Di balik layar (Tunjukkan 1 class OOP favoritmu)</li>
        <li><b>Slide 5:</b> Tantangan yang dihadapi & Penutup</li>
    </ol>
'''))
slides.append(build_slide(M11, 'm11-s4', '4. Presentation Preparation', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Backup Plan (Rencana Darurat)</h2>
    <div class="bg-red-900/30 p-4 rounded-xl border border-red-500">
        <h3 class="font-bold text-red-400 mb-2">Hukum Murphy: "Jika sesuatu bisa salah, ia akan salah pada saat presentasi."</h3>
        <p class="text-lg">Siapkan <b>Screenshot</b> dan <b>Video Pendek</b> aplikasimu saat sedang berjalan normal. Jika besok komputermu tiba-tiba error saat live demo, kamu bisa memutar video tersebut!</p>
    </div>
'''))
slides.append(build_slide(M11, 'm11-s5', '5. Final Refinement', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6 text-center">Final Polish Time! 🛠️</h2>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] text-center">
        <p class="text-lg">Gunakan sisa waktu ini untuk menyelesaikan UI, mencoba QA, dan menyiapkan PPT & Backup Video.</p>
    </div>
'''))
slides.append(build_slide(M11, 'm11-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket</h2>
    <p class="text-xl mb-4">Pastikan aplikasimu 100% siap dijalankan dan kode program sudah tersimpan (save) dengan aman!</p>
'''))
slides.append(build_slide(M11, 'm11-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Quality means doing it right when no one is looking."</p>
        <p class="text-xl">— Henry Ford</p>
    </div>
'''))


# ======================= MEETING 12: Showcase =======================
M12 = 12
slides.append(build_slide(M12, 'm12-s1', '1. Final Check', '''
    <h2 class="text-5xl font-display font-bold text-yellow mb-6 text-center mt-10">Showcase Day! 🎉</h2>
    <p class="text-2xl mb-4 text-center">Inilah momen untuk memamerkan maha karyamu!</p>
'''))
slides.append(build_slide(M12, 'm12-s1', '1. Final Check', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Checklist Sebelum Tampil</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>✅ Aplikasi sudah terbuka di background (VS Code siap di-Run).</li>
        <li>✅ Slide presentasi sudah terbuka.</li>
        <li>✅ Tarik napas panjang. Kamu hebat!</li>
    </ul>
'''))
slides.append(build_slide(M12, 'm12-s2', '2. Presentation Guide', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Cara Menjelaskan Kode</h2>
    <p class="mb-4 text-lg">Jangan membaca kode baris per baris ("def spasi init self kurung..."). Penonton akan bosan!</p>
    <div class="bg-blue-900/30 p-4 rounded-xl border border-blue-500">
        <p class="font-bold text-blue-400 mb-2">Cara Profesional:</p>
        <p>"Aplikasi ini menggunakan pola OOP. Saya punya Class <code>Akun</code> untuk menyimpan saldo, dan saat saya klik tombol ini, GUI akan memanggil <code>tambah_saldo()</code> di Class tersebut. Ini membuat kodenya sangat rapi dan modular!"</p>
    </div>
'''))
slides.append(build_slide(M12, 'm12-s2', '2. Presentation Guide', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Live Demo Sequence & Q&A</h2>
    <ul class="list-disc list-inside space-y-4 text-lg">
        <li><b>Saat Demo:</b> Ceritakan skenario. ("Bayangkan saya adalah seorang guru yang ingin mengisi nilai...").</li>
        <li><b>Saat Q&A (Tanya Jawab):</b> Dengarkan pertanyaan dengan baik.</li>
        <li>Jika tidak tahu jawabannya, katakan: <i>"Pertanyaan yang bagus. Saya belum mengimplementasikan itu, tapi mungkin saya akan mencoba memakai konsep Inheritance untuk membuatnya nanti!"</i></li>
    </ul>
'''))
slides.append(build_slide(M12, 'm12-s3', '3. Audience Etiquette', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Etika Penonton</h2>
    <p class="mb-4 text-lg">Saat temanmu presentasi:</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Perhatikan ke depan.</li>
        <li>Beri tepuk tangan yang meriah.</li>
        <li>Beri pertanyaan yang membangun, bukan menjatuhkan. ("Wah UI-nya bagus! Bagaimana cara kamu membuat tombolnya melengkung?")</li>
    </ul>
'''))
slides.append(build_slide(M12, 'm12-s4', '4. Showcase Time!', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <div class="text-8xl mb-6">🎤</div>
        <h2 class="text-5xl font-display font-bold text-yellow mb-6">Panggung Milik Kalian!</h2>
        <p class="text-2xl text-muted">Guru akan memanggil nama kalian satu per satu.</p>
    </div>
'''))
slides.append(build_slide(M12, 'm12-s5', '5. Reflection & Celebration', '''
    <h2 class="text-5xl font-display font-bold text-yellow mb-6 text-center mt-10">Selamat! 🎓</h2>
    <p class="text-2xl mb-4 text-center">Kalian telah resmi menguasai Object-Oriented Programming (OOP)!</p>
    <p class="text-xl text-center text-muted">Kalian kini menulis kode layaknya Programmer Senior di Industri Teknologi.</p>
'''))
slides.append(build_slide(M12, 'm12-s5', '5. Reflection & Celebration', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Final Quote of the Level</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Programs must be written for people to read, and only incidentally for machines to execute."</p>
        <p class="text-xl">— Harold Abelson</p>
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
        print("Deck HTML successfully updated with Batch 4 (Meetings 10-12) content via regex!")
    else:
        print("ERROR: Could not find insertion point.")
except Exception as e:
    print("Error:", e)
