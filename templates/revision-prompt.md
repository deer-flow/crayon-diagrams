# Revision Prompt Template

改图时使用增量提示词，不要重写整条提示词。原则：**先锁定不变项，再列改动项，最后重申负向约束。**

## 单点修订

```text
Keep the composition, style and all labels exactly as they are. Change only:

1. <具体改动，一条一句。>
   Current: <现在的样子>
   Wanted: <期望的样子>
2. <如果有第二条。>

Do not change anything else. Do not add new nodes, arrows, titles, legends or
text. Preserve the pure white background and handwritten lettering.
```

## 文字修订

```text
Keep the entire illustration unchanged. Correct only the label at <位置>.
It currently reads "<错误文本>"; it must read exactly "<正确文本>" in accurate
Simplified Chinese, in the same handwritten style and size. Do not move or
redraw anything else.
```

## 拓扑修订

```text
Keep the layout and style. Fix the graph only:

- Remove the edge <A -> B>; it should not exist.
- Add the edge <C -> D> labelled "<label>".
- Reverse the arrow between <E> and <F>; direction is <E -> F>.
- Merge the duplicate "<node>" into one node.

All other edges must remain exactly as before. Total edges: <M>. No extra
arrows, no new nodes.
```

## 风格修订

```text
Keep the composition and all labels. Restyle only:

- Background: pure WHITE (#FFFFFF), remove any cream tint or paper texture.
- Lettering: clearly handwritten with natural irregularity, not typeset.
- Fill: pale wax-crayon, reduced saturation; more white space.
- Remove all shadows, gradients, 3D and glossy highlights.
Do not change the graph, labels, or layout.
```

## 比例 / 裁切修订

```text
Regenerate at exactly <2:3>. The artwork must be edge-to-edge with no
letterboxing, no white bands, and no border. Keep the same content, relative
sizes and labels.
```

如果生成器反复无法输出目标比例：

```text
The generator returned a taller image with blank bands. Crop the artwork to
5:1 without resampling, keeping all subjects fully inside the frame.
```

## 重绘启动条件

出现以下任一情况，不要局部修，直接按新提示词重绘：

- 两条以上边错误，或主线关系错。
- 同一个节点重复出现，且无法通过一次修订合并。
- 整体风格跑偏（印刷体、3D、幼稚化）且已经修过一轮。
- 文字错误覆盖三处以上。

重绘时把出错的约束**提前**，并提高具体性：

```text
CRITICAL: exactly 8 nodes, exactly 8 edges. Every edge listed below.
Do not add any other connection.
```

## 修订记录

在 `prompt.txt` 末尾保留一条简短记录，方便下次接着改：

```text
Revision history:
- v1: initial layout.
- v2: moved Policy right of Eval; did not change labels.
- v3: corrected "等待决定" glyphs; everything else unchanged.
```
