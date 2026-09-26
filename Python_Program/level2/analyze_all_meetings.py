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
                c_end = block.rfind('"')
            content = block[c_start:c_end]

        slides.append({'title': title, 'subtitle': sub, 'content': content, 'raw': block})
    return slides

for m_num in range(2, 10):
    m_cur = text.find(f'{m_num}: [')
    m_next = text.find(f'{m_num+1}: [')
    m_slice = text[m_cur:m_next]
    slides = parse_meeting_slides(m_slice)
    print(f"\n==========================================")
    print(f"MEETING {m_num}: Total {len(slides)} slides")
    print(f"==========================================")
    for i, s in enumerate(slides):
        c_len = len(s['content'])
        print(f"[{i+1:02d}] {s['title']} | {s['subtitle']} ({c_len}b)")
