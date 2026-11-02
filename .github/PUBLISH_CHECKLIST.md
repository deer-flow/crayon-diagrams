# Publish checklist — crayon-diagrams

Report from the `github-launch` skill. Status is `pass`, `fail`, or `skip`. This file does not block `git push`.

| Item | Status | Note |
| --- | --- | --- |
| Intake recorded (kind, audience, languages, owner) | pass | Agent skill; Chinese tech-blog authors and Claude Code users; Python 3.9+; owner deer-flow, author LofiSu. |
| Secrets scan | pass | `git grep` over tracked files; no credential hits. |
| Personal data scan | pass | No local paths, phone numbers, or private emails in tracked files. |
| Dead demos removed or kept on purpose | pass | No framework demo or placeholder README; none removed. |
| License headers match LICENSE, or none required | pass | No SPDX headers; MIT requires none. |
| `.gitignore` covers secrets and build output | pass | Added `.env`, `.env.*` with `.env.example` exception, `*.pem`, `*.key`, `build/`, `dist/`. |
| Large binaries reviewed | pass | Largest tracked file is 237 KB; no file at or above 1 MB. |
| LICENSE present; SPDX matches the README | pass | MIT; both READMEs state SPDX `MIT`. |
| `README.md` and `README.zh-CN.md` share structure and facts | pass | Eight H2 sections in the same order; commands, URLs, and version numbers identical. |
| No double-brace uppercase placeholders left in published files | pass | No double-brace uppercase placeholders remain in the published paths. |
| About description is 160 characters or fewer | pass | 133 characters; leads with the product noun. |
| 5–10 topics | pass | 10 existing topics retained. |
| CI workflow matches the stack | pass | `validate.yml` runs the Mermaid parser, SKILL frontmatter check, and example layout check. |
| Pages decision recorded; the agent did not enable Pages | pass | `docs/index.html`, `docs/preview.webp`, and `docs/.nojekyll` written; Pages not enabled. |
| Homepage URL recorded; set only after the site loads | skip | `https://deer-flow.github.io/crayon-diagrams/` recorded; not set in the About field. |
| Product noun in the H1 and Features; stable headings and Pages meta; no FAQ section | pass | H1 and Features use `crayon-diagrams`; exact headings; title, meta, canonical, Open Graph, and JSON-LD set; no FAQ. |
| doc-lint pass on README.zh-CN.md and other Chinese docs this launch wrote | pass | Chinese README reviewed for concision, translationese, and technical-term parity. |
| Push | pass | Pushed to `deer-flow/crayon-diagrams` main as the initial import. |
