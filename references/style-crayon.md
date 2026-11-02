# 蜡笔手绘风格规范

目标观感：**技术杂志里的手绘插图**，不是儿童画，也不是矢量信息图。线条有蜡质颗粒，颜色克制，文字像认真手写但完全可读。

## 核心风格块（英文标注）

直接复制使用，按图替换颜色名词：

```text
Pure WHITE background, hand-drawn dark graphite/crayon outlines and arrows,
pale blue crayon shaded rounded rectangles, clearly HANDWRITTEN lettering
with natural slight irregularity (not typeset). Restrained warm orange accent.
Clean, friendly editorial sketch, visible wax-pencil grain inside shapes,
no paper tint, no shadows, no decorations, no watermark. Large legible labels,
generous whitespace. Compact almost-square composition suitable for a phone screen.
```

## 核心风格块（中文标注）

```text
Pure white background, hand-drawn outlines and VERY LEGIBLE handwritten
Simplified Chinese lettering, soft blue / amber / mint / lavender crayon fills,
dark charcoal text. Charming restrained wax crayon drawing, clean editorial
diagram, not photorealism. Large text readable on mobile, abundant white space.
No drop shadows, no dark background, no decoration unrelated to content.
Accurate Simplified Chinese; do not invent characters or use Traditional Chinese.
```

中文图建议再加一句：

```text
Keep every Chinese label short and exactly as quoted; verify each character.
```

## 调色板

| 角色 | 建议色 | 用法 |
| --- | --- | --- |
| 背景 | `#FFFFFF` | 纯白，不要米色/纸纹 |
| 线条/文字 | `#2B2B2B` 石墨 | 所有轮廓、箭头、手写字 |
| 消息/网关 | `#CFE3F3` 淡蓝 | Inbox、Outbox、Channel、Gateway |
| 事件/路由 | `#D8E8D4` 鼠尾草绿 | Source、Trigger、Eval、Policy |
| 任务/核心 | `#F4A261` 暖橙 | Persistent Task Records、人工动作、警示路径 |
| 等待/异步 | `#F2C14E` 琥珀 | 等待、暂停、超出授权 |
| 工作区 | `#DDE9F5` 极淡蓝 | Workspace、临时目录 |
| 辅助 | `#E3DDF2` 薰衣草 | 次要分组，少用 |
| 完成 | `#D9EFE6` 薄荷 | 已完成、成功 |

规则：

- 一张图最多 4 个语义色 + 石墨色。
- 颜色必须承担语义，并在同系列中保持一致。
- 填充是**蜡笔淡彩**，不是高饱和色块；留出白色纸面。
- 同一节点只用一种填充色，避免渐变。

## 线条与质感

- 轮廓：深石墨、略不均匀、端点圆润；允许轻微重复描边。
- 箭头：实线 = 主路径；虚线 = 监督、越权、异步提醒。虚线语义必须在图内可理解。
- 填充：可见蜡笔颗粒和轻微出界，不要完美对齐。
- 圆角矩形：手绘的不规则圆角，不是标准 UI 卡片。
- 阴影：禁止。立体感用线条疏密表达。
- 图标：极简手绘小图标（放大镜、文件夹、铃铛、纸卡），不要彩色贴纸风。

## 文字

- 中英文都用手写体，但必须**工整、直立、可读**。
- 中文标签控制在 2–8 个字；长概念拆成标题 + 一行副标题。
- 英文长标签允许换行 2–3 行，提示词里写明。
- 不要全大写长句；不要艺术字、描边字、渐变字。
- 数字、价格、版本号最容易错，生成后逐字核对。

## 常见风格跑偏与修正

| 跑偏 | 修正措辞 |
| --- | --- |
| 变成印刷体信息图 | `clearly HANDWRITTEN lettering, not typeset, natural slight irregularity` |
| 米色纸纹背景 | `pure WHITE background (#FFFFFF), no paper tint, no texture on background` |
| 儿童画/幼稚涂鸦 | `sophisticated friendly sketchbook technical illustration, restrained, not childish` |
| 3D / 阴影 / 渐变 | `flat 2D, no shadows, no gradients, no 3D, no glossy highlights` |
| 颜色过饱和 | `pale wax-crayon fills, restrained palette, lots of white space` |
| 装饰抢戏 | `no decorative doodles, no ornaments competing with arrows` |
| 中文乱码/错字 | 缩短标签；写 `accurate Simplified Chinese`；生成后逐字核对并局部重绘 |

## 版本变体

### 像素风文章横幅

只用于 hero，不用于解释结构：

```text
Premium pop-art poster meets 16-bit SNES sprite art. Crisp square pixels,
limited color ramp shading, stepped silhouettes, pixelated halftone fields,
electric cobalt, coral-red, lemon yellow, turquoise, ivory, deep navy outlines.
One continuous panoramic scene, 5:1, edge-to-edge, no letterboxing.
No photorealism, no 3D, no blur, no gradients except pixel dithering.
```

注意：不要让模型复刻知名游戏角色或第三方 IP；只使用原创吉祥物。

### 高密度架构图

节点多时，风格要更克制：

```text
Lean technical sketch: thinner lines, smaller fills, labels dominate.
No decorative elements at all. Prioritize legibility over charm.
```

如果节点仍然挤，拆成两张图，而不是缩小字号。

## 不同生成器的差异

这些差异来自实际出图经验，写提示词时按模型调整：

| 生成器 | 注意点 |
| --- | --- |
| 内置 `image_gen` | 对长提示词和精确文字较友好；仍会自行加标题，负向约束要写全 |
| DeepSeek 系列 | 风格化更强，文字和连线更易漂移；必须给精确文本契约与节点数 |
| Gemini / Nano Banana | 参考图编辑能力强；区分“内容参考”和“仅风格”尤其重要 |
| GPT Image | 指令跟随好，但容易把图做得“太干净”；强调 wax grain 和手写感 |
| Midjourney | 风格强、文字弱；适合无字 hero，不适合精确拓扑 |
| Seedream / 豆包 | 中文文字相对好；仍需逐字核对，长句拆短 |

通用原则：**模型越不擅长文字，标签越短；模型越不擅长拓扑，边清单越显式。**

## 禁止清单

```text
No paper tint, no cream background, no shadows, no gradients, no 3D,
no glossy highlights, no watermark, no signature, no border frame,
no decorative doodles, no clip-art icons, no printed/typeset fonts,
no photorealism, no product screenshots, no brand logos.
```
