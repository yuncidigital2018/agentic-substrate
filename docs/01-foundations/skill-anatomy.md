# Anatomy of a Skill: The Fundamental Unit of Agentic Software
# 技能模組解剖學：代理型軟體的基礎單元

> *"A Skill is to Agentic software what a function is to traditional programming — the atomic unit of reusable logic. But unlike a function, a Skill carries intent, context, and judgment."*
>
> *「Skill 之於代理型軟體，就如同函式之於傳統程式設計——可重用邏輯的原子單元。但不同於函式，Skill 承載意圖、情境與判斷力。」*

---

## 1. What is a Skill? ── 什麼是 Skill？

### 1.1 The Simple Definition 簡單定義

A **Skill** is a structured Markdown document that teaches an LLM **how to perform a specific task** — including when to activate, what process to follow, what to produce, and how to verify the result.

一個 **Skill** 是一份結構化的 Markdown 文件，教導 LLM **如何執行特定任務**——包括何時啟動、遵循什麼流程、產出什麼、以及如何驗證結果。

### 1.2 The Deeper Definition 深層定義

A Skill is a **cognitive interface contract** between a human designer and an LLM executor. It encodes:

Skill 是人類設計者與 LLM 執行者之間的**認知介面契約**。它編碼了：

- **Domain knowledge** 領域知識: What an expert in this area knows 這個領域的專家所知道的
- **Process logic** 流程邏輯: How an expert approaches this task step by step 專家如何一步步處理這個任務
- **Quality criteria** 品質標準: How an expert judges if the output is good 專家如何判斷輸出是否良好
- **Boundary conditions** 邊界條件: When this approach applies and when it doesn't 這個方法何時適用、何時不適用

### 1.3 Skill vs. Traditional Software Constructs 技能 vs 傳統軟體構件

| Construct 構件 | Logic 邏輯 | Flexibility 彈性 | Context Awareness 情境感知 | Human Readable 人類可讀 |
|---|---|---|---|---|
| **Function** 函式 | Hardcoded 寫死 | None 無 | None 無 | Code only 僅程式碼 |
| **API Endpoint** | Hardcoded 寫死 | Parameters only 僅參數 | None 無 | Docs required 需文件 |
| **Prompt Template** 提示模板 | Semi-flexible 半彈性 | Variable slots 變數插槽 | Minimal 最少 | Yes 是 |
| **MCP Tool** | Hardcoded + protocol 寫死+協議 | Typed parameters 型別參數 | Minimal 最少 | Schema only 僅 Schema |
| **Skill** 技能 | LLM-interpreted LLM 解讀 | Full 完全 | Deep 深度 | Fully 完全 |

The key insight: **a Skill doesn't execute logic — it guides an LLM to reason through logic.** The LLM is the execution engine; the Skill is the blueprint.

關鍵洞見：**Skill 不執行邏輯——它引導 LLM 推理邏輯。**LLM 是執行引擎；Skill 是藍圖。

---

## 2. The Seven Components of a Skill ── Skill 的七大組成部分

Every well-designed Skill contains seven components. Not all are required in every Skill, but understanding all seven is essential for designing effective ones.

每個設計良好的 Skill 包含七個組成部分。不是每個 Skill 都需要全部七個，但理解全部七個對於設計有效的 Skill 是必要的。

```
┌─────────────────────────────────────────────────┐
│                    SKILL                         │
│                                                  │
│  ┌──────────────┐  ┌─────────────────────────┐  │
│  │ ① Identity    │  │ ② Trigger Conditions    │  │
│  │   身份定義     │  │   觸發條件               │  │
│  └──────────────┘  └─────────────────────────┘  │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │ ③ Process Logic  流程邏輯                  │   │
│  │   Phase 1 → Phase 2 → ... → Phase N       │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  ┌──────────────┐  ┌─────────────────────────┐  │
│  │ ④ I/O Contract│  │ ⑤ Validation Rules     │  │
│  │   輸入/輸出契約│  │   驗證規則              │  │
│  └──────────────┘  └─────────────────────────┘  │
│                                                  │
│  ┌──────────────┐  ┌─────────────────────────┐  │
│  │ ⑥ Knowledge   │  │ ⑦ Composition Hooks    │  │
│  │   領域知識     │  │   組合掛鉤              │  │
│  └──────────────┘  └─────────────────────────┘  │
│                                                  │
└─────────────────────────────────────────────────┘
```

### ① Identity — 身份定義

The `name` and `description` in the YAML frontmatter. This is what the Agent sees **before** loading the full Skill — it's the "shop window" that determines whether this Skill gets activated.

YAML frontmatter 中的 `name` 和 `description`。這是 Agent 在載入完整 Skill **之前**看到的——它是決定這個 Skill 是否被啟動的「櫥窗」。

This follows the principle of **progressive discovery** (漸進式發現): at startup, the Agent sees only the name and a short description (20-50 tokens). Only when the Skill is triggered does the full content (potentially thousands of tokens) enter the context window.

這遵循**漸進式發現**原則：啟動時，Agent 只看到名稱和簡短描述（20-50 tokens）。只有當 Skill 被觸發時，完整內容（可能數千 tokens）才進入情境視窗。

**Real Example 真實案例** — a company portfolio database:
```yaml
---
name: company-portfolio
description: |
  Intelligent company database and project recommendation engine.
  Stores complete profiles for partner companies including
  40+ project execution records, core competencies, and awards.
  When the user mentions "find projects," "match requirements,"
  "which team fits," or "show our track record," activate this Skill.
---
```

**Design Principle 設計原則**: The description must contain **trigger keywords** (觸發關鍵字) — the natural language phrases that a user would actually say. This is semantic routing, not URL routing.

**設計原則**：描述必須包含**觸發關鍵字**——使用者實際會說的自然語言短語。這是語義路由，不是 URL 路由。

### ② Trigger Conditions — 觸發條件

Explicit rules for **when** this Skill should activate. Unlike traditional software where routing is based on URLs or function calls, Skill routing is based on **intent recognition**.

**何時**啟動此 Skill 的明確規則。不同於傳統軟體基於 URL 或函式呼叫的路由，Skill 路由基於**意圖識別**。

**Real Example 真實案例** — a proposal writing Skill:
```
Activate when the user mentions "write a proposal," "draft a bid,"
"RFP response," "project pitch," or "we need to submit by Friday."
```

**Real Example 真實案例** — a team profile formatting Skill:
```
Also activate when the user pastes unstructured text containing
names, job titles, education, and experience — and asks to
"clean this up," "make an org chart," or "format for the proposal."
```

Notice: the second example doesn't just list keywords — it describes a **behavioral pattern** (使用者貼上雜亂的文字). This is a level of routing sophistication that traditional software cannot achieve.

注意：第二個例子不只列出關鍵字——它描述了一個**行為模式**（使用者貼上雜亂文字）。這是傳統軟體無法達到的路由精細度。

### ③ Process Logic — 流程邏輯

The step-by-step execution flow. This is where a Skill most resembles a traditional program — but written in natural language for an LLM to interpret and follow.

逐步執行流程。這是 Skill 最像傳統程式的地方——但用自然語言編寫，讓 LLM 解讀和遵循。

**Three Process Architectures 三種流程架構**:

```
Linear 線性:           Phase 1 → Phase 2 → Phase 3 → Output
                       適用：簡單的轉換或生成任務

Iterative 迭代:        Phase 1 → Phase 2 → Validate → [Pass?]
                                    ↑                    │
                                    └── Fix ←── No ──────┘
                       適用：品質關鍵的生成任務

Branching 分支:        Phase 1 → [Classify] → Branch A → Output A
                                             → Branch B → Output B
                                             → Branch C → Output C
                       適用：多情境路由任務
```

**Real Example — Iterative Architecture 迭代架構** — a proposal writing Skill:

This Skill implements a "write-and-verify" loop (邊寫邊驗證) that mirrors software development methodology:

這個 Skill 實作了一個「邊寫邊驗證」迴圈，鏡像了軟體開發方法論：

```
Phase 0  Document inventory & feasibility check     文件盤點與可行性評估
Phase 1  Requirements analysis & research synthesis  需求解析與調研整合
Phase 2  Structure planning (define TOC)             架構規劃（決定目錄）
Phase 2.5 Build editorial guide & content map        建立編��指南與內容地圖
Phase 3  Chapter writing × real-time validation loop 章節撰寫 × 即時驗證循環 ← Core
Phase 4  Final integration & cross-check             最終整合校稿
Phase 5  Export                                      輸出
```

At Phase 3, **every chapter triggers an automatic validation report**. This is the Skill equivalent of unit testing — each module is verified before the next one begins.

在 Phase 3，**每一章都觸發自動驗證報告**。這是 Skill 版的單元測試——每個模組在下一個開始之前就被驗證。

**Real Example — Branching Architecture 分支架構** — a company portfolio Skill:

```
User Input → [Classify Query Type]
  → "find past projects"     → Company + Region + Domain search → List matches
  → "who can handle this?"   → Requirement matching             → Recommend team + evidence
  → "fill in the proposal"   → Chapter assist mode              → Auto-populate credentials
```

### ④ I/O Contract — 輸入/輸出契約

What the Skill expects to receive and what it promises to produce. This is the **interface** that enables Skill composition.

Skill 期望接收什麼以及承諾產出什麼。這是使 Skill 組合成為可能的**介面**。

**Real Example** — a document builder Skill:
```
Input  輸入:  Multiple Markdown chapter files (.md)
              + table/figure caption mappings
              + format specification file

Output 輸出:  Formatted Word document (.docx)
              with auto-generated TOC, figure index, table index
              in client-standard typography and layout
```

**Real Example** — a team profile formatting Skill:
```
Input  輸入:  Unstructured text (any format)
              — names, titles, education, experience
              — can be messy, incomplete, multi-format

Output 輸出:  Three structured blocks:
              1. Organization chart (SVG/PNG)
              2. Role & responsibility table (Markdown)
              3. Team member profiles (Markdown)
              + Optional: formatted .docx file
```

**Key Principle 關鍵原則**: The I/O contract is defined in **semantic terms**, not strict data types. "Unstructured text about team members" is a valid input specification because the LLM can interpret it. This is impossible in traditional programming.

**關鍵原則**：輸入/輸出契約以**語義**定義，而非嚴格的資料型別。「關於團隊成員的非結構化文字」是一個有效的輸入規格，因為 LLM 可以解讀它。這在傳統程式設計中是不可能的。

### ⑤ Validation Rules — 驗證規則

How to verify the output is correct. This is the Skill equivalent of **testing**.

如何驗證輸出是正確的。這是 Skill 版的**測試**。

**Three Levels of Validation 三個層級的驗證**:

| Level 層級 | Type 類型 | Description 描述 | Example 範例 |
|---|---|---|---|
| **L1** | Format Check 格式檢查 | Does the output match the expected structure? 輸出是否符合預期結構？ | Document builder: checks heading hierarchy, page format |
| **L2** | Content Consistency 內容一致性 | Are there internal contradictions? 是否有內部矛盾？ | Proposal writer: cross-chapter validation of numbers, terms, dates |
| **L3** | Goal Alignment 目標對齊 | Does the output achieve the stated objective? 輸出是否達成既定目標？ | Proposal writer: does content address all evaluation criteria? |

**Real Example — Multi-Layer Validation 多層驗證** — a proposal writing Skill:

This Skill produces **automatic validation artifacts** (自動產出驗證產物) at each stage:

| Artifact 產物 | Created When 建立時機 | Update Frequency 更新頻率 |
|---|---|---|
| `editorial_guide.md` | Phase 2.5 | Immutable baseline 不變動的基準 |
| `validation_log.md` | Phase 3 first chapter | After each chapter 每章完成後 |
| `progress_dashboard.md` | Phase 3 first chapter | After each chapter 每章完成後 |
| `validation_ch01.md` ~ `validation_ch07.md` | Per chapter completion | After revision 修正後更新 |
| `consistency_check_report.md` | Phase 4 | One-time 一次性 |

This is the most sophisticated validation architecture we've seen in any Skill design — it mirrors the testing pyramid in software engineering (unit tests → integration tests → end-to-end tests).

這是我們在任何 Skill 設計中見過的最精密的驗證架構——它鏡像了軟體工程中的測試金字塔（單元測試→整合測試→端對端測試）。

### ⑥ Knowledge — 領域知識

Domain-specific information embedded in the Skill that the LLM wouldn't know from its general training.

嵌入在 Skill 中的特定領域知識，是 LLM 從通用訓練中不會知道的。

**Three Knowledge Patterns 三種知識模式**:

| Pattern 模式 | Description 描述 | Example 範例 |
|---|---|---|
| **Inline** 內嵌 | Knowledge written directly in the Skill 知識直接寫在 Skill 中 | Team formatter: standard hierarchy rules for org charts (CEO → VP → Manager → Staff) |
| **Referenced** 引用 | Knowledge in separate files, loaded on demand 知識在獨立檔案中，按需載入 | Document builder: `references/format_spec.md` for typography rules |
| **External Data** 外部資料 | Structured data files (JSON, CSV) accessed by the Skill | Company portfolio: `portfolio_data.json` with 40+ project records |

**Real Example — External Data as Knowledge 外���資料作為知識** — a company portfolio Skill:
```
Core data file:
skills/company-portfolio/portfolio_data.json

Contains:
- ✅ Company profiles (registration, leadership, founding date)
- ✅ Core competencies & service domains (6 modules, 20+ service items)
- ✅ 40+ project execution records (name, client, year, scope)
- ✅ Search tag system for fast querying
```

This is where **Skills become a controlled form of RAG** (Skill 成為一種受控形式的 RAG). Unlike general RAG systems that search through unstructured document stores, a Data Skill provides:

這是 **Skills 成為受控形式 RAG** 的地方。與搜尋非結構化文件庫的一般 RAG 系統不同，Data Skill 提供：

- Curated, verified data 策展過的、已驗證的資料
- Defined query patterns 定義好的查詢模式
- Stable interface (rarely changes) 穩定的介面（很少改變）
- Domain-specific search logic 特定領域的搜尋邏輯

### ⑦ Composition Hooks — 組合掛鉤

How this Skill connects to other Skills — what it can receive from upstream Skills and what it can feed to downstream Skills.

這個 Skill 如何連接其他 Skills——它能從上游 Skills 接收什麼、能餵給下游 Skills 什麼。

**Real Example — The Proposal Pipeline 提案管線**:

```
[Proposal Writer]  (Process Skill)
    │ produces: chapter .md files
    │           + validation reports
    │           + progress dashboard
    ↓
[Company Portfolio]  (Data Skill) ←── called during team chapter
    │ provides: company profiles, past project records
    ↓
[Team Formatter]  (Transform Skill) ←── called during team chapter
    │ produces: org chart + team profiles .md
    ↓
[Document Builder]  (Integration Skill)
    │ consumes: all chapter .md files
    │ produces: final formatted .docx
    ↓
[Project Executor]  (Orchestration Skill) ←── after winning the bid
    │ consumes: proposal .md control tables
    │ produces: GitHub repo structure + agent handbook
```

Notice: this is not a rigid pipeline. The LLM decides **when** to call each Skill based on the task context. During the team chapter, the Proposal Writer may call Company Portfolio and Team Formatter. But for the introduction chapter, it works alone. The composition is **dynamic and context-driven**.

注意：這不是一個固定的管線。LLM 根據任務情境決定**何時**呼叫每個 Skill。在寫團隊章節時，Proposal Writer 可能呼叫 Company Portfolio 和 Team Formatter。但寫前言章節時，它獨立工作。組合是**動態的、情境驅動的**。

---

## 3. The Skill Taxonomy ── 技能分類學

Skills serve fundamentally different purposes. Understanding these types is essential for knowing what kind of Skill to build for a given need.

Skills 服務於根本不同的目的。理解這些類型對於知道在特定需求下建構什麼類型的 Skill 至關重要。

### Type 1: Data Skill — 資料型技能

**Purpose 目的**: Serve as a structured, queryable knowledge base.
**作用**：作為結構化的、可查詢的知識庫。

**Characteristics 特性**:
- Contains curated, rarely-changing data 包含策展過的、極少變動的資料
- Responds to queries, doesn't drive a process 回應查詢，不驅動流程
- Functions as **controlled RAG** 作為**受控 RAG** 運作
- High stability — the Skill definition rarely changes 高穩定性——Skill 定義很少改變

**Analogy 類比**: Like a reference book or a database 像一本參考書或資料庫

**Live Example**: A company portfolio Skill — stores 40+ project records, company profiles, award history. Queried by other Skills during proposal writing.

**實例**：公司作品集 Skill——儲存 40+ 專案記錄、公司簡介、獲獎紀錄。在提案撰寫過程中被其他 Skills 查詢。

```
┌─────────────────────────────┐
│      Data Skill              │
│  ┌───────────────────────┐  │
│  │ Curated Data (JSON/MD)│  │
│  └───────────────────────┘  │
│  ┌───────────────────────┐  │
│  │ Query Patterns         │  │
│  │  → by keyword          │  │
│  │  → by category         │  │
│  │  → by requirement match│  │
│  └───────────────────────┘  │
│  Output: Filtered results   │
└─────────────────────────────┘
```

### Type 2: Process Skill — 流程型技能

**Purpose 目的**: Guide the LLM through a multi-step workflow with validation.
**作用**：引導 LLM 走過一個包含驗證的多步驟工作流程。

**Characteristics 特性**:
- Has clear phases with defined entry/exit criteria 有明確的階段，具備定義的進入/退出標準
- Produces intermediate artifacts (not just final output) 產出中間產物（不只是最終輸出）
- Includes validation at each stage 在每個階段包含驗證
- Most complex Skill type 最複雜的 Skill 類型

**Analogy 類比**: Like a project methodology or a standard operating procedure 像專案方法論或標準作業程序

**Live Example**: A proposal writing Skill — guides a 6-phase process from requirement analysis to final document, with per-chapter validation.

**實例**：提案撰寫 Skill——引導從需求分析到最終文件的 6 階段流程，每章都有驗證。

```
┌──────────────────────────────────────┐
│          Process Skill                │
│                                       │
│  Phase 0  ──→  Phase 1  ──→  Phase 2 │
│                                       │
│  Phase 3: [Write Chapter] ──→ [Validate]
│                ↑                  │    │
│                └── Fix ←── Fail ──┘    │
│                                       │
│  Phase 4  ──→  Phase 5  ──→  Output   │
│                                       │
│  Artifacts: 驗證報告, 進度儀表板,      │
│             編輯指南, 章節 .md files    │
└──────────────────────────────────────┘
```

### Type 3: Transform Skill — 轉換型技能

**Purpose 目的**: Take input in one format/structure and produce output in another.
**作用**：接收一種格式/結構的輸入，產出另一種格式/結構的輸出。

**Characteristics 特性**:
- Clear input format → output format mapping 清楚的輸入格式→輸出格式映射
- May handle messy, unstructured input 可能處理雜亂的、非結構化輸入
- Embeds domain-specific formatting rules 嵌入特定領域的格式化規則
- Often has a "normalize → structure → format" pipeline 通常有「正規化→結構化→格式化」管線

**Analogy 類比**: Like a compiler or a document converter 像編譯器或文件轉換器

**Live Example**: A team profile Skill — takes messy team member data (any format) and produces structured org charts, role tables, and profile sections in proposal format.

**實例**：團隊資料格式化 Skill——接收雜亂的團隊成員資料（任何格式），產出結構化的組織圖、職掌表和個人介紹，符合提案格式。

```
┌──────────────────────────────────────┐
│         Transform Skill               │
│                                       │
│  [Messy Input]                        │
│       ↓                               │
│  Step 1: Extract & Normalize          │
│       ↓                               │
│  Step 2: Infer Structure              │
│       ↓                               │
│  Step 3: Format to Target             │
│       ↓                               │
│  [Structured Output]                  │
│  (org chart + tables + profiles)      │
└──────────────────────────────────────┘
```

### Type 4: Integration Skill — 整合型技能

**Purpose 目的**: Bridge between different systems, tools, or format ecosystems.
**作用**：在不同的系統、工具或格式生態系之間架橋。

**Characteristics 特性**:
- Consumes output from multiple upstream Skills 消費多個上游 Skills 的輸出
- Produces output in a specific tool/system format 以特定工具/系統格式產出
- Contains technical specifications (page layout, fonts, styles) 包含技術規格（頁面佈局、字型、樣式）
- May invoke external scripts or tools 可能呼叫外部腳本或工具

**Analogy 類比**: Like a build system or an export pipeline 像建置系統或匯出管線

**Live Example**: A document builder Skill — consumes multiple Markdown chapter files and produces a formatted Word document with client-standard typography, auto-generated TOC, figure index, and table index.

**實例**：文件建構 Skill——消費多個 Markdown 章節檔案，產出具有客戶標準排版、自動生成目錄、圖目錄和表目錄的格式化 Word 文件。

```
┌──────────────────────────────────────┐
│        Integration Skill              │
│                                       │
│  [Skill A output] ──┐                │
│  [Skill B output] ──┼──→ [Merge &   │
│  [Skill C output] ──┘     Format]    │
│                              ↓        │
│                    [External Tool]     │
│                     (gen_docx.js)      │
│                              ↓        │
│                    [Final .docx]       │
└──────────────────────────────────────┘
```

### Type 5: Orchestration Skill — 調度型技能

**Purpose 目的**: Coordinate multiple Skills and manage state across sessions.
**作用**：協調多個 Skills 並跨工作階段管理狀態。

**Characteristics 特性**:
- Defines a persistent execution context (repo, folder structure) 定義持續性的執行情境（repo、資料夾結構）
- Manages state through file system (not conversation memory) 透過檔案系統管理狀態（不是對話記憶）
- May define Agent behavior (role, communication style, trigger logic) 可能定義 Agent 行為（角色、溝通方式、觸發邏輯）
- Most architectural of all Skill types 所有 Skill 類型中最具架構性的

**Analogy 類比**: Like an operating system or a project management system 像作業系統或專案管理系統

**Live Example**: A project executor Skill — transforms proposal outputs into a GitHub repo structure with SOUL.md (agent identity), DAILY.md (state snapshot), MILESTONES.md (timeline), and a complete agent handbook that enables a persistent AI assistant to manage the project autonomously.

**實例**：專案執行 Skill——將提案產出轉化為 GitHub repo 結構，包含 SOUL.md（Agent 身份）、DAILY.md（狀態快照）、MILESTONES.md（時間線），以及完整的 Agent 工作手冊，讓持續性 AI 助理能自主管理專案。

```
┌──────────────────────────────────────────────┐
│           Orchestration Skill                 │
│                                               │
│  Defines:                                     │
│  ┌─────────────┐  ┌──────────────────────┐   │
│  │ Repo         │  │ Agent Behavior        │   │
│  │ Structure    │  │ (SOUL.md, STYLE.md)   │   │
│  └─────────────┘  └──────────────────────┘   │
│  ┌─────────────┐  ┌──────────────────────┐   │
│  │ State Files  │  │ Trigger Logic         │   │
│  │ (DAILY.md)   │  │ (TRIGGER.yaml)        │   │
│  └─────────────┘  └──────────────────────┘   │
│                                               │
│  Agent Lifecycle:                             │
│  Start → Read State → Decide → Act → Write   │
│    ↑                                    │     │
│    └──────── Next Session ──────────────┘     │
└──────────────────────────────────────────────┘
```

---

## 4. The Skill Lifecycle ── 技能生命週期

A Skill goes through distinct phases from conception to maturity:

Skill 從構想到成熟經歷不同的階段：

```
┌────────┐    ┌────────┐    ┌─────────┐    ┌──────────┐    ┌────────┐
│ Design  │ →  │ Draft   │ →  │ Test &   │ →  │ Stabilize│ →  │ Compose│
│ 設計    │    │ 草稿    │    │ Iterate  │    │ 穩定化   │    │ 組合   │
│         │    │         │    │ 測試迭代 │    │          │    │        │
└────────┘    └────────┘    └─────────┘    └──────────┘    └────────┘
     │              │             │               │              │
  Define         Write       Use it for       Lock the       Connect
  purpose &      first       real tasks;      interface;     with other
  scope          SKILL.md    refine based     document       Skills in
                             on results       I/O contract   pipelines
```

**Crucial Insight 關鍵洞見**: Once a Skill reaches the "Stabilize" phase, **its SKILL.md should change as rarely as a published API**. This is what makes Skills more stable than regular working documents — they're **interface contracts**, not living notes.

**關鍵洞見**：一旦 Skill 到達「穩定化」階段，**它的 SKILL.md 應該像已發布的 API 一樣很少改變**。這就是 Skills 比一般工作文件更穩定的原因——它們是**介面契約**，不是活筆記。

---

## 5. Skill Composition: The "a235bc1e" Pattern ── 技能組合：雜湊組合模式

This is the most powerful concept in the Agentic Substrate. Traditional software composition requires:

這是 Agentic Substrate 中最強大的概念。傳統軟體組合需要：

- Strict type matching between components 元件之間嚴格的型別匹配
- Explicit interface definitions 明確的介面定義
- Pre-coded integration logic 預先寫好的整合邏輯
- Compile-time or deploy-time binding 編譯時或部署時的綁定

Skill composition requires only:

Skill 組合只需要：

- **Defined I/O contracts** (in semantic terms) 定義好的輸入/輸出契約（以語義）
- **Markdown as interchange format** Markdown 作為交換格式
- **An LLM that understands both Skills** 一個理解兩個 Skills 的 LLM

### How It Works 運作方式

Given two independent Skill chains:

給定兩條獨立的 Skill 鏈：

```
Proposal Chain:  [Analyze] → [Plan] → [Write] → [Validate] → [Format]
                     a          b         c          d            e

Execution Chain: [Parse] → [Structure] → [Define] → [Generate] → [Deploy]
                    1          2            3           4            5
```

A new task might require: "Take the validated proposal (d), generate an execution structure (2→3), then format the combined result (e)."

一個新任務可能需要：「取得已驗證的建議書(d)，生成執行架構(2→3)，然後格式化組合結果(e)」。

```
Dynamic Composition: [d] → [2] → [3] → [e]
```

The LLM can do this because:

LLM 可以做到這一點，因為：

1. It reads Skill `d`'s output contract — knows it produces validated chapter .md files 它讀取 Skill `d` 的輸出契約——知道它產出已驗證的章節 .md 檔案
2. It reads Skill `2`'s input contract — knows it accepts structured .md content 它讀取 Skill `2` 的輸入契約——知道它接受結構化的 .md 內容
3. It understands **semantically** that validated chapters can feed into a structuring step 它**語義上**理解已驗證的章節可以餵入結構化步驟
4. No code integration is needed — just Markdown flowing between Skills 不需要程式碼整合——只是 Markdown 在 Skills 之間流動

**This is why Markdown as a universal protocol matters.** It's the common language that enables runtime composition without pre-coded integrations.

**這就是為什麼 Markdown 作為通用協議很重要。**它是在沒有預先寫好整合的情況下實現執行時組合的共同語言。

---

## 6. Design Guidelines ── 設計準則

### Do's ✓

1. **One Skill, one responsibility** 一個 Skill，一個職責
   - If a Skill does two unrelated things, split it 如果一個 Skill 做兩件不相關的事，拆分它

2. **Write trigger conditions in the user's language** 用使用者的語言寫觸發條件
   - Not "when NER detects entity" but "當使用者提到「查案例」" 不是程式語言，而是自然語言

3. **Define I/O contracts explicitly** 明確定義輸入/輸出契約
   - Even if the input is "messy text," say so 即使輸入是「雜亂文字」，也要說明

4. **Include validation at every phase** 在每個階段包含驗證
   - The best Skills validate as they go, not just at the end 最好的 Skills 邊做邊驗證，不只是最後

5. **Use progressive disclosure** 使用漸進式揭露
   - Front-load the identity and triggers; put detailed process logic deeper 前置身份和觸發條件；把詳細流程邏輯放更深處

6. **Store reference data separately** 將參考資料分開儲存
   - Use `references/` folder for specs, templates, and data files 使用 `references/` 資料夾存放規格、模板和資料檔案

### Don'ts ✗

1. **Don't embed volatile data in the Skill definition** 不要在 Skill 定義中嵌入易變資料
   - Company data changes → put in JSON, not in SKILL.md 公司資料會變→放在 JSON，不是 SKILL.md

2. **Don't write implementation code in the Skill** 不要在 Skill 中寫實作程式碼
   - The Skill describes *what to do*; the LLM decides *how to do it* Skill 描述*做什麼*；LLM 決定*怎麼做*

3. **Don't assume a specific LLM** 不要假設特定的 LLM
   - Write Skills that any capable LLM can follow 寫任何有能力的 LLM 都能遵循的 Skills

4. **Don't over-constrain the process** 不要過度約束流程
   - Leave room for the LLM to adapt to unexpected situations 留空間讓 LLM 適應意外情況

5. **Don't skip the stabilization phase** 不要跳過穩定化階段
   - A Skill used in production pipelines must have a stable interface 在生產管線中使用的 Skill 必須有穩定的介面

---

## 7. The Skill Maturity Model ── 技能成熟度模型

A framework for assessing how developed a Skill is:

評估 Skill 發展程度的框架：

| Level 等級 | Name 名稱 | Characteristics 特性 | Example 範例 |
|---|---|---|---|
| **L0** | Prompt 提示 | Just a prompt template, no structure 只是提示模板，沒有結構 | "Help me write a proposal" |
| **L1** | Guided 引導式 | Has steps but no validation 有步驟但沒有驗證 | Simple checklist-style Skill |
| **L2** | Validated 驗證式 | Has process + validation at each stage 有流程+每階段驗證 | A team profile formatter with input validation |
| **L3** | Composable 可組合式 | Has defined I/O contracts, connects to other Skills 有定義的 I/O 契約，連接其他 Skills | A document builder consuming outputs from multiple Skills |
| **L4** | Autonomous 自主式 | Manages state across sessions, drives Agent behavior 跨工作階段管理狀態，驅動 Agent 行為 | A project executor with repo-as-memory and agent handbook |

Most organizations starting with AI are at L0-L1. The goal of this framework is to help teams progress to L3-L4, where the real power of the Agentic Substrate emerges.

大多數開始使用 AI 的組織在 L0-L1。這個框架的目標是幫助團隊進步到 L3-L4，那裡 Agentic Substrate 的真正力量才會浮現。

---

## Summary ── 總結

A Skill is the **fundamental building block** of Agentic software. It is:

Skill 是代理型軟體的**基礎建構塊**。它是：

- **More than a prompt** — it carries process, validation, and domain knowledge 不只是 prompt——它承載流程、驗證和領域知識
- **Less than an app** — it doesn't run independently; it needs an LLM to interpret it 不及一個 App——它不獨立運行；它需要 LLM 來解讀
- **Stable like an API** — once mature, its interface rarely changes 穩定如 API——一旦成熟，其介面很少改變
- **Composable like functions** — can be chained, branched, and mixed dynamically 可組合如函式——可以動態地串接、分支和混合
- **Human-readable like documentation** — anyone can open and understand it 可讀如文件——任何人都能打開和理解

Understanding Skills is the foundation for everything else in this framework — from learning paths to system architecture to Agent design.

理解 Skills 是這個框架中所有其他內容的基礎——從學習路徑到系統架構到 Agent 設計。

---

*Previous: [The Agentic Substrate: Core Architecture ←](agentic-substrate.md)*
*Next: [The Five-Layer Model in Detail →](five-layer-model.md)*
