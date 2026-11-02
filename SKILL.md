---
name: crayon-diagrams
description: 为中文技术博客创作“蜡笔手绘”风格的技术插图（架构图、流程图、对比图、看板快照、文章横幅）。Use when the user asks for hand-drawn crayon/sketch-style technical diagrams, blog illustrations, architecture or process infographics, or wants to redraw a Mermaid/diagram in a consistent crayon style. Triggers include 画一张图、技术博客配图、手绘风格、蜡笔、架构图、流程图、对比图、信息图、crayon diagram, hand-drawn infographic, sketch diagram, blog hero image.
---

# Crayon Diagrams

把文章要讲清楚的结构，先变成**可校验的语义层**，再变成**图像生成提示词**。

这套 skill 的核心不是“画得好看”，而是三件事：

1. **关系准确**——节点、箭头、方向、标签一个不多一个不少。
2. **手机可读**——竖版、大字号、留白，读者在 390px 宽度下能看清。
3. **风格统一**——同一系列插图共享画布、线条、配色和字形。

风格只是最后一层。先保证图能讲清逻辑，再谈手绘质感。

---

## 何时使用

- 中文技术博客 / 公众号 / 小红书的技术配图。
- 把 Mermaid、白板草图、产品截图重绘成统一的手绘风格。
- 需要“人类在环”“任务看板”“消息网关”这类概念图。
- 需要一组风格一致的系列插图（架构 + 流程 + 对比）。

**不适用**：数据精确的可视化（用图表工具）、需要逐像素还原的产品截图、含第三方 IP 角色的二创（不要生成）。

---

## 工作流

### 0. 判断任务类型

| 类型 | 输入 | 产物 |
| --- | --- | --- |
| 新建拓扑图 | 口述结构 / 已有 Mermaid | `source.mmd` + `prompt.txt` + 图 |
| 重绘已有图 | 参考图 | 判定“内容参考”还是“仅风格参考” |
| 概念/版式图 | 内容清单（看板、对比、卡片流） | `content.md` + `prompt.txt` + 图 |
| 修订 | 上一版图 + 缺陷 | 增量修订提示词 |

### 1. 先写语义层，不要直接写提示词

拓扑图先写 Mermaid：

```bash
python3 scripts/mmd_outline.py path/to/source.mmd
```

把输出的 **Nodes / Edges / Labels 数量** 锁进提示词。概念图则写一份内容契约：每一行文字、每个分组、哪些元素之间**没有**箭头。

规则：

- 一张图只讲一个主张。超过约 15 个节点或 20 条边，拆图或删细节。
- 节点名用读者能懂的业务词，不用内部代号。
- 明确哪些关系**不存在**（“status groups 之间不要画箭头”），否则模型会自作主张连线。

### 2. 选版式

先选版式再写提示词，不要边写边想布局。常用版式见 `references/layout-patterns.md`：

- 垂直卡片流程（步骤 / 时间线）
- 状态看板快照（并列状态，不画箭头）
- 双面板对照（in the loop / on the loop）
- 三行概念对照（in / on / out）
- 中心脊梁架构图（Gateway → Agent → Records → Worker）
- 拓扑重绘（Mermaid → 手机竖版）
- 超宽文章横幅（5:1，独立裁切）

### 3. 按九块结构写提示词

完整说明见 `references/prompt-anatomy.md`，模板见 `templates/diagram-prompt.md`：

1. **生成器与输入**：模型、参考图角色（内容参考 / 仅风格 / 仅角色）。
2. **用途与受众**：技术博客、手机阅读、中文/英文标注。
3. **画布**：比例、像素、纯白背景、留白。
4. **风格**：手绘石墨/蜡笔轮廓、淡彩填充、手写字、禁止阴影/渐变/纸纹。
5. **精确文本契约**：逐条引用每个字符串，声明“只允许出现这些文字”。
6. **构图**：分区、位置、每条通道、颜色语义、箭头绕行。
7. **拓扑**：节点与边的完整清单，标注方向与标签。
8. **负向约束**：不要标题、图例、水印、多余箭头、发明步骤、品牌 Logo。
9. **修订记录**（改图时）：相对上一版改了什么，哪些必须保持不变。

### 4. 生成

- 有生图工具：直接调用，优先用参考图做风格锚点。
- 没有生图工具：把 `prompt.txt` 交给用户，附上比例与参考图说明。
- 一次只改一个变量；不要在同一次生成里同时改布局、配色和文案。

### 5. QA 后交付

逐项过 `references/qa-checklist.md`。重点：

- 每个字符串是否**逐字**正确（尤其中文，模型常写错字）。
- 箭头数量、方向、标签是否与语义层一致。
- 有没有多余标题、图例、箭头、水印。
- 手机宽度下是否可读，文字有没有被线穿过。

不合格时用 `templates/revision-prompt.md` 写**增量修订**，不要重写整段提示词。

### 6. 存档

同一张图的三件套放在一起，按内容命名（不要用 `final-v2`）：

```
examples/message-gateway/
├── source.mmd       # 语义层
├── prompt.txt       # 生成提示词
└── preview.webp     # 输出预览
```

---

## 硬规则

### 文本

- 所有要出现的文字**逐字引用**，中英文分开声明。
- 明确写 `Only permitted text: ...` / `Do not add any other words`。
- 长标签允许换行时，写明“可换 2 行”，避免模型缩写。
- 中文图必须写“准确的简体中文、手写但工整”；生成后逐字核对。

### 关系

- 枚举节点和边，给出数量（`Exactly 8 nodes`、`every connection must be visible`）。
- 双向关系要画成两条可分辨的箭头，或明确写“two separate directional arrows”。
- 虚线只用于**非主路径**（监督、越权、异步），并在提示词里说明虚线含义。
- 禁止交叉：给每条回流线分配独立通道（“route return arrows alongside their forward arrows”）。

### 参考图

- 只借风格时写死：`The reference is STYLE ONLY. Do NOT copy its graph or labels.`
- 要保留拓扑时写：`Input image is the content reference. Preserve all connections and labels; redesign the layout.`
- 借角色形象时写：`CHARACTER REFERENCES ONLY, not layouts`；不要复刻第三方 IP。

### 版式

- 手机竖版：`2:3` 或 `3:4`，大字号、少文字、大量留白。
- 不要在一张竖图里塞横向长流程；超过 5 步就拆成卡片或分图。
- 颜色承担语义：主路径、异步、人工、告警各用一种，且全系列保持一致。
- 一图一个视觉焦点；标题不是必须的，文章正文会解释。

### 负向约束（几乎每张图都要写）

```
No paper tint, no shadows, no gradients, no 3D, no watermark,
no title, no legend, no explanatory paragraphs, no extra arrows,
no invented steps, no product logos, no photorealism.
```

---

## 风格速查

完整风格块与配色见 `references/style-crayon.md`。核心描述：

> Pure white background, hand-drawn graphite/crayon outlines and arrows,
> pale blue / sage green / warm orange wax-crayon fills, clearly handwritten
> lettering with natural irregularity (not typeset), visible wax-pencil grain,
> clean friendly editorial sketch, generous whitespace, large mobile-legible labels.

三个变体：

- **英文标注**：handwritten English，适合架构图、拓扑图。
- **中文标注**：handwritten Simplified Chinese，工整、准确、大字号。
- **像素横幅**：16-bit 像素 + 波普海报，仅用于文章 hero，不用于解释结构。

---

## 快速模板

时间紧时，至少写全这五段：

```text
Use case: infographic-diagram for a Chinese technical blog. Optimized for mobile.

Canvas: portrait 2:3, pure white background, generous whitespace.
Style: hand-drawn graphite/crayon outlines, pale wax fills, handwritten
lettering, no shadows/gradients/paper tint/watermark.

Exact text (only these strings): "..." / "..." / "...". Simplified Chinese
must be written accurately; English exactly as quoted.

Layout: [版式] ... [分区、位置、颜色语义、每条箭头通道].

Graph: exactly N nodes: ...; exactly M edges: A -> B [label], ...
No extra arrows, no title, no legend, no invented steps.
```

---

## 文件索引

| 文件 | 用途 |
| --- | --- |
| `references/prompt-anatomy.md` | 九块结构、正反例、措辞习惯 |
| `references/style-crayon.md` | 风格块、配色、字形、模型差异 |
| `references/layout-patterns.md` | 七种版式与避坑 |
| `references/qa-checklist.md` | 交付前检查表与失败→修订对照 |
| `templates/diagram-prompt.md` | 可填空的完整提示词模板 |
| `templates/revision-prompt.md` | 增量修订模板 |
| `scripts/mmd_outline.py` | 从 Mermaid 提取节点/边/标签清单 |
| `examples/` | 8 组真实提示词（7 组含输出预览） |

## 交付话术

生成后给用户三样东西：

1. 图片（或提示词文件）。
2. 一句话说明这张图的主张。
3. 已知风险：哪些标签可能需人工核对、哪些关系被简化了。

不要声称“完全准确”。生图模型对文字和拓扑的保真度有限，QA 结果要如实说明。
