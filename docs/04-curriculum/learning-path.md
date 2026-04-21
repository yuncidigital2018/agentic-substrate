# Learning Path: From Chat to Agent
# 學習路徑：從聊天到 Agent

> *"You don't need to learn everything at once. You need to understand which level you're at — and what the next level looks like."*
> *「你不需要一次學會所有東西。你需要理解你在哪一級——以及下一級長什麼樣子。」*

---

## Who This Is For ── 這是給誰的

This learning path is designed for **everyone who uses AI for work** — not just engineers. If you've ever typed a question into ChatGPT, you're already at Level 1. This document shows you the complete journey from there to designing your own Agent workflows.

這個學習路徑是為**所有使用 AI 工作的人**設計的——不只是工程師。如果你曾經在 ChatGPT 裡打過一個問題，你已經在 Level 1 了。這份文件展示從那裡到設計自己的 Agent 工作流程的完整旅程。

Each level builds on the previous one. You don't skip levels — you grow through them. And the most important insight: **the jump from Level 1 to Level 2 is technical; the jump from Level 2 to Level 3 is not.** Level 3 is where domain experts — project managers, marketers, accountants, anyone who knows their work deeply — become the most important people in the room.

每一級建立在前一級之上。你不會跳級——你會逐漸成長。最重要的洞見：**從 Level 1 到 Level 2 的跳躍是技術性的；從 Level 2 到 Level 3 的跳躍不是。** Level 3 是領域專家——專案經理、行銷人員、會計、任何深入了解自己工作的人——成為房間裡最重要的人的地方。

---

## The Four Levels at a Glance ── 四個等級一覽

```
Level 4: Agent Orchestration 代理調度
"I design persistent AI workflows that manage projects across time"
「我設計跨時間管理專案的持續性 AI 工作流程」
    ▲
    │  You add: Memory + Identity + Multi-session continuity
    │  你加入：記憶 + 身份 + 多工作階段連續性
    │
Level 3: Skill Building 技能建構
"I create reusable AI workflows for my domain"
「我為我的領域建立可重用的 AI 工作流程」
    ▲
    │  You add: Structured process + Validation + Reusability
    │  你加入：結構化流程 + 驗證 + 可重用性
    │
Level 2: Tool Use 工具使用
"I use AI to act on files, data, and systems"
「我用 AI 對檔案、數據和系統採取行動」
    ▲
    │  You add: External tools (files, code, web, APIs)
    │  你加入：外部工具（檔案、程式碼、網路、API）
    │
Level 1: Conversation 對話
"I talk to AI and get responses"
「我和 AI 對話並得到回應」
```

Most people are at Level 1. Most of the value is at Level 3 and 4.

大多數人在 Level 1。大多數價值在 Level 3 和 4。

---

## Level 1: Conversation — The Starting Point ── 對話——起點

### What it looks like 看起來像什麼

You open ChatGPT, Claude, or Gemini. You type a question. You get an answer. You might have a back-and-forth conversation. When you close the tab, the interaction is over.

你打開 ChatGPT、Claude 或 Gemini。你打一個問題。你得到一個答案。你可能有來回的對話。當你關閉分頁，互動就結束了。

### What you're actually doing 你實際上在做什麼

You're using **Layer 1 (LLM) + Layer 5 (Interface)** of the Five-Layer Model. A brain behind a chat window. No tools. No Skills. No memory. No persistence.

你在使用五層模型的**第一層（LLM）+ 第五層（介面）**。聊天視窗後面的大腦。沒有工具。沒有 Skills。沒有記憶。沒有持久性。

### What's good about it 好處

- Zero setup — works instantly 零設置——立即可用
- Great for brainstorming, Q&A, learning, and drafting 非常適合腦力激盪、問答、學習和起草
- Low risk — conversation is ephemeral 低風險——對話是短暫的

### What's limiting 局限

- Every session starts from zero 每次工作階段都從零開始
- AI can't access your files, your data, or your systems AI 不能存取你的檔案、數據或系統
- Output quality depends entirely on how you phrase your question 輸出品質完全取決於你如何措辭問題
- No accumulated expertise — you re-explain context every time 沒有累積的專業知識——你每次都重新解釋背景

### The signal you're ready for Level 2 你準備好進入 Level 2 的訊號

You find yourself saying: "I wish it could just look at my file" or "I keep explaining the same thing every time" or "The answer is good but I need it to actually *do* something."

你發現自己在說：「我希望它能直接看我的檔案」或「我每次都在解釋同樣的事情」或「答案很好但我需要它真正*做*一些事情。」

### Mapping to the Five-Layer Model 對應到五層模型

```
Level 1 uses:
L1 ●  LLM Computation    ← The brain, doing the thinking
L2 ○  Tools              ← No hands
L3 ○  Skills             ← No expertise
L4 ○  Agent              ← No memory
L5 ●  Interface          ← The chat window
```

---

## Level 2: Tool Use — The Capability Jump ── 工具使用——能力的跳躍

### What it looks like 看起來像什麼

You use Claude Code, Cowork, Cursor, or any AI system that can access files, run code, search the web, and interact with external services. You don't just talk to AI — you tell it to **do things**.

你使用 Claude Code、Cowork、Cursor 或任何能存取檔案、執行程式碼、搜尋網路和與外部服務互動的 AI 系統。你不只是和 AI 對話——你告訴它去**做事情**。

"Read this spreadsheet and summarize the key trends."
「讀取這份試算表並摘要關鍵趨勢。」

"Search the web for the latest regulations on this topic."
「搜尋網路上關於這個主題的最新法規。」

"Create a chart from this data and save it as a PNG."
「從這些數據建立一個圖表並存為 PNG。」

### What changes 什麼改變了

The AI goes from **thinking** to **doing**. It's no longer just generating text — it's reading your actual files, writing real documents, executing real code. The output is not a chat message; it's a deliverable.

AI 從**想**變成**做**。它不再只是生成文字——它在讀取你的實際檔案、撰寫真實的文件、執行真實的程式碼。輸出不是聊天訊息；而是一份交付物。

### What you're actually doing 你實際上在做什麼

You're adding **Layer 2 (Tools & Protocols)** to the stack. The brain now has hands.

你在堆疊中加入了**第二層（工具與協議）**。大腦現在有了手。

### The honest challenge 誠實的挑戰

This level often requires some technical comfort. You might need to install Claude Code, configure MCP servers, or navigate a command line. This is the one level where engineering knowledge genuinely helps.

這一級通常需要一些技術熟悉度。你可能需要安裝 Claude Code、設定 MCP servers 或操作命令列。這是工程知識真正有幫助的一級。

But here's the good news: **you only need to cross this bridge once.** Products like Cowork are specifically designed to give you Level 2 capabilities without requiring engineering skills. The industry is actively working to lower this barrier.

但好消息是：**你只需要過這座橋一次。** 像 Cowork 這樣的產品專門設計來在不需要工程技能的情況下給你 Level 2 的能力。產業正積極降低這個門檻。

### The signal you're ready for Level 3 你準備好進入 Level 3 的訊號

You find yourself saying: "I keep telling it the same steps every time" or "The output is close but it doesn't follow our specific process" or "I want to save this workflow so I don't have to explain it again."

你發現自己在說：「我每次都在告訴它同樣的步驟」或「輸出很接近但它沒有遵循我們的具體流程」或「我想儲存這個工作流程，這樣我就不用再解釋一次。」

### Mapping to the Five-Layer Model 對應到五層模型

```
Level 2 uses:
L1 ●  LLM Computation    ← The brain
L2 ●  Tools              ← Now has hands (files, code, web)
L3 ○  Skills             ← Still no reusable expertise
L4 ○  Agent              ← Still no memory
L5 ●  Interface          ← CLI, Desktop, or IDE
```

---

## Level 3: Skill Building — Where Non-Engineers Become Essential ── 技能建構——非工程師成為關鍵的地方

### What it looks like 看起來像什麼

You create a SKILL.md file — a Markdown document that defines a complete workflow: when to trigger it, what inputs it needs, what steps to follow, what to validate, what to produce. The next time you (or anyone) needs this workflow, the AI follows the Skill instead of improvising.

你建立一個 SKILL.md 檔案——一份 Markdown 文件，定義一個完整的工作流程：何時觸發、需要什麼輸入、遵循什麼步驟、驗證什麼、產出什麼。下一次你（或任何人）需要這個工作流程時，AI 遵循 Skill 而非即興發揮。

### Why this is the most important level 為什麼這是最重要的一級

**This is where everything changes.** Not because the technology is more advanced — but because the bottleneck shifts.

**這是一切改變的地方。** 不是因為技術更先進——而是因為瓶頸轉移了。

At Level 1 and 2, the bottleneck is technical — can the AI access tools? Can it execute code? Engineers solve this.

在 Level 1 和 2，瓶頸是技術性的——AI 能存取工具嗎？能執行程式碼嗎？工程師解決這個。

At Level 3, the bottleneck is **domain knowledge** — does the AI know the right process? Does it understand the validation criteria? Does it know the institutional requirements? **Engineers can't solve this.** Only the people who do the work every day can.

在 Level 3，瓶頸是**領域知識**——AI 知道正確的流程嗎？理解驗證標準嗎？知道機構的要求嗎？**工程師解決不了這個。** 只有每天做這些工作的人才能。

This is why the Agentic Substrate framework insists that non-engineers are not "users" — they're **Layer 3 builders**. The accountant who knows the reconciliation process, the project manager who knows the review workflow, the marketer who knows the content pipeline — each one holds expertise that no amount of LLM training data can replace.

這就是為什麼 Agentic Substrate 框架堅持非工程師不是「使用者」——他們是**第三層建構者**。知道對帳流程的會計、知道審查工作流程的專案經理、知道內容管線的行銷人員——每一個人都掌握著再多 LLM 訓練資料也無法取代的專業知識。

### What you're actually doing 你實際上在做什麼

You're encoding your expertise into a format that AI can execute. A Skill is your knowledge, written down, made reusable.

你在將你的專業知識編碼成 AI 能執行的格式。一個 Skill 就是你的知識，被寫下來，變得可重用。

### You don't need to code 你不需要寫程式

A SKILL.md is a Markdown file — plain text with headings, bullet points, and descriptions. If you can write an email, you can write a Skill. The structure is:

SKILL.md 是一份 Markdown 檔案——帶標題、項目符號和描述的純文字。如果你會寫電子郵件，你就會寫 Skill。結構是：

```markdown
# My Skill Name

## Description
What this skill does and when to use it.

## Trigger
When should this skill activate?

## Process
Step 1: ...
Step 2: ...
Step 3: ...

## Validation
How do I know the output is correct?

## Output
What does the final deliverable look like?
```

That's it. You're describing your job. In plain language.

就這樣。你在描述你的工作。用平實的語言。

### Try it now 現在試試

If this sounds abstract, try the [Skill Self-Discovery](../../skills/skill-self-discovery/SKILL.md) exercise. It asks you seven natural questions about your everyday work — and then reveals that your answers are already a complete Skill definition. No jargon. No code. Just your expertise, structured.

如果這聽起來很抽象，試試[技能自我發現](../../skills/skill-self-discovery/SKILL.md)練習。它問你七個關於日常工作的自然問題——然後揭示你的答案已經是一個完整的 Skill 定義。沒有術語。沒有程式碼。只有你的專業知識，被結構化了。

Also read: [You Already Know How to Build a Skill](you-already-know.md) — the full story of why the gap between you and AI is vocabulary, not capability.

也讀讀：[你已經會建 Skill 了](you-already-know.md)——關於你和 AI 之間的差距是詞彙而非能力的完整故事。

### The signal you're ready for Level 4 你準備好進入 Level 4 的訊號

You find yourself saying: "I have multiple Skills that need to work together" or "I need the AI to remember what happened last session" or "I want an AI that manages this project over weeks, not minutes."

你發現自己在說：「我有多個 Skills 需要一起運作」或「我需要 AI 記得上次工作階段發生的事」或「我想要一個管理這個專案數週而非數分鐘的 AI。」

### Mapping to the Five-Layer Model 對應到五層模型

```
Level 3 uses:
L1 ●  LLM Computation    ← The brain
L2 ●  Tools              ← The hands
L3 ●  Skills             ← Now has reusable expertise
L4 ○  Agent              ← Still no persistent memory
L5 ●  Interface          ← Any interface works
```

---

## Level 4: Agent Orchestration — The Full Stack ── Agent 調度——完整堆疊

### What it looks like 看起來像什麼

You design an AI system that persists across sessions. It has an identity (SOUL.md), knows the current project state (DAILY.md), tracks progress over time (MILESTONES.md), and orchestrates multiple Skills to achieve complex, multi-week objectives. When it starts a new session, it reads its memory and picks up where it left off.

你設計一個跨工作階段持續的 AI 系統。它有身份（SOUL.md）、知道當前專案狀態（DAILY.md）、追蹤長期進度（MILESTONES.md），並調度多個 Skills 來達成複雜的、跨週目標。當它開始新的工作階段，它讀取記憶並從上次離開的地方繼續。

### What changes 什麼改變了

The AI goes from being a **tool you use** to a **colleague you work with**. It doesn't just execute tasks — it maintains context, tracks decisions, catches inconsistencies, and grows more capable over time as its understanding of the project deepens.

AI 從**你使用的工具**變成**你一起工作的同事**。它不只是執行任務——它維持脈絡、追蹤決策、捕捉不一致，並隨著對專案理解的加深而隨時間越來越有能力。

### What you're actually doing 你實際上在做什麼

You're adding **Layer 4 (Agent)** — memory, identity, and multi-session orchestration. The full five-layer stack is now in play.

你在加入**第四層（Agent）**——記憶、身份和多工作階段調度。完整的五層堆疊現在全部啟動。

### The building blocks 建構要件

Level 4 combines everything from the previous levels plus:

Level 4 結合了前面所有等級的內容加上：

| Component 組件 | Purpose 目的 | Format 格式 |
|---|---|---|
| **SOUL.md** | Agent identity — who it is, how it behaves Agent 身份——它是誰、如何表現 | Markdown |
| **DAILY.md** | Current state snapshot — what's done, what's next 當前狀態快照——什麼完成了、接下來做什麼 | Markdown |
| **MILESTONES.md** | Timeline with status markers 帶狀態標記的時間線 | Markdown |
| **Decision records** | Why decisions were made 為什麼做了這些決策 | Markdown in `decisions/` |
| **Memory index** | Where to find what 在哪裡找什麼 | Markdown |
| **Git repository** | Version history + collaboration 版本歷史 + 協作 | Git |

All Markdown. All human-readable. All version-controlled. The technical infrastructure is minimal — the real work is **designing the memory structure and the workflow**.

全部是 Markdown。全部人類可讀。全部有版本控制。技術基礎設施很少——真正的工作是**設計記憶結構和工作流程**。

### Who builds Level 4 systems 誰建構 Level 4 系統

This level typically requires collaboration between domain experts and engineers. The domain expert designs the workflow, the memory structure, and the validation criteria. The engineer sets up the Git repo, the agent loop, and the deployment infrastructure. Neither can do it alone.

這一級通常需要領域專家和工程師的協作。領域專家設計工作流程、記憶結構和驗證標準。工程師設置 Git repo、Agent 迴圈和部署基礎設施。兩者都不能單獨完成。

But the balance is shifting. Products like Cowork are making Level 4 increasingly accessible without engineering setup. The trajectory is clear: **what requires an engineer today will be possible for anyone tomorrow.**

但平衡正在轉移。像 Cowork 這樣的產品正使 Level 4 越來越容易在沒有工程設置的情況下實現。軌跡很清楚：**今天需要工程師的事，明天任何人都能做到。**

### Mapping to the Five-Layer Model 對應到五層模型

```
Level 4 uses:
L1 ●  LLM Computation    ← The brain
L2 ●  Tools              ← The hands
L3 ●  Skills             ← The expertise
L4 ●  Agent              ← Now has memory and identity
L5 ●  Interface          ← Any interface works

All five layers active. Full Agentic system.
五層全部啟動。完整的代理型系統。
```

---

## The Complete Map ── 完整地圖

Here's the entire journey in one view:

這是一張一覽全程的完整地圖：

```
                            What You Can Do               What You Need        Who You Are
                            你能做什麼                      你需要什麼            你是誰
────────────────────────────────────────────────────────────────────────────────────────────────
Level 1                     Ask questions, get answers     A browser             Anyone
Conversation                問問題、得到答案                一個瀏覽器             任何人
對話
────────────────────────────────────────────────────────────────────────────────────────────────
Level 2                     Read files, write documents,   Claude Code,          Anyone with
Tool Use                    execute code, search web       Cowork, or Cursor     basic tech
工具使用                     讀檔案、寫文件、               comfort
                            執行程式碼、搜尋網路            基本技術熟悉度
────────────────────────────────────────────────────────────────────────────────────────────────
Level 3                     Create reusable workflows      Domain knowledge      Domain experts
Skill Building              that produce consistent,       + a text editor       (YOU)
技能建構                     professional output                                  領域專家
                            建立可重用的工作流程，           領域知識               （就是你）
                            產出一致的專業輸出               + 文字編輯器
────────────────────────────────────────────────────────────────────────────────────────────────
Level 4                     Design persistent AI that      Level 3 Skills        Domain experts
Agent Orchestration         manages projects over time     + memory structure    + engineers
代理調度                     設計跨時間管理專案              + Git repo            (collaboration)
                            的持續性 AI                     Level 3 的 Skills      領域專家
                                                           + 記憶結構             + 工程師
                                                           + Git repo            （協作）
────────────────────────────────────────────────────────────────────────────────────────────────
```

### The Key Insight 關鍵洞見

Notice the "Who You Are" column. Level 1 and 2 are for anyone. Level 3 shifts to **domain experts** — the people who know the work. Level 4 is a collaboration between domain experts and engineers.

注意「你是誰」那欄。Level 1 和 2 是給任何人的。Level 3 轉向**領域專家**——了解工作的人。Level 4 是領域專家和工程師之間的協作。

**The most valuable transition in this entire path is from Level 2 to Level 3.** That's where AI stops being a generic assistant and starts being a domain-specific expert. And that transition is powered by **your knowledge**, not by engineering skill.

**整條路徑中最有價值的轉變是從 Level 2 到 Level 3。** 那是 AI 從通用助理變成特定領域專家的地方。而那個轉變由**你的知識**驅動，不是由工程技能。

---

## How the Curriculum Documents Connect ── 課程文件如何串接

This learning path doesn't exist in isolation — it connects to everything else in the Agentic Substrate framework:

這個學習路徑不是孤立的——它連接到 Agentic Substrate 框架中的所有其他內容：

```
Start Here 從這裡開始
│
├── "You Already Know" (you-already-know.md)
│    Why the gap is vocabulary, not capability
│    為什麼差距是詞彙，不是能力
│    → Builds confidence for Level 3
│      為 Level 3 建立信心
│
├── Skill Self-Discovery (skills/skill-self-discovery/)
│    Interactive exercise: discover you can already build Skills
│    互動練習：發現你已經能建構 Skills
│    → Practice for Level 3
│      Level 3 的練習
│
├── Core Architecture (docs/01-foundations/agentic-substrate.md)
│    The paradigm shift: why this is all happening
│    典範轉移：為什麼這一切在發生
│    → Context for all levels
│      所有等級的背景
│
├── Five-Layer Model (docs/01-foundations/five-layer-model.md)
│    The complete architectural model
│    完整的架構模型
│    → The map for the entire journey
│      整趟旅程的地圖
│
├── Skill Anatomy (docs/01-foundations/skill-anatomy.md)
│    How Skills are structured — seven components
│    Skills 如何結構化——七大組件
│    → Deep reference for Level 3
│      Level 3 的深度參考
│
├── Skill Composition (docs/02-architecture/skill-composition.md)
│    How Skills combine dynamically
│    Skills 如何動態組合
│    → Advanced Level 3 → Level 4 bridge
│      進階 Level 3 → Level 4 的橋梁
│
├── Memory & State (docs/02-architecture/memory-and-state.md)
│    How Agents remember across sessions
│    Agent 如何跨工作階段記憶
│    → Essential for Level 4
│      Level 4 的必備知識
│
└── Claude Case Study (docs/03-claude-case-study/claude-architecture.md)
     A real AI system validates the framework
     一個真實的 AI 系統驗證框架
     → Proof that this is real, not theory
       證明這是真的，不是理論
```

---

## Where to Start ── 從哪裡開始

**If you've never used AI for work** → Start at Level 1. Open Claude.ai or ChatGPT and have a conversation about a real work task. Notice what's useful and what's frustrating.

**如果你從未將 AI 用於工作** → 從 Level 1 開始。打開 Claude.ai 或 ChatGPT，就一個真實的工作任務進行對話。注意什麼有用、什麼令人沮喪。

**If you use AI regularly but it feels limited** → You're ready for Level 2. Try Cowork or Claude Code. The moment you see AI reading your actual files and producing real documents, you'll understand the Layer 2 difference.

**如果你經常使用 AI 但覺得受限** → 你準備好進入 Level 2 了。試試 Cowork 或 Claude Code。當你看到 AI 讀取你的實際檔案並產出真實文件的那一刻，你會理解第二層的差異。

**If you have deep domain expertise and want AI to do things "your way"** → You're ready for Level 3. Read [You Already Know](you-already-know.md), then try the [Skill Self-Discovery](../../skills/skill-self-discovery/SKILL.md) exercise. You'll realize you can build Skills today.

**如果你有深厚的領域專業知識並希望 AI 按「你的方式」做事** → 你準備好進入 Level 3 了。讀讀[你已經會建 Skill 了](you-already-know.md)，然後試試[技能自我發現](../../skills/skill-self-discovery/SKILL.md)練習。你會意識到你今天就能建構 Skills。

**If you want to build persistent AI workflows** → Level 4. Read [Memory & State](../02-architecture/memory-and-state.md) for the patterns, [Skill Composition](../02-architecture/skill-composition.md) for how Skills combine, and the [Claude Case Study](../03-claude-case-study/claude-architecture.md) for real-world validation.

**如果你想建構持續性 AI 工作流程** → Level 4。讀[記憶與狀態](../02-architecture/memory-and-state.md)了解模式、[Skill 組合](../02-architecture/skill-composition.md)了解 Skills 如何結合、[Claude 案例研究](../03-claude-case-study/claude-architecture.md)了解真實世界的驗證。

---

## A Note on Speed ── 關於速度的說明

There's no exam. There's no certification. There's no "you must spend X hours at Level 2 before advancing."

沒有考試。沒有認證。沒有「你必須在 Level 2 花 X 小時才能進階」。

Some people will move from Level 1 to Level 3 in an afternoon — especially domain experts who realize they've been doing "Skill design" their entire careers without the vocabulary. Others will spend months deepening their Level 2 capabilities before exploring Skills.

有些人會在一個下午內從 Level 1 到 Level 3——特別是意識到他們整個職業生涯都在做「Skill 設計」只是缺少詞彙的領域專家。其他人會花幾個月深化 Level 2 的能力，然後才探索 Skills。

Both paths are valid. The framework is here when you're ready.

兩條路徑都是有效的。當你準備好的時候，框架在這裡。

---

*Previous: [You Already Know ←](you-already-know.md)*
*Next: [Core Architecture →](../01-foundations/agentic-substrate.md)*
