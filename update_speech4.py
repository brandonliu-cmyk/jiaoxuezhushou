import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace s_feedback remaining lines
replacements = [
    ("s_feedback+=\"<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\' >\";';", "s_feedback+=\"- 大部分同学学习态度认真，课堂参与度高，能积极举手发言\\\\n\";'.replace('replace', ';')"),
    ("s_feedback+=\"<li>大部分同学学习态度认真，课堂参与度高，能积极举手发言</li>\";';", "s_feedback+=\"- 作业完成情况整体良好，但存在个体差异，需要针对性辅导\\\\n\";'.replace('replace', ';')"),
    ("s_feedback+=\"<li>作业完成情况整体良好，但存在个体差异，需要针对性辅导</li>\";';", "s_feedback+=\"- 班级凝聚力强，集体活动参与积极，学生之间互帮互助氛围浓厚\\\\n\";'.replace('replace', ';')"),
    ("s_feedback+=\"<li>班级凝聚力强，集体活动参与积极，学生之间互帮互助氛围浓厚</li>\";';", "s_feedback+=\"- 学生综合素养逐步提升，在各科目学习中都涌现出一批表现优异的学生\\\\n\\\\n\";'.replace('replace', ';')"),
    ("s_feedback+=\"<li>学生综合素养逐步提升，在各科目学习中都涌现出一批表现优异的学生</li>\";';", "s_feedback+=\"同时，我们也要客观看待班级中存在的问题：\\\\n\";'.replace('replace', ';')"),
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:50]}...")
    else:
        print(f"Not found: {old[:50]}...")

# Replace the closing ul/div and remaining content
old_remaining = """s_feedback+="</ul></div>";
      fullHTML += 's_feedback+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>同时，我们也要客观看待班级中存在的问题：</p>";
      fullHTML += 's_feedback+="<ul style=\\'font-size:14px;color:#555;line-height:2;padding-left:24px;\\' >";
      fullHTML += 's_feedback+="<li>部分学生在时间管理和学习计划方面还需加强</li>";
      fullHTML += 's_feedback+="<li>个别学生课堂注意力集中度有待提高，需要家校协同关注</li>";
      fullHTML += 's_feedback+="<li>学生在自主学习能力和探究精神方面还有提升空间</li>";
      fullHTML += 's_feedback+="</ul>";

      // 学生个例
      fullHTML += 's_feedback+="<div style=\\'background:#FFF9E6;border:1px solid #FFE082;border-radius:10px;padding:14px 16px;margin-top:12px;\\' >";
      fullHTML += 's_feedback+="<div style=\\'font-size:13px;font-weight:700;color:#E65100;margin-bottom:8px;\\'>🌟 学生代表案例</div>";
      fullHTML += 's_feedback+="<p style=\\'font-size:13px;color:#555;line-height:2;margin-bottom:8px;\\'>"+examples+"</p>";
      fullHTML += 's_feedback+="<p style=\\'font-size:13px;color:#555;line-height:2;\\'>以上这些案例告诉我们，每个孩子都有自己的闪光点，关键在于发现并加以培养。希望各位家长能结合自己孩子的特点，因材施教，共同帮助孩子成长进步。</p>";
      fullHTML += 's_feedback+="</div>";

      // 教学计划"""

new_remaining = """s_feedback+="- 部分学生在时间管理和学习计划方面还需加强\\\\n";
      fullHTML += 's_feedback+="- 个别学生课堂注意力集中度有待提高，需要家校协同关注\\\\n";
      fullHTML += 's_feedback+="- 学生在自主学习能力和探究精神方面还有提升空间\\\\n\\\\n";
      fullHTML += 's_feedback+="【学生代表案例】\\\\n";
      fullHTML += 's_feedback+=""+examples+"\\\\n\\\\n";
      fullHTML += 's_feedback+="以上这些案例告诉我们，每个孩子都有自己的闪光点，关键在于发现并加以培养。希望各位家长能结合自己孩子的特点，因材施教，共同帮助孩子成长进步。";

      // 教学计划"""

if old_remaining in content:
    content = content.replace(old_remaining, new_remaining)
    print("Replaced remaining s_feedback content")
else:
    print("Remaining content not found - checking...")
    idx = content.find("s_feedback+=\"</ul></div>")
    if idx != -1:
        print(f"Found at index {idx}")
        print(repr(content[idx:idx+800]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
