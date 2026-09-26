import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

# Replace <html lang="id" data-theme="dark"> with <html lang="id" data-theme="light">
html = html.replace('<html lang="id" data-theme="dark">', '<html lang="id" data-theme="light">')

# Replace the style block
style_block = """    <style>
        /* CSS Variables mimicking Level 4 Light Theme but with Level 1 colors */
        :root, html[data-theme="light"] {
            --bg: #e8f2ff;
            --bg2: #dbeeff;
            --sky: #cfe5ff;
            --nebula1: rgba(56,189,248,0.10);
            --nebula2: rgba(250,204,21,0.10);
            --card: rgba(255,255,255,0.96);
            --card-b: rgba(14,165,233,0.2);
            --nav: rgba(255,255,255,0.92);
            --nav-b: rgba(14,165,233,0.2);
            --text: #07152f;
            --muted: #334155;
            --chip: #ffffff;
            --chip-b: rgba(14,165,233,0.3);
            --chip-t: #0ea5e9;
            --stars: 0.12;
            --slide-accent: #0ea5e9;
            --line: rgba(14,165,233,.2);
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            background:
                radial-gradient(circle at 10% 10%, var(--nebula1), transparent 36%),
                radial-gradient(circle at 88% 12%, var(--nebula2), transparent 32%),
                radial-gradient(circle at 50% 105%, rgba(52,211,153,0.10), transparent 34%),
                linear-gradient(160deg, var(--bg) 0%, var(--bg2) 50%, var(--sky) 100%);
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
            opacity: var(--stars);
            background-image:
                radial-gradient(circle at 14% 24%, rgba(0,0,0,0.8) 0 1px, transparent 1.6px),
                radial-gradient(circle at 78% 68%, rgba(0,0,0,0.6) 0 1px, transparent 1.5px),
                radial-gradient(circle at 56% 38%, rgba(0,0,0,0.5) 0 1px, transparent 1.4px),
                radial-gradient(circle at 30% 82%, rgba(0,0,0,0.4) 0 1px, transparent 1.3px);
            background-size: 250px 250px, 320px 320px, 210px 210px, 280px 280px;
        }

        .topnav {
            background: var(--nav);
            backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--nav-b);
        }
        
        .planet-card { 
            background: var(--card); 
            border: 1.5px solid var(--card-b); 
            backdrop-filter: blur(12px); 
            box-shadow: 0 20px 40px -20px rgba(14,165,233,0.15);
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(14,165,233,0.2); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(14,165,233,0.3); }

        .btn-3d { 
            position: relative; transition: all 0.2s;
            box-shadow: 0 6px 0 #0284c7, 0 15px 30px -5px rgba(14, 165, 233, 0.3); border: none; cursor: pointer;
        }
        .btn-3d:hover { transform: translateY(-2px); box-shadow: 0 8px 0 #0284c7, 0 20px 40px -10px rgba(14, 165, 233, 0.4); }
        .btn-3d:active { transform: translateY(4px); box-shadow: 0 2px 0 #0284c7, 0 5px 10px -2px rgba(14, 165, 233, 0.2); }

        .section-jump {
            display: grid;
            grid-template-columns: auto minmax(0, 1fr);
            align-items: center;
            gap: .75rem;
            padding: .45rem .55rem .45rem .9rem;
            border: 1px solid var(--card-b);
            border-radius: 1rem;
            background: color-mix(in srgb, var(--card) 82%, transparent);
            box-shadow: inset 0 1px 0 rgba(255,255,255,.8);
        }
        .section-jump label {
            font-size: .61rem;
            line-height: 1;
            font-weight: 900;
            letter-spacing: .16em;
            text-transform: uppercase;
            color: var(--muted);
            white-space: nowrap;
        }

        #sectionSelector {
            width: 100%;
            min-width: 0;
            border: 1px solid var(--line);
            border-radius: .7rem;
            padding: .65rem .8rem;
            background: #ffffff;
            color: var(--text);
            font-weight: 800;
            outline: none;
        }

        #sectionSelector:focus-visible {
            outline: 3px solid color-mix(in srgb, var(--k-yellow) 70%, transparent);
            outline-offset: 3px;
        }

        #slideCard {
            --slide-accent: var(--k-blue-d);
            isolation: isolate;
            border-color: color-mix(in srgb, var(--slide-accent) 42%, var(--card-b));
            background:
                linear-gradient(145deg, color-mix(in srgb, var(--card) 96%, var(--slide-accent) 4%), var(--card));
            box-shadow:
                0 30px 70px -38px rgba(14, 165, 233, .3),
                inset 0 1px 0 rgba(255,255,255,.8);
        }

        #slideCard::before {
            content: "";
            position: absolute;
            inset: 0 0 auto;
            height: .38rem;
            z-index: 3;
            background: linear-gradient(90deg, var(--slide-accent), var(--k-green), var(--k-yellow));
        }

        .slide-stage {
            position: relative;
            z-index: 1;
            width: 100%;
            margin-block: auto;
            padding-block: 1rem;
            max-width: 1120px;
            margin: 0 auto;
        }
        
        .meta { display: flex; align-items: center; justify-content: center; gap: .55rem; flex-wrap: wrap; margin-bottom: 1rem; }
        .pill {
            display: inline-flex;
            align-items: center;
            gap: .35rem;
            padding: .48rem .8rem;
            border-radius: 999px;
            border: 1px solid color-mix(in srgb, var(--slide-accent) 36%, var(--card-b));
            background: color-mix(in srgb, var(--slide-accent) 10%, transparent);
            color: var(--text);
            font-size: .62rem;
            font-weight: 900;
            letter-spacing: .12em;
            text-transform: uppercase;
        }

        .meeting-tab { width:100%; display:grid; grid-template-columns:40px 1fr; gap:11px; align-items:center; padding:10px; color:var(--text); text-align:left; border:1px solid transparent; border-radius:15px; background:transparent; cursor:pointer; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
        .meeting-tab:hover { background: rgba(14,165,233,0.05); border-color: var(--card-b); transform: translateX(4px); }
        .meeting-tab[aria-current="true"] { background: linear-gradient(90deg, rgba(14,165,233,0.1), transparent); border-left: 3px solid var(--chip-t); border-radius: 0 15px 15px 0; }
        .meeting-num { width:40px; height:40px; display:grid; place-items:center; border-radius:12px; color:#fff; background:var(--k-blue-d); font-weight:950; }
        .meeting-tab:not([aria-current="true"]) .meeting-num { color:var(--text); background:rgba(14,165,233,0.1); }
        .meeting-copy strong { display:block; font-size:.83rem; font-family: 'Space Grotesk', sans-serif; font-weight: bold; }
        .meeting-copy small { margin-top:3px; color:var(--muted); font-size:.69rem; line-height:1.25; }

        .panel { 
            position: relative; border: 1px solid var(--card-b); border-radius: 1.25rem; 
            padding: 1.15rem; background: #ffffff; 
            box-shadow: 0 16px 30px -25px rgba(14, 165, 233, .2);
        }
        .panel h3, .panel h4 { font-size: 1rem; font-weight: 900; color: var(--slide-accent); margin-bottom: .45rem; }
        .panel.yellow h3 { color: var(--k-yellow-d); }
        .panel.green h3 { color: var(--k-green); }
        .panel.red h3 { color: #e11d48; }
        .panel p, .panel li { color: var(--muted); font-size: .9rem; line-height: 1.55; }

        .hero { 
            position: relative; overflow: hidden; border: 1px solid color-mix(in srgb, var(--slide-accent) 38%, var(--card-b)); 
            border-radius: 1.6rem; padding: 1.5rem; 
            background: radial-gradient(circle at 90% 10%, color-mix(in srgb, var(--slide-accent) 15%, transparent), transparent 35%),
                        linear-gradient(135deg, color-mix(in srgb, var(--bg2) 60%, transparent), color-mix(in srgb, var(--card) 60%, transparent));
            display: grid; grid-template-columns: 1.35fr .65fr; gap: 24px; align-items: center; min-height: 240px;
        }
        .hero-mark {
            font-size: clamp(4rem, 10vw, 7rem); display: grid; place-items: center;
        }
        .eyebrow { color: var(--k-blue-d); font-size: .78rem; font-weight: 950; letter-spacing: .14em; text-transform: uppercase; }

        .flow { display: flex; align-items: stretch; gap: .65rem; flex-wrap: wrap; }
        .flow > div { flex: 1 1 150px; display: flex; flex-direction: column; justify-content: center; min-height: 7rem; border: 1px solid var(--card-b); border-radius: 1.15rem; padding: 1rem; background: #ffffff; text-align: center; }
        .flow strong { color: var(--k-blue-d); display: block; margin-bottom: 5px; font-weight: 900; }

        .callout { display: flex; flex-direction: column; gap: .5rem; border-left: .32rem solid var(--k-yellow-d); border-radius: .3rem 1rem 1rem .3rem; padding: 1rem 1.1rem; background: #fefce8; color: var(--text); border-top: 1px solid #fef08a; border-right: 1px solid #fef08a; border-bottom: 1px solid #fef08a; }
        .callout strong { color: var(--text); }
        .mode-note { display: flex; gap: 10px; align-items: flex-start; padding: 13px 15px; border: 1px dashed var(--k-blue-d); border-radius: 14px; color: var(--k-blue-d); background: #f0f9ff; margin-top: 1rem; }

        details.reveal { margin-top: 1.5rem; border: 1px solid var(--card-b); border-radius: 0.75rem; overflow: hidden; background: #f8fafc; }
        details.reveal summary { width: 100%; padding: 1rem; background: #f1f5f9; color: var(--k-blue-d); border: none; text-align: left; font-weight: bold; cursor: pointer; display: flex; justify-content: space-between; align-items: center; list-style: none; }
        details.reveal summary::-webkit-details-marker { display: none; }
        details.reveal summary::after { content: "＋"; float: right; color: var(--text); }
        details.reveal[open] summary::after { content: "−"; }
        .reveal-body { padding: 1.5rem; border-top: 1px solid var(--card-b); }

        .choices { display: grid; gap: 10px; margin-top: 16px; }
        .choice { display: block; width: 100%; padding: 1rem; margin-bottom: 0.5rem; background: #ffffff; border: 1px solid var(--card-b); border-radius: 0.5rem; color: var(--text); cursor: pointer; text-align: left; transition: all 0.2s; font-weight: bold; }
        .choice:hover { background: #f0f9ff; border-color: var(--k-blue-d); }
        .choice.correct { border-color: #16a34a; background: #dcfce7; }
        .choice.wrong { border-color: #dc2626; background: #fee2e2; }
        .feedback { min-height: 1.6em; margin-top: 10px; color: var(--muted); font-weight: 800; display: none; }
        
        pre.code { position: relative; overflow: auto; margin: 16px 0; padding: 20px; border: 1px solid #cbd5e1; border-radius: 16px; color: #1e293b; background: #f8fafc; font: 500 .98rem/1.55 "SFMono-Regular",Consolas,"Liberation Mono",monospace; white-space: pre-wrap; tab-size: 4; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); }
        code { padding:.12em .32em; border-radius:6px; color:#b45309; background:#fef3c7; font-family:"SFMono-Regular",Consolas,"Liberation Mono",monospace; font-weight: 600; }
        .output { padding: 14px 17px; border-left: 4px solid var(--k-green); border-radius: 10px; color: #065f46; background: #d1fae5; font-family: "SFMono-Regular",Consolas,monospace; white-space: pre-wrap; margin-top: 0.5rem; border-top: 1px solid #a7f3d0; border-right: 1px solid #a7f3d0; border-bottom: 1px solid #a7f3d0; }

        .grid-2, .grid-3 { display: grid; gap: 16px; }
        .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        
        .quote { min-height: 300px; display: grid; place-items: center; text-align: center; }
        .quote blockquote { max-width: 780px; margin: 0; color: var(--text); font-size: clamp(1.65rem, 4vw, 3rem); font-weight: 850; line-height: 1.28; }
        .quote cite { display: block; margin-top: 22px; color: var(--k-blue-d); font-size: 1rem; font-style: normal; }

        ul, ol { padding-left: 1.35em; list-style-position: inside; }
        ul { list-style-type: disc; }
        ol { list-style-type: decimal; }
        li { margin: .42em 0; }
        
        #slideTitle { margin-bottom: 10px; font-size: clamp(1.8rem, 4vw, 3.15rem); line-height: 1.07; letter-spacing: -.025em; font-family: 'Orbitron', sans-serif; font-weight: 900; }
        #slideSubtitle { margin: 0; color: var(--muted); font-size: clamp(1rem, 2vw, 1.25rem); line-height: 1.5; font-weight: bold; }
        #slideContent { font-size: clamp(1rem, 1.65vw, 1.15rem); line-height: 1.65; font-weight: 500; }
        #slideContent p { margin-bottom: 1rem; }

        @media (max-width: 900px) {
            .hero { grid-template-columns: 1fr; }
            .grid-2, .grid-3 { grid-template-columns: 1fr; }
            .flow { flex-direction: column; }
        }
    </style>"""

html = re.sub(r'    <style>.*?</style>', style_block, html, flags=re.DOTALL)

with open('level1/main_deck.html', 'w') as f:
    f.write(html)

