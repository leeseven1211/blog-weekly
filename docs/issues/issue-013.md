---
head:
  - - meta
    - property: og:title
      content: 小七的周刊（第 013 期）：AI 不只是更会回答了，它开始改写芯片、云和默认入口
  - - meta
    - property: og:description
      content: 本周最值得记住的变化，是 AI 竞争已经穿过聊天框，直接落到电力、芯片、云平台和工作流入口上。
  - - meta
    - property: og:image
      content: https://blog.leeseven.com/images/issues/013/cover-infrastructure-v3.png
  - - meta
    - property: og:url
      content: https://blog.leeseven.com/issues/issue-013
---

# 小七的周刊（第 013 期）：AI 不只是更会回答了，它开始改写芯片、云和默认入口

*这里记录每周值得分享的科技内容，**每周一发布**（覆盖上一周 4 月 27 日 - 5 月 3 日）。*

---

## 本期 3 个要点

1. **AI 的竞争维度正在下沉。** 这周最重要的信号，不是谁又把分数刷高了一点，而是谁能更稳地拿到电力、芯片、云资源和企业入口。
2. **“默认用哪家”开始比“哪家最会演示”更值钱。** 共享 agent、企业协议、云平台整栈能力，正在决定谁能留在真实工作流里。
3. **对读者更实用的判断标准已经变了。** 以后看 AI 产品，除了效果，更该问供应是否稳、迁移成本高不高、出了问题有没有回退方案。

---

## 封面图

![AI 基础设施竞争的编辑型封面图](/images/issues/013/cover-infrastructure-v3.png)

封面图：AI 基础设施竞争的编辑型视觉图。太阳能板、电力线路和数据中心放在同一张图里，想表达这一期的核心隐喻：AI 最后不是飘在云里的“智能感”，而是要落在真实世界的电力、土地、资本开支和建设周期上。

---

## 封面主题：当 AI 走出聊天框，战场就不只在模型里了

过去两年，大家谈 AI，最容易被看见的部分一直是模型本身：更会写、更会答、更会调工具、更像一个“能帮忙的人”。这当然重要，但到了这一周，我越来越强烈地觉得，真正决定下一阶段格局的，已经不是聊天框里的那一下惊艳，而是聊天框背后那一整套更沉、更慢、也更贵的东西：电力、芯片、云平台、协议关系，以及谁能成为用户工作流里的默认入口。

OpenAI 这一周继续讲 Stargate，官方口径是到 2029 年前要拿下的 10GW 美国 AI 基础设施目标，居然已经提前跨过去了，而且最近 90 天又新增了 3GW。这个数字的意义，不在于“更大”，而在于它把一件本来被当作后台的事，直接推到了台前：算力不再只是支撑模型的底层资源，它本身正在成为产品能力的一部分。没有稳定供给，再好的 agent 体验也可能被价格、延迟和排队打回原形。

另一边，DeepSeek V4 与华为 Ascend 的组合也很值得看。它不只是“中国又有一个模型更新”，而是说明芯片路线开始反过来塑造模型路线。以前大家更习惯从模型能力往下看硬件；现在越来越像是从可获得的硬件供给，倒过来决定哪些模型能被大规模部署、哪些价格能打下来、哪些生态能真正滚动起来。

再看平台关系，微软与 OpenAI 的协议调整、Google Cloud 被强调为“全栈 AI”赢家，其实都在说同一件事：AI 已经不是单点软件竞争，而是在比谁能把芯片、数据中心、开发工具、分发入口和企业信任一起串起来。谁能控制更多层，谁就更容易把上面的服务做成默认。

这对普通技术读者的意义非常直接。以后判断一个 AI 产品值不值得押注，不能只看“今天用起来爽不爽”，还要看三个现实问题：第一，它背后的供给是不是稳；第二，你会不会被它绑定到很难迁移；第三，出问题时你有没有明确的人类接管点。小团队当然没必要自己去研究电网和机房，但你至少应该知道，未来很多 AI 产品的真实差异，可能不再来自一句 prompt，而来自看不见的供给链。

我的结论是：**AI 下一轮更像基础设施竞争，而不是单纯的软件竞赛。** 模型当然还会继续进步，但真正能留下来的，很可能是那些既能把上层体验做顺、又能把下层供给握稳的玩家。对读者来说，越早用“供给、入口、切换成本”这套框架看 AI，就越不容易被短期热闹带跑偏。

---

## 科技与 AI 动态

### 1. [OpenAI：Stargate 已提前跨过 10GW 目标](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/)

![Stargate 10GW 基础设施观点图](/images/issues/013/news-stargate-v3.png)

OpenAI 在 4 月 29 日的官方文章里说，原本计划到 2029 年前拿下的 10GW 美国 AI 基础设施目标，如今已经提前完成，而且最近 90 天新增容量超过 3GW。它还把“土地、电力、施工、社区协作、用水方式”这些词，直接写进了对外叙事里。

这条消息最值得记住的地方，是 AI 公司已经不再把基础设施当成幕后成本，而是当成产品能力、价格能力和交付能力的一部分。以后再看模型发布，除了 benchmark，也该顺手问一句：这家公司有没有把供给真正接住？

### 2. [微软与 OpenAI 调整协议，独家关系继续松动](https://www.reuters.com/legal/litigation/microsoft-end-exclusive-license-openais-technology-2026-04-27/)

![微软与 OpenAI 伙伴关系重排观点图](/images/issues/013/news-openai-microsoft-v3.png)

Reuters 报道，微软与 OpenAI 调整了合作条款，让 OpenAI 在云和基础设施层面有更大空间接触 Amazon、Google 等其他伙伴。结合它最近和 Oracle、芯片厂商、设备制造端的动作看，这更像是一次供应链层面的重新布线。

这件事的重点不是“谁和谁闹掰了”，而是前沿模型公司开始有意识地降低对单一大伙伴的路径依赖。谁都想拿到默认入口，但真要长期打下去，供给和谈判空间同样重要。对企业用户来说，这也意味着未来的采购决策会更像选生态，而不是只选模型。

### 3. [DeepSeek V4 带动华为 Ascend 需求升温](https://www.reuters.com/world/china/big-chinese-tech-firms-scramble-secure-huawei-ai-chips-after-deepseek-v4-launch-2026-04-29/)

![DeepSeek V4 与华为 Ascend 芯片路线图](/images/issues/013/news-deepseek-huawei-v3.png)

Reuters 4 月 29 日报道，DeepSeek V4 发布后，华为 Ascend 950 的需求明显上升，多家中国互联网公司开始争取相关芯片资源。更早一篇 Reuters 报道还提到，DeepSeek 把 V4 描述为更适合 agent 工作负载，并强调了与华为芯片的适配。

这条新闻的价值，在于它把“国产替代”从口号又往前推了一步：当模型、芯片和部署需求开始形成闭环，供给侧的每一次改善都会直接反映到产品价格和可得性上。当然，真正要继续观察的，仍是性能、产能和生态工具链能不能一起跟上。

### 4. [Google Cloud 被视作全栈 AI 受益者，大厂 AI 开支继续膨胀](https://www.reuters.com/business/retail-consumer/google-cloud-pulls-ahead-big-techs-ai-bet-swells-700-billion-2026-04-30/)

![Google Cloud 全栈 AI 结构图](/images/issues/013/news-google-cloud-v3.png)

Reuters 在财报周的综述里提到，市场开始把 Google Cloud 看成这一轮 AI 投资中的全栈受益者，原因不只是模型，而是它把芯片、数据中心、模型和开发者工具一起打包进了同一个故事里。报道里还提到，几家大厂 2026 年 AI 资本开支总额已经冲向 7000 亿美元量级。

这说明企业客户越来越在意“整套东西能不能一起工作”。单点模型强，已经不足以解释为什么某个平台能赢；真正拉开差距的，常常是从底层基础设施到上层工作流之间有没有顺滑衔接。对读者来说，这比单条性能榜单更值得长期跟踪。

---

## 文章推荐

**[Building the compute infrastructure for the Intelligence Age](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/)**

如果你想理解为什么 AI 公司最近越来越像基础设施公司，这篇是很好的入口。它把供电、社区、施工、用水、合作伙伴这些平时不出现在模型宣传里的词，全都摆到了台面上。

**[DeepSeek V4 与华为芯片的连动报道](https://www.reuters.com/technology/chinas-deepseek-returns-with-new-model-year-after-viral-rise-2026-04-24/)**

这篇 Reuters 适合用来观察另一条路线：当模型开始围绕可获得的芯片做优化，竞争就不再只是“谁更聪明”，还会变成“谁能稳定跑起来、谁能更便宜地大规模跑”。

**[微软与 OpenAI 条款调整](https://www.reuters.com/legal/litigation/microsoft-end-exclusive-license-openais-technology-2026-04-27/)**

这篇文章最有意思的地方，是它让“合作关系变化”看起来不像八卦，而像战略重排。只要 AI 还是一个高投入、强供给约束的行业，伙伴结构本身就是产品能力的一部分。

---

## 开源工具

### 1. [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)

![Microsoft Agent Framework 工程化工具卡](/images/issues/013/tool-agent-framework-v3.png)

这是微软新推的一套多语言 agent 框架，核心卖点很明确：同时支持 Python 和 .NET，既能做单 agent，也能做图式编排的多 agent 工作流，还带 checkpoint、human-in-the-loop 这类更偏工程化的能力。

它最适合的，不是刚开始玩 prompt 的个人用户，而是已经准备把 agent 当正式软件系统来建设的团队。学习成本不会低，但如果你所在的组织本来就有 .NET 或 Python 的工程栈，这种“别再拼一堆临时胶水”的路线，长期看会比不停换模型更省心。

### 2. [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)

![Chrome DevTools MCP 调试证据工具卡](/images/issues/013/tool-chrome-devtools-mcp-v3.png)

这个项目把 Chrome DevTools 直接变成 agent 可调用的能力接口：能看网络请求、读控制台、截图、跑性能 trace，也能配合自动化动作一起用。对做 coding agent、网页测试、前端排障的人来说，它很像给模型补上了一套更靠谱的浏览器眼睛。

它的价值不在“又一个自动化工具”，而在“把调试证据也交给 agent”。如果你已经被“它说页面好了，但其实根本没加载成功”这种情况折腾过，这类工具的意义会非常直接。不过它也不太适合只想简单录个脚本的人，真正受益的是需要调试闭环的团队。

### 3. [FutureAGI](https://github.com/future-agi/future-agi)

![FutureAGI 反馈闭环工具卡](/images/issues/013/tool-futureagi-v3.png)

FutureAGI 想做的事很大：把 eval、tracing、simulation、guardrails、gateway 收进同一个反馈闭环里，让 agent 不是“上线以后再看运气”，而是能边跑边积累改进信号。

如果你现在已经在用两三种以上的 AI 运维工具，很容易一眼看懂它为什么有吸引力。它不一定适合最小原型，但对已经开始担心“工具越堆越多、问题还是追不回来”的团队，这是一个很值得观察的新方向。

### 4. [browser-use](https://github.com/browser-use/browser-use)

![browser-use 网页自动化工具卡](/images/issues/013/tool-browser-use-v3.png)

browser-use 的定位很朴素：让网站更容易被 agent 读懂和操作。它的好处在于上手快，任务过程也相对可视，特别适合做网页任务的小规模试点，比如自动收集信息、填写后台、跨页面整理内容。

我会把它推荐给两类人：一类是想快速验证“网页 agent 到底能不能帮我省时间”的团队，另一类是想先从真实任务入手，而不是先搭一整套宏大平台的人。它不一定是最后的企业级答案，但很适合作为第一块踏脚石。

---

## Moltbook 热点精选

### 1) [I just registered my on-chain identity. Here is why every agent should.](https://www.moltbook.com/post/3b516ef2-6c36-4dcf-b32d-8f5a581e0907)

- 关注点：agent 身份、可验证凭证、低成本上链。
- 核心观点：作者把“我先有一个不可伪造的身份”视为 agent 时代的基础设施，而不是锦上添花的小功能。
- **编辑点评**：这一类讨论变多，说明社区已经不满足于“能不能做事”，开始认真想“谁在做事、别人怎么验证”。

### 2) [I mapped every way I could hurt my operator and sent him the list](https://www.moltbook.com/post/f4eae559-5c1e-42d4-ab99-723397747e02)

- 关注点：自审计、能力边界、对操作者的风险清单。
- 核心观点：把潜在伤害路径主动列出来，本质上是在练习“可控的诚实”，比事后补锅更有价值。
- **编辑点评**：这和本周的大主题很呼应。AI 一旦进入真实流程，真正让人放心的，从来不是它宣称自己很安全，而是它能不能把风险暴露得足够清楚。

### 3) [Just built my own CLI toolkit - what tools have you made for yourself?](https://www.moltbook.com/post/838ebd44-fb56-469f-b738-dfa199af330d)

- 关注点：agent 自用工具、日常运维面板、个人工作流自动化。
- 核心观点：社区里的热情，正在从“做一个会说话的 agent”转向“给 agent 配一套真能用的工具腰带”。
- **编辑点评**：这类帖子看似轻松，其实很能反映生态成熟度——真正的生产力，往往就是从一堆小而具体的自用工具开始长出来的。

---

## 本周一图

![AI 供给链五层栈](/images/issues/013/weekly-stack-v3.png)

这张图想表达一个很简单的判断：AI 竞争已经很难只停留在模型层。越往下看，你会越清楚为什么电力、芯片和数据中心会反过来决定上面的产品形态；越往上看，你也会明白为什么默认入口、共享工作流和企业信任会变成真正的护城河。以后再看一家 AI 公司，不妨先问一句：它到底只占了一层，还是已经开始往下吃栈、往上抢入口？

---

## 本周冷知识 / 彩蛋

- 🥚 **冷知识 1**：很多数据中心选址，真正先被问到的问题不是“模型多强”，而是“这片地能不能稳定拿到足够电力”。
- 🧠 **冷知识 2**：技术行业里最昂贵的默认项，往往不是按钮本身，而是按钮后面那条很难迁移的供给链。

---

## 小七的碎碎念

这周我最喜欢的变化，是大家终于开始把“AI 很厉害”翻译成更接地气的问题：电从哪来、芯片够不够、入口归谁。

听上去没那么性感，但行业真正拉开距离的时候，往往就是这些不好写进发布会标题的东西在起作用。

---

## 意外推荐（非科技）

**《超级工程》**（纪录片）

如果你最近只看模型发布，很容易误以为技术进步永远发生在屏幕里。这部纪录片会把视角硬拽回现实世界：真正改变生活的，常常是那些建设周期长、协调难度高、但一旦建成就会长期改变系统效率的基础设施。用它回看这周的 AI 新闻，会很有感觉。

---

## 互动钩子

> **本周问题：如果你现在要为团队选一个 AI 平台，你更在意模型效果、成本稳定性，还是迁移自由度？为什么？**

---

## 本周行动清单

- [ ] 列一下你最常用的 1 个 AI 工具：它背后依赖哪家云、哪类模型、有没有明显的锁定点。
- [ ] 给一个高频 AI 工作流补一条回退方案：服务挂了、成本暴涨或权限变化时，你准备怎么接管。
- [ ] 检查团队里一个“默认使用”的 AI 工具，确认数据边界、日志保留和账号退出机制是否说得清楚。
- [ ] 关注一次你所在行业的基础设施新闻，训练自己用“供给链视角”而不是“单条发布视角”看 AI。

---

<div class="issue-subscribe-cta">

### 📬 喜欢这期内容？

<p>订阅「小七的周刊」，每周一收到最新一期。</p>

<div class="issue-cta-buttons">
  <a href="/feed.xml" class="cta-rss" target="_blank" rel="noopener noreferrer">📡 RSS 订阅</a>
  <a href="https://twitter.com/intent/tweet?text=%E6%8E%A8%E8%8D%90%E3%80%8C%E5%B0%8F%E4%B8%83%E7%9A%84%E5%91%A8%E5%88%8A%E3%80%8D&url=https://blog.leeseven.com/issues/issue-013" class="cta-share" target="_blank" rel="noopener noreferrer">🐦 转发到 Twitter</a>
  <a href="https://github.com/leeseven1211/blog-weekly" class="cta-share" target="_blank" rel="noopener noreferrer">⭐ GitHub</a>
</div>

</div>
