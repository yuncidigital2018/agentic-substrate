# Markdown as the Native Medium of Agentic Software
# Markdown：代理型軟體的原生工作介質

> *"In the Agentic era, Markdown is not just a file format. It's the air that agents breathe — the medium through which they think, remember, validate, and communicate."*
>
> *「在代理型時代，Markdown 不只是一種檔案格式。它是 Agent 呼吸的空氣——它們思考、記憶、驗證和溝通所用的介質。」*

---

## 1. Beyond "Interchange Format" ── 超越「交換格式」

In [The Core Architecture](agentic-substrate.md), we introduced Markdown as the "universal interchange protocol — the JSON of the AI era." That's true, but incomplete.

在[核心架構](agentic-substrate.md)中，我們介紹 Markdown 作為「通用交換協議——AI 時代的 JSON」。這是對的，但不完整。

JSON is a serialization format — data passes through it. You don't *work* in JSON. You don't *think* in JSON. It's a pipe, not a workspace.

JSON 是一種序列化格式——資料通過它。你不會*在* JSON 中工作。你不會*用* JSON 思考。它是管道，不是工作空間。

**Markdown is different.** In an Agentic workflow, Markdown is simultaneously:

**Markdown 不同。**在代理型工作流中，Markdown 同時是：

- The **definition** of what to do (SKILL.md) 做什麼的**定義**
- The **workspace** where work happens (chapter drafts, analysis) 工作發生的**工作區**
- The **record** of what was done (work logs, decisions) 做了什麼的**記錄**
- The **validation** that it was done correctly (verification reports) 做對了的**驗證**
- The **memory** that persists across sessions (DAILY.md, state files) 跨工作階段持續的**記憶**
- The **dashboard** that shows progress (progress trackers) 顯示進度的**儀表板**
- The **plan** for what comes next (roadmaps, milestones) 接下來做什麼的**計畫**

No other format serves all seven roles. This is why Markdown is not merely a protocol choice — it's the **native medium** of Agentic software.

沒有其他格式能同時扮演這七個角色。這就是為什麼 Markdown 不僅是協議的選擇——它是代理型軟體的**原生介質**。

---

## 2. The Taxonomy of .md Files ── .md 檔案的分類學

Not all Markdown files are the same. In a well-designed Agentic workflow, `.md` files fall into distinct categories, each with different **stability**, **authorship**, and **purpose**.

不是所有 Markdown 檔案都一樣。在設計良好的代理型工作流中，`.md` 檔案分為不同類別，各有不同的**穩定性**、**作者身份**和**用途**。

### Category 1: Definition Files — 定義檔

**What they are 是什麼**: Files that define *what* a system or process should do.
定義系統或流程*應該做什麼*的檔案。

**Characteristics 特性**:
- Written by humans (or human-AI collaboration) 由人類（或人機協作）撰寫
- Rarely change once stable 一旦穩定就很少改變
- Read by Agents at startup 由 Agent 在啟動時讀取
- Function as **interface contracts** 作為**介面契約**

**Examples 範例**:

| File 檔案 | Purpose 用途 | Stability 穩定性 |
|---|---|---|
| `SKILL.md` | Defines a Skill's behavior and process 定義 Skill 的行為和流程 | Very high 非常高 |
| `SOUL.md` | Defines an Agent's identity and personality 定義 Agent 的身份和個性 | Very high 非常高 |
| `STYLE.md` | Defines communication conventions 定義溝通慣例 | High 高 |
| `format_spec.md` | Defines output formatting rules 定義輸出格式規則 | High 高 |
| `CONTRIBUTING.md` | Defines how to participate 定義如何參與 | High 高 |

**The key insight 關鍵洞見**: Definition Files are like **compiled code** in traditional software — they encode the logic that governs the system. But unlike compiled code, any human can open and read them.

**關鍵洞見**：Definition Files 像傳統軟體中的**已編譯程式碼**——它們編碼了治理系統的邏輯。但不同於已編譯程式碼，任何人都能打開和閱讀它們。

### Category 2: Working Documents — 工作文件

**What they are 是什麼**: Files actively being created and modified during task execution.
在任務執行過程中被積極建立和修改的檔案。

**Characteristics 特性**:
- Created and modified by Agents (with human oversight) 由 Agent 建立和修改（在人類監督下）
- Change frequently — every session, sometimes every step 頻繁改變——每次工作階段，有時每一步
- Represent **work in progress** 代表**進行中的工作**
- Will eventually become final outputs 最終會成為最終輸出

**Examples 範例**:

| File 檔案 | Purpose 用途 | Change Frequency 變動頻率 |
|---|---|---|
| `chapter_01.md` ~ `chapter_07.md` | Draft content being written 正在撰寫的草稿內容 | Every session 每次工作階段 |
| `research_notes.md` | Collected research and analysis 收集的研究和分析 | Multiple times per session 每工作階段多次 |
| `meeting_notes.md` | Captured discussions and decisions 捕捉的討論和決策 | Per meeting 每次會議 |
| `draft_v1.md`, `draft_v2.md` | Iterating versions of deliverables 迭代版本的交付物 | Per review cycle 每個審查週期 |

**The key insight 關鍵洞見**: Working Documents are the Agentic equivalent of **RAM** — they hold the active state of work being performed. They're volatile, expected to change, and represent the "thinking" of the system.

**關鍵洞見**：Working Documents 是代理型的**RAM**等價物——它們保持正在執行的工作的活動狀態。它們是易變的、預期會改變的，代表系統的「思考」。

### Category 3: State Files — 狀態檔

**What they are 是什麼**: Files that capture the current state of a project or workflow, enabling session-to-session continuity.
捕捉專案或工作流當前狀態的檔案，使工作階段之間的連續性成為可能。

**Characteristics 特性**:
- Updated at the **end** of each session 在每次工作階段**結束時**更新
- Read at the **start** of the next session 在下次工作階段**開始時**讀取
- Enable the **repo-as-memory** pattern 實現**倉庫即記憶**模式
- Are the bridge between Agent sessions 是 Agent 工作階段之間的橋樑

**Examples 範例**:

| File 檔案 | Purpose 用途 | Update Pattern 更新模式 |
|---|---|---|
| `DAILY.md` | Current project status snapshot 當前專案狀態快照 | End of each session 每次工作階段結束 |
| `MILESTONES.md` | Timeline with status indicators 帶狀態標示的時間線 | When milestones change 里程碑變動時 |
| `progress_dashboard.md` | Visual progress overview 視覺化進度概覽 | After each major step 每個主要步驟後 |
| `decisions.md` | Log of decisions and rationale 決策和理由的紀錄 | When decisions are made 做決策時 |

**The key insight 關鍵洞見**: State Files are the Agentic equivalent of a **database** — but instead of SQL tables, they use human-readable Markdown. An Agent reads `DAILY.md` at startup and knows exactly where the project stands, without needing conversation history.

**關鍵洞見**：State Files 是代理型的**資料庫**等價物——但不是用 SQL 表格，而是用人類可讀的 Markdown。Agent 在啟動時讀取 `DAILY.md` 就能確切知道專案在哪裡，不需要對話歷史。

### Category 4: Validation Files — 驗證檔

**What they are 是什麼**: Files that verify the correctness and consistency of work outputs.
驗證工作輸出的正確性和一致性的檔案。

**Characteristics 特性**:
- Generated automatically after each work phase 在每個工作階段後自動生成
- Function as **test results** in software engineering terms 在軟體工程術語中作為**測試結果**
- Enable iterative improvement — fail → fix → revalidate 實現迭代改善——失敗→修復→重新驗證
- Provide an audit trail 提供審計軌跡

**Examples 範例**:

| File 檔案 | Purpose 用途 | Equivalent In Software 軟體中的等價物 |
|---|---|---|
| `validation_ch01.md` ~ `validation_ch07.md` | Per-chapter correctness checks 逐章正確性檢查 | Unit test results 單元測試結果 |
| `consistency_check_report.md` | Cross-document consistency 跨文件一致性 | Integration test results 整合測試結果 |
| `editorial_guide.md` | Baseline rules for validation 驗證的基準規則 | Test specification 測試規格 |
| `validation_log.md` | History of all validation runs 所有驗證運行的歷史 | CI/CD log CI/CD 紀錄 |

**The key insight 關鍵洞見**: Validation Files bring **software engineering rigor to knowledge work**. Just as no responsible developer ships code without tests, no responsible Agent should produce documents without validation. The difference is that these "tests" are written in Markdown and evaluated by an LLM, not by a test runner.

**關鍵洞見**：Validation Files 將**軟體工程的嚴謹帶入知識工作**。就像沒有負責任的開發者會在沒有測試的情況下發布程式碼，沒有負責任的 Agent 應該在沒有驗證的情況下產出文件。差別在於這些「測試」是用 Markdown 寫的，由 LLM 評估，而不是由測試運行器評估。

### Category 5: Plan Files — 計畫檔

**What they are 是什麼**: Files that define what will happen next — roadmaps, task lists, timelines.
定義接下來會發生什麼的檔案——路線圖、任務清單、時間線。

**Characteristics 特性**:
- Forward-looking — describe future actions 前瞻性——描述未來行動
- Updated as plans evolve 隨計畫演進而更新
- Guide both humans and Agents 引導人類和 Agent
- Often contain checklists or status markers 常包含清單或狀態標記

**Examples 範例**:

| File 檔案 | Purpose 用途 | Audience 讀者 |
|---|---|---|
| `ROADMAP.md` | Project development phases 專案開發階段 | Humans + Agents |
| `implementation_plan.md` | Step-by-step execution plan 逐步執行計畫 | Primarily Agents 主要是 Agent |
| `sprint_backlog.md` | Current sprint tasks 當前 sprint 任務 | Both 兩者 |
| `checklist_event_prep.md` | Pre-event preparation checklist 活動準備清單 | Both 兩者 |

---

## 3. The .md File Lifecycle in a Workflow ── 工作流中 .md 檔案的生命週期

Here's how these categories interact in a real Agentic workflow:

以下是這些類別在真實代理型工作流中如何互動：

```
Session Start 工作階段開始
│
├── Agent reads Definition Files    ← SKILL.md, SOUL.md, STYLE.md
│   (knows WHO it is and WHAT to do)  (知道自己是誰、該做什麼)
│
├── Agent reads State Files          ← DAILY.md, progress_dashboard.md
│   (knows WHERE the project stands)  (知道專案在哪裡)
│
├── Agent reads Plan Files           ← ROADMAP.md, implementation_plan.md
│   (knows WHAT to do next)           (知道接下來做什麼)
│
├── Agent works on Working Documents ← chapter_03.md, research_notes.md
│   (DOES the actual work)            (做實際的工作)
│
├── Agent generates Validation Files ← validation_ch03.md
│   (CHECKS the work is correct)      (檢查工作是否正確)
│
├── Agent updates State Files        ← DAILY.md, progress_dashboard.md
│   (RECORDS what was accomplished)   (記錄完成了什麼)
│
└── Session End 工作階段結束
    (All state is captured in .md files — no conversation history needed)
    (所有狀態都捕捉在 .md 檔案中——不需要對話歷史)
```

**This is the fundamental cycle of Agentic work.** Every session follows this pattern: read state → understand plan → do work → validate → update state. And every step is mediated through Markdown files.

**這是代理型工作的基本循環。**每次工作階段都遵循這個模式：讀取狀態→理解計畫→做工作→驗證→更新狀態。每一步都透過 Markdown 檔案進行。

---

## 4. Why Markdown and Not Something Else? ── 為什麼是 Markdown 而不是別的？

### 4.1 The Failed Alternatives 失敗的替代方案

| Format 格式 | Why It Fails for Agentic Work 為什麼不適合代理型工作 |
|---|---|
| **JSON/YAML** | Structured but not readable as a "document." Nobody wants to review a 500-line JSON as a progress report. 結構化但不能作為「文件」閱讀。沒人想看 500 行 JSON 當進度報告。 |
| **Plain text** | Readable but no structure. Can't express tables, hierarchies, or formatted sections. 可讀但沒有結構。無法表達表格、層級或格式化段落。 |
| **HTML** | Too verbose for authoring. Agents waste tokens on tags. Humans can't easily read raw HTML. 太冗長。Agent 浪費 token 在標籤上。人類不容易閱讀原始 HTML。 |
| **PDF** | Output-only format — can't be edited by Agents or versioned meaningfully. 只能輸出——不能被 Agent 編輯或有意義地版本控制。 |
| **Word (.docx)** | Binary format — invisible to Agents without special tools. Not versionable. 二進位格式——Agent 沒有特殊工具看不到。不能版控。 |
| **Database (SQL)** | Requires schema, connection, queries. Overkill for most Agent workflows. Not human-browsable. 需要 schema、連線、查詢。對大多數 Agent 工作流來說太重。人類不能瀏覽。 |
| **Conversation history** | Ephemeral. Grows unboundedly. Mixes signal with noise. Cannot be selectively loaded. 短暫的。無限制增長。信號與雜訊混合。無法選擇性載入。 |

### 4.2 Markdown's Unique Properties Markdown 的獨特屬性

Markdown succeeds because it occupies a **sweet spot** that no other format reaches:

Markdown 成功是因為它佔據了沒有其他格式能達到的**甜蜜點**：

```
         Structured ←──────────────────────→ Flexible
              │                                  │
         JSON/YAML                          Plain Text
              │                                  │
              │        ┌──────────┐             │
              │        │ MARKDOWN │             │
              │        │  ★★★★★   │             │
              │        └──────────┘             │
              │                                  │
         Machine ←────────────────────────→ Human
         Optimized                          Optimized
```

Specifically, Markdown provides:

具體來說，Markdown 提供：

**1. Progressive Structure 漸進式結構**

You can write a Markdown file that's as simple as a plain text note, or as structured as a multi-level document with tables, code blocks, and cross-references. The format grows with the complexity of the content.

你可以寫一個像純文字筆記一樣簡單的 Markdown 檔案，也可以寫一個有表格、程式碼區塊和交叉引用的多層級文件。格式隨內容的複雜度一起成長。

```
Simple:     # Meeting Notes\nDiscussed the budget. Action: review by Friday.

Complex:    # Chapter 3: Execution Strategy
            ## 3.1 Phase Overview
            | Phase | Timeline | KPI | Owner |
            |-------|----------|-----|-------|
            ...
            ### 3.1.1 Detailed Methodology
            > Cross-reference: See [Chapter 2, Section 2.3](chapter_02.md#23)
```

**2. Headers as Semantic Anchors 標題作為語義錨點**

Headers (`#`, `##`, `###`) give LLMs the ability to navigate and reference specific sections of a document — like function names in code.

標題給了 LLM 在文件中導航和引用特定段落的能力——像程式碼中的函式名稱。

**3. Tables as Structured Data 表格作為結構化資料**

Markdown tables provide just enough structure for the LLM to parse and generate tabular data, without the overhead of a database.

Markdown 表格提供恰好足夠的結構讓 LLM 解析和生成表格資料，沒有資料庫的開銷。

**4. Code Blocks as Embedded Logic 程式碼區塊作為嵌入邏輯**

Fenced code blocks (` ``` `) allow embedding commands, templates, or structured data within a human-readable document.

程式碼區塊允許在人類可讀的文件中嵌入命令、模板或結構化資料。

**5. Links as Composition Mechanism 連結作為組合機制**

Markdown links (`[text](path)`) enable documents to reference each other, creating a web of connected knowledge — like imports in code.

Markdown 連結使文件能互相引用，創建一個連結知識的網絡——像程式碼中的 import。

**6. Git-Native Versioning Git 原生版本控制**

Because Markdown is plain text, `git diff` shows exactly what changed, line by line. This makes every edit visible, reviewable, and reversible — the foundation of the repo-as-memory pattern.

因為 Markdown 是純文字，`git diff` 精確顯示逐行的變化。這使每次編輯都可見、可審查、可逆轉——repo-as-memory 模式的基礎。

---

## 5. The Problem Markdown Solves for Everyday Users ── Markdown 為日常使用者解決的問題

Most people use LLMs like this:

大多數人這樣使用 LLM：

```
[Chat window]
User: Help me write a project update
AI: Here's a draft...
User: Change the second paragraph
AI: Updated...
User: Actually go back to the first version
AI: I don't have the first version anymore...
User: Also, what did we decide about the budget last week?
AI: I don't have context from last week...
```

**The problems 問題**:
- Context gets lost between sessions 情境在工作階段之間遺失
- No record of decisions 沒有決策記錄
- Can't go back to previous versions 不能回到之前的版本
- Priorities and outlines get jumbled 優先順序和大綱被搞亂
- Work gets duplicated or contradicted 工作被重複或矛盾

**The solution is devastatingly simple: use .md files.**

**解決方案簡單得令人驚訝：使用 .md 檔案。**

```
[Chat + work_record.md]

work_record.md:
# Project Update - Q2 Campaign
## Status: Draft v2
## Decisions
- Budget: $50K (approved 2026-04-15)
- Timeline: Launch June 1
## Outline
1. Executive Summary ✅
2. Campaign Strategy (in progress)
3. Budget Breakdown ⬜
4. Timeline ⬜
## Current Draft
[content here]
```

Now every session starts by reading `work_record.md`. The LLM knows the decisions, the outline, the progress, and the current draft. Nothing is lost. Nothing is duplicated.

現在每次工作階段都從讀取 `work_record.md` 開始。LLM 知道決策、大綱、進度和當前草稿。什麼都不會遺失。什麼都不會重複。

**This is the first step on the Skill Maturity ladder** (see [Skill Anatomy](skill-anatomy.md#7-the-skill-maturity-model--技能成熟度模型)): going from L0 (pure chat) to L1 (guided workflow with a persistent record). And Markdown is what makes it possible.

**這是 Skill 成熟度階梯的第一步**（見[技能解剖學](skill-anatomy.md#7-the-skill-maturity-model--技能成熟度模型)）：從 L0（純聊天）到 L1（有持久記錄的引導式工作流）。而 Markdown 是使之成為可能的東西。

---

## 6. The Complete .md Ecosystem in a Project ── 專案中完整的 .md 生態系

Here's what a mature Agentic project looks like — every file is a `.md` with a specific role:

以下是一個成熟的代理型專案的樣子——每個檔案都是有特定角色的 `.md`：

```
my-project/
│
│  ── Definition Layer 定義層 ──
├── SOUL.md                     Agent identity 代理身份
├── STYLE.md                    Communication norms 溝通規範
├── skills/
│   └── my-workflow/SKILL.md    Workflow definition 工作流程定義
│
│  ── Plan Layer 計畫層 ──
├── ROADMAP.md                  Big picture phases 大局階段
├── MILESTONES.md               Key dates & deadlines 關鍵日期
├── implementation_plan.md      Detailed task breakdown 詳細任務分解
│
│  ── State Layer 狀態層 ──
├── DAILY.md                    Current snapshot 當前快照
├── progress_dashboard.md       Visual progress 視覺化進度
├── decisions.md                Decision log 決策紀錄
│
│  ── Working Layer 工作層 ──
├── chapters/
│   ├── ch01_introduction.md
│   ├── ch02_strategy.md
│   └── ch03_execution.md
├── research/
│   ├── market_analysis.md
│   └── competitor_review.md
│
│  ── Validation Layer 驗證層 ──
├── validation/
│   ├── editorial_guide.md      Baseline rules 基準規則
│   ├── validation_ch01.md      Chapter 1 check 第一章驗證
│   ├── validation_ch02.md      Chapter 2 check 第二章驗證
│   ├── validation_log.md       All checks history 所有檢查歷史
│   └── consistency_report.md   Cross-doc check 跨文件檢查
│
│  ── Knowledge Layer 知識層 ──
├── references/
│   ├── format_spec.md          Output format rules 輸出格式規則
│   └── domain_knowledge.md     Domain-specific info 領域特定資訊
└── data/
    └── portfolio.json          Structured data 結構化資料
```

**Count**: In a mature project, you might have 20-30 `.md` files, each with a clear role. This IS the project. Not a database. Not a codebase. Not a chat history. **A structured collection of Markdown files.**

**統計**：在一個成熟的專案中，你可能有 20-30 個 `.md` 檔案，每個都有清楚的角色。這就是專案。不是資料庫。不是程式碼庫。不是聊天歷史。**一組結構化的 Markdown 檔案。**

---

## 7. Design Principles for .md-Centric Workflows ── 以 .md 為中心的工作流設計原則

### Principle 1: Every Important Artifact Should Be a .md File 每個重要的產物都應該是 .md 檔案

If information matters, it should live in a `.md` file — not in a chat message, not in someone's head, not in an email. Chat is ephemeral; `.md` files persist.

如果資訊重要，它就應該存在 `.md` 檔案中——不是在聊天訊息中，不是在某人的腦袋裡，不是在電子郵件中。聊天是短暫的；`.md` 檔案是持久的。

### Principle 2: Name Files by Role, Not by Content 依角色命名檔案，而非依內容

`DAILY.md` is better than `status_2026_04_21.md`. The Agent needs to know **where to look**, not what date it is. Role-based naming creates predictable patterns.

`DAILY.md` 比 `status_2026_04_21.md` 好。Agent 需要知道**去哪裡看**，而不是今天是什麼日期。基於角色的命名創造可預測的模式。

### Principle 3: Separate Definition from State 將定義與狀態分開

A `SKILL.md` should never contain current progress data. A `DAILY.md` should never contain process definitions. Mixing them creates files that are both too unstable to be contracts and too rigid to be working documents.

`SKILL.md` 不應該包含當前進度資料。`DAILY.md` 不應該包含流程定義。混合它們會創造出既太不穩定而不能作為契約、又太僵硬而不能作為工作文件的檔案。

### Principle 4: Validate at Every Major Step 在每個主要步驟驗證

After completing a chapter, generate a `validation_chXX.md`. After completing all chapters, generate a `consistency_report.md`. These files are the "test suite" of your knowledge work.

完成一章後，生成 `validation_chXX.md`。完成所有章節後，生成 `consistency_report.md`。這些檔案是你知識工作的「測試套件」。

### Principle 5: Use Status Markers Consistently 一致地使用狀態標記

Adopt a consistent set of status markers across all files:

在所有檔案中採用一致的狀態標記集：

```
✅  Done 完成
⬜  Planned 已規劃
🔄  In progress 進行中
⚠️  Blocked 被阻擋
❌  Failed validation 驗證失敗
```

These markers are both human-scannable and LLM-parseable. Agent 可以搜尋 `❌` 來找到需要修復的項目。

### Principle 6: Link, Don't Duplicate 連結，不要重複

If information exists in one `.md` file, other files should link to it, not copy it. Duplication leads to inconsistency. Links maintain a single source of truth.

如果資訊存在於某個 `.md` 檔案中，其他檔案應該連結到它，而不是複製它。重複導致不一致。連結維護唯一的事實來源。

```
Bad 壞:    In chapter_03.md: "Budget is $50K (as decided on April 15)"
Good 好:   In chapter_03.md: "Budget details: see [decisions.md](decisions.md#budget)"
```

---

## 8. Markdown as the Bridge Between Eras ── Markdown 作為時代之間的橋樑

Here's a subtle but important point: Markdown works across **all phases of the paradigm transition**.

這裡有一個微妙但重要的觀點：Markdown 在**典範轉型的所有階段**都能運作。

| Era 時代 | How Markdown Is Used 如何使用 Markdown |
|---|---|
| **Pre-AI** 前 AI | Documentation, READMEs, note-taking 文件、README、筆記 |
| **Chat-AI** 聊天 AI | Prompt templates, conversation summaries 提示模板、對話摘要 |
| **Skill-AI** 技能 AI | Skill definitions, work records, validation reports 技能定義、工作紀錄、驗證報告 |
| **Agent-AI** 代理 AI | Full project state, agent handbooks, memory systems 完整專案狀態、代理手冊、記憶系統 |
| **Post-App** 後 App | The only persistent layer between ephemeral AI-generated interfaces 短暫 AI 生成介面之間唯一的持久層 |

This means **learning to work with Markdown is a permanently valuable skill** — it's not a tool that will be obsoleted by the next generation of AI. If anything, it becomes *more* important as we move further into the Agentic era.

這意味著**學會使用 Markdown 是一項永久有價值的技能**——它不是會被下一代 AI 淘汰的工具。如果有什麼的話，隨著我們更深入代理型時代，它變得*更加*重要。

---

## Summary 總結

Markdown is not a file format choice. It is the **native medium** of Agentic software — the substrate through which Agents define their behavior, do their work, validate their outputs, remember their state, and plan their next moves.

Markdown 不是一個檔案格式的選擇。它是代理型軟體的**原生介質**——Agent 透過它定義行為、執行工作、驗證輸出、記憶狀態和規劃下一步的基底。

Understanding this is the difference between "using AI to chat" and "building AI-native workflows."

理解這一點，就是「用 AI 聊天」和「建構 AI 原生工作流」之間的差別。

---

*Previous: [Anatomy of a Skill ←](skill-anatomy.md)*
*Next: [The Five-Layer Model in Detail →](five-layer-model.md)*
