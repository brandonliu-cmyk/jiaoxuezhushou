import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update allContent section - find the marker and update the titles
old_allcontent = """allContent["开场问候"]={title:"一、开场问候",content:s_greeting};
      fullHTML += 'allContent["学情反馈"]={title:"二、学情反馈",content:s_feedback}';
      fullHTML += 'allContent["教学计划"]={title:"三、教学计划",content:s_plan}';
      fullHTML += 'allContent["家校配合建议"]={title:"四、家校配合建议",content:s_cooperation}';
      fullHTML += 'allContent["答疑环节"]={title:"五、答疑环节",content:s_qa}';
      fullHTML += 'allContent["结束语"]={title:"六、结束语",content:s_ending};"""

new_allcontent = """allContent["开场问候"]={title:"【一、开场问候】",content:s_greeting};
      fullHTML += 'allContent["学情反馈"]={title:"【二、学情反馈】",content:s_feedback}';
      fullHTML += 'allContent["教学计划"]={title:"【三、教学计划】",content:s_plan}';
      fullHTML += 'allContent["家校配合建议"]={title:"【四、家校配合建议】",content:s_cooperation}';
      fullHTML += 'allContent["答疑环节"]={title:"【五、答疑环节】",content:s_qa}';
      fullHTML += 'allContent["结束语"]={title:"【六、结束语】",content:s_ending};"""

if old_allcontent in content:
    content = content.replace(old_allcontent, new_allcontent)
    print("Replaced allContent titles")
else:
    print("allContent pattern not found")
    # Try to find it
    idx = content.find('allContent["开场问候"]')
    if idx != -1:
        print(f"Found at index {idx}")
        print(repr(content[idx:idx+300]))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
