# The Agentic Substrate: Core Architecture
# 代理型基底：核心架構原則

> *"Architecture matters as much as the model."*
> *「架構的重要性等同於模型本身。」*
>
> — Evidence: GPT-3.5 in an agentic loop achieved 95.1% on coding benchmarks vs. 48.1% in zero-shot mode (Andrew Ng, 2024)

---

## 1. The Paradigm Shift ── 典範轉移

### 1.1 From Deterministic to Probabilistic Computing 從確定性到概率性運算

Traditional software operates on **deterministic logic**: every input maps to a predefined output through hardcoded rules (`if-else`, `switch-case`, state machines). A developer writes every possible path.

傳統軟體運作在**確定性邏輯**上：每個輸入透過寫死的規則對應到預定義的輸出。開發者必須寫出每一條可能的路徑。

Agentic software operates on **probabilistic inference**: the LLM understands the *intent* behind a request, reasons about the *context*, and dynamically determines the execution path. No developer has pre-coded that specific path — the system generates it on the fly.

代理型軟體運作在**概率性推理**上：LLM 理解請求背後的*意圖*，推理*情境*，動態決定執行路徑。沒有任何開發者預先寫好那條特定路徑——系統即時生成它。

```
Traditional 傳統:    Input → [Hardcoded Logic] → Output
                     輸入  → [寫死的邏輯]     → 輸出

Agentic 代理型:      Intent → [LLM Reasoning + Context] → Dynamic Execution Path → Output
                     意圖  → [LLM 推理 + 情境]         → 動態執行路徑          → 輸出
```

### 1.2 The "Agentic Substrate" Defined 定義「代理型基底」

**Agentic Substrate** (代理型基底) is the foundational layer upon which all AI-native software is built. Just as an operating system provides the substrate for traditional applications, the Agentic Substrate provides the computational foundation for Skill-based, Agent-orchestrated software.

**Agentic Substrate**（代理型基底）是所有 AI 原生軟體建構其上的基礎層。就像作業系統為傳統應用程式提供基底，Agentic Substrate 為基於 Skill、由 Agent 調度的軟體提供運算基礎。

It consists of three fundamental layers:

它由三個基礎層構成：

```
┌─────────────────────────────────────────────────────┐
│                  Agent Layer 代理層                    │
│         Orchestration, Memory, Personality            │
│              調度、記憶、個性化                          │
├─────────────────────────────────────────────────────┤
│                  Skill Layer 技能層                    │
│     Composable functional units with defined I/O     │
│          可組合的功能單元，具有定義的輸入/輸出            │
├─────────────────────────────────────────────────────┤
│              LLM Computation Layer 運算層              │
│     Inference, Reasoning, Natural Language Understanding│
│             推理、邏輯思考、自然語言理解                  │
└─────────────────────────────────────────────────────┘
```

---

## 2. The Five-Layer Model ── 五層架構模型

To fully describe how an Agentic system operates, we expand into five layers:

要完整描述一個代理型系統如何運作，我們展開為五層：

### Layer 1: LLM Computation Layer ── LLM 運算層
**What it is**: The raw intelligence — the "cloud brain."
**是什麼**：原始智能——「雲端大腦」。

This is the foundation. An LLM (Claude, GPT, Gemini, Grok) provides the universal capabilities: natural language understanding, logical reasoning, code generation, multimodal processing, and most importantly — **intent comprehension**.

這是基礎。LLM（Claude、GPT、Gemini、Grok）提供通用能力：自然語言理解、邏輯推理、程式碼生成、多模態處理，以及最重要的——**意圖理解**。

Key characteristics 關鍵特性:
- Accessed via API (cloud) or local inference (edge) 透過 API（雲端）或本地推理（端側）存取
- Stateless by nature — each call is independent 本質上無狀態——每次呼叫都是獨立的
- The "reasoning engine" that powers everything above 驅動上層一切的「推理引擎」

**Analogy 類比**: If the Agentic Substrate is a computer, the LLM is the CPU. 如果 Agentic Substrate 是一台電腦，LLM 就是 CPU。

### Layer 2: Tool & Protocol Layer ── 工具與協議層
**What it is**: The hands and eyes — how the LLM interacts with the world.
**是什麼**：手和眼——LLM 與世界互動的方式。

LLMs on their own can only generate text. To become useful agents, they need **tools**: file readers, code executors, web searchers, database connectors, API callers.

LLM 本身只能生成文字。要成為有用的 Agent，它需要**工具**：檔案讀取器、程式碼執行器、網頁搜尋器、資料庫連接器、API 呼叫器。

The critical innovation here is **standardized protocols** like MCP (Model Context Protocol), which allow any tool to be discovered and used by any agent without custom integration code.

這裡的關鍵創新是**標準化協議**，如 MCP（Model Context Protocol），讓任何工具都能被任何 Agent 發現和使用，不需要自定義整合程式碼。

```
LLM  ←──  MCP  ──→  Tool A (File System)
                ──→  Tool B (Web Search)
                ──→  Tool C (Database)
                ──→  Tool D (External API)
                ──→  Tool E (Code Execution)
```

**Analogy 類比**: If the LLM is the CPU, tools are the I/O devices, and MCP is the USB standard. 如果 LLM 是 CPU，工具就是 I/O 裝置，MCP 就是 USB 標準。

### Layer 3: Skill Layer ── 技能層
**What it is**: The new "App" — composable, intelligent functional units.
**是什麼**：新型態的「App」——可組合的智慧功能單元。

This is where your insight becomes architecture. A **Skill** is not just a prompt or a tool — it's a **structured workflow definition** that tells the LLM:

這正是你的洞察轉化為架構的地方。一個 **Skill** 不只是一個 prompt 或工具——它是一個**結構化的工作流程定義**，告訴 LLM：

1. **Scope** 範圍: What this Skill is responsible for 這個 Skill 負責什麼
2. **Trigger** 觸發條件: When to activate 什麼時候啟動
3. **Process** 流程: Step-by-step execution logic 逐步執行邏輯
4. **I/O Contract** 輸入/輸出契約: What it receives and what it produces 接收什麼、產出什麼
5. **Validation** 驗證: How to verify the output is correct 如何驗證輸出正確性
6. **Composability** 可組合性: How it connects with other Skills 如何與其他 Skill 連接

#### Skill Taxonomy 技能分類學

Skills fall into several categories based on their function:

根據功能，Skills 分為幾個類別：

| Type 類型 | Description 描述 | Example 範例 |
|---|---|---|
| **Data Skill** 資料型 | Static or semi-static knowledge base 靜態或半靜態的知識庫 | A company portfolio database with 40+ project records 公司作品集資料庫 |
| **Process Skill** 流程型 | Linear, iterative workflow with validation 線性迭代工作流程，含驗證 | A proposal writer that guides chapter-by-chapter authoring with validation 逐章引導撰寫提案 |
| **Transform Skill** 轉換型 | Takes input in format A, outputs format B 接收格式A，產出格式B | A team profile formatter: messy text → structured org chart 雜亂文字→結構化組織圖 |
| **Integration Skill** 整合型 | Bridges between systems or formats 在系統或格式之間架橋 | A document builder: Markdown chapters → formatted Word/PDF 章節合併為排版文件 |
| **Orchestration Skill** 調度型 | Coordinates multiple Skills 協調多個 Skills | A project executor: proposal → tracked repo with agent handbook 提案→專案追蹤 |

#### The "a235bc1e" Pattern ── 雜湊組合模式

A critical insight: Skills are **composable atoms**. Given two linear Skill chains:

一個關鍵洞見：Skills 是**可組合的原子**。給定兩條線性 Skill 鏈：

```
Chain A:  [a] → [b] → [c] → [d] → [e]
Chain 1:  [1] → [2] → [3] → [4] → [5]
```

The LLM can dynamically compose them based on the task's actual needs:

LLM 可以根據任務的實際需求動態組合：

```
Composed: [a] → [2] → [3] → [5] → [b] → [c] → [1] → [e]
```

This is possible because:
這之所以可能，是因為：

- Each Skill has a defined **I/O contract** (what it takes in, what it puts out) 每個 Skill 有定義好的**輸入/輸出契約**
- The LLM understands the **semantic meaning** of each Skill's output, not just its data format LLM 理解每個 Skill 產出的**語義含義**，不只是資料格式
- Markdown serves as the **universal interchange format** — human-readable, LLM-parseable Markdown 作為**通用交換格式**——人類可讀、LLM 可解析

**This is fundamentally different from traditional API composition**, where you need strict type matching and explicit interface definitions. Here, the LLM acts as a **universal adapter** that understands what each piece means and how to connect them.

**這與傳統的 API 組合根本不同**，傳統方式需要嚴格的型別匹配和明確的介面定義。在這裡，LLM 充當**通用適配器**，理解每個部分的含義以及如何連接它們。

### Layer 4: Agent Layer ── 代理層
**What it is**: The persistent intelligence — the "colleague AI" that knows you.
**是什麼**：持續性的智慧——認識你的「同事 AI」。

An Agent is more than an LLM with tools. An Agent has:

Agent 不只是帶工具的 LLM。Agent 具有：

- **Persistent Memory** 持續記憶: It remembers past interactions, project contexts, preferences 記住過去的互動、專案情境、偏好
- **Personality & Role** 個性與角色: It operates as a specific team member (project manager, writer, analyst) 以特定團隊成員身份運作
- **Skill Awareness** 技能感知: It knows which Skills are available and when to invoke them 知道哪些 Skills 可用，以及何時呼叫
- **Goal Decomposition** 目標拆解: It breaks complex requests into executable steps 將複雜的請求拆解為可執行的步驟
- **State Management** 狀態管理: It tracks progress across sessions (e.g., via repo-as-memory pattern) 跨工作階段追蹤進度

The Agent layer is where **persistent assistants** live — they grow with you, read the project state at startup, execute tasks, write results back, and shut down. Next session, they resume from where they left off.

Agent 層是**持續性助理**所在之處——與你一起成長，在啟動時讀取專案狀態，執行任務，將結果寫回，然後關閉。下次工作階段，從上次結束的地方繼續。

```
Agent Lifecycle 代理生命週期:

  [Start] → Read repo/state → Understand context → Decompose task
     → Invoke Skills → Produce outputs → Write back to repo → [End]
              ↓
    Next session: [Start] → Read repo/state → ... (cycle continues)
```

### Layer 5: Interface Layer ── 介面層
**What it is**: How humans interact with the system.
**是什麼**：人類如何與系統互動。

This layer encompasses all the touchpoints:

這一層涵蓋所有接觸點：

| Interface 介面 | Function 功能 | Complexity 複雜度 |
|---|---|---|
| **Chat Window** 對話窗 | Ask questions, explore, learn 提問、探索、學習 | ★ Simple 簡單 |
| **Cowork / IDE** 協作環境 | Skill-powered workflows 技能驅動的工作流程 | ★★ Moderate 中等 |
| **CLI / Terminal** 命令列 | Direct agent control 直接代理控制 | ★★★ Advanced 進階 |
| **API / Programmatic** 程式化介面 | System-to-system integration 系統對系統整合 | ★★★★ Expert 專家 |
| **Ambient / Edge Node** 環境/端側節點 | AI-generated interfaces (Musk's vision) AI 生成介面 | ★★★★★ Future 未來 |

---

## 3. Design Principles ── 設計原則

These principles govern how Agentic systems should be designed:

以下原則指導代理型系統的設計方式：

### Principle 1: Simplicity Over Complexity 簡單勝過複雜

> *"Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."* — Anthropic

> *「從簡單的 prompt 開始，透過全面評估來優化，只在簡單方案不足時才加入多步驟代理系統。」*——Anthropic

Claude Code's architecture proves this: **only 1.6% of its codebase is AI decision logic**. The other 98.4% is deterministic infrastructure — permission gates, context management, tool routing, recovery logic. The agent loop itself is a simple `while` loop.

Claude Code 的架構證明了這一點：**只有 1.6% 的程式碼是 AI 決策邏輯**。其餘 98.4% 是確定性基礎設施——權限閘門、情境管理、工具路由、復原邏輯。代理迴圈本身就是一個簡單的 `while` 迴圈。

**Implication for Skill design**: A Skill should be as simple as possible. One Skill, one responsibility. Complexity comes from *composition*, not from individual complexity.

**對 Skill 設計的意涵**：Skill 應該盡可能簡單。一個 Skill，一個職責。複雜性來自*組合*，而不是個別的複雜性。

### Principle 2: Human Decision Authority 人類決策權

> *"Agents must be able to work autonomously; their independent operation is exactly what makes them valuable. But humans should retain control over how their goals are pursued."* — Anthropic

> *「Agent 必須能自主工作；獨立運作正是它們的價值所在。但人類應保留對目標追求方式的控制權。」*

The system should be **transparent** — the human can see what the Agent is planning, which Skills it's invoking, and what outputs it's producing. The Agent proposes; the human approves.

系統應該是**透明的**——人類可以看到 Agent 在規劃什麼、呼叫哪些 Skills、產出什麼結果。Agent 提案；人類核准。

### Principle 3: Markdown as Universal Protocol Markdown 作為通用協議

In the Agentic Substrate, **Markdown is the universal interchange format** — the "JSON of the AI era."

在 Agentic Substrate 中，**Markdown 是通用的交換格式**——「AI 時代的 JSON」。

Why Markdown? 為什麼是 Markdown？
- **Human-readable** 人類可讀: Anyone can open and understand it 任何人都能打開和理解
- **LLM-native** LLM 原生: LLMs naturally produce and consume Markdown LLM 天然產生和解析 Markdown
- **Structured enough** 足夠結構化: Headers, lists, tables provide structure 標題、列表、表格提供結構
- **Versionable** 可版本控制: Works perfectly with Git 完美配合 Git 使用
- **Composable** 可組合: Easy to merge, split, and transform 易於合併、分割和轉換

This is why Skills define their I/O contracts in Markdown. The output of one Skill is a `.md` file that another Skill can consume.

這就是為什麼 Skills 用 Markdown 定義其輸入/輸出契約。一個 Skill 的輸出是一個 `.md` 檔案，另一個 Skill 可以消費它。

### Principle 4: Repo as Memory 倉庫即記憶

For persistent Agents (like project management agents), the **Git repository IS the memory**:

對於持續性 Agent（如專案管理 Agent），**Git 倉庫就是記憶**：

- Agent starts → reads `.md` files from repo → reconstructs state Agent 啟動 → 從 repo 讀取 `.md` 檔案 → 重建狀態
- Agent works → produces outputs → writes `.md` files back to repo Agent 工作 → 產出結果 → 將 `.md` 檔案寫回 repo
- Agent stops → state is fully captured in repo Agent 停止 → 狀態完全保存在 repo 中
- Next session → repeat from step 1 下次工作階段 → 從第一步重複

No conversation history needed. No database required. **The repo is the single source of truth.**

不需要對話歷史。不需要資料庫。**Repo 是唯一的事實來源。**

### Principle 5: Skills as Stable Interfaces, Not Fragile Files 技能是穩定介面，不是脆弱檔案

A key distinction from your practice: **Skills are more stable than regular Markdown files** because they're designed as interfaces, not as working documents.

來自你實踐的關鍵區分：**Skills 比一般 Markdown 檔案更穩定**，因為它們被設計為介面，而非工作文件。

A regular `.md` file in a project is a living document — the Agent may read and modify it freely. A Skill's `.md` definition is an **interface contract** — it changes rarely and deliberately, much like a traditional API specification.

專案中的一般 `.md` 檔案是活文件——Agent 可以自由讀取和修改。Skill 的 `.md` 定義是**介面契約**——它很少改動，且是刻意修改，就像傳統的 API 規格書。

This distinction makes Skills function as a **controlled form of RAG** — reliable, structured knowledge that the LLM can access without the volatility of general-purpose documents.

這個區分使 Skills 成為一種**受控形式的 RAG**——可靠的、結構化的知識，LLM 可以存取，沒有通用文件的不穩定性。

### Principle 6: Graduated Autonomy 漸進式自主權

Not every task needs full agent autonomy. The system should support a **spectrum**:

不是每個任務都需要完全的代理自主權。系統應支持一個**光譜**：

```
Human-driven ←──────────────────────────────→ Agent-driven
人類驅動                                        代理驅動

[Chat Q&A] → [Guided Workflow] → [Supervised Agent] → [Autonomous Agent]
 對話問答     引導式工作流程      監督式代理           自主代理
```

Start with simpler patterns, prove reliability, then grant more autonomy. This matches Anthropic's observation that the most effective implementations start simple and layer complexity only when needed.

從簡單的模式開始，證明可靠性，然後授予更多自主權。這符合 Anthropic 的觀察：最有效的實作從簡單開始，只在需要時才疊加複雜性。

---

## 4. The Agentic Design Patterns ── 代理型設計模式

Building on Andrew Ng's foundational patterns and Anthropic's practical patterns:

基於 Andrew Ng 的基礎模式和 Anthropic 的實務模式：

### 4.1 Foundational Patterns 基礎模式 (Andrew Ng)

| Pattern 模式 | Description 描述 | When to use 適用時機 |
|---|---|---|
| **Reflection** 反思 | Agent critiques and revises its own output iteratively Agent 迭代批評和修改自己的輸出 | Quality-critical tasks 品質關鍵任務 |
| **Tool Use** 工具使用 | Agent calls external tools (APIs, databases, code execution) Agent 呼叫外部工具 | Any task requiring world interaction 需要與世界互動的任務 |
| **Planning** 規劃 | Agent decomposes goals into executable steps Agent 將目標分解為可執行步驟 | Complex, multi-step tasks 複雜多步驟任務 |
| **Multi-Agent** 多代理 | Multiple agents collaborate, debate, specialize 多個 Agent 協作、辯論、專業化 | Large-scale, diverse tasks 大規模多元任務 |

### 4.2 Compositional Patterns 組合模式 (Anthropic)

| Pattern 模式 | Description 描述 | Example 範例 |
|---|---|---|
| **Prompt Chaining** 提示鏈 | Sequential steps, each feeding the next 依序步驟，每步餵入下一步 | Data extraction → Analysis → Report |
| **Routing** 路由 | Classify input, send to specialized handler 分類輸入，送往專門處理器 | Customer query → FAQ / Technical / Billing |
| **Parallelization** 平行化 | Independent subtasks run simultaneously 獨立子任務同時執行 | Multi-section document generation |
| **Orchestrator-Workers** 調度者-工作者 | Central agent delegates to specialized workers 中央 Agent 委派給專業工作者 | Project executor coordinating Skills |
| **Evaluator-Optimizer** 評估-優化 | Iterative loop: generate → evaluate → improve 迭代循環：生成→評估→改善 | proposal-writer with validation loop |

### 4.3 The Claude Code Pattern: Simple Loop + Rich Infrastructure

Claude Code demonstrates that the most effective pattern is often the simplest:

Claude Code 展示了最有效的模式往往是最簡單的：

```
while (task_not_complete) {
    context   = gather_relevant_context()
    response  = LLM.reason(context + task)
    action    = parse_action(response)
    result    = execute_action(action)       // tool call, file edit, etc.
    context   = update_context(result)
}
```

The magic isn't in the loop — it's in the **infrastructure around it**: permission systems, context window management, error recovery, and tool definitions.

魔法不在迴圈——而在**圍繞它的基礎設施**：權限系統、情境視窗管理、錯誤復原和工具定義。

---

## 5. The Transition Landscape ── 過渡期地貌

We're currently in a transition period. Here's how the landscape maps:

我們正處於過渡期。以下是地貌的映射：

### Current State 現況 (2024-2026)

```
┌────────────────────────────────────────────────────────────────┐
│                     Cloud / SaaS Layer                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Existing  │  │ SaaS +   │  │ AI-Native│  │ Pure AI  │      │
│  │ SaaS      │→ │ AI Bolt- │→ │ SaaS     │→ │ Agent    │      │
│  │ (no AI)   │  │ on (API) │  │ (built on│  │ Services │      │
│  │           │  │          │  │  LLM)    │  │          │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
│                                                                 │
│                     Local / Edge Layer                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ CLI Tools │  │ VS Code  │  │ Claude   │  │ Full     │      │
│  │ (basic)   │→ │ + AI     │→ │ Code /   │→ │ Local    │      │
│  │           │  │ Copilot  │  │ Cowork   │  │ Agent    │      │
│  │           │  │          │  │          │  │ Infra    │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
│                                                                 │
│                     Mobile / Consumer Layer                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Apps +    │  │ OS-level │  │ AI-First │  │ Edge     │      │
│  │ Siri/     │→ │ AI       │→ │ Device   │→ │ Node     │      │
│  │ Assistant │  │ (Apple   │  │ (Rabbit, │  │ (Musk's  │      │
│  │           │  │  Intel.) │  │  Humane) │  │  Vision) │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└────────────────────────────────────────────────────────────────┘
                         Timeline →
```

### Where We Are Now 我們在哪裡

Early adopters are already operating at the **frontier of the Local/Edge layer** — building real Skill-based workflows with tools like Claude Code and Cowork, using repos as memory, composing Skills for complex knowledge work. They are ahead of most organizations who are still in the "SaaS + AI bolt-on" phase.

早期採用者已經在**本地/端側層的前沿**運作——用 Claude Code 和 Cowork 等工具建構真正的 Skill-based 工作流程，用 repo 作為記憶，為複雜知識工作組合 Skills。他們領先於大多數仍在「SaaS + AI 附加」階段的組織。

---

## 6. Looking Forward ── 展望

### The Convergence 匯聚

All paths lead to the same destination:

所有路徑都通向同一個目的地：

1. **SaaS companies** will either become Skill providers or become irrelevant SaaS 公司要麼成為 Skill 提供者，要麼變得無關
2. **Mobile OS** will evolve from app platforms to agent platforms 行動作業系統將從 App 平台演化為 Agent 平台
3. **Local development tools** will mature into full agent infrastructure 本地開發工具將成熟為完整的 Agent 基礎設施
4. **Hardware** will simplify to inference endpoints (Musk's Edge Nodes) 硬體將簡化為推理端點

The organizations that understand the Agentic Substrate — that build Skills instead of apps, that use LLMs as computation rather than features, that design for composition rather than silos — will be the ones that thrive.

理解 Agentic Substrate 的組織——建構 Skills 而非 App、將 LLM 作為運算而非功能、為組合而非孤島而設計——將是蓬勃發展的組織。

---

## References 參考資料

1. Andrew Ng, "Agentic Design Patterns" — Reflection, Tool Use, Planning, Multi-Agent (2024)
2. Anthropic, ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — Composable patterns for agent design
3. Liu et al., ["Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"](https://arxiv.org/abs/2604.14228) — Architecture analysis (2025)
4. Anthropic, ["Building Agents with the Claude Agent SDK"](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) — SDK design philosophy
5. Elon Musk, "Edge Node" vision — The future device as AI inference endpoint (2025)

---

*Next: [The Five-Layer Model in Detail →](five-layer-model.md)*
*下一篇：[五層架構模型詳解 →](five-layer-model.md)*
