# Quick Start — 5 Minutes to Your First Skill
# 快速入門——5 分鐘建立你的第一個 Skill

> *You don't need to read the docs. You don't need to understand the architecture. Just follow these steps.*
> *你不需要讀文件。不需要理解架構。只要跟著這些步驟。*

---

## Install 安裝

### Option A: Clone and Install 複製並安裝

```bash
git clone https://github.com/ahnchen1983/agentic-substrate.git
cd agentic-substrate
./install.sh
```

### Option B: Manual Copy 手動複製

Copy the `skills/` folder into your Claude Code project's `.claude/skills/` directory, or into your Cowork workspace.

把 `skills/` 資料夾複製到你的 Claude Code 專案的 `.claude/skills/` 目錄，或你的 Cowork 工作區。

### Option C: Cowork Plugin 安裝為 Cowork 插件

If this plugin is available in the Cowork marketplace, install it directly from there.

如果這個插件在 Cowork marketplace 上可用，直接從那裡安裝。

---

## Your First 5 Minutes 你的前五分鐘

### Path 1: "I'm Not Technical" 路徑一：「我不懂技術」

Open Claude Code or Cowork and say:

打開 Claude Code 或 Cowork，說：

> **"I want to discover my Skills"**
> **「我想發現我的 Skills」**

The **Skill Self-Discovery** Skill will activate. It asks you seven questions about your everyday work — no tech knowledge needed. At the end, you'll see that you already know how to build an AI Skill. The whole exercise takes about 5 minutes.

**Skill Self-Discovery** 會啟動。它問你七個關於日常工作的問題——不需要技術知識。最後，你會看到你已經會建 AI Skill 了。整個練習大約 5 分鐘。

### Path 2: "I Have a Messy Chat I Want to Organize" 路徑二：「我有一段亂七八糟的對話想整理」

If you've been in a long conversation and things are getting chaotic, say:

如果你在一段長對話中，事情變得混亂，說：

> **"Help me organize this conversation into a work record"**
> **「幫我把這段對話整理成工作紀錄」**

The **Conversation-to-Skill** Skill will analyze your chat, extract the key decisions and progress, and show you that your work record is already 80% of a reusable Skill.

**Conversation-to-Skill** 會分析你的對話，提取關鍵決策和進度，然後讓你看到你的工作紀錄已經是一個可重用 Skill 的 80%。

### Path 3: "I Want to Build a Skill Right Now" 路徑三：「我現在就想建一個 Skill」

If you know what you want, go straight to building:

如果你知道你要什麼，直接開建：

> **"I want to build a Skill for [your task]"**
> **「我想為 [你的任務] 建一個 Skill」**

The **Skill Builder** will guide you through the process step by step, adapting its questions to your role and domain.

**Skill Builder** 會一步步引導你，根據你的角色和領域調整問題。

### Path 4: "Just Show Me What's Available" 路徑四：「讓我看看有什麼」

Try any of these ready-to-use Skills by giving them the right input:

給它們正確的輸入，試試這些即用 Skills：

| Say this 這樣說 | Skill that activates 啟動的 Skill |
|---|---|
| Share meeting notes + "extract action items" | **Meeting Notes to Actions** |
| Share a document + "review this before I send it" | **Document Reviewer** |
| "Research [topic] for me" | **Research and Summarize** |
| "What's the project status?" + share project data | **Project Status Tracker** |
| Share two financial datasets + "reconcile these" | **Accounting Reconciler** |
| "I need to write a blog post about [topic]" | **Content Pipeline** |

---

## What Happens Next 接下來會怎樣

After trying a Skill, you'll naturally start thinking: "I have a workflow at work that could be a Skill too." That's the moment. Use the **Skill Builder** to capture it.

試了一個 Skill 之後，你自然會開始想：「我工作上也有一個流程可以變成 Skill。」那就是那個時刻。用 **Skill Builder** 來捕捉它。

The learning progression is:

學習進程是：

```
Try a Skill →  Build your first Skill  →  Build Skills for your team
試一個 Skill →  建你的第一個 Skill      →  為你的團隊建 Skills
```

---

## Learn More 深入了解

| Want to... 想要... | Read 閱讀 |
|---|---|
| Understand the architecture 理解架構 | [Core Architecture](docs/01-foundations/agentic-substrate.md) |
| See the big picture 看全貌 | [Interactive Visualization](index.html) |
| Learn how Skills work 了解 Skill 怎麼運作 | [Skill Anatomy](docs/01-foundations/skill-anatomy.md) |
| Understand the learning path 了解學習路徑 | [Learning Path](docs/04-curriculum/learning-path.md) |
| Hear Claude's perspective 聽 Claude 的觀點 | [A Letter from the Inside](docs/03-claude-case-study/claude-architecture.md) |
| See how this compares to others 看跟其他框架的比較 | [Landscape Analysis](docs/02-architecture/landscape.md) |

---

*Built by [Ahn Chen](https://github.com/ahnchen1983) & [Claude (Opus 4.6)](https://claude.ai)*
*由 Ahn Chen 和 Claude (Opus 4.6) 共同建構*
