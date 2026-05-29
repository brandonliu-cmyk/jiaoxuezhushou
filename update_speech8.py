import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of "// 答疑环节" section
start_marker = "// 答疑环节"
end_marker = "// 结束语"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Found s_qa section from {start_idx} to {end_idx}")
    
    new_section = """      // 答疑环节
      fullHTML += 'var s_qa="";';
      fullHTML += 's_qa+="【答疑环节】\\n\\n各位家长，以上是我今天的发言内容。接下来，我们进入家长答疑环节。\\n\\n";';
      fullHTML += 's_qa+="在座的各位家长在教育孩子的过程中，一定有很多经验和心得，也会有一些困惑和疑问。现在我把时间交给大家，欢迎各位畅所欲言：\\n\\n";';
      fullHTML += 's_qa+="- 关于孩子学习习惯培养方面的问题\\n";';
      fullHTML += 's_qa+="- 关于学科辅导与作业指导方面的问题\\n";';
      fullHTML += 's_qa+="- 关于孩子心理健康与情绪管理方面的问题\\n";';
      fullHTML += 's_qa+="- 关于家校沟通与配合方面的建议\\n";';
      fullHTML += 's_qa+="- 其他您关心的问题\\n\\n";';
      fullHTML += 's_qa+="（家长提问，教师逐一耐心解答，做好记录并在会后整理反馈）\\n\\n";';
      fullHTML += 's_qa+="感谢各位家长的积极提问和宝贵意见！针对大家提出的共性问题，我会整理后在班级群中进行统一回复；对于个性化问题，请会后单独与我沟通，我会尽我所能提供帮助。";';

      // 结束语"""
    
    content = content[:start_idx] + new_section + content[end_idx:]
    print("Replaced s_qa section")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
