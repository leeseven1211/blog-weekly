---
title: 第 003 期｜AI 的生产力悖论
date: 2026-02-23
description: 数千位 CEO 承认 AI 没带来生产力提升，但资本还在疯狂加注。这中间的裂缝，才是真正值得关注的故事。
---

# 第 003 期｜AI 的生产力悖论

> 每周一发布，记录上一周值得关注的技术动态。

*2026-02-23*

---

## 本期主题：花了几千亿，CEO 们说没啥用

Fortune 这周发了一篇很有意思的报道：[一项覆盖数千位 CEO 的调查显示](https://fortune.com/2026/02/17/ai-productivity-paradox-ceo-study-robert-solow-information-technology-age/)，AI 对就业和生产力的实际影响几乎为零。经济学家开始重提 Robert Solow 40 年前的老梗——"计算机无处不在，除了生产力统计数据"。

这不是反 AI 的论调，而是一个事实：大多数企业还没搞明白怎么用 AI 创造真正的价值。买了 Copilot 订阅，开了几个 ChatGPT 企业版账号，然后呢？工作流没变，决策方式没变，组织结构没变。AI 成了一个昂贵的搜索框。

与此同时，资本端的热情完全是另一个故事。OpenAI 本周放话[到 2030 年算力支出将达 6000 亿美元](https://www.reuters.com/technology/openai-sees-compute-spend-around-600-billion-by-2030-cnbc-reports-2026-02-20/)。Meta [扩大了与 Nvidia 的合作](https://www.cnbc.com/2026/02/17/meta-nvidia-deal-ai-data-center-chips.html)，数百万块 GPU 往数据中心里塞。纽约时报也注意到了这种割裂：[人们热爱互联网泡沫，但对 AI 热潮没那么买账](https://www.nytimes.com/2026/02/21/technology/ai-boom-backlash.html)。

我的看法很简单：**AI 的价值不在模型本身，在于你愿不愿意为它重新设计工作流。** 就像电力刚出现时，工厂只是把蒸汽机换成电动机，生产效率没变。直到有人重新设计了整条流水线，电力的价值才真正释放。AI 正处在"换电动机"的阶段，大部分人还没走到"重新设计流水线"那一步。

谁先走到，谁吃肉。

---

## 科技动态

**阿里发布 Qwen 3.5，开源模型追上闭源前沿** — 阿里在春节前夕发布 [Qwen 3.5](https://www.reuters.com/world/china/alibaba-unveils-new-qwen35-model-agentic-ai-era-2026-02-16/)，主打原生多模态和 Agent 任务执行能力。CNBC 的报道称其性能[已接近闭源前沿模型](https://www.cnbc.com/2026/02/17/china-alibaba-qwen-ai-agent-latest-model.html)。中国开源 AI 的追赶速度，比大多数人预期的要快。

**OpenAI 要做硬件了** — 据 [The Information 报道](https://www.reuters.com/business/openai-developing-ai-devices-including-smart-speaker-information-reports-2026-02-20/)，OpenAI 正在开发智能音箱等 AI 终端设备。同一周，Meta 也[重启了智能手表项目](https://www.reuters.com/business/meta-reboots-smartwatch-plan-aims-debut-2026-information-reports-2026-02-18/)。大模型公司集体往硬件走，逻辑很明确：控制入口，才能控制数据飞轮。

**Google 联手 Sea 做电商 AI** — [Google 与 Sea（Shopee 母公司）达成合作](https://www.reuters.com/world/asia-pacific/google-shopee-owner-sea-develop-ai-tools-e-commerce-gaming-2026-02-19/)，在电商和游戏场景中推 AI 工具。不是发论文，不是刷榜，是直接嵌到真实交易流程里。这种"AI 落地到业务毛细血管"的动作比任何 benchmark 都有说服力。

**NASA Artemis II 可能延期** — [发射前测试发现氦气流异常](https://www.reuters.com/science/nasa-roll-back-artemis-ii-spacecraft-impacting-march-launch-window-2026-02-21/)，火箭可能回撤检修，3 月发射窗口悬了。载人绕月这事，急不得。

**欧盟推"欧洲制造"法案** — [草案要求](https://www.reuters.com/sustainability/boards-policy-regulation/what-is-eus-draft-made-europe-law-2026-02-17/)公共资金支持的关键技术必须满足一定比例的欧洲本地化。清洁能源、先进制造首当其冲。保护主义？也许。但供应链安全焦虑是真实的。

**美国多州密集推进 AI 立法** — 华盛顿州的 [AI 监管法案 HB 2225](https://www.troutmanprivacy.com/2026/02/proposed-state-ai-law-update-february-23-2026/) 以 69-28 通过众议院。联邦层面没动静，各州先跑起来了。AI 合规将是 2026 年最绕不开的话题之一。

---

## 开源工具

- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** — 终端里的 AI 编程 Agent，不是问答，是直接帮你改代码、跑 Git 操作。用了就回不去。
- **[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)** — 把任意网站抓取转成 LLM 友好的结构化数据，做 RAG 管道的必备工具。
- **[n8n-io/n8n](https://github.com/n8n-io/n8n)** — 开源工作流自动化，比 Zapier 灵活，支持自托管。适合把各种 SaaS 和 AI 串起来。
- **[coollabsio/coolify](https://github.com/coollabsio/coolify)** — 自托管 PaaS，一个人也能管一堆应用。Vercel 的开源替代。
- **[ladybirdbrowser/ladybird](https://github.com/ladybirdbrowser/ladybird)** — 从零自研引擎的开源浏览器。不依赖 Chromium，这份勇气本身就值得关注。

---

## 值得一读

- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)（Rich Sutton）— AI 发展 70 年最大的教训：通用方法 + 算力 > 精心设计的先验知识。短文，常读常新。
- [How to Write Usefully](https://paulgraham.com/useful.html)（Paul Graham）— 写东西别追求"看起来对"，追求"有用"。四个字的写作准则。
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)（Anthropic）— MCP 让模型接入工具这件事有了标准化方案。做 Agent 集成的人必读。

---

## 一句话

> "You can see the computer age everywhere but in the productivity statistics."
>
> — Robert Solow, 1987

四十年了，把"computer"换成"AI"，这句话居然还能用。也许该着急的不是技术不行，而是我们用技术的方式还没变。

---

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank">📡 RSS 订阅</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank">⭐ GitHub</a>
</div>
</div>
