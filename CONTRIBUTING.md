# Contributing

欢迎补充新的版式、提示词模板、模型适配经验和示例。

## 可以贡献什么

- 新的版式（例如时序图、状态机、泳道图）及其避坑说明。
- 同一张图在不同生成器上的提示词适配。
- 更精确的 QA 规则或自动化检查。
- 真实示例：`source.mmd` + `prompt.txt` + 压缩预览图。

不适合：第三方 IP 角色二创、产品截图复刻、需要付费素材的示例。

## 新增示例

每个示例一个目录，目录名描述内容（不用 `test`、`final`、`v2`）：

```text
examples/<content-slug>/
├── source.mmd      # 拓扑图必需；概念图可省略
├── prompt.txt      # 实际使用的提示词，逐字保留
└── preview.webp    # 宽 1200px 左右，建议 < 300 KB
```

要求：

1. `prompt.txt` 是你实际用过的版本，不要事后美化。
2. 有拓扑的图必须附 `source.mmd`，并确保 `mmd_outline.py` 能无警告解析。
3. 预览图只放压缩版；原始大图不要入库。
4. 在 `README.md` 的示例表格里加一行说明版式和看点。
5. 在 `examples/README.md` 里补充生成器、迭代次数和已知缺陷。

## 修改提示词规范

- 保持九块结构（见 `references/prompt-anatomy.md`）。
- 文字必须逐字引用，并写明“只允许这些文字”。
- 新增经验时给出**失败现象 → 修正措辞**，不要只写“效果更好”。
- 中文文档；代码、提示词、变量名用英文。

## 本地检查

```bash
# Mermaid 解析（CI 会跑）
python3 scripts/mmd_outline.py examples/*/source.mmd --strict

# 每个示例必须有 prompt.txt
for dir in examples/*/; do test -f "$dir/prompt.txt" || echo "missing: $dir"; done
```

有 Pillow 时可以重新生成预览：

```bash
python3 scripts/make_previews.py original.png examples/<slug>/preview.webp
```

## 提交 PR

- 一个 PR 只做一件事：一个新示例、或一类文档改进。
- PR 描述里写：解决什么问题、验证方式、是否逐字核对过文字。
- 不要提交未授权的图片、字体、角色形象或品牌素材。
- 提交信息用英文祈使句，例如 `Add sequence-diagram example`。

## 风格底线

- 不复制他人有版权的插图；只学习构图和措辞。
- 不声称生成结果 100% 准确。
- 示例中的公司名、价格、数据必须是脱敏或虚构的。
