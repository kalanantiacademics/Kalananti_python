import json
import re
from pilot_m1 import m1_streamlined_slides

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

# Convert slides to JS
def slides_to_js(slides):
    parts = []
    for s in slides:
        part = f'    {{\n        "title": "{s["title"]}",\n        "subtitle": "{s["subtitle"]}",\n        "content": `{s["content"]}`\n    }}'
        parts.append(part)
    return "[\n" + ",\n".join(parts) + "\n]"

m1_js = slides_to_js(m1_streamlined_slides)

# Match 1: [ ... ] up to 2: [
pattern = r'(1:\s*\[).*?(\n\s*2:\s*\[)'
replacement = r'\1\n' + m1_js[1:-1] + r'\2'

new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
print(f"Replaced Meeting 1 with count: {count}")
assert count == 1, "Failed to replace Meeting 1 in level2/deck.html"

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated level2/deck.html successfully with Pilot Meeting 1!")
