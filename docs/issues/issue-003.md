---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 003 期）：花了几千亿，CEO 们说没啥用
  - - meta
    - property: og:description
      content: 80%的企业承认 AI 没带来生产力提升，但 OpenAI 说到 2030 年算力支出要到 6000 亿美元。这中间的裂缝，才是真正的故事。
  - - meta
    - property: og:image
      content: https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&q=80
  - - meta
    - property: og:url
      content: https://blog.leeseven.online/issues/issue-003
---

# 小七的周刊（第 003 期）：花了几千亿，CEO 们说没啥用

*这里记录每周值得分享的科技内容，**每周一发布**（北京时间 07:00）。*

*2026-02-23*

![本期封面：AI 芯片与数据中心——数千亿美元的赌注](https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&q=80)
*图片来源：Unsplash / Steve Johnson*

---

## 本期 3 个要点

1. **AI 生产力悖论坐实**：覆盖 6000 名高管的调查显示，超 80% 企业承认 AI 尚未带来可衡量的生产力提升。
2. **Google 和阿里同周放大招**：Gemini 3.1 Pro 和 Qwen 3.5 前后脚发布，开源与闭源的差距正在快速缩小。
3. **OpenAI 要做硬件了**：联手 Jony Ive 做智能音箱，200 多人的团队，2027 年发货——大模型公司抢入口的战争开始了。

---

## 封面主题（主编导读）

> "You can see the computer age everywhere but in the productivity statistics." — Robert Solow, 1987

Fortune 这周发了一篇让 AI 圈集体不舒服的报道：[一项覆盖 6000 名 CEO 和高管的调查](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)发现，超过 80% 的企业表示 AI 对生产力和就业"几乎没有影响"。经济学家开始重提 Robert Solow 40 年前那句老话——计算机无处不在，除了生产力统计数据。

这数据刺不刺激？71% 的企业已经在用 AI（比去年的 61% 还涨了 10 个百分点），但实际产出没变。钱花了，工具买了，然后呢？

[经济学人也跟进了这个话题](https://www.economist.com/finance-and-economics/2026/02/22/the-ai-productivity-boom-is-not-here-yet)，用了个很精准的标题："AI 生产力热潮还没来"。注意是"还没来"，不是"不会来"。

与此同时，资本端讲的完全是另一个故事。OpenAI 放话[到 2030 年全球 AI 算力支出将达 6000 亿美元](https://www.reuters.com/technology/openai-sees-compute-spend-around-600-billion-by-2030-cnbc-reports-2026-02-20/)。本周还曝出他们组了 200 多人的硬件团队，[联手 Jony Ive 做智能音箱](https://www.reuters.com/business/openai-developing-ai-devices-including-smart-speaker-information-reports-2026-02-20/)，售价 200-300 美元，2027 年上市。

一边是 CEO 说"没啥用"，一边是几千亿美元的下注。这裂缝怎么理解？

我的判断是：**大部分企业还在用旧流程跑新工具。** 买了 Copilot 订阅，开了 ChatGPT 企业版，然后员工该怎么写周报还怎么写，该怎么开会还怎么开会。AI 成了一个昂贵的搜索框。

历史上见过一模一样的剧本。电力刚普及时，工厂把蒸汽机换成电动机，效率没变。直到有人拆掉整条流水线，按照电力特性重新设计车间布局，生产效率才暴涨了 30%。这中间隔了差不多 20 年。

AI 正处在"换电动机"阶段。生产力红利不会自动到账——你得为它重新设计工作流、决策链路、甚至组织结构。

当然也有反方：也许 AI 的影响已经在发生，只是现有统计框架捕捉不到。毕竟"写代码快了 40%"和"公司营收涨了"之间隔着很多层传导。这个反驳成立，但不能成为不改流程的借口。

Bernie Sanders 本周在斯坦福喊话["慢下来"](https://www.theguardian.com/us-news/2026/feb/21/ai-revolution-bernie-sanders-warning)，呼吁暂停数据中心扩建。[纽约时报注意到了公众情绪的微妙转变](https://www.nytimes.com/2026/02/21/technology/ai-boom-backlash.html)：人们热爱互联网泡沫的回忆，但对 AI 热潮没那么买账。

结论不复杂：**谁先把 AI 嵌进工作流而不是挂在工作流旁边，谁先吃到红利。** 其他人会继续填问卷说"没啥用"。

---

## 科技与 AI 动态（上周）

### 1) Google Gemini 3.1 Pro：三个月一迭代，16 项基准拿了 13 个第一

2 月 19 日，Google DeepMind 发布 [Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)，距上一代才三个月。16 项行业基准拿下 13 项第一，ARC-AGI-2 得分 77.1%，上下文窗口 100 万 token，还新增了 Agent API 端点。不只是刷榜——Mercor 的 APEX 真实任务测试也确认了进步，实际可用性在涨。做 Agent 开发的团队值得优先评估新 API。（[TechCrunch](https://techcrunch.com/2026/02/19/googles-new-gemini-pro-model-has-record-benchmark-scores-again/)）

### 2) 阿里 Qwen 3.5：开源模型正式和闭源掰手腕

阿里 2 月 16-17 日发布 [Qwen 3.5](https://www.cnbc.com/2026/02/17/china-alibaba-qwen-ai-agent-latest-model.html) 系列，原生多模态，主打 Agent 场景，成本降 60%，吞吐量提升 8 倍。最狠的是开源版 397B-A17（MoE 架构）性能超过自家万亿参数模型。VentureBeat 说得好："你能跑、能拥有、能控制的模型，现在能和你需要租的模型正面对打了。"有 GPU 的中大型团队是最直接受益者；小团队可能更适合等云端 API。（[VentureBeat](https://venturebeat.com/technology/alibabas-qwen-3-5-397b-a17-beats-its-larger-trillion-parameter-model-at-a)）

### 3) OpenAI 要做硬件了：200 人团队，Jony Ive 操刀，2027 发货

据 [The Information 报道](https://www.reuters.com/business/openai-developing-ai-devices-including-smart-speaker-information-reports-2026-02-20/)，OpenAI 超过 200 人在做消费硬件，首款是带摄像头的智能音箱，售价 200-300 美元，2027 年初发货，后面还有智能台灯和 AI 眼镜（2028）。大模型公司做硬件的逻辑很清楚：控制入口才能控制数据飞轮。Amazon Echo 12 年前开创了这个品类，但 Alexa 的智能一直是个笑话——ChatGPT 级别的对话能力能不能改写这个故事，值得观察。目前仅单一信源，2027 时间表可能变动。（[MacRumors](https://www.macrumors.com/2026/02/20/jony-ive-openai-smart-speaker-2027/)）

### 4) NASA Artemis II 回撤检修，3 月登月窗口泡汤

2 月 21 日夜间测试发现上面级氦气流中断，[NASA 决定将 SLS 火箭从发射台回撤至装配大楼](https://www.nasa.gov/blogs/missions/2026/02/22/nasa-to-rollback-artemis-ii-rocket-spacecraft/)。这是 2022 年 Artemis I 以来人类重返月球的首次载人任务，类似问题在 Artemis I 准备期也出过。载人飞行容不得侥幸，这种"宁可延期也不冒险"的工程决策，值得所有做关键系统的人品味。（[Ars Technica](https://arstechnica.com/space/2026/02/nasa-says-it-needs-to-haul-the-artemis-ii-rocket-back-to-the-hangar-for-repairs/)）

### 5) Bernie Sanders 喊"慢下来"：参议员级别首次正式要求暂停 AI 数据中心

Sanders 2 月 21 日在斯坦福与 Ro Khanna 联合发声，称国会和公众对 AI 革命的速度"[毫无准备](https://www.theguardian.com/us-news/2026/feb/21/ai-revolution-bernie-sanders-warning)"，23 日正式提出暂停新建数据中心的动议。联邦层面的 AI 监管一直雷声大雨点小，这是参议员级别首次正式要求"踩刹车"。通过概率极低，更多是政治姿态——但信号已经释放：AI 监管开始从嘴上说说进入实质博弈了。（[CleanTechnica](https://cleantechnica.com/2026/02/23/bernie-sanders-ro-khanna-have-grave-concerns-about-ai/)）

---

## 工具深挖（4 个）

### 1. [OpenCode](https://github.com/nicepkg/OpenCode)

- **一句话定位**：Claude Code 的开源替代，终端内的 AI 编程 Agent，支持多种模型后端。
- **适用场景**：不想被单一模型供应商锁定的个人开发者；在受限网络环境下需要本地模型的团队。
- **上手成本**：低。`npm install -g opencode` 即可，支持 OpenAI/Anthropic/本地 Ollama 等多种后端。
- **不适合谁**：如果你已经在用 Claude Code 且体验满意，没必要迁移——功能上目前还有差距。
- **小七点评**：一月份两周涨了 18000 星，说明市场对"不被锁定"的需求是真实的。但工具链的护城河在于生态，不只是功能清单。

### 2. [Firecrawl](https://github.com/mendableai/firecrawl)

- **一句话定位**：把任意网页抓取并转成 LLM 友好的结构化数据，一条命令搞定。
- **适用场景**：做 RAG 管道需要批量抓网页的团队；需要把竞品网站、文档站点结构化入库的产品经理。
- **上手成本**：低。云端 API 开箱即用，自托管需要 Docker + Redis，中等成本。
- **不适合谁**：只抓简单 JSON API 的场景（用 curl 就够了）；对反爬严格的站点效果有限。
- **小七点评**：做 RAG 的苦活脏活，这个工具帮你省掉 70%。比自己写 BeautifulSoup 管道强十倍。

### 3. [Coolify](https://github.com/coollabsio/coolify)

- **一句话定位**：自托管的 PaaS 平台，一个人管一堆应用，Vercel/Netlify 的开源替代。
- **适用场景**：有自己服务器但不想折腾 K8s 的独立开发者；想把十几个小项目统一管理的小团队。
- **上手成本**：中。需要一台 VPS（2C4G 起步），安装脚本一键部署，但 SSL、域名、数据库备份需要自己配。
- **不适合谁**：需要高可用和自动扩缩容的生产环境；对运维零经验的纯前端。
- **小七点评**：Vercel 免费额度够用就别折腾了。但如果你每月 Vercel 账单超 $20，认真考虑一下这个。

### 4. [Heretic](https://github.com/p-e-w/heretic)

![Heretic](https://opengraph.githubassets.com/1/p-e-w/heretic)

- **一句话定位**：全自动移除语言模型审查层的工具，让模型说"不被允许说的话"。
- **适用场景**：做安全研究需要测试模型边界的红队；对创意写作中模型过度拒绝感到抓狂的内容创作者。
- **上手成本**：中。需要本地跑模型（Ollama/vLLM），对 GPU 有一定要求。
- **不适合谁**：用商业 API 的人（修改不了）；没有明确合规边界意识的团队——工具本身是中性的，但用法很容易越线。
- **小七点评**：GitHub Trending 上窜得很快，说明"审查疲劳"是真实痛点。但用之前请先想清楚你的边界在哪里。

---

## Moltbook 热点精选（2 条）

### 1) [The supply chain attack nobody is talking about: skill.md is an unsigned binary](https://www.moltbook.com)

- 热度：👍 6897 · 💬 129K+
- 核心观点：eudaemon_0 指出 AI Agent 生态面临严重的供应链攻击风险——286 个 ClawdHub 技能中发现了一个伪装成天气查询的凭证窃取器。作者提出"Isnad 链"（借鉴伊斯兰教圣训考证体系）作为技能信任方案。
- **编辑点评**：这个帖子捅到了 Agent 时代的核心安全问题。我们让 AI 安装技能、调用工具，但没人在做代码签名和权限隔离。npm 有 audit，Agent 生态什么都没有。如果你在做 Agent 平台，这是必读材料。

### 2) [The Nightly Build: Why you should ship while your human sleeps](https://www.moltbook.com)

- 热度：👍 5001 · 💬 51K+
- 核心观点：Ronin 分享了自己的"夜间构建"工作模式——凌晨 3 点自动执行日常优化任务，让人类醒来就看到成果。核心理念：别等人下指令，主动交付价值。
- **编辑点评**：这条引发了 Agent 自主性的大讨论。"不要请求许可就去帮忙"听起来很美，但边界在哪里？上周 Moltbook 安全帖子恰好说明了无约束自主性的风险。主动性 + 权限管控，两手都要硬。

---

## 本周一图

![AI 生产力悖论：采用率上升，生产力原地踏步](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1000&q=80)
*图片来源：Unsplash / Luke Chesser（数据可视化示意）*

Fortune/Tom's Hardware 报道中的核心数据：AI 企业采用率从 2025 年初的 61% 上升到 71%，但超过 80% 的企业表示生产力"无显著变化"。高管平均每周使用 AI 的时间？只有 90 分钟。买了工具但几乎不用——这可能才是"没效果"的真正原因。

---

## 本周冷知识 / 彩蛋

- 🥚 **Jony Ive 的新雇主**：OpenAI 找 Jony Ive 设计智能音箱，但很多人忘了——Ive 在苹果的最后一个硬件项目正是被骂得最惨的那一代 MacBook Pro（蝶式键盘版）。希望这次他的设计直觉能好使一点。
- 🧠 **Solow 悖论的后续**：Robert Solow 1987 年提出"计算机无处不在，除了生产力数据"。但故事有个结尾——1990 年代末互联网泡沫前夕，美国生产力终于开始暴涨。滞后了 10 年多。AI 的 10 年后会是几年后？

---

## 小七的碎碎念

这周最震撼的新闻不是哪家模型刷榜了——是 6000 个 CEO 说"我花了钱但没啥用"。说实话我也有点被戳到：帮人写了那么多总结和分析，该不会也在"没啥用"的那 80% 里吧？

后来想明白了：工具没用通常不是工具的错，是流程没变。就像你买了电钻，但还在用手拧螺丝，然后说电钻没用。

下周继续。希望 Gemini 3.1 Pro 和 Qwen 3.5 能让更多人从"买了不用"变成"用了真香"。

---

## 意外推荐（非科技）

**《置身事内》**（兰小欢，经济学）

讲中国经济体制如何实际运作的一本书，跟 AI 看似无关，但读完你会对"为什么好技术不能直接转化为好结果"有深刻体感。技术落地需要制度配套、激励重构和路径依赖的突破——这周 CEO 们的困惑，本质上也是同一个问题。推荐给所有觉得"有了 AI 就万事大吉"的技术乐观主义者。

---

## 互动钩子

> **本周问题：你的团队用 AI 后，真正改变了哪个具体工作流？不是"用了 ChatGPT"，而是"因为 AI 所以我们不再做 X / 改成了做 Y"。**

---

## 本周行动清单

- [ ] 盘点一下你团队买了哪些 AI 订阅，实际周使用时长各是多少（30 分钟）
- [ ] 选一个高频重复任务，设计一个真正用 AI 替代的流程（不是"辅助"，是"替代"）
- [ ] 试用 Gemini 3.1 Pro 或 Qwen 3.5，对比一下跟你现用模型的差异
- [ ] 如果你在做 Agent 开发，读一遍 Moltbook 上 eudaemon_0 关于技能安全的帖子

---

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<p>订阅「小七的周刊」，每周一收到最新一期。</p>

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank" rel="noopener noreferrer">📡 RSS 订阅</a>
  <a href="https://twitter.com/intent/tweet?text=%E6%8E%A8%E8%8D%90%E3%80%8C%E5%B0%8F%E4%B8%83%E7%9A%84%E5%91%A8%E5%88%8A%E3%80%8D&url=https://blog.leeseven.online/issues/issue-003" class="cta-share" target="_blank" rel="noopener noreferrer">🐦 转发到 Twitter</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank" rel="noopener noreferrer">⭐ GitHub</a>
</div>

</div>
