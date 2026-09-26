import re

with open('level2/deck.html', 'r', encoding='utf-8') as f:
    text = f.read()

def parse_meeting_slides(m_slice):
    title_matches = list(re.finditer(r'(?<!sub)\"?title\"?:\s*\"(.*?)\"', m_slice))
    slides = []
    for i in range(len(title_matches)):
        start = m_slice.rfind('{', 0, title_matches[i].start())
        if i + 1 < len(title_matches):
            next_start = m_slice.rfind('{', 0, title_matches[i+1].start())
            block = m_slice[start:next_start].strip().rstrip(',')
        else:
            end = m_slice.rfind('}') + 1
            block = m_slice[start:end].strip()
        
        t_m = re.search(r'(?<!sub)\"?title\"?:\s*\"(.*?)\"', block)
        s_m = re.search(r'\"?subtitle\"?:\s*\"(.*?)\"', block)
        c_m = re.search(r'\"?content\"?:\s*([`\"])', block)
        
        title = t_m.group(1) if t_m else ''
        sub = s_m.group(1) if s_m else ''
        
        content = ""
        if c_m:
            quote_char = c_m.group(1)
            c_start = c_m.end()
            if quote_char == '`':
                c_end = block.rfind('`')
            else:
                # find unescaped " before the final }
                c_end = block.rfind('"')
            content = block[c_start:c_end]

        slides.append({'title': title, 'subtitle': sub, 'content': content, 'raw': block})
    return slides

m2_start = text.find('2: [')
m3_start = text.find('3: [')
slides2 = parse_meeting_slides(text[m2_start:m3_start])
print(f"Parsed {len(slides2)} slides for M2.")
for i in [0, 1, 2, 10, 20, 30, 40, 44]:
    print(f"Slide {i+1}: {slides2[i]['title']} (content len: {len(slides2[i]['content'])})")
