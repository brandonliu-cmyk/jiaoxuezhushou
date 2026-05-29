import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of "// 家校配合建议" section
start_marker = "// 家校配合建议"
end_marker = "// 答疑环节"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Found s_cooperation section from {start_idx} to {end_idx}")
    
    new_section = """      // 家校配合建议
      fullHTML += 'var s_cooperation="";';
      fullHTML += 's_cooperation+="【家校配合建议】\\n\\n孩子的教育需要学校和家庭的共同努力。在此，我向各位家长提出以下几点配合建议：\\n\\n";';
      fullHTML += 's_cooperation+="作息与时间管理：\\n";';
      fullHTML += 's_cooperation+="- 确保孩子每天有充足的睡眠时间（建议8小时以上）\\n";';
      fullHTML += 's_cooperation+="- 帮助孩子制定合理的学习计划，培养时间管理意识\\n";';
      fullHTML += 's_cooperation+="- 控制孩子使用电子产品的时间，引导健康使用习惯\\n\\n";';
      fullHTML += 's_cooperation+="家庭学习指导：\\n";';
      fullHTML += 's_cooperation+="- 每天抽时间关注孩子的作业完成情况，适度辅导但不要包办代替\\n";';
      fullHTML += 's_cooperation+="- 为孩子营造良好的家庭学习氛围，以身作则树立榜样\\n";';
      fullHTML += 's_cooperation+="- 多与孩子进行学习方面的沟通，了解他们的困惑与需求\\n";';
      fullHTML += 's_cooperation+="- 鼓励孩子多阅读课外书籍，拓宽知识视野，培养阅读习惯\\n\\n";';
      fullHTML += 's_cooperation+="沟通与心理关怀：\\n";';
      fullHTML += 's_cooperation+="- 关注孩子的情绪变化，及时进行心理疏导与关怀\\n";';
      fullHTML += 's_cooperation+="- 多给予孩子积极的鼓励与肯定，增强自信心与学习动力\\n";';
      fullHTML += 's_cooperation+="- 建立平等对话的亲子关系，倾听孩子的想法与感受\\n";';
      fullHTML += 's_cooperation+="- 避免过度施压，关注孩子心理健康与承受能力\\n\\n";';
      fullHTML += 's_cooperation+="家校协同配合：\\n";';
      fullHTML += 's_cooperation+="- 积极配合学校和班级的工作要求，关注班级通知与消息\\n";';
      fullHTML += 's_cooperation+="- 主动与老师沟通孩子在家和在校的表现，形成教育合力\\n";';
      fullHTML += 's_cooperation+="- 积极参加学校组织的各类家长活动和开放日\\n";';
      fullHTML += 's_cooperation+="- 如有任何问题或建议，欢迎随时与老师联系沟通";';

      // 答疑环节"""
    
    content = content[:start_idx] + new_section + content[end_idx:]
    print("Replaced s_cooperation section")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
