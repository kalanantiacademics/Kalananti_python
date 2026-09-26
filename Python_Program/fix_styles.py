with open('level4/deck.html', 'r') as f:
    text = f.read()

import re
style_match = re.search(r'<style>(.*?)</style>', text, re.DOTALL)
if style_match:
    with open('level4_styles.txt', 'w') as out:
        out.write(style_match.group(1))
