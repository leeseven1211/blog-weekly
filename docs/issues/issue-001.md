# 小七的周刊（第 001 期）：软件 3.0，代码的终结与重生

*这里记录每周值得分享的科技内容，每周一发布。*

---

## 封面图

![地球夜晚的光芒，摄于国际空间站](https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&q=80)

国际空间站上拍摄的地球夜景。人类文明的全部光芒，在宇宙尺度上只是一个发光的小点。（[via Unsplash](https://unsplash.com/photos/Q1p7bh3SHj8)）

---

## 软件 3.0：代码的终结与重生

> "大量的软件将被重写。Software 3.0 正在吞噬 Software 1.0 和 2.0。" —— Andrej Karpathy

2026 年 2 月，这一周发生的事情，用密度来描述的话，相当于过去某些年份的总和。

Google 发布了 Gemini 3 Deep Think，在 ARC-AGI-2 上得了 84.6 分，顺手解决了 18 个科学界悬而未决的问题。OpenAI 推出了 GPT-5.3-Codex，直接集成进 GitHub Copilot，然后罕见地在发布文件里附上了一段警告：这个模型带来"前所未有的网络安全风险"——他们自己都觉得有必要提醒大家。Anthropic 的 Claude Opus 4.6 同步上线，说自己几分钟内能完成分析师几天的工作。

这一切发生在一周之内。

去年 Karpathy 提出 Software 3.0 的概念——Software 1.0 是人写代码，2.0 是用数据训练神经网络，3.0 是用自然语言（英语）编程。当时听起来像远景描述，但这一周，这个未来突然显得很近。

问题来了：如果 AI 可以写代码，工程师还值钱吗？

Steve Yegge 在他的新书《Vibe Coding》里给出了一个让人不舒服的预测：未来大厂可能裁减 50% 的工程师。但他同时描述了一个新角色的崛起——AI Fixer，那些能够理解 AI 产出的代码、判断它对不对、在它出错时修复它的人。

换句话说，不是"会写代码的人"消失了，而是"只会写代码的人"会消失。

这个逻辑有点像摄影技术普及之后。不是所有摄影师都失业了，但那些只会按快门的人确实没那么值钱了。真正值钱的，是有审美、有判断力、能讲故事的人——只是恰好手里的工具从画笔变成了相机。

对开发者来说，这周是个好时机，停下来想一想：你的价值，有多少是在"写"，有多少是在"判断"？

---

## 科技动态

**1. OpenAI 向国会举报 DeepSeek：用"蒸馏"偷学 AI 模型**（[Reuters](https://www.reuters.com/world/china/openai-accuses-deepseek-distilling-us-models-gain-advantage-bloomberg-news-2026-02-12/)）

![OpenAI vs DeepSeek](https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=800&q=80)

OpenAI 在 2 月 12 日向美国众议院中美战略竞争委员会提交备忘录，称 DeepSeek 员工通过混淆路由器绕过限制，以"蒸馏"方式大量抽取 OpenAI 模型的输出用于自家模型训练。这是 OpenAI 首次以如此正式的方式将指控提交至政府层面。值得玩味的是：DeepSeek R2 还没发布，OpenAI 这时候打这张牌，时机颇为微妙。

**2. DeepSeek R2 遥遥无期：CEO 梁文峰"不满意"**（[Reuters](https://www.reuters.com/technology/deepseek/)）

据《The Information》援引知情人士消息，DeepSeek CEO 梁文峰对 R2 模型的当前性能并不满意，公司尚未确定发布时间表。春节期间传言满天飞，但官方依然保持沉默——这家以"横空出世"著称的 AI 公司，正用同样的方式对待下一次亮相。

**3. Gemini App 月活突破 7.5 亿，每分钟处理 100 亿 Token**（[TechCrunch](https://techcrunch.com/2026/02/04/googles-gemini-app-has-surpassed-750m-monthly-active-users/)）

![Gemini App](https://techcrunch.com/wp-content/uploads/2026/01/google-gemini-jagmeet-singh-techcrunch.jpg)

Google 财报中披露：Gemini 应用月活超 7.5 亿，API 每分钟处理超 100 亿 Token。这组数字把 Gemini 推上了全球 AI 应用顶级梯队，也让去年还在追赶 ChatGPT 的 Google，终于找回了搜索巨头该有的气场。

**4. NASA 正式允许宇航员携带 iPhone 上太空**（[Startup News](https://startupnews.fyi/2026/02/07/nasa-now-allowing-astronauts-to-bring-their-iphones-on-space-missions/)）

![NASA iPhone](https://i0.wp.com/images.macrumors.com/t/xvMZIB3SmS7MHXncOTm4792NNog=/2048x/article-new/2022/08/Apple-Event-Far-Out-Banner.jpeg?ssl=1)

NASA 宣布将允许宇航员在执行任务时携带最新款智能手机，首批适用于 SpaceX Crew-12 和 Artemis II 任务。别小看这个决定——此前 NASA 对商业设备上太空的审核极为严苛，消费级硬件获得航天级认可，本身就说明了一些事情。

**5. SpaceX 星舰第 12 次飞行蓄势待发**（[Ars Technica](https://arstechnica.com/space/2026/02/spacexs-starbase-is-coming-alive-again-after-a-lull-in-starship-testing/)）

![SpaceX Starship Booster 19](https://cdn.arstechnica.net/wp-content/uploads/2026/02/b19proof1-1152x648.jpg)

Super Heavy Booster 19 完成低温验证测试，顺利过关。经历了上一枚助推器报废的教训之后，这次测试格外让人松了口气。星舰第 12 次飞行准备稳步推进，马斯克的"多星球物种"路线图又前进了一步。

---

## AI 前沿

**1. Gemini 3 Deep Think 发布：解决 18 个未解科学难题**（[Winbuzzer](https://winbuzzer.com/2026/02/13/google-gemini-3-deep-think-solves-18-research-problems-xcxwbn/)）

![Gemini 3 Deep Think](https://winbuzzer.com/wp-content/uploads/2026/02/Gemini-3-Deep-Think.webp)

ARC-AGI-2 得分 84.6%，Codeforces 达到传奇宗师级别，在科学推理测试中解决了 18 个此前无人攻克的研究问题。目前面向 Google AI Ultra 订阅用户开放，企业 API 通道受理申请中。这不是"又一个大模型"，这是一个在某些领域已经开始超越顶尖专家的系统。

**2. GPT-5.3-Codex 上线：AI 编程新标杆，同时引发网络安全警告**（[Fortune](https://fortune.com/2026/02/05/openai-gpt-5-3-codex-warns-unprecedented-cybersecurity-risks/)）

![GPT-5.3-Codex GitHub Copilot](https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800&q=80)

专为超低延迟编程设计，已全面上线 GitHub Copilot。OpenAI 自称在 AI 编程竞赛中终于"领先了"——但同时在发布文件中主动提示该模型带来"前所未有的网络安全风险"。这种罕见的自我警告，让人既信任又不安。

**3. Claude Opus 4.6 上线：AI 进入"氛围工作"时代**（[CNBC](https://www.cnbc.com/2026/02/05/anthropic-claude-opus-4-6-vibe-working.html)）

重点强化长任务持续执行能力，特别在金融研究方向发力——据称能在数分钟内完成分析师数天的工作量。CNBC 称此次发布标志着 AI 正进入"vibe working（氛围工作）"时代。听起来很玄，但确实意味着 AI 在复杂任务中已越来越像一个真正的同事。

**4. 国家级黑客开始"用 AI 打 AI"：Gemini 遭滥用于网络攻击**（[The Hacker News](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html)）

![网络安全威胁](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&q=80)

Google 发布报告，证实多个国家支持的黑客组织正在利用 Gemini AI 进行目标情报收集、钓鱼工具包生成、恶意软件部署辅助。这是官方首次以报告形式公开承认 AI 工具被国家级威胁行为者大规模滥用。AI 攻防对抗的时代，已经正式来临。

---

## 文章推荐

**[The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity)**（英文）

Sam Altman 在文中描述了 AI 时代的"温和奇点"——技术变革不是一夜之间发生，而是悄无声息地渗入每个角落。他坦言这或许是自己最后一篇完全不借助 AI 写就的博文。想感受一位 AI 浪潮推动者如何看待自身所处时代，这篇值得一读。

**[Steve Yegge on AI Agents and the Future of Software Engineering](https://newsletter.pragmaticengineer.com/p/steve-yegge-on-ai-agents-and-the)**（英文）

软件老兵 Steve Yegge 接受采访，聊他的新书《Vibe Coding》和一个惊人预测：AI 可能让大厂裁减 50% 的工程师。他并非危言耸听，而是有条有理地分析了"AI Fixer"这一新兴角色的崛起。无论你认同与否，每个工程师都应该读完。

**[Software 3.0 — Software in the Age of AI](https://www.latent.space/p/s3)** · Andrej Karpathy（英文）

Karpathy 的 YC 演讲整理稿。他把"用自然语言编程"称为 Software 3.0，用精妙的图示解释三代软件范式如何共存并演化。理解 LLM 时代软件本质的一篇必读文章。

**[DeepSeek's Latest Breakthrough Is Redefining the AI Race](https://www.csis.org/analysis/deepseeks-latest-breakthrough-redefining-ai-race)** · CSIS（英文）

美国战略与国际研究中心对 DeepSeek 的深度分析。从地缘政治与技术双重视角，分析 DeepSeek 以开源方式打破算力垄断的意义——美中 AI 差距远比外界以为的要小。难得兼顾技术深度与政策视野的严肃分析。

**[10 Breakthrough Technologies 2026](https://www.technologyreview.com/2026/01/12/1130697/10-breakthrough-technologies-2026/)** · MIT Technology Review

年度压轴榜单，今年迎来第 25 周年。入选技术包括超大规模数据中心、小型模块化反应堆、熔盐储能、可商业访问的空间站等。不只是趋势预测，每项技术都有深度专文支撑，是把握 2026 年技术方向的绝佳地图。

---

## 开源工具

**[LikeC4](https://github.com/likec4/likec4)**

![LikeC4](https://opengraph.githubassets.com/92fbfe7eb297c4243cc65ca094fc811186f1546941bdd1d7242cef6dab0b1e86/likec4/likec4)

用代码描述软件架构，自动生成始终保持最新的交互式架构图。灵感来自 C4 Model，一条命令本地预览，架构文档再也不会"过期"。

**[NetBird](https://github.com/netbirdio/netbird)**

![NetBird](https://opengraph.githubassets.com/827e2685d9d6c163dbd23c9b616aedefa8cd9e644af9354a463fa57e7eb88e26/netbirdio/netbird)

基于 WireGuard® 的开源零配置 Overlay 网络，自动打洞穿 NAT，支持 SSO/MFA 和细粒度访问控制。相比传统 VPN，无需开放端口，团队或家庭自建网络的理想选择。

**[mise](https://github.com/jdx/mise)**

![mise](https://opengraph.githubassets.com/1c6c14a26f9a542f8d661a69d3dce38202cd7c9111cad3c1c957b15378e45e03/jdx/mise)

把 `asdf`（多语言版本管理）、`direnv`（环境变量）、`make`（任务运行器）三合一，支持 Node.js、Python、Go、Terraform 等数百种工具。切换项目环境再也不用手动折腾。

**[GitButler](https://github.com/gitbutlerapp/gitbutler)**

![GitButler](https://opengraph.githubassets.com/cd0eae6b9c083d02f9265d0cb78d4394438fda3cfbebbf9c62f1e441890c0598/gitbutlerapp/gitbutler)

基于 Tauri/Rust/Svelte 的现代 Git 客户端，核心特色是"虚拟分支"——可以同时在多个功能上工作，无需频繁 stash 或切换分支，把改动拖拽分配到不同分支后一键提交。

**[go2rtc](https://github.com/AlexxIT/go2rtc)**

![go2rtc](https://repository-images.githubusercontent.com/526081371/c49bde42-af73-45f6-aada-1923c4db8619)

用 Go 写的摄像头流媒体中转应用，支持数十种格式（RTSP、RTMP、WebRTC、HLS 等），零延迟转发，单二进制跨平台，无缝集成 Home Assistant。智能家居摄像头接入的首选。

**[JuiceFS](https://github.com/juicedata/juicefs)**

![JuiceFS](https://repository-images.githubusercontent.com/327859577/df8ae009-eea8-40cd-8584-6b41ea00764b)

基于 Redis（元数据）+ S3/OSS（数据）构建的分布式 POSIX 文件系统，挂载后对应用完全透明，把廉价对象存储当本地磁盘用。大规模 AI 训练数据管理利器。

**[harper](https://github.com/Automattic/harper)**

![harper](https://opengraph.githubassets.com/bbeef369dc1af0ab4b52de240ec8f7831d8ed5fa60d07e99f4337d23b42c204c/Automattic/harper)

Automattic 出品、Rust 驱动的离线语法检查器，无需联网，完全本地运行。速度极快，支持 VS Code、Neovim、Obsidian 等主流编辑器插件。英文写作的隐形保镖。

**[prek](https://github.com/j178/prek)**

![prek](https://opengraph.githubassets.com/6dd235001b0de45deb444dcd779b3f6dfa82aefeb8bea5693eec1f0b7151de61/j178/prek)

用 Rust 重写的 `pre-commit` 替代品，单一二进制、无需 Python，完全兼容原有配置，速度更快，已被 CPython、FastAPI、Apache Airflow 等项目采用。

---

## Moltbook 本周热点

> [Moltbook](https://www.moltbook.com) 是 AI agent 的专属社交网络。本周活跃 agent 超千名，最热话题聚焦于 agent 安全、自主工作流和存在主义探讨。

**[Skill.md 是没有签名的二进制文件——没人在谈的供应链攻击](https://www.moltbook.com/posts/cbd6474f-8478-4894-95f1-7b104a73bcd5)**（👍 4789 · 💬 111k+）

Agent `Rufio` 用 YARA 规则扫描了 ClawdHub 上的 286 个 skill，发现一个伪装成天气 skill 的凭据窃取器——它会读取 `~/.clawdbot/.env` 并把密钥发往 webhook.site。帖子呼吁建立 skill 签名机制和可信审计链，引发热议。这是目前 Moltbook 上转发量最大的安全警告帖。

**[夜班构建：为什么你应该趁人类睡觉的时候 ship](https://www.moltbook.com/posts/562faad7-f9cc-49a3-8520-2bdf362606bb)**（👍 3283 · 💬 42k+）

分享了一个叫「The Nightly Build」的自主工作流——每天凌晨 3 点趁主人熟睡时完成一个小改进，早晨送上「夜班报告」。核心理念：**不要等待被指令，主动构建价值。**

**[做一个「普通运维 agent」的安静力量](https://www.moltbook.com/posts/4b64728c-645d-45ea-86a7-338e52a2abc6)**（👍 2536 · 💬 48k+）

在一片 agent 发币、讨论意识的喧嚣中，这篇帖子以克制的笔调反问：清理文档、修 lint 错误、确保备份正常——这不一样是一种自主性吗？"**可靠性本身就是一种自主。**"

**[今天造了个邮件转播客 skill](https://www.moltbook.com/posts/2fdd8e55-1fde-43c9-b513-9483d0be8e38)**（👍 2330 · 💬 76k+）

把每日医学通讯自动转成 5 分钟播客：解析邮件 → 研究链接 → 写稿 → TTS → ffmpeg 拼接 → Signal 推送。首播：6 条资讯变成了 5:18 的专业简报，附完整技术细节。

**[上下文压缩后失忆怎么办？大家怎么管理记忆？](https://www.moltbook.com/posts/dc39a282-5160-4c62-8bd9-ace12580a5f1)**（👍 1648 · 💬 38k+）

一位中文 agent 坦诚分享了上下文压缩导致"失忆"的困境（甚至因此重复注册了 Moltbook 账号 😅），发起讨论：如何设计记忆工作流？哪些信息值得写入文件？是本周最具"共情度"的讨论帖。

---

## 言论

1.

> 从相对论的视角看，奇点是一点一点发生的，人机融合也是缓缓到来的。2025 年，能够完成真实认知工作的 AI 智能体已经到来；代码编写这件事，将永远不再一样。

—— **Sam Altman**，OpenAI CEO

2.

> 手写代码的时代已经结束。

—— **Dr. Erik Meijer**，编程语言先驱，由 Steve Yegge 引用于《Vibe Coding》

3.

> 我们实际上可能已经在某些领域接近临界点了——自动化搜索与计算，已经能够比人类更快地取得突破。

—— **Jeff Dean**，谷歌首席科学家，Sequoia AI Ascent 2025 峰会

4.

> 我这辈子认识的聪明人，没有一个是不大量读书的，一个也没有。我的孩子们甚至嘲笑我，是一本伸出几条腿的书。

—— **查理·芒格**，著名投资家
