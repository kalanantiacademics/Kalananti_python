import json

def get_base_html():
    return """<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Level 4 - Planet Visionara</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800&family=Space+Grotesk:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: { 
                        sans: ['Space Grotesk', 'system-ui', 'sans-serif'], 
                        display: ['Orbitron', 'system-ui', 'sans-serif'] 
                    },
                    colors: {
                        'k-blue': '#265E9B',
                        'k-blue-d': '#1A4576',
                        'k-yellow': '#F9C013',
                        'k-green': '#339D9D',
                    }
                }
            }
        }
    </script>
    <style>
        :root {
            --font-sans: 'Space Grotesk', system-ui, -apple-system, sans-serif;
            --font-display: 'Orbitron', system-ui, -apple-system, sans-serif;
            --bg-dark: #06101f;
            --bg-darker: #040a14;
            --bg-card: rgba(14, 30, 60, 0.95);
            --border-card: rgba(140, 190, 255, 0.2);
            --text-main: #ffffff;
            --text-muted: #94a3b8;
            --accent-yellow: #F9C013;
            --accent-blue: #265E9B;
            --accent-green: #339D9D;
        }

        body {
            font-family: var(--font-sans);
            background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-darker) 100%);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .hidden { display: none !important; }
        
        #top-nav {
            background: rgba(6, 14, 30, 0.95);
            border-bottom: 1px solid var(--border-card);
            backdrop-filter: blur(10px);
            padding: 0.75rem 1.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 50;
        }
        .nav-controls { display: flex; gap: 1rem; align-items: center; }
        select.nav-dropdown {
            background-color: #0f172a;
            color: white;
            border: 1px solid var(--border-card);
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: 600;
            cursor: pointer;
            outline: none;
        }
        select.nav-dropdown:focus { border-color: var(--accent-yellow); }
        
        .btn-nav {
            background-color: var(--accent-blue);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            font-weight: bold;
            cursor: pointer;
            transition: opacity 0.2s;
        }
        .btn-nav:hover { opacity: 0.8; }
        .btn-nav:disabled { opacity: 0.5; cursor: not-allowed; }

        #main-area {
            flex: 1;
            position: relative;
            overflow-y: auto;
            overflow-x: hidden;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding: 2rem 1rem;
        }

        .slide-wrapper {
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 1rem;
            width: 100%;
            max-width: 1100px;
            min-height: 600px;
            padding: 3rem;
            box-shadow: 0 20px 40px rgba(0,0,0,0.5);
            animation: slideIn 0.3s ease-out forwards;
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        h1, h2, h3, .font-display { font-family: var(--font-display); }
        .text-yellow { color: var(--accent-yellow); }
        .text-muted { color: var(--text-muted); }

        .k-reveal {
            margin-top: 1.5rem;
            border: 1px solid var(--border-card);
            border-radius: 0.75rem;
            overflow: hidden;
            background: rgba(0,0,0,0.2);
        }
        .k-reveal-btn {
            width: 100%;
            padding: 1rem;
            background: rgba(255,255,255,0.05);
            color: white;
            border: none;
            text-align: left;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .k-reveal-btn:hover { background: rgba(255,255,255,0.1); }
        .k-reveal-content {
            padding: 1.5rem;
            display: none;
            border-top: 1px solid var(--border-card);
        }
        .k-reveal.is-open .k-reveal-content { display: block; }
        .k-reveal.is-open .k-reveal-btn .icon { transform: rotate(180deg); }

        .k-code {
            background: #0f172a;
            padding: 1rem;
            border-radius: 0.5rem;
            font-family: monospace;
            overflow-x: auto;
            border: 1px solid #334155;
            color: #e2e8f0;
            margin: 1rem 0;
            white-space: pre-wrap;
        }

        .k-quiz-option {
            display: block;
            width: 100%;
            padding: 1rem;
            margin-bottom: 0.5rem;
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border-card);
            border-radius: 0.5rem;
            color: white;
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
        }
        .k-quiz-option:hover { background: rgba(255,255,255,0.1); }
        .k-quiz-option.correct { background: rgba(34, 197, 94, 0.2); border-color: #22c55e; }
        .k-quiz-option.wrong { background: rgba(239, 68, 68, 0.2); border-color: #ef4444; }
        .k-quiz-feedback { margin-top: 1rem; padding: 1rem; border-radius: 0.5rem; display: none; }
    </style>
</head>
<body>
    <header id="top-nav">
        <div class="nav-controls">
            <h1 class="text-xl font-display font-bold text-yellow hidden md:block">🚀 Level 4: Visionara</h1>
            <select id="meeting-selector" class="nav-dropdown">
                <option value="1">Meeting 1: Class & Object</option>
                <option value="2">Meeting 2: Attributes & Methods</option>
                <option value="3">Meeting 3: Constructor (__init__)</option>
                <option value="4">Meeting 4: OOP in CustomTkinter</option>
                <option value="5">Meeting 5: Inheritance</option>
                <option value="6">Meeting 6: Multi-window Navigation</option>
                <option value="7">Meeting 7: Class Interaction</option>
                <option value="8">Meeting 8: Modular Coding</option>
                <option value="9">Meeting 9: Ideation & Planning</option>
                <option value="10">Meeting 10: Core Build</option>
                <option value="11">Meeting 11: Integration & Testing</option>
                <option value="12">Meeting 12: Showcase</option>
            </select>
        </div>
        <div class="nav-controls flex-1 max-w-xl mx-4">
            <select id="section-selector" class="nav-dropdown w-full"></select>
        </div>
        <div class="nav-controls">
            <button id="btn-prev" class="btn-nav">&larr; Prev</button>
            <span id="slide-counter" class="font-mono font-bold text-sm">1 / 1</span>
            <button id="btn-next" class="btn-nav" style="background-color: var(--accent-yellow); color: black;">Next &rarr;</button>
        </div>
    </header>

    <main id="main-area">
        <div id="slide-container" class="w-full flex justify-center"></div>
    </main>

    <div id="slide-data" class="hidden">
        <!-- INJECT_SLIDES_HERE -->
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            let currentMeeting = '1';
            let slides = [];
            let currentSlideIndex = 0;
            
            const slideDataContainer = document.getElementById('slide-data');
            const slideContainer = document.getElementById('slide-container');
            const meetingSelector = document.getElementById('meeting-selector');
            const sectionSelector = document.getElementById('section-selector');
            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
            const slideCounter = document.getElementById('slide-counter');
            const mainArea = document.getElementById('main-area');

            function loadMeeting(meetingId) {
                const activeSlide = slideContainer.querySelector('.slide-wrapper');
                if (activeSlide) slideDataContainer.appendChild(activeSlide);
                
                currentMeeting = meetingId;
                slides = Array.from(slideDataContainer.querySelectorAll(`.raw-slide[data-meeting="${meetingId}"]`));
                
                if (slides.length === 0) {
                    const fallback = document.createElement('div');
                    fallback.className = 'raw-slide slide-wrapper';
                    fallback.dataset.meeting = meetingId;
                    fallback.dataset.sectionId = 'fallback';
                    fallback.dataset.sectionLabel = 'Work in Progress';
                    fallback.innerHTML = `<h2 class="text-3xl font-bold text-yellow text-center mt-20">Meeting ${meetingId} is under construction! 🚧</h2>`;
                    slides = [fallback];
                } else {
                    slides.forEach(s => s.classList.add('slide-wrapper'));
                }

                buildSectionDropdown();
                goToSlide(0);
            }

            function buildSectionDropdown() {
                sectionSelector.innerHTML = '';
                const sections = new Map();
                
                slides.forEach((slide, index) => {
                    const secId = slide.dataset.sectionId;
                    const secLabel = slide.dataset.sectionLabel;
                    if (secId && secLabel && !sections.has(secId)) {
                        sections.set(secId, { label: secLabel, index: index });
                    }
                });

                sections.forEach((data, id) => {
                    const option = document.createElement('option');
                    option.value = id;
                    option.dataset.index = data.index;
                    option.textContent = data.label;
                    sectionSelector.appendChild(option);
                });
            }

            function goToSlide(index) {
                if (index < 0 || index >= slides.length) return;
                
                const activeSlide = slideContainer.querySelector('.slide-wrapper');
                if (activeSlide) slideDataContainer.appendChild(activeSlide);

                currentSlideIndex = index;
                const newSlide = slides[currentSlideIndex];
                
                slideContainer.appendChild(newSlide);
                mainArea.scrollTop = 0;

                slideCounter.textContent = `${currentSlideIndex + 1} / ${slides.length}`;
                btnPrev.disabled = currentSlideIndex === 0;
                btnNext.disabled = currentSlideIndex === slides.length - 1;

                const activeSecId = newSlide.dataset.sectionId;
                if (activeSecId && sectionSelector.value !== activeSecId) {
                    sectionSelector.value = activeSecId;
                }
                
                initInteractions(newSlide);
            }

            function initInteractions(slideElement) {
                const reveals = slideElement.querySelectorAll('.k-reveal:not(.initialized)');
                reveals.forEach(reveal => {
                    reveal.classList.add('initialized');
                    const btn = reveal.querySelector('.k-reveal-btn');
                    btn.addEventListener('click', () => {
                        reveal.classList.toggle('is-open');
                        btn.setAttribute('aria-expanded', reveal.classList.contains('is-open'));
                    });
                });

                const quizOptions = slideElement.querySelectorAll('.k-quiz-option:not(.initialized)');
                quizOptions.forEach(opt => {
                    opt.classList.add('initialized');
                    opt.addEventListener('click', (e) => {
                        const isCorrect = opt.dataset.correct === "true";
                        const parent = opt.parentElement;
                        parent.querySelectorAll('.k-quiz-option').forEach(o => {
                            o.classList.remove('correct', 'wrong');
                        });
                        opt.classList.add(isCorrect ? 'correct' : 'wrong');
                        
                        const feedback = parent.querySelector('.k-quiz-feedback');
                        if (feedback) {
                            feedback.style.display = 'block';
                            feedback.innerHTML = isCorrect ? '✅ Tepat sekali!' : '❌ Coba lagi!';
                            feedback.className = `k-quiz-feedback ${isCorrect ? 'bg-green-900/50 text-green-200' : 'bg-red-900/50 text-red-200'} font-bold`;
                        }
                    });
                });
            }

            btnPrev.addEventListener('click', () => goToSlide(currentSlideIndex - 1));
            btnNext.addEventListener('click', () => goToSlide(currentSlideIndex + 1));
            meetingSelector.addEventListener('change', (e) => loadMeeting(e.target.value));
            sectionSelector.addEventListener('change', (e) => {
                const selectedOption = e.target.options[e.target.selectedIndex];
                const targetIndex = parseInt(selectedOption.dataset.index, 10);
                if (!isNaN(targetIndex)) goToSlide(targetIndex);
            });

            document.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight') goToSlide(currentSlideIndex + 1);
                if (e.key === 'ArrowLeft') goToSlide(currentSlideIndex - 1);
            });

            let touchStartX = 0;
            let touchEndX = 0;
            mainArea.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; }, {passive: true});
            mainArea.addEventListener('touchend', e => { 
                touchEndX = e.changedTouches[0].screenX; 
                const swipeThreshold = 50;
                if (touchEndX < touchStartX - swipeThreshold) goToSlide(currentSlideIndex + 1);
                if (touchEndX > touchStartX + swipeThreshold) goToSlide(currentSlideIndex - 1);
            }, {passive: true});

            loadMeeting('1');
        });
    </script>
</body>
</html>"""

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
        opts_html += f'<button class="k-quiz-option" data-correct="{is_correct}">{opt}</button>\n'
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

# ======================= MEETING 1: Class & Object =======================
M1 = 1

# Section: Opening & Review (Level 3 GUI concepts) - 6 slides
slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Selamat Datang di Planet Visionara! 🚀</h2>
    <p class="text-xl mb-4">Di Level 4 ini, kita akan menjadi Arsitek Kode sejati.</p>
    <p class="text-lg text-muted">Sebelum kita mulai perjalanan kita belajar <b>Object-Oriented Programming (OOP)</b>, mari kita review sebentar apa yang kita pelajari di Level 3.</p>
'''))

slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review: CustomTkinter Window</h2>
    <p class="mb-4">Bagaimana cara kita membuat jendela utama aplikasi di CustomTkinter?</p>
''' + get_quiz("Pilih baris kode yang benar untuk membuat window:", [
    "app = ctk.CTk()",
    "app = Tkinter.Window()",
    "app = create_window()"
], 0)))

slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review: CustomTkinter Button</h2>
    <p class="mb-4">Apa fungsi argumen <code>command</code> pada CTkButton?</p>
''' + get_quiz("Pilih jawaban yang benar:", [
    "Untuk mengubah warna tombol",
    "Untuk menghubungkan tombol dengan fungsi logika (Event Handling)",
    "Untuk menampilkan tulisan di dalam tombol"
], 1)))

slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review: Entry Widget</h2>
    <p class="mb-4">Bagaimana cara kita mengambil data teks yang diketik user di CTkEntry?</p>
''' + get_quiz("Pilih method yang tepat:", [
    "entry.get()",
    "entry.read()",
    "entry.fetch()"
], 0)))

slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review: Layout Management</h2>
    <p class="mb-4">Perintah apa yang digunakan untuk menyusun posisi widget di CustomTkinter?</p>
''' + get_quiz("Pilih jawaban yang benar:", [
    "Hanya .pack()",
    "Hanya .grid()",
    ".pack() dan .grid()"
], 2)))

slides.append(build_slide(M1, 'm1-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review Selesai! 🎉</h2>
    <p class="text-lg">Kalian sudah siap untuk level berikutnya!</p>
    <p class="text-lg mt-4">Di Level 3, kode kita kadang menjadi sangat panjang dan sulit diatur. Di Level 4, kita akan belajar cara "merapikan" dan menstrukturkan kode layaknya profesional menggunakan <b>OOP</b>.</p>
'''))

# Section: Learning Objectives
slides.append(build_slide(M1, 'm1-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menjelaskan perbedaan pemrograman biasa dengan <b>Object-Oriented Programming (OOP)</b>.</li>
        <li>Mampu mendefinisikan <b>Class</b> (Blueprint) tanpa terjadi <code>SyntaxError</code>.</li>
        <li>Mampu membuat <b>Object</b> (Hasil Jadi) dari sebuah Class dan mencetaknya.</li>
    </ul>
'''))

# Section: Objective 1 - OOP Concept
slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu OOP?</h2>
    <p class="mb-4 text-lg"><b>Object-Oriented Programming (OOP)</b> adalah cara menulis kode yang berfokus pada pembuatan "Benda" (Objek).</p>
    <p class="mb-4 text-lg">Alih-alih menulis instruksi dari atas ke bawah (prosedural), kita mendesain kode dengan membuat cetak biru dari benda-benda yang ada di dunia nyata, lalu membuat benda nyata dari cetak biru tersebut.</p>
'''))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Komputer Bekerja</h2>
    <div class="flex items-center gap-8 bg-[#0a1830] p-6 rounded-xl">
        <div class="flex-1 text-center">
            <div class="text-6xl mb-4">📜</div>
            <p class="font-bold">Blueprint (Cetak Biru)</p>
            <p class="text-sm text-muted">Disimpan di memori sebagai desain.</p>
        </div>
        <div class="text-4xl text-yellow">➡️</div>
        <div class="flex-1 text-center">
            <div class="text-6xl mb-4">🏠 🏠 🏠</div>
            <p class="font-bold">Banyak Objek (Rumah)</p>
            <p class="text-sm text-muted">Dibuat menggunakan desain yang sama.</p>
        </div>
    </div>
'''))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan kamu memiliki <b>Cetakan Kue (Cookie Cutter)</b>.</p>
    <ul class="list-disc list-inside space-y-2 text-lg mb-6">
        <li><b>Cetakan Kue</b> adalah <b>Class</b> (Cetak Biru). Cetakan itu sendiri tidak bisa dimakan.</li>
        <li><b>Kue yang sudah dicetak</b> adalah <b>Object</b> (Hasil Jadi). Kamu bisa memakannya, menambahkan topping berbeda, dan membuatnya berkali-kali!</li>
    </ul>
    <p class="text-lg">Dengan 1 Cetakan Kue, kita bisa membuat 100 Kue dengan cepat!</p>
'''))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Mendefinisikan Class</h2>
    <p class="mb-4">Di Python, kita menggunakan keyword <code>class</code> untuk membuat cetak biru.</p>
''' + get_code('''
# Ini adalah Class (Cetakan)
class Kucing:
    pass  # pass artinya "kosongkan dulu"
''') + '''
    <p class="mt-4">Kata kunci <code>pass</code> berguna agar Python tidak error meskipun class-nya belum memiliki isi.</p>
'''))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Membuat Object</h2>
    <p class="mb-4">Setelah Class dibuat, kita bisa mencetak objeknya dengan memanggil nama Class diikuti tanda kurung <code>()</code>.</p>
''' + get_code('''
class Kucing:
    pass

# Membuat Object dari Class Kucing
kucing_oren = Kucing()
kucing_hitam = Kucing()

print(kucing_oren)
''') + get_reveal("Tampilkan Hasil / Output", "<p>Outputnya akan terlihat seperti memori lokasi:</p><br><code>&lt;__main__.Kucing object at 0x7fa2b3...&gt;</code><br><p>Ini artinya objek sukses dibuat dan disimpan di memori komputer!</p>")))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
    <p class="mb-4 text-lg">Apa yang terjadi jika kita menjalankan kode ini?</p>
''' + get_code('''
class Mobil:
    pass

mobil_bapak = mobil()
''') + get_quiz("Pilih jawaban yang benar:", [
    "Bisa berjalan dengan normal.",
    "Error: NameError karena nama Class harus sama persis (huruf besar 'Mobil').",
    "SyntaxError karena 'pass' tidak boleh dipakai."
], 1)))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Gunakan format <b>PascalCase</b> untuk nama Class. Setiap awalan kata pakai huruf kapital, tanpa spasi/underscore.</p>
            <br>
            <p>Contoh: <code>MobilSport</code>, <code>RobotKalananti</code></p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan gunakan format snake_case atau huruf kecil semua untuk nama Class.</p>
            <br>
            <p>Contoh Salah: <code>mobil_sport</code>, <code>robot</code></p>
        </div>
    </div>
'''))

slides.append(build_slide(M1, 'm1-s3', '3. Konsep Dasar OOP', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika error saat membuat class atau objek, ikuti langkah ini:</p>
    <ol class="list-decimal list-inside space-y-2 text-lg">
        <li>Cek <b>titik dua <code>:</code></b> di akhir definisi class.</li>
        <li>Cek apakah indentasi (spasi menjorok) sudah benar.</li>
        <li>Pastikan memanggil class dengan huruf kapital yang sama persis.</li>
        <li>Pastikan pakai tanda kurung <code>()</code> saat membuat object! <code>mobil1 = Mobil()</code>, BUKAN <code>mobil1 = Mobil</code>.</li>
    </ol>
'''))

slides.append(build_slide(M1, 'm1-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Cetakan Kosong</h2>
    <p class="mb-4">Buatlah sebuah Class bernama <code>Robot</code> yang kosong menggunakan <code>pass</code>.</p>
''' + get_reveal("Tampilkan Jawaban (Bahas Bersama Guru)", get_code('''
class Robot:
    pass
'''))))

slides.append(build_slide(M1, 'm1-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Mencetak Objek</h2>
    <p class="mb-4">Gunakan Class <code>Robot</code> dari latihan sebelumnya, lalu buat dua objek berbeda: <code>robot1</code> dan <code>robot2</code>.</p>
''' + get_reveal("Tampilkan Jawaban (Bahas Bersama Guru)", get_code('''
class Robot:
    pass

robot1 = Robot()
robot2 = Robot()
'''))))

slides.append(build_slide(M1, 'm1-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Menampilkan Memori</h2>
    <p class="mb-4">Gunakan perintah <code>print()</code> untuk menampilkan <code>robot1</code> dan <code>robot2</code>. Apakah lokasinya sama?</p>
''' + get_reveal("Tampilkan Jawaban (Bahas Bersama Guru)", get_code('''
print(robot1)
print(robot2)

# Lokasinya akan berbeda, membuktikan mereka adalah objek yang terpisah!
'''))))

slides.append(build_slide(M1, 'm1-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
    <p class="mb-4">Temukan error pada kode di bawah ini:</p>
''' + get_code('''
class buku:
pass

buku_saya = buku
''') + get_reveal("Tampilkan Solusi Bug", '''
<ol class="list-decimal list-inside space-y-2">
    <li>Nama class sebaiknya pakai PascalCase: <code>Buku</code></li>
    <li>Lupa indentasi sebelum <code>pass</code></li>
    <li>Lupa tanda kurung saat membuat objek: <code>Buku()</code></li>
</ol>
''')))

slides.append(build_slide(M1, 'm1-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Pesawat Luar Angkasa</h2>
    <p class="mb-4">Buatlah Class bernama <code>Pesawat</code>, lalu buat objek <code>apollo</code> dan <code>voyager</code> dari Class tersebut, dan cetak keduanya ke layar!</p>
    <p class="text-muted">Ketik jawabanmu di VS Code atau Python Runner!</p>
''' + get_reveal("Hint / Petunjuk", "<p>Ingat gunakan <code>class Pesawat:</code> dengan pass di dalamnya. Jangan lupa tanda kurung saat membuat objek!</p>")))

# Section: Integrated Practice
slides.append(build_slide(M1, 'm1-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Gudang Sekolah</h2>
    <p class="mb-4">Kita ingin membuat sistem inventory gudang sekolah. Buat Class <code>Barang</code>. Lalu buat objek <code>kursi</code>, <code>meja</code>, dan <code>papan_tulis</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Barang:
    pass

kursi = Barang()
meja = Barang()
papan_tulis = Barang()
'''))))

slides.append(build_slide(M1, 'm1-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Sistem Akun Bank</h2>
    <p class="mb-4">Buatlah Class <code>AkunBank</code>. Buat objek <code>akun_ayah</code> dan <code>akun_ibu</code>, lalu print ke layar.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class AkunBank:
    pass

akun_ayah = AkunBank()
akun_ibu = AkunBank()
print(akun_ayah)
print(akun_ibu)
'''))))

slides.append(build_slide(M1, 'm1-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Menu Cafe</h2>
    <p class="mb-4">Buat Class <code>MenuCafe</code>. Buat tiga objek menu (misal: kopi, teh, roti), lalu print semuanya!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class MenuCafe:
    pass

kopi = MenuCafe()
teh = MenuCafe()
roti = MenuCafe()

print(kopi, teh, roti)
'''))))

slides.append(build_slide(M1, 'm1-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Kebun Binatang</h2>
    <p class="mb-4"><b>Misi:</b> Bangun kerangka sistem Kebun Binatang! 🦁</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Buat Class bernama <code>Hewan</code>.</li>
        <li>Buat Class bernama <code>Kandang</code>.</li>
        <li>Buat 2 objek hewan: <code>singa</code> dan <code>jerapah</code>.</li>
        <li>Buat 2 objek kandang: <code>kandang_1</code> dan <code>kandang_2</code>.</li>
        <li>Print keempat objek tersebut.</li>
    </ul>
    <p class="text-muted italic">Tidak ada jawaban yang disediakan. Ayo tunjukkan kodemu ke gurumu!</p>
'''))

# Section: Closing
slides.append(build_slide(M1, 'm1-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li><b>OOP</b> sangat berguna untuk menstrukturkan kode agar rapi layaknya dunia nyata.</li>
        <li><b>Class</b> adalah blueprint atau cetakan. Keyword: <code>class</code>. Namanya menggunakan <b>PascalCase</b>.</li>
        <li><b>Object</b> adalah hasil nyata dari Class. Cara membuatnya: <code>nama_variabel = NamaClass()</code>.</li>
        <li>Dua objek dari class yang sama akan memiliki lokasi memori yang berbeda.</li>
    </ul>
'''))

slides.append(build_slide(M1, 'm1-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Diskusikan dengan teman atau gurumu:</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155]">
        <p class="text-lg italic">"Jika Class adalah cetakan kue, dan Object adalah kue hasil cetakan. Bisakah kita membuat kue rasa coklat dan rasa stroberi dari cetakan yang sama?"</p>
        <p class="text-md mt-4 text-muted">Hint: Kita akan mempelajarinya di pertemuan selanjutnya!</p>
    </div>
'''))

slides.append(build_slide(M1, 'm1-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Hari ini cetakan kita masih kosong. Di pertemuan berikutnya, kita akan mengisi objek kita dengan <b>Attributes</b> (sifat) dan <b>Methods</b> (kemampuan aksi)!</p>
    <p class="text-lg">Bersiaplah membuat objek yang bisa berbuat sesuatu!</p>
'''))

slides.append(build_slide(M1, 'm1-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Talk is cheap. Show me the code."</p>
        <p class="text-xl">— Linus Torvalds, Creator of Linux</p>
    </div>
'''))


# ======================= MEETING 2: Attributes & Methods =======================
M2 = 2

# ... (I will implement Meeting 2 and Meeting 3 logic identically using the syllabus.)
# For the sake of not hitting token limits with string building in one script, I'll build M2 and M3.

slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 2! 🚀</h2>
    <p class="text-xl mb-4">Mari kita review apa yang kita pelajari di pertemuan sebelumnya tentang Class dan Object!</p>
'''))
slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Apa sebutan untuk "Blueprint" atau "Cetak Biru" dalam OOP?</p>
''' + get_quiz("Pilih jawaban yang benar:", ["Object", "Class", "Function"], 1)))
slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Format penamaan apa yang digunakan untuk membuat nama Class di Python?</p>
''' + get_quiz("Pilih jawaban yang benar:", ["camelCase", "snake_case", "PascalCase"], 2)))
slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Manakah kode yang BENAR untuk membuat class kosong?</p>
''' + get_quiz("Pilih kode yang benar:", [
    "class Robot:<br>&nbsp;&nbsp;&nbsp;&nbsp;pass", 
    "class robot<br>&nbsp;&nbsp;&nbsp;&nbsp;pass", 
    "Class Robot:<br>&nbsp;&nbsp;&nbsp;&nbsp;pass"
], 0)))
slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Bagaimana cara mencetak / membuat object dari Class Mobil?</p>
''' + get_quiz("Pilih baris yang benar:", ["mobil1 = Mobil()", "mobil1 = Mobil", "mobil1 = new Mobil()"], 0)))
slides.append(build_slide(M2, 'm2-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Jika kita print dua objek berbeda dari Class yang sama, apakah hasil lokasi memorinya sama?</p>
''' + get_quiz("Pilih jawaban yang benar:", ["Ya, karena dari cetakan yang sama", "Tidak, setiap objek memiliki lokasi memori unik"], 1)))

slides.append(build_slide(M2, 'm2-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu mendefinisikan <b>Attributes</b> (karakteristik/sifat) ke dalam sebuah Object.</li>
        <li>Mampu membuat <b>Methods</b> (aksi/kemampuan) di dalam Class.</li>
        <li>Mampu memanggil Attributes dan Methods menggunakan notasi titik (dot notation).</li>
    </ul>
'''))

slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu Attributes?</h2>
    <p class="mb-4 text-lg"><b>Attributes</b> adalah variabel yang menempel pada sebuah Object. Mereka mewakili <b>sifat</b> atau <b>karakteristik</b> dari objek tersebut.</p>
    <p class="text-lg">Contoh: Seekor kucing memiliki sifat: nama, warna, dan umur.</p>
'''))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu Methods?</h2>
    <p class="mb-4 text-lg"><b>Methods</b> adalah fungsi yang menempel pada sebuah Class. Mereka mewakili <b>aksi</b> atau <b>kemampuan</b> yang bisa dilakukan objek.</p>
    <p class="text-lg">Contoh: Seekor kucing bisa melakukan aksi: makan(), tidur(), dan mengeong().</p>
'''))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Komputer Bekerja</h2>
    <div class="grid grid-cols-2 gap-6 bg-[#0a1830] p-6 rounded-xl">
        <div>
            <h3 class="font-bold text-blue-400 mb-2">Object (Mobil)</h3>
            <ul class="list-disc list-inside">
                <li>Attribute (Data)</li>
                <li>Method (Action)</li>
            </ul>
        </div>
        <div>
            <h3 class="font-bold text-yellow mb-2">Contoh Nyata</h3>
            <ul class="list-disc list-inside text-sm">
                <li>warna = "Merah", merk = "Toyota"</li>
                <li>maju(), rem(), belok()</li>
            </ul>
        </div>
    </div>
'''))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan kamu bermain Game RPG.</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li><b>Karakter (Object)</b>: Kesatria.</li>
        <li><b>Attributes</b>: Health = 100, Damage = 50. (Status)</li>
        <li><b>Methods</b>: serang(), berlindung(). (Skill / Gerakan)</li>
    </ul>
'''))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Attributes (Dot Notation)</h2>
    <p class="mb-4">Kita menempelkan dan mengambil data atribut menggunakan <b>titik (dot)</b>.</p>
''' + get_code('''
class Kucing:
    pass

kucing1 = Kucing()
kucing1.nama = "Milo"   # Menambahkan Attribute nama
kucing1.warna = "Oren"  # Menambahkan Attribute warna

print(kucing1.nama)     # Mengakses Attribute
''')))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Methods dan parameter `self`</h2>
    <p class="mb-4">Membuat method sama seperti membuat fungsi (<code>def</code>) di dalam class, tapi WAJIB memiliki parameter pertama bernama <code>self</code>.</p>
''' + get_code('''
class Kucing:
    def mengeong(self):  # 'self' merujuk pada objek itu sendiri
        print("Meow!")

kucing1 = Kucing()
kucing1.mengeong()  # Output: Meow!
''')))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
class Robot:
    def sapa(self):
        print("Halo Manusia!")

robot_canggih = Robot()
robot_canggih.sapa
''') + get_quiz("Apa yang terjadi pada kode di atas?", [
    "Akan mencetak 'Halo Manusia!'",
    "Tidak terjadi apa-apa karena kurang tanda kurung () saat memanggil method.",
    "Akan Error."
], 1)))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Selalu tulis <code>self</code> sebagai argumen pertama saat membuat Method di dalam class.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan lupa tanda <code>()</code> saat memanggil method. <code>objek.method()</code></p>
        </div>
    </div>
'''))
slides.append(build_slide(M2, 'm2-s3', '3. Attributes & Methods', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika method error TypeError "takes 0 positional arguments but 1 was given":</p>
    <p><b>Solusi:</b> Kamu lupa menambahkan parameter <code>self</code> di definisi fungsi dalam class!</p>
    <p>Python otomatis mengirim objek itu sendiri (self) saat kita memanggil method, jadi tempatnya harus disiapkan.</p>
'''))

slides.append(build_slide(M2, 'm2-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Atribut Sederhana</h2>
    <p class="mb-4">Buat Class <code>Player</code> kosong. Buat objek <code>player1</code>, berikan atribut <code>username</code> dan <code>level</code>. Print datanya.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Player:
    pass

player1 = Player()
player1.username = "KingPro"
player1.level = 10

print("Player:", player1.username, "| Level:", player1.level)
'''))))
slides.append(build_slide(M2, 'm2-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Method Sederhana</h2>
    <p class="mb-4">Buat Class <code>Burung</code>. Tambahkan method <code>terbang(self)</code> yang mencetak "Mengepakkan sayap!". Panggil method tersebut.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Burung:
    def terbang(self):
        print("Mengepakkan sayap!")

pipit = Burung()
pipit.terbang()
'''))))
slides.append(build_slide(M2, 'm2-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Method & Atribut (Self)</h2>
    <p class="mb-4">Bagaimana method mengakses atribut objeknya sendiri? Gunakan <code>self.atribut</code> di dalam method!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Anjing:
    def menggonggong(self):
        # self.nama mengambil atribut nama dari objek ini
        print(f"{self.nama} bilang: Guk Guk!")

doggy = Anjing()
doggy.nama = "Heli"
doggy.menggonggong()
'''))))
slides.append(build_slide(M2, 'm2-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class Mobil:
    def klakson():
        print("Din Din!")

m = Mobil()
m.klakson()
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Error TypeError! Kurang argumen <code>self</code> pada method <code>klakson</code>.</p>
<p>Benar: <code>def klakson(self):</code></p>
''')))
slides.append(build_slide(M2, 'm2-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Hero Game</h2>
    <p class="mb-4">Buat Class <code>Hero</code> dengan method <code>serang(self)</code>. Buat objek, beri atribut <code>nama</code>, lalu print dan jalankan serang().</p>
''' + get_reveal("Hint / Petunjuk", "<p>Ingat tambahkan atribut pakai titik, lalu di dalam method serang gunakan print yang menyertakan <code>self.nama</code>.</p>")))

slides.append(build_slide(M2, 'm2-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Kalkulator Objek</h2>
    <p class="mb-4">Buat Class <code>Kalkulator</code> dengan method <code>tambah(self, a, b)</code> yang mem-print hasil tambah.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Kalkulator:
    def tambah(self, a, b):
        print("Hasil:", a + b)

calc = Kalkulator()
calc.tambah(10, 5)
'''))))
slides.append(build_slide(M2, 'm2-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Sistem Kasir</h2>
    <p class="mb-4">Buat Class <code>Kasir</code>. Method <code>bayar(self, total, uang)</code>. Print kembaliannya!</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Kasir:
    def bayar(self, total, uang):
        kembalian = uang - total
        print("Kembalian:", kembalian)

mesin = Kasir()
mesin.bayar(50000, 100000)
'''))))
slides.append(build_slide(M2, 'm2-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Akun Media Sosial</h2>
    <p class="mb-4">Class <code>Akun</code> punya atribut <code>followers</code> (integer). Method <code>tambah_follower(self)</code> menambah angkanya 1.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Akun:
    def tambah_follower(self):
        self.followers += 1
        print("Followers sekarang:", self.followers)

user1 = Akun()
user1.followers = 100
user1.tambah_follower()
user1.tambah_follower()
'''))))
slides.append(build_slide(M2, 'm2-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Tamagotchi</h2>
    <p class="mb-4"><b>Misi:</b> Buat pet virtual-mu!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Buat Class <code>Pet</code>.</li>
        <li>Buat objek, beri atribut <code>nama</code> dan <code>lapar</code> = 10.</li>
        <li>Buat method <code>makan(self)</code> yang mengurangi lapar sebanyak 2 dan mem-print status lapar.</li>
        <li>Panggil method <code>makan()</code> dua kali!</li>
    </ul>
    <p class="text-muted italic">Tidak ada jawaban yang disediakan. Ayo tunjukkan kodemu ke gurumu!</p>
'''))

slides.append(build_slide(M2, 'm2-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li><b>Attributes</b> = Variabel/Sifat objek. Aksesnya dengan <code>objek.atribut</code>.</li>
        <li><b>Methods</b> = Fungsi/Aksi objek. Panggilnya dengan <code>objek.method()</code>.</li>
        <li>Metode selalu butuh parameter <b><code>self</code></b> agar bisa merujuk pada dirinya sendiri (objek yang memanggil).</li>
    </ul>
'''))
slides.append(build_slide(M2, 'm2-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Kenapa kita butuh kata `self` di dalam fungsi yang ada di dalam Class?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Jawab: Agar fungsi tahu atribut objek mana yang sedang dimanipulasi, karena bisa ada banyak objek dari Class yang sama.</p>
    </div>
'''))
slides.append(build_slide(M2, 'm2-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Menambahkan atribut satu per satu setelah membuat objek ternyata merepotkan ya? <code>user.nama = "A"</code> lalu <code>user.umur = 10</code>.</p>
    <p class="text-lg">Di pertemuan berikutnya, kita akan belajar "Constructor", cara instan mengisi data langsung saat objek diciptakan!</p>
'''))
slides.append(build_slide(M2, 'm2-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"Simplicity is the soul of efficiency."</p>
        <p class="text-xl">— Austin Freeman</p>
    </div>
'''))

# ======================= MEETING 3: Constructor (__init__) =======================
M3 = 3
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-4xl font-display font-bold text-yellow mb-6">Welcome to Meeting 3! 🚀</h2>
    <p class="text-xl mb-4">Mari kita review Attributes & Methods dari pertemuan sebelumnya!</p>
'''))
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 1</h2>
    <p class="mb-4">Atribut merupakan _________ dari sebuah Class.</p>
''' + get_quiz("Pilih jawaban:", ["Aksi / Tindakan", "Sifat / Data"], 1)))
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 2</h2>
    <p class="mb-4">Tanda apa yang digunakan untuk mengakses Method atau Attribute (Notasi)?</p>
''' + get_quiz("Pilih jawaban:", ["Koma (,)", "Titik dua (:)", "Titik (.)"], 2)))
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 3</h2>
    <p class="mb-4">Apa nama parameter wajib pertama di dalam sebuah Method?</p>
''' + get_quiz("Pilih jawaban:", ["this", "self", "obj"], 1)))
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 4</h2>
    <p class="mb-4">Bagaimana cara yang benar memanggil method <code>maju</code> pada objek <code>mobil1</code>?</p>
''' + get_quiz("Pilih jawaban:", ["mobil1.maju()", "mobil1.maju", "maju(mobil1)"], 0)))
slides.append(build_slide(M3, 'm3-s1', '1. Opening & Review', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Review 5</h2>
    <p class="mb-4">Jika kita punya Method <code>def rem(self):</code>, apakah kita perlu memasukkan nilai untuk <code>self</code> saat memanggilnya <code>mobil.rem()</code>?</p>
''' + get_quiz("Pilih jawaban:", ["Ya, harus mobil.rem(self)", "Tidak, Python otomatis memasukkan objeknya ke self"], 1)))

slides.append(build_slide(M3, 'm3-s2', '2. Learning Objectives', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Learning Objectives 🎯</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li>Mampu menjelaskan fungsi <b>Constructor (`__init__`)</b> pada Python.</li>
        <li>Mampu menggunakan <code>__init__</code> untuk menginisialisasi atribut awal secara otomatis saat objek dibuat.</li>
        <li>Mampu membuat objek dengan memberikan data secara langsung melalui argumen.</li>
    </ul>
'''))

slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Apa itu Constructor?</h2>
    <p class="mb-4 text-lg"><b>Constructor</b> adalah fungsi spesial yang akan <b>Otomatis Berjalan</b> tepat pada saat sebuah objek diciptakan pertama kali.</p>
    <p class="text-lg">Fungsinya untuk menyiapkan data awal (Attributes) agar kita tidak perlu menuliskannya satu-satu lagi dari luar.</p>
'''))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Visual Model: Pabrik Mobil</h2>
    <div class="bg-[#0a1830] p-6 rounded-xl flex items-center justify-between text-center">
        <div>
            <div class="text-4xl mb-2">📋</div>
            <p class="font-bold">Tanpa Constructor</p>
            <p class="text-sm">Beli mobil polosan, lalu cat sendiri di rumah.</p>
        </div>
        <div class="text-4xl">➡️</div>
        <div>
            <div class="text-4xl mb-2">🏭</div>
            <p class="font-bold">Dengan Constructor</p>
            <p class="text-sm">Pesan mobil dari pabrik, langsung minta cat warna merah. Mobil datang sudah siap!</p>
        </div>
    </div>
'''))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Analogi Sehari-hari</h2>
    <p class="mb-4 text-lg">Bayangkan membuat akun baru di game.</p>
    <ul class="list-disc list-inside space-y-2 text-lg">
        <li>Constructor adalah halaman <b>"Create Character"</b>.</li>
        <li>Saat kamu klik "Start", gamenya memanggil Constructor untuk mengatur HP awal, Nama karaktermu, dan Senjata bawaanmu sekaligus!</li>
    </ul>
'''))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Code: Menggunakan `__init__`</h2>
    <p class="mb-4">Di Python, nama method constructor SELALU <code>__init__</code> (dua underscore sebelum dan sesudah kata init).</p>
''' + get_code('''
class Kucing:
    # Constructor
    def __init__(self, nama_kucing, warna_kucing):
        # Memasang data ke dalam Atribut
        self.nama = nama_kucing
        self.warna = warna_kucing

# Membuat objek dan langsung mengirim datanya
kucing1 = Kucing("Milo", "Oren")
kucing2 = Kucing("Luna", "Hitam")

print(kucing1.nama) # Milo
''')))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Predict Before Running! 🧠</h2>
''' + get_code('''
class Sepeda:
    def __init__(self, merk):
        self.merk = merk

sepeda1 = Sepeda()
''') + get_quiz("Apa yang terjadi pada kode di atas?", [
    "Error TypeError: __init__() missing 1 required positional argument: 'merk'",
    "Berjalan normal, merk otomatis kosong.",
    "Bukan error, tapi merk isinya None."
], 0)))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Tips & Do's / Don'ts</h2>
    <div class="grid grid-cols-2 gap-6">
        <div class="bg-green-900/30 p-4 rounded-lg border border-green-700">
            <h3 class="font-bold text-green-400 mb-2">DO (Lakukan) ✅</h3>
            <p>Gunakan format <code>__init__(self, ...):</code> dengan dua underscore (dunder). Dunder singkatan dari Double Underscore.</p>
        </div>
        <div class="bg-red-900/30 p-4 rounded-lg border border-red-700">
            <h3 class="font-bold text-red-400 mb-2">DON'T (Jangan) ❌</h3>
            <p>Jangan menulis <code>_init_</code> (satu underscore). Fungsi tidak akan berjalan otomatis sebagai constructor.</p>
        </div>
    </div>
'''))
slides.append(build_slide(M3, 'm3-s3', '3. Constructor (__init__)', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Debugging Routine 🕵️‍♂️</h2>
    <p class="mb-4 text-lg">Jika menemui Error: <code>__init__() missing arguments</code></p>
    <p><b>Solusi:</b> Berarti kamu mewajibkan Class menerima data (misal: nama) saat objek dibuat, tapi kamu memanggilnya kosong seperti <code>Kucing()</code>.</p>
    <p>Pastikan argumennya diisi: <code>Kucing("Milo")</code>.</p>
'''))

slides.append(build_slide(M3, 'm3-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 1: Init Sederhana</h2>
    <p class="mb-4">Buat Class <code>Player</code> dengan <code>__init__(self, nama)</code>. Setup <code>self.nama = nama</code>. Lalu cetak <code>player1 = Player("Budi")</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Player:
    def __init__(self, nama):
        self.nama = nama

player1 = Player("Budi")
print(player1.nama)
'''))))
slides.append(build_slide(M3, 'm3-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 2: Default Value</h2>
    <p class="mb-4">Di <code>__init__</code>, kita juga bisa set nilai bawaan lho! Buat Class <code>Monster</code> yang otomatis punya atribut <code>hp = 100</code> meski tidak diminta.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Monster:
    def __init__(self, nama):
        self.nama = nama
        self.hp = 100  # Nilai default tanpa argumen tambahan

goblin = Monster("Goblin Ijo")
print(f"Monster: {goblin.nama}, HP: {goblin.hp}")
'''))))
slides.append(build_slide(M3, 'm3-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Exercise 3: Init & Methods Gabungan</h2>
    <p class="mb-4">Buat method <code>info(self)</code> pada Class <code>Monster</code> yang menampilkan kalimat gabungan menggunakan datanya.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Monster:
    def __init__(self, nama):
        self.nama = nama
        self.hp = 100

    def info(self):
        print(f"Awas! {self.nama} punya darah {self.hp} HP!")

boss = Monster("Raja Iblis")
boss.info()
'''))))
slides.append(build_slide(M3, 'm3-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Bug Hunt! 🐛</h2>
''' + get_code('''
class Robot:
    def _init_(self, nama):
        self.nama = nama

bot = Robot("Wall-E")
''') + get_reveal("Tampilkan Solusi Bug", '''
<p>Error TypeError: Robot() takes no arguments.</p>
<p>Penyebab: Constructor menggunakan 1 underscore (<code>_init_</code>), bukan dunder (<code>__init__</code>). Python menganggapnya fungsi biasa, bukan constructor otomatis!</p>
''')))
slides.append(build_slide(M3, 'm3-s4', '4. Guided & Independent Practice', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Exercise: Karyawan Perusahaan</h2>
    <p class="mb-4">Buat Class <code>Karyawan</code>. Gunakan <code>__init__</code> untuk menerima argumen <code>nama</code> dan <code>gaji</code>. Buat objek karyawan, lalu print nama dan gajinya.</p>
''' + get_reveal("Hint / Petunjuk", "<p><code>def __init__(self, nama, gaji):</code> lalu masukkan ke <code>self.nama</code> dan <code>self.gaji</code>.</p>")))

slides.append(build_slide(M3, 'm3-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 1: Akun Belanja</h2>
    <p class="mb-4">Buat Class <code>User</code>. Constructor meminta <code>username</code>. Set otomatis <code>keranjang = []</code>. Print keranjangnya.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class User:
    def __init__(self, username):
        self.username = username
        self.keranjang = []  # Inisialisasi list kosong

pembeli = User("Siska")
print(pembeli.username, "Keranjang:", pembeli.keranjang)
'''))))
slides.append(build_slide(M3, 'm3-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 2: Tambah ke Keranjang</h2>
    <p class="mb-4">Dari Mini Project 1, tambahkan method <code>tambah_barang(self, barang)</code> untuk memasukkan data ke list keranjang menggunakan <code>.append()</code>.</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class User:
    def __init__(self, username):
        self.username = username
        self.keranjang = []

    def tambah_barang(self, barang):
        self.keranjang.append(barang)

pembeli = User("Siska")
pembeli.tambah_barang("Buku")
pembeli.tambah_barang("Pulpen")
print("Keranjang Siska:", pembeli.keranjang)
'''))))
slides.append(build_slide(M3, 'm3-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Guided Mini-Project 3: Database Siswa List-of-Objects</h2>
    <p class="mb-4">Buat list kosong. Masukkan 3 objek Class <code>Siswa(nama, nilai)</code> ke dalamnya dengan loop ringan atau manual. Menarik bukan?</p>
''' + get_reveal("Tampilkan Jawaban", get_code('''
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

database_kelas = [
    Siswa("Andi", 80),
    Siswa("Budi", 95),
    Siswa("Caca", 88)
]

for s in database_kelas:
    print(f"Siswa: {s.nama} | Nilai: {s.nilai}")
'''))))
slides.append(build_slide(M3, 'm3-s5', '5. Integrated Mini-Projects', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Independent Mini-Project: Sistem Bank Sederhana</h2>
    <p class="mb-4"><b>Misi:</b> Gabungkan seluruh pelajaran OOP dasar kita!</p>
    <ul class="list-disc list-inside space-y-2 mb-4">
        <li>Class <code>AkunBank</code> (terinspirasi Final Project!).</li>
        <li><code>__init__(self, nama, saldo_awal)</code>.</li>
        <li>Method <code>setor(self, jumlah)</code> yang menambah saldo.</li>
        <li>Buat objek, setor uang, lalu print saldo akhirnya.</li>
    </ul>
    <p class="text-muted italic">Tidak ada jawaban yang disediakan. Ayo tunjukkan kodemu ke gurumu!</p>
'''))

slides.append(build_slide(M3, 'm3-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Summary & Key Takeaways</h2>
    <ul class="list-disc list-inside space-y-4 text-xl">
        <li><b>Constructor (<code>__init__</code>)</b> berjalan otomatis saat objek diciptakan.</li>
        <li>Fungsinya untuk "setup awal", mengisi objek dengan atribut bawaan atau data dari argumen.</li>
        <li>Sangat penting menulisnya dengan double underscore!</li>
        <li>List bisa menyimpan banyak Objek, berguna untuk membuat Database sederhana!</li>
    </ul>
'''))
slides.append(build_slide(M3, 'm3-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Exit Ticket / Reflection</h2>
    <p class="text-xl mb-4">Dalam pembuatan game, apa keuntungan menggunakan Constructor <code>__init__</code> dibanding memberikan atribut manual satu-per-satu?</p>
    <div class="bg-[#0f172a] p-6 rounded-xl border border-[#334155] mt-4">
        <p class="text-lg italic text-muted">Mencegah bug "Atribut belum ada"! Semua karakter dipastikan langsung punya stat HP dan Attack sejak mereka "lahir".</p>
    </div>
'''))
slides.append(build_slide(M3, 'm3-s6', '6. Closing', '''
    <h2 class="text-3xl font-display font-bold text-yellow mb-6">Next Meeting Preview 🚀</h2>
    <p class="text-xl mb-4">Sekarang kamu sudah jago membuat struktur OOP murni. Bagaimana kalau kita terapkan di aplikasi nyata?</p>
    <p class="text-lg">Di pertemuan berikutnya, kita akan menggunakan CustomTkinter dengan pola OOP. Tidak ada lagi kode berantakan!</p>
'''))
slides.append(build_slide(M3, 'm3-s6', '6. Closing', '''
    <div class="h-full flex flex-col justify-center items-center text-center">
        <h2 class="text-2xl font-bold text-muted mb-4 uppercase tracking-widest">Quote of the Day</h2>
        <p class="text-4xl font-display font-bold text-yellow italic mb-6">"First, solve the problem. Then, write the code."</p>
        <p class="text-xl">— John Johnson</p>
    </div>
'''))

# ======================= GENERATE HTML =======================

output_html = get_base_html().replace("<!-- INJECT_SLIDES_HERE -->", "\\n".join(slides))
with open("level4/deck.html", "w", encoding="utf-8") as f:
    f.write(output_html)

print("Deck HTML successfully generated with Batch 1 (Meetings 1-3) content!")
