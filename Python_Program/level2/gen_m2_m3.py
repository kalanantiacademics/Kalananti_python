# -*- coding: utf-8 -*-
"""Streamlined Meetings 2 and 3 for Level 2"""

def get_m2_slides():
    from streamline_all_m2_m9 import build_meeting_2
    return build_meeting_2()

def get_m3_slides():
    return [
        {
            "title": "Meeting 3: String Manipulation 🔤",
            "subtitle": "Seni Mengolah & Memproses Teks di Planet Modula",
            "content": """<div class="text-center space-y-6 max-w-3xl mx-auto">
    <div class="text-7xl mb-4 animate-bounce">🪓</div>
    <div class="inline-block px-4 py-1.5 rounded-full bg-blue-100 text-blue-800 dark:bg-blue-900/50 dark:text-blue-300 font-bold text-xs uppercase tracking-widest border border-blue-200 dark:border-blue-700">Python Level 2 • Sesi 3</div>
    <h3 class="text-3xl font-extrabold text-slate-800 dark:text-white">Selamat Datang di Dunia Manipulasi Teks!</h3>
    <p class="text-lg text-slate-600 dark:text-slate-300 leading-relaxed">
        Di dunia nyata, input dari pengguna seringkali berantakan: ada huruf besar-kecil yang tidak beraturan, spasi berlebih, atau kata-kata yang harus disensor. Hari ini kita akan menjadi <b>Master Editor Teks</b> dengan method sakti pemroses String!
    </p>
    <div class="p-4 bg-blue-50 dark:bg-slate-800/80 rounded-2xl border border-blue-200 dark:border-slate-700 text-sm font-semibold text-blue-900 dark:text-blue-200">
        🎯 Target Hari Ini: Menguasai <b>Text Casing</b> (<code>.upper()</code>, <code>.lower()</code>), <b>Split & Join</b>, <b>Strip</b>, dan <b>Replace</b>!
    </div>
</div>"""
        },
        {
            "title": "Objectives & Roadmap Sesi 3 🎯",
            "subtitle": "Target Penguasaan String Hari Ini",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <ul class="space-y-3">
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-blue-500/20 text-blue-500 font-bold flex items-center justify-center shrink-0">1</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">String sebagai Sekuens Karakter & Slicing</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memahami bahwa String di Python diperlakukan seperti List huruf yang memiliki index dan bisa diiris.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-indigo-500/20 text-indigo-500 font-bold flex items-center justify-center shrink-0">2</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Standarisasi Format Teks (upper, lower, title)</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Menyeragamkan input user agar perbandingan logika <code>if-else</code> tidak pernah meleset.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-amber-500/20 text-amber-500 font-bold flex items-center justify-center shrink-0">3</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Operasi Pisah & Sambung (.split() dan .join())</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Memecah kalimat menjadi list kata, dan menyambungkan kembali list menjadi satu kalimat rapi.</p>
            </div>
        </li>
        <li class="flex items-start gap-4 p-3.5 rounded-2xl bg-white/5 border border-white/10">
            <span class="w-8 h-8 rounded-xl bg-green-500/20 text-green-500 font-bold flex items-center justify-center shrink-0">4</span>
            <div>
                <b class="text-slate-800 dark:text-white text-base">Pembersihan & Sensor (.strip() dan .replace())</b>
                <p class="text-sm text-slate-500 dark:text-slate-400 mt-0.5">Membangun Bot Chat Filter dan sistem sanitasi data nomor telepon / akun.</p>
            </div>
        </li>
    </ul>
</div>"""
        },
        {
            "title": "Speed Review: Sesi 2 Challenge ⚡",
            "subtitle": "Uji Ingatan Kilat Dictionary",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <p class="text-center text-slate-600 dark:text-slate-300 text-sm font-semibold">Tebak output kode Dictionary berikut sebelum mulai:</p>
    <div class="grid md:grid-cols-3 gap-3 text-xs">
        <div class="p-4 rounded-2xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700 space-y-2">
            <b class="text-blue-800 dark:text-blue-300 text-sm">1. Akses Key</b>
            <div class="bg-black/30 p-2 rounded font-mono text-cyan-400">cadet = {"id": 101}<br>print(cadet["id"])</div>
            <p class="text-slate-500">Output: <code>101</code> (Langsung panggil label kuncinya).</p>
        </div>
        <div class="p-4 rounded-2xl bg-indigo-50 dark:bg-slate-800 border border-indigo-200 dark:border-slate-700 space-y-2">
            <b class="text-indigo-800 dark:text-indigo-300 text-sm">2. Akses Aman .get()</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">cadet.get("rank", "Cadet")</div>
            <p class="text-slate-500">Output: <code>"Cadet"</code> (Mencegah crash KeyError).</p>
        </div>
        <div class="p-4 rounded-2xl bg-amber-50 dark:bg-slate-800 border border-amber-200 dark:border-slate-700 space-y-2">
            <b class="text-amber-800 dark:text-amber-300 text-sm">3. Ekstrak .keys()</b>
            <div class="bg-black/30 p-2 rounded font-mono text-amber-300">print(list(cadet.keys()))</div>
            <p class="text-slate-500">Output: <code>['id']</code> (Hanya label pengenal).</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "String adalah Sekuens Karakter! 🧩",
            "subtitle": "Karakter, Spasi, dan Tanda Baca Memiliki Index",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">kata = "PYTHON"</div>
        <div class="grid grid-cols-6 gap-2 text-center text-xs mt-3">
            <div class="p-2 bg-slate-800 rounded border border-slate-700">P<br><span class="text-green-400">[0]</span></div>
            <div class="p-2 bg-slate-800 rounded border border-slate-700">Y<br><span class="text-green-400">[1]</span></div>
            <div class="p-2 bg-slate-800 rounded border border-slate-700">T<br><span class="text-green-400">[2]</span></div>
            <div class="p-2 bg-slate-800 rounded border border-slate-700">H<br><span class="text-green-400">[3]</span></div>
            <div class="p-2 bg-slate-800 rounded border border-slate-700">O<br><span class="text-green-400">[4]</span></div>
            <div class="p-2 bg-slate-800 rounded border border-slate-700">N<br><span class="text-green-400">[5]</span></div>
        </div>
        <div class="text-amber-400 mt-3">print(kata[0:3]) # Output: "PYT"</div>
        <div class="text-amber-400">print(kata[-1])  # Output: "N"</div>
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        💡 <b>Aturan Emas:</b> Slicing pada String menggunakan rumus yang sama persis dengan List: <code>[start : stop : step]</code>.
    </div>
</div>"""
        },
        {
            "title": "Text Casing: Mengubah Ukuran Huruf 🔠",
            "subtitle": ".upper(), .lower(), .title(), dan .capitalize()",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">pesan = "Halo Modula Explorer"</div>
        <div class="text-slate-300">1. print(pesan.upper())      <span class="text-green-400"># "HALO MODULA EXPLORER"</span></div>
        <div class="text-slate-300">2. print(pesan.lower())      <span class="text-green-400"># "halo modula explorer"</span></div>
        <div class="text-slate-300">3. print(pesan.title())      <span class="text-green-400"># "Halo Modula Explorer"</span></div>
        <div class="text-slate-300">4. print(pesan.capitalize()) <span class="text-green-400"># "Halo modula explorer"</span></div>
    </div>
    <div class="p-3 bg-green-50 dark:bg-slate-800 rounded-xl border border-green-200 dark:border-slate-700 text-xs">
        🛡️ <b>Kasus Nyata (Sanitasi Input):</b><br>
        <code>jawaban = input("Ingin lanjut? (y/n): ").lower()</code><br>
        Jika user mengetik <code>"Y"</code>, <code>"y"</code>, atau <code>" Y "</code>, program tetap mengenali jawabannya dengan benar!
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Membersihkan Input User 👨‍🏫",
            "subtitle": "Ketik Bersama Guru di Editor Python",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Program Pengecek Password & Role</span><br>
        role = input("Masukkan role kamu (admin/cadet): ").strip().lower()<br><br>
        if role == "admin":<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print("Selamat datang di Ruang Kendali Utama 🚀")<br>
        elif role == "cadet":<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print("Selamat datang di Simulator Latihan 🎮")<br>
        else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;print("Akses Ditolak: Role tidak dikenal ❌")
    </div>
    <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700 text-xs">
        💡 <b>Perhatikan Method Chaining:</b> <code>.strip().lower()</code> membuang spasi di awal/akhir sekaligus mengubah semua huruf menjadi kecil dalam 1 baris!
    </div>
</div>"""
        },
        {
            "title": "Operasi Potong & Sambung: .split() & .join() ✂️",
            "subtitle": "Mengubah String Menjadi List dan Sebaliknya",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-cyan-300 block">1. .split(pemisah) -> List</b>
            <div class="text-slate-400">kalimat = "apel,jeruk,mangga"</div>
            <div class="text-yellow-400">buah = kalimat.split(",")</div>
            <div class="text-green-400">print(buah)</div>
            <div class="text-slate-400"># Output: ['apel', 'jeruk', 'mangga']</div>
            <p class="text-slate-400 text-[11px] mt-1">Memotong teks berdasarkan koma atau spasi menjadi List terpisah.</p>
        </div>
        <div class="p-4 bg-slate-900 rounded-2xl border border-slate-700 font-mono text-xs text-white space-y-2">
            <b class="text-amber-300 block">2. lem.join(list) -> String</b>
            <div class="text-slate-400">kata = ["Python", "Kalananti", "Pro"]</div>
            <div class="text-yellow-400">gabung = " - ".join(kata)</div>
            <div class="text-green-400">print(gabung)</div>
            <div class="text-slate-400"># Output: "Python - Kalananti - Pro"</div>
            <p class="text-slate-400 text-[11px] mt-1">Menyatukan elemen List menjadi satu string dengan karakter lem di antaranya.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Membersihkan Debu: .strip() 🧹",
            "subtitle": "Mencukur Spasi Jahat di Awal dan Akhir Teks",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">username = "   BudiCyber99    "</div>
        <div class="text-yellow-400">bersih = username.strip()</div>
        <div class="text-green-400">print(f"Hasil: '{bersih}'") # Hasil: 'BudiCyber99'</div>
    </div>
    <div class="grid grid-cols-2 gap-3 text-xs">
        <div class="p-3 bg-blue-50 dark:bg-slate-800 rounded-xl border border-blue-200 dark:border-slate-700">
            <b class="text-blue-700 dark:text-blue-300">.lstrip()</b>
            <p class="text-slate-500 mt-0.5">Hanya membuang spasi di sisi <b>Kiri (Left)</b>.</p>
        </div>
        <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700">
            <b class="text-purple-700 dark:text-purple-300">.rstrip()</b>
            <p class="text-slate-500 mt-0.5">Hanya membuang spasi di sisi <b>Kanan (Right)</b>.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Mencari & Mengganti: .replace() 🔄",
            "subtitle": "Tukar Guling Kata Tertentu Secara Otomatis",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">pesan = "Kucing itu sangat nakal, kucing itu lari!"</div>
        <div class="text-yellow-400">sensor = pesan.replace("nakal", "lucu")</div>
        <div class="text-green-400">print(sensor)</div>
        <div class="text-slate-400"># Output: "Kucing itu sangat lucu, kucing itu lari!"</div>
    </div>
    <div class="p-3 bg-amber-50 dark:bg-slate-800 rounded-xl border border-amber-200 dark:border-slate-700 text-xs">
        💡 <b>Penting:</b> <code>.replace(lama, baru)</code> mengganti <b>SEMUA</b> kemunculan kata lama di seluruh teks, kecuali kita menambahkan batas hitungan ketiga: <code>.replace(lama, baru, 1)</code>.
    </div>
</div>"""
        },
        {
            "title": "Guided Exercise: Bot Sensor Kata Terlarang 🤖",
            "subtitle": "Membangun Filter Chat Mini Otomatis",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-green-400 leading-relaxed border border-slate-700">
        <span class="text-slate-500"># Sistem Filter Chat Game</span><br>
        kata_terlarang = ["bodoh", "curang", "jelek"]<br>
        chat = input("Tulis pesan chat kamu: ")<br><br>
        for kata in kata_terlarang:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;if kata in chat.lower():<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bintang = "*" * len(kata)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chat = chat.replace(kata, bintang)<br><br>
        print("Pesan terkirim:", chat)
    </div>
    <div class="p-3 bg-purple-50 dark:bg-slate-800 rounded-xl border border-purple-200 dark:border-slate-700 text-xs">
        🎯 <b>Kunci Logika:</b> <code>"*" * len(kata)</code> otomatis membuat bintang sebanyak jumlah huruf kata terlarang!
    </div>
</div>"""
        },
        {
            "title": "Detektif Bug: String Immutability Trap 🐛",
            "subtitle": "String Tidak Bisa Diubah Langsung Seperti List!",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="grid md:grid-cols-2 gap-4">
        <div class="p-4 rounded-2xl bg-red-50 dark:bg-slate-800 border border-red-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-red-700 dark:text-red-400 text-sm">🚨 Jebakan TypeError:</b>
            <div class="bg-black/30 p-2 rounded font-mono text-red-400">
                nama = "Budi"<br>
                nama[0] = "D" # ERROR!<br>
                # TypeError: 'str' does not support assignment
            </div>
            <p class="text-slate-500">String di Python bersifat <b>Immutable</b> (tidak bisa diubah per huruf).</p>
        </div>
        <div class="p-4 rounded-2xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700 text-xs space-y-2">
            <b class="text-green-700 dark:text-green-400 text-sm">✅ Solusi Benar:</b>
            <div class="bg-black/30 p-2 rounded font-mono text-green-400">
                nama = "Budi"<br>
                nama_baru = "D" + nama[1:]<br>
                print(nama_baru) # "Dudi"
            </div>
            <p class="text-slate-500">Buat string baru dengan menggabungkan potongan (slicing) atau pakai <code>.replace()</code>.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Exercise 2: Independent (Pembersih Nomor HP) 💻",
            "subtitle": "Tantangan Mandiri Tingkat Pemula",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10 space-y-3">
        <div class="inline-block px-3 py-1 rounded bg-blue-500/20 text-blue-400 font-bold text-xs uppercase">Mission Brief</div>
        <h4 class="text-lg font-bold text-slate-800 dark:text-white">Normalisasi Kontak Internasional</h4>
        <p class="text-sm text-slate-600 dark:text-slate-300">
            Pengguna sering memasukkan nomor HP dengan format berbeda: <code>"0812-3456-7890"</code> atau <code>" 0812 3456 7890 "</code>.
        </p>
        <ul class="text-xs space-y-1.5 text-slate-500 list-disc list-inside">
            <li>Hapus semua spasi di depan dan belakang dengan <code>.strip()</code>.</li>
            <li>Hapus tanda strip <code>-</code> dan spasi di tengah dengan <code>.replace()</code>.</li>
            <li>Jika nomor diawali dengan <code>"08"</code>, ubah menjadi kode negara <code>"+628"</code>!</li>
        </ul>
    </div>
</div>"""
        },
        {
            "title": "⚠️ CHALLENGE MODE: Ujian Manipulasi Teks ⚠️",
            "subtitle": "Pilih 1 dari 3 Tantangan Kode Nyata Berikut",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-center">
    <div class="text-6xl animate-bounce">🏆</div>
    <h3 class="text-2xl font-bold text-slate-800 dark:text-white">Uji Nyali Editor Teks Cyber!</h3>
    <div class="grid grid-cols-3 gap-3 text-left text-xs">
        <div class="p-4 rounded-xl bg-green-50 dark:bg-slate-800 border border-green-200 dark:border-slate-700">
            <span class="text-xl">🕵️‍♂️</span>
            <b class="block mt-1 text-green-700 dark:text-green-300 font-bold">Challenge 1: Sandi Agen</b>
            <p class="text-slate-500 mt-1">Balik kata dan tukar huruf vokal menjadi angka rahasia.</p>
        </div>
        <div class="p-4 rounded-xl bg-blue-50 dark:bg-slate-800 border border-blue-200 dark:border-slate-700">
            <span class="text-xl">📰</span>
            <b class="block mt-1 text-blue-700 dark:text-blue-300 font-bold">Challenge 2: Editor Berita</b>
            <p class="text-slate-500 mt-1">Ubah judul berita menjadi format slug URL web yang bersih.</p>
        </div>
        <div class="p-4 rounded-xl bg-purple-50 dark:bg-slate-800 border border-purple-200 dark:border-slate-700">
            <span class="text-xl">🤖</span>
            <b class="block mt-1 text-purple-700 dark:text-purple-300 font-bold">Challenge 3: Analisis Teks</b>
            <p class="text-slate-500 mt-1">Hitung jumlah kata, karakter unik, dan frekuensi kata spesifik.</p>
        </div>
    </div>
</div>"""
        },
        {
            "title": "Challenge 1: Sandi Rahasia Agen 🕵️‍♂️",
            "subtitle": "Enkripsi Pesan Menggunakan Metode String Berantai",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">pesan = input("Masukkan pesan rahasia: ")</div>
        <div class="text-slate-400"># Aturan sandi: a->4, e->3, i->1, o->0, s->5</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Gunakan <code>.lower()</code> pada pesan input.</li>
            <li>Ganti huruf vokal menjadi angka sesuai aturan dengan <code>.replace()</code> berantai.</li>
            <li>Balikkan susunan teks dengan slicing mundur <code>[::-1]</code>!</li>
            <li>Cetak kode rahasia yang sudah terenkripsi.</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 2: Generator URL Slug Web 📰",
            "subtitle": "Mengubah Judul Artikel Menjadi Alamat Web SEO Friendly",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">judul = "  Belajar Python Pemula di Kalananti 2026!  "</div>
        <div class="text-green-400"># Target Slug: "belajar-python-pemula-di-kalananti-2026"</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Bersihkan spasi ujung dengan <code>.strip()</code> dan ubah ke huruf kecil dengan <code>.lower()</code>.</li>
            <li>Hapus tanda seru <code>!</code> dan tanda baca lain dengan <code>.replace()</code>.</li>
            <li>Pecah kalimat menjadi list kata dengan <code>.split()</code>.</li>
            <li>Satukan kembali menggunakan lem tanda strip <code>"-"</code> via <code>"-".join(kata)</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Challenge 3: Robot Analisis Teks 🤖",
            "subtitle": "Statistik Panjang, Kata Kunci, dan Hitung Karakter",
            "content": """<div class="max-w-3xl mx-auto space-y-4 text-left">
    <div class="p-4 bg-slate-900 rounded-2xl font-mono text-xs text-white border border-slate-700 space-y-2">
        <div class="text-cyan-300">paragraf = "Python adalah bahasa yang hebat. Belajar Python sangat menyenangkan."</div>
    </div>
    <div class="p-4 rounded-2xl bg-white/5 border border-white/10 text-xs space-y-2">
        <b>Instruksi Misi:</b>
        <ol class="list-decimal list-inside space-y-1 text-slate-400">
            <li>Hitung total karakter dengan <code>len(paragraf)</code>.</li>
            <li>Hitung total kata dengan memecahnya via <code>.split()</code> lalu cek panjang list-nya.</li>
            <li>Hitung berapa kali kata "python" muncul menggunakan <code>.lower().count("python")</code>!</li>
        </ol>
    </div>
</div>"""
        },
        {
            "title": "Summary & Cheat Sheet Sesi 3 📝",
            "subtitle": "Rangkuman Method Pemroses Teks",
            "content": """<div class="max-w-3xl mx-auto space-y-3 text-left">
    <div class="overflow-x-auto">
        <table class="w-full text-xs text-left text-slate-600 dark:text-slate-300 border-collapse">
            <thead>
                <tr class="border-b border-slate-200 dark:border-slate-700 font-bold text-slate-800 dark:text-white">
                    <th class="py-2">Method</th>
                    <th class="py-2">Fungsi</th>
                    <th class="py-2">Contoh Hasil</th>
                </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-[11px]">
                <tr>
                    <td class="py-1.5 text-cyan-400">.upper() / .lower()</td>
                    <td>Ubah semua ke huruf besar / kecil</td>
                    <td><code>"hi".upper() -> "HI"</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-green-400">.strip()</td>
                    <td>Buang spasi liar di tepi kiri & kanan</td>
                    <td><code>" a ".strip() -> "a"</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-yellow-400">.split(x)</td>
                    <td>Potong string menjadi List</td>
                    <td><code>"a,b".split(",") -> ['a','b']</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-purple-400">x.join(list)</td>
                    <td>Satukan List menjadi String</td>
                    <td><code>"-".join(['a','b']) -> "a-b"</code></td>
                </tr>
                <tr>
                    <td class="py-1.5 text-pink-400">.replace(a, b)</td>
                    <td>Ganti kata lama menjadi baru</td>
                    <td><code>"cat".replace("c","b") -> "bat"</code></td>
                </tr>
            </tbody>
        </table>
    </div>
</div>"""
        },
        {
            "title": "Refleksi & Quote of the Day 🌟",
            "subtitle": "Selamat, Kamu Telah Menguasai String Processing!",
            "content": """<div class="text-center space-y-6 max-w-2xl mx-auto mt-4">
    <div class="text-6xl animate-pulse">🌟</div>
    <blockquote class="text-lg italic text-slate-600 dark:text-slate-300 font-medium">
        "Teks adalah jembatan komunikasi antara manusia dan mesin. Kuasai manipulasi teks, dan kamu bisa mengolah data dunia."
    </blockquote>
    <div class="p-4 bg-green-50 dark:bg-slate-800 rounded-2xl border border-green-200 dark:border-slate-700 text-sm font-semibold text-green-900 dark:text-green-300">
        🚀 Sampai jumpa di Sesi 4: <b>File Handling Dasar (Save & Load Data Permanen)</b>!
    </div>
</div>"""
        }
    ]
