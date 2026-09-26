import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

# 1. Fix the min-height issue for scrolling
# <main id="mainContent" class="flex-1 flex flex-col gap-6 relative min-w-0">
html = html.replace('class="flex-1 flex flex-col gap-6 relative min-w-0"', 'class="flex-1 flex flex-col gap-6 relative min-w-0 min-h-0"')

# <article id="slideCard" class="planet-card flex-1 rounded-[3rem] p-8 sm:p-14 shadow-2xl flex flex-col relative overflow-hidden overflow-y-auto custom-scrollbar" aria-live="polite">
# Actually, if we just make sure it has min-h-0 it should work.
html = html.replace('aria-live="polite">', 'aria-live="polite" style="min-height: 0;">')

# 2. Fix the IDE code styling
css_replacements = {
    r'pre\.code\s*\{[^}]*\}': 'pre.code { position: relative; overflow: auto; margin: 20px 0; padding: 24px; border: 1px solid #334155; border-radius: 1.25rem; color: #e2e8f0; background: #1e1e1e; font: 500 1.05rem/1.6 "Courier New", Consolas, "Liberation Mono", monospace; white-space: pre-wrap; tab-size: 4; box-shadow: inset 0 2px 10px rgba(0,0,0,0.2); }',
    r'code\s*\{[^}]*\}': 'code { padding: .15em .4em; border-radius: 6px; color: #ef4444; background: #fee2e2; font-family: "Courier New", Consolas, "Liberation Mono", monospace; font-weight: 700; }',
    r'\.output\s*\{[^}]*\}': '.output { padding: 16px 20px; border-left: 5px solid var(--k-green); border-radius: 12px; color: #a7f3d0; background: #064e3b; font-family: "Courier New", Consolas, monospace; white-space: pre-wrap; margin-top: 0.75rem; font-weight: 600; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1); }'
}

for pattern, replacement in css_replacements.items():
    html = re.sub(pattern, replacement, html)

with open('level1/main_deck.html', 'w') as f:
    f.write(html)
