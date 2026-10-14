# SecondMe Framework

<p align="center">
  <img src="docs/assets/hero.svg" alt="SecondMe Framework：认识自己，不把自己固定为标签" width="100%">
</p>

<p align="center">
  <strong>一个持续修正的自我理解框架。</strong>
  <br>
  从真实经历与自然对话出发，用证据而不是标签理解自己。
</p>

<p align="center">
  <a href="prompts/secondme-lite.md">即刻体验</a> ·
  <a href="#如何运作">框架总览</a> ·
  <a href="#方法与理论">维度与理论</a> ·
  <a href="PRIVACY.md">隐私原则</a>
</p>

<p align="center"><sub>Experimental v0.4 · 中文优先 · MIT License · Privacy-first</sub></p>

---

## 新版重点：不懂怎么问，也能开始

**[引导式探索（推荐新手）](prompts/guided-exploration.md)** → **[AI 帮你发现下一问](prompts/next-questions.md)** → **[生成完整 Output 报告](prompts/full-report.md)** → **[增量更新与纠错](prompts/update-output.md)**。

不要求先有心理学知识、固定人生目标或完整日记；问题随这个人的回答调整。报告允许专属章节、丰富长文、相互矛盾的解释和证据不足的留白。**可共享分析方法，不强行共享人物内容结构。**

[从零到长期报告的完整路径](docs/JOURNEY.md) · [个人化建模原则](framework/person_specific_modeling.md) · [完整 Output 协议](framework/output_reports.md)

## Agent / WorkBuddy 专家团（可选）

除了直接复制提示词，现在还提供 **[SecondMe Agent 与 WorkBuddy 专家团指南](docs/WORKBUDDY_AGENT_GUIDE.md)**：

- `AGENTS.md`：跨工具协作约定。
- [7 位项目级 Agents](.codebuddy/agents/)：1 位主理人 + 探索、证据、反证、纵向、报告、隐私 6 位按需专家。
- [两项 Skills](.codebuddy/skills/)：自适应探索和完整 Output。
- [WorkBuddy 专家团 ZIP 构建器](scripts/package_workbuddy_team.py)：`python scripts/package_workbuddy_team.py` 即可本地打包所需 `plugin.json`、Agent、Skill 与 512px 抽象头像。

**已提供代码与格式校验；并不代表专家团已自动安装在你的 WorkBuddy、通过产品端导入或完成市场上架。** 专家合作只有运行时确实调度了多个 Agent 才称为“多 Agent”；普通对话无需召唤全队。个人资料始终由使用者选择存储与授权。

## 60 秒开始

| 你的目标 | 推荐入口 |
| --- | --- |
| **从零开始，不知道该问什么** | [引导式探索提示词](prompts/guided-exploration.md)：AI 每次根据真实回答选择一个问题 |
| **已有材料，想要全量分析** | [完整 Output 报告提示词](prompts/full-report.md)，支持充分长文、优缺点、反证、纵向修订和专属章节 |
| **建立长期个人档案** | [Use this template 创建自己的 Private 仓库](https://github.com/CochraneK/Secondme-Framework/generate)，在 `my/` 保存本人资料，`custom/` 保存个性化提示词 |
| **今后获得新方法** | 在私人仓库启用可选的框架更新工作流，查看并合并更新 PR；不自动覆盖个人资料 |

**第一次使用 GitHub？请按 [中文入门指南（从零开始）](docs/START_HERE.md) 操作。** 它详细说明如何确认仓库为 Private、保存记录、启用更新及处理失败。

<sub>当前项目是方法与文件模板，尚未提供自动跨会话记忆、自动读取私人仓库或自动创建人物模型的完整运行服务。</sub>

## 为什么是 SecondMe？

我们会改变。一次测试、一段聊天或一个人格标签，都不足以概括一个真实的人。

SecondMe 希望做的，是把**生活中的真实材料**转化为**有来源、可质疑、能随着时间改变的工作模型**。

| 原则 | 这意味着什么 |
| --- | --- |
| **证据优先** | 明确区分「本人自述」「直接观察」「推断」「未知」。 |
| **动态更新** | 允许矛盾、反例和变化；旧结论可以降权、改写或退休。 |
| **主体性优先** | 心理学理论与 AI 是参考，不是替你定义人生的权威。 |
| **隐私优先** | 公开可复用的方法；个人经历与记录只存在于你选择的私有空间。 |

**它不是**临床诊断工具、正式人格测评，也不是已经接通所有历史记录的数字分身。

## 如何运作

![SecondMe 核心机制：真实材料、证据分层、12维地图、方法选择、阶段模型与修订循环](docs/assets/framework.svg)

使用时不会要求你完成所有步骤的复杂填报。可以只从一个问题开始，**按需要选择最少的方法**。

- **真实材料**：聊天、自述、经历与使用者自愿提供的观察。
- **证据协议**：保留来源；区别事件、观察、推断、外部观点和未知。
- **维度地图**：以 12 个观察维度整理信息，不形成统一人格总分。
- **方法选择**：依据具体问题选择 1–3 个有解释增益的视角。
- **阶段模型**：解释需包含适用范围、其他可能性和可推翻它的证据。
- **持续修订**：后来发生的真实经历，可以改变甚至否定此前的模型。

## 人的十二个维度

![Human Ontology 中文分类：个体基础、价值与社会、行动与经历、自我与时间](docs/assets/dimensions.svg)

**12 个维度是整理材料的分类地图，不是 12 个已验证、彼此独立的人格因子。** 可以交叉、留空，或随着理解加深而改变。详见 [Human Ontology](framework/human_ontology.md)。

### 人人都有的 20 类生活专题入口

理解一个人不能只谈人格理论。v0.3 开始，所有从 Template 新建的私人仓库也会得到**同一套完整的可选专题目录**：

| 我想记录…… | 对应专题与空白模板 |
|---|---|
| **欣赏的老师、学者、公众人物** | [人物与角色卡](templates/PEOPLE_CHARACTERS_TEMPLATE.md) |
| **最喜欢的小说、影视、游戏角色** | [人物与角色卡](templates/PEOPLE_CHARACTERS_TEMPLATE.md) |
| **价值、个人金句、喜欢什么** | [价值语句](templates/VALUES_QUOTES_TEMPLATE.md) · [偏好](templates/PREFERENCE_TEMPLATE.md) |
| **家人、朋友、亲密关系、同事** | [关系记录](templates/RELATIONSHIP_TEMPLATE.md) |
| **人生时间线、重要选择与反思** | [时间线](templates/TIMELINE_TEMPLATE.md) · [决策](templates/DECISION_TEMPLATE.md) |
| **阅读、音乐、电影、游戏、旅行** | [文化与兴趣](templates/CULTURE_MEDIA_TEMPLATE.md) · [经历](templates/EXPERIENCE_TEMPLATE.md) |
| **自己的创作、命名、故事、梦境** | [创作与命名](templates/CREATIVE_LEXICON_TEMPLATE.md) · [梦境](templates/DREAM_TEMPLATE.md) |
| **Idea、项目、普通快乐、休息** | [想法与承诺](templates/IDEAS_PROJECTS_TEMPLATE.md) · [日常生活](templates/DAILY_LIFE_TEMPLATE.md) |

**[打开 20 类生活专题地图 →](framework/personal_domains.md)** · **[打开通用专题导航模板 →](templates/DOMAIN_INDEX_TEMPLATE.md)**

这些是「生活资料的可选专题」，**不是另外 20 种人格因子**。所有人拥有相同的空白容器，但每个人收藏的人物、喜欢的角色、经历和决定均来自自己；`EMPTY` 不代表该人缺少这一面。


## 从聊天到真正可更新的个人 Output

| 想实现的目标 | 已提供的方法 |
| --- | --- |
| 我完全不知道该问什么 | [自适应发现与提问路由](framework/adaptive_discovery.md) · [引导 prompt](prompts/guided-exploration.md) |
| 我想知道有没有忽视的重要问题 | [问题发现 prompt](prompts/next-questions.md) |
| 我希望分析足够深，不止贴人格标签 | [个体优先](framework/person_specific_modeling.md) · [纵向推理与竞争解释](framework/longitudinal_reasoning.md) |
| 我想区别喜欢、需要、责任和决定 | [八种判断镜头（非量表）](framework/judgment_lenses.md) |
| 我需要可长期维护的全部 Output | [报告方法](framework/output_reports.md) · [Full Output prompt](prompts/full-report.md) · [可改模板](templates/OUTPUT_REPORT_TEMPLATE.md) |
| 我带来新经历、想纠正旧报告 | [增量更新 prompt](prompts/update-output.md) |
| 我想接入 AI-Persona 的规范 | [类型、来源和选择性本体映射](framework/semantic_interoperability.md) |

**有方法，不代表自动完成：** 当前版本不自动读取跨会话历史、不自动分析整个私人仓库、不替用户部署长驻 Agent，也不保证私人全量报告具有科学测量效度。公开仓库只提供通用方法、提示词、空模板和独立虚构示例。

## 方法与理论

面对不同问题，SecondMe 不会用某一个理论解释所有人。下面是**可选的参考池**，并不代表已部署自动打分、模型训练或完成临床效度验证。

| 分析方向 | 可参考的理论或方法 | 典型问题 |
| --- | --- | --- |
| 人格与气质 | 大五人格、HEXACO | 哪些倾向跨情境相对稳定？ |
| 认知与学习 | 元认知、认知风格、信息加工 | 怎样学习、推理和修正看法？ |
| 动机与价值 | 自我决定理论、期待—价值 | 为什么愿意做、又为何犹豫？ |
| 情绪与情境 | 情绪调节、情境反应 | 哪些情境会改变感受？ |
| 关系与互动 | 依恋理论、双人互动与边界 | 如何处理双方不同的需要？ |
| 身份与时间 | 叙事身份、自我差异、可能自我 | 我如何理解变化中的自己？ |
| 选择与行动 | 决策权衡、趋近—回避、人—环境适配 | 选择的成本、可能性和可逆性是什么？ |
| 发展与环境 | 生态系统视角、人生历程 | 环境、文化与人生阶段怎样起作用？ |

**Method Router** 先看问题、证据和时间尺度，再选择理论，并寻找竞争解释。如果证据不足，**不知道**也是合格答案。参见 [方法选择器](framework/method_router.md)。

### 证据分类

`SELF_REPORTED` 本人自述 · `EVENT` 具体事件 · `OBSERVED` 可观察材料 · `INFERRED` 候选推断 · `EXTERNAL` 外部参考 · `UNKNOWN` 未知。

它们是**来源与推断状态标签**，不是对人的评价分数。详见 [证据协议](framework/evidence_protocol.md)、[模型更新](framework/model_update.md) 与 [主体性边界](framework/agency_and_external_advisors.md)。

## 从这里开始

![SecondMe 使用路径：立即复制提示词自然对话，或创建 Private 仓库长期记录](docs/assets/quickstart.svg)

**路径 A · 五分钟体验**

1. 打开 [引导式探索提示词](prompts/guided-exploration.md)（或更简短的 [Lite](prompts/secondme-lite.md)），复制到日常使用的 AI 聊天工具。
2. 从最近一件真实的小事聊起，不用做长问卷。遇到不知道如何继续时，让 AI 使用 [下一问机制](prompts/next-questions.md)。
3. 让 AI 区分事实、解释、反例与未知；发现不准确就直接纠正。想要报告时再使用 [Full Output](prompts/full-report.md)，选择性存入 Private 仓库。

**路径 B · 建立长期私有模型**

1. 使用 [Use this template](https://github.com/CochraneK/Secondme-Framework/generate) 创建新的 **Private** 仓库。你不需要 Fork，也不需要复制任何私人历史。
2. 将 [空白模板](templates/) 复制到 `my/` 后自愿填写；个人化提示词放在 `custom/`，不要修改官方原件。私有仓库不等于本地加密，涉及健康、关系等敏感材料时应进一步最小化。
3. 用 [阶段复盘提示词](prompts/review.md) 根据新经历调整旧认识，不让 AI 擅自增加人生任务。详细点击步骤见 [第一次使用指南](docs/START_HERE.md)。

## 框架更新：不覆盖私人资料

朋友通过模板创建自己的私有 SecondMe 后，并不具备 GitHub 原生的 Fork 同步功能。因此 v0.2 加入了 **[SecondMe Updater](docs/UPDATES.md)**：

- **定期或手动检查**公开框架的新版本；
- 只选择性更新 `framework/`、`prompts/`、`templates/` 中未经用户修改的官方 Markdown；
- 遇到已修改文件就**跳过并报告冲突**，个人资料、个性化设置、示例及可执行脚本不自动同步；
- 在使用者的**私人仓库**内生成待审核 Pull Request，**不会自动合并**。

`my/` 可用于私人仓库中自愿版本管理的个人资料，`custom/` 用于定制。需要离线保留的内容可自行放进 `.private/`（已列入 Git 忽略规则）。**Private GitHub 仓库仍是云端服务，不代表端到端加密。**

> 更新器当前基线是 **v0.2.0**；这是已经提供的更新机制，不代表已有待升级的新版本。使用前需要仓库启用 GitHub Actions 及适当的 PR 权限。[查看安装与权限说明 →](docs/UPDATES.md)

## 开源框架如何持续演化？

每个人都可以在自己的私人 SecondMe 中长期探索；当发现可推广的方法时，**先在私人环境里审查、独立重写成通用内容，再经人工确认发布到公开仓库**。私人经历与 Git 历史不能自动上行。

公开方法的新版本，则通过版本指纹和可审核 PR，供每个使用者按自己的意愿更新；不会覆盖个人资料或个性化模型。

[了解方法演化与发布规范 →](docs/EVOLUTION.md) · [查看安全更新机制 →](docs/UPDATES.md)

## 项目结构

```text
SecondMe-Framework/
├── prompts/       Lite、引导探索、发现问题、全量 Output、增量更新
├── framework/     12维可选地图 + 20类专题、动态推理、个性化、Output
├── templates/     私人生活专题、风格选择与 Output 报告空白模板
├── examples/      独立虚构的教学材料（非个人记忆）
├── docs/assets/   中文 SVG 框架图及视觉素材
├── docs/        首次使用指南、更新协议与框架演化规则
├── my/           20类空白私人导航与使用说明（无真实个人数据）
├── custom/       个性化提示词的空白使用说明
├── scripts/      安全更新器与发布清单工具
├── .secondme/    官方版本清单与文件指纹
├── .github/      提议更新 PR 的可选工作流
├── tests/        防覆盖与路径安全的离线测试
├── PRIVACY.md     隐私与脱敏边界
├── CONTRIBUTING.md
└── ROADMAP.md
```

### 示例与记忆的边界

[examples/](examples/) **只用于演示方法，不是标准答案，更不是使用者的个人记忆**。浏览仓库或创建副本不会自动导入示例；但如果把整个仓库作为 AI 检索材料，示例仍可能产生叙事锚定。因此，私人使用时请将 `examples/` **排除在人物记忆、画像和蒸馏输入之外**。

### 隐私与贡献

这个仓库**不承载真实的 SecondMe 个人档案**。请勿通过公开 Issue、PR 或示例提交真实聊天、健康资料、亲密关系记录或改名后的真实案例。详见 [PRIVACY.md](PRIVACY.md) 和 [CONTRIBUTING.md](CONTRIBUTING.md)。

当前 **v0.4** 提供了 12 维本体、20 类生活专题、提示词、方法文档、空白模板、虚构教学示例，以及可选的框架版本检查与更新 PR；**尚未实现**自动跨会话记忆、数据库、可视化交互界面、正式测量或数字人运行时。后续想法见 [ROADMAP.md](ROADMAP.md)。

---

<p align="center"><strong>好的自我模型，应当允许未来的你证明今天的模型是错的。</strong></p>
<p align="center"><sub>Open methods. Private lives. A model that can change.</sub></p>
