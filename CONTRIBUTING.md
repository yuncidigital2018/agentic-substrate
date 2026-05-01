# Contributing to Agentic Substrate
# 貢獻指南

Thank you for your interest in contributing! This is a knowledge framework, not a code library — so contributing here looks a little different.

感謝你有興趣貢獻！這是一個知識框架，不是程式庫——所以這裡的貢獻方式跟一般 repo 有點不同。

---

## Ways to Contribute 貢獻方式

### 1. Report Issues 回報問題

Found a factual error, broken link, unclear explanation, or inconsistency between documents?

發現事實錯誤、失效連結、不清楚的解釋或文件之間的不一致？

→ [Open an Issue](../../issues/new) with the label `content-fix`.

### 2. Suggest Improvements 建議改善

Have an idea for a better analogy, a missing concept, or a section that needs more depth?

有更好的類比、遺漏的概念、或需要更深入的段落？

→ [Open an Issue](../../issues/new) with the label `enhancement`.

### 3. Share Real-World Examples 分享真實案例

The most valuable contributions are **real-world Skill designs** from your own practice. If you've built Skills for non-coding workflows (HR, marketing, legal, finance, education, etc.), your experience fills a gap that the entire community needs.

最有價值的貢獻是來自你自己實踐的**真實 Skill 設計**。如果你為非寫程式的工作流（HR、行銷、法務、財務、教育等）建構過 Skills，你的經驗填補了整個社群需要的空缺。

→ [Open an Issue](../../issues/new) with the label `case-study`.

### 4. Translate 翻譯

This repo is bilingual (English + Traditional Chinese). If you'd like to add another language or improve existing translations:

本 repo 是雙語的（英文 + 繁體中文）。如果你想添加其他語言或改善現有翻譯：

→ [Open an Issue](../../issues/new) with the label `translation`.

### 5. Write New Sections 撰寫新章節

Check the README for sections marked with ⬜. Those are planned but not yet written. If you want to take one on:

查看 README 中標記 ⬜ 的章節。那些是已規劃但尚未撰寫的。如果你想承接：

→ Open an Issue to claim it first, then submit a PR.

---

## Writing Guidelines 撰寫準則

### Style 風格

- **Bilingual**: Every section should have both English and Traditional Chinese (繁體中文). English first, Chinese follows.
- **Concrete over abstract**: Use real examples, diagrams, and comparisons. Avoid jargon without explanation.
- **Practitioner voice**: Write as someone who builds things, not as an academic. Theory should serve practice.
- **No emojis in body text**: Keep the tone professional. Emojis are fine in file trees or status indicators only.

### Structure 結構

- Use `##` for major sections, `###` for subsections
- Include ASCII diagrams where they aid understanding
- Every concept should have at least one concrete example
- Cross-reference other documents in the repo when relevant

### Formatting 格式

- Line length: no hard limit, but keep paragraphs readable
- Tables: use Markdown tables for comparisons
- Code blocks: use fenced code blocks with language hints where applicable
- Links: use relative paths for internal links (`../02-architecture/landscape.md`)

---

## Contributing a Skill 貢獻一個 Skill

The most impactful contribution you can make is a **new Skill** from your own domain. Here's how:

你能做的最有影響力的貢獻是來自你自己領域的**新 Skill**。方法如下：

### Step 1: Create Your Skill 建立你的 Skill

Use the [Skill Builder](skills/skill-builder/SKILL.md) to guide you through the process, or write a SKILL.md from scratch using this template:

```
skills/examples/your-skill-name/
└── SKILL.md
```

Your SKILL.md must include YAML frontmatter:

```yaml
---
name: your-skill-name
description: >
  What this Skill does and when to use it.
  Include specific trigger phrases in quotes.
metadata:
  version: "0.1.0"
  type: "Process | Transform | Data | Integration | Orchestration"
  domain: "Your Domain"
---
```

### Step 2: Follow the Seven Components 遵循七大組件

Every Skill should address all seven components from [Skill Anatomy](docs/01-foundations/skill-anatomy.md):

1. **Identity** — Name, type, who it's for
2. **Trigger Conditions** — When to activate
3. **Process Logic** — Step-by-step workflow
4. **I/O Contract** — What it needs, what it produces
5. **Validation Rules** — How to verify correctness
6. **Knowledge** — Domain-specific expertise
7. **Composition Hooks** — What connects upstream/downstream

### Step 3: Add Wikilinks 加入 Wikilinks

Use Obsidian-style wikilinks to connect your Skill to related Skills. This enables automatic knowledge graph generation and helps agents discover related capabilities.

使用 Obsidian 風格的 wikilinks 來連接你的 Skill 與相關 Skill。這能自動產生知識圖譜，幫助 Agent 發現相關能力。

**In the body text**, reference other Skills with `[[skill-name]]`:

```markdown
This workflow pairs well with [[document-reviewer]] for quality assurance.
For the initial content gathering, see [[research-and-summarize]].
```

**In the Related Skills section** at the bottom:

```markdown
## Related Skills
- [[skill-builder]] — Use this to create new Skills from scratch
- [[document-reviewer]] — Quality assurance for document outputs
```

**Rules:**
- Use lowercase with hyphens: `[[my-skill-name]]` (matches the directory name)
- Add wikilinks the first time you mention another Skill in the body
- Always include a `## Related Skills` section at the bottom
- Wikilinks are **in addition to** markdown links — keep both formats

### Step 4: Quality Checklist 品質清單

Before submitting, verify:

- [ ] Bilingual (EN + ZH-TW) or at minimum English
- [ ] Process Logic is specific enough that an AI can follow it without clarifying questions
- [ ] Validation Rules are objectively checkable (not "looks good")
- [ ] Knowledge section contains real domain expertise, not generic advice
- [ ] YAML frontmatter is present and well-formed
- [ ] At least one concrete example is included
- [ ] File path follows convention: `skills/examples/your-skill-name/SKILL.md`

### Step 4: Submit 提交

Open a PR with the title: `Add Skill: [skill-name] ([domain])`

Example: `Add Skill: invoice-processor (Accounting)`

---

## Pull Request Process PR 流程

1. **Fork** the repo and create a branch from `main`
2. **Write** your contribution following the guidelines above
3. **Self-review**: Check for bilingual completeness, broken links, and consistency with existing docs
4. **Submit** a PR with a clear title and description of what you're adding/changing
5. **Respond** to review feedback — we may suggest edits for consistency or clarity

---

## Code of Conduct 行為準則

Be respectful. This is a learning-oriented community. We welcome disagreement on ideas but not personal attacks. Contributions from all backgrounds and experience levels are valued — this framework was built specifically to be accessible to non-engineers.

請尊重他人。這是一個以學習為導向的社群。我們歡迎對想法的不同意見，但不接受人身攻擊。我們重視來自所有背景和經驗水平的貢獻——這個框架本身就是為非工程師也能理解而建構的。

---

## Questions? 問題？

If you're not sure whether something is worth contributing, or how to approach it — just open an Issue and ask. We'd rather have the conversation than miss the contribution.

如果你不確定某個內容是否值得貢獻，或不知道如何著手——直接開 Issue 來問。我們寧可多一次對話，也不想錯過好的貢獻。
