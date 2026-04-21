# Level 4: Agent Orchestration — AI as a Colleague
# Level 4：Agent 調度——AI 作為同事

> *"An Agent doesn't just do what you ask. It remembers, plans, and follows up — like a colleague who never forgets."*
> *「Agent 不只做你要求的。它記得、規劃、跟進——像一個永遠不會忘記的同事。」*

---

## What This Level Covers 這一級涵蓋什麼

At Level 4, AI moves from executing individual tasks to **managing ongoing work across time**. An Agent has identity, memory, and the ability to orchestrate multiple Skills to achieve complex, multi-session objectives. When it starts a new session, it reads its state and continues where it left off.

在 Level 4，AI 從執行個別任務進化到**跨時間管理持續性工作**。一個 Agent 有身份、記憶，以及調度多個 Skills 來達成���雜、多工作階段目標的能力。當它開始新的工作階段，它讀取狀態並從上次離開的地方繼續。

This is the full five-layer stack in action. Every layer is active.

這是完整的五��堆疊在運作。每一層都是活躍的。

---

## What Makes an Agent Different from a Skill Agent 和 Skill 有什麼不同

| Dimension 面向 | Skill | Agent |
|---|---|---|
| **Duration 持續時間** | Single session 單一工作階段 | Multiple sessions over days/weeks 跨天/週的多個工作階段 |
| **Memory 記憶** | None between sessions 工作階段之間沒有 | Persistent — reads and writes state 持久——讀寫狀態 |
| **Identity 身份** | Defined by its SKILL.md 由 SKILL.md 定義 | Has a SOUL.md — personality, boundaries, values 有 SOUL.md |
| **Scope 範圍** | One task, one workflow 一個任務、一個流程 | Multiple tasks, multiple Skills 多個任務、多個 Skills |
| **Initiative 主動性** | Responds to triggers 回應觸發 | Can proactively flag issues, track deadlines 能主動標記問題、追蹤截止日 |

---

## The Agent Memory System Agent 記憶系統

An Agent's memory is a set of Markdown files in a Git repository — human-readable, version-controlled, and accessible to both the AI and the team. This is the **Repo-as-Memory** pattern from [Memory & State](../02-architecture/memory-and-state.md).

Agent 的記憶是 Git repository 中的一組 Markdown 檔案——人類可讀、版本控制、AI 和團隊都能存取。這是[記憶與狀態](../02-architecture/memory-and-state.md)中的 **Repo-as-Memory** 模式。

### Core Memory Files 核心記憶檔案

```
project-repo/
├── SOUL.md              ← Who the Agent is 身份定義
├── DAILY.md             ← Current state snapshot 當前狀態快照
├── MILESTONES.md        ← Timeline with status 帶狀態的時間線
├── decisions/           ← Why decisions were made 決策紀錄
│   ├── 001-chose-vendor-a.md
│   └── 002-timeline-change.md
├── memory-index.md      ← Where to find what 索引
└── skills/              ← Reusable workflows 可重用的工作流程
    ├── weekly-report/
    └── client-update/
```

### The Session Cycle 工作階段循環

Every time the Agent starts a new session:

```
Start Session
    │
    ▼
Read State ──→ SOUL.md + DAILY.md + MILESTONES.md
    │           "Who am I? Where are we? What's next?"
    ▼
Understand ──→ Parse current priorities, blockers, deadlines
    │
    ▼
Execute ────→ Run relevant Skills, produce deliverables
    │
    ▼
Validate ───→ Check outputs against criteria
    │
    ▼
Write Back ─→ Update DAILY.md, decision records, milestones
    │
    ▼
End Session ─→ State is preserved for next time
```

The key insight: **the Agent doesn't rely on conversation history.** It relies on files. Every session starts from scratch but reads its state from the repo. This means the Agent works even if the previous conversation was deleted, the model was changed, or a different person continues the work.

關鍵洞見：**Agent 不依賴對話歷史。** 它依賴���案。每個工作階��從頭開���但從 repo 讀取狀態。這意味著即使之前��對話被刪除、模型被更換、或不同的人繼續工作，Agent 也能運作。

---

## SOUL.md — The Agent's Identity Agent 的身份

A SOUL.md defines who the Agent is. Example:

```markdown
# Project Agent: Cultural Affairs Q3

## Identity
I am the project management agent for the Q3 Cultural Affairs initiative.
I track deliverables, flag risks, and produce status reports.

## Boundaries
- I do NOT make budget decisions — I flag them for the PM
- I do NOT communicate with the client directly
- I DO proactively alert when deadlines are at risk

## Communication Style
- Internal reports: direct, data-driven, flag problems early
- Client-facing drafts: formal but warm, emphasize achievements

## Skills I Use
- weekly-report
- client-update
- meeting-notes-to-actions
- document-reviewer
```

---

## Practical Agent Patterns 實用 Agent 模式

### Pattern 1: The Project Tracker 專案追蹤器

An Agent that maintains project state, tracks milestones, and produces weekly status reports. It reads task data, compares against the plan, flags delays, and drafts the report for human review.

### Pattern 2: The Research Assistant 研究助理

An Agent that maintains a research knowledge base over time. Each session, it can incorporate new sources, update its synthesis, and maintain a living summary document that grows as the research progresses.

### Pattern 3: The Team Coordinator 團隊協調者

An Agent that reads meeting notes, extracts action items, tracks their completion status, and sends reminders. Over multiple sessions, it builds a picture of who does what, who's often late, and what typically blocks progress.

### Pattern 4: The Document Pipeline 文件流水線

An Agent that manages a document through its lifecycle — from draft through review, revision, formatting, and final approval. It remembers review feedback across sessions and ensures nothing is lost between rounds.

---

## Who Builds Level 4 誰建構 Level 4

Level 4 typically requires collaboration:

Level 4 通常需要協作：

**The domain expert** designs:
- What the Agent should track 追蹤什麼
- What decisions it should escalate 什麼決策要升級
- What quality standards to enforce 執行什麼品質標準
- What the memory structure should look like 記憶結構應該長什麼樣

**The engineer** sets up:
- The Git repository structure Git repository 結構
- The agent loop (session start → read → execute → write → end) Agent 迴圈
- Deployment and scheduling 部署和排程
- Integration with external systems 與外部系統的整合

**But this balance is shifting.** Products like Cowork and Claude Code are making it increasingly possible for non-engineers to design and run Agent workflows with minimal technical setup. The trajectory is clear: the domain expert's role grows while the engineering barrier shrinks.

**但這個平衡正在轉移。** 像 Cowork 和 Claude Code 這樣的產品正讓非工程師越來越有可能用最少的技術設置來設計和執行 Agent 工作流程。

---

## Exercises 練習

### Exercise 1: Design a SOUL.md 設計一份 SOUL.md

Pick a project or ongoing responsibility. Write a SOUL.md for an Agent that would manage it. Define: identity, boundaries, communication style, and Skills it would use. Don't build it — just design it. The design exercise alone clarifies your thinking about the workflow.

### Exercise 2: Map the Memory 繪製記憶地圖

For the same project, sketch the memory structure. What files would the Agent need? What would DAILY.md contain? What decisions should be recorded? What milestones matter? This exercise reveals how much implicit knowledge lives in your head vs. in written documents.

### Exercise 3: Simulate a Session 模擬一個工作階段

Give your SOUL.md and a sample DAILY.md to an AI. Ask it to "read your state and decide what to do next." Watch what it prioritizes, what it misses, and what it asks about. This tells you where your memory design needs more detail.

---

## Further Reading 延伸閱讀

| Topic 主題 | Document 文件 |
|---|---|
| Memory architecture 記憶架構 | [Memory & State](../02-architecture/memory-and-state.md) |
| Skill composition ��能組合 | [Skill Composition](../02-architecture/skill-composition.md) |
| Real implementation 真實實作 | [Claude Architecture Case Study](../03-claude-case-study/claude-architecture.md) |
| Design patterns 設計模式 | [Agentic Design Patterns](../02-architecture/agentic-design-patterns.md) |

---

## The Bigger Picture 更大的圖景

Level 4 is where AI stops being a feature and starts being a paradigm. An Agent isn't just a smarter chatbot — it's a new kind of software entity that combines human expertise (captured in Skills) with machine persistence (captured in memory) to produce outcomes that neither could achieve alone.

Level 4 是 AI 不再只是一個功能而開始成為一個典範的地方。Agent 不只是一個更聰明的聊天機器人——它是一種新的軟體實體，結合人類專業知識（捕捉在 Skills 中）和機器持久性（捕捉在記憶中），產出兩者單獨都無法達成的成果。

This is the vision of the [Agentic Substrate](../01-foundations/agentic-substrate.md) framework: a world where the unit of software isn't an app or a service, but a Skill — and where Agents orchestrate those Skills to handle the full complexity of real work.

這是 [Agentic Substrate](../01-foundations/agentic-substrate.md) 框架的願景：一個軟體單元不是 app 或 service，而是 Skill 的世界——Agent 調度這些 Skills 來處理真實工作的全���複雜性。

You've now seen the complete journey: from conversation to tools to Skills to Agents. The question isn't whether this future is coming — it's whether you'll be building it or watching it happen.

你現在已經���到了���整的旅程：從對話到工具到 Skills 到 Agents。問題不是這個未來是否會來——而是你會建構它還是旁觀它發生。

---

*Previous: [Level 3: Skill Building ←](level-3-skills.md)*
*Back to: [Learning Path Overview](learning-path.md)*
