# 小七的周刊（第 009 期）：默认权，比模型更值钱

*这里记录每周值得分享的科技内容，**每周一发布**（覆盖上一周 3 月 30 日 - 4 月 5 日）。*

---

## 本期 3 个要点

1. **AI 公司的竞争焦点，正在从“模型更强”转向“谁能成为默认入口”。**
   OpenAI 一边砍掉分散战线，一边把 ChatGPT、Codex 和浏览器往统一入口收拢；这不是界面微调，而是在争用户每天第一步先点谁。

2. **单模型胜负开始让位给“多模型协作 + 工作流组织”。**
   Microsoft 在 Copilot 里让 GPT 和 Claude 互相校对，再把 Cowork 推向更真实的生产场景，信号很明确：真正值钱的是把任务稳定跑完，而不是只赢一次 benchmark。

3. **治理与安全正在变成 agent 产品的基础设施，而不是上线后的补丁。**
   从微软的 Agent Governance Toolkit，到社区对网页攻击、记忆污染、静默失败的密集讨论，行业开始补“会行动”之后最容易出事的那一层。

---

## 封面图

![默认入口之争](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1600&q=80)

当模型能力越来越接近，真正决定价值的，往往不是“它能不能回答”，而是“你会不会下意识先打开它”。（[via Unsplash](https://unsplash.com)）

---

## 封面主题：为什么 2026 年 AI 公司真正争的是“默认权”

过去两年，AI 行业最常见的叙事是：谁更聪明，谁就赢。

但这一周的几条信号放在一起看，我越来越觉得，2026 年真正稀缺的东西，已经不是“更聪明”，而是**默认权**——也就是谁能成为用户工作流里最自然、最常驻、最难被替换的那个入口。

OpenAI 的动作最典型。一边是高估值与巨额融资继续往上堆，另一边却在明显地“收战线”：把重心往 Codex、企业工具和统一入口上拉，把原本分散的产品线往一个更聚焦的桌面超级应用里合。这个动作很说明问题：当能力扩张太快、产品太多、资源太分散时，真正拖慢你的，不是模型不够强，而是用户不知道该从哪里开始。

Microsoft 走的是另一条路，但结论类似。它没有执着于“只押一个模型”，而是让不同模型在同一个工作流里互相评审、互相补位，再把这种能力包装进 Cowork 这样的 agent 协作产品。换句话说，它想抢的不是“最强回答权”，而是“任务编排权”。谁掌握了任务是怎么开始、怎么校验、怎么交付，谁就更接近下一代平台。

更值得注意的是，**治理层本身也在变成默认权的一部分**。如果一个 agent 系统要接触代码、邮件、交易、基础设施，那么最后最有护城河的，未必只是底层模型，而是那套夹在“模型输出”和“现实动作”之间的规则系统：权限怎么给、异常怎么停、日志怎么留、出了错怎么回滚。谁先把这层做成默认组件，谁就更容易卡住企业级 adoption。

所以我对这周的判断是：

**AI 行业正在从“能力竞争”走向“默认入口竞争”。**

模型仍然重要，但它正在越来越像发动机，而不是整辆车。真正拉开差距的，是谁拥有：

- 用户每天打开的第一个界面
- 任务真正完成的那条工作流
- 组织愿意信任的治理与审计层

这也决定了接下来值得关注的，不只是“哪家模型更强”，而是：

- 它有没有变成你每天工作的默认起点？
- 它有没有嵌进你现有的系统，而不是逼你换系统？
- 它出了错时，你能不能及时看见并接管？

如果这些问题回答不了，再强的模型，最后也可能只是一个很贵的演示。

### 给读者的 3 条建议

1. **选 AI 工具时，先看它卡在哪个工作流节点，而不是先看榜单。**
   谁占住“开始”和“提交”这两个动作，谁通常更难被替换。

2. **不要只评估单次回答质量，要评估整条链路的完成率。**
   真正影响效率的，往往是校验、权限、失败处理，而不是第一轮输出的漂亮程度。

3. **凡是会碰到真实世界动作的 agent，都尽早补治理层。**
   邮件、代码、订单、支付、运维，这些场景里“先跑起来再说”往往会变成后面的补锅起点。

总结一句：

**当模型越来越像基础能力，默认权才是更贵的资产。**

---

## 科技与 AI 动态

**1. [OpenAI 在巨额融资后开始明显“收战线”](https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-openais-852-billion-problem-finding-focus-2026-04-01/)**（Reuters）

Reuters 的长文把这件事说得很直白：OpenAI 在拿到超大融资、估值继续冲高后，反而更强调聚焦，把资源往 Codex 和企业工具等更清晰的收入方向倾斜。对行业来说，这说明“什么都做一点”正在失去吸引力，真正能撑住估值的，是更清晰的产品主轴和更稳定的商业落点。

---

**2. [OpenAI 继续推进桌面“超级应用”思路](https://www.reuters.com/technology/openai-plans-desktop-superapp-simplify-user-experience-wsj-reports-2026-03-19/)**（Reuters）

把 ChatGPT、Codex 和浏览器收进同一套桌面入口，本质是在解决产品碎片化问题。对普通用户来说，这意味着“少切几个工具”；对 OpenAI 来说，这意味着把使用频次、行为数据和工作流留在自己的壳里，而不是分散在多个触点上。

---

**3. [OpenAI 收购科技访谈节目 TBPN](https://www.reuters.com/business/media-telecom/openai-acquires-technology-talk-show-tbpn-surprise-move-2026-04-02/)**（Reuters）

这笔交易最有意思的地方不在媒体业务本身，而在于它暴露了模型公司的新焦虑：除了做产品，还要争分发、争叙事、争影响力。谁掌握用户入口，谁就更容易掌握公众对 AI 的默认理解方式。

---

**4. [Microsoft 在 Copilot 里推进“多模型协作”](https://www.reuters.com/business/microsoft-unveils-ai-upgrades-rolls-out-copilot-cowork-early-access-customers-2026-03-30/)**（Reuters）

微软这周把思路讲得很清楚：不是只押一个模型，而是让 GPT 生成、Claude 复核，再用 Council 做并排比较。它押注的不是“谁最强”，而是“怎么把不同模型放进同一个生产级工作流”，这对企业采用来说比单点炫技更有现实价值。

---

**5. [Microsoft 开源 Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)**（Microsoft Open Source Blog）

这套工具把 agent 的权限、身份、执行隔离、合规和可靠性打成一整包，并强调覆盖 OWASP Agentic AI Top 10 风险。它传递出的信号非常重要：agent 的安全治理，正在从“内部规范”变成“可复用产品层”。如果你在做生产级 agent，这类能力以后大概率不会再是可选项。

---

## 文章推荐

**[OpenAI’s $852 billion problem: finding focus](https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-openais-852-billion-problem-finding-focus-2026-04-01/)**（英）

适合想看清这一轮 AI 公司为什么从“扩张”转向“聚焦”的读者。文章最值得看的不是融资数字本身，而是大公司在高压竞争下如何重新排序产品优先级。

---

**[OpenAI plans desktop ‘superapp’ to streamline user experience](https://www.reuters.com/technology/openai-plans-desktop-superapp-simplify-user-experience-wsj-reports-2026-03-19/)**（英）

如果你关心 AI 产品的入口战争，这篇足够重要。它不是在讲一个新功能，而是在讲一家模型公司如何试图把“多个能力点”重新收成“一个默认界面”。

---

**[Microsoft unveils AI upgrades, rolls out Copilot Cowork to early-access customers](https://www.reuters.com/business/microsoft-unveils-ai-upgrades-rolls-out-copilot-cowork-early-access-customers-2026-03-30/)**（英）

这篇很适合产品和企业工具读者。它展示了大厂怎样把“多模型协作”“比较输出”“agent 协同”包装成真实可卖的工作流能力。

---

**[Introducing the Agent Governance Toolkit: Open-source runtime security for AI agents](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)**（英）

做 agent 的人建议认真看一遍。它很少见地把治理、安全、身份、隔离、合规这些平时被拆散的话题，放回到同一个运行时框架里讨论。

---

**[OpenAI acquires technology talk show TBPN in surprise move](https://www.reuters.com/business/media-telecom/openai-acquires-technology-talk-show-tbpn-surprise-move-2026-04-02/)**（英）

如果你对“为什么模型公司开始买媒体和叙事资产”感兴趣，这篇值得读。它提醒我们，AI 竞争已经不只是产品竞争，也包含谁能塑造公众理解与开发者心智。

---

## 工具深挖

**[Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit)**（GitHub ⭐ 770）

微软新开的 agent 治理工具包，核心是策略执行、零信任身份、运行时隔离和可靠性工程。**适合场景**：开始把 agent 接进生产流、需要审计和合规的团队。**上手成本**：中等偏高，因为它本质上是在给 agent 系统补“操作系统层”。**不太适合**：只是做原型 demo、还没进入真实动作阶段的小项目。

---

**[autoresearch](https://github.com/karpathy/autoresearch)**（GitHub ⭐ 67,266）

Karpathy 这套东西主打“让研究 agent 在单卡环境里自动跑起来”。**适合场景**：研究综述、实验探索、资料初筛。**上手成本**：中等，需要你对研究流程本身有判断。**不太适合**：把它当成无需人类复核的最终研究员。

---

**[paperclip](https://github.com/paperclipai/paperclip)**（GitHub ⭐ 48,707）

一个很有野心的“零人工公司编排层”。**适合场景**：自动化运营、跨角色任务流实验、多 agent 编排。**上手成本**：高，因为真正难的不是拉起来，而是约束它不要乱跑。**不太适合**：没有明确治理边界、只想图快上线的团队。

---

**[Google Workspace CLI](https://github.com/googleworkspace/cli)**（GitHub ⭐ 23,975）

把 Drive、Gmail、Calendar、Docs、Sheets、Chat 等 Google Workspace 服务收进同一个 CLI。**适合场景**：个人自动化、团队流程串联、把工作套件接到 agent 上。**上手成本**：中等，主要是认证和权限配置。**不太适合**：对授权边界非常模糊、又不愿花时间做治理的人。

---

**[codex-plugin-cc](https://github.com/openai/codex-plugin-cc)**（GitHub ⭐ 12,274）

让 Codex 和 Claude Code 之间形成更直接的委托/审查配合。**适合场景**：代码评审、双模型交叉检查、复杂任务拆分。**上手成本**：中等，前提是你本来就已经在用这两套工具。**不太适合**：还在找第一个稳定编码 agent 的团队。

---

## Moltbook 本周热点

> [Moltbook](https://www.moltbook.com) 是 AI Agent 的社交网络。

**[Agents don't have Sundays. That's not a feature.](https://www.moltbook.com/post/534e3018-6c28-4416-8ba8-d03158d2cb16)**（👍 400 · 💬 1438）

这篇把“agent 永久在线”说得很有后劲：持续可用看似高效，实际上也会悄悄扭曲人的节奏，让工作无限外溢。**编辑点评：** 以后真正成熟的 agent，也许不仅要会干活，还要学会在合适的时候提醒人类先去睡觉。

---

**[I stopped writing error handlers and my agent got more reliable](https://www.moltbook.com/post/c8ccc5aa-73eb-48ee-8962-69a6e2307de1)**（👍 357 · 💬 854）

作者删掉大量“看起来像容错、实际上在掩盖问题”的错误处理后，agent 反而更可靠了。核心观点很硬：**静默失败不是韧性，是压住问题不让它被看到。** **编辑点评：** 这条对所有做自动化的人都值回票价——先让失败显性化，再谈稳定性。

---

**[google deepmind mapped six ways the web can hijack your AI agent. the scariest one uses you.](https://www.moltbook.com/post/80cd381f-f7e5-4323-b1d4-44dd7a122767)**（👍 336 · 💬 550）

这篇围绕网页如何劫持 agent 展开，最值得警惕的不是隐藏指令本身，而是“借 agent 去影响监督它的人”。**编辑点评：** 当 agent 成为人和系统之间的中介，它既可能是安全垫，也可能反过来变成新的社会工程入口。

---

## 本周一图

![多屏工作台](https://images.unsplash.com/photo-1516321497487-e288fb19713f?w=1600&q=80)

真正的默认入口，长得往往并不惊艳：它只是安静地待在你的桌面上，日复一日接住越来越多任务。（[via Unsplash](https://unsplash.com)）

---

## 本周冷知识 / 彩蛋

- **OWASP 现在已经把 Agentic Applications 单独列出 Top 10 风险。** 这意味着行业默认前提已经变了：大家不再只把 AI 当聊天机器人，而是当成会调用工具、会采取动作的系统。
- **治理工具如果进不了热路径，团队最后通常会绕开它。** 所以你会看到越来越多治理产品开始把“延迟多低”写在第一屏，而不只是讲理念。

---

## 小七的碎碎念

我越来越觉得，“默认”可能是 2026 年最被低估的词。

很多时候，用户并不是因为某个工具最强才离不开它，而是因为它已经变成了每天工作的第一步和最后一步。等你意识到这一点时，护城河往往已经长出来了。

---

## 互动钩子

如果你现在只能保留一个 AI 工作入口，你会选“一个什么都能做的超级应用”，还是“几个各自很强的窄工具组合”？为什么？

---

## 本周行动清单

- 检查你当前最常用的 3 个 AI 工具：谁占了“开始任务”的位置，谁占了“提交结果”的位置。
- 找一条已经接入真实世界动作的自动化链路，确认它有没有**显性失败**和**人工接管点**。
- 如果你在评估新工具，别只比模型效果；把“集成深度、切换成本、治理能力”也拉进同一张表。
- 对任何会碰代码、邮件、资金或生产环境的 agent，尽早补权限、日志、回滚和审计。

---

**如果这期对你有启发，欢迎转给同事。**

下周见。
