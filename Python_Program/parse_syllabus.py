import csv
import urllib.request
from collections import defaultdict

url = "https://docs.google.com/spreadsheets/d/1nbaaeUrlCb_BUJwdVKovwNy0RGmkspYOfzK9CZLy7cM/export?format=csv&gid=1156327196"
response = urllib.request.urlopen(url)
lines = [l.decode('utf-8') for l in response.readlines()]

# The actual headers are on the second row
headers = lines[1].strip().split(',')
reader = csv.DictReader(lines[1:])

levels = defaultdict(list)

for row in reader:
    if row.get('program_id') == 'B2C_PYTHON':
        level = row.get('level_id', '').strip()
        if level.isdigit() or level == '0':
            levels[level].append(row)

with open('syllabus_python_kalananti.md', 'w') as f:
    f.write("# Kalananti B2C Python Program - Syllabus\n\n")
    
    for level in sorted(levels.keys(), key=lambda x: int(x) if x.isdigit() else 99):
        if level == '0':
            f.write(f"## Trial Class (Level {level})\n\n")
        else:
            f.write(f"## Level {level}\n\n")
            
        first_row = levels[level][0]
        f.write(f"**Planet Theme:** {first_row.get('planet_theme', '')}\n\n")
        
        f.write("| Session | Unit / Topic Title | Sub-Topic | Learning Objective | Activity Breakdown & Mastery |\n")
        f.write("|---------|--------------------|-----------|--------------------|------------------------------|\n")
        
        for row in sorted(levels[level], key=lambda x: int(x.get('session_order', '99')) if x.get('session_order', '').isdigit() else 99):
            session = row.get('session_order', '')
            unit = row.get('topic_title', '').replace('\n', '<br>')
            topic = row.get('sub-topic_title', '').replace('\n', '<br>')
            objective = row.get('learning_objective', '').replace('\n', '<br>')
            
            activity = row.get('activity_breakdown', '').replace('\n', '<br>')
            focus = row.get('mastery_focus', '').replace('\n', ' ')
            activity_mastery = f"**Focus:** {focus}<br>**Activity:**<br>{activity}" if activity else focus
            
            f.write(f"| {session} | {unit} | {topic} | {objective} | {activity_mastery} |\n")
            
        f.write("\n---\n\n")

print("Generated syllabus_python_kalananti.md")
