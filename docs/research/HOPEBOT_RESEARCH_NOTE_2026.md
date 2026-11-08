# HopeBot 参考审查｜如何借鉴对话式澄清，而不变成临床测评系统

> 2026-11-08 · 外部研究方法参考（External reference）。本文件是公开文献和公开仓库的独立评述；不包含任何真实 SecondMe 使用者的私人数据、临床访谈或匿名化现实个案。**不是 HopeBot 官方文件，也不构成对其临床有效性的认证。**

## 被审查的不同材料

- 研究与早期公开材料：[candiceguo0528/HopeBot](https://github.com/candiceguo0528/HopeBot)。其 README 记述早期 GPT-3.5 Turbo、10 个合成角色与 20 名评阅者的教学/初步评估。
- 应用代码：[candiceguo0528/HopeBot-Candice](https://github.com/candiceguo0528/HopeBot-Candice)。可以看到 Streamlit + LangChain/Chroma 检索、文本与语音、模型输出结构化响应。
- 2026 年论文：Guo et al., *Feasibility and user evaluation of HopeBot: An LLM-powered conversational chatbot for depression screening*, PLOS Digital Health, published 2026-06-25. DOI: [10.1371/journal.pdig.0001446](https://doi.org/10.1371/journal.pdig.0001446)。该正式研究使用 GPT-4o，132 名参与者比较自填 PHQ-9 与聊天式 PHQ-9，两者 ICC 约 0.92，中位绝对分差 1；但 28% 的个体落到相邻的不同严重度等级。

**重要：**早期仓库 README 的 20 人评阅与论文的 132 名参与者不是同一个样本，也不能由此认定仓库中的每个代码文件都等于发表研究使用的冻结部署版本。该研究验证的是**施测形式的一致性**，没有以临床访谈作为诊断金标准；不能推出临床诊断准确率或对长期人格建模的效度。

## 可以迁移的方法：Conversation as interface, evidence as contract

1. **先自然沟通**：让使用者先讲与自己相关的生活内容；只有本人希望时才进入结构化采集。不能强制在 15/20 轮之后切换心理问卷。
2. **模糊回答澄清**：在归属、时间、频率、行为与主观感受未确定时，用一个中性的问题澄清，而不是根据话术反向塑造答案。
3. **结构化结果单独验证**：大模型可以提出候选解析；事实卡和可计算字段应由独立校验检查类型、来源、缺失和矛盾。模型自然语言不等于审核通过的结构化事实。
4. **真实知识 RAG 与私人证据 RAG 分离**：外部文献、临床科普、通用方法可以支撑解释背景，但不能写成使用者自己的经历或“已证实的个人价值观”。对私人索引实行权限和来源隔离。
5. **同时保留文本/语音选择**：语音帮助某些人开口，但也会带来识别错误、成本、隐私与延迟。论文中约半数偏好文字；SecondMe 不应默认语音优于打字。
6. **采用可评估的流程**：数据来源忠实度、说话者归属准确率、漏报率、误报率、用户更正是否传播、本人是否觉得被理解、实际完成时间和隐私风险，分别评估。

## 不能照搬以及具体需要审计的部分

- **不得强制 PHQ-9**：SecondMe 是个人认知和证据系统，不是自动心理咨询师。若未来加入任何临床量表，须独立审核量表许可、标准化内容、知情同意、适用人群、风险应对与研究伦理，不能把框架当医疗器械。
- **拒答 ≠ 零分**：公开的 `HopeBot-Candice/app0.py` 提示词包含“跳过的 PHQ-9 题目按 A/0 分记录并附 note”。作为软件设计示例，它提示缺失值与实际零分必须分开。不能据此断定论文研究数据存在同样错误，论文报告其分析样本没有项目级缺失。
- **不能自称临床治疗师**：公开代码有此类角色设定，和第二阶段提醒“虚拟助手非医生”的文字并存。SecondMe 不应让 AI 冒充有执照的临床人员。
- **结构化计算应独立于生成**：论文描述后端确定性合计；公开代码包含对模型生成的 JSON 分类/分数进行解析并累加的实现。这两者可能对应不同迭代阶段，不能只凭仓库复现论文结论。未来任何可计算测量须有独立的确定性映射、原始输入核对、缺失规则、单元测试和异常路径。
- **“关怀”不能变成算法诱导**：过多澄清可能诱发过度思考并改变使用者本来的叙述；论文亦收到了此类用户反馈。SecondMe 要保留“我不知道/不想回答/只想聊天”的合法状态。
- **RAG 不能自动保证安全**：引用检索来源不代表来源内容可靠或适合当前个人；需要版本、出处、相关性和用户可见的证据边界。
- **不照搬语料与代码**：不复制该项目的训练对话、心理资料、真实参加者反馈或第三方文本进入 SecondMe-Framework。借鉴流程并另写通用、虚构的示范。

## SecondMe 的可执行结论

把这种方法提炼为可选的 **Consentful Conversational Structuring**：`chat → clarify (if genuinely necessary) → candidate extraction → validation → optional private save → model delta`。

详细通用方法见 [framework/consentful_conversational_structuring.md](../../framework/consentful_conversational_structuring.md)，可复制的提问方式见 [prompts/clarify-before-claim.md](../../prompts/clarify-before-claim.md)。

建议以完全虚构语料进行三组对照测试：(A) 直接归档、(B) 最多一次澄清、(C) 固定问题表。比较归属错误、准确来源、漏填比例、用户中断与过度干预。**这是待实施的测试计划，不是已得到的效果。**
