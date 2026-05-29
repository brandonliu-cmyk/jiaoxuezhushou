import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update s_feedback section
old_feedback = """      // 学情反馈
      fullHTML += 'var s_feedback="";';
      fullHTML += 's_feedback+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>"+classInfo+"</p>";';
      fullHTML += 's_feedback+="<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:10px;padding:14px 16px;margin-bottom:12px;\\'>";';
      fullHTML += 's_feedback+="<div style=\\'font-size:13px;font-weight:700;color:#1B5EA7;margin-bottom:8px;\\'>📊 班级整体表现</div>";';
      fullHTML += 's_feedback+="<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\'>";';
      fullHTML += 's_feedback+="<li>大部分同学学习态度认真，课堂参与度高，能积极举手发言</li>";';
      fullHTML += 's_feedback+="<li>作业完成情况整体良好，但存在个体差异，需要针对性辅导</li>";';
      fullHTML += 's_feedback+="<li>班级凝聚力强，集体活动参与积极，学生之间互帮互助氛围浓厚</li>";';
      fullHTML += 's_feedback+="<li>学生综合素养逐步提升，在各科目学习中都涌现出一批表现优异的学生</li>";';
      fullHTML += 's_feedback+="</ul></div>";';
      fullHTML += 's_feedback+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>同时，我们也要客观看待班级中存在的问题：</p>";';
      fullHTML += 's_feedback+="<ul style=\\'font-size:14px;color:#555;line-height:2;padding-left:24px;\\'>";';
      fullHTML += 's_feedback+="<li>部分学生在时间管理和学习计划方面还需加强</li>";';
      fullHTML += 's_feedback+="<li>个别学生课堂注意力集中度有待提高，需要家校协同关注</li>";';
      fullHTML += 's_feedback+="<li>学生在自主学习能力和探究精神方面还有提升空间</li>";';
      fullHTML += 's_feedback+="</ul>";

      // 学生个例
      fullHTML += 's_feedback+="<div style=\\'background:#FFF9E6;border:1px solid #FFE082;border-radius:10px;padding:14px 16px;margin-top:12px;\\'>";';
      fullHTML += 's_feedback+="<div style=\\'font-size:13px;font-weight:700;color:#E65100;margin-bottom:8px;\\'>🌟 学生代表案例</div>";';
      fullHTML += 's_feedback+="<p style=\\'font-size:13px;color:#555;line-height:2;margin-bottom:8px;\\'>"+examples+"</p>";';
      fullHTML += 's_feedback+="<p style=\\'font-size:13px;color:#555;line-height:2;\\'>以上这些案例告诉我们，每个孩子都有自己的闪光点，关键在于发现并加以培养。希望各位家长能结合自己孩子的特点，因材施教，共同帮助孩子成长进步。</p>";';
      fullHTML += 's_feedback+="</div>";';

      // 教学计划"""

new_feedback = """      // 学情反馈
      fullHTML += 'var s_feedback="";';
      fullHTML += 's_feedback+="【学情反馈】\\\\n\\\\n"+classInfo+"\\\\n\\\\n";';
      fullHTML += 's_feedback+="班级整体表现：\\\\n";';
      fullHTML += 's_feedback+="- 大部分同学学习态度认真，课堂参与度高，能积极举手发言\\\\n";';
      fullHTML += 's_feedback+="- 作业完成情况整体良好，但存在个体差异，需要针对性辅导\\\\n";';
      fullHTML += 's_feedback+="- 班级凝聚力强，集体活动参与积极，学生之间互帮互助氛围浓厚\\\\n";';
      fullHTML += 's_feedback+="- 学生综合素养逐步提升，在各科目学习中都涌现出一批表现优异的学生\\\\n\\\\n";';
      fullHTML += 's_feedback+="同时，我们也要客观看待班级中存在的问题：\\\\n";';
      fullHTML += 's_feedback+="- 部分学生在时间管理和学习计划方面还需加强\\\\n";';
      fullHTML += 's_feedback+="- 个别学生课堂注意力集中度有待提高，需要家校协同关注\\\\n";';
      fullHTML += 's_feedback+="- 学生在自主学习能力和探究精神方面还有提升空间\\\\n\\\\n";';
      fullHTML += 's_feedback+="【学生代表案例】\\\\n";';
      fullHTML += 's_feedback+=""+examples+"\\\\n\\\\n";';
      fullHTML += 's_feedback+="以上这些案例告诉我们，每个孩子都有自己的闪光点，关键在于发现并加以培养。希望各位家长能结合自己孩子的特点，因材施教，共同帮助孩子成长进步。";';

      // 教学计划"""

if old_feedback in content:
    content = content.replace(old_feedback, new_feedback)
    print("Replaced s_feedback section")
else:
    print("s_feedback section not found")

# Update s_plan section
old_plan = """      // 教学计划
      fullHTML += 'var s_plan="";';
      fullHTML += 's_plan+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>各位家长，接下来我来介绍一下"+semester+"各学科的教学安排与重点：</p>";';
      fullHTML += 's_plan+="<div style=\\'display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:12px;\\'>";';
      fullHTML += 's_plan+="<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:8px;padding:10px 14px;\\'><div style=\\'font-size:12px;font-weight:600;color:#1B5EA7;margin-bottom:4px;\\'>📚 语文学科</div><div style=\\'font-size:12px;color:#555;line-height:1.7;\\'>重点培养阅读理解能力与写作表达能力，加强古诗词积累与运用。</div></div>";';
      fullHTML += 's_plan+="<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:8px;padding:10px 14px;\\'><div style=\\'font-size:12px;font-weight:600;color:#1B5EA7;margin-bottom:4px;\\'>🔢 数学学科</div><div style=\\'font-size:12px;color:#555;line-height:1.7;\\'>注重基础计算能力与逻辑思维培养，加强应用题分析与解决能力训练。</div></div>";';
      fullHTML += 's_plan+="<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:8px;padding:10px 14px;\\'><div style=\\'font-size:12px;font-weight:600;color:#1B5EA7;margin-bottom:4px;\\'>🌍 英语学科</div><div style=\\'font-size:12px;color:#555;line-height:1.7;\\'>强化听说读写综合能力培养，增加口语表达与阅读拓展训练。</div></div>";';
      fullHTML += 's_plan+="<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:8px;padding:10px 14px;\\'><div style=\\'font-size:12px;font-weight:600;color:#1B5EA7;margin-bottom:4px;\\'>🎨 其他学科</div><div style=\\'font-size:12px;color:#555;line-height:1.7;\\'>音体美及综合实践课程注重素养培育，促进学生全面发展与个性特长培养。</div></div>";';
      fullHTML += 's_plan+="</div>";';
      fullHTML += 's_plan+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>"+semester+"教学重点：</p>";';
      fullHTML += 's_plan+="<ul style=\\'font-size:14px;color:#555;line-height:2;padding-left:24px;\\'>";';
      fullHTML += 's_plan+="<li>系统梳理本学期核心知识点，帮助学生构建完整的知识体系</li>";';
      fullHTML += 's_plan+="<li>加强学法指导，培养学生自主学习能力和良好的学习习惯</li>";';
      fullHTML += 's_plan+="<li>注重分层教学，针对不同层次学生制定个性化提升方案</li>";';
      fullHTML += 's_plan+="<li>加强学科实践活动，提升学生综合运用知识解决问题的能力</li>";';
      fullHTML += 's_plan+="</ul>";

      // 家校配合建议"""

new_plan = """      // 教学计划
      fullHTML += 'var s_plan="";';
      fullHTML += 's_plan+="【教学计划】\\\\n\\\\n各位家长，接下来我来介绍一下"+semester+"各学科的教学安排与重点：\\\\n\\\\n";';
      fullHTML += 's_plan+="语文学科：重点培养阅读理解能力与写作表达能力，加强古诗词积累与运用。\\\\n";';
      fullHTML += 's_plan+="数学学科：注重基础计算能力与逻辑思维培养，加强应用题分析与解决能力训练。\\\\n";';
      fullHTML += 's_plan+="英语学科：强化听说读写综合能力培养，增加口语表达与阅读拓展训练。\\\\n";';
      fullHTML += 's_plan+="其他学科：音体美及综合实践课程注重素养培育，促进学生全面发展与个性特长培养。\\\\n\\\\n";';
      fullHTML += 's_plan+=""+semester+"教学重点：\\\\n";';
      fullHTML += 's_plan+="- 系统梳理本学期核心知识点，帮助学生构建完整的知识体系\\\\n";';
      fullHTML += 's_plan+="- 加强学法指导，培养学生自主学习能力和良好的学习习惯\\\\n";';
      fullHTML += 's_plan+="- 注重分层教学，针对不同层次学生制定个性化提升方案\\\\n";';
      fullHTML += 's_plan+="- 加强学科实践活动，提升学生综合运用知识解决问题的能力";';

      // 家校配合建议"""

if old_plan in content:
    content = content.replace(old_plan, new_plan)
    print("Replaced s_plan section")
else:
    print("s_plan section not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved successfully")
