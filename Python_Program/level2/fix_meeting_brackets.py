# -*- coding: utf-8 -*-
"""Fix missing closing brackets for meetings 1 to 9 in level2/deck.html"""

import re

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

# For any pattern: "}\n\n            N: [" where N is 2..10, replace with "}\n    ],\n            N: ["
for n in range(2, 11):
    pattern = rf'(\}}\n+)(\s*{n}:\s*\[)'
    replacement = rf'\}}\n    ],\n\2'
    content, count = re.subn(pattern, replacement, content, count=1)
    print(f"Fixed transition to Meeting {n}: count = {count}")

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved deck.html with proper closing brackets.")
