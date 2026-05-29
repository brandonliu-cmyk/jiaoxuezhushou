import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace each section one line at a time
# Check if s_feedback starts with the old format
if "s_feedback+=\"<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>\"+classInfo" in content:
    print("Found s_feedback with old format")
    
    # Replace line by line
    content = content.replace(
        "s_feedback+=\"<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>\"+classInfo+\"</p>\";';",
        "s_feedback+=\"【学情反馈】\\\\n\\\\n\"+classInfo+\"\\\\n\\\\n\";';"
    )
    content = content.replace(
        "s_feedback+=\"<div style=\\'background:#F8FBFF;border:1px solid #D8E2EE;border-radius:10px;padding:14px 16px;margin-bottom:12px;\\' >\";';",
        "s_feedback+=\"班级整体表现：\\\\n\";';"
    )
    content = content.replace(
        "s_feedback+=\"<div style=\\'font-size:13px;font-weight:700;color:#1B5EA7;margin-bottom:8px;\\'>📊 班级整体表现</div>\";';",
        "s_feedback+=\"- 大部分同学学习态度认真，课堂参与度高，能积极举手发言\\\\n\";';"
    )
    content = content.replace(
        "s_feedback+=\"<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\' >\";';",
        "s_feedback+=\"- 作业完成情况整体良好，但存在个体差异，需要针对性辅导\\\\n\";';"
    )
    print("Replaced s_feedback lines")
else:
    print("s_feedback pattern not found, checking actual content...")
    # Find where s_feedback starts
    idx = content.find("var s_feedback")
    if idx != -1:
        snippet = content[idx:idx+500]
        print(f"Found s_feedback at index {idx}")
        print("First 500 chars:")
        print(repr(snippet))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved")
