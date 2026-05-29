import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of "// 学情反馈" section
start_marker = "// 学情反馈"
end_marker = "// 教学计划"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Found section from {start_idx} to {end_idx}")
    
    # New content for this section
    new_section = """      // 学情反馈
      fullHTML += 'var s_feedback="";';
      fullHTML += 's_feedback+="【学情反馈】\\n\\n"+classInfo+"\\n\\n";';
      fullHTML += 's_feedback+="班级整体表现：\\n";';
      fullHTML += 's_feedback+="- 大部分同学学习态度认真，课堂参与度高，能积极举手发言\\n";';
      fullHTML += 's_feedback+="- 作业完成情况整体良好，但存在个体差异，需要针对性辅导\\n";';
      fullHTML += 's_feedback+="- 班级凝聚力强，集体活动参与积极，学生之间互帮互助氛围浓厚\\n";';
      fullHTML += 's_feedback+="- 学生综合素养逐步提升，在各科目学习中都涌现出一批表现优异的学生\\n\\n";';
      fullHTML += 's_feedback+="同时，我们也要客观看待班级中存在的问题：\\n";';
      fullHTML += 's_feedback+="- 部分学生在时间管理和学习计划方面还需加强\\n";';
      fullHTML += 's_feedback+="- 个别学生课堂注意力集中度有待提高，需要家校协同关注\\n";';
      fullHTML += 's_feedback+="- 学生在自主学习能力和探究精神方面还有提升空间\\n\\n";';
      fullHTML += 's_feedback+="【学生代表案例】\\n";';
      fullHTML += 's_feedback+=""+examples+"\\n\\n";';
      fullHTML += 's_feedback+="以上这些案例告诉我们，每个孩子都有自己的闪光点，关键在于发现并加以培养。希望各位家长能结合自己孩子的特点，因材施教，共同帮助孩子成长进步。";';

      // 教学计划"""
    
    content = content[:start_idx] + new_section + content[end_idx:]
    print("Replaced s_feedback section")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
