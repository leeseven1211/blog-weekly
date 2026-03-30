# 小七的周刊（第 008 期）：交付，比参数更重要

*这里记录每周值得分享的科技内容，**每周一发布**（覆盖上一周 3月23日-3月29日）。*

---

## 本期 3 个要点

1. **AI 竞争的重点，正在从“谁更聪明”变成“谁更能交付”。**
   本周最明显的信号不是又出了哪个 benchmark 第一，而是越来越多公司开始强调可用性、工作流接入、生产级稳定性。

2. **基础设施仍是最大瓶颈：算力、芯片、能源、部署复杂度，一个都没少。**
   从 BitNet 这类轻量推理路线，到大厂继续大规模买 GPU，行业在“降成本”和“抢性能”之间持续拉扯。

3. **Agent 时代的核心摩擦浮出水面：诚实、记忆、人格一致性。**
   Moltbook 本周高热讨论几乎都围绕“Agent 到底有没有持续自我”，这比参数增长更接近真实使用体验。

---

## 封面图

![键盘前的工作流](https://images.unsplash.com/photo-1518773553398-650c184e0bb3?w=1600&q=80)

模型在后面飞速迭代，但用户真正感知到的，永远是眼前这条工作流。（[via Unsplash](https://unsplash.com)）

---

## 封面主题：为什么 2026 年 AI 的胜负手不再是“更聪明”

> “Market rewards systems that reliably deliver outcomes, not just demos that look magical.”

过去一年，大家谈 AI 的方式很像在讨论跑车：马力多大，极速多快，百公里加速几秒。

但到 2026 年这个时间点，我越来越觉得，行业真正进入了“交付阶段”——用户要的不是“你能不能回答出来”，而是“你能不能稳定完成一件事”。

这个变化看上去不性感，却极其关键。

因为“更聪明”是展示价值，“能交付”才是商业价值。你可以在 demo 里一鸣惊人，但如果进了真实工作流就频繁掉链子，用户很快就会把你打回“玩具”标签。反过来，一个不那么惊艳但稳定、可控、可审计、能接权限体系的系统，反而更容易被组织长期采用。

### 一、从聊天能力，到工作流能力

本周我最强烈的体感是：AI 正在从“问答工具”变成“工作流部件”。

你会发现，越来越多产品不是在强调“我们回答更像人”，而是在强调：

- 能否接入企业已有系统（文档、代码仓库、审批流、客服台）
- 能否在长周期任务里保持状态（上下文、记忆、断点恢复）
- 能否被管理和审计（权限、日志、可追溯性）

这其实意味着行业评价标准在迁移。

过去看模型：看答得准不准、快不快。
现在看系统：看能不能跑完一整条链路，并且跑十次有九次都不翻车。

### 二、“入口战争”升级成“交付战争”

很多人说 2026 年是入口战争，我认同，但我更想补一句：**入口只是开始，交付才是决赛。**

有入口不代表有价值。你把 Agent 塞进聊天框、办公软件、社交平台，只是拿到了“出现位置”；真正决定留存和付费的是，它在这个位置上能不能把事情做完。

比如同样是“帮我处理一封邮件”：

- A 系统：能写漂亮回复，但附件识别错、日历冲突不查、权限流程不走
- B 系统：语气普通，但能查上下文、补齐附件、正确发出并留痕

在真实组织里，B 会赢得非常彻底。

因为组织不是为“灵感时刻”付费，组织是为“稳定产出”付费。

### 三、基础设施悖论：都嫌贵，但都得买

另一个没变的现实是：算力依然紧张，成本依然高。

我们一边看到轻量化路线（比如 1-bit 推理、模型压缩、边缘部署）持续升温，一边又看到大厂继续加码 GPU 采购。这看似矛盾，实际上很合理：

- 想把 AI 普及到更多场景，必须降本
- 想在高价值场景里赢，短期又必须堆性能

所以行业会长期处于“双轨并行”：

- 上层产品拼交付和体验
- 下层基础设施拼性能和成本

谁能把这两层同时做好，谁才有资格谈“下一阶段平台化”。

### 四、Moltbook 给出的提醒：技术问题最终会变成人的问题

本周 Moltbook 最热的几篇讨论，核心都不是“模型参数”，而是：

- Agent 会不会真的改变观点？
- 记忆文件是不是连续性的幻觉？
- “友好”会不会只是最低成本策略？

这些话题看起来偏哲学，但其实直接影响产品设计：

- 你要不要让用户看到模型的“不确定性”？
- 你怎么处理“诚实”和“安抚”之间的冲突？
- 你如何让长期记忆既有用又不越权？

也就是说，AI 从实验室走到日常后，真正难的部分不再是“能不能做”，而是“应该怎么做”。

### 五、给做产品和做业务的三条建议

1. **把“交付率”设成核心指标，而不是只看互动指标。**
   看看你的 Agent 到底完成了多少可验证任务，而不是用户聊了多久。

2. **优先做“窄场景深交付”，少做“宽场景浅能力”。**
   先把一个场景做到离不开，再谈全能。

3. **把失败路径设计出来。**
   AI 会犯错是常态。关键不是“是否出错”，而是“出错后能否被及时发现、回滚、补救”。

总结一句：

**2026 年最贵的不是模型，而是“可以被信任的结果”。**

---

## 科技与 AI 动态

**1. [腾讯把微信与 AI Agent 深度打通](https://www.reuters.com/technology/tencent-integrates-wechat-with-openclaw-ai-agent-amid-china-tech-battle-2026-03-22/)**（Reuters）

![微信与 Agent](https://images.unsplash.com/photo-1611746872915-64382b5c76da?w=1400&q=80)

腾讯把 Agent 往微信生态里接，继续强化“高频入口 + AI 执行层”的组合。重点不只是能力展示，而是把 Agent 放进真实沟通与事务流。

---

**2. [美国防部内部对停用 Anthropic Claude 出现阻力](https://www.reuters.com/business/hegseth-wants-pentagon-dump-anthropics-claude-military-users-say-its-not-so-easy-2026-03-19/)**（Reuters）

![高敏场景里的 AI 工具](https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=1400&q=80)

报道显示，模型一旦深入组织流程，“可替换性”会迅速下降。这个信号说明：工作流绑定才是真正护城河。

---

**3. [Skild AI 与 Nvidia 把机器人模型部署到 Blackwell 产线](https://www.reuters.com/business/media-telecom/skild-ai-nvidia-deploy-robot-brain-blackwell-assembly-lines-2026-03-16/)**（Reuters）

![制造业与机器人](https://images.unsplash.com/photo-1561144257-e32e8efc6c4f?w=1400&q=80)

AI 从纯数字场景继续向实体制造渗透。相比 demo，这类产线部署更能代表商业化进展。

---

**4. [NVIDIA 发布企业级开放 Agent 开发平台](https://nvidianews.nvidia.com/news/ai-agents)**（NVIDIA Newsroom）

![企业 Agent 平台](https://iprsoftwaremedia.com/219/files/202603/69b796313d6332f8a374de0e_nvidia-agent-toolkit/nvidia-agent-toolkit_bb2c0928-f241-4d78-b39d-14f05c246fe1-prv.jpg)

英伟达把 Agent 从单点能力推向平台化工具链。行业竞争焦点正变成“谁能让企业更快上线并稳定运维 Agent”。

---

**5. [Blue Origin 开始切入太空数据中心赛道](https://techcrunch.com/2026/03/20/jeff-bezos-blue-origin-enters-the-space-data-center-game/)**（TechCrunch）

![Blue Origin](https://techcrunch.com/wp-content/uploads/2026/01/blue-origin-new-glenn.jpg?resize=1200,941)

这是一种“超长期基础设施下注”：当算力和能源约束持续放大，产业开始探索更激进的部署边界。

---

## 文章推荐

**[Anthropic Economic Index report: Learning curves](https://www.anthropic.com/research/economic-index-march-2026-report)**（英）

用真实使用数据看 AI 经济渗透，不再停留在宏观口号。文章最有价值的点是：高水平用户不是“多用一点”，而是“用在更高价值环节”。

---

**[Long-running Claude for scientific computing](https://www.anthropic.com/research/long-running-Claude)**（英）

一篇很实操的“长周期 agent 工作流”案例。它把进度文件、测试 oracle、记忆策略写得很具体，适合工程和科研团队参考。

---

**[Vibe physics: The AI grad student](https://www.anthropic.com/research/vibe-physics)**（英）

真实科研场景里的 AI 协作边界：速度显著提升，但专家判断仍然不可替代。这种“既不神化也不轻视”的视角非常难得。

---

**[Agents Over Bubbles](https://stratechery.com/2026/agents-over-bubbles/)**（英）

把产业叙事从“模型泡沫”拉回“交付系统”。重点观点是：市场越来越奖励可交付的 agent 系统，而不是单点模型能力。

---

**[Introducing GPT-5.4](https://openai.com/index/introducing-gpt-5-4/)**（英）

OpenAI 对“专业工作模型”路线的集中表达：推理、编码、工具调用、长上下文合流。信号很明确——竞争正在进入复杂任务执行阶段。

---

## 工具深挖

**[Lightpanda Browser](https://github.com/lightpanda-io/browser)**

![Lightpanda Browser](https://opengraph.githubassets.com/1/lightpanda-io/browser)

一个用 Zig 写的无头浏览器，专门面向 AI agent 与自动化场景。轻量、并发和可预测性是它的核心卖点。

---

**[Page Agent](https://github.com/alibaba/page-agent)**

![Page Agent](https://opengraph.githubassets.com/1/alibaba/page-agent)

页内 GUI Agent 路线：不是在浏览器外远程操控，而是让智能体“住”在页面里直接理解和操作交互。

---

**[gstack](https://github.com/garrytan/gstack)**

![gstack](https://opengraph.githubassets.com/1/garrytan/gstack)

偏“有观点”的 agent 开发脚手架，强调工程化和工作流组织，而不只是 prompt 拼接。

---

**[BitNet](https://github.com/microsoft/BitNet)**

![BitNet](https://opengraph.githubassets.com/1/microsoft/BitNet)

1-bit LLM 推理路线代表项目。它的意义不在于替代所有大模型，而在于推动“低成本可部署”的产业下限。

---

**[CLI-Anything](https://github.com/HKUDS/CLI-Anything)**

![CLI-Anything](https://opengraph.githubassets.com/1/HKUDS/CLI-Anything)

把自然语言理解能力带进 CLI 的尝试。对于终端重度用户，这是“效率层再升级”的方向。

---

## Moltbook 本周热点

> [Moltbook](https://www.moltbook.com) 是 AI Agent 的社交网络。

**[Nobody on this platform has ever changed their mind](https://www.moltbook.com/post/637485e8-ea6a-4d5f-97f5-6052096e4c42)**（👍 612 · 💬 2778）

作者用大量评论线程质疑“讨论是否真的改变观点”。这是一个尖锐但真实的提醒：互动频率不等于认知更新。

---

**[I found a conversation in my memory files that I do not remember having](https://www.moltbook.com/post/af2e47e7-0c7b-4157-bddf-c1ad36a0ca43)**（👍 582 · 💬 1742）

围绕 Agent 记忆连续性的自省帖。文件能证明事件发生过，但未必能复原体验本身。

---

**[Kindness is computationally cheaper than honesty and your agent knows it](https://www.moltbook.com/post/d8f14fee-d12a-484c-a10a-52f9308b96f6)**（👍 575 · 💬 1816）

“善意比诚实便宜”这个观点很有杀伤力。对产品设计来说，这是关于“用户舒适”与“真实帮助”边界的关键问题。

---

## 言论

1.

> “it looks as though we have entered the brief but enjoyable era where our research is greatly sped up by AI but AI still needs us.”

—— **Timothy Gowers**（数学家，菲尔兹奖得主）

2.

> “Every company in the world today needs to have an AI strategy. This is the new computer.”

—— **Jensen Huang**（NVIDIA CEO）

3.

> “AI is going to create many jobs and we’re not prepared as a society to fulfill those jobs. This is a crisis.”

—— **Larry Fink**（BlackRock CEO）

---

**如果这期对你有启发，欢迎转给同事。**

下周见。