import re

def main():
    # 1. Extract Level 4 Slides
    with open("level4/deck.html", "r", encoding="utf-8") as f:
        l4_html = f.read()

    slides_match = re.search(r'(<div id="slide-data" class="hidden">.*?</div>)\s*<script>', l4_html, re.DOTALL)
    if not slides_match:
        print("ERROR: Could not extract slides from level4/deck.html")
        return
    l4_slides = slides_match.group(1)

    # 2. Extract Level 3 Shell HTML (everything before script)
    with open("level3/deck.html", "r", encoding="utf-8") as f:
        l3_html = f.read()

    shell_match = re.search(r'(<!DOCTYPE html>.*?)<!-- Data & Script -->', l3_html, re.DOTALL)
    if not shell_match:
        print("ERROR: Could not extract shell from level3/deck.html")
        return
    l3_shell = shell_match.group(1)

    # 3. Modify Level 3 Shell for Level 4
    # Change Title
    l3_shell = l3_shell.replace("Python Level 3 - Mission Control", "Python Level 4 - Planet Visionara")
    l3_shell = l3_shell.replace("Python Level 3", "Python Level 4")
    l3_shell = l3_shell.replace("Python L3", "Python L4")
    l3_shell = l3_shell.replace("Mission Control", "Planet Visionara")
    l3_shell = l3_shell.replace("MISSION CONTROL", "PLANET VISIONARA")

    # Inject Objective Dropdown into topnav
    # We replace the `<div class="w-24"></div>` at the end of topnav with the dropdown.
    dropdown_html = '''
            <div class="flex-1 max-w-xl mx-4 hidden md:block">
                <select id="section-selector" class="w-full px-4 py-2 bg-[var(--bg2)] text-[var(--text)] border border-[var(--card-b)] rounded-xl focus:outline-none focus:ring-2 focus:ring-k-blue font-bold"></select>
            </div>
            <div class="w-8"></div>
    '''
    l3_shell = l3_shell.replace('<div class="w-24"></div>', dropdown_html)

    # 4. Construct the New JS Engine
    js_engine = """
<!-- Data & Script -->
    <script>
        // --- Core Application State ---
        let currentMeeting = 1;
        let currentSlideIndex = 0;
        let slides = [];
        const totalMeetings = 12;

        // --- DOM Elements ---
        const welcomeMessage = document.getElementById('welcomeMessage');
        const meetingSelectionSection = document.getElementById('meetingSelectionSection');
        const welcomeOverlay = document.getElementById('welcomeOverlay');
        const displayTeacherName = document.getElementById('displayTeacherName');
        const teacherInputSection = document.getElementById('teacherInputSection');
        const welcomeBackSection = document.getElementById('welcomeBackSection');
        const mainContent = document.getElementById('mainContent');
        
        const slideDataContainer = document.getElementById('slide-data');
        const slideContent = document.getElementById('slideContent');
        const slideTitle = document.getElementById('slideTitle');
        const slideSubtitle = document.getElementById('slideSubtitle');
        const meetingTag = document.getElementById('meetingTag');
        const sectionSelector = document.getElementById('section-selector');
        const btnPrev = document.getElementById('prevBtn');
        const btnNext = document.getElementById('nextBtn');
        const slideCounter = document.getElementById('slideCounter');
        const progressBar = document.getElementById('progressBar');
        const meetingNav = document.getElementById('meetingNav');
        
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebarOverlay');
        const hamburgerBtn = document.getElementById('hamburgerBtn');
        const closeSidebarBtn = document.getElementById('closeSidebarBtn');

        // --- Welcome Logic (from Level 3) ---
        function checkTeacherName() {
            let teacher = localStorage.getItem("teacherName");
            if (teacher) {
                if(teacherInputSection) teacherInputSection.classList.add('hidden');
                if(welcomeBackSection) welcomeBackSection.classList.remove('hidden');
                if(displayTeacherName) displayTeacherName.innerText = teacher;
            } else {
                if(teacherInputSection) teacherInputSection.classList.remove('hidden');
                if(welcomeBackSection) welcomeBackSection.classList.add('hidden');
            }
        }

        window.startClass = function() {
            const name = document.getElementById('teacherName') ? document.getElementById('teacherName').value : '';
            const hobby = document.getElementById('teacherHobby') ? document.getElementById('teacherHobby').value : '';
            const food = document.getElementById('teacherFood') ? document.getElementById('teacherFood').value : '';
            
            if (name.trim()) {
                localStorage.setItem("teacherName", name);
                localStorage.setItem("teacherHobby", hobby || "Ngoding 💻");
                localStorage.setItem("teacherFood", food || "Nasi Goreng 🍛");
                showMeetingSelection();
            } else {
                alert("Mohon masukkan nama kakak pengajar dulu ya! 😊");
            }
        }

        window.enterClass = function() { showMeetingSelection(); }

        window.resetTeacher = function() {
            localStorage.removeItem("teacherName");
            localStorage.removeItem("teacherHobby");
            localStorage.removeItem("teacherFood");
            if(document.getElementById('teacherName')) document.getElementById('teacherName').value = "";
            if(document.getElementById('teacherHobby')) document.getElementById('teacherHobby').value = "";
            if(document.getElementById('teacherFood')) document.getElementById('teacherFood').value = "";
            checkTeacherName();
        }

        function showMeetingSelection() {
            if(teacherInputSection) teacherInputSection.classList.add('hidden');
            if(welcomeBackSection) welcomeBackSection.classList.add('hidden');
            if(welcomeMessage) welcomeMessage.classList.add('hidden');
            if(meetingSelectionSection) meetingSelectionSection.classList.remove('hidden');
            
            const grid = document.getElementById('meetingGrid');
            if(grid) {
                grid.innerHTML = '';
                for (let i = 1; i <= 12; i++) {
                    const btn = document.createElement('button');
                    
                    // Count slides for this meeting to see if it's locked
                    const meetingSlides = slideDataContainer.querySelectorAll(`.raw-slide[data-meeting="${i}"]`);
                    const isLocked = meetingSlides.length === 0;
                    
                    let topic = "Belum tersedia";
                    if (!isLocked) {
                        topic = "Visionara " + i; // A placeholder, we can refine this later
                    }

                    btn.className = `p-6 rounded-3xl transition-all duration-300 flex flex-col items-center justify-center gap-3 border ${!isLocked ? 'planet-card border-[var(--card-b)] hover:-translate-y-2 hover:shadow-2xl cursor-pointer hover:border-k-yellow' : 'bg-[var(--bg2)] border-[var(--card-b)] opacity-50 cursor-not-allowed'}`;
                    btn.innerHTML = `
                        <span class="text-3xl font-display font-black ${!isLocked ? 'text-[var(--text)]' : 'text-muted'}">MISI ${i}</span>
                        <span class="text-[10px] text-center font-bold uppercase tracking-widest ${!isLocked ? 'text-k-blue' : 'text-muted/60'} mt-1">${topic}</span>
                    `;
                    if (!isLocked) btn.onclick = () => selectMeeting(i);
                    grid.appendChild(btn);
                }
            }
        }

        function selectMeeting(id) {
            currentMeeting = id;
            currentSlideIndex = 0;
            if(welcomeOverlay) welcomeOverlay.style.opacity = '0';
            setTimeout(() => {
                if(welcomeOverlay) welcomeOverlay.style.display = 'none';
                if(mainContent) {
                    mainContent.classList.remove('hidden');
                    setTimeout(() => {
                        mainContent.classList.remove('opacity-0');
                        renderSidebar();
                        loadMeeting(id);
                    }, 50);
                }
            }, 1000);
        }

        // --- Sidebar ---
        function renderSidebar() {
            if (!meetingNav) return;
            meetingNav.innerHTML = '';
            for (let i = 1; i <= 12; i++) {
                const meetingSlides = slideDataContainer.querySelectorAll(`.raw-slide[data-meeting="${i}"]`);
                const isLocked = meetingSlides.length === 0;

                const btn = document.createElement('button');
                btn.className = `w-full text-left p-4 rounded-2xl meeting-tab flex items-center justify-between ${currentMeeting == i ? 'active font-bold text-k-blue' : 'text-muted'} ${isLocked ? 'opacity-50 cursor-not-allowed' : ''}`;
                
                let iconHtml = currentMeeting == i 
                    ? '<span class="w-2 h-2 rounded-full bg-k-yellow shadow-[0_0_8px_rgba(249,192,19,0.8)]"></span>' 
                    : (isLocked ? '<span class="text-[10px]">🔒</span>' : '<span class="w-1.5 h-1.5 rounded-full bg-muted/30"></span>');

                btn.innerHTML = `
                    <span class="text-sm font-black uppercase tracking-widest">Misi ${i}</span>
                    ${iconHtml}
                `;
                if (!isLocked) {
                    btn.onclick = () => {
                        closeSidebar();
                        loadMeeting(i);
                        renderSidebar();
                    };
                }
                meetingNav.appendChild(btn);
            }
        }

        function toggleSidebar() {
            const isClosed = sidebar.classList.contains('-translate-x-full');
            if (isClosed) {
                sidebar.classList.remove('-translate-x-full');
                sidebarOverlay.classList.remove('hidden');
            } else {
                closeSidebar();
            }
        }
        function closeSidebar() {
            sidebar.classList.add('-translate-x-full');
            sidebarOverlay.classList.add('hidden');
        }
        if (hamburgerBtn) hamburgerBtn.addEventListener('click', toggleSidebar);
        if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', closeSidebar);
        if (sidebarOverlay) sidebarOverlay.addEventListener('click', closeSidebar);

        // --- Slide Engine (Level 4 adaptation to Level 3 shell) ---
        function loadMeeting(meetingId) {
            currentMeeting = meetingId;
            slides = Array.from(slideDataContainer.querySelectorAll(`.raw-slide[data-meeting="${meetingId}"]`));
            
            buildSectionDropdown();
            goToSlide(0);
        }

        function buildSectionDropdown() {
            if (!sectionSelector) return;
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
            
            currentSlideIndex = index;
            const newSlide = slides[currentSlideIndex];
            
            // Extract title and subtitle if present in the slide HTML
            // In level 4, we used <h2> for title and <p> for subtitle inside the raw-slide.
            const h2 = newSlide.querySelector('h2');
            const p = newSlide.querySelector('p');
            
            if (h2) {
                slideTitle.innerHTML = h2.innerHTML;
                h2.style.display = 'none'; // hide it from content
            } else {
                slideTitle.innerHTML = newSlide.dataset.sectionLabel || "Mission Control";
            }
            
            if (p) {
                slideSubtitle.innerHTML = p.innerHTML;
                p.style.display = 'none'; // hide it from content
            } else {
                slideSubtitle.innerHTML = "";
            }

            meetingTag.textContent = `Meeting ${currentMeeting}`;

            // Inject the rest of the content
            slideContent.innerHTML = '';
            // We append a clone to avoid permanently stripping the h2/p from the original raw-slide.
            // Wait, we need the original slide for interactive elements to retain state?
            // Actually cloning is safer because the original remains untouched in slideDataContainer.
            const slideClone = newSlide.cloneNode(true);
            const cloneH2 = slideClone.querySelector('h2');
            const cloneP = slideClone.querySelector('p');
            if (cloneH2) cloneH2.remove();
            if (cloneP) cloneP.remove();
            
            slideContent.appendChild(slideClone);
            
            // Re-apply classes needed for Level 3 theme
            slideClone.style.display = 'block';

            // Navigation State
            slideCounter.textContent = `Slide ${currentSlideIndex + 1} / ${slides.length}`;
            if (progressBar) progressBar.style.width = `${((currentSlideIndex + 1) / slides.length) * 100}%`;
            btnPrev.disabled = currentSlideIndex === 0;
            btnNext.disabled = currentSlideIndex === slides.length - 1;

            const activeSecId = newSlide.dataset.sectionId;
            if (activeSecId && sectionSelector && sectionSelector.value !== activeSecId) {
                sectionSelector.value = activeSecId;
            }
            
            initInteractions(slideClone);
            
            // Animate transition
            const slideContainer = document.getElementById('slideContainer');
            slideContainer.classList.remove('slide-transition');
            slideContainer.style.opacity = '0';
            slideContainer.style.transform = 'translateY(10px)';
            
            setTimeout(() => {
                slideContainer.classList.add('slide-transition');
                slideContainer.style.opacity = '1';
                slideContainer.style.transform = 'translateY(0)';
            }, 50);
        }

        function initInteractions(slideElement) {
            // Level 4 specific interactions (Reveals, Quizzes)
            const reveals = slideElement.querySelectorAll('.k-reveal');
            reveals.forEach(reveal => {
                const btn = reveal.querySelector('.k-reveal-btn');
                if(btn) {
                    btn.addEventListener('click', () => {
                        reveal.classList.toggle('is-open');
                        btn.setAttribute('aria-expanded', reveal.classList.contains('is-open'));
                    });
                }
            });

            const quizOptions = slideElement.querySelectorAll('.k-quiz-option');
            quizOptions.forEach(opt => {
                opt.addEventListener('click', (e) => {
                    const isCorrect = opt.dataset.correct === "true";
                    const parent = opt.parentElement;
                    parent.querySelectorAll('.k-quiz-option').forEach(o => {
                        o.classList.remove('correct', 'wrong', 'bg-green-500', 'bg-red-500');
                    });
                    opt.classList.add(isCorrect ? 'correct' : 'wrong');
                    
                    if (isCorrect) {
                        opt.style.backgroundColor = 'rgba(34, 197, 94, 0.4)';
                        opt.style.borderColor = '#22c55e';
                    } else {
                        opt.style.backgroundColor = 'rgba(239, 68, 68, 0.4)';
                        opt.style.borderColor = '#ef4444';
                    }
                    
                    const feedback = parent.querySelector('.k-quiz-feedback');
                    if (feedback) {
                        feedback.style.display = 'block';
                        feedback.innerHTML = isCorrect ? '✅ Tepat sekali!' : '❌ Coba lagi!';
                        feedback.className = `k-quiz-feedback ${isCorrect ? 'bg-green-900/50 text-green-200' : 'bg-red-900/50 text-red-200'} font-bold p-3 mt-2 rounded`;
                    }
                });
            });
        }

        // --- Event Listeners ---
        if(btnPrev) btnPrev.addEventListener('click', () => goToSlide(currentSlideIndex - 1));
        if(btnNext) btnNext.addEventListener('click', () => goToSlide(currentSlideIndex + 1));
        if(sectionSelector) {
            sectionSelector.addEventListener('change', (e) => {
                const selectedOption = e.target.options[e.target.selectedIndex];
                const targetIndex = parseInt(selectedOption.dataset.index, 10);
                if (!isNaN(targetIndex)) goToSlide(targetIndex);
            });
        }

        document.addEventListener('keydown', (e) => {
            if (welcomeOverlay && welcomeOverlay.style.display !== 'none') return; // Don't slide if in welcome
            if (e.key === 'ArrowRight') goToSlide(currentSlideIndex + 1);
            if (e.key === 'ArrowLeft') goToSlide(currentSlideIndex - 1);
        });

        // Add extra CSS styles for level 4 features inside the level 3 shell
        const extraStyles = document.createElement('style');
        extraStyles.innerHTML = `
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
            color: var(--text);
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
            border: 1px solid var(--card-b);
            border-radius: 0.5rem;
            color: var(--text);
            cursor: pointer;
            text-align: left;
            transition: all 0.2s;
        }
        .k-quiz-option:hover { background: rgba(255,255,255,0.1); }
        `;
        document.head.appendChild(extraStyles);

        // Initialization
        window.addEventListener('load', () => {
            const loader = document.getElementById('mission-loader');
            if (loader) {
                setTimeout(() => {
                    loader.classList.add('loaded');
                    checkTeacherName();
                }, 2000);
            } else {
                checkTeacherName();
            }
        });
    </script>
</body>
</html>
"""

    # 5. Assemble final HTML
    final_html = l3_shell + "\\n" + l4_slides + "\\n" + js_engine

    # 6. Write out the final HTML back to level4/deck.html
    with open("level4/deck.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print("Level 4 UI Port complete!")

if __name__ == "__main__":
    main()
