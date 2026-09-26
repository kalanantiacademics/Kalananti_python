'use strict';

const topics = {
  1:'Introduction & Setup', 2:'Data Types & Variables', 3:'Operators',
  4:'Input & Formatting String', 5:'Logika If–Else', 6:'Elif, Function & Random',
  7:'Perulangan (Loops)', 8:'Random & Lists', 9:'Flashback & Proyek Akhir',
  10:'Pengerjaan Proyek 1', 11:'Pengerjaan Proyek 2', 12:'Showcase & Presentasi'
};

const esc = value => String(value)
  .replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;')
  .replaceAll('"','&quot;').replaceAll("'",'&#039;');

const list = (items, ordered=false) => {
  const tag = ordered ? 'ol' : 'ul';
  return `<${tag}>${items.map(item => `<li>${item}</li>`).join('')}</${tag}>`;
};

const code = source => `<pre class="code"><span aria-hidden="true">⌨ </span>${esc(source)}</pre>`;
const output = text => `<div class="output" aria-label="Output yang diharapkan">${esc(text)}</div>`;
const modeNote = text => `<div class="mode-note"><span aria-hidden="true">↔</span><div><strong>Online / offline:</strong> ${text}</div></div>`;
const reveal = (label, body) => `<details class="reveal"><summary>${label}</summary><div class="reveal-body">${body}</div></details>`;
const panels = items => `<div class="grid-${Math.min(items.length,3)}">${items.map((item,index) => `<div class="panel ${item.tone || (index===1?'yellow':'')}"><h3>${item.title}</h3>${item.body}</div>`).join('')}</div>`;

function makeSlide(meeting, sectionId, sectionLabel, title, subtitle, content, objectiveId='') {
  return { meeting, sectionId, sectionLabel, objectiveId, title, subtitle, content };
}

function reviewSlide(meeting, index, item) {
  const sectionId = `m${meeting}-review`;
  let interaction = '';
  if (item.choices) {
    interaction = `<div class="choices" role="group" aria-label="Pilihan jawaban">${item.choices.map((choice,i) => `<button class="choice" type="button" data-correct="${i===item.correct}" data-explain="${esc(item.answer)}">${choice}</button>`).join('')}</div><div class="feedback" aria-live="polite">Pilih satu jawaban.</div>`;
  } else {
    interaction = reveal('Buka jawaban setelah mencoba', `<p>${item.answer}</p>` + (item.code ? code(item.code) : ''));
  }
  return makeSlide(meeting, sectionId, 'Review Aktif', `${item.type} ${index + 1}`, item.title,
    `<div class="split-layout"><div class="illustration-side anim-bounce">🤔</div><div class="content-side"><div class="panel yellow"><p class="eyebrow">Coba dulu · jangan langsung buka jawaban</p><h3>${item.prompt}</h3>${item.snippet ? code(item.snippet) : ''}${interaction}</div>${modeNote(item.offline || 'Tulis prediksi di kertas atau tunjukkan kartu A/B/C sebelum membuka jawaban.')}</div></div>`);
}

function objectiveDivider(meeting, index, obj) {
  return makeSlide(meeting, `m${meeting}-obj-${index+1}`, `Objective ${index+1} — ${obj.label}`,
    `Objective ${index+1}: ${obj.label}`, obj.mastery,
    `<div class="hero"><div><p class="eyebrow">Target terukur</p><h2>${obj.goal}</h2><div class="callout"><strong>Berhasil jika:</strong> ${obj.success}</div></div><div class="hero-mark anim-bounce" aria-hidden="true">${obj.icon}</div></div>`, `OBJ-${meeting}.${index+1}`);
}

function detailedObjectiveSlides(meeting, index, obj) {
  if (obj.guided.length !== 3) throw new Error(`Meeting ${meeting} objective ${index+1} harus memiliki tepat 3 latihan terpandu.`);
  const sec = `m${meeting}-obj-${index+1}`;
  const label = `Objective ${index+1} — ${obj.label}`;
  const id = `OBJ-${meeting}.${index+1}`;
  const slide = (title, subtitle, content) => makeSlide(meeting,sec,label,title,subtitle,content,id);
  const slides = [objectiveDivider(meeting,index,obj)];
  slides.push(slide(`Definisi Teknis: ${obj.term}`, 'Pahami arti istilah sebelum memakai analogi',
    `<div class="split-layout"><div class="content-side"><div class="panel"><h3>${obj.term}</h3><p>${obj.formal}</p></div><div class="callout"><strong>Yang perlu diucapkan dengan tepat:</strong> ${obj.accuracy}</div></div><div class="illustration-side anim-float">📖</div></div>`));
  slides.push(slide('Model Komputer: Apa yang Terjadi?', 'Ikuti urutan eksekusi dari kiri ke kanan',
    `<div class="flow">${obj.model.map((step,i) => `<div><strong>${i+1}. ${step.title}</strong><span>${step.body}</span></div>`).join('')}</div>${modeNote('Trace urutan dengan pointer di layar; tanpa layar, gambar kotak dan panah di kertas.')}`));
  slides.push(slide(`Analogi: ${obj.analogy.title}`, 'Analogi membantu, tetapi definisi teknis tetap utama',
    panels([{title:'Bayangkan',body:`<p>${obj.analogy.body}</p>`},{title:'Batas Analogi',body:`<p>${obj.analogy.boundary}</p>`,tone:'red'}])));
  slides.push(slide('Contoh Minimal + Hasil', 'Ketik di file .py, simpan, lalu jalankan di VS Code',
    `<div class="split-layout"><div class="illustration-side anim-bounce">💻</div><div class="content-side">${code(obj.example.code)}<p><strong>Output yang diharapkan:</strong></p>${output(obj.example.output)}</div></div>`));
  slides.push(slide('Predict Before Running', 'Prediksi dulu, baru buktikan di VS Code',
    `<div class="split-layout"><div class="content-side"><div class="panel yellow"><h3>${obj.predict.prompt}</h3>${obj.predict.code ? code(obj.predict.code) : ''}${reveal('Cek prediksi', `<p>${obj.predict.answer}</p>`)}</div>${modeNote('Online: tulis di chat. Offline: tunjukkan jawaban dengan kartu atau kertas lipat.')}</div><div class="illustration-side anim-float">🔮</div></div>`));
  slides.push(slide('Do / Don’t', 'Kebiasaan kecil yang membuat kode lebih aman dibaca',
    panels([{title:'DO ✅',body:list(obj.do) ,tone:'green'},{title:'DON’T ⛔',body:list(obj.dont),tone:'red'}])));
  slides.push(slide(`Debugging ${obj.term}`, 'Gunakan bukti, bukan menebak acak',
    `<div class="flow"><div><strong>1. Baca</strong>Pesan error lengkap</div><div><strong>2. Cari</strong>Baris yang ditunjuk</div><div><strong>3. Periksa</strong>${obj.debug.check}</div><div><strong>4. Ubah satu</strong>${obj.debug.fix}</div><div><strong>5. Jalankan</strong>Bandingkan hasil</div></div><div class="callout"><strong>Error yang sering muncul:</strong> <code>${obj.debug.error}</code> — ${obj.debug.cause}</div>`));
  obj.guided.forEach((exercise,i) => slides.push(slide(`Latihan Terpandu ${i+1} dari 3`, exercise.title,
    `<div class="split-layout"><div class="illustration-side anim-float">🎯</div><div class="content-side"><div class="panel"><h3>Misi</h3><p>${exercise.prompt}</p>${exercise.starter ? code(exercise.starter) : ''}</div>${reveal('Buka solusi setelah didiskusikan', `${exercise.solution ? code(exercise.solution) : ''}${exercise.output ? output(exercise.output) : ''}<p>${exercise.reason || ''}</p>`)}</div></div>`)));
  slides.push(slide('Bug Hunt 🐛', obj.bug.title,
    `<div class="split-layout"><div class="content-side"><div class="panel red"><h3>Kode bermasalah</h3>${code(obj.bug.code)}<p><strong>Gejala:</strong> ${obj.bug.error}</p></div>${reveal('Diagnosis dan urutan perbaikan', `<p><strong>Penyebab:</strong> ${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output ? output(obj.bug.output) : ''}`)}</div><div class="illustration-side anim-bounce" style="font-size: 10rem;">🐛</div></div>`));
  slides.push(slide('Latihan Mandiri', 'Kerjakan sendiri; gunakan hints bertahap bila benar-benar perlu',
    `<div class="split-layout"><div class="illustration-side anim-float">🧗‍♂️</div><div class="content-side"><div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal('Hint bertahap', list(obj.independent.hints,true))}${reveal('Cek jawaban setelah mencoba', `${code(obj.independent.solution)}${obj.independent.output ? output(obj.independent.output) : ''}`)}</div></div>`));
  slides.push(slide('Skill Check', 'Jelaskan kode dengan kata-katamu sendiri',
    `<div class="split-layout"><div class="content-side"><div class="panel green"><h3>Bukti penguasaan</h3>${list(obj.skillCheck)}</div><p class="lead">Jika satu bukti belum tercapai, kembali ke latihan yang paling dekat—error adalah petunjuk untuk langkah berikutnya.</p></div><div class="illustration-side anim-float">🏆</div></div>`));
  return slides;
}

function compactObjectiveSlides(meeting, index, obj) {
  if (obj.guided.length !== 3) throw new Error(`Meeting ${meeting} objective ${index+1} harus memiliki tepat 3 latihan terpandu.`);
  const sec = `m${meeting}-obj-${index+1}`;
  const label = `Objective ${index+1} — ${obj.label}`;
  const id = `OBJ-${meeting}.${index+1}`;
  const slide = (title, subtitle, content) => makeSlide(meeting,sec,label,title,subtitle,content,id);
  const slides = [objectiveDivider(meeting,index,obj)];
  slides.push(slide(`Teknis + Model: ${obj.term}`, 'Definisi tepat dan urutan kerja komputer',
    `<div class="split-layout"><div class="content-side"><div class="panel"><p>${obj.formal}</p><p><strong>Ketepatan:</strong> ${obj.accuracy}</p></div><div class="flow">${obj.model.map((step,i)=>`<div><strong>${i+1}. ${step.title}</strong>${step.body}</div>`).join('')}</div></div><div class="illustration-side anim-float">⚙️</div></div>`));
  slides.push(slide(`Analogi: ${obj.analogy.title}`, 'Gunakan analogi tanpa mengubah arti teknis',
    panels([{title:'Membantu membayangkan',body:`<p>${obj.analogy.body}</p>`},{title:'Batas analogi',body:`<p>${obj.analogy.boundary}</p>`,tone:'red'}])));
  slides.push(slide('Contoh Minimal + Prediksi', 'Tebak hasil sebelum menjalankan',
    `<div class="split-layout"><div class="illustration-side anim-bounce">💻</div><div class="content-side">${code(obj.example.code)}${reveal('Cek output dan prediksi', `${output(obj.example.output)}<p>${obj.predict.answer}</p>`)}</div></div>`));
  slides.push(slide('Do / Don’t / Debug', 'Tiga kebiasaan untuk kode yang dapat dipercaya',
    panels([{title:'DO ✅',body:list(obj.do),tone:'green'},{title:'DON’T ⛔',body:list(obj.dont),tone:'red'},{title:'DEBUG 🔎',body:`<p>Periksa ${obj.debug.check}. <code>${obj.debug.error}</code> berarti ${obj.debug.cause}</p>`}])));
  obj.guided.forEach((exercise,i) => slides.push(slide(`Latihan Terpandu ${i+1} dari 3`,exercise.title,
    `<div class="split-layout"><div class="illustration-side anim-float">🎯</div><div class="content-side"><div class="panel"><p>${exercise.prompt}</p>${exercise.starter?code(exercise.starter):''}</div>${reveal('Buka solusi setelah mencoba',`${code(exercise.solution)}${exercise.output?output(exercise.output):''}<p>${exercise.reason||''}</p>`)}</div></div>`)));
  slides.push(slide('Bug Hunt 🐛',obj.bug.title,
    `<div class="split-layout"><div class="content-side"><div class="panel red">${code(obj.bug.code)}<p>${obj.bug.error}</p></div>${reveal('Diagnosis dan perbaikan',`<p>${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output?output(obj.bug.output):''}`)}</div><div class="illustration-side anim-bounce" style="font-size: 10rem;">🐛</div></div>`));
  slides.push(slide('Latihan Mandiri','Gunakan hint hanya bila diperlukan',
    `<div class="split-layout"><div class="illustration-side anim-float">🧗‍♂️</div><div class="content-side"><div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal('Hint',list(obj.independent.hints,true))}${reveal('Cek jawaban setelah mencoba',`${code(obj.independent.solution)}${obj.independent.output?output(obj.independent.output):''}`)}</div></div>`));
  return slides;
}

function integratedSlides(config) {
  const m = config.meeting;
  const sec = `m${m}-guided-projects`;
  const slides = config.guidedProjects.map((project,i) => makeSlide(m,sec,'Guided Mini-Projects',`Guided Mini-Project ${i+1} dari 3`,project.title,
    `<div class="split-layout"><div class="illustration-side anim-float">🛠️</div><div class="content-side"><div class="panel yellow"><h3>Problem dulu</h3><p>${project.problem}</p>${list(project.requirements)}</div>${reveal('Buka worked solution setelah mencoba',`${code(project.solution)}${project.output?output(project.output):''}<p>${project.connection}</p>`)}</div></div>`));
  const ind = config.independentProject;
  slides.push(makeSlide(m,`m${m}-independent-project`,'Independent Mini-Project','Independent Mini-Project',ind.title,
    `<div class="hero"><div><p class="eyebrow">Karya mandiri · tidak ada final answer</p><h2>${ind.mission}</h2>${list(ind.requirements)}</div><div class="hero-mark anim-bounce" aria-hidden="true">${ind.icon}</div></div>`));
  slides.push(makeSlide(m,`m${m}-independent-project`,'Independent Mini-Project','Starter Code','Mulai dari kerangka, lalu isi dengan keputusanmu sendiri',
    `<div class="split-layout"><div class="illustration-side anim-bounce">🚀</div><div class="content-side">${code(ind.starter)}<div class="callout">Starter ini sengaja belum lengkap. Jangan menunggu contoh final—buat versimu.</div></div></div>`));
  slides.push(makeSlide(m,`m${m}-independent-project`,'Independent Mini-Project','Hints, Acceptance Criteria, dan Bonus','Periksa hasil tanpa membandingkan dengan satu jawaban tunggal',
    panels([{title:'Minimum Goal',body:list(ind.acceptance),tone:'green'},{title:'Hints',body:list(ind.hints,true)},{title:'Bonus Opsional',body:list(ind.bonus),tone:'yellow'}]) + modeNote('Pair-check layar saat online; saat offline, tukar laptop atau baca kode teman bergantian.')));
  return slides;
}

function closingSlides(config) {
  const m=config.meeting, sec=`m${m}-closing`;
  return [
    makeSlide(m,sec,'Closing','Debugging Recap','Ulangi rutinitas yang sama setiap menemukan error',
      `<div class="split-layout"><div class="content-side"><div class="flow"><div><strong>1</strong>Baca error</div><div><strong>2</strong>Cari baris</div><div><strong>3</strong>Cek ejaan, tanda, tipe, indentasi, state</div><div><strong>4</strong>Ubah satu hal</div><div><strong>5</strong>Jalankan dan bandingkan</div></div><div class="callout">Fokus hari ini: ${config.debugRecap}</div></div><div class="illustration-side anim-bounce">🔎</div></div>`),
    makeSlide(m,sec,'Closing','Key Takeaways','Tiga hal yang perlu kamu bawa pulang',panels(config.takeaways.map((x,i)=>({title:`${i+1}`,body:`<p>${x}</p>`,tone:i===2?'green':''})))),
    makeSlide(m,sec,'Closing','Exit Ticket','Jawab tanpa membuka catatan',
      `<div class="split-layout"><div class="illustration-side anim-float">🎟️</div><div class="content-side"><div class="panel yellow"><h3>${config.exitTicket}</h3><p>Tulis satu contoh kode pendek atau jelaskan secara lisan.</p></div>${modeNote('Online: kirim private chat. Offline: tulis di sticky note atau selembar kertas.')}</div></div>`),
    makeSlide(m,sec,'Closing','Next Mission Preview',`Meeting ${m+1}: ${topics[m+1] || 'Showcase'}`,
      `<div class="hero"><div><p class="eyebrow">Misi berikutnya</p><h2>${config.preview}</h2><p class="lead">Simpan file latihan hari ini agar bisa dipakai untuk review aktif.</p></div><div class="hero-mark anim-bounce" aria-hidden="true">🔭</div></div>`),
    makeSlide(m,sec,'Closing','Quote of the Day','Satu kalimat untuk dibawa pulang',
      `<div class="quote"><div><blockquote>“${config.quote.text}”</blockquote><cite>— ${config.quote.author}</cite></div></div>`)
  ];
}

function buildConceptMeeting(config) {
  const m=config.meeting;
  let slides=[makeSlide(m,`m${m}-opening`,'Opening',`Meeting ${m}: ${config.title}`,config.unit,
    `<div class="hero"><div><p class="eyebrow">Planet Novara · Basic Python</p><h2>${config.mission}</h2><p class="lead">${config.intro}</p>${modeNote('Semua contoh dijalankan di VS Code. Tanpa internet, deck, reveal, kuis, dan latihan tetap berfungsi.')}</div><div class="hero-mark anim-bounce" aria-hidden="true">${config.icon}</div></div>` )];
  config.review.forEach((item,i)=>slides.push(reviewSlide(m,i,item)));
  slides.push(makeSlide(m,`m${m}-objectives`,'Learning Objectives','Learning Objectives','Target yang bisa diamati pada akhir meeting',
    `<div class="grid-${Math.min(config.objectives.length,3)}">${config.objectives.map((obj,i)=>`<div class="panel"><p class="eyebrow">OBJ-${m}.${i+1}</p><h3>${obj.goal}</h3><p>${obj.success}</p></div>`).join('')}</div>`));
  config.objectives.forEach((obj,i)=>slides.push(...(config.objectives.length===3?compactObjectiveSlides(m,i,obj):detailedObjectiveSlides(m,i,obj))));
  slides.push(...integratedSlides(config),...closingSlides(config));
  return slides;
}

const conceptMeetings = {};

conceptMeetings[1] = {
  meeting:1, title:'Introduction & Setup', unit:'Unit 1 · Basic Foundations', icon:'🛠️',
  mission:'Siapkan alat, tulis instruksi pertama, dan buktikan Python dapat menjalankannya.',
  intro:'Meeting ini menyambung Trial Class tentang Input–Process–Output. Jika kamu belum ikut Trial, lima tantangan awal berfungsi sebagai diagnostic warm-up.',
  review:[
    {type:'Predict Output',title:'Flashback Trial: Output',prompt:'Apa yang tampil dari kode ini?',snippet:'print("Halo, Novara!")',answer:'Terminal menampilkan: Halo, Novara!',offline:'Tulis persis output-nya, termasuk tanda baca.'},
    {type:'Susun Alur',title:'Flashback Trial: Input–Process–Output',prompt:'Urutkan: komputer menghitung panjang nama, menampilkan hasil, menerima nama.',answer:'Input: menerima nama → Process: menghitung panjang nama → Output: menampilkan hasil.'},
    {type:'Concept Quiz',title:'Flashback Trial: Decomposition',prompt:'Decomposition berarti…',choices:['Memecah masalah besar menjadi langkah kecil','Menghapus semua kode','Menghafal semua syntax'],correct:0,answer:'Decomposition membantu kita menyelesaikan bagian kecil satu per satu.'},
    {type:'Complete Code',title:'Flashback Trial: Variable',prompt:'Lengkapi agar nama tersimpan: ____ = "Nara"',answer:'nama = "Nara"',code:'nama = "Nara"'},
    {type:'Explain',title:'Flashback Trial: f-string & Logic',prompt:'Mengapa {nama} bisa berubah di f-string, sedangkan teks lain tetap?',answer:'Karena ekspresi di dalam { } dievaluasi, lalu hasilnya disisipkan ke string. If/else yang sempat terlihat di Trial akan dipelajari mendalam pada Meeting 5.'}
  ],
  objectives:[
    {
      label:'Setup & Verification', term:'Python Toolchain', icon:'🔧', mastery:'Python dan VS Code terpasang serta terhubung.',
      goal:'Memasang atau membuka Python, VS Code, dan extension Python, lalu memverifikasi versinya.',
      success:'perintah versi menampilkan Python 3 dan VS Code dapat memilih interpreter Python.',
      formal:'Toolchain adalah kumpulan alat yang dipakai untuk menulis, menjalankan, dan memeriksa program. Python interpreter mengeksekusi file <code>.py</code>; VS Code adalah editor; extension Python membantu editor mengenali bahasa dan interpreter.',
      accuracy:'VS Code bukan Python. Extension juga bukan interpreter—ketiganya memiliki tugas berbeda.',
      model:[{title:'Tulis',body:'VS Code menyimpan teks sebagai file .py.'},{title:'Pilih interpreter',body:'VS Code menunjuk instalasi Python 3.'},{title:'Jalankan',body:'Interpreter membaca instruksi dari atas ke bawah.'},{title:'Lihat bukti',body:'Terminal menampilkan output atau error.'}],
      analogy:{title:'Meja Kerja',body:'VS Code seperti meja tulis, file .py seperti resep, dan interpreter seperti koki yang menjalankan resep.',boundary:'Koki dapat menebak maksud manusia; interpreter tidak. Ia mengikuti syntax secara tepat.'},
      example:{code:'python --version',output:'Python 3.x.x'},
      predict:{prompt:'Jika file disimpan sebagai halo.txt, apakah tombol Run Python pasti mengenalinya?',answer:'Tidak. Gunakan ekstensi .py agar editor dan interpreter mengenalinya sebagai file Python.'},
      do:['Unduh Python dari python.org bila belum tersedia.','Pasang extension “Python” dari Microsoft.','Pilih interpreter Python 3 yang benar.'],
      dont:['Menganggap extension sudah memasang Python.','Memakai Live Server untuk menjalankan file Python.','Menyimpan file sebagai .txt atau tanpa ekstensi.'],
      debug:{check:'nama file, versi Python, dan interpreter aktif',fix:'pilih interpreter yang benar lalu jalankan ulang',error:'python: command not found',cause:'terminal belum menemukan instalasi Python atau perintah pada perangkat berbeda'},
      guided:[
        {title:'Cek versi Python',prompt:'Buka terminal VS Code dan cek versi Python.',starter:'python --version',solution:'python --version',output:'Python 3.x.x',reason:'Pada sebagian macOS/Linux, perintahnya dapat berupa python3 --version.'},
        {title:'Buat folder Level 1',prompt:'Buat folder novara-level1 dan buka folder itu lewat File → Open Folder.',solution:'Folder: novara-level1\nFile nanti: hello_world.py',reason:'Folder proyek membuat file mudah ditemukan.'},
        {title:'Pilih interpreter',prompt:'Buka Command Palette, pilih “Python: Select Interpreter”, lalu pilih Python 3.',solution:'Command Palette → Python: Select Interpreter → Python 3.x',reason:'Nama menu dapat sedikit berbeda antar sistem operasi.'}
      ],
      bug:{title:'File tidak berjalan sebagai Python',code:'hello_world.txt',error:'Tombol Run Python tidak muncul atau file dibuka sebagai teks biasa.',cause:'Ekstensi file salah.',fix:'hello_world.py'},
      independent:{title:'Bukti Setup Mandiri',prompt:'Siapkan folder dan file Python tanpa mengikuti langkah layar satu per satu.',requirements:['Folder bernama novara-level1','File bernama cek_setup.py','Terminal menampilkan Python 3'],hints:['Periksa ekstensi file','Lihat interpreter di status bar','Coba python3 --version bila python tidak ditemukan'],solution:'# cek_setup.py\nprint("Setup Novara siap!")',output:'Setup Novara siap!'},
      skillCheck:['Dapat membedakan editor, extension, dan interpreter.','Dapat menemukan file .py sendiri.','Dapat menunjukkan output versi Python 3.']
    },
    {
      label:'Program Output Pertama', term:'print()', icon:'🗣️', mastery:'Menulis, menyimpan, dan menjalankan hello_world.py tanpa SyntaxError.',
      goal:'Membuat file <code>hello_world.py</code> dan menampilkan beberapa output dengan <code>print()</code>.',
      success:'minimal tiga baris output tampil sesuai urutan tanpa <code>NameError</code> atau <code>SyntaxError</code>.',
      formal:'<code>print()</code> adalah built-in function Python yang menulis representasi nilai ke standard output, biasanya terminal. Teks literal ditulis di dalam tanda kutip.',
      accuracy:'<code>print()</code> menampilkan output; ia tidak menyimpan data dan tidak mencetak ke printer kertas.',
      model:[{title:'Parse',body:'Python memeriksa nama fungsi, kurung, dan kutip.'},{title:'Evaluate',body:'Isi di dalam kurung dinilai.'},{title:'Call',body:'Function print dipanggil.'},{title:'Display',body:'Teks muncul di terminal dan baris berpindah.'}],
      analogy:{title:'Papan Pengumuman',body:'print() seperti menaruh pesan di papan agar dapat dilihat.',boundary:'Pesan di terminal hanya output sementara; bukan data yang otomatis tersimpan ke file.'},
      example:{code:'print("Halo, Dunia!")\nprint("Aku tiba di Planet Novara.")',output:'Halo, Dunia!\nAku tiba di Planet Novara.'},
      predict:{prompt:'Berapa baris output yang muncul?',code:'print("A")\nprint("B")\nprint("C")',answer:'Tiga baris, berurutan A, B, C. Setiap pemanggilan print() berpindah baris secara default.'},
      do:['Tulis print dengan huruf kecil.','Pasangkan kurung buka–tutup dan kutip buka–tutup.','Simpan file sebelum menjalankan.'],
      dont:['Menulis Print atau PRINT.','Menghapus kutip dari teks biasa.','Membaca ikon ▶ sebagai bukti bahwa file sudah tersimpan.'],
      debug:{check:'ejaan print, pasangan kurung, dan pasangan kutip',fix:'perbaiki satu tanda lalu jalankan ulang',error:'SyntaxError: unterminated string literal',cause:'tanda kutip pembuka tidak memiliki pasangan penutup'},
      guided:[
        {title:'Salam Novara',prompt:'Tampilkan satu salam dan satu nama planet pada dua baris.',starter:'print("...")',solution:'print("Halo, Penjelajah!")\nprint("Planet Novara")',output:'Halo, Penjelajah!\nPlanet Novara'},
        {title:'Tiga Fakta',prompt:'Tampilkan nama, hobi, dan cita-cita pada tiga baris.',solution:'print("Nama: Nara")\nprint("Hobi: Menggambar")\nprint("Cita-cita: Programmer")',output:'Nama: Nara\nHobi: Menggambar\nCita-cita: Programmer'},
        {title:'ASCII Badge',prompt:'Buat bingkai sederhana memakai karakter = dan |.',solution:'print("==========")\nprint("| NOVARA |")\nprint("==========")',output:'==========\n| NOVARA |\n=========='},
      ],
      bug:{title:'Python mengira teks adalah nama',code:'print(Halo Novara)',error:'SyntaxError muncul sebelum program berjalan.',cause:'Teks literal tidak diapit tanda kutip.',fix:'print("Halo Novara")',output:'Halo Novara'},
      independent:{title:'Poster Terminal',prompt:'Buat poster terminal tentang satu hal yang kamu sukai.',requirements:['Minimal empat print()','Ada judul, isi, dan penutup','Output sama persis dengan rencana'],hints:['Rancang output di kertas dulu','Gunakan simbol sederhana untuk bingkai','Cek setiap pasangan kutip'],solution:'print("=== BUKU FAVORIT ===")\nprint("Judul: Petualangan Novara")\nprint("Alasan: Ceritanya seru")\nprint("====================")',output:'=== BUKU FAVORIT ===\nJudul: Petualangan Novara\nAlasan: Ceritanya seru\n===================='},
      skillCheck:['Dapat menjelaskan peran print().','Dapat memperkirakan jumlah dan urutan baris output.','Dapat memperbaiki kutip atau kurung yang tidak berpasangan.']
    }
  ],
  guidedProjects:[
    {title:'Robot Penyapa',problem:'Buat robot terminal yang menyapa dalam tiga tahap.',requirements:['Pembuka','Pesan utama','Penutup'],solution:'print("Robot Novara aktif!")\nprint("Halo, penjelajah baru!")\nprint("Sampai jumpa!")',output:'Robot Novara aktif!\nHalo, penjelajah baru!\nSampai jumpa!',connection:'Menggabungkan urutan instruksi dan print().'},
    {title:'Menu Kantin Statis',problem:'Tampilkan judul dan tiga menu tanpa menerima input.',requirements:['Empat atau lebih print()','Tata letak mudah dibaca'],solution:'print("=== KANTIN NOVARA ===")\nprint("1. Roti")\nprint("2. Susu")\nprint("3. Buah")',output:'=== KANTIN NOVARA ===\n1. Roti\n2. Susu\n3. Buah',connection:'Melatih satu ide per baris output.'},
    {title:'Kartu Misi',problem:'Tampilkan nama misi, status, dan pesan semangat.',requirements:['Bingkai simbol','Tiga informasi'],solution:'print("+----------------+")\nprint("| MISI: SETUP    |")\nprint("| STATUS: SIAP   |")\nprint("| AYO NGODING!   |")\nprint("+----------------+")',connection:'Menghubungkan setup file dengan output yang dirancang.'}
  ],
  independentProject:{title:'Novara Mission Badge',mission:'Rancang badge terminal versimu sendiri.',icon:'🪪',requirements:['Minimal lima baris output','Memuat nama panggilan, minat, dan tujuan belajar','Tata letak terbaca'],starter:'# novara_badge.py\nprint("...")\n# lanjutkan desainmu',hints:['Sketsa output dulu','Pastikan panjang bingkai konsisten','Jalankan setelah setiap dua baris'],acceptance:['File .py tersimpan','Program berjalan tanpa error','Semua informasi tampil berurutan'],bonus:['Tambahkan ikon Unicode yang aman','Buat dua versi desain']},
  debugRecap:'bedakan error setup, ekstensi file, kutip, dan kurung.',
  takeaways:['VS Code, extension, dan interpreter adalah tiga komponen berbeda.','File Python memakai ekstensi .py dan dijalankan oleh interpreter.','print() menampilkan nilai ke terminal sesuai urutan.'],
  exitTicket:'Jelaskan perjalanan satu baris print() dari file .py sampai terlihat di terminal.',
  preview:'Kita akan memberi nama pada data dan mengenali String, Integer, Float, serta Boolean.',
  quote:{text:'The best way to predict the future is to invent it.',author:'Alan Kay'}
};

conceptMeetings[2] = {
  meeting:2,title:'Data Types & Variables',unit:'Unit 1 · Basic Foundations',icon:'📦',
  mission:'Beri nama pada data agar Python dapat menyimpan, memakai, dan memperbaruinya.',
  intro:'Kita melanjutkan output dari Meeting 1. Sekarang pesan tidak harus ditulis ulang karena nilai dapat dirujuk melalui variable.',
  review:[
    {type:'Predict Output',title:'Urutan print()',prompt:'Apa urutan output?',snippet:'print("dua")\nprint("satu")',answer:'dua lalu satu. Python menjalankan instruksi dari atas ke bawah.'},
    {type:'Find the Bug',title:'Tanda Kutip',prompt:'Temukan satu penyebab error.',snippet:'print("Halo Novara)',answer:'Tanda kutip penutup hilang. Perbaiki menjadi print("Halo Novara").'},
    {type:'Complete Code',title:'Function Output',prompt:'Lengkapi nama function: ____("Siap!")',answer:'print("Siap!")'},
    {type:'Reorder',title:'Alur Menjalankan File',prompt:'Urutkan: lihat output, simpan .py, tulis kode, jalankan.',answer:'Tulis kode → simpan sebagai .py → jalankan → lihat output.'},
    {type:'Quick VS Code',title:'Bukti Setup',prompt:'Buka hello_world.py dan tambahkan satu print() baru. Apa bukti berhasil?',answer:'Terminal menampilkan baris baru sesuai teks yang ditulis.'}
  ],
  objectives:[
    {
      label:'Variables, Names & Comments',term:'Variable Assignment',icon:'🏷️',mastery:'Membuat dan memperbarui variable dengan nama yang valid.',
      goal:'Membuat minimal tiga variable, memakai nama bermakna, dan menambahkan comment yang relevan.',
      success:'kode berjalan tanpa NameError dan nilai terbaru dapat ditampilkan.',
      formal:'Assignment dengan operator <code>=</code> mengikat sebuah nama ke suatu object/value. Saat nama dipakai lagi, Python mencari binding terbaru pada scope tersebut. Comment dimulai dengan <code>#</code> dan diabaikan interpreter sampai akhir baris.',
      accuracy:'Variable bukan kotak fisik dan <code>=</code> bukan perbandingan; di sini ia melakukan assignment.',
      model:[{title:'Evaluasi kanan',body:'Python menilai value di kanan =.'},{title:'Bind nama',body:'Nama di kiri merujuk value itu.'},{title:'Gunakan nama',body:'Python mencari value saat nama disebut.'},{title:'Reassign',body:'Nama dapat diarahkan ke value baru.'}],
      analogy:{title:'Label pada Loker',body:'Nama variable seperti label yang membantu menemukan isi loker.',boundary:'Satu value dapat dirujuk beberapa nama, dan cara memori Python bekerja lebih kompleks daripada satu kotak tetap.'},
      example:{code:'# profil penjelajah\nnama = "Alya"\numur = 13\nprint(nama)\nprint(umur)',output:'Alya\n13'},
      predict:{prompt:'Apa output terakhir?',code:'skor = 10\nskor = 25\nprint(skor)',answer:'25, karena assignment kedua membuat nama skor merujuk nilai terbaru.'},
      do:['Gunakan snake_case: makanan_favorit.','Mulai nama dengan huruf atau underscore.','Tulis comment yang menjelaskan alasan atau konteks.'],
      dont:['Memakai spasi pada nama variable.','Memulai nama dengan angka.','Menggunakan kata kunci seperti if sebagai nama.'],
      debug:{check:'ejaan nama dan apakah assignment sudah dijalankan lebih dulu',fix:'samakan ejaan persis atau pindahkan assignment sebelum penggunaan',error:'NameError',cause:'Python tidak menemukan nama tersebut pada saat baris dijalankan'},
      guided:[
        {title:'Profil Tiga Data',prompt:'Simpan nama, kelas, dan hobi lalu tampilkan.',solution:'nama = "Raka"\nkelas = "8A"\nhobi = "Futsal"\nprint(nama)\nprint(kelas)\nprint(hobi)',output:'Raka\n8A\nFutsal'},
        {title:'Update Status',prompt:'Buat status awal “belum siap”, ubah menjadi “siap”, lalu tampilkan.',solution:'status = "belum siap"\nstatus = "siap"\nprint(status)',output:'siap'},
        {title:'Comment Berguna',prompt:'Tambahkan comment yang menjelaskan tujuan variable.',solution:'# target poin untuk naik level\ntarget_poin = 100\nprint(target_poin)',output:'100'}
      ],
      bug:{title:'Nama berbeda satu huruf',code:'nama_siswa = "Dina"\nprint(nama_siswi)',error:'NameError: name \'nama_siswi\' is not defined',cause:'Assignment memakai nama_siswa, tetapi print memakai nama_siswi.',fix:'nama_siswa = "Dina"\nprint(nama_siswa)',output:'Dina'},
      independent:{title:'Kartu Profil Variable',prompt:'Simpan empat informasi tentang karakter fiksi.',requirements:['Empat nama variable valid','Satu comment bermakna','Semua value ditampilkan'],hints:['Gunakan snake_case','Assignment sebelum print','Cek huruf besar-kecil'],solution:'# profil karakter\nnama_karakter = "Nova"\nasal = "Novara"\nlevel = 1\naktif = True\nprint(nama_karakter)\nprint(asal)\nprint(level)\nprint(aktif)',output:'Nova\nNovara\n1\nTrue'},
      skillCheck:['Dapat menjelaskan assignment sebagai binding nama ke value.','Dapat memperbaiki NameError akibat typo.','Dapat membedakan comment dengan output.']
    },
    {
      label:'Basic Data Types',term:'str, int, float, bool',icon:'🧩',mastery:'Mengenali empat tipe data dasar dan memeriksanya dengan type().',
      goal:'Membuat String, Integer, Float, dan Boolean lalu memeriksa tipenya dengan <code>type()</code>.',
      success:'empat value ditulis dengan literal yang tepat dan hasil type() sesuai prediksi.',
      formal:'Tipe data menentukan jenis value dan operasi yang didukung. <code>str</code> menyimpan teks, <code>int</code> bilangan bulat, <code>float</code> bilangan desimal, dan <code>bool</code> hanya <code>True</code> atau <code>False</code>.',
      accuracy:'Angka di dalam kutip adalah str, bukan int. Boolean Python memakai huruf awal kapital.',
      model:[{title:'Baca literal',body:'Python melihat kutip, titik desimal, atau kata True/False.'},{title:'Buat object',body:'Value dibuat dengan tipe tertentu.'},{title:'Bind nama',body:'Variable merujuk object.'},{title:'Cek type()',body:'Python mengembalikan class tipenya.'}],
      analogy:{title:'Kategori Barang',body:'Toko memisahkan buku, makanan, dan alat tulis karena perlakuannya berbeda.',boundary:'Tipe Python adalah bagian dari model eksekusi, bukan hanya label visual; tipe menentukan operasi yang valid.'},
      example:{code:'judul = "Misi Novara"\npoin = 80\nsuhu = 26.5\naktif = True\nprint(type(judul))\nprint(type(poin))\nprint(type(suhu))\nprint(type(aktif))',output:"<class 'str'>\n<class 'int'>\n<class 'float'>\n<class 'bool'>"},
      predict:{prompt:'Apa tipe setiap value?',code:'kode = "101"\njumlah = 101\ntepat = False',answer:'kode adalah str karena memakai kutip; jumlah adalah int; tepat adalah bool.'},
      do:['Pakai kutip untuk teks.','Pakai titik sebagai pemisah desimal.','Tulis True dan False dengan kapital awal.'],
      dont:['Menulis desimal dengan koma.','Menganggap "12" sama tipe dengan 12.','Menulis true atau false huruf kecil.'],
      debug:{check:'kutip, titik desimal, dan kapitalisasi Boolean',fix:'ubah literal sesuai tipe yang dimaksud',error:'NameError: name \'true\' is not defined',cause:'true huruf kecil dianggap nama variable yang belum dibuat'},
      guided:[
        {title:'Empat Tipe',prompt:'Buat satu contoh untuk setiap tipe dasar.',solution:'planet = "Novara"\nroket = 3\nbahan_bakar = 72.5\nsiap = True',reason:'Perhatikan bentuk literalnya.'},
        {title:'Detektif type()',prompt:'Tampilkan tipe dari nilai "15", 15, dan 15.0.',solution:'print(type("15"))\nprint(type(15))\nprint(type(15.0))',output:"<class 'str'>\n<class 'int'>\n<class 'float'>"},
        {title:'Perbaiki Boolean',prompt:'Buat status login yang valid dan tampilkan tipenya.',solution:'sudah_login = False\nprint(type(sudah_login))',output:"<class 'bool'>"}
      ],
      bug:{title:'Koma bukan desimal Python',code:'suhu = 26,5\nprint(type(suhu))',error:'Output type menjadi tuple, bukan float.',cause:'Koma membentuk kumpulan nilai; literal float memakai titik.',fix:'suhu = 26.5\nprint(type(suhu))',output:"<class 'float'>"},
      independent:{title:'Data Astronaut',prompt:'Buat data astronaut dengan empat tipe berbeda.',requirements:['Nama str','Jumlah misi int','Tinggi float','Status aktif bool'],hints:['Tentukan tipe sebelum menulis','Gunakan type() untuk membuktikan','Periksa kutip dan kapital'],solution:'nama = "Luna"\njumlah_misi = 4\ntinggi = 158.5\naktif = True\nprint(type(nama))\nprint(type(jumlah_misi))\nprint(type(tinggi))\nprint(type(aktif))'},
      skillCheck:['Dapat membedakan "7", 7, dan 7.0.','Dapat menulis Boolean valid.','Dapat memakai type() untuk memeriksa prediksi.']
    }
  ],
  guidedProjects:[
    {title:'Kartu Pemain',problem:'Simpan nama, skor, akurasi, dan status online.',requirements:['Empat tipe dasar','Nama variable bermakna'],solution:'nama = "Kai"\nskor = 120\nakurasi = 87.5\nonline = True\nprint(nama)\nprint(skor)\nprint(akurasi)\nprint(online)',output:'Kai\n120\n87.5\nTrue',connection:'Menggabungkan assignment, tipe, dan output Meeting 1.'},
    {title:'Inventori Roket',problem:'Buat empat data inventori sederhana.',requirements:['Comment tujuan','Minimal tiga tipe'],solution:'# data inventori roket\nnama_barang = "Kapsul"\njumlah = 2\nberat = 4.75\ntersedia = True\nprint(nama_barang, jumlah, berat, tersedia)',connection:'Memakai comment dan beberapa value dalam print.'},
    {title:'Status Misi',problem:'Ubah status dan poin setelah misi selesai.',requirements:['Reassignment dua variable','Tampilkan value terbaru'],solution:'status = "berjalan"\npoin = 0\nstatus = "selesai"\npoin = 100\nprint(status)\nprint(poin)',output:'selesai\n100',connection:'Menunjukkan variable dapat diperbarui.'}
  ],
  independentProject:{title:'Digital Character Card',mission:'Rancang data karakter orisinal dan tampilkan sebagai kartu terminal.',icon:'🧙',requirements:['Minimal lima variable','Memakai keempat tipe dasar','Minimal dua comment relevan','Output tertata'],starter:'# character_card.py\n# identitas karakter\nnama = "..."\n# tambahkan data lain\nprint(nama)',hints:['Rencanakan nama dan tipe di tabel kecil','Pakai type() saat ragu','Cek ejaan variable satu per satu'],acceptance:['Semua variable dibuat sebelum digunakan','Keempat tipe muncul','Program berjalan tanpa NameError'],bonus:['Lakukan satu reassignment','Tampilkan tipe salah satu value']},
  debugRecap:'cek apakah nama sudah dibuat, ejaannya sama, dan literal memiliki tipe yang dimaksud.',
  takeaways:['Assignment mengikat nama ke value.','Nama variable valid, konsisten, dan bermakna membuat kode mudah dibaca.','str, int, float, dan bool memiliki bentuk literal dan perilaku berbeda.'],
  exitTicket:'Apa perbedaan "25", 25, dan 25.0? Berikan nama tipe masing-masing.',
  preview:'Variable angka akan kita olah memakai operator matematika.',
  quote:{text:'Simplicity is prerequisite for reliability.',author:'Edsger W. Dijkstra'}
};

conceptMeetings[3] = {
  meeting:3,title:'Operators',unit:'Unit 1 · Basic Foundations',icon:'🧮',mission:'Gunakan Python sebagai kalkulator yang menyimpan hasil di variable.',intro:'Kita memakai int dan float dari Meeting 2. Hari ini tidak ada input pengguna dulu—fokus pada operasi matematika dan urutan perhitungan.',
  review:[
    {type:'Concept Quiz',title:'Tipe Data',prompt:'Mana yang bertipe int?',choices:['"42"','42','42.0'],correct:1,answer:'42 tanpa kutip dan tanpa titik desimal adalah int.'},
    {type:'Find the Bug',title:'Boolean',prompt:'Mengapa baris ini error?',snippet:'aktif = true',answer:'Boolean Python ditulis True dengan T kapital.'},
    {type:'Predict Output',title:'Reassignment',prompt:'Apa output-nya?',snippet:'poin = 5\npoin = 9\nprint(poin)',answer:'9, karena nama poin merujuk value terbaru.'},
    {type:'Complete Code',title:'Variable Valid',prompt:'Ubah nama tidak valid “jumlah siswa” menjadi snake_case.',answer:'jumlah_siswa'},
    {type:'Explain',title:'Comment',prompt:'Apakah # hitung skor tampil di terminal? Mengapa?',answer:'Tidak. Interpreter mengabaikan comment dari # hingga akhir baris.'}
  ],
  objectives:[
    {label:'Arithmetic Operators',term:'+, -, *, /',icon:'➗',mastery:'Menghasilkan perhitungan +, -, *, dan / dengan benar.',goal:'Menggunakan empat arithmetic operators dasar dan memprediksi hasilnya.',success:'minimal empat operasi menghasilkan angka yang sesuai, termasuk hasil / sebagai float.',formal:'Arithmetic operators membentuk expression. Python mengevaluasi operand dan operator untuk menghasilkan value baru. Operator <code>/</code> melakukan true division dan menghasilkan float.',accuracy:'Operator membuat hasil baru; ia tidak otomatis mengubah operand atau variable asal.',model:[{title:'Baca operand',body:'Ambil angka kiri dan kanan.'},{title:'Pilih operator',body:'Terapkan aturan +, -, *, atau /.'},{title:'Buat hasil',body:'Expression menghasilkan value baru.'},{title:'Output',body:'print menampilkan hasil bila dipanggil.'}],analogy:{title:'Mesin Kalkulator',body:'Masukkan dua angka, pilih tombol operasi, lalu lihat hasil.',boundary:'Python mengikuti precedence dan tipe data; ia tidak menebak maksud soal cerita.'},example:{code:'print(12 + 3)\nprint(12 - 3)\nprint(12 * 3)\nprint(12 / 3)',output:'15\n9\n36\n4.0'},predict:{prompt:'Apa output 7 / 2?',code:'print(7 / 2)',answer:'3.5. Operator / menghasilkan pembagian sebenarnya.'},do:['Gunakan * untuk perkalian.','Gunakan / untuk pembagian.','Pakai spasi di sekitar operator agar terbaca.'],dont:['Menulis × atau ÷ di kode.','Menganggap / selalu menghasilkan int.','Membagi dengan nol.'],debug:{check:'simbol operator dan tipe operand',fix:'ganti simbol atau value yang salah',error:'ZeroDivisionError',cause:'program mencoba membagi angka dengan nol'},guided:[{title:'Empat Operasi',prompt:'Hitung 20 dan 5 dengan empat operator.',solution:'print(20 + 5)\nprint(20 - 5)\nprint(20 * 5)\nprint(20 / 5)',output:'25\n15\n100\n4.0'},{title:'Harga Dua Buku',prompt:'Satu buku 12.000. Hitung harga dua buku.',solution:'print(12000 * 2)',output:'24000'},{title:'Bagi Rata',prompt:'Bagi 15 permen kepada 3 anak.',solution:'print(15 / 3)',output:'5.0'}],bug:{title:'Simbol matematika bukan syntax Python',code:'hasil = 8 × 4\nprint(hasil)',error:'SyntaxError: invalid character',cause:'Python memakai * untuk perkalian.',fix:'hasil = 8 * 4\nprint(hasil)',output:'32'},independent:{title:'Kalkulator Bekal',prompt:'Hitung total harga tiga jenis bekal dari angka tetap.',requirements:['Memakai + dan *','Minimal tiga expression','Semua hasil tampil'],hints:['Hitung subtotal per jenis','Gunakan angka tanpa kutip','Cek * bukan x'],solution:'roti = 5000 * 2\nsusu = 7000 * 1\nbuah = 4000 * 3\ntotal = roti + susu + buah\nprint(total)',output:'29000'},skillCheck:['Membedakan * dengan simbol ×.','Memprediksi hasil / sebagai float.','Mengenali ZeroDivisionError.']},
    {label:'Expressions with Variables',term:'Numeric Expression',icon:'📊',mastery:'Menghitung angka yang tersimpan di variable.',goal:'Menyusun expression dari variable dan menyimpan hasilnya pada variable baru.',success:'hasil perhitungan dapat dijelaskan dari operand, operator, dan urutan evaluasi.',formal:'Expression adalah kombinasi value, nama, dan operator yang dievaluasi menjadi value. Parentheses dapat mengatur bagian yang dihitung lebih dahulu.',accuracy:'Nama variable tidak berubah kecuali ada assignment baru ke nama itu.',model:[{title:'Lookup',body:'Cari value setiap nama.'},{title:'Kelompokkan',body:'Kerjakan parentheses lebih dulu.'},{title:'Evaluate',body:'Ikuti precedence * dan / sebelum + dan -.'},{title:'Assign',body:'Bind hasil ke nama di kiri =.'}],analogy:{title:'Label Bahan Resep',body:'Harga dan jumlah diberi label, lalu resep total merujuk label itu.',boundary:'Expression Python harus eksplisit; menempelkan dua nama tidak berarti perkalian.'},example:{code:'harga = 8000\njumlah = 3\ntotal = harga * jumlah\nprint(total)',output:'24000'},predict:{prompt:'Berapa total?',code:'a = 2\nb = 5\nhasil = a + b * 3\nprint(hasil)',answer:'17 karena b * 3 dikerjakan sebelum +. Gunakan (a + b) * 3 jika ingin 21.'},do:['Gunakan nama yang menjelaskan isi angka.','Simpan hasil penting di variable.','Gunakan parentheses saat maksud urutan perlu jelas.'],dont:['Menulis angka sebagai string.','Mengubah operand tanpa alasan.','Mengandalkan tebakan precedence.'],debug:{check:'tipe value, ejaan nama, dan urutan operasi',fix:'cetak subtotal atau tambahkan parentheses',error:'TypeError',cause:'operator menerima kombinasi tipe yang tidak didukung'},guided:[{title:'Luas Persegi Panjang',prompt:'Hitung luas dari panjang dan lebar.',solution:'panjang = 8\nlebar = 5\nluas = panjang * lebar\nprint(luas)',output:'40'},{title:'Sisa Uang',prompt:'Hitung sisa dari uang awal dikurangi harga.',solution:'uang = 50000\nharga = 18000\nsisa = uang - harga\nprint(sisa)',output:'32000'},{title:'Rata-Rata Sederhana',prompt:'Hitung rata-rata tiga nilai dengan parentheses.',solution:'n1 = 80\nn2 = 90\nn3 = 85\nrata = (n1 + n2 + n3) / 3\nprint(rata)',output:'85.0'}],bug:{title:'Angka tersimpan sebagai teks',code:'harga = "5000"\njumlah = 2\ntotal = harga + jumlah',error:'TypeError: can only concatenate str ...',cause:'harga adalah str, sedangkan jumlah int.',fix:'harga = 5000\njumlah = 2\ntotal = harga * jumlah\nprint(total)',output:'10000'},independent:{title:'Skor Turnamen',prompt:'Hitung skor akhir dari poin dasar, bonus, dan penalti.',requirements:['Tiga variable input tetap','Expression memakai +, *, dan -','Hasil disimpan'],hints:['Beri nama setiap komponen','Tentukan bonus per kemenangan','Cetak subtotal bila perlu'],solution:'poin_dasar = 50\nmenang = 3\nbonus_per_menang = 10\npenalti = 5\nskor_akhir = poin_dasar + menang * bonus_per_menang - penalti\nprint(skor_akhir)',output:'75'},skillCheck:['Menjelaskan expression dan assignment.','Menggunakan parentheses dengan sengaja.','Mendiagnosis TypeError dari str dan int.']}
  ],
  guidedProjects:[
    {title:'Kasir Mini Tetap',problem:'Hitung total dua jenis barang.',requirements:['Subtotal per barang','Total akhir'],solution:'pensil = 3000 * 2\nbuku = 7000 * 3\ntotal = pensil + buku\nprint(total)',output:'27000',connection:'Menggabungkan variable numerik dan operators.'},
    {title:'Penghitung Waktu',problem:'Ubah 2 jam 15 menit menjadi total menit.',requirements:['Variable jam dan menit','Gunakan * dan +'],solution:'jam = 2\nmenit = 15\ntotal_menit = jam * 60 + menit\nprint(total_menit)',output:'135',connection:'Menerjemahkan soal menjadi expression.'},
    {title:'Poin Eksplorasi',problem:'Hitung poin setelah bonus dan penalti.',requirements:['Minimal tiga komponen','Output skor akhir'],solution:'poin = 100\nbonus = 25 * 2\npenalti = 10\nskor = poin + bonus - penalti\nprint(skor)',output:'140',connection:'Membangun proses dari langkah kecil.'}
  ],
  independentProject:{title:'Kalkulator Rencana Tabungan',mission:'Hitung target tabungan dari angka yang sudah ditetapkan di kode.',icon:'💰',requirements:['Uang awal, tabungan mingguan, jumlah minggu','Hitung total akhir dan selisih terhadap target','Tampilkan minimal dua hasil'],starter:'uang_awal = 50000\ntabungan_mingguan = 20000\njumlah_minggu = 4\n# tulis perhitunganmu',hints:['Hitung tambahan tabungan','Jumlahkan dengan uang awal','Kurangi target untuk melihat selisih'],acceptance:['Memakai variable numerik','Minimal tiga operator relevan','Hasil sesuai hitungan manual'],bonus:['Bandingkan dua skenario minggu','Buat perhitungan rata-rata per hari']},
  debugRecap:'cek operator, tipe operand, pembagian nol, serta parentheses.',takeaways:['Operators mengevaluasi angka menjadi value baru.','/ menghasilkan float.','Expression dengan variable mengikuti precedence dan dapat diperjelas dengan parentheses.'],exitTicket:'Mengapa (2 + 5) * 3 berbeda dari 2 + 5 * 3?',preview:'Program akan menerima jawaban pengguna dengan input() dan membuat pesan menggunakan f-string.',quote:{text:'Programs are meant to be read by humans and only incidentally for computers to execute.',author:'Donald Knuth'}
};

conceptMeetings[4] = {
  meeting:4,title:'Input & Formatting String',unit:'Unit 1 · Basic Foundations',icon:'💬',mission:'Buat program yang bertanya, menyimpan jawaban, lalu membalas secara personal.',intro:'Meeting 3 memakai angka tetap. Sekarang pengguna memberi input saat program berjalan dan f-string menyisipkan value ke dalam pesan.',
  review:[
    {type:'Predict Output',title:'Precedence',prompt:'Apa hasilnya?',snippet:'print(2 + 4 * 3)',answer:'14; perkalian dikerjakan sebelum penjumlahan.'},
    {type:'Find the Bug',title:'Perkalian',prompt:'Perbaiki simbol yang salah.',snippet:'hasil = 5 x 4',answer:'Gunakan hasil = 5 * 4.'},
    {type:'Complete Code',title:'Simpan Hasil',prompt:'Lengkapi: total __ harga * jumlah',answer:'total = harga * jumlah'},
    {type:'Concept Quiz',title:'True Division',prompt:'Apa tipe hasil 8 / 2?',choices:['int','float','str'],correct:1,answer:'4.0 bertipe float.'},
    {type:'Quick VS Code',title:'Trace Variable',prompt:'Cetak subtotal sebelum total. Mengapa ini membantu?',answer:'Kita dapat membandingkan hasil tiap langkah dan menemukan perhitungan yang salah.'}
  ],
  objectives:[
    {label:'User Input',term:'input()',icon:'⌨️',mastery:'Menerima jawaban pengguna dan menyimpannya.',goal:'Memanggil <code>input()</code> dengan prompt yang jelas dan memakai jawaban pengguna.',success:'program berhenti menunggu input, menerima teks, lalu melanjutkan tanpa NameError.',formal:'<code>input(prompt)</code> menampilkan prompt, menunggu pengguna mengetik dan menekan Enter, lalu mengembalikan jawaban sebagai <code>str</code>.',accuracy:'input() selalu mengembalikan str pada pembelajaran ini, meskipun pengguna mengetik digit.',model:[{title:'Prompt',body:'Teks pertanyaan ditampilkan.'},{title:'Pause',body:'Program menunggu Enter.'},{title:'Return',body:'Jawaban dikembalikan sebagai str.'},{title:'Assign',body:'Nama variable merujuk jawaban.'}],analogy:{title:'Pewawancara',body:'Pewawancara bertanya lalu menunggu jawaban sebelum lanjut.',boundary:'input() menerima satu baris teks; ia tidak memahami maksud atau memvalidasi otomatis.'},example:{code:'nama = input("Siapa namamu? ")\nprint(nama)',output:'Siapa namamu? Nara\nNara'},predict:{prompt:'Apa tipe umur?',code:'umur = input("Umur: ")\nprint(type(umur))',answer:"Tetap <class 'str'>, walaupun pengguna mengetik 13."},do:['Tulis prompt yang jelas.','Beri spasi di akhir prompt.','Simpan return value ke variable.'],dont:['Mengharapkan input berjalan tanpa menekan Enter.','Menganggap digit otomatis menjadi int.','Menampilkan data pribadi sungguhan.'],debug:{check:'kurung, kutip, dan apakah return value disimpan',fix:'perbaiki pemanggilan input atau nama variable',error:'EOFError',cause:'lingkungan menjalankan input tanpa sumber masukan; gunakan terminal VS Code'},guided:[{title:'Tanya Nama',prompt:'Minta nama dan tampilkan kembali.',solution:'nama = input("Nama: ")\nprint(nama)',output:'Nama: Nara\nNara'},{title:'Tanya Hobi',prompt:'Minta hobi dan simpan jawabannya.',solution:'hobi = input("Hobi favorit: ")\nprint(hobi)'},{title:'Dua Pertanyaan',prompt:'Minta nama dan planet favorit.',solution:'nama = input("Nama: ")\nplanet = input("Planet favorit: ")\nprint(nama)\nprint(planet)'}],bug:{title:'Return value tidak disimpan',code:'input("Nama: ")\nprint(nama)',error:'NameError: name \'nama\' is not defined',cause:'Jawaban input tidak di-assignment ke nama.',fix:'nama = input("Nama: ")\nprint(nama)'},independent:{title:'Wawancara Mini',prompt:'Tanyakan tiga hal aman tentang karakter fiksi.',requirements:['Tiga input()','Prompt jelas','Semua jawaban ditampilkan'],hints:['Satu variable per jawaban','Hindari data pribadi nyata','Cek ejaan nama'],solution:'nama = input("Nama karakter: ")\nkekuatan = input("Kekuatan: ")\nasal = input("Asal planet: ")\nprint(nama)\nprint(kekuatan)\nprint(asal)'},skillCheck:['Menjelaskan program berhenti saat input().','Menyatakan return value input() adalah str.','Memperbaiki NameError karena jawaban tidak disimpan.']},
    {label:'Formatted Strings',term:'f-string',icon:'✨',mastery:'Menyisipkan variable ke dalam pesan yang rapi.',goal:'Membuat minimal dua f-string yang menyisipkan jawaban pengguna.',success:'value muncul di posisi {expression} tanpa mencetak kurung kurawal mentah.',formal:'f-string adalah string literal berawalan <code>f</code>. Expression di dalam <code>{ }</code> dievaluasi saat baris dijalankan lalu hasilnya diformat ke dalam string.',accuracy:'Kurung kurawal menandai expression; f-string bukan sekadar menempel teks secara visual.',model:[{title:'Temukan f',body:'Python mengenali formatted string.'},{title:'Cari { }',body:'Ambil expression di dalamnya.'},{title:'Evaluate',body:'Dapatkan value expression.'},{title:'Build',body:'Sisipkan hasil ke string akhir.'}],analogy:{title:'Template Undangan',body:'Bagian nama tamu diganti sesuai data penerima.',boundary:'Python hanya mengganti expression yang valid di { }; ia tidak mencari kata yang mirip otomatis.'},example:{code:'nama = "Nara"\nplanet = "Novara"\nprint(f"Halo {nama}, selamat datang di {planet}!")',output:'Halo Nara, selamat datang di Novara!'},predict:{prompt:'Apa yang salah jika huruf f dihapus?',code:'nama = "Nara"\nprint("Halo {nama}")',answer:'Output menjadi Halo {nama}; expression tidak dievaluasi.'},do:['Letakkan f tepat sebelum kutip.','Gunakan nama variable valid di { }.','Baca output untuk mengecek spasi dan tanda baca.'],dont:['Menulis variable di luar { }.','Mencampur kutip pembuka dan penutup.','Menampilkan data sensitif.'],debug:{check:'huruf f, pasangan { }, dan ejaan expression',fix:'tambahkan f atau samakan nama variable',error:'NameError inside f-string',cause:'expression di dalam { } memakai nama yang belum dibuat'},guided:[{title:'Sapaan Personal',prompt:'Sapa nama dari input.',solution:'nama = input("Nama: ")\nprint(f"Halo, {nama}!")'},{title:'Profil Dua Data',prompt:'Gabungkan nama dan hobi dalam satu kalimat.',solution:'nama = input("Nama: ")\nhobi = input("Hobi: ")\nprint(f"{nama} suka {hobi}.")'},{title:'Status Misi',prompt:'Masukkan nama misi dan status, lalu format output.',solution:'misi = input("Misi: ")\nstatus = input("Status: ")\nprint(f"Misi {misi} berstatus {status}.")'}],bug:{title:'f hilang',code:'nama = "Luna"\nprint("Selamat datang, {nama}!")',error:'Program berjalan tetapi output salah: {nama} tampil mentah.',cause:'String tidak diberi prefix f.',fix:'nama = "Luna"\nprint(f"Selamat datang, {nama}!")',output:'Selamat datang, Luna!'},independent:{title:'Tiket Perjalanan',prompt:'Minta nama, tujuan, dan kendaraan lalu cetak tiket satu kalimat.',requirements:['Tiga input()','Minimal satu f-string','Tanda baca rapi'],hints:['Simpan semua jawaban dulu','Tambahkan f sebelum kutip','Gunakan tiga {variable}'],solution:'nama = input("Nama: ")\ntujuan = input("Tujuan: ")\nkendaraan = input("Kendaraan: ")\nprint(f"Tiket {nama}: menuju {tujuan} dengan {kendaraan}.")'},skillCheck:['Membedakan string biasa dan f-string.','Menjelaskan kapan expression dievaluasi.','Mendiagnosis {nama} yang tampil mentah.']}
  ],
  guidedProjects:[
    {title:'Penyapa Kelas',problem:'Minta nama dan kelas lalu tampilkan sapaan.',requirements:['Dua input','Satu f-string'],solution:'nama = input("Nama: ")\nkelas = input("Kelas: ")\nprint(f"Halo {nama} dari kelas {kelas}!")',connection:'Menggabungkan input, variable, dan output.'},
    {title:'Rekomendasi Statis Personal',problem:'Minta hobi lalu balas dengan kalimat personal tanpa condition.',requirements:['Satu input','Dua print'],solution:'hobi = input("Hobi: ")\nprint(f"Wah, {hobi} terdengar seru!")\nprint(f"Semoga kamu makin jago {hobi}.")',connection:'Output dapat memakai value yang sama berulang.'},
    {title:'Kartu Tim',problem:'Minta nama tim dan motto, lalu format kartu.',requirements:['Dua input','Bingkai output'],solution:'tim = input("Nama tim: ")\nmotto = input("Motto: ")\nprint("=== KARTU TIM ===")\nprint(f"Tim: {tim}")\nprint(f"Motto: {motto}")',connection:'Menggabungkan print biasa dan f-string.'}
  ],
  independentProject:{title:'Digital Travel Ticket',mission:'Buat program tiket terminal yang mempersonalisasi data pengguna.',icon:'🎫',requirements:['Minimal tiga input aman','Minimal tiga f-string','Ada judul dan penutup'],starter:'print("=== NOVARA TRAVEL ===")\nnama = input("Nama panggilan: ")\n# lanjutkan pertanyaan dan tiketmu',hints:['Rancang pertanyaan sebelum output','Simpan setiap jawaban','Periksa f dan { }'],acceptance:['Program menunggu input dengan benar','Semua jawaban muncul pada tiket','Tidak ada {variable} mentah'],bonus:['Gunakan satu angka tetap dari Meeting 3','Buat nomor tiket dari dua variable tetap']},
  debugRecap:'cek return value input(), tipe str, huruf f, pasangan { }, dan ejaan nama.',takeaways:['input() menunggu lalu mengembalikan str.','Jawaban perlu disimpan agar dapat dipakai lagi.','f-string mengevaluasi expression dalam { } saat dijalankan.'],exitTicket:'Mengapa input 12 belum tentu dapat langsung dijumlahkan dengan angka 3?',preview:'Kita akan membandingkan value dan memilih output dengan if–else.',quote:{text:'Talk is cheap. Show me the code.',author:'Linus Torvalds'}
};

conceptMeetings[5] = {
  meeting:5,title:'Logika If–Else',unit:'Unit 2 · Logic & Control Flow',icon:'🚦',mission:'Ajarkan program membandingkan value dan memilih satu dari dua jalur.',intro:'Input dan f-string membuat program berbicara dengan pengguna. Comparison operators dan if–else membuat responsnya bergantung pada kondisi.',
  review:[
    {type:'Predict Output',title:'f-string',prompt:'Apa output jika nama = "Ari"?',snippet:'nama = "Ari"\nprint(f"Halo {nama}!")',answer:'Halo Ari!'},
    {type:'Find the Bug',title:'Prefix f',prompt:'Mengapa {hobi} tampil mentah?',snippet:'print("Hobiku {hobi}")',answer:'Tambahkan prefix f: print(f"Hobiku {hobi}").'},
    {type:'Concept Quiz',title:'Tipe input()',prompt:'Jika mengetik 15, input() mengembalikan…',choices:['int','str','float'],correct:1,answer:'input() mengembalikan str.'},
    {type:'Complete Code',title:'Simpan Jawaban',prompt:'Lengkapi: kota __ input("Kota: ")',answer:'kota = input("Kota: ")'},
    {type:'Quick VS Code',title:'Dua Input',prompt:'Buat dua input lalu tampilkan dalam satu f-string.',answer:'Contoh: print(f"{nama} tinggal di {kota}.")'}
  ],
  objectives:[
    {label:'Comparison Operators',term:'==, !=, >, <',icon:'⚖️',mastery:'Menghasilkan Boolean dari perbandingan.',goal:'Membandingkan value dengan ==, !=, >, dan < lalu memprediksi True/False.',success:'empat perbandingan menghasilkan Boolean yang tepat tanpa tertukar assignment.',formal:'Comparison expression membandingkan dua operand dan menghasilkan <code>bool</code>. <code>==</code> menguji kesetaraan; <code>!=</code> ketidaksamaan; <code>></code> lebih besar; <code><</code> lebih kecil.',accuracy:'<code>=</code> melakukan assignment, sedangkan <code>==</code> melakukan comparison.',model:[{title:'Ambil kiri',body:'Evaluasi operand kiri.'},{title:'Ambil kanan',body:'Evaluasi operand kanan.'},{title:'Bandingkan',body:'Terapkan operator.'},{title:'Hasil',body:'Dapatkan True atau False.'}],analogy:{title:'Wasit',body:'Wasit membandingkan dua skor lalu menyatakan kondisi benar atau salah.',boundary:'Python memakai aturan tipe dan case-sensitive; "A" dan "a" tidak sama.'},example:{code:'skor = 80\nprint(skor == 80)\nprint(skor != 50)\nprint(skor > 70)\nprint(skor < 100)',output:'True\nTrue\nTrue\nTrue'},predict:{prompt:'Apa hasilnya?',code:'kode = "Nova"\nprint(kode == "nova")',answer:'False karena String Python case-sensitive.'},do:['Gunakan == untuk mengecek sama.','Baca operator dari kiri ke kanan.','Uji contoh yang menghasilkan True dan False.'],dont:['Memakai = untuk bertanya “sama?”.','Menganggap huruf besar-kecil sama.','Membandingkan angka str dengan int.'],debug:{check:'jumlah tanda =, tipe operand, dan kapitalisasi',fix:'samakan tipe/value atau ganti operator',error:'TypeError',cause:'operator urutan seperti > menerima tipe yang tidak dapat dibandingkan'},guided:[{title:'Cek Kode',prompt:'Bandingkan kode input tetap dengan "NOVARA".',solution:'kode = "NOVARA"\nprint(kode == "NOVARA")',output:'True'},{title:'Skor Berbeda',prompt:'Buktikan 75 tidak sama dengan 50.',solution:'skor = 75\nprint(skor != 50)',output:'True'},{title:'Batas Umur',prompt:'Cek apakah umur 13 lebih kecil dari 17.',solution:'umur = 13\nprint(umur < 17)',output:'True'}],bug:{title:'Assignment menggantikan comparison',code:'skor = 80\nprint(skor = 80)',error:'SyntaxError: invalid syntax',cause:'Argumen print memakai assignment, bukan comparison.',fix:'skor = 80\nprint(skor == 80)',output:'True'},independent:{title:'Detektif Angka',prompt:'Buat empat comparison tentang dua angka tetap.',requirements:['Memakai ==, !=, >, <','Tampilkan semua hasil','Prediksi sebelum run'],hints:['Satu print per comparison','Baca posisi kiri-kanan','Hasil hanya True/False'],solution:'a = 12\nb = 7\nprint(a == b)\nprint(a != b)\nprint(a > b)\nprint(a < b)',output:'False\nTrue\nTrue\nFalse'},skillCheck:['Membedakan = dan ==.','Memprediksi Boolean.','Menguji dua sisi kondisi.']},
    {label:'If–Else & Indentation',term:'if / else',icon:'🔀',mastery:'Menjalankan tepat satu cabang berdasarkan kondisi.',goal:'Menulis struktur if–else berindentasi untuk memilih satu dari dua output.',success:'kondisi True menjalankan blok if, kondisi False menjalankan blok else, tanpa IndentationError.',formal:'<code>if</code> mengevaluasi kondisi. Jika truthy, suite/blok if dijalankan; bila kondisi False, suite <code>else</code> dijalankan. Indentation menentukan baris yang menjadi anggota blok.',accuracy:'if–else tidak menjalankan kedua cabang; pada pasangan ini tepat satu cabang dipilih.',model:[{title:'Evaluasi',body:'Kondisi menjadi True/False.'},{title:'Pilih',body:'True → if; False → else.'},{title:'Jalankan blok',body:'Eksekusi baris berindentasi.'},{title:'Lanjut',body:'Keluar dari struktur dan lanjut ke bawah.'}],analogy:{title:'Dua Pintu',body:'Jika punya tiket masuk pintu A; jika tidak, masuk pintu B.',boundary:'Program tidak memahami alasan—hanya hasil kondisi yang diberikan.'},example:{code:'nilai = 78\nif nilai > 70:\n    print("Lulus")\nelse:\n    print("Coba lagi")',output:'Lulus'},predict:{prompt:'Cabang mana berjalan?',code:'cuaca = "hujan"\nif cuaca == "cerah":\n    print("Main")\nelse:\n    print("Bawa payung")',answer:'Cabang else: Bawa payung.'},do:['Akhiri if dan else dengan :.','Indentasi konsisten empat spasi.','Uji contoh True dan False.'],dont:['Meletakkan kondisi setelah else.','Mencampur tab dan spasi.','Menggunakan == untuk assignment awal.'],debug:{check:'titik dua dan indentasi setiap blok',fix:'rapikan blok menjadi empat spasi',error:'IndentationError',cause:'Python tidak menemukan atau tidak konsisten membaca blok setelah if/else'},guided:[{title:'Cek Kelulusan',prompt:'Nilai 65: tampilkan Lulus jika >= tidak dipelajari; gunakan > 60.',solution:'nilai = 65\nif nilai > 60:\n    print("Lulus")\nelse:\n    print("Belajar lagi")',output:'Lulus'},{title:'Password Tetap',prompt:'Bandingkan password dengan "nova123".',solution:'password = "nova123"\nif password == "nova123":\n    print("Akses diterima")\nelse:\n    print("Akses ditolak")',output:'Akses diterima'},{title:'Suhu',prompt:'Jika suhu > 30 tampilkan Panas, selain itu Sejuk.',solution:'suhu = 27\nif suhu > 30:\n    print("Panas")\nelse:\n    print("Sejuk")',output:'Sejuk'}],bug:{title:'Blok tidak berindentasi',code:'umur = 13\nif umur < 17:\nprint("Remaja")\nelse:\nprint("Dewasa")',error:'IndentationError: expected an indented block',cause:'Isi cabang harus masuk ke kanan.',fix:'umur = 13\nif umur < 17:\n    print("Remaja")\nelse:\n    print("Dewasa")',output:'Remaja'},independent:{title:'Gerbang Misi',prompt:'Minta kode pengguna lalu beri respons diterima/ditolak.',requirements:['Satu input()','Satu comparison ==','if–else berindentasi','f-string opsional'],hints:['Simpan kode dulu','Tulis titik dua','Empat spasi pada print'],solution:'kode = input("Kode misi: ")\nif kode == "NOVARA":\n    print("Akses diterima")\nelse:\n    print("Akses ditolak")'},skillCheck:['Menjelaskan kondisi dan cabang.','Menunjukkan indentasi sebagai syntax blok.','Menguji jalur True dan False.']}
  ],
  guidedProjects:[
    {title:'Cek Jawaban Quiz',problem:'Bandingkan jawaban dengan "python".',requirements:['input','if–else','dua output'],solution:'jawaban = input("Bahasa kita: ")\nif jawaban == "python":\n    print("Benar!")\nelse:\n    print("Coba lagi")',connection:'Input Meeting 4 mengontrol kondisi Meeting 5.'},
    {title:'Penjaga Cuaca',problem:'Respons berbeda untuk cuaca "hujan".',requirements:['String comparison','f-string'],solution:'cuaca = input("Cuaca: ")\nif cuaca == "hujan":\n    print("Bawa payung")\nelse:\n    print(f"Nikmati cuaca {cuaca}")',connection:'Menggabungkan f-string dan else.'},
    {title:'Level Poin',problem:'Jika poin > 100 tampilkan Naik Level.',requirements:['Variable angka tetap','Operator >'],solution:'poin = 120\nif poin > 100:\n    print("Naik level!")\nelse:\n    print("Kumpulkan poin lagi")',output:'Naik level!',connection:'Operator matematika menjadi dasar keputusan.'}
  ],
  independentProject:{title:'Terminal Mood Responder',mission:'Buat program dua cabang yang merespons satu mood pilihan.',icon:'🙂',requirements:['Input mood','Comparison ==','if–else','Respons personal dengan f-string'],starter:'nama = input("Nama: ")\nmood = input("Mood (senang/lelah): ")\n# tulis keputusanmu',hints:['Pilih satu value untuk kondisi if','else menangani semua value lain','Uji dua input berbeda'],acceptance:['Kedua jalur pernah diuji','Tepat satu respons tiap run','Indentasi konsisten'],bonus:['Tambahkan perhitungan poin tetap sebelum kondisi','Normalisasi petunjuk input dengan huruf kecil secara manual—method belum wajib']},
  debugRecap:'cek = versus ==, titik dua, tipe operand, dan indentasi.',takeaways:['Comparison menghasilkan Boolean.','if memilih blok saat kondisi True; else menangani False.','Indentasi adalah bagian dari syntax Python.'],exitTicket:'Apa yang terjadi jika kondisi if False dan tidak ada else?',preview:'Kita menambah pilihan dengan elif, membungkus aksi dalam function, dan memakai random.',quote:{text:'The most dangerous phrase in the language is, “We’ve always done it this way.”',author:'Grace Hopper'}
};

conceptMeetings[6] = {
  meeting:6,title:'Elif, Function & Random',unit:'Unit 2 · Logic & Control Flow',icon:'🎲',mission:'Tangani banyak pilihan, beri nama pada aksi, dan hasilkan pilihan acak.',intro:'Meeting ini memiliki tiga objective yang saling menyambung: elif memilih lebih dari dua jalur, function mengemas langkah, dan module random memberi hasil acak.',
  review:[
    {type:'Predict Branch',title:'Cabang if',prompt:'Apa output untuk nilai 40?',snippet:'nilai = 40\nif nilai > 60:\n    print("Lulus")\nelse:\n    print("Latihan lagi")',answer:'Latihan lagi.'},
    {type:'Find the Bug',title:'Titik Dua',prompt:'Tanda apa yang hilang?',snippet:'if status == "siap"\n    print("Mulai")',answer:'Tambahkan : setelah kondisi.'},
    {type:'Complete Code',title:'Comparison',prompt:'Lengkapi agar mengecek kesamaan: kode __ "NOVA"',answer:'kode == "NOVA"'},
    {type:'Reorder',title:'Urutan Keputusan',prompt:'Urutkan: jalankan blok, evaluasi kondisi, lanjut program.',answer:'Evaluasi kondisi → jalankan satu blok → lanjut program.'},
    {type:'Explain',title:'Indentation',prompt:'Mengapa print di bawah if perlu empat spasi?',answer:'Indentasi menandai bahwa print adalah anggota blok if.'}
  ],
  objectives:[
    {label:'Multiple Branches with elif',term:'elif',icon:'🚪',mastery:'Memilih satu dari tiga atau lebih cabang.',goal:'Menulis rantai if–elif–else dan menguji setiap jalurnya.',success:'tiga input berbeda mencapai tiga output yang sesuai.',formal:'<code>elif</code> menambahkan kondisi yang diperiksa hanya jika semua kondisi sebelumnya False. Python menjalankan cabang pertama yang kondisinya True, lalu melewati cabang sisanya.',accuracy:'elif bukan beberapa if terpisah; urutan kondisi memengaruhi hasil.',model:[{title:'if',body:'Cek kondisi pertama.'},{title:'elif',body:'Cek jika sebelumnya False.'},{title:'else',body:'Fallback jika semua False.'}],analogy:{title:'Loket Bertingkat',body:'Coba loket pertama; jika tidak cocok, lanjut ke loket berikutnya.',boundary:'Begitu satu cabang cocok, cabang setelahnya tidak diperiksa.'},example:{code:'warna = "kuning"\nif warna == "merah":\n    print("Berhenti")\nelif warna == "kuning":\n    print("Hati-hati")\nelse:\n    print("Jalan")',output:'Hati-hati'},predict:{answer:'Untuk warna kuning, if False lalu elif True; else dilewati.'},do:['Urutkan kondisi secara masuk akal.','Gunakan : dan indentasi.','Uji setiap cabang.'],dont:['Menaruh elif setelah else.','Menganggap semua cabang berjalan.'],debug:{check:'urutan kondisi, titik dua, indentasi',error:'SyntaxError near elif',cause:'elif salah posisi atau if sebelumnya tidak lengkap'},guided:[{title:'Lampu Lalu Lintas',prompt:'Buat output merah, kuning, atau hijau.',solution:'lampu = "hijau"\nif lampu == "merah":\n    print("Berhenti")\nelif lampu == "kuning":\n    print("Hati-hati")\nelse:\n    print("Jalan")'},{title:'Rating Cuaca',prompt:'Tangani panas, hujan, dan selainnya.',solution:'cuaca = "hujan"\nif cuaca == "panas":\n    print("Minum")\nelif cuaca == "hujan":\n    print("Payung")\nelse:\n    print("Nikmati")'},{title:'Pilihan Menu',prompt:'Tangani pilihan A, B, dan lainnya.',solution:'pilihan = "B"\nif pilihan == "A":\n    print("Mulai")\nelif pilihan == "B":\n    print("Bantuan")\nelse:\n    print("Keluar")'}],bug:{title:'elif setelah else',code:'if skor > 80:\n    print("A")\nelse:\n    print("C")\nelif skor > 60:\n    print("B")',error:'SyntaxError',cause:'else harus menjadi cabang terakhir.',fix:'if skor > 80:\n    print("A")\nelif skor > 60:\n    print("B")\nelse:\n    print("C")'},independent:{title:'Tiga Respons Mood',prompt:'Tangani senang, lelah, dan input lain.',requirements:['if–elif–else','Tiga output'],hints:['Tulis else terakhir'],solution:'mood = input("Mood: ")\nif mood == "senang":\n    print("Bagikan semangat!")\nelif mood == "lelah":\n    print("Istirahat sebentar.")\nelse:\n    print("Terima kasih sudah cerita.")'}},
    {label:'Simple Functions',term:'def dan function call',icon:'🪄',mastery:'Mendefinisikan dan memanggil function sederhana.',goal:'Membuat function tanpa parameter lalu memanggilnya minimal dua kali.',success:'kode di dalam function hanya berjalan saat function dipanggil.',formal:'<code>def</code> membuat function object dan mengikatnya ke sebuah nama. Body function tidak dijalankan saat definisi; ia dijalankan setiap kali ada function call dengan <code>()</code>.',accuracy:'Function menyimpan perilaku yang dapat dipanggil; definisi saja tidak menjalankan body.',model:[{title:'def',body:'Buat dan beri nama function.'},{title:'call',body:'Temukan nama lalu jalankan body.'},{title:'return',body:'Kembali ke baris setelah call.'}],analogy:{title:'Tombol Aksi',body:'Definisi seperti memasang tombol; call seperti menekannya.',boundary:'Function call harus ditulis eksplisit dan body mengikuti indentasi.'},example:{code:'def sapa():\n    print("Halo, Novara!")\n\nsapa()\nsapa()',output:'Halo, Novara!\nHalo, Novara!'},predict:{answer:'Tanpa baris sapa(), tidak ada output dari body function.'},do:['Gunakan nama aksi seperti tampilkan_menu.','Tambahkan ().','Indentasi body.'],dont:['Mengira def langsung menjalankan body.','Lupa memanggil function.'],debug:{check:'titik dua, indentasi, dan tanda () saat call',error:'NameError',cause:'nama function salah atau dipanggil sebelum didefinisikan'},guided:[{title:'Salam Dua Kali',prompt:'Buat function salam lalu panggil dua kali.',solution:'def salam():\n    print("Selamat datang!")\n\nsalam()\nsalam()'},{title:'Tampilkan Menu',prompt:'Function menampilkan tiga pilihan.',solution:'def tampilkan_menu():\n    print("1. Main")\n    print("2. Keluar")\n\ntampilkan_menu()'},{title:'Pesan Semangat',prompt:'Buat function dengan dua print.',solution:'def semangat():\n    print("Tarik napas")\n    print("Coba satu langkah lagi")\n\nsemangat()'}],bug:{title:'Function tidak dipanggil',code:'def mulai():\n    print("Misi dimulai")',error:'Tidak ada output.',cause:'Kode hanya mendefinisikan function.',fix:'def mulai():\n    print("Misi dimulai")\n\nmulai()',output:'Misi dimulai'},independent:{title:'Function Kartu Status',prompt:'Buat function yang menampilkan kartu tiga baris.',requirements:['def','Body tiga print','Dipanggil dua kali'],hints:['Tulis call tanpa indentasi'],solution:'def kartu_status():\n    print("=== STATUS ===")\n    print("Misi siap")\n    print("==============")\n\nkartu_status()\nkartu_status()'}},
    {label:'Random Module',term:'random.randint()',icon:'🎰',mastery:'Mengimpor random dan menghasilkan integer acak.',goal:'Menggunakan import random dan randint untuk menghasilkan angka dalam batas inklusif.',success:'hasil selalu berada dalam batas dan dapat berubah antar-run.',formal:'Module adalah file/library berisi nama yang dapat dipakai. <code>import random</code> memuat module; <code>random.randint(a, b)</code> mengembalikan integer acak semu dari a sampai b, termasuk kedua batas.',accuracy:'Hasil pseudo-random dibuat algoritme; batas randint bersifat inklusif.',model:[{title:'import',body:'Muat module sekali.'},{title:'call',body:'Panggil randint(a,b).'},{title:'generate',body:'Pilih integer dalam rentang.'}],analogy:{title:'Dadu Digital',body:'Setiap lempar memberi hasil yang sulit diprediksi.',boundary:'Komputer memakai algoritme pseudo-random, bukan keberuntungan sungguhan.'},example:{code:'import random\nangka = random.randint(1, 6)\nprint(angka)',output:'Salah satu angka 1, 2, 3, 4, 5, atau 6'},predict:{answer:'Angka 1 dan 6 sama-sama mungkin karena batas randint inklusif.'},do:['Import di bagian atas.','Pastikan batas bawah <= batas atas.','Uji rentang berkali-kali.'],dont:['Mengharapkan hasil selalu berbeda.','Lupa prefix random.'],debug:{check:'import dan urutan batas',error:'NameError: random is not defined',cause:'module belum di-import'},guided:[{title:'Dadu',prompt:'Acak 1–6.',solution:'import random\nprint(random.randint(1, 6))'},{title:'Koin Angka',prompt:'Acak 0 atau 1.',solution:'import random\nprint(random.randint(0, 1))'},{title:'Poin Bonus',prompt:'Acak bonus 10–20.',solution:'import random\nbonus = random.randint(10, 20)\nprint(bonus)'}],bug:{title:'Import hilang',code:'angka = random.randint(1, 10)\nprint(angka)',error:'NameError',cause:'Nama random belum tersedia.',fix:'import random\nangka = random.randint(1, 10)\nprint(angka)'},independent:{title:'Generator Nomor Misi',prompt:'Buat nomor misi acak 100–999.',requirements:['import random','randint inklusif','f-string output'],hints:['Import paling atas'],solution:'import random\nnomor = random.randint(100, 999)\nprint(f"Nomor misi: {nomor}")'}},
  ],
  guidedProjects:[
    {title:'Dadu Berkomentar',problem:'Acak dadu lalu beri respons if–elif–else.',requirements:['randint','tiga jalur'],solution:'import random\ndadu = random.randint(1, 6)\nif dadu == 6:\n    print("Hebat!")\nelif dadu > 3:\n    print("Lumayan!")\nelse:\n    print("Coba lagi!")',connection:'Menggabungkan random dan branching.'},
    {title:'Function Lempar Koin',problem:'Masukkan random ke function lalu panggil dua kali.',requirements:['def','randint','dua call'],solution:'import random\ndef lempar_koin():\n    print(random.randint(0, 1))\n\nlempar_koin()\nlempar_koin()',connection:'Function mengulang aksi terstruktur.'},
    {title:'Cuaca Acak',problem:'Acak kode 1–3 dan tampilkan cuaca berbeda.',requirements:['randint 1–3','if–elif–else'],solution:'import random\nkode = random.randint(1, 3)\nif kode == 1:\n    print("Cerah")\nelif kode == 2:\n    print("Hujan")\nelse:\n    print("Berawan")',connection:'Satu angka acak mengontrol satu cabang.'}
  ],
  independentProject:{title:'Mystery Mission Generator',mission:'Buat program acak dengan minimal tiga hasil dan satu function.',icon:'🕵️',requirements:['import random','Satu function','randint','if–elif–else','Output f-string'],starter:'import random\n\ndef jalankan_misi():\n    kode = random.randint(1, 3)\n    # lanjutkan cabangmu\n\njalankan_misi()',hints:['Pastikan else terakhir','Gunakan kode 1, 2, 3','Uji minimal lima run'],acceptance:['Semua cabang dapat muncul','Function dipanggil','Tidak ada NameError'],bonus:['Panggil function dua kali','Tambahkan poin acak kedua']},
  debugRecap:'cek urutan cabang, call function, import module, dan batas randint.',takeaways:['elif diperiksa berurutan setelah kondisi sebelumnya False.','Body function berjalan saat dipanggil.','randint menghasilkan integer pseudo-random dalam batas inklusif.'],exitTicket:'Apa bedanya mendefinisikan function dan memanggil function?',preview:'Kita akan mengulang instruksi otomatis dengan for dan while.',quote:{text:'Everybody in this country should learn how to program a computer, because it teaches you how to think.',author:'Steve Jobs'}
};

conceptMeetings[7] = {
  meeting:7,title:'Perulangan (Loops)',unit:'Unit 2 · Logic & Control Flow',icon:'🔁',mission:'Ulangi instruksi secara otomatis dengan jumlah atau kondisi yang jelas.',intro:'Function mengemas aksi; loop menentukan berapa kali aksi berjalan. Kita belajar for untuk jumlah terencana dan while untuk pengulangan berbasis kondisi.',
  review:[
    {type:'Predict Branch',title:'elif',prompt:'Cabang pertama yang cocok?',snippet:'x = 2\nif x == 1:\n    print("A")\nelif x == 2:\n    print("B")\nelse:\n    print("C")',answer:'B.'},
    {type:'Find the Bug',title:'Function Call',prompt:'Mengapa tidak ada output?',snippet:'def sapa():\n    print("Halo")',answer:'Tambahkan sapa() setelah definisi.'},
    {type:'Concept Quiz',title:'randint',prompt:'random.randint(1, 3) dapat menghasilkan…',choices:['Hanya 1 dan 2','1, 2, atau 3','0 sampai 3'],correct:1,answer:'Kedua batas inklusif.'},
    {type:'Complete Code',title:'Import',prompt:'Lengkapi sebelum random.randint: ______ random',answer:'import random'},
    {type:'Explain',title:'Urutan Cabang',prompt:'Mengapa elif setelah cabang True dilewati?',answer:'Rantai if–elif–else menjalankan cabang pertama yang cocok.'}
  ],
  objectives:[
    {label:'For Loop with range()',term:'for dan range()',icon:'🔢',mastery:'Mengulang blok dengan jumlah terencana.',goal:'Menulis for loop dengan range() dan memprediksi nilai loop variable.',success:'jumlah iterasi dan output cocok dengan rentang yang ditulis.',formal:'<code>for</code> mengambil item satu per satu dari iterable. <code>range(stop)</code> menghasilkan urutan integer mulai 0 dan berhenti sebelum stop.',accuracy:'range(5) menghasilkan 0,1,2,3,4—bukan sampai 5.',model:[{title:'Buat range',body:'Siapkan urutan angka.'},{title:'Ambil item',body:'Bind ke loop variable.'},{title:'Jalankan body',body:'Eksekusi blok.'},{title:'Ulangi',body:'Berhenti saat item habis.'}],analogy:{title:'Daftar Giliran',body:'Petugas memanggil setiap nomor dalam daftar satu per satu.',boundary:'Loop mengikuti iterable; ia tidak memutuskan berhenti dari rasa “cukup”.'},example:{code:'for nomor in range(3):\n    print(nomor)',output:'0\n1\n2'},predict:{prompt:'Berapa kali “Go!” tampil?',code:'for i in range(4):\n    print("Go!")',answer:'Empat kali.'},do:['Indentasi body.','Gunakan nama loop variable bermakna.','Ingat stop tidak ikut.'],dont:['Lupa titik dua.','Mengubah loop variable tanpa alasan.','Menyalin print berkali-kali.'],debug:{check:'range, titik dua, dan indentasi',fix:'trace nilai loop variable di kertas',error:'IndentationError',cause:'body for tidak menjorok'},guided:[{title:'Hitung 0–4',prompt:'Tampilkan 0 sampai 4.',solution:'for angka in range(5):\n    print(angka)',output:'0\n1\n2\n3\n4'},{title:'Semangat 3 Kali',prompt:'Ulangi pesan tiga kali.',solution:'for i in range(3):\n    print("Aku bisa!")'},{title:'Poin Bertahap',prompt:'Tampilkan i * 10 untuk range(4).',solution:'for i in range(4):\n    print(i * 10)',output:'0\n10\n20\n30'}],bug:{title:'Titik dua hilang',code:'for i in range(3)\n    print(i)',error:'SyntaxError',cause:'Header for harus diakhiri :.',fix:'for i in range(3):\n    print(i)'},independent:{title:'Countdown For',prompt:'Tampilkan 3,2,1 memakai perhitungan dari i.',requirements:['Satu for','range(3)','Tiga output'],hints:['Nilai i: 0,1,2','Hitung 3 - i'],solution:'for i in range(3):\n    print(3 - i)',output:'3\n2\n1'},skillCheck:['Memprediksi jumlah iterasi.','Menjelaskan stop range tidak ikut.','Memperbaiki syntax blok for.']},
    {label:'While Loop',term:'while',icon:'⏳',mastery:'Mengulang selama kondisi True dan memperbarui state.',goal:'Menulis while loop yang berhenti karena kondisi akhirnya False.',success:'loop selesai tanpa infinite loop dan perubahan state dapat dijelaskan.',formal:'<code>while</code> mengevaluasi kondisi sebelum setiap iterasi. Body berjalan selama kondisi True. Program harus mengubah state atau memiliki jalan lain agar kondisi dapat menjadi False.',accuracy:'while tidak otomatis menghitung iterasi; programmer bertanggung jawab pada kondisi dan update.',model:[{title:'Cek',body:'Evaluasi kondisi.'},{title:'Run',body:'Jika True, jalankan body.'},{title:'Update',body:'Ubah state.'},{title:'Cek lagi',body:'Berhenti saat False.'}],analogy:{title:'Isi Botol',body:'Tuang selama botol belum penuh, lalu berhenti.',boundary:'Komputer tidak melihat keadaan dunia kecuali state dinyatakan dalam variable.'},example:{code:'hitung = 3\nwhile hitung > 0:\n    print(hitung)\n    hitung = hitung - 1\nprint("Mulai!")',output:'3\n2\n1\nMulai!'},predict:{prompt:'Apa yang terjadi tanpa update?',code:'x = 1\nwhile x > 0:\n    print(x)',answer:'Infinite loop karena x selalu 1.'},do:['Tentukan state awal.','Pastikan ada update menuju False.','Uji dengan nilai kecil.'],dont:['Membuat kondisi selalu True tanpa kontrol.','Lupa indentasi update.','Menutup terminal tanpa membaca penyebab.'],debug:{check:'state awal, kondisi, dan update',fix:'trace state per iterasi lalu hentikan terminal bila loop tak berakhir',error:'Infinite loop (tanpa pesan error)',cause:'kondisi tidak pernah menjadi False'},guided:[{title:'Hitung 1–3',prompt:'Gunakan while untuk 1 sampai 3.',solution:'angka = 1\nwhile angka < 4:\n    print(angka)\n    angka = angka + 1',output:'1\n2\n3'},{title:'Energi Turun',prompt:'Mulai 3, kurangi sampai 0.',solution:'energi = 3\nwhile energi > 0:\n    print(energi)\n    energi = energi - 1'},{title:'Dua Percobaan',prompt:'Ulangi pesan dua kali.',solution:'percobaan = 0\nwhile percobaan < 2:\n    print("Coba")\n    percobaan = percobaan + 1'}],bug:{title:'Update ke arah salah',code:'x = 3\nwhile x > 0:\n    print(x)\n    x = x + 1',error:'Output terus membesar.',cause:'x menjauh dari kondisi False.',fix:'x = 3\nwhile x > 0:\n    print(x)\n    x = x - 1',output:'3\n2\n1'},independent:{title:'Baterai Menurun',prompt:'Mulai baterai 30 dan kurangi 10 sampai 0.',requirements:['while','update -10','berhenti'],hints:['Kondisi baterai > 0','Cetak sebelum update'],solution:'baterai = 30\nwhile baterai > 0:\n    print(baterai)\n    baterai = baterai - 10\nprint("Isi daya")',output:'30\n20\n10\nIsi daya'},skillCheck:['Menjelaskan kondisi dicek sebelum iterasi.','Menemukan infinite loop.','Memilih for atau while sesuai kebutuhan.']}
  ],
  guidedProjects:[
    {title:'Tabel Perkalian 5',problem:'Gunakan for untuk 1×5 sampai 5×5.',requirements:['range','expression'],solution:'for i in range(5):\n    angka = i + 1\n    print(angka * 5)',output:'5\n10\n15\n20\n25',connection:'Operators dipakai di dalam loop.'},
    {title:'Peluncuran Roket',problem:'Countdown while lalu tampilkan “Meluncur!”.',requirements:['state menurun','output akhir'],solution:'detik = 3\nwhile detik > 0:\n    print(detik)\n    detik = detik - 1\nprint("Meluncur!")',connection:'Kondisi mengontrol pengulangan.'},
    {title:'Dadu Tiga Kali',problem:'Panggil random.randint di dalam for tiga kali.',requirements:['import random','for'],solution:'import random\nfor i in range(3):\n    print(random.randint(1, 6))',connection:'Loop mengulang aksi random.'}
  ],
  independentProject:{title:'Training Counter',mission:'Buat pelatih terminal yang mengulang instruksi dan countdown istirahat.',icon:'🏋️',requirements:['Satu for loop','Satu while loop','Output jelas','Tidak infinite'],starter:'for ronde in range(3):\n    # pesan latihan\n    pass\n\nistirahat = 3\n# buat countdown while',hints:['Ganti pass dengan print','Kurangi state while','Uji bagian for dan while terpisah'],acceptance:['For berjalan tiga kali','While berhenti','Urutan output masuk akal'],bonus:['Panggil satu function di dalam loop','Tambahkan poin acak']},
  debugRecap:'cek iterable/range, kondisi, update state, titik dua, dan indentasi.',takeaways:['for cocok untuk iterable/jumlah terencana.','range stop tidak ikut.','while berjalan selama kondisi True dan memerlukan update state.'],exitTicket:'Kapan kamu memilih while daripada for?',preview:'Kita akan menyimpan banyak value dalam list lalu memilih item secara acak.',quote:{text:'The only way to learn a new programming language is by writing programs in it.',author:'Dennis Ritchie'}
};

conceptMeetings[8] = {
  meeting:8,title:'Random & Lists',unit:'Unit 2 · Logic & Control Flow',icon:'🎒',mission:'Simpan banyak item dalam satu list dan pilih satu item secara acak.',intro:'List menjadi koleksi sederhana untuk data sejenis. Random akan memilih item tanpa kita menulis banyak cabang.',
  review:[
    {type:'Predict Output',title:'range()',prompt:'Nilai apa yang tampil?',snippet:'for i in range(3):\n    print(i)',answer:'0, 1, 2.'},
    {type:'Find the Bug',title:'Infinite Loop',prompt:'Apa yang hilang?',snippet:'x = 3\nwhile x > 0:\n    print(x)',answer:'Update seperti x = x - 1.'},
    {type:'Concept Quiz',title:'Pilih Loop',prompt:'Mengulang tepat lima kali paling langsung memakai…',choices:['for range(5)','while True','if'],correct:0,answer:'for range(5).'},
    {type:'Complete Code',title:'Body Loop',prompt:'Lengkapi tanda: for i in range(2)__',answer:'Titik dua (:).'},
    {type:'Explain',title:'State While',prompt:'Mengapa state harus berubah?',answer:'Agar kondisi punya kesempatan menjadi False dan loop berhenti.'}
  ],
  objectives:[
    {label:'List Basics',term:'list dan index',icon:'🧺',mastery:'Membuat list dan mengambil item dengan index.',goal:'Menyimpan minimal empat item dalam list dan mengaksesnya dengan index yang valid.',success:'item pertama dan terakhir yang diminta tampil tanpa IndexError.',formal:'List adalah sequence mutable yang menyimpan referensi item secara berurutan. Literal list memakai <code>[ ]</code>; index dimulai dari 0.',accuracy:'Index 0 adalah item pertama. List dapat berisi banyak item; variable list merujuk koleksi tersebut.',model:[{title:'Buat',body:'Evaluasi item dalam [ ].'},{title:'Urutkan',body:'Pertahankan posisi.'},{title:'Index',body:'Cari posisi mulai 0.'},{title:'Return',body:'Berikan item di posisi itu.'}],analogy:{title:'Rak Bernomor',body:'Setiap barang berada pada slot berurutan.',boundary:'Nomor slot Python dimulai 0 dan akses di luar rentang adalah error.'},example:{code:'planet = ["Novara", "Modula", "Archius"]\nprint(planet[0])\nprint(planet[2])',output:'Novara\nArchius'},predict:{prompt:'Apa output buah[1]?',code:'buah = ["apel", "mangga", "jeruk"]\nprint(buah[1])',answer:'mangga.'},do:['Pisahkan item dengan koma.','Gunakan kutip untuk String.','Hitung index mulai 0.'],dont:['Memakai parentheses untuk literal list.','Mengakses index yang tidak ada.','Menganggap index mulai 1.'],debug:{check:'bracket, koma, dan rentang index',fix:'hitung posisi mulai 0',error:'IndexError',cause:'index berada di luar panjang list'},guided:[{title:'List Hobi',prompt:'Buat tiga hobi dan tampilkan pertama.',solution:'hobi = ["baca", "gambar", "musik"]\nprint(hobi[0])',output:'baca'},{title:'Item Tengah',prompt:'Tampilkan item index 1.',solution:'warna = ["biru", "kuning", "hijau"]\nprint(warna[1])',output:'kuning'},{title:'Loop List',prompt:'Tampilkan tiap item dengan for.',solution:'menu = ["roti", "susu", "buah"]\nfor item in menu:\n    print(item)',output:'roti\nsusu\nbuah'}],bug:{title:'Index terlalu besar',code:'tim = ["Ari", "Bela", "Cici"]\nprint(tim[3])',error:'IndexError: list index out of range',cause:'Index valid hanya 0,1,2.',fix:'tim = ["Ari", "Bela", "Cici"]\nprint(tim[2])',output:'Cici'},independent:{title:'Playlist Mini',prompt:'Buat list empat lagu fiksi lalu tampilkan pilihan ke-1 dan ke-4.',requirements:['Empat String','Index valid','Dua output'],hints:['Ke-1 index 0','Ke-4 index 3'],solution:'lagu = ["Orbit", "Nova", "Komet", "Cahaya"]\nprint(lagu[0])\nprint(lagu[3])',output:'Orbit\nCahaya'},skillCheck:['Menjelaskan list sebagai sequence.','Menghitung index dari 0.','Memperbaiki IndexError.']},
    {label:'Random Choice from List',term:'random.choice()',icon:'🎯',mastery:'Memilih satu item acak dari list non-kosong.',goal:'Menggunakan random.choice() pada list dan menjelaskan kemungkinan output.',success:'hasil selalu salah satu item list dan dapat berubah antar-run.',formal:'<code>random.choice(sequence)</code> mengembalikan satu item dari sequence non-kosong dengan pemilihan pseudo-random.',accuracy:'choice mengembalikan item, bukan index; list kosong menyebabkan IndexError.',model:[{title:'Import',body:'Muat random.'},{title:'List',body:'Siapkan kandidat.'},{title:'Choice',body:'Pilih satu posisi valid.'},{title:'Return',body:'Kembalikan item.'}],analogy:{title:'Undian Nama',body:'Satu kertas dipilih dari wadah kandidat.',boundary:'Pemilihan pseudo-random dan kandidat harus sudah ada di list.'},example:{code:'import random\nwarna = ["biru", "kuning", "hijau"]\npilihan = random.choice(warna)\nprint(pilihan)',output:'Salah satu: biru / kuning / hijau'},predict:{prompt:'Bisakah output menjadi merah?',code:'opsi = ["biru", "kuning"]\nprint(random.choice(opsi))',answer:'Tidak, karena merah tidak ada dalam list.'},do:['Pastikan list tidak kosong.','Import random.','Simpan pilihan bila dipakai lagi.'],dont:['Mengharapkan urutan tertentu.','Memanggil choice pada [].','Menganggap choice menghapus item.'],debug:{check:'import, nama list, dan apakah list berisi item',fix:'isi list atau perbaiki nama',error:'IndexError: Cannot choose from an empty sequence',cause:'random.choice menerima list kosong'},guided:[{title:'Pilih Snack',prompt:'Pilih satu dari tiga snack.',solution:'import random\nsnack = ["roti", "buah", "yogurt"]\nprint(random.choice(snack))'},{title:'Misi Acak',prompt:'Simpan hasil choice lalu pakai f-string.',solution:'import random\nmisi = ["scan", "jelajah", "riset"]\npilihan = random.choice(misi)\nprint(f"Misi: {pilihan}")'},{title:'Tiga Pilihan',prompt:'Gunakan for untuk melakukan choice tiga kali.',solution:'import random\nwarna = ["biru", "kuning", "hijau"]\nfor i in range(3):\n    print(random.choice(warna))'}],bug:{title:'List kosong',code:'import random\nopsi = []\nprint(random.choice(opsi))',error:'IndexError',cause:'Tidak ada kandidat untuk dipilih.',fix:'import random\nopsi = ["A", "B"]\nprint(random.choice(opsi))'},independent:{title:'Rekomendasi Aktivitas',prompt:'Pilih satu aktivitas acak dan tampilkan personal.',requirements:['List minimal empat','random.choice','f-string'],hints:['Import paling atas','Simpan hasil choice'],solution:'import random\nnama = "Nara"\naktivitas = ["membaca", "jalan kaki", "menggambar", "merapikan meja"]\npilihan = random.choice(aktivitas)\nprint(f"{nama}, coba {pilihan} hari ini!")'},skillCheck:['Menjelaskan hasil harus berasal dari list.','Membedakan choice dan randint.','Mendiagnosis list kosong.']}
  ],
  guidedProjects:[
    {title:'Generator Menu',problem:'Pilih menu acak dari list.',requirements:['Empat menu','f-string'],solution:'import random\nmenu = ["nasi", "sup", "roti", "salad"]\npilihan = random.choice(menu)\nprint(f"Menu hari ini: {pilihan}")',connection:'List menyimpan kandidat; random memilih.'},
    {title:'Tim Acak',problem:'Pilih satu nama dari list tim.',requirements:['List nama fiksi','choice'],solution:'import random\ntim = ["Nova", "Luna", "Orion"]\nprint(random.choice(tim))',connection:'Mengakses item tanpa menulis index manual.'},
    {title:'Challenge Spinner',problem:'Function memilih tantangan acak.',requirements:['def','choice','function call'],solution:'import random\ndef pilih_tantangan():\n    tantangan = ["10 squat", "baca 5 menit", "rapikan meja"]\n    print(random.choice(tantangan))\n\npilih_tantangan()',connection:'Menggabungkan Meetings 6–8.'}
  ],
  independentProject:{title:'Novara Random Recommender',mission:'Buat rekomendasi acak berdasarkan daftar buatanmu.',icon:'🎁',requirements:['List minimal lima item','random.choice','Satu function','Input nama','f-string hasil'],starter:'import random\n\ndef rekomendasi():\n    pilihan = ["...", "..."]\n    # pilih dan tampilkan\n\nrekomendasi()',hints:['Isi list sebelum choice','Simpan result','Uji beberapa kali'],acceptance:['Hasil selalu anggota list','Function dipanggil','Tidak ada list kosong'],bonus:['Jalankan rekomendasi tiga kali dengan loop','Pakai if untuk respons pada satu item khusus']},
  debugRecap:'cek bracket/koma, index mulai 0, list kosong, import, dan nama sequence.',takeaways:['List menyimpan item berurutan dan mutable.','Index dimulai 0.','random.choice mengembalikan satu item dari sequence non-kosong.'],exitTicket:'Apa perbedaan random.randint(1, 3) dan random.choice(["A", "B", "C"])?',preview:'Kita akan memetakan semua konsep Meeting 1–8 ke proposal final project yang realistis.',quote:{text:'Python is an experiment in how much freedom programmers need.',author:'Guido van Rossum'}
};

const projectMap = [
  'Meeting 1 → file .py dan print() untuk output terminal',
  'Meeting 2 → variable dan basic data types untuk menyimpan state',
  'Meeting 3 → operators untuk proses hitung',
  'Meeting 4 → input() dan f-string untuk interaksi',
  'Meeting 5 → comparison dan if–else untuk keputusan',
  'Meeting 6 → elif, function, dan random untuk aksi terstruktur',
  'Meeting 7 → for/while untuk pengulangan',
  'Meeting 8 → list dan random.choice untuk banyak data'
];

function workshopItem(meeting, section, label, item) {
  const body = item.template
    ? `${item.intro ? `<p>${item.intro}</p>` : ''}<pre class="code copy-ready" id="${item.copyId}">${esc(item.template)}</pre><button class="copy-btn" type="button" data-copy-target="${item.copyId}">Salin framework</button><div class="feedback" aria-live="polite">Jika clipboard diblokir, pilih teks lalu salin manual.</div>`
    : `${item.lead ? `<p class="lead">${item.lead}</p>` : ''}${item.bullets ? list(item.bullets,item.ordered) : ''}${item.extra || ''}`;
  return makeSlide(meeting,`m${meeting}-${section}`,label,item.title,item.subtitle || 'Final Project Level 1',`<div class="panel ${item.tone||''}">${body}</div>${item.mode ? modeNote(item.mode) : ''}`);
}

function workshopCover(meeting,title,mission,icon) {
  return makeSlide(meeting,`m${meeting}-opening`,'Opening',`Meeting ${meeting}: ${title}`,'Unit 3 · Final Project Level 1',
    `<div class="hero"><div><p class="eyebrow">Project Workshop</p><h2>${mission}</h2><p class="lead">Project wajib memakai konsep yang sudah dipelajari pada Meetings 1–8. Bonus tidak boleh menghalangi MVP.</p>${modeNote('Kerja dapat dilakukan lewat screen share atau langsung di VS Code; simpan bukti lokal agar internet bukan syarat.')}</div><div class="hero-mark anim-bounce" aria-hidden="true">${icon}</div></div>`);
}

function workshopObjectives(meeting,items) {
  return makeSlide(meeting,`m${meeting}-objectives`,'Workshop Objectives','Workshop Objectives','Deliverable yang harus terlihat di akhir meeting',
    `<div class="grid-3">${items.map((x,i)=>`<div class="panel"><p class="eyebrow">Target ${i+1}</p><h3>${x}</h3></div>`).join('')}</div>`);
}

const m9Reviews = [
  {type:'Flashback',title:'Output & Data',prompt:'Sebutkan satu fitur proyek yang memakai print dan variable.',answer:'Contoh: kartu skor menyimpan skor lalu print menampilkannya.'},
  {type:'Flashback',title:'Process',prompt:'Operator apa yang dibutuhkan kalkulator total harga?',answer:'Minimal * untuk subtotal dan + untuk total.'},
  {type:'Flashback',title:'Decision',prompt:'Bagaimana program memilih respons benar/salah?',answer:'Comparison menghasilkan Boolean lalu if–else memilih cabang.'},
  {type:'Flashback',title:'Automation',prompt:'Kapan for lebih cocok daripada while?',answer:'Saat jumlah pengulangan atau iterable sudah jelas.'},
  {type:'Flashback',title:'Collection & Random',prompt:'Bagaimana memilih satu item dari banyak kandidat?',answer:'Simpan kandidat dalam list non-kosong lalu gunakan random.choice().'}
];

const m9Phases = {
  'inspiration|Inspiration & Discovery':[
    {title:'Galeri Ide yang Realistis',bullets:['Quiz terminal 3 soal','Kalkulator tabungan dengan angka input sebagai bonus terbimbing','Petualangan pilihan teks','Random activity recommender','Score challenge dengan loop'],extra:'<div class="callout">Semua ide berakhir di terminal dan dapat dibuat tanpa library baru.</div>'},
    {title:'Batas Teknologi Level 1',bullets:['Wajib: basic Python Meetings 1–8','Tidak wajib: GUI, file/database, web, API','Jangan menjanjikan akun/login sungguhan atau multiplayer'],tone:'red'},
    {title:'Temukan Masalah Kecil',lead:'Pilih masalah yang dapat dibantu program terminal dalam beberapa menit.',bullets:['Siapa yang mengalami masalah?','Apa keputusan atau hitungan yang berulang?','Output apa yang benar-benar membantu?']},
    {title:'Kenali Target User',bullets:['Tuliskan satu jenis pengguna, bukan “semua orang”','Nyatakan kebutuhan pengguna dalam satu kalimat','Hindari meminta data pribadi nyata'],extra:reveal('Contoh', '<p>“Siswa yang bingung memilih aktivitas istirahat membutuhkan rekomendasi sederhana.”</p>')},
    {title:'Input–Process–Output Ide',bullets:['Input: data apa yang diberikan?','Process: hitung, bandingkan, ulangi, atau acak?','Output: apa yang terlihat di terminal?'],extra:'<div class="flow"><div><strong>Input</strong>nama/pilihan</div><div><strong>Process</strong>condition/loop</div><div><strong>Output</strong>pesan/hasil</div></div>'},
    {title:'Cek Keamanan Ide',bullets:['Gunakan nama panggilan atau data fiksi','Jangan menyimpan password sungguhan','Jangan menyalin karya orang lain tanpa memahami'],tone:'yellow'}
  ],
  'ideation|Idea Generation & Selection':[
    {title:'Brainstorm 3×3',bullets:['Tulis 3 masalah','Untuk tiap masalah, tulis 3 solusi terminal','Jangan menilai ide selama dua menit pertama'],mode:'Online: ketik di dokumen bersama. Offline: gunakan sembilan sticky notes.'},
    {title:'Gabungkan Konsep',bullets:['Input + if–else → quiz','Operators + variable → calculator','List + random → recommender','Loop + score → challenge berulang']},
    {title:'Matriks Pilihan',bullets:['Berguna bagi target user','Memakai konsep yang dikuasai','Selesai dalam Meetings 9–11','Mudah didemokan tanpa internet']},
    {title:'Skor Ide 1–3',bullets:['Manfaat: 1 rendah, 3 jelas','Kesulitan: 1 sulit, 3 mudah','Kesesuaian syllabus: 1 lemah, 3 kuat','Pilih total tertinggi']},
    {title:'Feasible vs Over-scoped',extra:panels([{title:'Feasible ✅',body:'<p>Quiz terminal tiga soal dan skor.</p>',tone:'green'},{title:'Over-scoped ⛔',body:'<p>Game online multiplayer dengan akun dan database.</p>',tone:'red'}])},
    {title:'Kalimat Solusi',lead:'Lengkapi: “Program saya membantu [user] untuk [tujuan] dengan [cara].”',extra:reveal('Contoh', '<p>Program saya membantu siswa memilih kegiatan istirahat dengan rekomendasi acak dari list.</p>')}
  ],
  'mvp|MVP & Syllabus Mapping':[
    {title:'Apa itu MVP?',lead:'Minimum Viable Product adalah versi terkecil yang sudah menyelesaikan masalah inti dan dapat didemokan.',bullets:['Berjalan dari awal sampai akhir','Tiga fitur wajib bekerja','Bonus boleh belum ada']},
    {title:'Aturan 3 Fitur MVP',bullets:['Fitur 1 — menerima input yang dibutuhkan','Fitur 2 — memproses dengan hitung/condition/loop/random','Fitur 3 — menampilkan output yang berguna'],tone:'green'},
    {title:'Required vs Bonus',extra:panels([{title:'Required',body:'<p>Harus ada agar solusi bekerja.</p>',tone:'green'},{title:'Silver Bonus',body:'<p>Polish kecil memakai konsep yang sudah dipelajari.</p>'},{title:'Gold Bonus',body:'<p>Tambahan setelah semua test MVP lolos.</p>',tone:'yellow'}])},
    {title:'Traceability Map Meetings 1–4',bullets:projectMap.slice(0,4)},
    {title:'Traceability Map Meetings 5–8',bullets:projectMap.slice(4)},
    {title:'Feature → Concept',lead:'Setiap fitur wajib harus memiliki satu atau lebih sumber konsep Meetings 1–8.',extra:'<div class="flow"><div><strong>Input nama</strong>M4 input()</div><div><strong>Cek pilihan</strong>M5 if–else</div><div><strong>Rekomendasi</strong>M8 list + choice</div></div>'},
    {title:'Dependency Check',bullets:['Apakah butuh internet? Ubah agar tidak.','Apakah butuh library baru? Jadikan bonus atau hapus.','Apakah butuh data pribadi? Ganti data fiksi.','Apakah satu fitur bergantung fitur lain? Bangun yang dasar dulu.']},
    {title:'MVP Approval Gate',bullets:['Masalah dan user jelas','Tepat tiga fitur MVP','Semua fitur terhubung syllabus','Core flow dapat selesai di terminal','Risiko dan fallback tertulis'],extra:'<div class="callout">Jika satu belum lolos, kecilkan scope sebelum coding.</div>'}
  ],
  'flow|Program Flow & Design':[
    {title:'Alur Utama Program',bullets:['Start','Tampilkan judul','Terima input','Process','Tampilkan output','End atau loop yang jelas'],ordered:true},
    {title:'Pseudocode, Bukan Python Penuh',lead:'Pseudocode menuliskan logika dengan bahasa sederhana sebelum syntax.',extra:code('MULAI\nTANYA nama\nPILIH rekomendasi dari list\nTAMPILKAN rekomendasi untuk nama\nSELESAI')},
    {title:'Flowchart Simbol Minimum',bullets:['Oval: mulai/selesai','Jajar genjang: input/output','Kotak: process','Belah ketupat: decision','Panah: urutan']},
    {title:'Decision Path Test',bullets:['Jalur kondisi True','Jalur kondisi False','Setiap elif','Input yang tidak sesuai petunjuk'],extra:'<div class="callout">Gambar satu panah untuk setiap cabang.</div>'},
    {title:'Data Plan',bullets:['Nama variable','Contoh value','Tipe data','Siapa yang mengubah value','Di mana value dipakai']},
    {title:'Function Plan',bullets:['Pilih aksi berulang atau bagian yang punya tujuan jelas','Gunakan nama kata kerja','Tulis input/output function bila ada—parameter belum wajib']},
    {title:'Risk Board',bullets:['Risk: input berbeda kapital','Risk: infinite loop','Risk: list kosong','Risk: scope terlalu besar','Tulis pencegahan atau fallback untuk tiap risk']}
  ],
  'framework|Copy-ready Planning Framework':[
    {title:'Framework Google Docs — Bagian 1',copyId:'m9-template-1',intro:'Salin teks ini ke Google Docs atau dokumen lokal.',template:'NAMA PROYEK:\nMASALAH:\nTARGET USER:\nSOLUSI YANG DIUSULKAN:\n\n3 FITUR MVP:\n1.\n2.\n3.\n\nBONUS SILVER:\nBONUS GOLD:'},
    {title:'Framework Google Docs — Bagian 2',copyId:'m9-template-2',template:'KONSEP MEETINGS 1–8 YANG DIPAKAI:\n- Fitur 1 →\n- Fitur 2 →\n- Fitur 3 →\n\nPROGRAM FLOW (INPUT–PROCESS–OUTPUT):\nInput:\nProcess:\nOutput:'},
    {title:'Framework Google Docs — Bagian 3',copyId:'m9-template-3',template:'ASSET/DATA YANG DIBUTUHKAN:\n\nPOSSIBLE ERRORS / RISKS:\n1.\n2.\n3.\n\nFALLBACK:'},
    {title:'Framework Google Docs — Milestones',copyId:'m9-template-4',template:'MILESTONE MEETING 9: proposal disetujui\nMILESTONE MEETING 10: core mechanic/MVP bekerja\nMILESTONE MEETING 11: test, polish, README, presentasi siap\n\nBUKTI PROGRES:\n- screenshot / output:\n- build journal:'},
    {title:'Definition of Done',copyId:'m9-template-5',template:'DEFINITION OF DONE:\n[ ] Tiga fitur MVP bekerja\n[ ] Jalur positif dan negatif diuji\n[ ] Tidak ada error yang diketahui pada demo utama\n[ ] Output mudah dibaca\n[ ] README singkat selesai\n[ ] Screenshot/video backup tersedia\n[ ] Pitch dan PPT siap'}
  ],
  'approval|Approval & Milestones':[
    {title:'Proposal Peer Check',bullets:['Teman dapat menjelaskan masalahmu','Teman menemukan tiga fitur MVP','Teman dapat menunjuk konsep sumber tiap fitur'],mode:'Online: komentar dokumen. Offline: tukar lembar proposal.'},
    {title:'Milestone Board',bullets:['Hari ini: proposal + flow + DoD','Meeting 10: MVP/core mechanic + pitch draft','Meeting 11: tested, polished, documented, rehearsed']},
    {title:'Status Akhir Meeting 9',extra:panels([{title:'READY',body:'<p>Semua approval gate lolos.</p>',tone:'green'},{title:'REVISE',body:'<p>Scope perlu dikecilkan atau mapping belum jelas.</p>',tone:'yellow'},{title:'BLOCKED',body:'<p>Dependency tidak tersedia; pilih fallback.</p>',tone:'red'}])}
  ],
  'closing|Reflection & Closing':[
    {title:'Debugging Sebelum Coding',bullets:['Debug ide: apakah solusi menjawab masalah?','Debug scope: dapatkah MVP selesai?','Debug flow: adakah cabang buntu?','Ubah satu keputusan per revisi.']},
    {title:'Exit Ticket Proposal',lead:'Sebutkan proyekmu, target user, tiga fitur MVP, dan satu risiko dalam 45 detik.',mode:'Rekam voice note saat online atau presentasi ke pasangan saat offline.'}
  ]
};

function buildMeeting9() {
  let slides=[workshopCover(9,'Flashback & Proyek Akhir','Keluar dengan proposal feasible, tiga fitur MVP, dan program flow yang disetujui.','🧭')];
  m9Reviews.forEach((x,i)=>slides.push(reviewSlide(9,i,x)));
  slides.push(workshopObjectives(9,['Memilih masalah dan target user yang jelas.','Memetakan tiga fitur MVP ke Meetings 1–8.','Menyelesaikan flow, risks, milestones, dan definition of done.']));
  Object.entries(m9Phases).forEach(([key,items])=>{const [sec,label]=key.split('|'); items.forEach(item=>slides.push(workshopItem(9,sec,label,item)));});
  slides.push(makeSlide(9,'m9-closing','Reflection & Closing','Quote of the Day','Rencanakan yang bisa dibangun',`<div class="quote"><div><blockquote>“The most important single aspect of software development is to be clear about what you are trying to build.”</blockquote><cite>— Bjarne Stroustrup</cite></div></div>`));
  if(slides.length!==45) throw new Error(`Meeting 9 slide count ${slides.length}, expected 45`);
  return slides;
}

const pair = (title,lead,bullets=[]) => ({title,lead,bullets});
function addPairs(slides,m,sec,label,pairs){ pairs.forEach(x=>slides.push(workshopItem(m,sec,label,x))); }
function statusReviews(meeting,items){ return items.map((x,i)=>reviewSlide(meeting,i,{type:'Status Check',title:x[0],prompt:x[1],answer:x[2]||'Tunjukkan bukti konkret di file, terminal, journal, atau screenshot.'})); }

function buildMeeting10(){
  let s=[workshopCover(10,'Core Build & Pitch Draft','Keluar dengan core mechanic/MVP yang bekerja, bukti progres, dan pitch 45–60 detik.','💻')];
  s.push(...statusReviews(10,[
    ['Proposal','Bisakah kamu menunjukkan proposal dan tiga fitur MVP?','Bukti: proposal Meeting 9 dengan mapping syllabus.'],
    ['Flow','Di bagian mana input, process, dan output terjadi?','Tunjukkan pada pseudocode/flowchart.'],
    ['Dependency','Apakah semua kebutuhan tersedia offline?','Jika tidak, aktifkan fallback sebelum build.'],
    ['First Build','Apa potongan terkecil yang dapat diuji dalam 15 menit?','Pilih satu output atau core decision, bukan seluruh proyek.']
  ]));
  s.push(workshopObjectives(10,['Menyiapkan folder dan build order.','Menyelesaikan core mechanic/MVP serta test-as-you-build.','Membuat bukti progres, pitch draft, dan outline PPT.']));
  addPairs(s,10,'setup','Setup & Build Plan',[
    pair('Folder Verification','Buka satu folder proyek yang berisi file utama .py, proposal, dan folder evidence.', ['Nama file tanpa spasi berlebihan','Tidak ada password/token','Path mudah ditemukan saat demo']),
    pair('Environment Verification','Jalankan python --version dan satu print sederhana sebelum coding panjang.'),
    pair('Naming Plan','Pilih main.py atau nama proyek yang jelas; jangan membuat lima file untuk proyek Level 1.'),
    pair('Backup Awal','Duplikasi folder dengan nama bertanggal atau simpan salinan aman sebelum perubahan besar.'),
    pair('Build Journal','Catat waktu, perubahan, hasil test, dan next step dalam empat baris setiap checkpoint.'),
    pair('Build Order','Urutkan: output statis → input → process → condition/loop/random → output final.',[],)
  ]);
  addPairs(s,10,'build','Implementation Checkpoints',[
    pair('Checkpoint 1 — Program Opens','File berjalan dan menampilkan judul tanpa error.'),
    pair('Checkpoint 2 — Input Arrives','Semua prompt jelas dan jawaban tersimpan dengan nama variable konsisten.'),
    pair('Checkpoint 3 — Core Process','Satu perhitungan, decision, loop, atau random choice menghasilkan value yang benar.'),
    pair('Checkpoint 4 — Output Explains Result','f-string menampilkan hasil beserta konteks, bukan angka tanpa label.'),
    pair('Checkpoint 5 — True Path','Uji input yang membuat kondisi utama True dan catat output.'),
    pair('Checkpoint 6 — False Path','Uji input lain agar else benar-benar berjalan.'),
    pair('Checkpoint 7 — Every elif','Buat satu test untuk setiap elif; cabang yang tidak diuji belum dianggap selesai.'),
    pair('Checkpoint 8 — Loop Stops','Trace state dan buktikan while berhenti atau for memiliki jumlah iterasi tepat.'),
    pair('Checkpoint 9 — Random Bounds','Jalankan beberapa kali; hasil randint/choice tetap dalam kandidat.'),
    pair('Checkpoint 10 — Function Call','Pastikan function didefinisikan sebelum call dan body benar-benar berjalan.'),
    pair('Checkpoint 11 — Feature 1 Done','Tandai done hanya bila acceptance criteria fitur 1 terlihat.'),
    pair('Checkpoint 12 — Feature 2 Done','Hubungkan process tanpa merusak fitur 1; run ulang regression test.'),
    pair('Checkpoint 13 — Feature 3 Done','Output akhir membuat MVP dapat dipakai dari awal sampai akhir.'),
    pair('Starter Architecture Boundary','Gunakan urutan sederhana: import → function bila perlu → variable/list → input → process → output. Ini kerangka, bukan final answer.'),
    pair('Working MVP Gate','MVP bekerja jika tiga fitur wajib dapat didemokan berurutan tanpa mengedit kode saat demo.')
  ]);
  addPairs(s,10,'debug','Debugging Clinic & Tests',[
    pair('Clinic: NameError','Cari typo atau nama yang dipakai sebelum assignment; samakan ejaan persis.'),
    pair('Clinic: TypeError','Cetak type() dan periksa apakah digit dari input masih str; jangan menambah konsep baru tanpa dukungan.'),
    pair('Clinic: IndentationError','Rapikan satu blok menjadi empat spasi; jangan campur tab dan spasi.'),
    pair('Clinic: Infinite Loop','Hentikan run, trace state, lalu perbaiki update menuju kondisi False.'),
    pair('Test-as-you-build','Setelah satu perubahan kecil: save → run → input test → compare expected → journal.')
  ]);
  addPairs(s,10,'evidence','Progress Evidence',[
    pair('Screenshot 1','Ambil bukti terminal menampilkan core mechanic, bukan hanya kode.'),
    pair('Screenshot 2','Ambil satu jalur berbeda atau hasil random lain.'),
    pair('Build Journal Entry','Tulis: yang dibuat, yang bekerja, error, fix, langkah berikutnya.'),
    pair('Checkpoint Demo','Jelaskan satu bagian kode tanpa membaca semua baris.',[],)
  ]);
  addPairs(s,10,'pitch','Pitch Draft & PPT Outline',[
    pair('Elevator Pitch Formula','Hook → problem/user → solution → key feature → impact/call to action.'),
    pair('Level 1 Pitch Example','“Bingung memilih istirahat? RehatKu membantu siswa mendapat rekomendasi acak dari list dalam beberapa detik.”'),
    pair('45–60 Second Draft','Targetkan 90–130 kata; gunakan bahasa sendiri dan satu contoh hasil terminal.'),
    pair('PPT Outline Awal','Slide 1 judul; 2 masalah/user; 3 solusi; 4 flow; 5 fitur/demo; 6 learning/reflection.'),
    pair('Code Explanation Plan','Pilih satu potongan: input–process–output atau condition/loop. Jelaskan tujuan dan alur, bukan setiap karakter.')
  ]);
  addPairs(s,10,'closing','Reflection & Closing',[
    pair('MVP Checklist','Tiga fitur berjalan, test positif/negatif ada, bukti progres tersimpan.'),
    pair('Exit Ticket','Demo core mechanic selama 30 detik dan sebutkan satu bug beserta fix.'),
    pair('Prepare Meeting 11','Bawa folder, journal, daftar bug, pitch draft, dan outline PPT.')
  ]);
  s.push(makeSlide(10,'m10-closing','Reflection & Closing','Quote of the Day','Bangun inti dulu',`<div class="quote"><div><blockquote>“Make it work, make it right, make it fast.”</blockquote><cite>— Kent Beck</cite></div></div>`));
  if(s.length!==45) throw new Error(`Meeting 10 slide count ${s.length}, expected 45`); return s;
}

function buildMeeting11(){
  let s=[workshopCover(11,'Completion, Testing & Presentation','Keluar dengan proyek presentation-ready, QA evidence, README, backup demo, dan rehearsal.','🧪')];
  s.push(...statusReviews(11,[['MVP Demo','Bisakah proyek berjalan dari awal sampai akhir?'],['Known Bugs','Apa error yang masih terbuka dan dampaknya?'],['Evidence','Di mana screenshot dan build journal tersimpan?'],['Pitch Draft','Bisakah problem, user, solution dijelaskan dalam 45–60 detik?']]));
  s.push(workshopObjectives(11,['Menyelesaikan required features.','Menguji, memulihkan kegagalan, dan polish output.','Menyiapkan README, backup demo, PPT, pitch, dan rehearsal.']));
  addPairs(s,11,'complete','Required Feature Completion',[
    pair('Freeze Scope','Hentikan fitur baru dan hapus janji fitur yang belum bekerja; required MVP lebih penting daripada bonus.'),pair('Feature 1 Acceptance','Jalankan acceptance criteria fitur pertama dan simpan hasil.'),pair('Feature 2 Acceptance','Uji process/decision pada lebih dari satu input.'),pair('Feature 3 Acceptance','Pastikan output akhir jelas bagi target user.'),pair('Integration Run','Jalankan tiga fitur berurutan tanpa reset manual.')
  ]);
  addPairs(s,11,'qa','QA & Test Cases',[
    pair('QA Mindset','Expected dan actual harus dibandingkan; “tidak crash” belum cukup.'),pair('Positive Test','Gunakan input normal yang seharusnya berhasil.'),pair('Negative Test','Gunakan pilihan salah atau value batas untuk menguji fallback.'),pair('Boundary Test','Uji angka tepat di sekitar > atau <.'),pair('Case-sensitive Test','Uji variasi kapital bila petunjuk input berpotensi membingungkan.'),pair('Loop Test','Hitung iterasi dan buktikan loop berhenti.'),pair('Random Test','Run minimal lima kali; semua hasil tetap valid.'),pair('Regression Test','Setelah fix, jalankan ulang test fitur yang sebelumnya lolos.')
  ]);
  addPairs(s,11,'recovery','Debug & Failure Recovery',[
    pair('Read the Traceback','Mulai dari baris terakhir error lalu cari file dan nomor baris milikmu.'),pair('One Fix at a Time','Ubah satu penyebab, save, run, dan catat hasil.'),pair('Safe Restore','Jika fix merusak lebih banyak, kembali ke backup checkpoint terakhir.'),pair('Live Demo Failure','Tetap tenang, jelaskan expected behavior, lalu gunakan screenshot/video backup.'),pair('Known Limitation','Nyatakan batas program dengan jujur; jangan menyebut bug sebagai fitur.')
  ]);
  addPairs(s,11,'polish','Terminal Polish',[
    pair('Readable Prompts','Berikan contoh format jawaban dan spasi setelah titik dua.'),pair('Readable Output','Gunakan judul, label, dan f-string agar angka memiliki makna.'),pair('Consistent Language','Pilih istilah dan kapitalisasi yang sama sepanjang program.'),pair('No Sensitive Data','Ganti nama/password nyata dengan data fiksi atau panggilan.')
  ]);
  addPairs(s,11,'docs','Evidence & README',[
    pair('Screenshot Set','Simpan pembuka, fitur utama, dan satu jalur alternatif.'),pair('Backup Demo','Rekam video pendek atau rangkaian screenshot bila live run gagal.'),pair('README — What','Nama, masalah, target user, dan ringkasan solusi.'),pair('README — How','Cara membuka folder, menjalankan file, dan format input.'),pair('README — Limits','Fitur, batasan, serta konsep Meetings 1–8 yang digunakan.')
  ]);
  addPairs(s,11,'presentation','PPT 5–7 Slides',[
    pair('Slide 1 — Hook & Title','Satu hook, nama proyek, dan nama pembuat.'),pair('Slide 2 — Problem & User','Masalah nyata kecil dan target user spesifik.'),pair('Slide 3 — Solution & IPO','Tampilkan input–process–output.'),pair('Slide 4 — Key Code','Pilih condition/loop/random dan jelaskan tujuan.'),pair('Slide 5–6 — Demo & Tests','Tampilkan fitur, hasil, serta satu bukti QA.')
  ]);
  addPairs(s,11,'rehearsal','Pitch & Rehearsal',[
    pair('Refine Pitch','Buang detail yang tidak membantu problem, solution, feature, impact.'),pair('Rehearsal Protocol','Timer → pitch → demo → Q&A → feedback dua kekuatan/satu saran.'),pair('Peer Feedback','Gunakan prompt: jelas apa masalahnya? demo membuktikan fitur? penjelasan kode dapat dipahami?')
  ]);
  addPairs(s,11,'closing','Readiness & Closing',[
    pair('Final Readiness Status','READY: semua wajib lolos; READY WITH BACKUP: demo live berisiko tetapi bukti ada; REVISE: required feature belum bekerja.'),pair('Exit Ticket','Sebutkan satu positive test, satu negative test, dan hasil aktualnya.'),pair('Pack for Showcase','Folder final, backup, PPT, README, charger, dan catatan pitch.')
  ]);
  s.push(makeSlide(11,'m11-closing','Readiness & Closing','Quote of the Day','Debugging adalah berpikir dengan bukti',`<div class="quote"><div><blockquote>“The most effective debugging tool is still careful thought, coupled with judiciously placed print statements.”</blockquote><cite>— Brian Kernighan</cite></div></div>`));
  if(s.length!==45) throw new Error(`Meeting 11 slide count ${s.length}, expected 45`); return s;
}

function buildMeeting12(){
  const m=12; let s=[workshopCover(12,'Showcase & Presentasi','Presentasikan problem, solusi, kode Level 1, live demo, dan refleksi dengan percaya diri.','🎤')];
  const items=[
    ['check','Final Check','File Final','Buka folder final, jalankan file utama, dan jangan mengedit saat giliran dimulai.'],
    ['check','Final Check','Presentation-day Checklist','Laptop, charger, PPT, README, screenshot/video backup, serta timer sudah siap.'],
    ['present','Presenter Flow','Urutan Presentasi','Hook → problem/user → solution → IPO → key code → demo → learning → Q&A.'],
    ['present','Presenter Flow','Open with a Hook','Gunakan pertanyaan, situasi singkat, atau hasil mengejutkan—bukan meminta maaf.'],
    ['present','Presenter Flow','Problem & Target User','Sebutkan siapa yang dibantu dan masalah kecil yang benar-benar diselesaikan.'],
    ['present','Presenter Flow','Solution & Key Feature','Jelaskan solusi satu kalimat lalu tunjukkan fitur paling penting.'],
    ['code','Level 1 Code Explanation','Explain Input–Process–Output','Tunjuk baris input(), proses operator/condition/loop/random, lalu output print/f-string.'],
    ['code','Level 1 Code Explanation','Explain Condition Logic','Nyatakan kondisi, kapan True/False, dan cabang output yang berjalan.'],
    ['code','Level 1 Code Explanation','Explain Loop Logic','Nyatakan apa yang diulang, berapa lama, dan mengapa loop berhenti.'],
    ['code','Level 1 Code Explanation','Do Not Read Every Line','Pilih 5–10 baris penting; jelaskan tujuan, alur value, dan hasil.'],
    ['demo','Live Demo','Demo Sequence','Reset terminal → jalankan → isi input → tunjukkan core feature → tunjukkan hasil → hentikan dengan rapi.'],
    ['demo','Live Demo','Positive & Alternative Path','Bila waktu cukup, demo satu input normal dan satu cabang berbeda.'],
    ['demo','Live Demo','Backup Plan','Jika live app gagal: jelaskan gejala singkat, jangan debug lama, buka screenshot/video, lanjut presentasi.'],
    ['demo','Live Demo','Level 1 Visible Expectation','Terminal program berjalan; IPO terlihat; condition/loop logic dapat dijelaskan.'],
    ['timing','Time Management','Suggested Presenter Timing','Hook/problem 45 dtk; solution/code 90 dtk; demo 2 mnt; reflection 30 dtk; Q&A 1 mnt.'],
    ['criteria','Visible Criteria','Apa yang Audiens Lihat','Problem jelas, tiga fitur bekerja, kode dipahami, demo siap, komunikasi jujur.'],
    ['audience','Audience','Audience Etiquette','Dengarkan, jangan mengganggu perangkat, catat satu hal kuat, dan tunggu sesi tanya jawab.'],
    ['audience','Audience','Useful Peer Feedback','“Saya memahami…”, “Bukti fitur yang saya lihat…”, “Satu pertanyaan/saran…”'],
    ['qa','Q&A','Menjawab Pertanyaan','Ulangi inti pertanyaan, jawab singkat, lalu hubungkan ke kode atau demo.'],
    ['qa','Q&A','Saying I Don’t Know Yet','Katakan jujur: “Saya belum tahu. Saya akan mengecek bagian … setelah presentasi.”'],
    ['reflect','Reflection','Technical Reflection','Konsep mana paling membantu? Bug apa paling mengubah cara berpikirmu?'],
    ['reflect','Reflection','Creator Reflection','Apa yang kamu banggakan dan apa satu peningkatan bila punya waktu lagi?'],
    ['celebrate','Celebration','Mission Complete','Rayakan proses: proposal, build, test, explain, dan keberanian menunjukkan karya.']
  ];
  items.forEach(([sec,label,title,lead])=>s.push(workshopItem(m,sec,label,{title,lead,mode:sec==='audience'?'Online: gunakan chat hanya saat feedback; offline: gunakan kartu catatan.':''})));
  s.push(makeSlide(12,'m12-celebrate','Celebration','Quote of the Day','Terus bereksperimen',`<div class="quote"><div><blockquote>“There was no choice but to be pioneers.”</blockquote><cite>— Margaret Hamilton</cite></div></div>`));
  if(s.length!==25) throw new Error(`Meeting 12 slide count ${s.length}, expected 25`); return s;
}

const deckData = {};
for(let meeting=1; meeting<=8; meeting++) deckData[meeting]=buildConceptMeeting(conceptMeetings[meeting]);
deckData[9]=buildMeeting9(); deckData[10]=buildMeeting10(); deckData[11]=buildMeeting11(); deckData[12]=buildMeeting12();
window.deckData = deckData;

const dom = {
  meetingNav:document.getElementById('meetingNav'), sectionSelector:document.getElementById('sectionSelector'),
  meetingPill:document.getElementById('meetingPill'), sectionPill:document.getElementById('sectionPill'), objectivePill:document.getElementById('objectivePill'),
  title:document.getElementById('slideTitle'), subtitle:document.getElementById('slideSubtitle'), content:document.getElementById('slideContent'),
  card:document.getElementById('slideCard'), prev:document.getElementById('prevBtn'), next:document.getElementById('nextBtn'),
  counter:document.getElementById('slideCounter'), bar:document.getElementById('progressBar'), progress:document.querySelector('.progress-track'),
  menu:document.getElementById('menuBtn'), sidebar:document.getElementById('sidebar'), overlay:document.getElementById('sidebarOverlay')
};
let currentMeeting=1, currentIndex=0;

function renderMeetingNav(){
  dom.meetingNav.innerHTML='';
  for(let m=1;m<=12;m++){
    const button=document.createElement('button'); button.type='button'; button.className='meeting-tab';
    button.dataset.meeting=String(m); button.setAttribute('aria-current',m===currentMeeting?'true':'false');
    button.innerHTML=`<span class="meeting-num">${m}</span><span class="meeting-copy"><strong>Meeting ${m}</strong><small>${topics[m]}</small></span>`;
    button.addEventListener('click',()=>{currentMeeting=m;currentIndex=0;buildSectionSelector();renderMeetingNav();renderSlide();closeSidebar();});
    dom.meetingNav.appendChild(button);
  }
}

function buildSectionSelector(){
  dom.sectionSelector.innerHTML=''; const seen=new Set();
  deckData[currentMeeting].forEach((slide,index)=>{
    if(seen.has(slide.sectionId)) return; seen.add(slide.sectionId);
    const option=document.createElement('option'); option.value=slide.sectionId; option.dataset.index=String(index); option.textContent=slide.sectionLabel;
    dom.sectionSelector.appendChild(option);
  });
}

function updateHash(){ history.replaceState(null,'',`#meeting=${currentMeeting}&slide=${currentIndex+1}`); }
function renderSlide(){
  const slides=deckData[currentMeeting], slide=slides[currentIndex];
  dom.meetingPill.textContent=`Meeting ${currentMeeting}`; dom.sectionPill.textContent=slide.sectionLabel;
  dom.objectivePill.hidden=!slide.objectiveId; dom.objectivePill.textContent=slide.objectiveId||'';
  dom.title.textContent=slide.title; dom.subtitle.textContent=slide.subtitle; dom.content.innerHTML=slide.content;
  dom.counter.textContent=`Slide ${currentIndex+1} / ${slides.length}`;
  const percent=((currentIndex+1)/slides.length)*100; dom.bar.style.width=`${percent}%`;
  dom.progress.setAttribute('aria-valuemax',String(slides.length)); dom.progress.setAttribute('aria-valuenow',String(currentIndex+1));
  dom.prev.disabled=currentIndex===0; dom.next.disabled=currentIndex===slides.length-1;
  dom.sectionSelector.value=slide.sectionId; dom.card.scrollTop=0; initSlideInteractions(); updateHash();
  
  // Trigger slide-in animation
  const stage = document.querySelector('.slide-stage');
  stage.classList.remove('animate-in');
  void stage.offsetWidth; // trigger reflow
  stage.classList.add('animate-in');
}


function go(delta){ const target=currentIndex+delta; if(target>=0&&target<deckData[currentMeeting].length){currentIndex=target;renderSlide();} }
function initSlideInteractions(){
  dom.content.querySelectorAll('.choice').forEach(button=>button.addEventListener('click',()=>{
    const group=button.closest('.choices'); group.querySelectorAll('.choice').forEach(x=>x.classList.remove('correct','wrong'));
    const correct=button.dataset.correct==='true'; button.classList.add(correct?'correct':'wrong');
    const feedback=group.nextElementSibling; feedback.textContent=correct?`✅ Tepat. ${button.dataset.explain}`:'Belum tepat. Baca prompt lagi lalu coba pilihan lain.';
  }));
  dom.content.querySelectorAll('[data-copy-target]').forEach(button=>button.addEventListener('click',async()=>{
    const target=document.getElementById(button.dataset.copyTarget); const feedback=button.nextElementSibling;
    try{await navigator.clipboard.writeText(target.textContent);feedback.textContent='Tersalin ✓';}
    catch(_){feedback.textContent='Clipboard diblokir. Pilih teks pada kotak lalu salin manual.';}
  }));
}
function openSidebar(){dom.sidebar.classList.add('open');dom.overlay.classList.add('open');dom.menu.setAttribute('aria-expanded','true');}
function closeSidebar(){dom.sidebar.classList.remove('open');dom.overlay.classList.remove('open');dom.menu.setAttribute('aria-expanded','false');}

dom.prev.addEventListener('click',()=>go(-1)); dom.next.addEventListener('click',()=>go(1));
dom.sectionSelector.addEventListener('change',()=>{const option=dom.sectionSelector.selectedOptions[0];currentIndex=Number(option.dataset.index);renderSlide();});
dom.menu.addEventListener('click',()=>dom.sidebar.classList.contains('open')?closeSidebar():openSidebar()); dom.overlay.addEventListener('click',closeSidebar);
document.addEventListener('keydown',event=>{
  const tag=document.activeElement?.tagName?.toLowerCase(); if(['input','textarea','select','button','summary'].includes(tag)) return;
  if(event.key==='ArrowRight'){event.preventDefault();go(1);} if(event.key==='ArrowLeft'){event.preventDefault();go(-1);}
});
let touchX=null;
dom.card.addEventListener('touchstart',event=>{if(event.target.closest('button,select,summary,details'))return;touchX=event.changedTouches[0].clientX;},{passive:true});
dom.card.addEventListener('touchend',event=>{if(touchX===null)return;const dx=event.changedTouches[0].clientX-touchX;touchX=null;if(Math.abs(dx)>55)go(dx<0?1:-1);},{passive:true});

const match=location.hash.match(/meeting=(\d+)&slide=(\d+)/);
if(match){const m=Number(match[1]),i=Number(match[2])-1;if(deckData[m]&&i>=0&&i<deckData[m].length){currentMeeting=m;currentIndex=i;}}
renderMeetingNav(); buildSectionSelector(); renderSlide();
