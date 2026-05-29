import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the position of "// 结束语" section
start_marker = "// 结束语"
end_marker = "// 构建内容区"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    print(f"Found s_ending section from {start_idx} to {end_idx}")
    
    new_section = """      // 结束语
      fullHTML += 'var s_ending="";';
      fullHTML += 's_ending+="【结束语】\\n\\n尊敬的各位家长，今天的家长会到此即将接近尾声。\\n\\n";';
      fullHTML += 's_ending+=""+purpose+"这是我们今天家长会的核心目的，也是我在接下来的工作中会重点关注的方面。\\n\\n";';
      fullHTML += 's_ending+="每一个孩子的成长都倾注了家庭和学校共同的心血。教育是一场长跑，需要我们有足够的耐心和智慧。让我们携手同行，用爱与责任共同托起明天的太阳，为孩子的健康成长保驾护航！\\n\\n";';
      fullHTML += 's_ending+="最后，再次感谢各位家长的到来与支持！如果您在会后有任何问题或建议，欢迎随时与我联系沟通。期待我们携手合作，共同见证孩子们的成长与进步！\\n\\n";';
      fullHTML += 's_ending+="祝各位家长身体健康，工作顺利，阖家幸福！\\n\\n";';
      fullHTML += 's_ending+=""+teacher+"\\n";';
      fullHTML += 's_ending+=""+new Date().getFullYear()+"年";';

      // 构建内容区"""
    
    content = content[:start_idx] + new_section + content[end_idx:]
    print("Replaced s_ending section")
else:
    print(f"Markers not found: start={start_idx}, end={end_idx}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
