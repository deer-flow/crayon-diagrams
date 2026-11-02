# 交付前 QA 检查表

生成后用 60 秒过一遍。结构错误优先于美观问题；文字错误优先于风格问题。

## 1. 语义与拓扑

- [ ] 节点数量与 `source.mmd` / 内容契约一致。
- [ ] 每条边都存在，方向正确，箭头头部清楚。
- [ ] 该有的合流只有一个（例如两个 Ticket 汇入同一个 Executor）。
- [ ] 该有的终点确实是终端节点，没有继续延伸。
- [ ] 没有多余箭头、发明出来的步骤、重复节点。
- [ ] 双向关系画成了两条可分辨的箭头，或一条明确的 `<->`。
- [ ] 虚线只出现在非主路径，且含义在图中可理解。
- [ ] 回流线没有和去程重叠，没有穿过文字或节点。

用脚本核对：

```bash
python3 scripts/mmd_outline.py source.mmd
```

把输出的 `Nodes (N)` / `Edges (M)` 与提示词里的 `Exactly N nodes / M edges` 对齐。

## 2. 文字

- [ ] 每个字符串逐字正确，标点、大小写、空格一致。
- [ ] 中文是简体，没有错字、缺笔、生造字。
- [ ] 英文没有被翻译、缩写或改写。
- [ ] 数字、价格、版本号、比较符号（`<`、`$`）正确。
- [ ] 没有出现提示词之外的标题、图例、副标题、说明段落。
- [ ] 标签在正确的箭头/节点旁，没有错位。
- [ ] 文字没有被线穿过，没有被裁切。

中文图的检查方法：放大到 200%，从左到右、从上到下逐个读。模型最常错的是形近字和长句。

## 3. 版式与可读性

- [ ] 手机宽度（约 390px）下，正文标签仍可读。
- [ ] 视觉焦点符合图的意图（例如 Task Records 是中心）。
- [ ] 留白足够，没有元素挤在一起。
- [ ] 分区清晰，但没有多余的边框和装饰。
- [ ] 比例正确（2:3 / 3:4 / 1:1 / 5:1），没有白边或 letterbox。
- [ ] 角色/图标没有遮挡关键文字或箭头。

## 4. 风格

- [ ] 背景是纯白，不是米色或纸纹。
- [ ] 线条是手绘石墨/蜡笔，不是印刷矢量线。
- [ ] 文字是手写感，不是排版字体。
- [ ] 填充是淡彩蜡笔，不是高饱和色块。
- [ ] 没有阴影、渐变、3D、高光。
- [ ] 蜡笔颗粒可见但不脏。
- [ ] 同一系列的颜色语义一致。

## 5. 合规

- [ ] 没有水印、签名、边框、二维码。
- [ ] 没有品牌 Logo、产品名、产品截图。
- [ ] 没有复刻第三方 IP 角色或知名游戏画面。
- [ ] 没有编造真实价格、数据、引用。

## 6. 交付

- [ ] `source.mmd`、`prompt.txt`、预览图放在同一目录。
- [ ] 文件名描述内容，而不是 `final-v2`。
- [ ] 在回复里说明：这张图的主张、被简化的关系、需要人工核对的标签。
- [ ] 没有声称“完全准确”。

---

## 失败 → 修订措辞

| 问题 | 增量修订措辞 |
| --- | --- |
| 多了标题/副标题 | `Remove all titles and subtitles. Only the quoted labels may appear.` |
| 多了箭头 | `Remove the arrow between X and Y; there are exactly N edges as listed.` |
| 少了一条边 | `Add the missing edge A -> B labelled "...". Keep everything else unchanged.` |
| 箭头方向反了 | `Reverse the arrow between A and B; the direction is A -> B.` |
| 标签贴错线 | `Move the label "..." onto the arrow from X to Y; it is currently on the wrong route.` |
| 中文错字 | `Correct the label "..." to exactly "..." in accurate Simplified Chinese; keep the handwriting style.` |
| 文字被线穿过 | `Reroute the arrow so it does not cross the label "..." or any node.` |
| 交叉过多 | `Route the return path along the outer margin; do not cross the forward arrows.` |
| 节点重复 | `Each named node must appear exactly once. Merge the duplicate "..." into one node.` |
| 回流线重叠 | `Separate the return arrow from the forward arrow by a visible offset; both arrowheads must be clear.` |
| 背景发黄 | `Pure white background (#FFFFFF); remove all paper tint and texture.` |
| 字太像印刷体 | `Make the lettering clearly handwritten with natural slight irregularity, not typeset.` |
| 画面太幼稚 | `More restrained and sophisticated sketchbook style; remove decorative doodles and bold colors.` |
| 比例不对/有白边 | `Regenerate edge-to-edge at exactly 2:3; no letterboxing or blank bands.` |
| 行 3 出现了人 | `Remove the human icon, human label and dashed connector from row 3 entirely.` |
| 投递分支连到研究线 | `The short delivery arrow to "You" must not connect to the research step.` |

## 重绘还是局部修？

- **局部问题**（一个错字、一条线、一个标签错位）：写增量修订，要求“其余保持不变”。
- **结构问题**（≥2 条边错误、节点重复、主线关系错）：重写提示词，把出错的约束提前并加粗。
- **风格问题**（整体发灰/幼稚/印刷体）：换风格块，不要只改形容词。
- **文字问题反复出现**：把标签缩短到 2–4 字，或把文字层留给排版工具后期添加。

## 回复模板

```text
已完成：<一句话主张>

需要你核对：
- 中文标签：<列出 1–2 个最可能出错的>
- 已简化：<被合并或省略的关系>
- 生成器限制：<例如 5:1 需要裁切、某条虚线可能被画成实线>
```
