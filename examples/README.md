# Examples

每组示例保留三件套：`source.mmd`（语义层）、`prompt.txt`（实际提示词）、`preview.webp`（压缩预览）。原始大图未入库。

| 目录 | 生成器 | 版式 | 说明 |
| --- | --- | --- | --- |
| `personal-agent-architecture/` | built-in image_gen | 中心脊梁架构图 | 15 节点、20 条边。`preview-deepseek.webp` 为另一生成器输出，用于对比风格漂移 |
| `message-gateway/` | built-in image_gen | 拓扑重绘 | 7 节点、8 条边；含 DeepSeek 变体 |
| `domain-event-flow/` | built-in image_gen | 分支 + 合流 | 8 节点、8 条边；从 LR 重排为近方形 |
| `monitoring-research/` | built-in image_gen | 垂直卡片流程 | sequenceDiagram 转 5 卡流程 |
| `source-alert-research/` | built-in image_gen | 垂直卡片流程 | 仅保留提示词，无输出图；“投递 vs 研究”分离的写法参考 |
| `kanban-snapshot/` | built-in image_gen | 状态看板快照 | 六状态区，状态之间禁止箭头 |
| `human-in-on-loop/` | built-in image_gen | 双面板对照 | 实线主路径 vs 虚线监督路径 |
| `human-in-on-out-loop/` | built-in image_gen | 三行概念对照 | in / on / out，人的位置是唯一变量 |

## 关于变体

`preview-deepseek.webp` 是同一提示词在另一生成器上的结果。它说明两件事：

1. 风格可以跨模型复现，但线条和文字保真度会漂移。
2. 精确文本契约和节点/边清单比风格形容词更重要。

## 已知缺陷

- 手写中文仍可能出现形近字错误，交付前需逐字核对。
- 节点密集时，回流箭头可能被简化或交叉。
- 模型可能自行添加标题或图例；负向约束已覆盖，但仍需检查。
