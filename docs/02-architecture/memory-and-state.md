# Memory & State: How Agents Remember
# 記憶與狀態：Agent 如何記得

> *"The difference between a helpful stranger and a trusted colleague is memory."*
> *「一個熱心的陌生人和一個可信賴的同事之間的差距，就是記憶。」*

Every time you open ChatGPT, it feels like talking to a brilliant person with amnesia. You explain your project, your preferences, your context — and then the session ends. Next time, you do it all over again.

每次你打開 ChatGPT，就像在和一個有失憶症的天才對話。你解釋你的專案、你的偏好、你的背景——然後工作階段結束。下一次，你一切從頭來過。

This isn't a minor inconvenience. It's the **central bottleneck** of the entire Agentic paradigm. Without memory, an LLM is a powerful calculator. With memory, it becomes a collaborator.

這不是一個小不便。這是整個代理型典範的**核心瓶頸**。沒有記憶，LLM 是一台強大的計算機。有了記憶，它成為一個協作者。

This document explores how the memory problem works, why it's harder than it seems, and what practical patterns have emerged to solve it.

本文件探討記憶問題如何運作、為什麼比想像中更難，以及哪些實務模式已經浮現來解決它。

---

## 1. The Fundamental Constraint: LLMs Are Stateless ── 根本性約束：LLM 天生無狀態

An LLM has no built-in memory between sessions. Every API call is independent — the model receives a prompt, generates a response, and forgets everything. This is by design: stateless inference is simpler, more scalable, and more secure.

LLM 在工作階段之間沒有內建記憶。每次 API 呼叫都是獨立的——模型收到一個 prompt、生成一個回應、然後忘記一切。這是刻意的設計：無狀態推理更簡單、更可擴展、更安全。

But this means the **entire burden of continuity falls on the system built around the LLM**, not the LLM itself. Every piece of context the model "knows" in a given session had to be explicitly placed in its context window by something else — a system prompt, a tool call, a file read, or a retrieved document.

但這意味著**連續性的全部負擔落在圍繞 LLM 建構的系統上**，而非 LLM 本身。模型在某次工作階段中「知道」的每一條資訊，都必須被其他東西明確地放入它的 context window——系統提示、工具呼叫、檔案讀取或檢索到的文件。

This is fundamentally different from how human memory works:

這與人類記憶的運作方式根本不同：

| Aspect 面向 | Human Memory 人類記憶 | LLM "Memory" LLM「記憶」 |
|---|---|---|
| Persistence 持久性 | Automatic — experiences are stored without effort 自動——經歷不費力地儲存 | None by default — must be explicitly built 預設為零——必須明確建構 |
| Retrieval 檢索 | Associative — triggered by cues, often unconscious 聯想式——由線索觸發，常是無意識的 | Explicit — must be placed in context window 明確的——必須被放入 context window |
| Capacity 容量 | Enormous but fuzzy 龐大但模糊 | Precise but limited (context window size) 精確但有限（context window 大小） |
| Forgetting 遺忘 | Gradual and selective 漸進和選擇性的 | Absolute — outside the window = gone 絕對的——不在視窗內 = 不存在 |
| Update 更新 | Continuous and unconscious 持續且無意識的 | Manual — someone must write the update 手動的——必須有人寫入更新 |

The engineering challenge is clear: **build a memory system around a fundamentally amnesiac core.**

工程挑戰很明確：**圍繞一個根本性失憶的核心建構記憶系統。**

---

## 2. Three Types of Memory ── 三種記憶類型

Just as computer science distinguishes registers, RAM, and disk storage, Agentic systems have three tiers of memory with different speeds, capacities, and lifespans:

就像計算機科學區分暫存器、RAM 和磁碟儲存，代理型系統也有三層記憶，具有不同的速度、容量和壽命：

```
┌─────────────────────────────────────────────────────────────┐
│  Type 1: Working Memory (Context Window)                     │
│  工作記憶（Context Window）                                    │
│                                                              │
│  Speed: Instant   Capacity: 128K-200K tokens   Life: 1 turn │
│  速度：即時        容量：128K-200K tokens        壽命：一輪     │
│  ──────────────────────────────────────────────────────────── │
│  Everything the LLM can "see" right now.                     │
│  LLM 此刻能「看到」的一切。                                    │
│  System prompt + conversation history + tool results +       │
│  retrieved documents. If it's not here, the model doesn't    │
│  know it exists.                                             │
│  系統提示 + 對話歷史 + 工具結果 + 檢索文件。                    │
│  不在這裡，模型就不知道它存在。                                  │
├─────────────────────────────────────────────────────────────┤
│  Type 2: Session Memory (Conversation State)                 │
│  工作階段記憶（對話狀態）                                       │
│                                                              │
│  Speed: Fast      Capacity: Megabytes          Life: 1 session│
│  速度：快          容量：MB 級                    壽命：一次工作階段│
│  ──────────────────────────────────────────────────────────── │
│  Files created during a session. Work records, drafts,       │
│  intermediate outputs. Accessible via tool calls (Read,      │
│  Write, Bash). Survives within the session but may not       │
│  persist after session ends.                                 │
│  工作階段中建立的檔案。工作紀錄、草稿、中間產出。                  │
│  透過工具呼叫存取。在工作階段內存活，                             │
│  但工作階段結束後可能不持久。                                    │
├─────────────────────────────────────────────────────────────┤
│  Type 3: Persistent Memory (Long-Term State)                 │
│  持久記憶（長期狀態）                                           │
│                                                              │
│  Speed: Slow      Capacity: Unlimited          Life: Forever │
│  速度：慢          容量：無限                     壽命：永久     │
│  ──────────────────────────────────────────────────────────── │
│  State files in a Git repo, database records, knowledge      │
│  bases. Survives across sessions, across agents, across      │
│  time. Must be explicitly read into working memory to be     │
│  useful.                                                     │
│  Git repo 中的狀態檔、資料庫紀錄、知識庫。                      │
│  跨工作階段、跨 Agent、跨時間存活。                              │
│  必須明確讀入工作記憶才能使用。                                   │
└─────────────────────────────────────────────────────────────┘
```

### The Computer Analogy ── 電腦類比

This three-tier structure maps directly to traditional computing:

這個三層結構直接對應到傳統運算：

| Agentic Memory 代理型記憶 | Computer Analogy 電腦類比 | Key Property 關鍵特性 |
|---|---|---|
| Working Memory (Context Window) | **RAM** | Fast, limited, volatile — lost when session ends 快速、有限、易失——工作階段結束就消失 |
| Session Memory (Files in Session) | **Local Disk** | Larger, persistent within session, accessible via I/O 更大、工作階段內持久、透過 I/O 存取 |
| Persistent Memory (Git Repo / DB) | **Network Storage / Cloud** | Unlimited, permanent, shared across agents 無限、永久、跨 Agent 共享 |

The key engineering insight: **every memory tier requires a different access pattern**. Working memory is always "on." Session memory requires a tool call (read a file). Persistent memory requires explicit retrieval (read from repo, query a database).

關鍵工程洞見：**每一層記憶都需要不同的存取模式**。工作記憶永遠「開著」。工作階段記憶需要工具呼叫（讀取檔案）。持久記憶需要明確的檢索（從 repo 讀取、查詢資料庫）。

---

## 3. The Context Window: RAM of the Agentic Era ── Context Window：代理型時代的 RAM

The context window is the single most important constraint in Agentic system design. Everything the LLM reasons about must fit in this window. Understanding its properties is essential.

Context window 是代理型系統設計中最重要的單一約束。LLM 推理的一切都必須放進這個視窗。理解它的特性至關重要。

### 3.1 Properties ── 特性

**Fixed Size 固定大小**: Current models offer 128K-200K token windows (~300-500 pages of text). This sounds enormous, but consider: a single session with a complex project can easily consume 50K+ tokens in system prompts, Skill definitions, file contents, and conversation history.

**固定大小**：目前模型提供 128K-200K token 的視窗（約 300-500 頁文字）。這聽起來很大，但想想看：一個複雜專案的單次工作階段，光是系統提示、Skill 定義、檔案內容和對話歷史就能輕易消耗 50K+ tokens。

**Recency Bias 近時偏差**: LLMs tend to attend more strongly to tokens near the beginning (system prompt) and end (recent turns) of the context window. Information in the middle gets less attention — the well-documented "lost in the middle" phenomenon.

**近時偏差**：LLM 傾向於更強烈地關注 context window 開頭（系統提示）和結尾（最近的對話回合）附近的 tokens。中間的資訊得到較少關注——這是有充分記載的「中間遺失」現象。

**No Automatic Prioritization 沒有自動優先排序**: The LLM doesn't know which parts of the context window are important for the current task. It treats a 3,000-token Skill definition with the same passive attention as a 50-token status message. The system around the LLM must make prioritization decisions.

**沒有自動優先排序**：LLM 不知道 context window 中的哪些部分對當前任務重要。它對一個 3,000-token 的 Skill 定義和一個 50-token 的狀態訊息給予同樣的被動關注。LLM 周圍的系統必須做優先排序決策。

### 3.2 Context Window Management Strategies ── Context Window 管理策略

Smart context window management is what separates effective Agentic systems from wasteful ones:

聰明的 context window 管理是區分有效代理型系統和浪費型系統的關鍵：

**Strategy 1: Progressive Loading 漸進式載入**

Don't load everything at once. Load Skill definitions in tiers:

不要一次載入全部。分層載入 Skill 定義：

```
Tier 0:  Skill name only              ←  ~5 tokens each
         僅技能名稱
Tier 1:  Name + description           ← ~30 tokens each
         名稱 + 描述
Tier 2:  Full definition              ← ~500-3000 tokens each
         完整定義

10 Skills at Tier 0 = ~50 tokens
10 Skills at Tier 2 = ~5,000-30,000 tokens

The Agent loads only the Skills it needs to Tier 2.
Agent 只將需要的 Skills 載入到 Tier 2。
```

This is the approach used by the Agent Skills Open Standard — and it's one of its key innovations. The LLM reads Tier 0/1 lists to decide which Skills deserve full loading.

這是 Agent Skills 開放標準使用的方法——也是它的關鍵創新之一。LLM 讀取 Tier 0/1 列表來決定哪些 Skills 值得完整載入。

**Strategy 2: Summarization Checkpoints 摘要檢查點**

When a conversation grows long, summarize earlier segments and replace them with compressed versions:

當對話變長時，摘要較早的段落並用壓縮版本取代：

```
Before 之前:
[System Prompt] [Turn 1] [Turn 2] ... [Turn 47] [Turn 48]
                 ↑ Most of this is stale context
                   大部分是過時的上下文

After 之後:
[System Prompt] [Summary of Turns 1-40] [Turn 41] ... [Turn 48]
                 ↑ Compressed to essentials
                   壓縮至精華
```

This is how most modern agent systems handle long conversations — including Claude Code, which automatically compacts conversation history when approaching context limits.

這是大多數現代 Agent 系統處理長對話的方式——包括 Claude Code，它在接近 context 限制時會自動壓縮對話歷史。

**Strategy 3: Externalize to Files 外部化到檔案**

Move reference material out of the conversation and into files. Read them only when needed:

將參考材料從對話中移出並放入檔案。只在需要時讀取：

```
❌ Bad 不好: Paste the entire 2,000-line codebase into the conversation
             把整個 2,000 行程式碼貼到對話中

✅ Good 好:  Keep files on disk, use Read tool to access specific sections
             將檔案放在磁碟上，用 Read 工具存取特定段落
```

This is the fundamental reason Agentic systems use file-based workflows. Files are the "disk" that extends the limited "RAM" of the context window.

這是代理型系統使用基於檔案的工作流程的根本原因。檔案是擴展 context window 有限「RAM」的「磁碟」。

**Strategy 4: Structured Context Injection 結構化上下文注入**

When loading information into the context window, structure it for LLM comprehension:

將資訊載入 context window 時，為 LLM 理解而結構化：

```
❌ Bad 不好:
Here's everything about the project: [wall of text]

✅ Good 好:
## Current State
- Phase: Execution (Month 2 of 6)
- Last completed: Deliverable 3 (approved)
- Next due: Deliverable 4 (deadline: 2026-05-15)
- Blockers: None
- Key decision pending: Vendor selection for D5
```

Structured injection reduces the tokens needed and increases the model's ability to locate and use the relevant information.

結構化注入減少所需的 tokens 並增加模型定位和使用相關資訊的能力。

---

## 4. The Repo-as-Memory Pattern ── 倉庫即記憶模式

The most powerful persistent memory pattern to emerge in the Agentic era is **Repo-as-Memory** — using a Git repository as the Agent's long-term memory system.

在代理型時代浮現的最強大的持久記憶模式是**倉庫即記憶**——使用 Git 倉庫作為 Agent 的長期記憶系統。

### 4.1 The Core Insight ── 核心洞見

An Agent doesn't need a database, a vector store, or a custom memory API. It needs a **Git repo with well-structured Markdown files**. Here's why:

Agent 不需要資料庫、向量儲存或自定義記憶 API。它需要的是**一個有良好結構的 Markdown 檔案的 Git repo**。原因如下：

```
Traditional Memory System          Repo-as-Memory
傳統記憶系統                         倉庫即記憶
┌──────────────────────┐           ┌──────────────────────┐
│  Vector DB / SQL DB   │           │  Git Repository       │
│  - Requires setup     │           │  - Works immediately  │
│  - Custom query API   │           │  - Read/Write files   │
│  - Black-box storage  │           │  - Human-readable     │
│  - Drift over time    │           │  - Full version history│
│  - Hard to debug      │           │  - git diff = audit   │
│  - Requires infra     │           │  - Free on GitHub     │
└──────────────────────┘           └──────────────────────┘
```

### 4.2 The File Anatomy of Agent Memory ── Agent 記憶的檔案解剖

A repo functioning as Agent memory uses a predictable file structure where each file type serves a specific memory role:

作為 Agent 記憶運作的 repo 使用可預測的檔案結構，每種檔案類型服務特定的記憶角色：

```
project-repo/
│
├── SOUL.md                ← WHO: Agent identity, personality, role
│                             誰：Agent 身份、個性、角色
│
├── DAILY.md               ← NOW: Current state snapshot
│                             現在：當前狀態快照
│
├── MILESTONES.md          ← WHEN: Timeline with status markers
│                             何時：帶狀態標記的時間線
│
├── docs/
│   ├── deliverables/      ← WHAT: Work products
│   │   ├── D1-report.md      什麼：工作產物
│   │   ├── D2-analysis.md
│   │   └── ...
│   │
│   └── decisions/         ← WHY: Decision records
│       ├── 001-vendor.md     為什麼：決策紀錄
│       └── 002-scope.md
│
├── .agent/
│   ├── handbook.md        ← HOW: Agent operating instructions
│   │                         如何：Agent 操作說明
│   └── memory-index.md    ← WHERE: Index of all memory files
│                             哪裡：所有記憶檔的索引
│
└── .git/                  ← HISTORY: Complete version history
                              歷史：完整版本紀錄
```

### 4.3 The Agent Session Cycle ── Agent 工作階段循環

Every Agent session follows the same pattern — a cycle that transforms a stateless LLM into a stateful collaborator:

每次 Agent 工作階段都遵循相同的模式——一個將無狀態 LLM 轉化為有狀態協作者的循環：

```
                    ┌───────────────┐
                    │   Session     │
                    │   Starts      │
                    └───────┬───────┘
                            │
                    ┌───────▼───────┐
              ┌─────┤  1. Read State │  ← git pull + read DAILY.md
              │     │     讀取狀態    │     + read SOUL.md
              │     └───────┬───────┘
              │             │
              │     ┌───────▼───────┐
              │     │  2. Understand │  ← Parse milestones, find
              │     │     理解       │     next task, check blockers
              │     └───────┬───────┘
              │             │
              │     ┌───────▼───────┐
              │     │  3. Execute    │  ← Do the actual work:
              │     │     執行       │     write, analyze, create
              │     └───────┬───────┘
              │             │
              │     ┌───────▼───────┐
              │     │  4. Validate   │  ← Check quality, run tests,
              │     │     驗證       │     verify against criteria
              │     └───────┬───────┘
              │             │
              │     ┌───────▼───────┐
              │     │  5. Write Back │  ← Update DAILY.md, commit
              │     │     寫回       │     deliverables, git push
              │     └───────┬───────┘
              │             │
              │     ┌───────▼───────┐
              └────►│  Session Ends │  ← All state is in the repo
                    │  工作階段結束   │     所有狀態都在 repo 裡
                    └───────────────┘

Next session starts at step 1 — reads the repo, and continues.
下一次工作階段從步驟 1 開始——讀取 repo，然後繼續。
```

**The critical property**: At the end of every session, the Agent writes its state back to the repo. This means:

**關鍵特性**：在每次工作階段結束時，Agent 將狀態寫回 repo。這意味著：

- A different Agent (or a different instance of the same Agent) can pick up exactly where the previous one left off 不同的 Agent（或同一 Agent 的不同實例）可以從上一個離開的地方精確接續
- No conversation history is needed — the repo IS the memory 不需要對話歷史——repo 就是記憶
- Humans can inspect the state at any time by reading the same files 人類可以隨時透過讀取相同的檔案來檢視狀態
- `git log` provides a complete, timestamped history of everything the Agent has done `git log` 提供 Agent 所做一切的完整、帶時間戳的歷史

### 4.4 Why Git, Specifically ── 為什麼是 Git

Git is not the only way to persist state. But it offers unique properties that no other storage system combines:

Git 不是持久化狀態的唯一方法。但它提供其他儲存系統無法組合的獨特特性：

| Property 特性 | Why It Matters for Agents 為什麼對 Agent 重要 |
|---|---|
| **Version History** 版本歷史 | Every change is recorded — full audit trail of Agent decisions 每個變更都有紀錄——Agent 決策的完整審計軌跡 |
| **Diffability** 可差異化 | `git diff` shows exactly what changed, enabling review 精確顯示改了什麼，使審查成為可能 |
| **Branching** 分支 | Agents can experiment without risk — create a branch, try something, merge or discard Agent 可以無風險地實驗——建立分支、嘗試、合併或丟棄 |
| **Collaboration** 協作 | Multiple Agents and humans can work on the same repo with standard merge workflows 多個 Agent 和人類可以用標準合併流程在同一 repo 上協作 |
| **Distribution** 分散式 | Repo can be cloned, backed up, moved between environments — Agent memory is portable Agent 記憶可以被克隆、備份、在環境之間移動——Agent 記憶是可攜的 |
| **Plain Text** 純文字 | No proprietary format — any tool can read it, any LLM can process it 沒有專有格式——任何工具都能讀取，任何 LLM 都能處理 |

---

## 5. Four Practical Memory Patterns ── 四種實務記憶模式

Beyond the Repo-as-Memory architecture, several specific patterns have proven effective in real-world deployments:

除了倉庫即記憶架構之外，幾種特定模式已經在真實部署中證明有效：

### Pattern 1: The SOUL.md Pattern — Agent Identity ── Agent 身份

**Problem 問題**: How does an Agent know who it is, what it's good at, and how it should behave?

Agent 如何知道自己是誰、擅長什麼、應該如何表現？

**Solution 解法**: A `SOUL.md` file at the repo root that defines the Agent's identity, role, personality, communication style, and operating principles. The Agent reads this at the start of every session.

在 repo 根目錄放一個 `SOUL.md` 檔案，定義 Agent 的身份、角色、個性、溝通風格和運作原則。Agent 在每次工作階段開始時讀取它。

```markdown
# SOUL.md — Project Manager Agent

## Identity
I am the project manager for the [Project Name] initiative.
I track deliverables, maintain timelines, and coordinate
between team members and stakeholders.

## Operating Principles
- Always check DAILY.md before taking any action
- Never modify deliverables without validation
- Escalate blockers to the human lead within 24 hours
- Write in Traditional Chinese for all stakeholder-facing documents

## Communication Style
- Direct and concise
- Use bullet points for status updates
- Include data and evidence for all claims
```

**Why it works 為什麼有效**: The SOUL.md loads into working memory once per session (~200-500 tokens) and provides consistent identity across all interactions. Without it, the Agent's personality and judgment would drift between sessions.

SOUL.md 每次工作階段載入工作記憶一次（約 200-500 tokens），在所有互動中提供一致的身份。沒有它，Agent 的個性和判斷會在工作階段之間漂移。

### Pattern 2: The State Snapshot — DAILY.md ── 狀態快照

**Problem 問題**: How does an Agent know what's happening right now — what's done, what's next, what's blocked?

Agent 如何知道現在發生什麼——什麼完成了、接下來做什麼、什麼被阻擋了？

**Solution 解法**: A single `DAILY.md` file that serves as the current-state snapshot. Updated at the end of every session.

一個 `DAILY.md` 檔案作為當前狀態快照。在每次工作階段結束時更新。

```markdown
# DAILY.md — Last Updated: 2026-04-21

## Current Phase
Phase 2: Execution (Month 3 of 6)

## Status Summary
- ✅ D1 Kickoff Report — delivered, approved
- ✅ D2 Needs Assessment — delivered, approved  
- ✅ D3 Program Design — delivered, under review
- 🔄 D4 Implementation Plan — in progress (60%)
- ⬜ D5 Mid-term Report — not started
- ⬜ D6 Final Report — not started

## Current Focus
Writing D4 Section 3: Resource Allocation

## Blockers
- Waiting for client feedback on D3 (sent 04-18, follow up if no reply by 04-23)

## Next Actions
1. Complete D4 Section 3
2. Follow up on D3 review if no response
3. Begin D5 outline once D4 is submitted
```

**Why it works 為什麼有效**: The Agent reads this one file and immediately knows the project state, priorities, and blockers — without reading the entire conversation history or scanning dozens of files. This is the Agentic equivalent of a human reading their task board at the start of the workday.

Agent 讀取這一個檔案就立即知道專案狀態、優先順序和阻擋點——不需要讀取整個對話歷史或掃描數十個檔案。這是人類在工作日開始時看任務板的代理型等價物。

### Pattern 3: The Decision Record ── 決策紀錄

**Problem 問題**: Weeks into a project, nobody remembers *why* a decision was made. The Agent proposes something already rejected, or contradicts a prior agreement.

專案進行幾週後，沒人記得*為什麼*做了某個決定。Agent 提出已被拒絕的建議，或與之前的協議矛盾。

**Solution 解法**: A `decisions/` folder with one file per significant decision, recording the context, options considered, decision made, and rationale.

一個 `decisions/` 資料夾，每個重要決策一個檔案，記錄背景、考慮的選項、做出的決定和理由。

```markdown
# Decision 003: Choose Survey Platform

## Date: 2026-03-15
## Status: Decided

## Context
Need an online survey tool for the needs assessment (D2).
Budget: NT$30,000. Must support Traditional Chinese.

## Options Considered
1. Google Forms — Free, but limited analytics
2. SurveyCake — NT$12,000/year, Taiwan-based, good analytics
3. Typeform — NT$25,000/year, beautiful UI but no zh-TW support

## Decision
SurveyCake (#2)

## Rationale
Best balance of cost, language support, and analytics.
Client has used it before and trusts the platform.
```

**Why it works 為什麼有效**: When the Agent encounters a related question later, it can read the decision record and understand not just *what* was decided, but *why*. This prevents contradictions and enables the Agent to make consistent follow-up decisions.

當 Agent 稍後遇到相關問題時，它可以讀取決策紀錄，不只理解*什麼*被決定了，還有*為什麼*。這防止矛盾，並使 Agent 能做出一致的後續決策。

### Pattern 4: The Memory Index ── 記憶索引

**Problem 問題**: As the repo grows, the Agent doesn't know where to look. It wastes tokens reading irrelevant files or misses critical information buried in a forgotten folder.

隨著 repo 成長，Agent 不知道該看哪裡。它浪費 tokens 讀取無關的檔案，或錯過埋在被遺忘資料夾中的關鍵資訊。

**Solution 解法**: A `memory-index.md` that maps every important file in the repo, its purpose, and when to consult it.

一個 `memory-index.md` 映射 repo 中每個重要檔案、它的目的，以及何時查閱。

```markdown
# Memory Index

## Always Read at Startup
- `SOUL.md` — Agent identity and operating principles
- `DAILY.md` — Current state snapshot

## Read When Working on Deliverables
- `docs/deliverables/` — All deliverable files
- `docs/templates/` — Output templates and formats

## Read When Making Decisions
- `docs/decisions/` — All decision records
- `docs/constraints.md` — Budget, timeline, scope constraints

## Read When Communicating with Client
- `docs/stakeholders.md` — Who's who and preferences
- `SOUL.md` — Communication style guidelines
```

**Why it works 為什麼有效**: The index is cheap to load (~200 tokens) and acts as a routing table for the Agent's attention. Instead of scanning everything, the Agent reads the index and targets exactly the files relevant to its current task.

索引載入成本低（約 200 tokens），作為 Agent 注意力的路由表。Agent 不需要掃描一切，讀取索引就能精確定位與當前任務相關的檔案。

---

## 6. Memory and the Five-Layer Model ── 記憶與五層模型

Memory is not a single feature — it operates at every layer of the Agentic stack:

記憶不是單一功能——它在代理型堆疊的每一層都有運作：

| Layer 層 | Memory Role 記憶角色 | Example 範例 |
|---|---|---|
| **L1: LLM** 運算 | Context window as working memory 以 Context window 作為工作記憶 | The 200K tokens the model can "see" 模型能「看到」的 200K tokens |
| **L2: Tools** 工具 | File system and external storage as extended memory 以檔案系統和外部儲存作為擴展記憶 | Read/Write files, query databases 讀寫檔案、查詢資料庫 |
| **L3: Skills** 技能 | Skill definitions as procedural memory 以 Skill 定義作為程序性記憶 | SKILL.md files that encode "how to do X" 編碼「如何做 X」的 SKILL.md 檔案 |
| **L4: Agents** 代理 | Repo-as-memory as episodic and semantic memory 以倉庫即記憶作為情節和語義記憶 | SOUL.md, DAILY.md, decision records |
| **L5: Interface** 介面 | Conversation history as interaction memory 以對話歷史作為互動記憶 | Chat logs, user preferences, session context 對話紀錄、使用者偏好、工作階段脈絡 |

Notice the parallel to cognitive science:

注意與認知科學的平行：

- **Working memory** (L1): What you're thinking about right now 你正在想的事
- **Procedural memory** (L3): How to ride a bike — you don't need to think about it 怎麼騎腳踏車——你不需要想它
- **Episodic memory** (L4): What happened in the meeting last Tuesday 上週二的會議發生了什麼
- **Semantic memory** (L4): General knowledge about your domain 你領域的一般知識

Traditional software doesn't have this problem — a database application remembers everything by default. The Agentic paradigm reintroduces the memory challenge because the core computation layer (LLM) is stateless. The entire memory architecture must be **built**, not assumed.

傳統軟體沒有這個問題——資料庫應用預設就記得一切。代理型典範重新引入了記憶挑戰，因為核心運算層（LLM）是無狀態的。整個記憶架構必須被**建構**，而非假設存在。

---

## 7. Anti-Patterns: What Doesn't Work ── 反模式：什麼行不通

### Anti-Pattern 1: Conversation History as Memory 對話歷史作為記憶

**The temptation 誘惑**: Just keep the entire conversation going forever — the model remembers everything in the chat.

就讓整段對話永遠持續——模型在聊天中記得一切。

**Why it fails 為什麼失敗**:
- Context window eventually overflows, forcing lossy summarization 最終 Context window 溢出，迫使有損摘要
- "Lost in the middle" makes important early context unreliable 「中間遺失」使重要的早期脈絡不可靠
- No structure — the Agent must parse a wall of chat to find a single fact 沒有結構——Agent 必須解析一大片聊天來找到一個事實
- Cannot be shared between Agents or sessions 不能在 Agent 或工作階段之間共享
- Human cannot review or edit the "memory" 人類不能審查或編輯「記憶」

**Better approach 更好的方法**: Extract important information from conversations into structured state files. Let the conversation be volatile; let the state files be persistent.

從對話中提取重要資訊到結構化的狀態檔。讓對話是易失的；讓狀態檔是持久的。

### Anti-Pattern 2: Embedding Everything into a Vector Store 把一切嵌入向量儲存

**The temptation 誘惑**: Use RAG (Retrieval-Augmented Generation) with a vector database to store everything the Agent has ever seen.

用 RAG（檢索增強生成）搭配向量資料庫來儲存 Agent 見過的一切。

**Why it fails for most Agentic use cases 為什麼在大多數代理型使用情境中失敗**:
- Semantic search is approximate — retrieval may miss critical exact matches 語義搜尋是近似的——檢索可能錯過關鍵的精確匹配
- Embedding quality degrades for specialized domain language 嵌入品質在專業領域語言中退化
- No version history — you can't `git diff` a vector store 沒有版本歷史——你不能 `git diff` 一個向量儲存
- Infrastructure overhead — requires hosting, maintenance, and cost 基礎設施負擔——需要託管、維護和成本
- Black box — humans can't easily inspect what's stored or why it was retrieved 黑箱——人類不能輕易檢視儲存了什麼或為什麼被檢索

**When vector stores ARE appropriate 什麼時候向量儲存是合適的**: Large-scale knowledge bases with thousands of documents where the Agent can't predict which document is relevant. For project-scale memory (dozens to hundreds of files), structured Markdown files in a Git repo are simpler, cheaper, more transparent, and more reliable.

大規模知識庫，有數千份文件，Agent 無法預測哪份文件相關時。對於專案規模的記憶（數十到數百個檔案），Git repo 中的結構化 Markdown 檔案更簡單、更便宜、更透明、更可靠。

### Anti-Pattern 3: Monolithic State Files 單體式狀態檔

**The temptation 誘惑**: Put all project state into a single massive `STATE.md` file.

把所有專案狀態放入一個巨大的 `STATE.md` 檔案。

**Why it fails 為什麼失敗**:
- One file grows to thousands of lines, consuming excessive context window 一個檔案成長到數千行，消耗過多 context window
- Agent reads irrelevant sections for every task Agent 在每個任務中都讀取無關的段落
- Merge conflicts when multiple sessions update concurrently 多個工作階段同時更新時產生合併衝突
- Violates the "Separate Definition from State" design principle 違反「將定義與狀態分開」的設計原則

**Better approach 更好的方法**: One file per concern — DAILY.md for current state, MILESTONES.md for timeline, separate decision records, separate deliverable files. Small, focused files that the Agent loads selectively.

每個關注點一個檔案——DAILY.md 管當前狀態、MILESTONES.md 管時間線、獨立的決策紀錄、獨立的交付物檔案。小而聚焦的檔案，Agent 選擇性載入。

---

## 8. The State of the Art ── 技術現況

Memory is the most actively evolving area of Agentic architecture. Here's where leading systems stand:

記憶是代理型架構中最活躍演化的領域。以下是領先系統的現況：

| System 系統 | Working Memory | Session Memory | Persistent Memory |
|---|---|---|---|
| **ChatGPT** | Context window | Conversation history | Memory feature (limited, auto-summarized) 記憶功能（有限、自動摘要） |
| **Claude.ai** | Context window | Conversation + Projects | Project knowledge (limited) 專案知識（有限） |
| **Claude Code** | Context window + auto-compaction | File system + CLAUDE.md | Git repo + memory files Git repo + 記憶檔案 |
| **Cowork** | Context window + auto-compaction | File system + session files | Workspace folder + artifacts 工作區資料夾 + artifacts |
| **Cursor** | Context window | File system + .cursorrules | Repository state |
| **Custom Agents** 自訂 Agent | Context window | File system | Full repo-as-memory (SOUL.md, DAILY.md, etc.) 完整倉庫即記憶 |

The trend is clear: systems are moving toward **file-based persistent memory** with **Git as the version control layer**. The more mature the system, the more sophisticated its memory architecture.

趨勢很明顯：系統正朝向**基於檔案的持久記憶**配合 **Git 作為版本控制層**發展。系統越成熟，記憶架構越精密。

---

## 9. Design Principles for Agent Memory ── Agent 記憶的設計原則

From real-world deployments, six principles emerge:

從真實部署中，浮現六個原則：

**Principle 1: Never Depend on Conversation History for Critical State 永遠不要依賴對話歷史來保存關鍵狀態**

Conversations are volatile. They get summarized, truncated, or lost. Any information that matters beyond the current session must be written to a file.

對話是易失的。它們會被摘要、截斷或遺失。任何超越當前工作階段重要的資訊都必須寫入檔案。

**Principle 2: Make Memory Human-Readable 讓記憶人類可讀**

If a human can't read and understand the Agent's memory files, the system is a black box. Use Markdown, not binary formats or proprietary schemas.

如果人類不能讀取和理解 Agent 的記憶檔案，系統就是黑箱。使用 Markdown，不要用二進位格式或專有 schema。

**Principle 3: Separate What Changes Often from What Changes Rarely 將經常改變的和很少改變的分開**

SOUL.md (identity) changes rarely. DAILY.md (status) changes every session. Deliverable files change when being actively worked on. Mixing change frequencies in one file creates unnecessary noise.

SOUL.md（身份）很少改變。DAILY.md（狀態）每次工作階段都改變。交付物檔案在被積極處理時改變。在一個檔案中混合不同的變更頻率會產生不必要的噪音。

**Principle 4: Write State at Session End, Read State at Session Start 工作階段結束時寫入狀態，工作階段開始時讀取狀態**

This is the fundamental contract of session-based memory. If the Agent crashes or the session ends unexpectedly, the worst case is losing one session's work — not all accumulated memory.

這是基於工作階段的記憶的基本契約。如果 Agent 崩潰或工作階段意外結束，最壞的情況是遺失一次工作階段的工作——而非所有累積的記憶。

**Principle 5: Index Everything 為一切建索引**

A memory system is only as good as its retrieval. Maintain a memory index that tells the Agent where to look for what. The index itself should be cheap to load (under 500 tokens).

記憶系統只有在能檢索時才有價值。維護一個記憶索引，告訴 Agent 在哪裡找什麼。索引本身載入成本應低（500 tokens 以下）。

**Principle 6: Use Git for Everything 用 Git 處理一切**

Version control isn't just for code. It's the infrastructure layer that makes Agent memory auditable, reversible, shareable, and trustworthy.

版本控制不只是用於程式碼。它是讓 Agent 記憶可審計、可逆轉、可分享、可信任的基礎設施層。

---

## 10. Looking Forward ── 展望未來

The memory problem is far from solved. Current approaches work well for project-scale use cases (dozens of files, single-team scope), but significant challenges remain:

記憶問題遠未解決。目前的方法在專案規模的使用情境（數十個檔案、單一團隊範圍）運作良好，但仍有重大挑戰：

**The Cross-Project Memory Challenge 跨專案記憶挑戰**: An Agent that managed Project A knows things relevant to Project B — but if they're in separate repos, that knowledge is siloed. How do you build memory that spans projects without creating an unmanageable monolith?

管理 A 專案的 Agent 知道與 B 專案相關的事——但如果它們在不同的 repo，知識就被隔離了。如何建構跨專案的記憶又不會變成無法管理的龐然大物？

**The Memory Curation Challenge 記憶策展挑戰**: Over time, memory files accumulate outdated information. Who decides what to keep, what to archive, and what to discard? Currently, this requires human judgment — but it shouldn't forever.

隨時間推移，記憶檔案累積過時的資訊。誰來決定保留什麼、歸檔什麼、丟棄什麼？目前，這需要人類判斷——但不應該永遠如此。

**The Privacy and Access Control Challenge 隱私與存取控制挑戰**: When multiple Agents share a repo, which Agent should see which memories? A project manager Agent and a content creator Agent working on the same project may need different views of the same memory.

當多個 Agent 共享一個 repo 時，哪個 Agent 應該看到哪些記憶？在同一專案工作的專案經理 Agent 和內容創作者 Agent 可能需要相同記憶的不同視角。

These challenges point toward an emerging discipline: **Agent Memory Engineering** — the systematic design of how AI systems accumulate, organize, retrieve, and prune knowledge across time and contexts.

這些挑戰指向一個正在浮現的學科：**Agent 記憶工程**——系統性地設計 AI 系統如何跨時間和脈絡累積、組織、檢索和修剪知識。

The repo-as-memory pattern is the first mature solution. It won't be the last.

倉庫即記憶模式是第一個成熟的解決方案。它不會是最後一個。

---

## References 參考資料

1. Anthropic. ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — 2024
2. Liu, J., et al. ["Dive into Claude Code"](https://arxiv.org/abs/2604.14228) — arXiv, 2025
3. Mei, K., Li, Z., et al. ["AIOS: LLM Agent Operating System"](https://arxiv.org/abs/2403.16971) — COLM 2025
4. Anthropic. [Agent Skills Open Standard](https://github.com/anthropics/skills) — GitHub, 2025

---

*Previous: [Skill Composition Patterns ←](skill-composition.md)*
*Next: [Agentic Design Patterns →](agentic-design-patterns.md)*
