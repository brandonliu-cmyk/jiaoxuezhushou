import os
os.chdir(r'd:\AI教育平台项目资料\12-教学助手优化')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace s_intro, s_greeting, s_feedback, s_plan, s_cooperation, s_qa, s_ending, allContent sections
old_sections = """      // 开场白
      fullHTML += 'var s_intro="";';
      fullHTML += 's_intro+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:12px;\\'>尊敬的各位家长朋友们：</p>";';
      fullHTML += 's_intro+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:12px;\\'>大家好！首先非常感谢各位家长在百忙之中抽出时间参加今天的家长会。我是"+teacher+"，今天非常荣幸能够与大家面对面地交流孩子的教育成长问题。</p>";';
      fullHTML += 's_intro+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:12px;\\'>今天我们家长会的主题是「"+meetingTheme+"」，主要想围绕以下几个方面和大家进行深入交流：</p>";';
      fullHTML += 's_intro+="<ul style=\\'font-size:14px;color:#555;line-height:2;padding-left:24px;margin-bottom:12px;\\'>";';
      fullHTML += 's_intro+="<li>班级整体情况介绍</li>";';
      fullHTML += 's_intro+="<li>学期学情分析与反馈</li>";';
      fullHTML += 's_intro+="<li>各学科教学情况与重点</li>";';
      fullHTML += 's_intro+="<li>家校合作的具体建议</li>";';
      fullHTML += 's_intro+="<li>家长互动答疑环节</li>";';
      fullHTML += 's_intro+="</ul>";';
      fullHTML += 's_intro+="<p style=\\'font-size:14px;color:#555;line-height:2;\\'>希望今天的交流能够帮助大家更全面地了解孩子在校的表现，也让我们携手为孩子的健康成长创造更好的环境。</p>";';

      // 开场问候
      fullHTML += 'var s_greeting="";';
      fullHTML += 's_greeting+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>在正式交流之前，我想先向各位家长表达几点感谢：</p>";';
      fullHTML += 's_greeting+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>第一，感谢各位家长一直以来对学校和班级工作的理解与支持。孩子的教育离不开家庭和学校的紧密配合，正是因为有大家的信任和配合，我们的班级才能不断进步。</p>";';
      fullHTML += 's_greeting+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>第二，感谢大家今天准时参会。教育孩子是学校和家庭共同的责任，今天大家能够放下手中的事务来参加家长会，体现了对孩子的重视和对学校的信任。</p>";';
      fullHTML += 's_greeting+="<p style=\\'font-size:14px;color:#555;line-height:2;\\'>第三，希望各位家长在今天的交流中畅所欲言，积极分享您在家庭教育中的经验和方法，让我们互相学习，共同提高。</p>";';

      // 学情反馈
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

      // 教学计划
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

      // 家校配合建议
      fullHTML += 'var s_cooperation="";';
      fullHTML += 's_cooperation+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>孩子的教育需要学校和家庭的共同努力。在此，我向各位家长提出以下几点配合建议：</p>";';
      fullHTML += 's_cooperation+="<div style=\\'background:#FFF8F8;border:1px solid #FFCDD2;border-radius:10px;padding:14px 16px;margin-bottom:10px;\\'>";';
      fullHTML += 's_cooperation+="<div style=\\'font-size:13px;font-weight:700;color:#C62828;margin-bottom:8px;\\'>⏰ 作息与时间管理</div>";';
      fullHTML += 's_cooperation+="<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\'>";';
      fullHTML += 's_cooperation+="<li>确保孩子每天有充足的睡眠时间（建议8小时以上）</li>";';
      fullHTML += 's_cooperation+="<li>帮助孩子制定合理的学习计划，培养时间管理意识</li>";';
      fullHTML += 's_cooperation+="<li>控制孩子使用电子产品的时间，引导健康使用习惯</li>";';
      fullHTML += 's_cooperation+="</ul></div>";';
      fullHTML += 's_cooperation+="<div style=\\'background:#F3E5F5;border:1px solid #CE93D8;border-radius:10px;padding:14px 16px;margin-bottom:10px;\\'>";';
      fullHTML += 's_cooperation+="<div style=\\'font-size:13px;font-weight:700;color:#7B1FA2;margin-bottom:8px;\\'>📖 家庭学习指导</div>";';
      fullHTML += 's_cooperation+="<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\'>";';
      fullHTML += 's_cooperation+="<li>每天抽时间关注孩子的作业完成情况，适度辅导但不要包办代替</li>";';
      fullHTML += 's_cooperation+="<li>为孩子营造良好的家庭学习氛围，以身作则树立榜样</li>";';
      fullHTML += 's_cooperation+="<li>多与孩子进行学习方面的沟通，了解他们的困惑与需求</li>";';
      fullHTML += 's_cooperation+="<li>鼓励孩子多阅读课外书籍，拓宽知识视野，培养阅读习惯</li>";';
      fullHTML += 's_cooperation+="</ul></div>";';
      fullHTML += 's_cooperation+="<div style=\\'background:#E8F5E9;border:1px solid #A5D6A7;border-radius:10px;padding:14px 16px;margin-bottom:10px;\\'>";';
      fullHTML += 's_cooperation+="<div style=\\'font-size:13px;font-weight:700;color:#2E7D32;margin-bottom:8px;\\'>💬 沟通与心理关怀</div>";';
      fullHTML += 's_cooperation+="<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\'>";';
      fullHTML += 's_cooperation+="<li>关注孩子的情绪变化，及时进行心理疏导与关怀</li>";';
      fullHTML += 's_cooperation+="<li>多给予孩子积极的鼓励与肯定，增强自信心与学习动力</li>";';
      fullHTML += 's_cooperation+="<li>建立平等对话的亲子关系，倾听孩子的想法与感受</li>";';
      fullHTML += 's_cooperation+="<li>避免过度施压，关注孩子心理健康与承受能力</li>";';
      fullHTML += 's_cooperation+="</ul></div>";';
      fullHTML += 's_cooperation+="<div style=\\'background:#E3F2FD;border:1px solid #90CAF9;border-radius:10px;padding:14px 16px;\\'>";';
      fullHTML += 's_cooperation+="<div style=\\'font-size:13px;font-weight:700;color:#1565C0;margin-bottom:8px;\\'>🤝 家校协同配合</div>";';
      fullHTML += 's_cooperation+="<ul style=\\'font-size:13px;color:#555;line-height:2;padding-left:20px;\\'>";';
      fullHTML += 's_cooperation+="<li>积极配合学校和班级的工作要求，关注班级通知与消息</li>";';
      fullHTML += 's_cooperation+="<li>主动与老师沟通孩子在家和在校的表现，形成教育合力</li>";';
      fullHTML += 's_cooperation+="<li>积极参加学校组织的各类家长活动和开放日</li>";';
      fullHTML += 's_cooperation+="<li>如有任何问题或建议，欢迎随时与老师联系沟通</li>";';
      fullHTML += 's_cooperation+="</ul></div>";

      // 答疑环节
      fullHTML += 'var s_qa="";';
      fullHTML += 's_qa+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>各位家长，以上是我今天的发言内容。接下来，我们进入家长答疑环节。</p>";';
      fullHTML += 's_qa+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>在座的各位家长在教育孩子的过程中，一定有很多经验和心得，也会有一些困惑和疑问。现在我把时间交给大家，欢迎各位畅所欲言：</p>";';
      fullHTML += 's_qa+="<ul style=\\'font-size:14px;color:#555;line-height:2;padding-left:24px;margin-bottom:12px;\\'>";';
      fullHTML += 's_qa+="<li>关于孩子学习习惯培养方面的问题</li>";';
      fullHTML += 's_qa+="<li>关于学科辅导与作业指导方面的问题</li>";';
      fullHTML += 's_qa+="<li>关于孩子心理健康与情绪管理方面的问题</li>";';
      fullHTML += 's_qa+="<li>关于家校沟通与配合方面的建议</li>";';
      fullHTML += 's_qa+="<li>其他您关心的问题</li>";';
      fullHTML += 's_qa+="</ul>";';
      fullHTML += 's_qa+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>（家长提问，教师逐一耐心解答，做好记录并在会后整理反馈）</p>";';
      fullHTML += 's_qa+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>感谢各位家长的积极提问和宝贵意见！针对大家提出的共性问题，我会整理后在班级群中进行统一回复；对于个性化问题，请会后单独与我沟通，我会尽我所能提供帮助。</p>";

      // 结束语
      fullHTML += 'var s_ending="";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>尊敬的各位家长，今天的家长会到此即将接近尾声。</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>"+purpose+"这是我们今天家长会的核心目的，也是我在接下来的工作中会重点关注的方面。</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>每一个孩子的成长都倾注了家庭和学校共同的心血。教育是一场长跑，需要我们有足够的耐心和智慧。让我们携手同行，用爱与责任共同托起明天的太阳，为孩子的健康成长保驾护航！</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>最后，再次感谢各位家长的到来与支持！如果您在会后有任何问题或建议，欢迎随时与我联系沟通。期待我们携手合作，共同见证孩子们的成长与进步！</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;margin-bottom:10px;\\'>祝各位家长身体健康，工作顺利，阖家幸福！</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;text-align:right;margin-top:16px;\\'>"+teacher+"</p>";';
      fullHTML += 's_ending+="<p style=\\'font-size:14px;color:#555;line-height:2;text-align:right;\\'>"+new Date().getFullYear()+"年</p>";

      // 构建内容区
      fullHTML += 'var allContent={};';
      fullHTML += 'allContent["开场问候"]={title:"一、开场问候",content:s_greeting};';
      fullHTML += 'allContent["学情反馈"]={title:"二、学情反馈",content:s_feedback};';
      fullHTML += 'allContent["教学计划"]={title:"三、教学计划",content:s_plan};';
      fullHTML += 'allContent["家校配合建议"]={title:"四、家校配合建议",content:s_cooperation};';
      fullHTML += 'allContent["答疑环节"]={title:"五、答疑环节",content:s_qa};';
      fullHTML += 'allContent["结束语"]={title:"六、结束语",content:s_ending};';"""

new_sections = """      // 开场白
      fullHTML += 'var s_intro="";';
      fullHTML += 's_intro+="尊敬的各位家长朋友们：\\\\n\\\\n大家好！首先非常感谢各位家长在百忙之中抽出时间参加今天的家长会。我是"+teacher+"，今天非常荣幸能够与大家面对面地交流孩子的教育成长问题。\\\\n\\\\n今天我们家长会的主题是「"+meetingTheme+"」，主要想围绕以下几个方面和大家进行深入交流：\\\\n";';
      fullHTML += 's_intro+="- 班级整体情况介绍\\\\n";';
      fullHTML += 's_intro+="- 学期学情分析与反馈\\\\n";';
      fullHTML += 's_intro+="- 各学科教学情况与重点\\\\n";';
      fullHTML += 's_intro+="- 家校合作的具体建议\\\\n";';
      fullHTML += 's_intro+="- 家长互动答疑环节\\\\n\\\\n";';
      fullHTML += 's_intro+="希望今天的交流能够帮助大家更全面地了解孩子在校的表现，也让我们携手为孩子的健康成长创造更好的环境。";';

      // 开场问候
      fullHTML += 'var s_greeting="";';
      fullHTML += 's_greeting+="在正式交流之前，我想先向各位家长表达几点感谢：\\\\n\\\\n";';
      fullHTML += 's_greeting+="第一，感谢各位家长一直以来对学校和班级工作的理解与支持。孩子的教育离不开家庭和学校的紧密配合，正是因为有大家的信任和配合，我们的班级才能不断进步。\\\\n\\\\n";';
      fullHTML += 's_greeting+="第二，感谢大家今天准时参会。教育孩子是学校和家庭共同的责任，今天大家能够放下手中的事务来参加家长会，体现了对孩子的重视和对学校的信任。\\\\n\\\\n";';
      fullHTML += 's_greeting+="第三，希望各位家长在今天的交流中畅所欲言，积极分享您在家庭教育中的经验和方法，让我们互相学习，共同提高。";';

      // 学情反馈
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

      // 教学计划
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

      // 家校配合建议
      fullHTML += 'var s_cooperation="";';
      fullHTML += 's_cooperation+="【家校配合建议】\\\\n\\\\n孩子的教育需要学校和家庭的共同努力。在此，我向各位家长提出以下几点配合建议：\\\\n\\\\n";';
      fullHTML += 's_cooperation+="作息与时间管理：\\\\n";';
      fullHTML += 's_cooperation+="- 确保孩子每天有充足的睡眠时间（建议8小时以上）\\\\n";';
      fullHTML += 's_cooperation+="- 帮助孩子制定合理的学习计划，培养时间管理意识\\\\n";';
      fullHTML += 's_cooperation+="- 控制孩子使用电子产品的时间，引导健康使用习惯\\\\n\\\\n";';
      fullHTML += 's_cooperation+="家庭学习指导：\\\\n";';
      fullHTML += 's_cooperation+="- 每天抽时间关注孩子的作业完成情况，适度辅导但不要包办代替\\\\n";';
      fullHTML += 's_cooperation+="- 为孩子营造良好的家庭学习氛围，以身作则树立榜样\\\\n";';
      fullHTML += 's_cooperation+="- 多与孩子进行学习方面的沟通，了解他们的困惑与需求\\\\n";';
      fullHTML += 's_cooperation+="- 鼓励孩子多阅读课外书籍，拓宽知识视野，培养阅读习惯\\\\n\\\\n";';
      fullHTML += 's_cooperation+="沟通与心理关怀：\\\\n";';
      fullHTML += 's_cooperation+="- 关注孩子的情绪变化，及时进行心理疏导与关怀\\\\n";';
      fullHTML += 's_cooperation+="- 多给予孩子积极的鼓励与肯定，增强自信心与学习动力\\\\n";';
      fullHTML += 's_cooperation+="- 建立平等对话的亲子关系，倾听孩子的想法与感受\\\\n";';
      fullHTML += 's_cooperation+="- 避免过度施压，关注孩子心理健康与承受能力\\\\n\\\\n";';
      fullHTML += 's_cooperation+="家校协同配合：\\\\n";';
      fullHTML += 's_cooperation+="- 积极配合学校和班级的工作要求，关注班级通知与消息\\\\n";';
      fullHTML += 's_cooperation+="- 主动与老师沟通孩子在家和在校的表现，形成教育合力\\\\n";';
      fullHTML += 's_cooperation+="- 积极参加学校组织的各类家长活动和开放日\\\\n";';
      fullHTML += 's_cooperation+="- 如有任何问题或建议，欢迎随时与老师联系沟通";';

      // 答疑环节
      fullHTML += 'var s_qa="";';
      fullHTML += 's_qa+="【答疑环节】\\\\n\\\\n各位家长，以上是我今天的发言内容。接下来，我们进入家长答疑环节。\\\\n\\\\n";';
      fullHTML += 's_qa+="在座的各位家长在教育孩子的过程中，一定有很多经验和心得，也会有一些困惑和疑问。现在我把时间交给大家，欢迎各位畅所欲言：\\\\n\\\\n";';
      fullHTML += 's_qa+="- 关于孩子学习习惯培养方面的问题\\\\n";';
      fullHTML += 's_qa+="- 关于学科辅导与作业指导方面的问题\\\\n";';
      fullHTML += 's_qa+="- 关于孩子心理健康与情绪管理方面的问题\\\\n";';
      fullHTML += 's_qa+="- 关于家校沟通与配合方面的建议\\\\n";';
      fullHTML += 's_qa+="- 其他您关心的问题\\\\n\\\\n";';
      fullHTML += 's_qa+="（家长提问，教师逐一耐心解答，做好记录并在会后整理反馈）\\\\n\\\\n";';
      fullHTML += 's_qa+="感谢各位家长的积极提问和宝贵意见！针对大家提出的共性问题，我会整理后在班级群中进行统一回复；对于个性化问题，请会后单独与我沟通，我会尽我所能提供帮助。";';

      // 结束语
      fullHTML += 'var s_ending="";';
      fullHTML += 's_ending+="【结束语】\\\\n\\\\n尊敬的各位家长，今天的家长会到此即将接近尾声。\\\\n\\\\n";';
      fullHTML += 's_ending+=""+purpose+"这是我们今天家长会的核心目的，也是我在接下来的工作中会重点关注的方面。\\\\n\\\\n";';
      fullHTML += 's_ending+="每一个孩子的成长都倾注了家庭和学校共同的心血。教育是一场长跑，需要我们有足够的耐心和智慧。让我们携手同行，用爱与责任共同托起明天的太阳，为孩子的健康成长保驾护航！\\\\n\\\\n";';
      fullHTML += 's_ending+="最后，再次感谢各位家长的到来与支持！如果您在会后有任何问题或建议，欢迎随时与我联系沟通。期待我们携手合作，共同见证孩子们的成长与进步！\\\\n\\\\n";';
      fullHTML += 's_ending+="祝各位家长身体健康，工作顺利，阖家幸福！\\\\n\\\\n";';
      fullHTML += 's_ending+=""+teacher+"\\\\n";';
      fullHTML += 's_ending+=""+new Date().getFullYear()+"年";';

      // 构建内容区
      fullHTML += 'var allContent={};';
      fullHTML += 'allContent["开场问候"]={title:"【一、开场问候】",content:s_greeting};';
      fullHTML += 'allContent["学情反馈"]={title:"【二、学情反馈】",content:s_feedback};';
      fullHTML += 'allContent["教学计划"]={title:"【三、教学计划】",content:s_plan};';
      fullHTML += 'allContent["家校配合建议"]={title:"【四、家校配合建议】",content:s_cooperation};';
      fullHTML += 'allContent["答疑环节"]={title:"【五、答疑环节】",content:s_qa};';
      fullHTML += 'allContent["结束语"]={title:"【六、结束语】",content:s_ending};'"""

if old_sections in content:
    content = content.replace(old_sections, new_sections)
    print("Replaced main sections successfully")
else:
    print("Main sections not found - checking partial match...")
    idx = content.find("// 开场白")
    if idx != -1:
        print(f"Found '// 开场白' at index {idx}")
        # Let's check what's actually in the file
        snippet = content[idx:idx+300]
        print("First 300 chars after '// 开场白':")
        print(repr(snippet))

# Replace result display section (h2 to div)
old_display = """      fullHTML += 'p+="<div id=\\'resultBody\\' style=\\'padding:22px 26px 30px;\\'>";';
      fullHTML += 'p+="<h2 style=\\'font-size:16px;color:#1B5EA7;margin-bottom:14px;font-weight:700;border-left:4px solid #1B5EA7;padding-left:10px;\\'>开场白</h2>"+s_intro;';
      fullHTML += 'for(var idx=0;idx<structs.length;idx++){';
      fullHTML += 'var s=structs[idx];';
      fullHTML += 'if(allContent[s]){';
      fullHTML += 'p+="<h2 style=\\'font-size:15px;color:#1B5EA7;margin:20px 0 10px;font-weight:700;border-left:3px solid #1B5EA7;padding-left:8px;\\'>"+allContent[s].title+"</h2>"+allContent[s].content;';
      fullHTML += '}else{';
      fullHTML += 'p+="<h2 style=\\'font-size:15px;color:#1B5EA7;margin:20px 0 10px;font-weight:700;border-left:3px solid #1B5EA7;padding-left:8px;\\'>"+s+"</h2><p style=\\'color:#888;font-size:13px;\\'>（"+s+"具体内容可根据实际情况补充）</p>";';
      fullHTML += '}}';
      fullHTML += 'if(extra){';
      fullHTML += 'p+="<h2 style=\\'font-size:15px;color:#1B5EA7;margin:20px 0 10px;font-weight:700;border-left:3px solid #1B5EA7;padding-left:8px;\\'>附：附加说明</h2><p style=\\'font-size:13px;color:#555;line-height:1.8;\\'>"+extra.replace(/\\\\n/g,"<br>")+"</p>";';
      fullHTML += '}';"""

new_display = """      fullHTML += 'p+="<div id=\\'resultBody\\' style=\\'padding:22px 26px 30px;font-size:14px;line-height:1.8;color:#555;\\'>";';
      fullHTML += 'p+="<div style=\\'font-size:16px;color:#1B5EA7;margin-bottom:12px;font-weight:700;\\'>【开场白】</div><div style=\\'margin-bottom:16px;white-space:pre-line;\\'>"+s_intro+"</div>";';
      fullHTML += 'for(var idx=0;idx<structs.length;idx++){';
      fullHTML += 'var s=structs[idx];';
      fullHTML += 'if(allContent[s]){';
      fullHTML += 'p+="<div style=\\'font-size:16px;color:#1B5EA7;margin:16px 0 10px;font-weight:700;\\'>"+allContent[s].title+"</div>";';
      fullHTML += 'p+="<div style=\\'line-height:1.8;white-space:pre-line;\\'>"+allContent[s].content+"</div>";';
      fullHTML += '}else{';
      fullHTML += 'p+="<div style=\\'font-size:16px;color:#1B5EA7;margin:16px 0 10px;font-weight:700;\\'>【"+s+"】</div><div style=\\'color:#888;\\'>（"+s+"具体内容可根据实际情况补充）</div>";';
      fullHTML += '}}';
      fullHTML += 'if(extra){';
      fullHTML += 'p+="<div style=\\'font-size:16px;color:#1B5EA7;margin:16px 0 10px;font-weight:700;\\'>【附：附加说明】</div><div style=\\'font-size:13px;color:#555;line-height:1.8;white-space:pre-line;\\'>"+extra+"</div>";';
      fullHTML += '}';"""

if old_display in content:
    content = content.replace(old_display, new_display)
    print("Replaced display section successfully")
else:
    print("Display section not found - checking partial match...")
    if "// 构建内容区" in content:
        idx = content.find("// 构建内容区")
        snippet = content[idx:idx+500]
        print("Content around '构建内容区':")
        print(repr(snippet))

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("File saved successfully")
