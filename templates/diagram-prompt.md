# Diagram Prompt Template

复制整段，替换 `<...>`。方括号 `[...]` 是写作提示，提交前删除。

---

## A. 拓扑图 / 架构图

```text
Use case: infographic-diagram / style-transfer for a Chinese technical blog,
optimized for reading on a mobile phone.

<input role — choose one>
Input image is the content reference. Preserve all specified graph connections
and exact labels; completely redesign the layout for a portrait canvas.
[or] The reference image is STYLE ONLY. Do NOT copy its graph, nodes or labels.

Canvas: portrait <2:3 | 3:4>, about <1200 x 1600>, pure WHITE background,
generous margins and whitespace.

Style: hand-drawn dark graphite/crayon outlines and arrows, pale blue / sage
green / warm orange wax-crayon fills, clearly HANDWRITTEN lettering with natural
slight irregularity (not typeset), visible wax-pencil grain. Clean, friendly
editorial sketch. No paper tint, no shadows, no gradients, no 3D, no watermark.

Exact text — use these strings verbatim, no additions:
- <string 1>
- <string 2>
- <string 3>
Only permitted text: the strings above. No title, no legend, no subtitle,
no explanatory prose. Chinese must be accurate Simplified Chinese; English
must be spelled exactly as quoted. Long labels may wrap over <2> lines.

Layout: <central vertical spine / two branches / stacked panels / three rows>.
<Where each group sits. Which node is the visual focus. Which color each group
uses. Where the return paths run. What must converge and what must stay separate.>

Graph — exactly <N> nodes: <node list>.
Exactly <M> directed edges:
  A -> B [label]
  B -> C
  ...
Every connection above must be visible with a clear arrowhead. Each named node
appears exactly once. No spurious arrows, no ambiguous crossings, no line
through text or nodes. Labels belong beside the correct arrows.

Negative constraints: no title, no legend, no extra arrows, no invented steps,
no duplicated labels, no watermark, no signature, no decorative doodles,
no product logos or brand names. <Any case-specific ban.>
```

---

## B. 概念图 / 看板 / 对照图

```text
Use case: infographic-diagram for a Chinese technical blog, mobile-first.

Canvas: portrait <2:3>, pure white background, abundant whitespace.

Style: <crayon style block from references/style-crayon.md>.

Exact text — use these strings verbatim:
- Heading: "<...>"
- Subtitle: "<...>"
- Region labels: "<...>" / "<...>" / "<...>"
- Card titles: "<...>" / "<...>" / "<...>"
Only permitted text: the strings above. No numbering, no extra words,
no English except <BABA / PR / You>. Accurate Simplified Chinese.

Composition: <two columns and three rows / three stacked rows / top and bottom
panels>. <What each region contains. What is NOT connected. Where the human
or icon sits. Which colors carry which meaning.>

<If this is a snapshot:>
This is a SNAPSHOT of different states, NOT a sequential workflow.
DO NOT draw arrows between status groups.

<If this is a comparison:>
The three loops must be the same size and structure, so the position of the
human is the only visual difference. Row <N> must contain NO human icon and
NO supervision connector.

Negative constraints: no title beyond the quoted heading, no legend, no arrows
between groups, no extra cards, no invented details, no watermark,
no photorealism, no shadows, no gradients, no paper tint.
```

---

## C. 超宽横幅

```text
Create an original editorial hero banner for a Chinese technical blog.
EXACT aspect ratio 5:1, target <3200 x 640> pixels, edge-to-edge, no letterboxing.

Art direction: <16-bit pixel art | crayon | flat editorial>.
<Palette. Line quality. Texture.>

Composition: one continuous panoramic scene with <3> interlocking color zones,
not separate boxed portraits. <Subject 1> on the left, <subject 2> in the center,
<subject 3> on the right. Keep props economical; subjects dominate. Leave
breathing room around each subject. The final image itself must be a 5:1 banner,
not a banner inside a taller canvas.

No headline, no long words, no UI, no logos, no third-party characters,
no photorealism, no 3D, no blur, no gradients except pixel dithering,
no watermark.
```

---

## 提交前自检

- [ ] 参考图角色已明确（内容参考 / 仅风格 / 仅角色）。
- [ ] 画布比例和背景已写死。
- [ ] 每个字符串都在契约里，且只出现一次。
- [ ] 节点数、边数、方向、标签完整。
- [ ] 至少写了 6 条负向约束。
- [ ] 手机可读：竖版、大字号、每卡不超过三行。
