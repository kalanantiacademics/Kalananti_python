import sys

level2_path = '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2C/Python_Program/level2/deck.html'
level3_path = '/Users/yazidhilmi/Documents/cloud/Kalananti-cloud/Academic_Content/B2C/Python_Program/level3/deck.html'

with open(level2_path, 'r', encoding='utf-8') as f:
    l2_content = f.read()

with open(level3_path, 'r', encoding='utf-8') as f:
    l3_content = f.read()

# Extract meetingData from level2
l2_start = l2_content.find('const meetingData = {')
l2_end = l2_content.find('// --- DOM Elements ---', l2_start)
if l2_start == -1 or l2_end == -1:
    print("Could not find meetingData boundaries in level2")
    sys.exit(1)
l2_meeting_data = l2_content[l2_start:l2_end]

# Apply light mode color fixes to level2 meetingData
l2_meeting_data = l2_meeting_data.replace('bg-slate-900 text-slate-800', 'bg-slate-900 text-slate-100')
l2_meeting_data = l2_meeting_data.replace('bg-slate-900 text-green-400', 'bg-slate-900 text-green-400') # keep this one
l2_meeting_data = l2_meeting_data.replace('text-blue-200', 'text-k-blue font-semibold')
l2_meeting_data = l2_meeting_data.replace('text-blue-300', 'text-k-blue')
l2_meeting_data = l2_meeting_data.replace('text-cyan-300', 'text-k-green font-bold')
l2_meeting_data = l2_meeting_data.replace('text-green-300', 'text-k-green font-bold')
l2_meeting_data = l2_meeting_data.replace('text-slate-300', 'text-[var(--text)] opacity-90')
l2_meeting_data = l2_meeting_data.replace('text-slate-400', 'text-muted')

# Find meetingData in level3 to replace it
l3_start = l3_content.find('const meetingData = {')
l3_end = l3_content.find('// --- DOM Elements ---', l3_start)
if l3_start == -1 or l3_end == -1:
    print("Could not find meetingData boundaries in level3")
    sys.exit(1)

l3_prefix = l3_content[:l3_start]
l3_suffix = l3_content[l3_end:]

# Replace Title text outside of meetingData
l3_prefix = l3_prefix.replace('Level 3', 'Level 2')
l3_suffix = l3_suffix.replace('Level 3', 'Level 2')

new_content = l3_prefix + l2_meeting_data + l3_suffix

with open(level2_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Level 2 successfully migrated to Mission Control theme using safe string replacement!")
