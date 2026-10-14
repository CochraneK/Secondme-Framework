# 语义互操作边界｜参考 AI-Persona Human Ontology v2

> 通用方法参考，不复制 AI-Persona 源代码和规范；以其官方版本为准：
> [Human Ontology v2](https://github.com/CochraneK/AI-persona/blob/main/ontology/human_ontology.v2.json) · [Consumer Contract](https://github.com/CochraneK/AI-persona/blob/main/ontology/CONSUMER_CONTRACT.md) · [Claims](https://github.com/CochraneK/AI-persona/blob/main/evaluation/CLAIMS.md)

## 可以复用什么

AI-Persona 的一个重要贡献是将人物知识分清 **entity / quality-disposition / role / relation / process-event / state**，并提供版本化语义契约、局部 MECE、类型化关系、字段级 provenance 以及 `observed / inferred / generated` 等不同来源类别。

在 SecondMe 中的实际价值是防止：
- 某次关系互动被强行写成全球稳定人格；
- 某个角色、职业、健康状态成为人的唯一身份；
- 生成、猜测、真实观察和明确选择互相冒充；
- 说话者归属错误、事件时间与后来回忆时间混淆；
- 数据库为了补齐字段从原始文本中编造事实。

## 不要做什么

- 不把 AI-Persona 的 18 个 namespace 强行变成所有人必填的 18 栏报告；
- 不将 SecondMe 的 12 维“探索地图”误称为和 AI-Persona v2 一一对应、唯一同义的本体；
- 不从合成人物的 archetype、诊断、故事弧线或概率先验推导真实用户的心理机制；
- 不把 `PersonaKernel` JSON 当作一个人完整的故事；
- 不因为别人采用了特殊的个人概念，就新增正式 canonical ontology 字段；
- 不把机器结构/一致性通过宣称为真人科学心理测量有效。

## 选择性映射

`person note → evidence wrapper → optional semantic projection → consumer`

对应不清时保留 `partial_mapping / unmapped / review_needed`。映射表仅在用户明确需要跨工具、问卷或研究系统互操作时启用。原本的个性化 Markdown 叙事始终保持独立权威。

**One canonical home 是概念存储规则，不是“人的意义只能属于一个格子”。** 连续、模糊、多值、关系、时间变化等概念无需全局 MECE。

## 应用示例（完全虚构）

童话人物“纸鹤”在画展里拒绝了帮助一位朋友。这是一个有时间的**事件/关系观察**，并不能证明纸鹤是“冷漠型人”。可能与任务负荷、个人边界或彼此误会有关。不同人对同一事件的解释可以同时留存，直到有足够资料区分。

## 科学与工程状态

AI-Persona 官方 v2 的工程契约与机器能力检查，不自动证明任何使用者的个人分析可信、科学或通用。关于模型能否改善实际探索和长期报告，须另行做隐私合规、用户确认与下游实测。

> 复用技术上的清晰，保护真人表达上的自由。
