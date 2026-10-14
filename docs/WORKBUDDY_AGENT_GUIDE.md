# SecondMe Agent 与 WorkBuddy 专家团｜安装指南

> 公开通用工具 v0.1（2026-10-14）。**项目 Agent/Skills 已提供，真实 WorkBuddy 产品端导入及市场发布尚未实测。** 专家团采用腾讯官方文档结构；不是自动记忆服务、心理诊断或持续监控进程。

## 1. 不要把所有格式混为一谈

| 层级 | 文件/位置 | 用途 |
| --- | --- | --- |
| 跨工具协作约束 | [AGENTS.md](../AGENTS.md) | 仓库通用的隐私、证据、个人化和写入权限约束 |
| 项目记忆 | [项目说明](../.codebuddy/CODEBUDDY.md) | WorkBuddy/CodeBuddy 读取工作区知识 |
| 专项代理 | [项目 Agents](../.codebuddy/agents/) | 主理人和 6 位按需召唤的审查/编辑专家 |
| 任务技能 | [项目 Skills](../.codebuddy/skills/) | 按需启用引导探索或长期 Output 的工作流 |
| 专家团安装包 | `dist/secondme-expert-team.zip`（**本地构建**） | 带 `plugin.json`、头像、团队成员和技能的 WorkBuddy ZIP |
| 私人资料 | 使用者自己控制的 Private `my/` | 生活材料、个人长期模型、完整报告；**不进入公开安装包** |
| 能力执行 | WorkBuddy/CodeBuddy 当前模型与工具权限 | 真正读写文件、调度 Agent；仓库里的 Markdown 本身不会自行执行 |

官方参考：[WorkBuddy 项目配置](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)、[CodeBuddy 子代理](https://www.workbuddy.cn/docs/cli/sub-agents)、[WorkBuddy Expert Team](https://open.workbuddy.cn/en/docs/expert-team)、[WorkBuddy Skills](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。

## 2. 方案 A：在自己电脑的 WorkBuddy 项目中使用（优先推荐）

1. 把此公开模板作为一个**新的 Private 工作区**使用（或在安全、经授权的文件夹里打开模板副本）。
2. 在 WorkBuddy/CodeBuddy 将该文件夹作为当前项目工作区；项目级 `.codebuddy/agents/*.md` 与 `.codebuddy/skills/*/SKILL.md` 按官方项目配置自动发现。
3. 可直接说：“使用 SecondMe 主理人，我不知道怎么开始认识自己，先问我一个问题。”
4. 需要深入时说：“请调用证据审查与反证专家，检查你对我的理解，最后让报告专家整理完整 Output。”
5. 文件保存到**自己私有副本**的 `my/reports/OUTPUT_FULL.md`；没有授权写入或只在网页对话中使用时，输出可复制的 Markdown，不要声称已完成保存。

**注意**：GitHub public 仓库不是个人工作区；不要在原 public 仓库提交自己的私密资料。云端 WorkBuddy、项目资料库和协作任务不是本地离线保密容器，使用前查看其隐私和共享设置。即使私有仓库也不是端到端加密。

## 3. 方案 B：安装 WorkBuddy 专家团 ZIP（仅本地构建，尚未实际导入验证）

需要 Python 3.10+。在公开仓库的根目录运行：

```bash
python scripts/package_workbuddy_team.py
```

生成 `dist/secondme-expert-team.zip`（不会读取 `my/`、`custom/`、日记或其他私人数据）。可选：

```bash
python scripts/package_workbuddy_team.py --output /tmp/secondme-team.zip
python -m unittest discover -s tests -v
```

ZIP 内有如下**已生成的内容**：

```text
.codebuddy-plugin/plugin.json    ← expertType=team，主理人和成员声明
settings.json                    ← 默认主理人
agents/*.md                     ← 7 个 Agent
skills/*/SKILL.md               ← 引导/Output 两项 Skill
avatars/*.png                   ← 纯代码生成的 512px 抽象头像
README.md
```

WorkBuddy 中通过“专家·技能·连接器 → 我的专家 → 创建专家团”选择对应上传/创建流程，或根据当时客户端的“导入/创建专家团”入口操作。**此处只提供结构与打包器，不能声称已在你的 WorkBuddy 账号安装、上架或通过平台审核。**

打包器中的作者邮箱是 `maintainer@example.com` 占位符：**正式申请上架前必须换成真实公开联系渠道并检查相关官方政策**。包内不需要、也不包含任何第三方个人数据或 API key。

## 4. 专家团怎么协作，不是“六个人轮流夸你”

```text
普通聊天  → 主理人直接自然回应（不必调度专家）
不知道问什么 → 引导专家（一次一个好问题）
新的人格结论 → 来源审查 → 反证挑战 → 当事人可纠正
跨年份变化 → 纵向专家检查 event_time 与 interpreted_at
完整报告 → 编辑专家独立组织此人专属叙事
保存/分享/导出 → 隐私专家确认边界 → 本人授权 → 实际写入并核验
```

只有运行时真正可调用独立子 Agent 时才说“专家团已协作”；不支持则退化成单 Agent 执行不同检查，并明确说明。多个专家同意也不代表关于人的判断就是事实。

**不让用户接受主理人的“心理预测”**。用户可随时说：“先不分析”“跳过这个问题”“这是错误归因”“我不需要这种格式”。

## 5. 未来怎样升级为真正持续运行的 Agent

文件提示词 + Skills + 子代理协作 = **可部署的 Agent 配置**。要长期自动做这些，还需要独立可授权的软件能力：

- 私有资料持久化与按需检索（local-first 或自选可信存储，MCP 只在授权后接入）；
- 逐条证据 ID、事件时间、说话者、旧结论依赖关系；
- 无授权时只读/无写入，重要结论写入经过本人批准；
- Output 版本与 Delta 引用，严格区分报告、原始资料和第三方引用；
- 自动调度、定期复盘**只能由用户主动启用**，不默认持续收集和上报；
- 真实用户研究与伦理/隐私评估，检验提问质量和偏差。

当前打包器**不提供**上述长期数据服务。它提供的是可复用的专业分工与工作流程。

## 6. 调试

- 检查文件：`.codebuddy/agents/` 中所有文件以 `---` YAML frontmatter 开头且名称唯一。
- 检查 ZIP：执行 `python scripts/package_workbuddy_team.py` 后用任何 ZIP 查看器查看 `.codebuddy-plugin/plugin.json`、`settings.json`、7 个 Agent、8 张 PNG。
- 若专家未出现：确认 WorkBuddy 当前为该项目工作区、平台实际加载项目配置；某些 Web/客户端配置可能不共享。官方项目级 Agent 和专家团市场是两种不同的发布入口。
- 若平台拒绝 ZIP：对照 [官方 Expert Team 规范](https://open.workbuddy.cn/en/docs/expert-team) 的类别、头像、团队字段，并确认作者信息真实；目前没有进行真人账号上架测试。
- 若 AI 声称读过隐私资料但没见到实际文件：这是错误；停止本次自动提取，核实权限与来源。
