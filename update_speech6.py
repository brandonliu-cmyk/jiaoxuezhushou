import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of "// 教学计划" section
start_marker = "// 教学计划"
end_marker = "// 家校配合建议"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Found s_plan section from {start_idx} to {end_idx}")
    
    new_section = """      // 教学计划
      fullHTML += 'var s_plan="";';
      fullHTML += 's_plan+="【教学计划】\\n\\n各位家长，接下来我来介绍一下"+semester+"各学科的教学安排与重点：\\n\\n";';
      fullHTML += 's_plan+="语文学科：重点培养阅读理解能力与写作表达能力，加强古诗词积累与运用。\\n";';
      fullHTML += 's_plan+="数学学科：注重基础计算能力与逻辑思维培养，加强应用题分析与解决能力训练。\\n";';
      fullHTML += 's_plan+="英语学科：强化听说读写综合能力培养，增加口语表达与阅读拓展训练。\\n";';
      fullHTML += 's_plan+="其他学科：音体美及综合实践课程注重素养培育，促进学生全面发展与个性特长培养。\\n\\n";';
      fullHTML += 's_plan+=""+semester+"教学重点：\\n";';
      fullHTML += 's_plan+="- 系统梳理本学期核心知识点，帮助学生构建完整的知识体系\\n";';
      fullHTML += 's_plan+="- 加强学法指导，培养学生自主学习能力和良好的学习习惯\\n";';
      fullHTML += 's_plan+="- 注重分层教学，针对不同层次学生制定个性化提升方案\\n";';
      fullHTML += 's_plan+="- 加强学科实践活动，提升学生综合运用知识解决问题的能力";';

      // 家校配合建议"""
    
    content = content[:start_idx] + new_section + content[end_idx:]
    print("Replaced s_plan section")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
