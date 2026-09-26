import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

new_style = """    <style>
        :root, html[data-theme="light"] {
            --bg: #f0f8ff;
            --bg2: #e0f2fe;
            --sky: #bae6fd;
            --card: #ffffff;
            --card-b: #bae6fd;
            --nav: rgba(255,255,255,0.95);
            --nav-b: #bae6fd;
            --text: #1e293b;
            --muted: #475569;
            --slide-accent: #0284c7;
            --k-blue: #0ea5e9;
            --k-blue-d: #0369a1;
            --k-yellow: #f59e0b;
            --k-yellow-d: #d97706;
            --k-green: #10b981;
            --chip-b: #bfdbfe;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background: linear-gradient(160deg, #f0f8ff 0%, #e0f2fe 50%, #bae6fd 100%);
            background-attachment: fixed;
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }

        body::before {
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: -20;
            opacity: 0.04;
            background-image: radial-gradient(circle at center, #0369a1 0 1px, transparent 1.6px);
            background-size: 30px 30px;
        }

        .topnav {
            background: var(--nav);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--nav-b);
        }
        
        .planet-card { 
            background: var(--card); 
            border: 1px solid var(--card-b); 
            box-shadow: 0 15px 35px -10px rgba(2, 132, 199, 0.12);
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(14,165,233,0.3); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(14,165,233,0.5); }

        .btn-3d { 
            position: relative; transition: all 0.2s;
            box-shadow: 0 6px 0 #0284c7, 0 15px 30px -5px rgba(14, 165, 233, 0.3); border: none; cursor: pointer;
        }
        .btn-3d:hover { transform: translateY(-2px); box-shadow: 0 8px 0 #0284c7, 0 20px 40px -10px rgba(14, 165, 233, 0.4); }
        .btn-3d:active { transform: translateY(4px); box-shadow: 0 2px 0 #0284c7, 0 5px 10px -2px rgba(14, 165, 233, 0.2); }

        .section-jump {
            display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; gap: .75rem;
            padding: .45rem .55rem .45rem .9rem; border: 1px solid var(--card-b); border-radius: 1rem;
            background: #ffffff;
        }
        .section-jump label { font-size: .65rem; line-height: 1; font-weight: 900; letter-spacing: .16em; text-transform: uppercase; color: var(--muted); white-space: nowrap; }
        #sectionSelector { width: 100%; min-width: 0; border: 1px solid #e2e8f0; border-radius: .7rem; padding: .65rem .8rem; background: #f8fafc; color: var(--text); font-weight: 800; outline: none; }
        #sectionSelector:focus-visible { outline: 3px solid #bae6fd; outline-offset: 1px; border-color: var(--k-blue); }

        #slideCard {
            background: #ffffff;
            border: 1px solid #bae6fd;
            border-radius: 2rem;
            box-shadow: 0 35px 60px -15px rgba(2, 132, 199, 0.15), 0 0 0 1px rgba(255,255,255,0.8) inset;
            position: relative;
            overflow: hidden;
        }
        #slideCard::before {
            content: ""; position: absolute; inset: 0 0 auto; height: .45rem; z-index: 3;
            background: linear-gradient(90deg, var(--k-blue), var(--k-green), var(--k-yellow));
        }

        .slide-stage { position: relative; z-index: 1; width: 100%; margin-block: auto; padding-block: 1rem; max-width: 1000px; margin: 0 auto; }
        
        .meta { display: flex; align-items: center; justify-content: center; gap: .75rem; flex-wrap: wrap; margin-bottom: 1.25rem; }
        
        .pill {
            display: inline-flex; align-items: center; padding: .5rem 1rem; border-radius: 999px;
            background: #eff6ff; color: var(--k-blue-d); font-size: .65rem; font-weight: 900;
            letter-spacing: .15em; text-transform: uppercase; border: 1.5px solid #dbeafe;
            box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        #meetingPill { background: var(--k-yellow); color: #ffffff; border-color: var(--k-yellow-d); box-shadow: 0 4px 10px -2px rgba(245, 158, 11, 0.4); }

        .meeting-tab { width:100%; display:grid; grid-template-columns:40px 1fr; gap:11px; align-items:center; padding:10px; color:var(--text); text-align:left; border:1px solid transparent; border-radius:15px; background:transparent; cursor:pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
        .meeting-tab:hover { background: #f0f9ff; border-color: var(--card-b); transform: translateX(4px); }
        .meeting-tab[aria-current="true"] { background: #e0f2fe; border-left: 3px solid var(--k-blue); border-radius: 0 15px 15px 0; }
        .meeting-num { width:40px; height:40px; display:grid; place-items:center; border-radius:12px; color:#fff; background:var(--k-blue-d); font-weight:950; }
        .meeting-tab:not([aria-current="true"]) .meeting-num { color:var(--k-blue-d); background:#e0f2fe; }
        .meeting-copy strong { display:block; font-size:.83rem; font-family: 'Space Grotesk', sans-serif; font-weight: bold; }
        .meeting-copy small { margin-top:3px; color:var(--muted); font-size:.69rem; line-height:1.25; }

        .panel { 
            position: relative; border: 1.5px solid #e2e8f0; border-radius: 1.5rem; 
            padding: 1.75rem; background: #ffffff; 
            box-shadow: 0 10px 25px -10px rgba(0, 0, 0, 0.05);
        }
        .panel h3, .panel h4 { font-size: 1.15rem; font-weight: 900; color: var(--k-blue-d); margin-bottom: .75rem; }
        .panel.yellow h3 { color: var(--k-yellow-d); }
        .panel.green h3 { color: #059669; }
        .panel.red h3 { color: #e11d48; }
        .panel p, .panel li { color: var(--muted); font-size: 1rem; line-height: 1.6; }

        .hero { 
            position: relative; overflow: hidden; border: 1.5px solid #bae6fd; 
            border-radius: 1.75rem; padding: 2rem; 
            background: linear-gradient(135deg, #f0f9ff 0%, #ffffff 100%);
            display: grid; grid-template-columns: 1.4fr 0.6fr; gap: 24px; align-items: center; min-height: 240px;
            box-shadow: 0 10px 30px -10px rgba(2, 132, 199, 0.1);
        }
        .hero-mark { font-size: clamp(4rem, 10vw, 7rem); display: grid; place-items: center; filter: drop-shadow(0 10px 15px rgba(0,0,0,0.1)); }
        .eyebrow { color: var(--k-blue-d); font-size: .85rem; font-weight: 950; letter-spacing: .15em; text-transform: uppercase; }

        .flow { display: flex; align-items: stretch; gap: 1rem; flex-wrap: wrap; }
        .flow > div { flex: 1 1 180px; display: flex; flex-direction: column; justify-content: center; min-height: 8rem; border: 1.5px solid #e2e8f0; border-radius: 1.25rem; padding: 1.25rem; background: #ffffff; text-align: center; box-shadow: 0 4px 15px -5px rgba(0,0,0,0.03); }
        .flow strong { color: var(--k-blue-d); display: block; margin-bottom: 8px; font-weight: 900; font-size: 1.1rem; }

        .callout { display: flex; flex-direction: column; gap: .75rem; border-left: 5px solid var(--k-yellow-d); border-radius: .5rem 1rem 1rem .5rem; padding: 1.25rem 1.5rem; background: #fffbeb; color: #78350f; border-top: 1.5px solid #fde68a; border-right: 1.5px solid #fde68a; border-bottom: 1.5px solid #fde68a; box-shadow: 0 4px 6px -1px rgba(253, 230, 138, 0.3); }
        .callout strong { color: #92400e; }
        
        .mode-note { display: flex; gap: 12px; align-items: flex-start; padding: 16px 20px; border: 2px dashed #bae6fd; border-radius: 16px; color: #0369a1; background: #f0f9ff; margin-top: 1.5rem; font-weight: 600; font-size: 0.95rem; line-height: 1.5; }

        details.reveal { margin-top: 1.5rem; border: 1.5px solid #e2e8f0; border-radius: 1rem; overflow: hidden; background: #ffffff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.03); }
        details.reveal summary { width: 100%; padding: 1.25rem; background: #f8fafc; color: var(--k-blue-d); border: none; text-align: left; font-weight: bold; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none; font-size: 1.05rem; }
        details.reveal summary::-webkit-details-marker { display: none; }
        details.reveal summary::after { content: "＋"; float: right; color: var(--text); }
        details.reveal[open] summary::after { content: "−"; }
        .reveal-body { padding: 1.5rem; border-top: 1.5px solid #e2e8f0; }

        .choices { display: grid; gap: 12px; margin-top: 20px; }
        .choice { display: block; width: 100%; padding: 1.25rem; margin-bottom: 0.5rem; background: #ffffff; border: 2px solid #e2e8f0; border-radius: 1rem; color: var(--text); cursor: pointer; text-align: left; transition: all 0.2s; font-weight: bold; font-size: 1.05rem; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .choice:hover { background: #f0f9ff; border-color: var(--k-blue); transform: translateY(-1px); box-shadow: 0 4px 10px rgba(14, 165, 233, 0.15); }
        .choice.correct { border-color: #10b981; background: #ecfdf5; color: #047857; }
        .choice.wrong { border-color: #ef4444; background: #fef2f2; color: #b91c1c; }
        .feedback { min-height: 1.6em; margin-top: 12px; color: var(--muted); font-weight: 800; display: none; }
        
        pre.code { position: relative; overflow: auto; margin: 20px 0; padding: 24px; border: 1px solid #cbd5e1; border-radius: 1.25rem; color: #1e293b; background: #f8fafc; font: 500 1.05rem/1.6 "SFMono-Regular",Consolas,"Liberation Mono",monospace; white-space: pre-wrap; tab-size: 4; box-shadow: inset 0 2px 4px rgba(0,0,0,0.02); }
        code { padding:.15em .4em; border-radius:6px; color:#c2410c; background:#ffedd5; font-family:"SFMono-Regular",Consolas,"Liberation Mono",monospace; font-weight: 600; }
        .output { padding: 16px 20px; border-left: 5px solid var(--k-green); border-radius: 12px; color: #065f46; background: #d1fae5; font-family: "SFMono-Regular",Consolas,monospace; white-space: pre-wrap; margin-top: 0.75rem; font-weight: 600; }

        .grid-2, .grid-3 { display: grid; gap: 20px; }
        .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        
        .quote { min-height: 300px; display: grid; place-items: center; text-align: center; }
        .quote blockquote { max-width: 800px; margin: 0; color: #0f172a; font-size: clamp(1.8rem, 4.5vw, 3.2rem); font-weight: 900; line-height: 1.3; }
        .quote cite { display: block; margin-top: 24px; color: var(--k-blue-d); font-size: 1.1rem; font-style: normal; font-weight: bold; }

        ul, ol { padding-left: 1.4em; list-style-position: inside; }
        ul { list-style-type: disc; }
        ol { list-style-type: decimal; }
        li { margin: .5em 0; }
        
        #slideTitle { margin-bottom: 12px; font-size: clamp(2rem, 5vw, 3.8rem); line-height: 1.1; letter-spacing: -.03em; font-family: 'Orbitron', sans-serif; font-weight: 900; color: #0f172a; }
        #slideSubtitle { margin: 0; color: #475569; font-size: clamp(1.1rem, 2.2vw, 1.35rem); line-height: 1.5; font-weight: bold; }
        #slideContent { font-size: clamp(1.05rem, 1.8vw, 1.2rem); line-height: 1.7; font-weight: 500; color: #1e293b; }
        #slideContent p { margin-bottom: 1.2rem; }

        @media (max-width: 900px) {
            .hero { grid-template-columns: 1fr; }
            .grid-2, .grid-3 { grid-template-columns: 1fr; }
            .flow { flex-direction: column; }
        }
    </style>"""

html = re.sub(r'    <style>.*?</style>', new_style, html, flags=re.DOTALL)

# Remove the inline style from meetingPill
html = re.sub(r'<span class="pill font-bold" id="meetingPill" style="[^"]*">', r'<span class="pill font-bold" id="meetingPill">', html)

with open('level1/main_deck.html', 'w') as f:
    f.write(html)
