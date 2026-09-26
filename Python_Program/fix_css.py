import re

with open('level1/main_deck.html', 'r') as f:
    html = f.read()

# Revert and properly replace
new_css = """        pre.code { position: relative; overflow: auto; margin: 20px 0; padding: 24px; border: 1px solid #334155; border-radius: 1.25rem; color: #e2e8f0; background: #1e1e1e; font: 500 1.05rem/1.6 "Courier New", Consolas, "Liberation Mono", monospace; white-space: pre-wrap; tab-size: 4; box-shadow: inset 0 2px 10px rgba(0,0,0,0.2); }
        code { padding: .15em .4em; border-radius: 6px; color: #ef4444; background: #fee2e2; font-family: "Courier New", Consolas, "Liberation Mono", monospace; font-weight: 700; }
        .output { padding: 16px 20px; border-left: 5px solid var(--k-green); border-radius: 12px; color: #a7f3d0; background: #064e3b; font-family: "Courier New", Consolas, monospace; white-space: pre-wrap; margin-top: 0.75rem; font-weight: 600; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1); }"""

html = re.sub(r'        pre\.code \{.*?\n        code \{.*?\n        \.output \{.*?\}', new_css, html, flags=re.DOTALL)

with open('level1/main_deck.html', 'w') as f:
    f.write(html)
