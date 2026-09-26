import json
import re

from generate_m9 import m9_slides
from generate_m10 import m10_slides
from generate_m11 import m11_slides
from generate_m12 import m12_slides

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Inject Normalized CSS into <style> if not already present
normalized_css = """
        /* --- Mock Window Normalized Components --- */
        .mock-window {
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 20px 35px -10px rgba(0, 0, 0, 0.45);
            border: 1px solid rgba(255, 255, 255, 0.15);
            background: #1e1e1e;
            font-family: 'Space Grotesk', sans-serif;
            margin: 1rem auto;
            text-align: left;
        }
        .mock-window.light-mode {
            background: #f8f9fa;
            border-color: #cbd5e1;
            color: #1e293b;
        }
        .mock-window-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 14px;
            background: #2b2b2b;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }
        .mock-window.light-mode .mock-window-header {
            background: #e2e8f0;
            border-bottom: 1px solid #cbd5e1;
        }
        .mock-window-title {
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.05em;
            color: #cbd5e1;
        }
        .mock-window.light-mode .mock-window-title {
            color: #334155;
        }
        .mock-window-controls {
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .win-btn {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            display: inline-block;
        }
        .win-close { background: #ff5f56; border: 1px solid #e0443e; }
        .win-min { background: #ffbd2e; border: 1px solid #dea123; }
        .win-max { background: #27c93f; border: 1px solid #1aab29; }
        .mock-window-content {
            padding: 16px;
            position: relative;
        }
        .mock-window-badge {
            display: inline-block;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            padding: 3px 10px;
            border-radius: 999px;
            background: rgba(38, 94, 155, 0.15);
            color: #2563eb;
            border: 1px solid rgba(37, 99, 235, 0.25);
            margin-bottom: 10px;
        }
        html[data-theme="dark"] .mock-window-badge {
            background: rgba(56, 189, 248, 0.15);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
        }
"""

if "/* --- Mock Window Normalized Components --- */" not in content:
    content = content.replace("</style>", normalized_css + "\n    </style>")
    print("Injected normalized .mock-window CSS successfully.")

# 2. Standardize Meeting 1, 2, 3 Titles for sidebar compatibility
content = content.replace('"title": "Welcome to Level 3! 🚀"', '"title": "Meeting 1: Intro to Tkinter/CustomTkinter 🚀"')
content = content.replace('"title": "Welcome to Session 2! 🚀"', '"title": "Meeting 2: Labels & Buttons 🔤"')
content = content.replace('"title": "Welcome to Session 3! 🚀"', '"title": "Meeting 3: Entry Widgets (Input) ⌨️"')
print("Standardized Meeting 1, 2, 3 titles for sidebar.")

# 3. Replace Meetings 9, 10, 11, 12 in meetingData
def slides_to_js(slides):
    parts = []
    for s in slides:
        part = f'        {{\n            "title": "{s["title"]}",\n            "subtitle": "{s["subtitle"]}",\n            "content": `{s["content"]}`\n        }}'
        parts.append(part)
    return "[\n" + ",\n".join(parts) + "\n    ]"

new_m9_js = '    "9": ' + slides_to_js(m9_slides)
new_m10_js = '    "10": ' + slides_to_js(m10_slides)
new_m11_js = '    "11": ' + slides_to_js(m11_slides)
new_m12_js = '    "12": ' + slides_to_js(m12_slides)

new_all_m9_m12 = f"{new_m9_js},\n{new_m10_js},\n{new_m11_js},\n{new_m12_js}\n}};"

# Match from "9": [ up to the end of meetingData (};)
pattern = r'\"9\":\s*\[.*?\n\s*\}\s*;\s*//\s*---\s*DOM'
replacement = new_all_m9_m12 + "\n\n        // --- DOM"

new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
if count == 0:
    # Try another pattern if comment differs
    pattern2 = r'\"9\":\s*\[.*?\n\s*\}\s*;'
    new_content, count = re.subn(pattern2, new_all_m9_m12, content, flags=re.DOTALL)

print(f"Replaced Meetings 9-12 with count: {count}")
assert count > 0, "Failed to replace Meetings 9-12!"

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated level3/deck.html successfully!")
