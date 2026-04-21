# Level 3: Skill Building — Where Your Expertise Becomes Reusable
# Level 3：技能建構——你的專業知識變得可重用

> *"An engineer can make AI work. Only you can make AI work YOUR way."*
> *「工程師能讓 AI 運作。只有你能讓 AI 按你的方式運作。」*

---

## What This Level Covers 這一級涵蓋什麼

At Level 3, you stop giving AI ad-hoc instructions and start building **reusable workflow definitions** — Skills. A Skill is a Markdown file that captures your process, your validation criteria, your domain knowledge, and your quality standards. Once written, any AI system can follow it consistently, every time.

在 Level 3，��不再給 AI 臨時指令，而是開始建構**可重用的工作流程定義**——Skills。一個 Skill 是一份 Markdown 檔案，捕捉你的流程、你的驗證標準、你的領域知識和你的品質標準。一旦寫好，任何 AI 系統都能一致地遵循，每一次。

**This is the level where non-engineers become the most important builders.** The bottleneck is no longer technical — it's domain knowledge. And that's what you have.

**這是非工程師成為最重要建構者的級別。** 瓶頸不再是技術——而是領域知識。而那正是你擁有的。

---

## Your First Skill — Three Paths 你的第���個 Skill——三條路徑

### Path A: Guided Discovery 引導式發現

If you're not sure you can do this, start with the [Skill Self-Discovery](../../skills/skill-self-discovery/SKILL.md) exercise. It asks seven questions about your everyday work and reveals that your answers already form a complete Skill. Takes 5 minutes. Zero jargon.

如果你不確定自己能不能做���，從[技能自我��現](../../skills/skill-self-discovery/SKILL.md)練習開始。它問七個關於日常工作的問題，然後揭示你的答案已經形成一個完整的 Skill。5 分鐘。零術語。

### Path B: Extract from a Conversation 從對話中提取

If you've already been working with AI on a task and have a long, messy conversation, use [Conversation-to-Skill](../../skills/conversation-to-skill/SKILL.md). It analyzes your chat, extracts the workflow, and structures it into a Skill.

如果你已經在和 AI 合作一個任務，有一段冗長混亂的對話，用 [Conversation-to-Skill](../../skills/conversation-to-skill/SKILL.md)。它分析你的對話、���取工作流程，並結構化為一個 Skill。

### Path C: Build Deliberately 刻意建構

If you know exactly what workflow you want to capture, use the [Skill Builder](../../skills/skill-builder/SKILL.md). It walks you through the seven components with role-specific questions adapted to your domain.

如果你確切知道要捕捉什麼工作流程���用 [Skill Builder](../../skills/skill-builder/SKILL.md)。它帶你走過七個組件，用適應你領域的角色特定問題。

---

## The Seven Components — In Plain Language 七大組件——���白話文

Every Skill has the same seven components. Here they are, stripped of all jargon:

每個 Skill 都有同樣的七個組件。以下是去除所有���語的版本：

| # | Component 組件 | In Plain Language 白話文 | Your Equivalent 你的對應 |
|---|---|---|---|
| 1 | Identity 身份 | What is this workflow and who is it for? | "I do expense reports for our department" |
| 2 | Trigger 觸發 | What tells you to start? | "When receipts come in before the 5th" |
| 3 | Process 流程 | What steps do you follow? | "First I check amounts, then categories..." |
| 4 | I/O 輸入輸出 | What do you need, what do you produce? | "I need receipts + form; I produce the ledger" |
| 5 | Validation 驗證 | How do you know it's done right? | "Amounts must match exactly" |
| 6 | Knowledge 知識 | What tricks do you know? | "Dept. B always miscategorizes transport" |
| 7 | Composition 組合 | What connects to this? | "Output feeds into the monthly report" |

That's it. If you can answer these seven questions about your work, you can build a Skill.

就這樣。如果你能回答這七個關於工作的問題，你就能建一個 Skill。

---

## Writing Your SKILL.md 撰寫你的 SKILL.md

A SKILL.md is just a text file with headings. The minimum viable Skill:

SKILL.md 只是一個帶標題的文字檔。最小可行 Skill：

```markdown
---
name: my-task-name
description: >
  What this Skill does and when to use it.
---

# My Task Name

## When to Use
- [Trigger 1]
- [Trigger 2]

## Process
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Input
- [What you need to start]

## Output
- [What you produce when done]

## Quality Checks
- [How to verify the output is correct]

## Things to Know
- [Domain knowledge, shortcuts, exceptions]
```

Save this in a `skills/my-task-name/SKILL.md` file, and any AI system that supports Skills can follow it.

把這個存在 `skills/my-task-name/SKILL.md` 檔案裡，任何支援 Skills 的 AI 系統都能遵循它。

---

## What Makes a Good Skill 什麼是好的 Skill

### Specific, Not Generic 具體，不要泛泛

❌ "Review documents for errors"
✅ "Review government project quarterly reports for: KPI accuracy against contract targets, budget utilization percentages matching accounting system, photo captions in both Chinese and English, executive summary under 500 words"

### Your Words, Not Jargon 你的話，不要術語

Write it exactly how you'd explain to a new colleague. If you say "核銷" in real life, write "核銷" — not "expense reconciliation." The AI will understand both; your future self will understand your words better.

完全按照你向新同事解釋的方式寫。如果你在現實中說「核銷」，就寫「核銷」。

### Validation That's Checkable 可檢查的驗證

❌ "Make sure it looks good"
✅ "All amounts must match to the cent. Every table must have a title. Budget utilization must not exceed 100% for any line item."

### Knowledge That Only You Have 只有你有的知識

The Knowledge section is what makes your Skill invaluable. This is the stuff no AI can figure out from training data:

知識庫部分是讓你的 Skill 無價的地方。這是 AI 從訓練資料中無法自己搞清楚的：

- "Department B always miscategorizes transportation as supplies" B 部門總���把交通費歸成雜支
- "The system crashes if you enter more than 50 items at once, so batch in groups of 30" 系統一次超過 50 筆會當掉，所以分成 30 筆一批
- "Client X prefers narrative format, not bullet points" 客戶 X 偏好敘述格式，不要列點

---

## Exercises 練習

### Exercise 1: The 15-Minute Skill 15 分鐘 Skill

Pick one task you do at least monthly. Set a timer for 15 minutes. Write a SKILL.md using the template above. Don't aim for perfection — aim for "a new colleague could follow this." You can refine later.

選一件你至少每月做一次的任務。設定 15 分鐘計時器。用上面的模板寫一份 SKILL.md。不追求完美——追求「新同事能跟著做」。之後可以精煉。

### Exercise 2: The Test Run 試跑

Give your SKILL.md to an AI (Claude Code, Cowork) along with the required input. Ask it to follow the Skill step by step. Watch where it succeeds and where it goes wrong. The errors tell you what your Skill is missing — add that to the Knowledge section.

把你的 SKILL.md 和所需輸入給 AI（Claude Code、Cowork）。要求它一步步遵循 Skill。看它哪裡成功、哪裡出錯。錯誤告訴你 Skill 缺什麼——把那些加到知識庫。

### Exercise 3: The Knowledge Audit 知識審計

Look at your completed Skill. Now ask yourself: "What would go wrong if a smart person who's never done this job tried to follow these steps?" Write down every edge case, exception, and trick you can think of. Add them all to the Knowledge section.

看看你完成的 Skill。然後問自己：「如果一個聰明但從沒做過這份工作的人試著遵循這些步驟，會出什麼問題？」寫下你能想到的每個邊界案例、例外和訣竅。全部加到知識庫。

---

## See Real Examples 看真實範例

Six ready-to-use Skills are included in the [Example Gallery](../../skills/examples/):

| Skill | Type | What It Does |
|---|---|---|
| [meeting-notes-to-actions](../../skills/examples/meeting-notes-to-actions/) | Transform | Notes → action items with owners |
| [document-reviewer](../../skills/examples/document-reviewer/) | Process | Four-pass systematic review |
| [research-and-summarize](../../skills/examples/research-and-summarize/) | Process | Structured research with sourcing |
| [project-status-tracker](../../skills/examples/project-status-tracker/) | Orchestration | Multi-source → unified dashboard |
| [accounting-reconciler](../../skills/examples/accounting-reconciler/) | Transform | Financial data → reconciliation report |
| [content-pipeline](../../skills/examples/content-pipeline/) | Process | Brief → published content |

Read them. Study the structure. Notice how each one uses the same seven components but adapts them to a specific domain.

---

## When You've Outgrown Level 3 當你超越 Level 3 的時候

You'll know it's time for Level 4 when:

- You have multiple Skills that need to work together 你有多個 Skills 需要一起運作
- You need AI to remember what happened in previous sessions 你需要 AI 記得先前的工作階段
- You want a persistent AI that manages a project over weeks 你想要一個跨週管理專案的持續性 AI
- You're coordinating a workflow that's too complex for a single Skill 你在協調一個對單一 Skill 來說太複雜的工作流程

These are signals for [Level 4: Agent Orchestration](level-4-agents.md).

---

*Previous: [Level 2: Tool Use ←](level-2-tools.md)*
*Next: [Level 4: Agent Orchestration →](level-4-agents.md)*
