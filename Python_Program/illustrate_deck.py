import re

with open('level1/main_deck.js', 'r') as f:
    js = f.read()

# Helper function to wrap in split-layout
def wrap_split(content, icon, reverse=False):
    rev_class = ' reverse' if reverse else ''
    return f'`<div class="split-layout{rev_class}"><div class="illustration-side anim-float">{icon}</div><div class="content-side">{content}</div></div>`'

# 1. reviewSlide
js = js.replace(
    '`<div class="panel yellow"><p class="eyebrow">Coba dulu · jangan langsung buka jawaban</p><h3>${item.prompt}</h3>${item.snippet ? code(item.snippet) : \'\'}${interaction}</div>${modeNote(item.offline || \'Tulis prediksi di kertas atau tunjukkan kartu A/B/C sebelum membuka jawaban.\')}`',
    '`<div class="split-layout"><div class="illustration-side anim-bounce">🤔</div><div class="content-side"><div class="panel yellow"><p class="eyebrow">Coba dulu · jangan langsung buka jawaban</p><h3>${item.prompt}</h3>${item.snippet ? code(item.snippet) : \'\'}${interaction}</div>${modeNote(item.offline || \'Tulis prediksi di kertas atau tunjukkan kartu A/B/C sebelum membuka jawaban.\')}</div></div>`'
)

# 2. detailedObjectiveSlides & compactObjectiveSlides
# - Definisi Teknis
js = js.replace(
    '`<div class="panel"><h3>${obj.term}</h3><p>${obj.formal}</p></div><div class="callout"><strong>Yang perlu diucapkan dengan tepat:</strong> ${obj.accuracy}</div>`',
    '`<div class="split-layout"><div class="content-side"><div class="panel"><h3>${obj.term}</h3><p>${obj.formal}</p></div><div class="callout"><strong>Yang perlu diucapkan dengan tepat:</strong> ${obj.accuracy}</div></div><div class="illustration-side anim-float">📖</div></div>`'
)
js = js.replace(
    '`<div class="panel"><p>${obj.formal}</p><p><strong>Ketepatan:</strong> ${obj.accuracy}</p></div><div class="flow">${obj.model.map((step,i)=>`<div><strong>${i+1}. ${step.title}</strong>${step.body}</div>`).join(\'\')}</div>`',
    '`<div class="split-layout"><div class="content-side"><div class="panel"><p>${obj.formal}</p><p><strong>Ketepatan:</strong> ${obj.accuracy}</p></div><div class="flow">${obj.model.map((step,i)=>`<div><strong>${i+1}. ${step.title}</strong>${step.body}</div>`).join(\'\')}</div></div><div class="illustration-side anim-float">⚙️</div></div>`'
)

# - Contoh Minimal + Hasil
js = js.replace(
    '    `${code(obj.example.code)}<p><strong>Output yang diharapkan:</strong></p>${output(obj.example.output)}`',
    '    `<div class="split-layout"><div class="illustration-side anim-bounce">💻</div><div class="content-side">${code(obj.example.code)}<p><strong>Output yang diharapkan:</strong></p>${output(obj.example.output)}</div></div>`'
)
# - Contoh Minimal + Prediksi
js = js.replace(
    '    `${code(obj.example.code)}${reveal(\'Cek output dan prediksi\', `${output(obj.example.output)}<p>${obj.predict.answer}</p>`)}`',
    '    `<div class="split-layout"><div class="illustration-side anim-bounce">💻</div><div class="content-side">${code(obj.example.code)}${reveal(\'Cek output dan prediksi\', `${output(obj.example.output)}<p>${obj.predict.answer}</p>`)}</div></div>`'
)

# - Predict Before Running
js = js.replace(
    '`<div class="panel yellow"><h3>${obj.predict.prompt}</h3>${obj.predict.code ? code(obj.predict.code) : \'\'}${reveal(\'Cek prediksi\', `<p>${obj.predict.answer}</p>`)}</div>${modeNote(\'Online: tulis di chat. Offline: tunjukkan jawaban dengan kartu atau kertas lipat.\')}`',
    '`<div class="split-layout"><div class="content-side"><div class="panel yellow"><h3>${obj.predict.prompt}</h3>${obj.predict.code ? code(obj.predict.code) : \'\'}${reveal(\'Cek prediksi\', `<p>${obj.predict.answer}</p>`)}</div>${modeNote(\'Online: tulis di chat. Offline: tunjukkan jawaban dengan kartu atau kertas lipat.\')}</div><div class="illustration-side anim-float">🔮</div></div>`'
)

# - Latihan Terpandu (Misi)
js = js.replace(
    '`<div class="panel"><h3>Misi</h3><p>${exercise.prompt}</p>${exercise.starter ? code(exercise.starter) : \'\'}</div>${reveal(\'Buka solusi setelah didiskusikan\', `${exercise.solution ? code(exercise.solution) : \'\'}${exercise.output ? output(exercise.output) : \'\'}<p>${exercise.reason || \'\'}</p>`)}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🎯</div><div class="content-side"><div class="panel"><h3>Misi</h3><p>${exercise.prompt}</p>${exercise.starter ? code(exercise.starter) : \'\'}</div>${reveal(\'Buka solusi setelah didiskusikan\', `${exercise.solution ? code(exercise.solution) : \'\'}${exercise.output ? output(exercise.output) : \'\'}<p>${exercise.reason || \'\'}</p>`)}</div></div>`'
)
js = js.replace(
    '`<div class="panel"><p>${exercise.prompt}</p>${exercise.starter?code(exercise.starter):\'\'}</div>${reveal(\'Buka solusi setelah mencoba\',`${code(exercise.solution)}${exercise.output?output(exercise.output):\'\'}<p>${exercise.reason||\'\'}</p>`)}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🎯</div><div class="content-side"><div class="panel"><p>${exercise.prompt}</p>${exercise.starter?code(exercise.starter):\'\'}</div>${reveal(\'Buka solusi setelah mencoba\',`${code(exercise.solution)}${exercise.output?output(exercise.output):\'\'}<p>${exercise.reason||\'\'}</p>`)}</div></div>`'
)

# - Bug Hunt (red panel)
js = js.replace(
    '`<div class="panel red"><h3>Kode bermasalah</h3>${code(obj.bug.code)}<p><strong>Gejala:</strong> ${obj.bug.error}</p></div>${reveal(\'Diagnosis dan urutan perbaikan\', `<p><strong>Penyebab:</strong> ${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output ? output(obj.bug.output) : \'\'}`)}`',
    '`<div class="split-layout"><div class="content-side"><div class="panel red"><h3>Kode bermasalah</h3>${code(obj.bug.code)}<p><strong>Gejala:</strong> ${obj.bug.error}</p></div>${reveal(\'Diagnosis dan urutan perbaikan\', `<p><strong>Penyebab:</strong> ${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output ? output(obj.bug.output) : \'\'}`)}</div><div class="illustration-side anim-bounce" style="font-size: 10rem;">🐛</div></div>`'
)
js = js.replace(
    '`<div class="panel red">${code(obj.bug.code)}<p>${obj.bug.error}</p></div>${reveal(\'Diagnosis dan perbaikan\',`<p>${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output?output(obj.bug.output):\'\'}`)}`',
    '`<div class="split-layout"><div class="content-side"><div class="panel red">${code(obj.bug.code)}<p>${obj.bug.error}</p></div>${reveal(\'Diagnosis dan perbaikan\',`<p>${obj.bug.cause}</p>${code(obj.bug.fix)}${obj.bug.output?output(obj.bug.output):\'\'}`)}</div><div class="illustration-side anim-bounce" style="font-size: 10rem;">🐛</div></div>`'
)

# - Latihan Mandiri (yellow panel)
js = js.replace(
    '`<div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal(\'Hint bertahap\', list(obj.independent.hints,true))}${reveal(\'Cek jawaban setelah mencoba\', `${code(obj.independent.solution)}${obj.independent.output ? output(obj.independent.output) : \'\'}`)}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🧗‍♂️</div><div class="content-side"><div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal(\'Hint bertahap\', list(obj.independent.hints,true))}${reveal(\'Cek jawaban setelah mencoba\', `${code(obj.independent.solution)}${obj.independent.output ? output(obj.independent.output) : \'\'}`)}</div></div>`'
)
js = js.replace(
    '`<div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal(\'Hint\',list(obj.independent.hints,true))}${reveal(\'Cek jawaban setelah mencoba\',`${code(obj.independent.solution)}${obj.independent.output?output(obj.independent.output):\'\'}`)}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🧗‍♂️</div><div class="content-side"><div class="panel yellow"><h3>${obj.independent.title}</h3><p>${obj.independent.prompt}</p>${list(obj.independent.requirements)}</div>${reveal(\'Hint\',list(obj.independent.hints,true))}${reveal(\'Cek jawaban setelah mencoba\',`${code(obj.independent.solution)}${obj.independent.output?output(obj.independent.output):\'\'}`)}</div></div>`'
)

# - Skill Check
js = js.replace(
    '`<div class="panel green"><h3>Bukti penguasaan</h3>${list(obj.skillCheck)}</div><p class="lead">Jika satu bukti belum tercapai, kembali ke latihan yang paling dekat—error adalah petunjuk untuk langkah berikutnya.</p>`',
    '`<div class="split-layout"><div class="content-side"><div class="panel green"><h3>Bukti penguasaan</h3>${list(obj.skillCheck)}</div><p class="lead">Jika satu bukti belum tercapai, kembali ke latihan yang paling dekat—error adalah petunjuk untuk langkah berikutnya.</p></div><div class="illustration-side anim-float">🏆</div></div>`'
)

# 3. integratedSlides
# - Guided Mini Projects
js = js.replace(
    '`<div class="panel yellow"><h3>Problem dulu</h3><p>${project.problem}</p>${list(project.requirements)}</div>${reveal(\'Buka worked solution setelah mencoba\',`${code(project.solution)}${project.output?output(project.output):\'\'}<p>${project.connection}</p>`)}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🛠️</div><div class="content-side"><div class="panel yellow"><h3>Problem dulu</h3><p>${project.problem}</p>${list(project.requirements)}</div>${reveal(\'Buka worked solution setelah mencoba\',`${code(project.solution)}${project.output?output(project.output):\'\'}<p>${project.connection}</p>`)}</div></div>`'
)
# - Independent Mini Project Starter
js = js.replace(
    '`${code(ind.starter)}<div class="callout">Starter ini sengaja belum lengkap. Jangan menunggu contoh final—buat versimu.</div>`',
    '`<div class="split-layout"><div class="illustration-side anim-bounce">🚀</div><div class="content-side">${code(ind.starter)}<div class="callout">Starter ini sengaja belum lengkap. Jangan menunggu contoh final—buat versimu.</div></div></div>`'
)

# 4. closingSlides
# - Exit Ticket
js = js.replace(
    '`<div class="panel yellow"><h3>${config.exitTicket}</h3><p>Tulis satu contoh kode pendek atau jelaskan secara lisan.</p></div>${modeNote(\'Online: kirim private chat. Offline: tulis di sticky note atau selembar kertas.\')}`',
    '`<div class="split-layout"><div class="illustration-side anim-float">🎟️</div><div class="content-side"><div class="panel yellow"><h3>${config.exitTicket}</h3><p>Tulis satu contoh kode pendek atau jelaskan secara lisan.</p></div>${modeNote(\'Online: kirim private chat. Offline: tulis di sticky note atau selembar kertas.\')}</div></div>`'
)
# - Debugging Recap
js = js.replace(
    '`<div class="flow"><div><strong>1</strong>Baca error</div><div><strong>2</strong>Cari baris</div><div><strong>3</strong>Cek ejaan, tanda, tipe, indentasi, state</div><div><strong>4</strong>Ubah satu hal</div><div><strong>5</strong>Jalankan dan bandingkan</div></div><div class="callout">Fokus hari ini: ${config.debugRecap}</div>`',
    '`<div class="split-layout"><div class="content-side"><div class="flow"><div><strong>1</strong>Baca error</div><div><strong>2</strong>Cari baris</div><div><strong>3</strong>Cek ejaan, tanda, tipe, indentasi, state</div><div><strong>4</strong>Ubah satu hal</div><div><strong>5</strong>Jalankan dan bandingkan</div></div><div class="callout">Fokus hari ini: ${config.debugRecap}</div></div><div class="illustration-side anim-bounce">🔎</div></div>`'
)

with open('level1/main_deck.js', 'w') as f:
    f.write(js)
