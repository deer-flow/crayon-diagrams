# 提示词解剖：九块结构

一条能稳定出图的提示词，通常由九块组成。不是每条都必须写全，但**文本契约**和**拓扑/构图**不能省。

## 1. 生成器与输入

说明用什么模型、参考图扮演什么角色。参考图的角色不清，是风格跑偏和拓扑被篡改的头号原因。

```text
Generator: built-in image_gen
Reference: user-provided Human in/on the Loop diagram

Use case: style-transfer / infographic-diagram.
Input image is the semantic reference/edit target; preserve the exact workflow
relationships and labels but completely redesign the layout.
```

只借风格时：

```text
The reference image is STYLE ONLY: match its white background, handwritten
lettering and crayon texture. Do NOT copy its graph, nodes or labels.
```

三种参考角色，必须显式二选一：

| 写法 | 含义 |
| --- | --- |
| `Input image is the content reference` | 保留关系与文字，重排布局 |
| `STYLE ONLY. Do NOT copy its graph or labels` | 只借视觉语言 |
| `CHARACTER REFERENCES ONLY, not layouts` | 只借角色特征，不复刻画面 |

## 2. 用途与受众

一句话交代场景，模型会据此调整信息密度和字号。

```text
Use case: infographic-diagram for a Chinese technical blog, optimized for
reading on a mobile phone. Clean editorial diagram, not photorealism.
```

## 3. 画布

明确比例、像素、背景和留白。移动端优先，不要用横版塞长流程。

```text
Canvas: portrait 3:4 aspect ratio, about 1200 x 1600, pure white background
(#FFFFFF), generous margins. Two clearly separated panels stacked TOP and BOTTOM.
```

常用比例：

- `2:3`：卡片流、看板、概念对照。
- `3:4`：架构图、双面板。
- `1:1` / 近方形：紧凑拓扑。
- `5:1`：文章 hero 横幅，需单独裁切。

## 4. 风格

用同一段风格块，保证系列一致。完整版本见 `style-crayon.md`。

```text
Pure white background, hand-drawn dark graphite/crayon outlines and arrows,
pale blue crayon shaded rounded rectangles, clearly HANDWRITTEN lettering with
natural slight irregularity (not typeset). Restrained warm orange accent.
Clean, friendly editorial sketch, visible wax-pencil grain inside shapes,
no paper tint, no shadows, no decorations, no watermark.
```

风格块里最容易被忽略、但最影响观感的四件事：

1. `pure white`——否则模型给你米色纸纹。
2. `handwritten (not typeset)`——否则变成印刷体信息图。
3. `visible wax-pencil grain`——否则像普通矢量图。
4. `no shadows, no gradients`——否则有廉价 3D 感。

## 5. 精确文本契约

把所有字符串逐条列出，并声明“只允许这些文字”。模型默认会补标题、图例和副标题，必须禁止。

```text
Exact text, use these strings verbatim:
- Top heading: "多项任务，一眼看清"
- Subtitle: "同一时刻 · 不同状态"
- Status labels: "排队" / "执行中" / "等待事件" / "等待你" / "待验收" / "已完成"
- Card titles: "升级兼容性测试" / "BABA 下跌研究" / ...

Only permitted text: the headings above, "AI", "人", "执行".
No subtitles, no legend, no extra words or numbers.
```

中文图额外加：

```text
Very large extremely legible Chinese labels; neat upright hand-lettered
appearance, accurate Simplified Chinese. English headings bold and large,
keep exactly as written.
```

写契约时的习惯：

- 中文用直角引号或代码格式包起来，和普通描述分开。
- 一行文字对应一个 `label:`，不要让模型自己组合。
- 明确换行：`which may wrap over 2 lines`。
- 明确禁止：`do not abbreviate`、`do not translate`。
- 数字和单位照抄：`BABA < $100`、`USD 100`。

## 6. 构图

讲清“谁在哪、走哪条通道、什么颜色、怎么绕开”。不要只给节点列表。

```text
Composition: central vertical spine Message Gateway, Inbox, Front Agent,
Persistent Task Records, Task Dispatching, Worker Agent, with workspaces at
bottom. Put You upper left; Kanban in the left margin around Task Records,
with a clean outer left route from You. Put Outbox upper/right of Front Agent.

Reserve clear lanes for the Task Records -> Outbox fast alert path and the
Worker -> Task Records progress path. Avoid arrow crossings wherever possible;
no line through text or nodes.
```

构图块的四个要素：

1. **主轴**：读者视线的第一落点。
2. **分区**：用色块、留白或细线分隔，不要用大标题。
3. **通道**：每条回流/异步路径单独占一条曲线，不和去程重叠。
4. **颜色语义**：`messaging nodes blue, event/routing nodes green, task records orange`。

## 7. 拓扑

最容易被模型“优化”掉的部分。节点、边、方向、标签要显式枚举。

```text
Graph (exactly 8 nodes: Source, Thread, Existing Ticket, Policy, Eval,
New Ticket, Decision Record, Executor):
Source -> Thread [Emit Trigger]
Thread -> Existing Ticket [Subscription Fan-out]
Thread -> Eval [New Work Candidate]
Policy -> Eval [Assessment Rules]
Eval -> New Ticket [Accept with Mandate]
Eval -> Decision Record [Ignore or Unavailable]
New Ticket -> Executor
Existing Ticket -> Executor [Additional Context]

Every connection must be visible with a correct arrowhead. No spurious arrows.
```

写法建议：

- 先给节点数和节点名，再给边。模型会拿它当检查表。
- 边用 `A -> B [label]`，双向写 `A <-> B` 或“two separate directional arrows”。
- 明确终点：`Decision Record is a terminal node on the right.`
- 明确合流：`Existing Ticket and New Ticket converge at ONE shared Executor.`
- 用 `scripts/mmd_outline.py` 生成清单，避免手抄漏边。

## 8. 负向约束

把“不要什么”写成完整清单。负向约束不是可选项，尤其对文字和箭头。

```text
No title, no prose, no extra arrows, no icon needed. No watermark. No paper
tint, no shadows, no gradients, no dark background, no decoration unrelated
to content. This is our own proposed board, NOT a recreation or screenshot
of any existing product. Do not include company logos or product names.
```

常见必须禁止项：

- 标题 / 副标题 / 图例 / 解释段落
- 多余箭头、发明步骤、重复标签
- 水印、签名、边框、装饰涂鸦
- 品牌名、Logo、产品截图
- 照片级真实感、3D、渐变、阴影

## 9. 修订记录

改图时不要重写全文，写“保持 + 修改”：

```text
Keep the composition and all labels exactly as before. Change only:
1. Move the "Policy" node to the right of "Eval" so it does not sit on the arrow.
2. Redraw the return arrow with a wider curve; it currently crosses "Outbox".
Everything else must remain pixel-identical in layout.
```

同时记录生成器的已知问题：

```text
Requested 5:1; generator returned a taller file with white bands, so final
delivery is a 5:1 crop of the artwork.
```

---

## 长度与信息密度

- 一条提示词 300–900 字是正常的；拓扑复杂时可以更长。
- 重复不是问题，**矛盾**才是问题。同一句颜色/文字规则不要前后不一致。
- 提示词是给模型看的检查表，不是给人看的文章。用短句、清单、祈使句。
- 每增加一个“可选装饰”，就多一个偏离风险。默认不加。

## 正反例

| 弱写法 | 强写法 |
| --- | --- |
| Draw an architecture diagram | Exactly 15 nodes; every edge listed with direction and label |
| Use Chinese labels | Exact text: "等待你", "确认破坏性变更"; accurate Simplified Chinese |
| Make it hand-drawn | Handwritten lettering with natural irregularity, not typeset; visible wax grain |
| Add some arrows | 8 directed edges as listed; no spurious arrows; no crossings |
| Nice colors | Messaging blue, task records orange, event routing green, workspaces pale blue |
| Mobile friendly | Portrait 2:3, 1200x1600, large labels readable at 390px width |
