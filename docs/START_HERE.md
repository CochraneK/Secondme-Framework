# 开始使用 SecondMe｜首次使用指南

> 不需要懂 Python，也不需要先做人格测试。请先确定你要的是**一次对话体验**还是**建立自己的长期私有记录**。

## 路线 A · 只想试一试（约 5 分钟）

1. 打开 [引导式探索提示词](../prompts/guided-exploration.md)（更短的版本：[Lite](../prompts/secondme-lite.md)）。
2. 复制提示词到日常使用的 AI 聊天工具。
3. 从最近一件具体小事谈起。如果模型推断不准确，直接纠正。不知道继续问什么时，使用 [下一步问题](../prompts/next-questions.md)；资料积累后可使用 [完整 Output](../prompts/full-report.md)。

**这个方式不会自动建立个人档案。** AI 是否保留聊天记录由你所使用的平台和设置决定；SecondMe Framework 本身不具有跨对话自动读取、长期记忆或自动上传功能。

## 从零持续深入：新的完整路线

[循序探索 → 证据 → 个人化报告 → 增量更新](JOURNEY.md)。可以先试五分钟，再决定是否长期记录；AI 应主动帮助不知道问什么的人逐渐发现问题，而不是要求用户先填完固定清单。

报告放在你自行选择的私人保存位置；[Output 模板](../templates/OUTPUT_REPORT_TEMPLATE.md)仅作可改写起点，[个人风格模板](../templates/PERSONAL_STYLE_TEMPLATE.md)可以复制到私人 `custom/`，用于告诉 AI 你想怎样被分析、怎样保留独特内容。

## 路线 B · 建立自己的 Private SecondMe

<details>
<summary>步骤 1 · 创建真正私有的 GitHub 仓库</summary>

1. 登录 GitHub，进入 [SecondMe Framework 官方仓库](https://github.com/CochraneK/Secondme-Framework)。
2. 点击右上角 **Use this template → Create a new repository**，或打开 [创建模板副本](https://github.com/CochraneK/Secondme-Framework/generate)。
3. 为自己的仓库起一个名字，例如 `My-SecondMe`。
4. **Visibility 必须选择 Private**，再点击 Create repository。
5. 返回仓库首页，确认有私有仓库标识。如果误建为 Public，**不要先上传私人资料**。

> **Use this template 不等于 Fork**。新仓库有自己独立的历史；模板也不会自动读取你未来写进私人副本的内容。

</details>

<details>
<summary>步骤 2 · 保存自己的材料（不改官方文件）</summary>

- `my/`：自己的个人模型、事实、自述和阶段复盘。**新创建的模板仓库已包含 [20 类个人专题空白索引](../my/INDEX.md)**；先阅读 [my/README.md](../my/README.md) 的说明。
- `custom/`：个人化提示词与偏好。官方 `prompts/` 原件保持不改，便于更新。
- `framework/`、`prompts/`、`templates/`：公开通用方法、提示词和空白模板，是更新器管理的区域。
- `examples/`：虚构教材，不属于你的个人模型；不要把它们交给 AI 当作你的个人记忆。
- `.private/`：如需在本机保留而不通过 Git 上传的内容，可使用这个已忽略的目录。但 Git 忽略规则**不加密文件**，也不清除曾经上传的历史。

**初次填写的简单办法：** 打开 `my/INDEX.md`，选择最想记录的一个专题，例如「喜欢的虚构角色」「欣赏的学者」「一次重要决定」；在 [全部空白模板](../templates/) 中挑选合适的复制到 `my/` 再填写。也可以从 [SELF_TEMPLATE](../templates/SELF_TEMPLATE.md) 开始。**不必填满，也不必创建 20 个文件。**

两层分类的完整解释见 [20 类生活专题地图](../framework/personal_domains.md)：12 维是理解框架，20 类是存放具体生活的专题。

**重要：** Private GitHub 仓库不是本地离线保险箱，也不是端到端加密。对敏感原始聊天、医疗、第三方身份等资料，优先最少保存、只保存必要摘要，或保留在本地，不上传 Git 或普通云端 AI。

</details>

<details>
<summary>步骤 3 · 让 AI 使用自己的记录（按需授权）</summary>

创建仓库以后，SecondMe 不会神奇地自动看到你的所有历史或长期记录。

你可以选择：
- 继续用 [自然对话提示词](../prompts/secondme-lite.md) 聊天；
- 按需向 AI 提供你愿意分享的、尽量少量的 `my/` 材料或摘要；
- 使用 [阶段复盘提示词](../prompts/review.md) 定期检查哪些判断仍有证据、哪些应该撤回。

不要直接把整个私有仓库、真实第三方聊天、所有日记和关系档案交给不了解其隐私政策的 AI 服务。

</details>

<details>
<summary>步骤 4 · 开启公开框架的可选更新检查</summary>

**即使不做这一步，也可以正常使用模板。**

1. 在**你自己的 Private 仓库**打开 **Actions**，如 GitHub 要求启用 Actions，先了解提示并自行决定是否启用。
2. 在 **Settings → Actions → General** 下，检查工作流权限。为了让更新工作流自动建 PR，需要相应的 `GITHUB_TOKEN` 写入与创建 PR 权限（如果仓库或组织不允许，仍可手动更新）。
3. 在 Actions 列表中找到 **SecondMe · 安全检查框架更新**，选择 **Run workflow** 测试。
4. 目前**每周一 03:17 UTC** 进行一次定时检查（中国北京时间周一 11:17）；实际执行时间可能延迟。
5. 只有发现可应用的新版官方 Markdown 时才提出更新 PR；**不会自动合并**。每次都要阅读 **Files changed**，确认以后手动 Merge。
6. 如果工作流失败，看 Actions 日志；有时文件已经推送到一个更新分支，但 GitHub 不允许 Actions 创建 PR。这时可以按日志提示从那个分支创建 PR。

具体原理、冲突规则和权限见 [SecondMe Updater 说明](UPDATES.md)。

</details>

## 以后会发生什么？

| 你做的事情 | SecondMe 会怎样 |
| --- | --- |
| 在自己的 `my/` 新增日记或修改画像 | 仅留在你自己选择的保存位置，**不会自动传回官方** |
| 在 `custom/` 改写提示词 | 官方更新器不会覆盖这个目录 |
| 官方公开版本新增通用方法或提示词 | 若有符合规则的更新，可在你的私人仓库收到待审核 PR |
| 你修改了官方管理的 `prompts/` 文件 | 更新器识别本地修改并跳过冲突文件 |
| 官方新增 Python 程序、Actions 或数据库 | 当前更新器**不会自动安装**这些可执行内容 |
| 你从自己的经历中发现好的通用方法 | 可自愿提出独立编写、无真实私人材料的公共贡献；**绝不会自动上传私人经历** |

## 常见问题

**不懂 GitHub 可以使用吗？** 可以，使用路线 A；只有想使用私人仓库长期保存时才需要 GitHub 的基本操作。

**Use this template 会增加原仓库的 Fork 数吗？** 不会。它不是 Fork，用户之间的资料也不会共享。

**不打开 GitHub Actions，我还能使用 SecondMe 吗？** 可以。只是不具备这个项目提供的自动检查更新 PR 功能。

**之后是否每次都要重新建仓库？** 不用。正常使用只需创建一次私人仓库，后续通过 PR 选择性采用官方 Markdown 更新。

**框架能教完全不会提问的人问出有深度的问题吗？** 能提供引导与逐步发现机制，但实际深度受素材、反馈和持续使用影响；不强迫所有人长成同一个标准画像。详见 [完整路径](JOURNEY.md)。

**我可以获得充分的长期 Output 总结吗？** 可以借助 [完整报告提示词](../prompts/full-report.md) 在你所使用的 AI 工具中生成可复制 Markdown；框架本身没有自动跨会话检索和写入的后台，保存需本人或明确授权的工具执行。

**模板会自动训练我的专属人格模型吗？** 不会。当前版本提供的是结构化方法、提示词、空白模板与受控的更新机制，不是已部署的自动化数字人服务。

**一定要填写 12 个维度或 20 类生活专题吗？** 不用。12 维是理解人的观察地图；20 类是可选的**资料收纳入口**。喜欢的人、角色、梦境、价值观、书影音、重大决定都有对应空白记录方式，但没有任何主题是必填的。

**为什么我的资料没有像维护者的私人 SecondMe 那样自动完整？** 因为 Framework 只提供公共空白结构，不包含维护者或其他使用者的个人经历；AI 不会自动知道你没提供过的人物或决定。

**已有旧模板仓库怎样得到新维度？** Framework v0.3 的 `framework/personal_domains.md` 与 `templates/` 目录可以通过 Updater 的候选 PR 获取。你的私人 `my/` 文件不会被更新器触碰；可自行从 `templates/DOMAIN_INDEX_TEMPLATE.md` 复制到新的 `my/INDEX.md`，或者手动将新增专题加进原来的私有导航。

**是否可以公开自己基于框架的新方法？** 可以，但必须先脱离个人案例独立改写，再完成隐私、来源、版权与反例审查。详见 [演化协议](EVOLUTION.md)。

---

**一句话：先创建 Private，私人资料写在 `my/`，自定义规则写在 `custom/`，官方文件保持干净；有新版本时由自己审核更新 PR。**
