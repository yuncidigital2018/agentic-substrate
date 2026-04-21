# The Five-Layer Model: A Deep Dive
# 五層架構模型：深度解析

> *"The future of software is already here — it's just unevenly distributed across five layers."*
> *「軟體的未來已經到來——只是不均勻地分佈在五個層次之中。」*

---

## 1. Start From What You Already Know ── 從你已經知道的開始

Before we explain the five-layer model, let's look at **what's actually happening right now** — the tools you're already using, the patterns you're already seeing.

在解釋五層模型之前，讓我們先看看**現在正在發生什麼**——你已經在使用的工具、你已經在觀察到的模式。

### The LLM as a Cloud Brain ── LLM 作為雲端大腦

LLMs (Claude, GPT, Gemini, Grok, Llama...) are essentially **cloud brains** — extremely intelligent, capable of reasoning, code generation, analysis, and natural language understanding. They exist as API endpoints in data centers, or increasingly, as local models running on your own hardware.

LLM（Claude、GPT、Gemini、Grok、Llama……）本質上是**雲端大腦**——極度聰明，具備推理、程式碼生成、分析和自然語言理解能力。它們作為 API 端點存在於資料中心，或越來越多地作為本地模型運行在你的硬體上。

This is the foundation. Everything else builds on this raw intelligence.

這是基礎。其他一切都建立在這種原始智能之上。

### The Chat Window: Simplest Use ── 對話窗口：最單純的使用

The way most people experience this intelligence today is through **a chat window**: ChatGPT, Gemini, Grok, Claude.ai. You type a question, you get an answer.

大多數人今天體驗這種智能的方式是透過**對話窗口**：ChatGPT、Gemini、Grok、Claude.ai。你打一個問題，得到一個答案。

This is real. This is useful. But this is also **the simplest possible use** — like using a supercomputer to run a calculator app. The chat window is just one interface to a much deeper system.

這是真實的。這是有用的。但這也是**最單純的使用方式**——就像用超級電腦來跑計算機 App。對話窗口只是一個更深層系統的其中一個介面。

### Skills: When LLM Becomes Software ── Skills：當 LLM 變成軟體

The real shift happens when you move from "ask a question, get an answer" to **structured workflows with defined processes, validation, and composability**.

真正的轉變發生在從「問一個問題，得到一個答案」轉到**有定義流程、驗證和可組合性的結構化工作流程**。

In Claude Code and Cowork, you can create **Skills** — Markdown files (`.md`) that define a complete processing workflow: what triggers it, what steps to follow, what to validate, what to produce. When a Skill is activated, the LLM doesn't just "chat" — it follows a structured, iterative process:

在 Claude Code 和 Cowork 中，你可以建立 **Skills**——Markdown 檔案（`.md`）定義完整的處理工作流程：什麼觸發它、要遵循什麼步驟、驗證什麼、產出什麼。當 Skill 被啟動時，LLM 不只是「聊天」——它遵循一個結構化的迭代流程：

```
Skill activated → Read inputs → Process step by step →
  → Produce intermediate records → Validate → Iterate →
    → Produce final output

Skill 啟動 → 讀取輸入 → 逐步處理 →
  → 產出中間紀錄 → 驗證 → 迭代 →
    → 產出最終成果
```

This is where LLM stops being a chatbot and starts being **software** — linear, iterative, producing work records and half-products along the way, until the final deliverable is complete.

這就是 LLM 從聊天機器人轉變為**軟體**的地方——線性、迭代、在過程中產出工作紀錄和半成品，直到最終交付物完成。

### Skills Can Be Big or Small ── Skills 可大可小

Skills are flexible in scope:

Skills 的範圍很彈性：

**A small Skill** might be a company's basic data — rarely changing, but frequently needed. Build it once, call it whenever. If designed well, it functions like a **controlled RAG** (Retrieval Augmented Generation) — an internal database the LLM can query without hallucinating, because the data is curated and structured. Unlike regular `.md` working files that get constantly modified during work, a well-designed Data Skill stays stable.

**小型 Skill** 可能是公司的基本資料——極少變動，但經常需要。建好一次，需要時就呼叫。如果設計得好，它的功能就像**受控的 RAG**（檢索增強生成）——一個 LLM 可以查詢而不會幻覺的內部資料庫，因為資料是經過策展和結構化的。與在工作中不斷被修改的一般 `.md` 工作檔不同，設計良好的 Data Skill 保持穩定。

**A large Skill** might orchestrate an entire project pipeline — guiding chapter-by-chapter authoring with built-in validation at each step, tracking progress, and producing formatted deliverables.

**大型 Skill** 可能調度整個專案流程——引導逐章撰寫，每步都有內建的驗證，追蹤進度，產出格式化的交付物。

### The "a235bc1e" Insight: Skills Compose Like Hash Functions ── 雜湊組合的洞見

Here's where it gets powerful. If you have two linear Skill chains:

這裡是它變得強大的地方。如果你有兩條線性 Skill 鏈：

```
Chain A:  [a] → [b] → [c] → [d] → [e]     (e.g., a proposal writing pipeline)
Chain 1:  [1] → [2] → [3] → [4] → [5]     (e.g., a project tracking pipeline)
```

As long as each Skill's input/output contracts are well-defined (in Markdown), the LLM can **dynamically compose** them based on the task's actual needs:

只要每個 Skill 的輸入/輸出契約有良好的定義（用 Markdown），LLM 就可以根據任務的實際需求**動態組合**：

```
Composed: [a] → [2] → [3] → [5] → [b] → [c] → [1] → [e]
```

This is the new form of software: **individual functional units, callable via LLM, composable into whatever workflow the situation demands**. Not pre-coded paths. Not rigid pipelines. Dynamic, intent-driven composition.

這是軟體的新形式：**個別的功能單元，可透過 LLM 呼叫，可組合成情境所需的任何工作流程**。不是預先寫好的路徑。不是僵硬的管線。動態的、意圖驅動的組合。

### Agents: The Persistent Colleague ── Agent：持續性的同事

Beyond Skills, there are **Agents** — persistent AI assistants that maintain continuity across sessions. They read the project state at startup, execute tasks, write results back, and shut down. Next session, they resume from where they left off. Over time, they grow with you, becoming increasingly familiar with your projects, preferences, and work patterns.

在 Skills 之上，還有 **Agents**——跨工作階段維持連續性的持續性 AI 助理。它們在啟動時讀取專案狀態，執行任務，將結果寫回，然後關閉。下次工作階段，從上次結束的地方繼續。隨時間推移，它們與你一起成長，越來越熟悉你的專案、偏好和工作模式。

### The Transition Period: Three Tracks ── 過渡時期：三條軌道

Right now, we're in a transition period where AI capabilities are being integrated across three parallel tracks:

現在我們處於一個過渡時期，AI 能力正在三條平行軌道上被整合：

```
Track 1: Cloud / SaaS
雲端/SaaS 軌道
┌──────────────────────────────────────────────────────┐
│  Existing SaaS services adding AI via API            │
│  現有 SaaS 服務透過 API 加入 AI                       │
│                                                      │
│  Notion AI, Canva AI, Figma AI, Salesforce Einstein  │
│  → Connecting to LLMs to provide "near-AI" features  │
│    串接 LLM 提供「類 AI」功能                         │
└──────────────────────────────────────────────────────┘

Track 2: Local / Desktop
本地/桌面軌道
┌──────────────────────────────────────────────────────┐
│  CLI + IDE + local models building complete           │
│  on-device AI integration                            │
│  透過 CLI + IDE + 本地模型建構完整的地端 AI 整合       │
│                                                      │
│  Claude Code, Cursor, VS Code + Copilot,             │
│  Windsurf, Ollama, AnythingLLM                       │
│  → Full agentic capability on your machine           │
│    在你的電腦上實現完整的代理能力                      │
└──────────────────────────────────────────────────────┘

Track 3: Mobile / Edge
行動/端側軌道
┌──────────────────────────────────────────────────────┐
│  iOS and Android integrating intelligence            │
│  into the operating system itself                    │
│  iOS 和 Android 將智能整合進作業系統本身               │
│                                                      │
│  Apple Intelligence, Google Gemini Nano,             │
│  Samsung Galaxy AI                                   │
│  → Iterating toward on-device AI services            │
│    朝向裝置端 AI 服務迭代前進                         │
└──────────────────────────────────────────────────────┘
```

All three tracks are converging toward the same destination: **a world where LLM is the computation layer, Skills are the functional units, and Agents orchestrate the workflow**. They just approach it from different starting points.

三條軌道都在匯聚到同一個目的地：**LLM 是運算層、Skills 是功能單元、Agent 調度工作流程的世界**。它們只是從不同的起點出發。

---

## 2. So Why Five Layers? ── 那為什麼是五層？

### How This Model Was Built ── 這個模型是怎麼建立的

The Five-Layer Model is not a proprietary specification from any AI company. It is a **descriptive architectural model** — synthesized from three sources:

五層模型不是任何 AI 公司的私有規格。它是一個**描述性的架構模型**——從三個來源合成而來：

**Source 1: Observable system architecture ── 來源一：可觀察的系統架構**

If you look at how Claude Code actually works, you can observe distinct layers: the LLM processes text (computation), tools read/write files and execute code (tools), SKILL.md files define workflows (skills), a `while` loop orchestrates everything with memory (agent), and CLI/Cowork present results to humans (interface). These layers aren't a theory imposed on the system — they're what you see when you examine the system.

如果你觀察 Claude Code 實際如何運作，你能看到不同的層次：LLM 處理文字（運算）、工具讀寫檔案和執行程式碼（工具）、SKILL.md 檔案定義工作流程（技能）、一個 `while` 迴圈搭配記憶調度一切（代理）、CLI/Cowork 向人類呈現結果（介面）。這些層次不是強加於系統的理論——它們是你檢視系統時看到的東西。

**Source 2: Existing academic and industry frameworks ── 來源二：既有的學術和產業框架**

Several researchers and organizations have described parts of this picture:

幾位研究者和組織已經描述了這幅圖的部分：

| Framework 框架 | What They Describe 描述了什麼 | What They Miss 遺漏了什麼 |
|---|---|---|
| **Andrew Ng's 4 Patterns** | Reflection, Tool Use, Planning, Multi-Agent — how agents reason and coordinate | No Skill layer; focuses on reasoning patterns, not system architecture |
| Andrew Ng 的 4 種模式 | 反思、工具使用、規劃、多代理——Agent 如何推理和協調 | 沒有 Skill 層；聚焦推理模式，非系統架構 |
| **Anthropic's "Building Effective Agents"** | Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer | Practical patterns but no unifying layer model |
| Anthropic 的「建構有效 Agent」 | 提示鏈接、路由、平行化、調度-工人、評估-優化 | 實用模式但無統一的分層模型 |
| **AIOS (Rutgers University)** | LLM as OS kernel — complete system architecture with process scheduling | Academic; treats LLM as kernel (too low-level); misses the Skill abstraction |
| AIOS（羅格斯大學） | LLM 作為 OS 核心——完整系統架構含進程排程 | 學術性；把 LLM 當核心（太底層）；遺漏 Skill 抽象 |
| **SKILL.md Standard** | Standardized format for defining Skills | Defines the format but not the surrounding architecture |
| SKILL.md 標準 | 定義 Skills 的標準化格式 | 定義了格式但沒有周邊架構 |
| **Superpowers (obra)** | Working Skills + plugin installation for Claude Code and Cursor | Engineer-only; no conceptual framework explaining why it works |
| Superpowers（obra） | 可用的 Skills + Claude Code 和 Cursor 的插件安裝 | 只限工程師；沒有解釋為什麼有效的概念框架 |

Each describes a piece. None provides the full picture. The Five-Layer Model is the **connective tissue** that ties these perspectives together into a coherent architecture.

每個都描述了一塊。沒有一個提供完整的圖像。五層模型是把這些觀點綁在一起成為連貫架構的**結締組織**。

**Source 3: Practitioner experience ── 來源三：實踐者經驗**

This framework emerged from building 40+ real-world AI-native projects — not coding projects, but knowledge work: proposal writing, project management, team coordination, document production. In these projects, AI agents didn't just assist. They operated as collaborative team members, using Skills to execute domain-specific workflows. The patterns that emerged from this practice are what the five layers describe.

這個框架從建構 40 多個真實 AI 原生專案中浮現——不是程式設計專案，而是知識工作：提案撰寫、專案管理、團隊協作、文件製作。在這些專案中，AI Agent 不只是輔助。它們作為協作團隊成員運作，使用 Skills 執行特定領域的工作流程。從這些實踐中浮現的模式，就是五層所描述的。

### The Five Layers, Explained ── 五層，解釋

Each layer represents a **qualitative leap** in what becomes possible:

每一層代表能力上的**質變**：

```
┌─────────────────────────────────────────────────────────┐
│  Layer 5: Interface 介面層                               │
│  "How humans experience the system"                      │
│  Chat window │ Cowork │ CLI │ API │ Ambient device       │
├─────────────────────────────────────────────────────────┤
│  Layer 4: Agent 代理層                                   │
│  "How the system sustains purpose across time"           │
│  Memory │ Identity │ Orchestration │ Repo-as-state       │
├─────────────────────────────────────────────────────────┤
│  Layer 3: Skill 技能層                                   │
│  "How the system organizes work into reusable units"     │
│  Workflow definition │ Validation │ Composition           │
├─────────────────────────────────────────────────────────┤
│  Layer 2: Tool & Protocol 工具與協議層                    │
│  "How the system acts on the world"                      │
│  File I/O │ Web │ Code exec │ APIs │ MCP                │
├─────────────────────────────────────────────────────────┤
│  Layer 1: LLM Computation 運算層                         │
│  "How the system thinks"                                 │
│  Inference │ Reasoning │ Language │ Multimodal            │
└─────────────────────────────────────────────────────────┘
```

Remove any layer and the system degrades:

移除任何一層，系統就會退化：

- Without Layer 1: no intelligence — just static scripts
  沒有第一層：沒有智能——只有靜態腳本
- Without Layer 2: intelligence trapped in a box — can think but can't act
  沒有第二層：智能被困在盒子裡——能想但不能做
- Without Layer 3: every task starts from zero — no accumulated workflow knowledge
  沒有第三層：每個任務都從零開始——沒有累積的工作流程知識
- Without Layer 4: no continuity — each session is a stranger
  沒有第四層：沒有連續性——每次工作階段都像陌生人
- Without Layer 5: no human access — a brilliant system nobody can use
  沒有第五層：沒有人類入口——一個無人能用的天才系統

---

## 3. Where Today's Products Sit ── 今天的產品在哪裡

This is the key to understanding the model: **every AI product you use today implements some subset of these five layers**. The difference between products is which layers they cover and how deeply.

這是理解模型的關鍵：**你今天使用的每個 AI 產品都實作了這五層的某個子集**。產品之間的差異在於它們涵蓋哪些層以及多深入。

### Product-to-Layer Mapping ── 產品對應層級

```
                    Layer 1   Layer 2   Layer 3   Layer 4   Layer 5
                    LLM       Tools     Skills    Agent     Interface
                    運算層     工具層    技能層     代理層    介面層
─────────────────────────────────────────────────────────────────────
ChatGPT / Gemini    ●         ◐         ○         ○         ● (Chat)
(web chat)          (cloud)   (search,  (no       (no       
                              code)     reusable  memory    
                                        skills)   across    
                                                  sessions) 

Claude.ai           ●         ◐         ○         ◐         ● (Chat)
(web chat)          (cloud)   (search,  (Projects (limited  
                              artifacts) as proto- memory)  
                                        skills)            

Claude Code         ●         ●         ●         ●         ● (CLI)
(CLI)               (API)     (full     (SKILL.md (CLAUDE.md,
                              file,     system)   hooks,    
                              bash,               memory)   
                              MCP)                          

Cowork              ●         ●         ●         ●         ● (Desktop)
(desktop)           (API)     (full     (installed (session  
                              file,     Skills,   memory,   
                              bash,     plugins)  artifacts)
                              MCP)                          

Cursor / Windsurf   ●         ●         ◐         ◐         ● (IDE)
(IDE)               (API)     (file,    (.cursorrules (limited
                              terminal) as proto-  memory)  
                                        skills)            

Notion AI /         ◐         ◐         ○         ○         ● (Web app)
Canva AI            (via API) (limited  (no       (no       
(SaaS + AI)                   to app's  reusable  agent     
                              scope)    skills)   loop)     

Apple Intelligence  ◐         ◐         ○         ○         ● (OS)
/ Galaxy AI         (on-      (system   (pre-     (limited) 
(mobile OS)         device)   actions)  defined             
                                        only)               

─────────────────────────────────────────────────────────────────────
● = Full implementation  ◐ = Partial  ○ = Missing/minimal
```

### What This Map Reveals ── 這張地圖揭示了什麼

**The products that feel most "agentic" are the ones that implement all five layers.** Claude Code and Cowork reach full coverage. Most chat interfaces cover only Layer 1 + Layer 5 (brain + window). SaaS products adding AI typically only connect Layer 1 partially, through their existing interface.

**感覺最「代理化」的產品，是實作了全部五層的產品。** Claude Code 和 Cowork 達到完整覆蓋。大多數對話介面只涵蓋第一層 + 第五層（大腦 + 窗口）。加入 AI 的 SaaS 產品通常只透過現有介面部分連接第一層。

**The Skill layer (Layer 3) is the differentiator.** This is what separates "AI-powered" from "AI-native." Products without a Skill layer can answer questions, but they can't accumulate domain expertise into reusable, composable workflows. Every task starts from zero.

**技能層（第三層）是區分因素。**這是區分「AI 加持」和「AI 原生」的關鍵。沒有技能層的產品可以回答問題，但無法將領域專長累積為可重用、可組合的工作流程。每個任務都從零開始。

---

## 4. Layer-by-Layer Deep Dive ── 逐層深度解析

### Layer 1: LLM Computation ── LLM 運算層

**The cloud brain.** 雲端大腦。

```
┌─────────────────────────────────────────────────────────┐
│                  LLM Computation Layer                   │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │   Language   │  │  Reasoning  │  │   Generation    │ │
│  │ Understanding│  │   & Logic   │  │   & Synthesis   │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐ │
│  │  Multimodal │  │    Code     │  │     Intent      │ │
│  │  Processing │  │ Generation  │  │  Comprehension  │ │
│  └─────────────┘  └─────────────┘  └─────────────────┘ │
│                                                         │
│  Properties:                                            │
│  • Stateless (each call independent)                    │
│  • Probabilistic (not deterministic)                    │
│  • Context-window bounded                               │
│  • Accessed via API or local inference                   │
└─────────────────────────────────────────────────────────┘
```

#### Three Access Modes ── 三種存取模式

| Mode 模式 | Latency 延遲 | Privacy 隱私 | Cost 成本 | Example 範例 |
|---|---|---|---|---|
| **Cloud API** 雲端 | ~1-5s | Data leaves device | Per-token 按 token 計費 | Claude API, GPT API, Gemini API |
| **Local Inference** 本地推理 | ~0.5-30s | Data stays on device | Hardware cost 硬體成本 | Ollama + Llama, MLX, LM Studio |
| **Edge / On-device** 端側 | ~0.1-2s | Fully private 完全私密 | Device purchase | Apple Intelligence, Gemini Nano |

The critical design insight: **the upper layers don't need to know which mode is being used**. A Skill that works with Claude via API should work with a local model too. This is why Layer 1 is a clean abstraction — it's a swappable computation engine.

關鍵設計洞見：**上層不需要知道使用哪種模式**。一個透過 API 使用 Claude 的 Skill，也應該能與本地模型運作。這就是為什麼第一層是乾淨的抽象——它是可替換的運算引擎。

#### Statelessness: Feature, Not Bug ── 無狀態：是特性，不是缺陷

The LLM is stateless by nature — each API call is independent, with no memory of previous calls. The "memory" you experience when chatting with Claude is an **illusion created by Layer 4** (the Agent layer), which feeds conversation history back into each new LLM call. The LLM itself never "remembers" anything.

LLM 天生無狀態——每次 API 呼叫都是獨立的，不記得之前的呼叫。你在與 Claude 聊天時感受到的「記憶」，是**第四層（Agent 層）製造的幻象**，它把對話歷史回饋給每次新的 LLM 呼叫。LLM 本身從不「記得」任何事。

This is actually a design advantage: any instance can handle any request (scalability), one user's session can't contaminate another's (isolation), and the same input produces the same probability distribution (reproducibility).

這其實是設計優勢：任何實例都能處理任何請求（可擴展性）、一個使用者的工作階段不會污染另一個（隔離性）、相同的輸入產生相同的機率分佈（可重現性）。

#### The Context Window ── 上下文窗口

The single most important constraint. Everything the LLM "knows" during a single call must fit in this window:

最重要的單一限制。LLM 在一次呼叫中「知道」的一切，都必須裝進這個窗口：

```
Context Window (e.g., 200K tokens):
┌───────────────────────────────────────────────────────┐
│ System Prompt (Skill definitions, persona, rules)     │  ~2-5K
├───────────────────────────────────────────────────────┤
│ Conversation History (previous turns)                 │  ~50-100K
├───────────────────────────────────────────────────────┤
│ Active Context (current files, tool results)          │  ~10-30K
├───────────────────────────────────────────────────────┤
│ ← Remaining: Available for reasoning & generation →   │  Variable
└───────────────────────────────────────────────────────┘
```

This is why **Skill design matters** — a poorly designed Skill dumps 50K tokens of raw data into the window; a well-designed Skill provides only the relevant subset.

這就是為什麼 **Skill 設計很重要**——設計不良的 Skill 把 50K token 的原始資料丟進窗口；設計良好的 Skill 只提供相關子集。

#### Layer 1 Design Principles ── 第一層設計原則

1. **Treat the LLM as a commodity** 把 LLM 當商品看待: Design Skills and Agents to be LLM-agnostic where possible. Today's best model is tomorrow's baseline.
   盡可能設計 LLM 無關的 Skills 和 Agents。今天最好的模型是明天的基準線。

2. **Budget your context window** 預算化管理上下文窗口: Know how many tokens your Skill definitions, conversation history, and active files consume. Leave room for reasoning.
   了解你的 Skill 定義、對話歷史和活躍檔案消耗多少 token。留空間給推理。

3. **Don't fight statelessness** 不要與無狀態對抗: Push state management to Layer 4. Use files and repos, not prompt engineering tricks.
   把狀態管理推到第四層。使用檔案和 repo，而不是 prompt 工程技巧。

---

### Layer 2: Tool & Protocol ── 工具與協議層

**The hands and eyes.** 手和眼。

Without Layer 2, the LLM is a brain in a jar — it can think brilliantly but can't touch the world. This layer provides the sensory and motor capabilities.

沒有第二層，LLM 就是瓶中的大腦——能聰明地思考但觸碰不到世界。這一層提供感知和動作能力。

#### Tool Categories ── 工具分類

| Category 類別 | Examples 範例 | Direction 方向 |
|---|---|---|
| **Read** 讀取 | File read, web search, database query | World → LLM |
| **Write** 寫入 | File write, send message, create record | LLM → World |
| **Execute** 執行 | Run code, shell command, API call | LLM → World → LLM |
| **Observe** 觀察 | Screenshot, monitor process, check status | World → LLM (continuous) |

Every tool, regardless of complexity, follows the same pattern: a name, a description, typed parameters, and a deterministic function. **Tools themselves are deterministic** — `read_file("/doc.md")` always returns the same content. The AI decision is *which* tool to call and with *what* parameters — that happens in the upper layers.

每個工具，不論複雜度，都遵循相同的模式：名稱、描述、型別化參數、確定性函數。**工具本身是確定性的**——`read_file("/doc.md")` 總是回傳相同內容。AI 的決策是呼叫*哪個*工具、用*什麼*參數——這發生在上層。

#### MCP: The USB Standard for AI ── MCP：AI 的 USB 標準

The Model Context Protocol (MCP) is to Agentic software what USB was to hardware: a standard interface that lets any tool connect to any agent without custom integration.

Model Context Protocol（MCP）之於代理型軟體，就如 USB 之於硬體：一個讓任何工具連接任何 Agent 的標準介面。

```
Before MCP: N agents × M tools = N×M integrations  (explosion)
After MCP:  N agents + M tools = N+M integrations  (linear)
```

This is the same mathematical advantage that made USB, TCP/IP, and HTTP successful — the network effect applied to tool interoperability.

這與 USB、TCP/IP 和 HTTP 成功的數學優勢相同——將網路效應應用於工具互操作性。

#### The Tool Discovery Problem ── 工具發現問題

More tools available means more capability, but also more tokens consumed listing them and more cognitive load for the LLM. Well-designed systems use **progressive discovery**:

更多可用工具意味著更多能力，但也消耗更多 token 列出它們，增加 LLM 的認知負擔。設計良好的系統使用**漸進式發現**：

```
Level 0: Name only               ~5 tokens per tool
Level 1: Name + description      ~20-50 tokens per tool
Level 2: Full schema on demand   ~200-500 tokens per tool
```

Claude Code uses this strategy — deferred tools show only their name until explicitly requested. This keeps the base token cost low while maintaining full capability.

Claude Code 使用這種策略——延遲工具只顯示名稱，直到明確請求。這保持了基礎 token 成本低，同時維持完整能力。

#### Layer 2 Design Principles ── 第二層設計原則

1. **Tools should be dumb** 工具應該簡單: A tool reads a file. It doesn't decide *which* file to read. Decision-making belongs to the upper layers.
   工具讀取檔案。它不決定讀*哪個*檔案。決策屬於上層。

2. **Protocol over integration** 協議優於整合: Prefer standardized protocols (MCP) over custom API wrappers.
   偏好標準化協議（MCP）而非自定義 API 包裝。

3. **Fail loudly, recover gracefully** 大聲失敗，優雅恢復: When a tool fails, return a clear error. Let the upper layers decide how to handle it.
   工具失敗時，回傳清楚的錯誤。讓上層決定如何處理。

---

### Layer 3: Skill ── 技能層

**The new "App."** 新型態的「App」。

This is the most important conceptual contribution of the Agentic Substrate framework. While other frameworks focus on agents (Layer 4) or tools (Layer 2), we argue that the **Skill is the fundamental unit of Agentic software** — just as the "App" was the fundamental unit of mobile software.

這是 Agentic Substrate 框架最重要的概念貢獻。當其他框架聚焦 Agent（第四層）或工具（第二層）時，我們主張 **Skill 是代理型軟體的基本單元**——就像「App」是行動軟體的基本單元。

For the complete anatomy (seven components, five types, maturity model), see [Anatomy of a Skill](skill-anatomy.md). Here we focus on Layer 3's **architectural role** within the stack.

完整解剖（七大組件、五種類型、成熟度模型）請見[技能模組解剖學](skill-anatomy.md)。

#### Why Skills Must Be a Separate Layer ── 為什麼 Skills 必須是獨立的一層

```
Without Skills (tools directly serving Agent):
沒有 Skills（工具直接服務 Agent）：

  User: "Create a project status report"

  Agent must figure out EVERYTHING from scratch:
  → What does a status report look like?
  → Which files to read? What format?
  → How to validate? What domain conventions?
  → Result: inconsistent every time, context window
    filled with ad-hoc instructions

With Skills (mediating layer):
有 Skills（居中調解層）：

  User: "Create a project status report"

  Agent recognizes → [project-status-tracker] Skill
  → Skill provides: template, inputs, validation, format
  → Agent follows the Skill's process
  → Result: consistent, validated, improvable
```

The key: **Skills encode domain knowledge that would otherwise be lost between sessions.** They are the institutional memory of *how work should be done*.

關鍵：**Skills 編碼了否則會在工作階段間流失的領域知識。**它們是*工作應該如何執行*的組織記憶。

#### Skill Stability vs. Working Files ── Skill 的穩定性 vs. 工作檔

This is a practical distinction that matters for system design:

這是對系統設計很重要的實務區分：

```
Working .md files (volatile):        Skill .md files (stable):
工作用 .md 檔（易變）：               Skill .md 檔（穩定）：

  work-record.md    ← changes daily     SKILL.md      ← rarely changes
  progress.md       ← updates per task   data.json     ← curated, versioned
  draft-ch03.md     ← iterates heavily   templates/    ← standardized

  → These are Layer 3 OUTPUTS           → These are Layer 3 DEFINITIONS
    這些是第三層的產出                     這些是第三層的定義
```

A well-designed Data Skill (like a company database) is stable — built once, curated carefully, called whenever needed. It functions as a **controlled RAG**: the LLM queries structured, verified data instead of searching the open web. This stability is what makes it reliable. Working files, by contrast, are meant to be created, modified, and finalized during the work process.

設計良好的 Data Skill（如公司資料庫）是穩定的——建立一次、仔細策展、需要時就呼叫。它的功能像是**受控的 RAG**：LLM 查詢結構化、經驗證的資料，而非搜尋開放網路。這種穩定性正是它可靠的原因。工作檔案則相反，它們是為了在工作過程中被建立、修改和定稿的。

#### The Skill Boundary Contract ── Skill 的邊界契約

Every Skill defines a clear contract with the layers above and below:

每個 Skill 定義了與上下層之間的清楚契約：

```
        Layer 4 (Agent)
             │
             │  Trigger: "When should this Skill activate?"
             │  Input:   "What does this Skill need?"
             │  Output:  "What does this Skill produce?"
             ▼
┌───────────────────────────────┐
│        Skill (Layer 3)        │
│                               │
│  Process Logic                │
│  Validation Rules             │
│  Domain Knowledge             │
└───────────────────────────────┘
             │
             │  Tool calls: "Read this" / "Write that"
             ▼
        Layer 2 (Tools)
```

#### Skill Loading: Token Economics ── Skill 載入：Token 經濟學

An Agent with 20 Skills doesn't load all their full definitions:

擁有 20 個 Skills 的 Agent 不會載入所有完整定義：

```
At rest (Level 1 summaries):   20 Skills × ~30 tokens = ~600 tokens
Active (one Skill triggered):  + ~500-2000 tokens for the active Skill
                               ─────────────────────────────────
                               Total: ~1000-2600 tokens

vs. loading all 20 fully:     20 × ~1000 = ~20,000 tokens  (wasteful)
```

#### Layer 3 Design Principles ── 第三層設計原則

1. **One Skill, one job** 一個 Skill，一個工作: If it does two unrelated things, split it. Composability comes from combining single-purpose Skills.
   做兩件不相關的事就拆分。可組合性來自組合單一用途的 Skills。

2. **Encode the expert, not just the steps** 編碼專家，不只是步驟: Capture judgment calls, "when to deviate," and validation criteria that only an experienced practitioner knows.
   捕捉判斷決策、「何時偏離」、只有經驗豐富的實踐者才知道的驗證標準。

3. **Design for composition** 為組合而設計: Every Skill should clearly define what it produces in a way that other Skills can consume. Markdown is the default interchange format.
   每個 Skill 都應清楚定義產出，讓其他 Skills 可以使用。Markdown 是預設的交換格式。

---

### Layer 4: Agent ── 代理層

**The persistent colleague.** 持續性的同事。

If Skills are the applications, the Agent is the operating system — but not for hardware resources. The Agent manages **cognitive resources**: which Skills to invoke, in what order, with what context, and how to maintain continuity across sessions.

如果 Skills 是應用程式，Agent 就是作業系統——但不是管理硬體資源。Agent 管理的是**認知資源**：呼叫哪些 Skills、以什麼順序、帶什麼上下文、如何跨工作階段維持連續性。

#### The Agent Loop: Surprisingly Simple ── Agent 迴圈：出乎意料地簡單

At its core, an Agent is a `while` loop. Claude Code's entire decision engine works like this:

核心上，Agent 就是一個 `while` 迴圈。Claude Code 的整個決策引擎是這樣運作的：

```
while (task not complete):
    context = gather(system_prompt, memory, conversation, files)
    response = llm.call(context)           ← Layer 1
    if response.has_tool_calls:
        results = execute(tool_calls)      ← Layer 2
        continue                           ← loop back
    else:
        return response to user            ← Layer 5
```

The profound insight from studying Claude Code's architecture: **only ~1.6% of the codebase is AI decision logic**. The other ~98.4% is deterministic infrastructure — permission checks, context assembly, error recovery, tool routing. The intelligence lives in the LLM (Layer 1), not in complex agent logic.

從研究 Claude Code 架構得到的深刻洞見：**只有約 1.6% 的程式碼是 AI 決策邏輯**。其餘約 98.4% 是確定性基礎設施——權限檢查、上下文組裝、錯誤恢復、工具路由。智能住在 LLM（第一層），不是在複雜的 Agent 邏輯中。

This validates a key design principle: **simplicity over complexity**. Don't build elaborate agent frameworks — build a simple loop and invest in assembling the right context.

這驗證了一個關鍵設計原則：**簡單勝過複雜**。不要建構精密的 Agent 框架——建構簡單的迴圈，把投資放在組裝正確的上下文。

#### Memory: The Illusion of Continuity ── 記憶：連續性的幻象

Memory is what transforms a stateless LLM into a persistent colleague. Layer 4 manages three tiers:

記憶是將無狀態的 LLM 轉變為持續性同事的關鍵。第四層管理三個層級：

```
┌────────────────────────────────────────────┐
│  Conversation Memory (Short-term)           │
│  對話記憶（短期）                            │
│  Lives in: Context window                   │
│  Duration: Current session only             │
├────────────────────────────────────────────┤
│  Project Memory (Medium-term)               │
│  專案記憶（中期）                            │
│  Lives in: CLAUDE.md, project .md files     │
│  Duration: Across sessions, per project     │
├────────────────────────────────────────────┤
│  Persistent Memory (Long-term)              │
│  持久記憶（長期）                            │
│  Lives in: Memory files, user preferences   │
│  Duration: Across all projects              │
└────────────────────────────────────────────┘
```

#### Repo-as-Memory: State That Survives ── Repo 即記憶：存活的狀態

For complex, long-running projects, the most robust memory strategy: use a **Git repository as the Agent's memory**.

對於複雜、長期運行的專案，最穩健的記憶策略：使用 **Git repository 作為 Agent 的記憶**。

```
Session N:
  [Boot] → git pull → read state files → understand "where we are"
        → execute tasks → update state files
        → git commit + push → [Shutdown]

Session N+1:
  [Boot] → git pull → read state files → see yesterday's results
        → continue from where we left off → ...
```

The Agent doesn't depend on conversation history. It reads the repo, rebuilds its understanding, executes, writes back, and shuts down. **The repo IS the memory.** Next session starts fresh from the repo state — no conversation replay needed.

Agent 不依賴對話歷史。它讀取 repo，重建理解，執行，寫回，然後關閉。**Repo 就是記憶。**下次工作階段從 repo 狀態重新開始——不需要重播對話。

#### Orchestration Patterns ── 調度模式

The Agent orchestrates Skills using patterns borrowed from team management:

Agent 使用借自團隊管理的模式來調度 Skills：

```
Sequential:    [A] → [B] → [C]        (Research → Draft → Review)
Parallel:      [A] ─┐
               [B] ─┼→ [Merge]        (Gather from 3 sources)
               [C] ─┘
Routing:       Input →┬→ [A] if X     (Different Skill per doc type)
                      ├→ [B] if Y
                      └→ [C] if Z
Eval-loop:     [Generate] → [Evaluate] (Draft → Validate → Revise)
                   ↑            │       until quality met
                   └────────────┘
```

These are the same patterns identified by Andrew Ng (Planning, Multi-Agent) and Anthropic (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer) — but here they're placed in context as **Layer 4 behaviors** operating on Layer 3 Skills.

這些與 Andrew Ng（規劃、多代理）和 Anthropic（提示鏈接、路由、平行化、調度-工人、評估-優化）識別的模式相同——但在這裡它們被放在上下文中，作為**第四層行為**操作第三層 Skills。

#### Layer 4 Design Principles ── 第四層設計原則

1. **Simple loop, smart context** 簡單迴圈，聰明上下文: Don't build complex control flow. Build a simple loop and invest in assembling the right context for each LLM call.
   不要建構複雜的控制流程。建構簡單的迴圈，投資在為每次 LLM 呼叫組裝正確的上下文。

2. **State lives in files, not in memory** 狀態存在檔案中，不在記憶體中: Write state to `.md` / `.yaml` / `.json` so the next session can resume without replaying conversation history.
   將狀態寫入 `.md` / `.yaml` / `.json`，讓下次工作階段可以不重播對話歷史就恢復。

3. **Orchestrate, don't micromanage** 調度，不要微管理: The Agent decides *which* Skills to invoke. It does not dictate *how* each Skill does its work.
   Agent 決定呼叫*哪些* Skills。它不指定每個 Skill *如何*執行工作。

---

### Layer 5: Interface ── 介面層

**How humans experience the system.** 人類如何體驗系統。

This layer encompasses every surface through which people interact with the Agentic stack.

這一層涵蓋人們與代理堆疊互動的每個表面。

#### The Interface Spectrum ── 介面光譜

```
Simplicity ◄──────────────────────────────────────────► Power

Chat         Cowork/        CLI/         API/          Ambient/
Window       Desktop        Terminal     Programmatic   Edge
  │            │               │            │             │
  ▼            ▼               ▼            ▼             ▼
"Ask a      "Work on a     "Direct      "System-to-   "AI is
question"   project        agent        system"        the room"
            together"      control"
```

| Interface 介面 | Who Uses It 使用者 | Layers Engaged 參與層級 | Example 範例 |
|---|---|---|---|
| **Chat** 對話 | Everyone 所有人 | L1 + L5 (mostly) | ChatGPT, Gemini, Claude.ai |
| **Collaborative** 協作 | Knowledge workers 知識工作者 | All 5 layers | Cowork, Claude Projects |
| **CLI** 命令列 | Developers 開發者 | L1-L4 deeply | Claude Code, Cursor terminal |
| **API** 程式化 | Engineers 工程師 | L1-L2 primarily | Claude API, OpenAI API |
| **Ambient** 環境 | Everyone (future) 所有人（未來） | All 5 layers | On-device AI-generated interfaces |

The critical insight: **a Skill should work identically regardless of which interface invokes it**. The same [document-reviewer] Skill produces the same validated output whether triggered from a chat window, Cowork desktop, CLI command, or API call. The interface is presentation; the Skill is logic.

關鍵洞見：**無論哪個介面呼叫，一個 Skill 都應該相同地運作**。同一個 [document-reviewer] Skill 無論從對話窗口、Cowork 桌面、CLI 命令或 API 呼叫觸發，都產出相同的驗證過的輸出。介面是呈現；Skill 是邏輯。

#### Layer 5 Design Principles ── 第五層設計原則

1. **Progressive complexity** 漸進式複雜度: Match the interface to the user's expertise level. Don't force CLI on everyone or simplify everything to chat.
   匹配介面與使用者的專業水平。

2. **Interface-independent Skills** 介面無關的 Skills: A Skill should work across all interfaces. The interface only changes how results are presented, not how work is done.
   Skill 應跨所有介面運作。介面只改變結果的呈現方式，不改變工作的執行方式。

3. **Human-in-the-loop by default** 預設人類在迴圈中: Until agents reach high maturity, keep human checkpoints for critical decisions.
   在 Agent 達到高成熟度之前，為關鍵決策保留人類檢查點。

---

## 5. Cross-Layer Dynamics ── 跨層動態

### Tracing a Real Request ── 追蹤一個真實請求

```
User types in Cowork (Layer 5):
  "Generate a weekly status report for the project"

  │
  ▼
Layer 4 (Agent):
  → Reads project memory (CLAUDE.md, recent files)
  → Recognizes this matches [project-status-tracker] Skill
  → Loads the Skill's full definition
  │
  ▼
Layer 3 (Skill):
  → Process: (1) gather data, (2) analyze, (3) format, (4) validate
  → Requests tool actions for step 1
  │
  ▼
Layer 2 (Tools):
  → git log --since="1 week ago"
  → Read open-issues.md, milestones.md
  → Returns data to Layer 3
  │
  ▼
Layer 1 (LLM):
  → Receives all context (Skill + data + instructions)
  → Synthesizes a coherent narrative
  → Applies validation criteria from the Skill
  │
  ▼
Layer 2 (Tools):
  → Writes status-report-2026-W16.md
  │
  ▼
Layer 4 (Agent):
  → Updates state: "Status report generated"
  → Commits to repo
  │
  ▼
Layer 5 (Interface):
  → Shows report to user with download link
  → "Here's your weekly status report."
```

### Layers Can Combine Independently ── 層與層可以獨立組合

This is what makes the model powerful: **the layers are not locked into one configuration**. Different products implement different combinations, and the combinations will keep evolving:

這是讓模型強大的原因：**層與層不是鎖死在一種配置中**。不同的產品實作不同的組合，而組合會持續演化：

```
Today (2025-2026):
今天：

  Chat-only:        L1 ─────────────────── L5
                    (LLM)                 (Chat)

  Claude Code:      L1 ── L2 ── L3 ── L4 ── L5
                    (API)  (tools) (Skills) (agent) (CLI)

  SaaS + AI:        L1 ── L2(partial) ──── L5
                    (API)  (app-scoped)    (Web app)

Emerging (2026-2027):
新興：

  Mobile OS:        L1(edge) ── L2 ── L3 ── L4 ── L5
                    (on-device)  (system) (OS-level) (persistent) (native UI)

  Multi-agent:      L1 ── L2 ── L3 ── L4a ── L4b ── L4c ── L5
                                       (PM)   (writer) (reviewer)

Future (AGI-like):
未來（類 AGI）：

  Full stack:       L1(hybrid) ── L2(universal) ── L3(ecosystem) ── L4(autonomous) ── L5(ambient)
                    (cloud+edge)   (all tools)      (all Skills)     (self-directing)   (everywhere)
```

The trajectory is clear: as each layer matures and as more layers are connected, the system behaves more like what people imagine when they think of AGI — not a single superintelligent model, but a **complete stack** of intelligence, tools, expertise, memory, and interfaces working together seamlessly.

軌跡很清楚：隨著每一層成熟，隨著更多層被連接，系統的行為越來越像人們想像中的 AGI——不是單一的超級智能模型，而是智能、工具、專長、記憶和介面**完整堆疊**地無縫協作。

### Failure Cascades ── 失敗瀑布

When things go wrong, failures cascade upward:

當事情出錯時，失敗向上瀑布：

| Failure Point 失敗點 | Example 範例 | Recovery 恢復 |
|---|---|---|
| Layer 2 (tool error) | File not found, API timeout | Agent retries or tries alternative tool |
| Layer 1 (LLM error) | Hallucination, reasoning error | Skill validation rules catch it → retry |
| Layer 3 (Skill flaw) | Missing step, bad validation | Human review catches → Skill update |
| Layer 4 (orchestration) | Wrong Skill selected, state corruption | May require session restart |

Design principle: **catch failures as low as possible**. Layer 2 failures should be handled at Layer 2. Only escalate when lower-layer recovery is impossible.

設計原則：**盡可能在低層級捕捉失敗**。第二層的失敗應在第二層處理。只有在低層恢復不可能時才向上升級。

---

## 6. The Bigger Picture ── 更大的圖像

### Comparing Computing Paradigms ── 比較計算範式

| | Traditional 傳統 | Web/Cloud 雲端 | Agentic 代理型 |
|---|---|---|---|
| **Logic** 邏輯 | Compiled code | APIs + microservices | LLM inference |
| **Data Access** 資料存取 | File system, DB | REST APIs, GraphQL | Tools via MCP |
| **Functional Unit** 功能單元 | Function/Class | Service/Endpoint | Skill |
| **Orchestration** 調度 | Main function | API gateway | Agent |
| **Interface** 介面 | GUI (predetermined) | Browser (predetermined) | Conversation (dynamic) |
| **Composition** 組合 | Import/dependency | API calls (typed) | Semantic adaptation by LLM |
| **State** 狀態 | Variables in RAM | Database/session | `.md` files in repo |

### The Fundamental Shift: Syntactic → Semantic Composition ── 根本轉變：語法式→語義式組合

The deepest difference between the Agentic stack and all previous computing paradigms is the **nature of the composition glue**.

代理堆疊與所有先前計算範式之間的最深層差異，在於**組合黏合劑的本質**。

Traditional computing: composition is **syntactic** — types must match, interfaces must be implemented, contracts satisfied at compile time. If Module A outputs `TypeX` and Module B expects `TypeY`, you get a compile error.

傳統計算：組合是**語法式的**——型別必須匹配、介面必須實作、契約在編譯時滿足。如果模組 A 輸出 `TypeX` 而模組 B 期望 `TypeY`，你得到編譯錯誤。

Agentic computing: composition is **semantic** — the LLM understands the *meaning* of each component's output and adapts it to the next component's input. This is what enables the "a235bc1e" pattern — dynamic, intent-driven composition that no rigid type system could express.

代理型計算：組合是**語義式的**——LLM 理解每個組件輸出的*含義*，並將其適配到下一個組件的輸入。這就是「a235bc1e」模式之所以可能——動態的、意圖驅動的組合，沒有僵硬的型別系統能表達。

**This is the architectural foundation of what will eventually look like AGI**: not a single breakthrough model, but a mature five-layer stack where any Skill can compose with any other Skill, orchestrated by Agents that maintain persistent context, accessible through whatever interface fits the situation.

**這就是最終看起來像 AGI 的架構基礎**：不是單一突破性的模型，而是成熟的五層堆疊，任何 Skill 都能與其他 Skill 組合，由維持持續上下文的 Agent 調度，透過適合情境的任何介面存取。

---

## Summary ── 總結

The Five-Layer Model is not a theoretical exercise. It's a **map of what's already happening** — a way to understand why some AI products feel magical and others feel like "AI bolted onto old software."

五層模型不是理論練習。它是**已經在發生之事的地圖**——一種理解為什麼某些 AI 產品感覺神奇、而其他的感覺像「AI 焊接在舊軟體上」的方式。

```
Layer 5: Interface      ← How you experience it (chat, desktop, CLI, API, ambient)
Layer 4: Agent          ← How it remembers and orchestrates (memory, skill routing)
Layer 3: Skill          ← How it knows what to do (reusable workflow units)
Layer 2: Tool           ← How it touches the world (files, web, code, APIs)
Layer 1: LLM            ← How it thinks (inference, reasoning, understanding)
```

Each layer has a single responsibility:

- **Layer 1** thinks. 思考。
- **Layer 2** acts. 行動。
- **Layer 3** knows how. 知道怎麼做。
- **Layer 4** remembers and decides. 記憶與決策。
- **Layer 5** communicates. 溝通。

The products implementing all five layers — Claude Code, Cowork — represent the leading edge. The products implementing only some layers — chat windows, SaaS-plus-AI — are earlier stops on the same journey. And the future points toward full-stack integration across cloud, local, and edge, where these five layers work together so seamlessly that the technology becomes invisible.

實作了全部五層的產品——Claude Code、Cowork——代表前沿。只實作部分層的產品——對話窗口、SaaS 加 AI——是同一旅程上更早的站點。而未來指向雲端、本地和端側的全堆疊整合，這五層協作得如此無縫，以至於技術變得不可見。

---

## Cross-References ── 相關文件

- [The Agentic Substrate: Core Architecture](agentic-substrate.md) — The overview that introduces the five layers
  核心架構文件——介紹五層的總覽
- [Anatomy of a Skill](skill-anatomy.md) — Deep dive into Layer 3 internals
  技能模組解剖學——深入第三層內部
- [Markdown as the Native Medium](markdown-as-medium.md) — How Markdown connects all layers as the universal interchange format
  Markdown 作為原生媒介——Markdown 如何作為通用交換格式連接所有層
- [Landscape Analysis](../02-architecture/landscape.md) — How other frameworks describe parts of this picture
  生態比較——其他框架如何描述這幅圖的部分

---

*Next: [Agentic Design Patterns →](../02-architecture/agentic-design-patterns.md)*
*下一篇：[代理型設計模式 →](../02-architecture/agentic-design-patterns.md)*
