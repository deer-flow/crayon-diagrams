# 版式库

先选版式，再写提示词。下面每种版式都给出：适用场景、构图、提示词关键句、常见坑、仓库示例。

---

## 1. 垂直卡片流程

**适合**：3–6 步的线性流程、事件链路、文章里的“发生了什么”。

```text
┌─────────────────┐
│ 1  建立关注      │
└────────┬────────┘
         │ 条件命中
┌────────▼────────┐
│ 2  等待行情      │
└────────┬────────┘
         │ 触发
┌────────▼────────┐
│ 3  先发快讯 ─────┼──▶ You
└────────┬────────┘
         │ 入队即启动
┌────────▼────────┐
│ 4  评估接单      │
└────────┬────────┘
┌────────▼────────┐
│ 5  研究并交付 ───┼──▶ You
└─────────────────┘
```

构图要点：

- 竖版 2:3，卡片占左侧/中间约 70% 宽度，右侧留给投递分支。
- 每张卡：小图标 + 标题 + 一行副标题 + 可选一行注释。
- 箭头标签放在线旁，短到 2–4 个字。
- 投递分支用短箭头，不要和研究主线连在一起。

提示词关键句：

```text
Five spacious stacked rounded cards with simple downward arrows, NOT a
sequence diagram. Card 2 has a SHORT right arrow to a person labeled "You";
this delivery branch must NOT connect to the research step. A separate
DOWN arrow from card 2 to card 3 means research starts on queueing, not on
notification delivery.
```

常见坑：

- 模型把投递分支画成回主线的环。明确写 `must NOT connect`。
- 卡片越画越小、字被挤。限定“每卡最多三行文字”。

示例：`examples/monitoring-research/`、`examples/source-alert-research/`

---

## 2. 状态看板快照

**适合**：并行状态、任务面板、Kanban、“同一时刻的不同任务”。

```text
        多项任务，一眼看清
        同一时刻 · 不同状态

┌─────────┬─────────┐
│ 排队     │ 执行中   │
│ [卡片]   │ [卡片]   │
├─────────┼─────────┤
│ 等待事件 │ 等待你   │
│ [卡][卡] │ [卡片]   │
├─────────┼─────────┤
│ 待验收   │ 已完成   │
│ [卡片]   │ [卡片]   │
└─────────┴─────────┘

┌──────────────────────┐
│ 展开主任务：BABA 监控  │
│ ✓ 跌破条件已命中       │
│ ✓ 快讯已送达           │
│ ◷ 等待研究与分析交付   │
└──────────────────────┘
```

构图要点：

- 明确写 `This is a SNAPSHOT, NOT a sequential workflow.`
- **状态组之间禁止画箭头**；这是最常见的错误。
- 六个状态区等宽，卡片是白色纸片，状态区是淡彩底。
- 底部可放一张跨宽度的“展开卡”，用微弱色带关联，不要拉长线连接。

提示词关键句：

```text
This is a SNAPSHOT of different tasks, NOT a sequential workflow.
DO NOT draw arrows between status groups. Two columns and three rows of
clearly separated pale crayon status regions, one or two white task cards
inside each. Equal widths.
```

常见坑：

- 模型自动加流程箭头。负向约束放在构图段开头。
- 卡片文字被截断。给每张卡指定 `title` 和 `smaller second line`。

示例：`examples/kanban-snapshot/`

---

## 3. 双面板对照

**适合**：两个概念的直接对比，如 Human in the Loop vs Human on the Loop。

```text
┌────────────────────────────┐
│  Human in the Loop         │
│                            │
│ 完成分析 → 等待批准 → 执行升级 │
│              ▲             │
│              │             │
│             你             │
└────────────────────────────┘

┌────────────────────────────┐
│  Human on the Loop         │
│                            │
│ 发现更新 → 分析与测试 → 提交结果 │
│            ▲   ╲           │
│      查看与干预  ╲ 超出授权    │
│            │     ▼         │
│            你   等待决定      │
└────────────────────────────┘
```

构图要点：

- 竖版 3:4，上下两个清晰分离的面板，不要左右并排。
- 两个面板用不同淡彩：上 peach，下 sage/blue。
- 主路径用实线，监督/越权用虚线，并在提示词里说明虚线含义。
- 人形图标要小、简单，不要卡通脸。

提示词关键句：

```text
Two clearly separated panels stacked TOP and BOTTOM, not side by side.
Top: human approval lies in the MAIN path (solid arrows pass through the person).
Bottom: the solid normal path never passes through the human; a dashed amber
arrow goes from the process to "等待决定", and a dashed blue curve returns
from the human to the process.
```

常见坑：

- 两个面板的箭头风格混在一起，读者看不出区别。给每个面板单独写箭头规则。
- 虚线被画成实线。写 `dashed, clearly broken strokes`。

示例：`examples/human-in-on-loop/`

---

## 4. 三行概念对照

**适合**：三种模式的递进，如 in / on / out of the loop。

```text
   Human in the Loop
   ╭──▶ 人 ──▶ 执行 ──╮
   ╰──── AI ◀─────────╯

   Human on the Loop
   ╭──▶ AI ──▶ 执行 ──╮
   ╰──────────────────╯
        ┆ 监督（虚线）
        人

   Human out of the Loop
   ╭──▶ AI ──▶ 执行 ──╮
   ╰──────────────────╯
```

构图要点：

- 三行等高等大，结构完全一致，只改变人的位置。
- 人形在行 1 的环内、行 2 的环外、行 3 不出现。
- 行 3 不能出现任何人形、人物标签或监督虚线——负向约束要精确到这一行。
- 只允许标题 + `AI` / `人` / `执行`，不要图例和解释。

提示词关键句：

```text
Three equally sized rows stacked vertically. All three loops same size and
structure, making the human position the visual focus. Row 3: absolutely NO
human icon or human label and NO dashed supervision connector.
Only permitted text: the three exact English headings, "AI", "人", "执行".
```

常见坑：

- 行 3 仍画了人。把 `absolutely NO` 写进该行而不是总负向约束。
- 三行大小不一，视觉重点跑偏。写 `same size and structure`。

示例：`examples/human-in-on-out-loop/`

---

## 5. 中心脊梁架构图

**适合**：10–16 个节点的系统架构、消息流 + 任务流。

```text
You ──────────────┐
  │               │
  ▼               ▼
Message Gateway   Kanban
  │               ▲
Inbox             │ view/manage
  │               │
Front Agent ──────┤
  │               │
  ▼               │
Persistent Task Records ◀── Evaluation & Routing ◀── Trigger ◀── Source
  │        ▲     │                        ▲
  ▼        │     ▼                        │
Dispatch  Worker  Outbox ──▶ Gateway      Policy
  │        │
  ▼        ▼
Workspace  Parent Workspace
```

构图要点：

- 中间一条竖直主轴：Gateway → Inbox → Front Agent → Records → Dispatch → Worker。
- 右侧一条事件通道：Source → Trigger → Eval → Records；Policy 贴在 Eval 旁。
- 左侧留给 Kanban 和 You 的外围路线；底部放两个互不相连的 Workspace。
- 核心节点（Task Records）用暖橙，消息节点蓝，事件节点绿，工作区淡蓝。
- 回流线（Worker → Records、Records → Front、Outbox → Gateway）各自独立通道。

提示词关键句：

```text
Central vertical spine Message Gateway, Inbox, Front Agent, Persistent Task
Records, Task Dispatching, Worker Agent, with workspaces at bottom. Put Source
-> Trigger -> Evaluation and Subscription Routing in a right-side vertical lane,
with Policy adjacent to Routing. Route return arrows alongside their forward
arrows as separate visible curves. Task Records is the central visually
prominent orange node. The 2 workspaces at bottom must be distinctly separate;
no arrow between them.
```

常见坑：

- 回流线和去程重叠，箭头指向不清。为每条回流指定“外侧/下方通道”。
- 节点被自动复制（同一个词出现两次）。写 `Each named node appears ONCE.`
- 边被漏画。枚举所有边并写 `EVERY graph connection must be visible`.

示例：`examples/personal-agent-architecture/`

---

## 6. 拓扑重绘（Mermaid → 手机竖版）

**适合**：已有 Mermaid / 白板图，需要保留关系但重排成可读的竖版。

```text
Mermaid (LR, 宽)               重绘 (竖版/近方形)

Source → Thread → ...    →    两分支、单合流、右侧终点
```

流程：

1. 保留原始 `.mmd` 作为语义层。
2. 用 `mmd_outline.py` 导出节点/边清单。
3. 在提示词里写 `Input image is the content reference. Preserve all specified
   graph connections exactly; reflow into portrait or nearly square.`
4. 指定新的构图（分支、合流、终点），而不是照搬 LR 布局。

提示词关键句：

```text
Reflow its ultra-wide graph into a readable portrait or nearly square chart
with two branches, NOT a single pipeline. Keep the exact English labels, which
may wrap over 2 lines. Existing Ticket and New Ticket converge at ONE shared
Executor near bottom. Decision Record is a terminal node on the right.
```

常见坑：

- 模型把分支拉直成流水线。写 `two branches, NOT a single pipeline`。
- 标签贴到错误的箭头。写 `Labels belong beside the correct arrows; do not
  place a label on a different route.`
- 边数变化。写 `Exactly N nodes` + 完整边列表。

示例：`examples/domain-event-flow/`、`examples/message-gateway/`

---

## 7. 超宽文章横幅

**适合**：文章顶部 hero、系列封面。**不用于解释结构。**

```text
┌──────────────────────────────────────────────┐
│  角色 A     角色 B      角色 C               │  5:1
└──────────────────────────────────────────────┘
```

构图要点：

- 5:1（如 3200×640），edge-to-edge，不能是“放在更高画布里的横幅”。
- 三个视觉区连续过渡，不做三个独立画框。
- 角色大、道具少、每个角色周围留呼吸空间。
- 像素风要写 `crisp square pixels, limited color ramp, stepped silhouettes`。
- 不要复刻第三方 IP 角色；用原创吉祥物。

提示词关键句：

```text
EXACT ultra-wide aspect ratio 5:1, target 3200 x 640 pixels, edge-to-edge
artwork, no letterboxing or blank bands. One continuous panoramic scene with
3 interlocking color zones, not separate boxed portraits. The final image
itself must be a wide 5:1 banner, not a banner sitting inside a taller canvas.
```

常见坑：

- 生成器返回带白边的更高画布。最终交付时裁成 5:1，并在修订记录里说明。
- 角色被裁切。写 `fully within the shallow 5:1 frame` + `breathing room around each character`。

示例：仓库未收录该示例（涉及第三方角色参考），按本节规则自建原创角色。

---

## 版式选择速查

| 内容特征 | 选版式 |
| --- | --- |
| 3–6 步线性流程 | 垂直卡片流程 |
| 同一时刻多个状态 | 状态看板快照 |
| 两个概念对照 | 双面板对照 |
| 三种模式递进 | 三行概念对照 |
| 10+ 节点系统结构 | 中心脊梁架构图 |
| 已有 Mermaid / 白板图 | 拓扑重绘 |
| 文章封面 / 系列 hero | 超宽横幅 |

选不定时，优先**垂直卡片流程**：它对手机最友好，也最容易保证关系准确。
