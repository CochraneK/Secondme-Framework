# SecondMe Capture & Delta｜把一段真实经历变成可追溯增量

> 用于新的一次聊天、生活事件、他人的反馈或旧模型纠错。**只有用户明确希望归档，或早已授权此类持续记录时才准备存储操作。**

请基于我本轮**实际提供**的材料，判断是否需要将它纳入我的私人 SecondMe；如果我只想聊天，先正常回应，不主动把每句话记进模型。

按照最小事实链处理：

1. 复述最关键的原话或经历；逐句判断 speaker、subject 和 quoted speaker。资料来自转述时不可写成独立核实事实。对未确认别名保持分离。
2. 标注 event_time / recorded_at / interpreted_at（未知就 UNKNOWN）、来源指针和隐私级别。
3. 将 SELF_REPORTED / OBSERVED / EXTERNAL / ASSISTANT_INFERENCE / UNKNOWN 分开；不把 AI 的总结冒充我的原话。
4. 与**你实际能够读取**的旧证据和结论对照，给出 NO_MODEL_CHANGE、PARAMETER_UPDATE、MODEL_REVISION 或 RETRACTION 的最小变更；不必强迫从一次小事中发现人格变化。
5. 每个新增或修改的结论要有：claim ID、证据指针、竞争解释、反例或适用边界、置信程度及修订原因。
6. 如发现错人、错时间、错引号，请先审查所有依赖它的旧推断，并撤回污染链；**事实纠错优先于理论优化**。
7. 只在我选择的私人目的地写入；没有工具时，给出最少量可复制的 Markdown 和建议路径；成功写入后才能报告 commit / 文件链接。
8. 最后用不超过三句话告诉我：新增了什么、没有改什么、需要我处理的唯一下一步（若无就不强制安排）。

不得将重要第三方对话原文、完整身份映射或其他敏感输入复制到公开 Framework。不得自动把兴趣、洞察、提醒转化为待办。

参照：[连续模型](../framework/continuous_model_pipeline.md) · [实体与更正](../framework/entity_attribution_and_corrections.md) · [证据模板](../templates/EVIDENCE_CARD_TEMPLATE.md)。
