import re

with open('deck.html', 'r') as f:
    l3 = f.read()

with open('../level2/deck.html', 'r') as f:
    l2 = f.read()

# 1. Extract Meeting Data from Level 3
match_data = re.search(r'const meetingContent = (\{.*?\n        \n    </script>)', l3, re.DOTALL)
if match_data:
    meeting_data = match_data.group(1).replace("\n    </script>", "")
else:
    match_data = re.search(r'const meetingContent = (\{.*?\n    \]\n\};?)', l3, re.DOTALL)
    if match_data:
        meeting_data = match_data.group(1)
    else:
        print("Data match failed!")
        exit(1)

# Ensure data terminates properly
if not meeting_data.endswith(';'):
    meeting_data += ';'

# 2. Extract specific styles from Level 3
style_match = re.search(r'<style>(.*?)</style>', l3, re.DOTALL)
l3_style = style_match.group(1) if style_match else ""

welcome_style = "\n".join(re.findall(r'(#welcomeOverlay.*?\}|\.fade-in.*?\}|\.delay-500ms.*?\}|\.bounce-slow.*?\})', l3_style, re.DOTALL))
mock_style = ""
mock_match = re.search(r'/\* --- VISUAL ELEVATION: Realistic Window Mocks --- \*/(.*?)(/\* --- ANIMATED ROADMAP --- \*/|</style>)', l3_style, re.DOTALL)
if mock_match:
    mock_style = "/* --- VISUAL ELEVATION: Realistic Window Mocks --- */\n" + mock_match.group(1)

# 3. Extract Welcome Overlay from Level 3
welcome_html = ""
welcome_match = re.search(r'<!-- Welcome Overlay -->(.*?)<!-- Main Content -->', l3, re.DOTALL)
if welcome_match:
    welcome_html = "<!-- Welcome Overlay -->\n" + welcome_match.group(1).strip()

# 4. Construct CSS
l2_head_match = re.search(r'(<head>.*?)<style>', l2, re.DOTALL)
l2_head = l2_head_match.group(1) if l2_head_match else ""

l2_style_match = re.search(r'<style>(.*?)</style>', l2, re.DOTALL)
l2_style = l2_style_match.group(1) if l2_style_match else ""

final_style = "<style>\n" + l2_style + "\n" + welcome_style + "\n" + mock_style + "\n</style>\n</head>"

# 5. Construct Body
l2_body_match = re.search(r'<body[^>]*>(.*?)<!-- Data & Script -->', l2, re.DOTALL)
l2_body = l2_body_match.group(1) if l2_body_match else ""

l2_body = l2_body.replace('🐍 Python Level 2', '🐍 Python Level 3')
l2_body = l2_body.replace('<div class="h-screen flex flex-col">', '<div id="mainContent" class="h-screen flex flex-col opacity-0 hidden transition-opacity duration-1000">', 1)

final_body = '<body class="h-full overflow-hidden bg-slate-950 text-slate-800">\n' + welcome_html + "\n" + l2_body

# 6. Construct Scripts
l2_script_match = re.search(r'<!-- Data & Script -->(.*?)$', l2, re.DOTALL)
l2_script = l2_script_match.group(1) if l2_script_match else ""

l2_script = re.sub(r'const meetingData = \{.*?\n        \};\n', lambda m: 'const meetingData = ' + meeting_data + '\n', l2_script, flags=re.DOTALL)
# fallback
if 'const meetingData =' not in l2_script:
    l2_script = re.sub(r'const meetingData = \{.*?\n        \};', lambda m: 'const meetingData = ' + meeting_data, l2_script, flags=re.DOTALL)

welcome_script = """
        // --- Welcome Logic from Level 3 ---
        const welcomeMessage = document.getElementById('welcomeMessage');
        const meetingSelectionSection = document.getElementById('meetingSelectionSection');
        const welcomeOverlay = document.getElementById('welcomeOverlay');
        const displayTeacherName = document.getElementById('displayTeacherName');
        const teacherInputSection = document.getElementById('teacherInputSection');
        const welcomeBackSection = document.getElementById('welcomeBackSection');

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
                    const isLocked = !meetingData[i] || (i > 1 && meetingData[i].length === 1 && meetingData[i][0].content.includes("Soon"));
                    btn.className = `p-4 rounded-xl border transition-all duration-300 flex flex-col items-center justify-center gap-2 ${!isLocked ? 'bg-slate-800 border-slate-700 hover:bg-slate-700 hover:border-cyan-400 hover:scale-105 cursor-pointer' : 'bg-slate-900/50 border-slate-800 opacity-50 cursor-not-allowed'}`;
                    btn.innerHTML = `
                        <span class="text-2xl font-bold ${!isLocked ? 'text-white' : 'text-gray-600'}">Meeting ${i}</span>
                        <span class="text-xs text-center ${!isLocked ? 'text-gray-400' : 'text-gray-700'}">${!isLocked ? 'Klik untuk mulai' : 'Belum tersedia'}</span>
                    `;
                    if (!isLocked) btn.onclick = () => selectMeeting(i);
                    grid.appendChild(btn);
                }
            }
        }

        function selectMeeting(id) {
            currentMeeting = id;
            currentSlide = 1;
            if(welcomeOverlay) welcomeOverlay.style.opacity = '0';
            setTimeout(() => {
                if(welcomeOverlay) welcomeOverlay.style.display = 'none';
                const mainContent = document.getElementById('mainContent');
                if(mainContent) {
                    mainContent.classList.remove('hidden');
                    setTimeout(() => {
                        mainContent.classList.remove('opacity-0');
                        renderSidebar();
                        renderSlide();
                    }, 50);
                }
            }, 1000);
        }
        
        checkTeacherName();
"""

l2_script = l2_script.replace('        // --- Data Structure ---', '        // --- Data Structure ---\n' + welcome_script)

final_html = "<!DOCTYPE html>\n<html lang=\"en\">\n" + l2_head + final_style + "\n" + final_body + "\n<!-- Data & Script -->" + l2_script + "\n</html>"

with open('deck.html.new', 'w') as f:
    f.write(final_html)

print("deck.html.new generated successfully!")
