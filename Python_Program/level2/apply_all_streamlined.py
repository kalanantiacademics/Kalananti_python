# -*- coding: utf-8 -*-
"""Apply streamlined Meetings 2-9 to level2/deck.html"""

import re
from gen_m2_m3 import get_m2_slides, get_m3_slides
from gen_m4_m5 import get_m4_slides, get_m5_slides
from gen_m6_m7 import get_m6_slides, get_m7_slides
from gen_m8_m9 import get_m8_slides, get_m9_slides

with open("deck.html", "r", encoding="utf-8") as f:
    content = f.read()

def slides_to_js(slides):
    parts = []
    for s in slides:
        clean_title = s["title"].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        clean_sub = s["subtitle"].replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        part = f'    {{\n        "title": "{clean_title}",\n        "subtitle": "{clean_sub}",\n        "content": `{s["content"]}`\n    }}'
        parts.append(part)
    return "[\n" + ",\n".join(parts) + "\n    ]"

meetings_to_update = {
    2: get_m2_slides(),
    3: get_m3_slides(),
    4: get_m4_slides(),
    5: get_m5_slides(),
    6: get_m6_slides(),
    7: get_m7_slides(),
    8: get_m8_slides(),
    9: get_m9_slides()
}

new_content = content

for m_num, slides in meetings_to_update.items():
    next_num = m_num + 1
    js_str = slides_to_js(slides)
    pattern = rf'([\s{{]{m_num}:\s*\[).*?(\],\s*\n\s*{next_num}:\s*\[)'
    replacement = rf'\g<1>\n' + js_str[1:-5] + rf'\g<2>'
    
    new_content, count = re.subn(pattern, replacement, new_content, flags=re.DOTALL)
    print(f"Replaced Meeting {m_num} ({len(slides)} slides) with match count: {count}")
    assert count == 1, f"Failed to replace Meeting {m_num} in level2/deck.html"

with open("deck.html", "w", encoding="utf-8") as f:
    f.write(new_content)


print("\nSuccessfully updated level2/deck.html for Meetings 2 through 9!")
