# Agentic Design Patterns
# 代理型設計模式

> *"The best agent architecture is the simplest one that gets the job done reliably."*
> *「最好的 Agent 架構，是能可靠完成工作的最簡單架構。」*
> — Anthropic, "Building Effective Agents"

---

## 1. What Are Design Patterns For? ── 設計模式的用途

In traditional software engineering, design patterns (Singleton, Observer, Factory...) solved recurring structural problems. In Agentic software, we face a different set of recurring problems:

在傳統軟體工程中，設計模式（Singleton、Observer、Factory……）解決的是重複出現的結構問題。在代理型軟體中，我們面對的是不同的重複問題：

- How should an Agent decide **which Skill to invoke**? Agent 應該如何決定**呼叫哪個 Skill**？
- How should multiple Skills **coordinate** on a complex task? 多個 Skills 應該如何在複雜任務上**協調**？
- How should an Agent **verify** its own output quality? Agent 應該如何**驗證**自己的產出品質？
- How should a system **decompose** a goal that's too big for one step? 系統應該如何**分解**一步做不完的目標？
- When should you use **one agent** vs. **multiple agents**? 什麼時候該用**一個 Agent** vs. **多個 Agent**？

This document catalogs the patterns that answer these questions, drawn from two primary sources — Andrew Ng's foundational framework and Anthropic's practical guide — and then places them within the [Five-Layer Model](../01-foundations/five-layer-model.md) to show where each pattern operates in the stack.

本文件收錄回答這些問題的模式，來自兩個主要來源——Andrew Ng 的基礎框架和 Anthropic 的實務指南——然後將它們放入[五層模型](../01-foundations/five-layer-model.md)中，顯示每個模式在堆疊中的操作位置。

### The Golden Rule ── 黃金法則

Before diving in, the most important principle:

在深入之前，最重要的原則：

> **Start with the simplest pattern that could work. Add complexity only when you can measure that the simpler approach is failing.**
> **從可能可行的最簡單模式開始。只在你能衡量出簡單方法正在失敗時，才添加複雜性。**

This isn't just good advice — it's an empirical finding. Claude Code, one of the most capable agent systems in production, uses a simple `while` loop as its core architecture. Only ~1.6% of its codebase is AI decision logic. The sophistication lives in the **context assembly**, not the control flow.

這不只是好建議——它是經驗發現。Claude Code，最有能力的生產環境 Agent 系統之一，使用簡單的 `while` 迴圈作為核心架構。只有約 1.6% 的程式碼是 AI 決策邏輯。精密之處在於**上下文組裝**，而不是控制流程。

---

## 2. The Two Pattern Families ── 兩個模式家族

Two influential frameworks have defined the vocabulary for Agentic design patterns. They approach the problem from different angles but are complementary:

兩個有影響力的框架定義了代理型設計模式的詞彙。它們從不同角度切入但互補：

```
Andrew Ng (2024)                    Anthropic (2025)
──────────────────                  ──────────────────
Asks: "What cognitive               Asks: "How do you compose
abilities make agents               agents in practice?"
effective?"                         提問：「實務上如何組合
提問：「什麼認知能力                  Agent？」
讓 Agent 有效？」

4 Foundational Patterns:            5 Compositional Patterns:
  • Reflection                        • Prompt Chaining
  • Tool Use                          • Routing
  • Planning                          • Parallelization
  • Multi-Agent                       • Orchestrator-Workers
                                      • Evaluator-Optimizer

Focus: Agent reasoning              Focus: Agent architecture
聚焦：Agent 的推理能力               聚焦：Agent 的架構組合
```

Ng's patterns describe **what an agent can do**. Anthropic's patterns describe **how to wire agents together**. Both are necessary. Neither is sufficient alone.

Ng 的模式描述 **Agent 能做什麼**。Anthropic 的模式描述**如何將 Agent 連接在一起**。兩者都是必要的。單獨任何一個都不夠。

---

## 3. Foundational Patterns (Andrew Ng) ── 基礎模式

These four patterns represent the core cognitive capabilities that transform a basic LLM into an effective agent. Andrew Ng demonstrated their power with a striking data point: **GPT-3.5 in an agentic loop achieved 95.1% on coding benchmarks, compared to 48.1% in zero-shot mode** — a weaker model with good patterns outperformed a stronger model without them.

這四個模式代表將基本 LLM 轉變為有效 Agent 的核心認知能力。Andrew Ng 用一個驚人的數據點展示了它們的威力：**GPT-3.5 在代理迴圈中達到編碼基準的 95.1%，而零次模式只有 48.1%**——一個較弱的模型搭配好的模式，表現超過沒有模式的更強模型。

### Pattern 1: Reflection ── 反思

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ Generate │ ──→ │ Critique │ ──→ │ Revise   │ ──→ (loop until satisfied)
│ 生成     │     │ 批評     │     │ 修改     │
└──────────┘     └──────────┘     └──────────┘
                      │
                      ▼
               "Is this output
                good enough?"
```

**What it is** 是什麼: The agent generates output, then **critiques its own work** against defined criteria, then revises. This loop repeats until quality thresholds are met.

Agent 生成產出，然後根據定義的標準**批評自己的作品**，然後修改。這個迴圈重複直到達到品質門檻。

**Why it matters** 為什麼重要: Without reflection, the LLM's first attempt is the final answer — and first attempts are often mediocre. With reflection, even a weaker model can iteratively improve to high quality.

沒有反思，LLM 的第一次嘗試就是最終答案——而第一次嘗試往往平庸。有了反思，即使較弱的模型也能迭代改善到高品質。

**Real-world example** 真實範例:

A document review Skill that:
1. Reads a draft document
2. Identifies issues (logical gaps, missing evidence, unclear phrasing)
3. Rewrites problematic sections
4. Re-evaluates the revised version
5. Repeats until all criteria pass

文件審查 Skill：(1) 讀取草稿文件 (2) 識別問題 (3) 改寫問題段落 (4) 重新評估修改版 (5) 重複直到所有標準通過

**Where it sits in the Five-Layer Model** 在五層模型中的位置:

Reflection is primarily a **Layer 1** (LLM reasoning) pattern, but it becomes powerful when combined with **Layer 3** (Skill) validation rules. The Skill defines *what* to check; the LLM's reflection capability executes the checking.

反思主要是**第一層**（LLM 推理）模式，但與**第三層**（Skill）驗證規則結合時變得強大。Skill 定義*檢查什麼*；LLM 的反思能力執行檢查。

**Design guidance** 設計指引:

- Always define **explicit criteria** for the reflection. "Is this good?" is too vague. "Does this section contain a specific metric, a comparison to baseline, and a recommendation?" is actionable.
  永遠定義**明確的標準**。「這個好嗎？」太模糊。「這個段落是否包含具體指標、基準比較和建議？」才可執行。
- Set a **maximum iteration count** (typically 2-3 rounds). Diminishing returns are real.
  設定**最大迭代次數**（通常 2-3 輪）。收益遞減是真實的。
- Consider using **separate LLM calls** for generation and critique — different system prompts can create productive tension.
  考慮使用**分開的 LLM 呼叫**進行生成和批評——不同的系統提示可以產生有建設性的張力。

---

### Pattern 2: Tool Use ── 工具使用

```
┌──────────┐     ┌──────────┐     ┌──────────┐
│ LLM      │ ──→ │ Decide   │ ──→ │ Execute  │ ──→ result back to LLM
│ reasons  │     │ which    │     │ tool     │
│          │     │ tool     │     │          │
└──────────┘     └──────────┘     └──────────┘
                                       │
                                  ┌────┴────┐
                                  │ Read    │
                                  │ Write   │
                                  │ Search  │
                                  │ Execute │
                                  │ Observe │
                                  └─────────┘
```

**What it is** 是什麼: The LLM decides when and how to use external tools — file readers, code executors, web searchers, API callers — to interact with the world beyond its training data.

LLM 決定何時以及如何使用外部工具——檔案讀取器、程式碼執行器、網頁搜尋器、API 呼叫器——與訓練資料以外的世界互動。

**Why it matters** 為什麼重要: This is the pattern that transforms LLMs from knowledge bases into **operational systems**. Without tool use, an LLM can only recite what it was trained on. With tool use, it can read your actual files, search real-time information, run calculations, and produce deliverables.

這是將 LLM 從知識庫轉變為**可運作系統**的模式。沒有工具使用，LLM 只能背誦訓練內容。有了工具使用，它能讀取你的實際檔案、搜尋即時資訊、執行計算、產出交付物。

**Where it sits in the Five-Layer Model** 在五層模型中的位置:

Tool Use is the bridge between **Layer 1** (LLM reasoning about what to do) and **Layer 2** (tools that actually do it). The LLM decides; the tool executes. The result feeds back to the LLM for the next decision.

工具使用是**第一層**（LLM 推理該做什麼）和**第二層**（實際執行的工具）之間的橋樑。LLM 決策；工具執行。結果回饋給 LLM 做下一個決策。

**Design guidance** 設計指引:

- Keep tool descriptions **precise and concise**. The LLM reads these descriptions to decide which tool to use — vague descriptions lead to wrong tool selection.
  保持工具描述**精確簡潔**。LLM 閱讀這些描述來決定使用哪個工具——模糊的描述導致錯誤的工具選擇。
- Return **structured error messages** from tools. "File not found: /path/to/file.md" is far better than a generic exception.
  從工具回傳**結構化的錯誤訊息**。
- Consider **progressive tool discovery** to manage context window costs (see [Five-Layer Model, Layer 2](../01-foundations/five-layer-model.md)).
  考慮**漸進式工具發現**來管理上下文窗口成本。

---

### Pattern 3: Planning ── 規劃

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Complex Goal │ ──→ │ Decompose    │ ──→ │ Execute      │
│ 複雜目標     │     │ into steps   │     │ step by step │
│              │     │ 分解為步驟    │     │ 逐步執行      │
└──────────────┘     └──────────────┘     └──────────────┘
                           │
                     ┌─────┴─────┐
                     │ Step 1    │
                     │ Step 2    │
                     │ Step 3    │ ← may replan if
                     │ ...       │   conditions change
                     │ Step N    │
                     └───────────┘
```

**What it is** 是什麼: The agent breaks a complex goal into a sequence of smaller, executable steps. As it executes, it may revise the plan based on new information (replanning).

Agent 將複雜目標分解為一系列較小的可執行步驟。在執行過程中，它可能根據新資訊修改計劃（重新規劃）。

**Why it matters** 為什麼重要: Many real-world tasks are too complex for a single LLM call. Planning allows the agent to tackle tasks that would otherwise exceed its context window or reasoning capacity.

許多真實世界的任務對單次 LLM 呼叫來說太複雜。規劃允許 Agent 處理那些否則會超過上下文窗口或推理能力的任務。

**Real-world example** 真實範例:

A project status report Skill that plans:
1. Identify the reporting period (this week)
2. Gather commit history from git
3. Read open issues and milestones
4. Cross-reference completed work against planned milestones
5. Identify blockers and risks
6. Format the report according to template
7. Validate completeness

Each step depends on the previous step's output, and the agent can skip or add steps based on what it discovers.

**Where it sits in the Five-Layer Model** 在五層模型中的位置:

Planning is a **Layer 4** (Agent) capability that operates on **Layer 3** (Skills). The Agent plans which Skills to invoke and in what order. Individual Skills don't need to know about the overall plan — they just do their job when called.

規劃是**第四層**（Agent）能力，操作在**第三層**（Skills）上。Agent 規劃呼叫哪些 Skills 以及什麼順序。個別 Skills 不需要知道整體計劃——被呼叫時做好自己的工作即可。

**Design guidance** 設計指引:

- **Prefer incremental planning over upfront planning** 偏好漸進式規劃而非預先規劃. Plan the next 2-3 steps, execute them, then replan based on results. Long upfront plans often become obsolete after the first step reveals unexpected conditions.
  規劃接下來 2-3 步，執行，然後根據結果重新規劃。長預先計劃在第一步揭示意外狀況後往往就過時了。
- **Use todo lists or state files** 使用待辦清單或狀態檔案. Writing the plan to a file makes it inspectable by the human and resumable across sessions.
  將計劃寫入檔案，讓人類可檢視、跨工作階段可恢復。
- **Build in checkpoints** 建立檢查點. After each major step, verify the output before proceeding. This prevents cascading errors.
  在每個主要步驟後，繼續之前先驗證輸出。防止錯誤連鎖。

---

### Pattern 4: Multi-Agent ── 多代理

```
┌──────────────────────────────────────────────┐
│              Orchestrator Agent               │
│              調度者 Agent                      │
│                                              │
│    ┌──────────┐ ┌──────────┐ ┌──────────┐   │
│    │ Agent A  │ │ Agent B  │ │ Agent C  │   │
│    │ Researcher│ │ Writer  │ │ Reviewer │   │
│    │ 研究員   │ │ 撰寫者  │ │ 審查者   │   │
│    └──────────┘ └──────────┘ └──────────┘   │
│         │            │            │          │
│         ▼            ▼            ▼          │
│    [research    [draft from  [review and     │
│     findings]    research]   provide         │
│                              feedback]       │
└──────────────────────────────────────────────┘
```

**What it is** 是什麼: Multiple specialized agents collaborate on a task, each with its own role, perspective, or expertise. They may work sequentially (pipeline), in parallel (fan-out), or interactively (debate).

多個專業化 Agent 在任務上協作，各有自己的角色、觀點或專長。它們可能依序工作（管線）、平行工作（扇出），或互動式工作（辯論）。

**Why it matters** 為什麼重要: Specialization improves quality. A single agent trying to be researcher + writer + reviewer tends to produce mediocre output. Separate agents with focused roles produce better results, because each agent's system prompt and context is optimized for its specific task.

專業化提升品質。一個試圖同時擔任研究員 + 撰寫者 + 審查者的 Agent 往往產出平庸。有聚焦角色的分開 Agent 產出更好的結果，因為每個 Agent 的系統提示和上下文都為其特定任務而優化。

**Where it sits in the Five-Layer Model** 在五層模型中的位置:

Multi-Agent is a **Layer 4** pattern. Each agent is a Layer 4 instance with its own identity, memory, and Skill set. They coordinate through shared Layer 2 resources (files, repos) or through a parent agent that orchestrates them.

多代理是**第四層**模式。每個 Agent 是一個有自己身份、記憶和 Skill 集的第四層實例。它們透過共享的第二層資源（檔案、repo）或透過調度它們的父 Agent 來協調。

```
Five-Layer View of Multi-Agent:

  L5 (Interface) ─── human sees unified result ───────────────
  L4 (Agent)     ─── Agent A ──── Agent B ──── Agent C ──────
  L3 (Skill)     ─── Skills A ─── Skills B ─── Skills C ─────
  L2 (Tools)     ─── shared file system, repo, MCP servers ──
  L1 (LLM)       ─── same or different LLM instances ────────
```

**Design guidance** 設計指引:

- **Don't default to multi-agent** 不要預設使用多代理. A single agent with well-designed Skills often outperforms multiple agents with poorly defined roles. Multi-agent adds communication overhead and failure modes.
  設計良好的 Skills 的單一 Agent，往往勝過角色定義不良的多 Agent。多代理增加通訊開銷和失敗模式。
- **Define clear hand-off contracts** 定義清楚的交接契約. Each agent should know exactly what it receives and what it must produce. Markdown files are the natural hand-off medium.
  每個 Agent 應確切知道它接收什麼和必須產出什麼。
- **Use shared state, not messages** 使用共享狀態，而非訊息. Rather than agents "talking" to each other, have them read/write shared files. This is more robust and inspectable.
  與其讓 Agent「對話」，不如讓它們讀寫共享檔案。這更穩健且可檢視。

---

## 4. Compositional Patterns (Anthropic) ── 組合模式

Anthropic's "Building Effective Agents" paper (2025) defines five patterns for **how to wire agent components together**. These are practical architecture blueprints, not abstract reasoning patterns.

Anthropic 的「建構有效 Agent」論文（2025）定義了五種**如何將 Agent 組件連接在一起**的模式。這些是實用的架構藍圖，不是抽象的推理模式。

### Pattern A: Prompt Chaining ── 提示鏈

```
[Step 1] ──→ output ──→ [Step 2] ──→ output ──→ [Step 3] ──→ final result
  Gate ✓                  Gate ✓                  Gate ✓
```

**What it is** 是什麼: A task is decomposed into a fixed sequence of steps, where each step's output becomes the next step's input. Between steps, there may be **programmatic gates** — validation checks that ensure quality before proceeding.

任務被分解為固定的步驟序列，每個步驟的輸出成為下一步的輸入。步驟之間可能有**程式化閘門**——在繼續之前確保品質的驗證檢查。

**When to use** 適用時機: Tasks where the workflow is **predictable** and can be expressed as a linear pipeline. Each step should be simple enough for a single LLM call.

工作流程**可預測**且能表達為線性管線的任務。每步應簡單到單次 LLM 呼叫就能完成。

**Real-world example** 真實範例:

```
Data extraction pipeline:
資料擷取管線：

  [Read raw data]              ← Step 1: Extract
       │
       ▼ (gate: data format valid?)
  [Categorize and structure]   ← Step 2: Transform
       │
       ▼ (gate: all categories assigned?)
  [Generate summary report]    ← Step 3: Synthesize
       │
       ▼ (gate: report completeness check)
  [Format for delivery]        ← Step 4: Format
```

**Mapping to the Five-Layer Model** 對應五層模型:

Prompt Chaining maps naturally to **a single Skill's process logic** (Layer 3). The "steps" in the chain are the steps defined in the Skill's workflow. The gates are the Skill's validation rules. The Agent (Layer 4) may not even be involved — a single Skill can execute a chain autonomously.

提示鏈自然對應到**單一 Skill 的流程邏輯**（第三層）。鏈中的「步驟」是 Skill 工作流程中定義的步驟。閘門是 Skill 的驗證規則。Agent（第四層）甚至可能不需要參與——單一 Skill 可以自主執行一條鏈。

---

### Pattern B: Routing ── 路由

```
                    ┌──→ [Handler A] (if category X)
                    │
[Classify input] ──┼──→ [Handler B] (if category Y)
                    │
                    └──→ [Handler C] (if category Z)
```

**What it is** 是什麼: An initial step classifies the input, then routes it to the appropriate specialized handler. Each handler is optimized for its specific category.

初始步驟分類輸入，然後路由到適當的專業處理器。每個處理器針對其特定類別優化。

**When to use** 適用時機: When inputs are diverse and a single approach can't handle all cases well. When you have **distinct expertise** for different input types.

輸入多樣且單一方法無法良好處理所有情況時。當你對不同輸入類型有**獨特專長**時。

**Real-world example** 真實範例:

```
Customer support routing:
客戶支援路由：

  [Analyze customer message]
       │
       ├──→ Technical issue     → [Technical troubleshooting Skill]
       │                          技術故障排除
       ├──→ Billing question    → [Billing lookup Skill]
       │                          帳務查詢
       ├──→ Feature request     → [Feature request logging Skill]
       │                          功能需求記錄
       └──→ General inquiry     → [FAQ response Skill]
                                  常見問答
```

**Mapping to the Five-Layer Model** 對應五層模型:

Routing is a **Layer 4** (Agent) behavior that selects among **Layer 3** (Skills). The Agent reads the Skill descriptions (Level 1 summaries — name + one-line description), matches the user's intent to the most relevant Skill, and loads that Skill's full definition.

路由是**第四層**（Agent）行為，從**第三層**（Skills）中選擇。Agent 讀取 Skill 描述（第一級摘要——名稱 + 一行描述），將使用者意圖匹配到最相關的 Skill，並載入該 Skill 的完整定義。

This is exactly what happens in Claude Code and Cowork: the system prompt contains short descriptions of all available Skills, and the LLM routes to the appropriate one based on the user's message.

這正是 Claude Code 和 Cowork 中發生的事：系統提示包含所有可用 Skills 的短描述，LLM 根據使用者的訊息路由到適當的 Skill。

**Design guidance** 設計指引:

- The **Skill description is the routing key** Skill 描述就是路由鍵. Write descriptions with trigger keywords that match how users naturally express their intent. "When user mentions 'team data', 'org chart', 'format profiles'..." is good routing.
  用觸發關鍵字撰寫描述，匹配使用者自然表達意圖的方式。
- When multiple Skills could match, **prefer specificity** 偏好具體性. A Skill description that says "I handle X, Y, and Z" is more routable than "I handle general tasks."
  當多個 Skills 都能匹配時，偏好具體的。

---

### Pattern C: Parallelization ── 平行化

```
               ┌──→ [Subtask A] ──→ result A ──┐
               │                                 │
[Input] ──→ Fork ──→ [Subtask B] ──→ result B ──┼──→ [Aggregate] ──→ final
               │                                 │
               └──→ [Subtask C] ──→ result C ──┘
```

**What it is** 是什麼: Independent subtasks run simultaneously, then their results are aggregated. Two variants:

獨立子任務同時執行，然後彙整結果。兩種變體：

- **Sectioning** 分段: Split the work by section — each subtask handles a different part of the output 按段落分割——每個子任務處理輸出的不同部分
- **Voting** 投票: Run the same task multiple times and aggregate (majority vote, best-of-N) 多次執行相同任務並彙整（多數決、N 取最佳）

**When to use** 適用時機: When subtasks are truly independent — no subtask needs another's output to proceed. Common for multi-section documents, multi-source research, or quality assurance through redundancy.

子任務真正獨立時——沒有子任務需要另一個的輸出才能繼續。常用於多段落文件、多來源研究，或透過冗餘進行品質保證。

**Real-world example** 真實範例:

```
Multi-source research:
多來源研究：

  "Research the competitive landscape of AI coding tools"
       │
       ├──→ [Search academic papers]     ──→ academic findings
       ├──→ [Search industry reports]    ──→ market data
       ├──→ [Search GitHub repositories] ──→ open source landscape
       └──→ [Search user reviews]        ──→ practitioner sentiment
                                              │
                                         [Synthesize] ──→ comprehensive report
```

**Mapping to the Five-Layer Model** 對應五層模型:

Parallelization is a **Layer 4** (Agent) orchestration pattern. The Agent decomposes the task, dispatches to multiple Layer 3 Skills (or multiple instances of the same Skill with different parameters), then aggregates. The individual Skills don't know they're running in parallel — they just do their job.

平行化是**第四層**（Agent）調度模式。Agent 分解任務，分派到多個第三層 Skills（或相同 Skill 的多個實例帶不同參數），然後彙整。個別 Skills 不知道它們在平行執行——它們只是做自己的工作。

In practice, many systems implement parallelization through subagents — lightweight agent instances that run independently and report back.

在實務中，許多系統透過子代理實作平行化——輕量級 Agent 實例獨立運行並回報。

---

### Pattern D: Orchestrator-Workers ── 調度者-工作者

```
┌────────────────────────────────────────────┐
│           Orchestrator Agent                │
│           調度者 Agent                       │
│                                            │
│  Receives task → Plans → Delegates         │
│  → Monitors → Aggregates → Delivers        │
│                                            │
│    ┌──────────┐ ┌──────────┐ ┌─────────┐  │
│    │ Worker 1 │ │ Worker 2 │ │ Worker 3│  │
│    │ (Skill A)│ │ (Skill B)│ │(Skill C)│  │
│    └──────────┘ └──────────┘ └─────────┘  │
└────────────────────────────────────────────┘
```

**What it is** 是什麼: A central orchestrator agent decomposes the task and dynamically delegates subtasks to worker agents, each equipped with appropriate Skills. Unlike parallelization (which has a fixed split), the orchestrator **decides dynamically** what to delegate based on the task's needs.

中央調度者 Agent 分解任務，動態委派子任務給工作者 Agent，每個配備適當的 Skills。與平行化（固定分割）不同，調度者根據任務需求**動態決定**委派什麼。

**When to use** 適用時機: Complex tasks where you can't predict the subtasks in advance. The orchestrator uses **planning** (Pattern 3) to figure out what needs to be done, then uses **tool use** (Pattern 2) or **routing** (Pattern B) to assign each subtask.

無法預先預測子任務的複雜任務。調度者使用**規劃**（模式 3）來搞清楚需要做什麼，然後使用**工具使用**（模式 2）或**路由**（模式 B）來分配每個子任務。

**Real-world example** 真實範例:

```
Project execution workflow:
專案執行工作流程：

  Orchestrator receives: "Set up project tracking for the new contract"

  Orchestrator plans:
    1. Convert proposal deliverables into work items → [transform Skill]
    2. Create repo structure with state files       → [integration Skill]
    3. Define milestone schedule                    → [planning Skill]
    4. Set up monitoring triggers                   → [config Skill]
    5. Generate team handbook                       → [document Skill]

  Each worker executes its Skill independently.
  Orchestrator monitors progress and handles dependencies.
```

**Mapping to the Five-Layer Model** 對應五層模型:

This is the **canonical Layer 4 pattern**. The orchestrator is a Layer 4 Agent with full access to Layer 3 Skills. Workers can be simpler agents (or even just Skill invocations without full agent capabilities). The orchestrator's power comes from its ability to **dynamically compose** Skills based on the task — the ["a235bc1e" pattern](../01-foundations/agentic-substrate.md) in action.

這是**典範的第四層模式**。調度者是具有完整第三層 Skills 存取的第四層 Agent。工作者可以是較簡單的 Agent（或甚至只是沒有完整 Agent 能力的 Skill 呼叫）。調度者的力量來自它能根據任務**動態組合** Skills——[「a235bc1e」模式](../01-foundations/agentic-substrate.md)的實踐。

---

### Pattern E: Evaluator-Optimizer ── 評估-優化

```
┌──────────┐     ┌──────────┐
│ Generator│ ──→ │ Evaluator│
│ 生成者   │     │ 評估者   │
│          │ ←── │          │
│  revise  │     │ feedback │
│  修改    │     │ 回饋     │
└──────────┘     └──────────┘
    loop until evaluator approves
```

**What it is** 是什麼: One LLM call generates output, another evaluates it against criteria and provides specific feedback. The generator revises based on feedback. The loop continues until the evaluator approves.

一個 LLM 呼叫生成產出，另一個根據標準評估並提供具體回饋。生成者根據回饋修改。迴圈持續直到評估者批准。

**When to use** 適用時機: When there are **clear, evaluable quality criteria** and when iteration reliably improves the output. This is the "write → edit → rewrite" pattern that any professional knows.

有**清楚、可評估的品質標準**，且迭代確實能改善產出時。這是任何專業人士都知道的「寫→編輯→重寫」模式。

**How it differs from Reflection** 與反思的差異:

Reflection (Ng's pattern) uses the same agent to generate and critique. Evaluator-Optimizer uses **separate agents** (or separate LLM calls with different system prompts) for each role. The separation creates productive tension — the evaluator doesn't rationalize the generator's choices.

反思（Ng 的模式）使用相同 Agent 生成和批評。評估-優化使用**分開的 Agent**（或帶不同系統提示的分開 LLM 呼叫）。分離產生有建設性的張力——評估者不會為生成者的選擇找理由。

**Real-world example** 真實範例:

```
Proposal writing with validation:
含驗證的提案撰寫：

  [Writer Agent]                    [Validator Agent]
  writes chapter draft    ──→      checks against criteria:
                                   ✓ Addresses all RFP requirements?
                                   ✓ Budget items match scope?
                                   ✓ Timeline is realistic?
                                   ✓ No contradictions with other chapters?
                          ←──      returns specific issues:
  revises based on                 "Section 3.2 mentions 10 events
  feedback                          but budget only covers 8"
```

**Mapping to the Five-Layer Model** 對應五層模型:

The generator is typically a **Layer 3 Skill** (like a document writer). The evaluator is either a validation component within the same Skill or a **separate Skill** dedicated to evaluation. The **Layer 4 Agent** manages the loop — deciding when quality is sufficient to stop iterating.

生成者通常是**第三層 Skill**（如文件撰寫者）。評估者是同一 Skill 內的驗證組件，或是專門用於評估的**獨立 Skill**。**第四層 Agent** 管理迴圈——決定品質何時足夠停止迭代。

---

## 5. Unified Pattern Map ── 統一模式地圖

### How the Patterns Relate ── 模式之間的關係

These nine patterns (4 foundational + 5 compositional) aren't alternatives — they're **building blocks that combine**:

這九個模式（4 個基礎 + 5 個組合）不是替代方案——它們是**可組合的建構塊**：

```
Foundational (Ng)         Compositional (Anthropic)       Combined Example
基礎                      組合                            組合範例
─────────────────         ──────────────────              ──────────────
Reflection            +   Evaluator-Optimizer          =  Self-improving Skill
                                                          with separate critic

Tool Use              +   Prompt Chaining              =  Multi-step data pipeline
                                                          that reads/writes files

Planning              +   Orchestrator-Workers         =  Dynamic project
                                                          execution system

Multi-Agent           +   Routing + Parallelization    =  Specialized team of
                                                          agents handling diverse
                                                          requests concurrently
```

### Pattern-to-Layer Mapping ── 模式與層級對應

| Pattern 模式 | Primary Layer 主要層級 | Interacts With 互動層級 |
|---|---|---|
| Reflection | L1 (LLM reasoning) | L3 (Skill validation rules) |
| Tool Use | L1 → L2 (LLM decides, tool executes) | L4 (Agent manages tool results) |
| Planning | L4 (Agent decomposes goals) | L3 (Skills are the planned units) |
| Multi-Agent | L4 (multiple Agent instances) | L2 (shared state via files/repo) |
| Prompt Chaining | L3 (Skill process logic) | L2 (tools at each step) |
| Routing | L4 (Agent selects Skill) | L3 (Skill descriptions as routing keys) |
| Parallelization | L4 (Agent dispatches) | L3 (independent Skill instances) |
| Orchestrator-Workers | L4 (orchestrator Agent) | L3 (worker Skills) |
| Evaluator-Optimizer | L3-L4 (Skill + Agent loop) | L1 (separate LLM calls for each role) |

### Complexity Spectrum ── 複雜度光譜

```
Simplest                                                    Most Complex
最簡單                                                        最複雜

Single LLM    Prompt      Routing    Evaluator-   Orchestrator-   Multi-Agent
call          Chaining               Optimizer    Workers         System
單次 LLM 呼叫  提示鏈       路由       評估-優化    調度-工作者       多代理系統

"Answer my    "Step by    "Pick the  "Draft,      "Plan, then    "Team of
question"     step"       right      evaluate,    delegate to    specialized
                          handler"   revise"      workers"       agents"

  ──────────────────────────────────────────────────────────────────→
  Start here.                                    Go here only when needed.
  從這裡開始。                                     只在需要時才走到這裡。
```

---

## 6. Anti-Patterns ── 反模式

Just as important as knowing what works is knowing what doesn't:

知道什麼不行跟知道什麼行一樣重要：

### Anti-Pattern 1: Premature Multi-Agent ── 過早的多代理

**Symptom** 症狀: Building a multi-agent system when a single agent with good Skills would suffice.

當單一 Agent 搭配好的 Skills 就足夠時，建構多代理系統。

**Why it's harmful** 為什麼有害: Each agent boundary adds communication overhead, potential misalignment, and debugging complexity. Messages between agents consume tokens. State synchronization between agents is error-prone.

每個 Agent 邊界增加通訊開銷、潛在的不對齊和除錯複雜度。Agent 之間的訊息消耗 token。Agent 之間的狀態同步容易出錯。

**Fix** 修正: Ask "Can I solve this with a single agent that has the right Skills?" If yes, do that. Add agents only when you can demonstrate that a single agent consistently fails at the task.

問「我能用一個有正確 Skills 的單一 Agent 解決這個嗎？」如果是，就那樣做。

### Anti-Pattern 2: Infinite Reflection Loop ── 無限反思迴圈

**Symptom** 症狀: An evaluator-optimizer loop that never converges — each revision introduces new issues.

評估-優化迴圈永不收斂——每次修改都引入新問題。

**Why it's harmful** 為什麼有害: Wastes tokens, time, and may actually degrade output quality after a certain point.

浪費 token、時間，且可能在某個點之後實際降低產出品質。

**Fix** 修正: Set hard iteration limits (2-3 rounds typically). Define explicit "good enough" criteria. If the output doesn't converge in 3 rounds, the Skill design needs improvement, not more iterations.

設定硬性迭代限制（通常 2-3 輪）。定義明確的「夠好」標準。如果產出在 3 輪內不收斂，需要改善的是 Skill 設計，不是更多迭代。

### Anti-Pattern 3: Over-Planning ── 過度規劃

**Symptom** 症狀: The agent spends many LLM calls creating an elaborate plan before doing any real work.

Agent 在做任何實際工作之前，花費許多 LLM 呼叫來建立精密的計劃。

**Why it's harmful** 為什麼有害: Plans become obsolete the moment execution begins and reveals unexpected conditions. Long plans consume context window space. The planning itself can hallucinate steps that aren't needed.

計劃在執行開始、揭示意外狀況的那一刻就過時了。長計劃消耗上下文窗口空間。規劃本身可能幻覺出不需要的步驟。

**Fix** 修正: Plan 2-3 steps ahead, execute, reassess. Let the task teach you what comes next.

規劃前面 2-3 步，執行，重新評估。讓任務教你下一步是什麼。

### Anti-Pattern 4: Invisible Routing ── 隱形路由

**Symptom** 症狀: The agent silently picks the wrong Skill because Skill descriptions are ambiguous or overlapping.

Agent 因為 Skill 描述模糊或重疊而靜默地選錯 Skill。

**Why it's harmful** 為什麼有害: The user gets plausible-looking but incorrect output. They may not realize the wrong Skill was used until significant work has been done.

使用者得到看似合理但不正確的輸出。他們可能直到大量工作完成後才意識到使用了錯的 Skill。

**Fix** 修正: Write Skill descriptions with explicit, non-overlapping trigger keywords. Test routing by trying ambiguous inputs and checking which Skill activates. Consider showing the user which Skill was selected: "I'm using [project-status-tracker] for this. Is that right?"

用明確、不重疊的觸發關鍵字撰寫 Skill 描述。考慮向使用者顯示選擇了哪個 Skill。

---

## 7. Decision Guide: Which Pattern When? ── 決策指南：何時用哪個模式？

```
Start here: Can a single LLM call handle this?
從這裡開始：單次 LLM 呼叫能處理嗎？
  │
  ├── Yes → Just do it. No pattern needed.
  │         直接做。不需要模式。
  │
  └── No → Is the workflow predictable (same steps every time)?
           工作流程可預測嗎（每次相同步驟）？
            │
            ├── Yes → Prompt Chaining (Pattern A)
            │         提示鏈
            │         Add Evaluator-Optimizer (E) if quality is critical
            │         品質關鍵時加入評估-優化
            │
            └── No → Does the input type vary?
                     輸入類型是否多樣？
                      │
                      ├── Yes → Routing (Pattern B)
                      │         路由
                      │
                      └── No → Can subtasks run independently?
                               子任務能獨立執行嗎？
                                │
                                ├── Yes → Parallelization (Pattern C)
                                │         平行化
                                │
                                └── No → Is it too complex for one agent?
                                         對一個 Agent 來說太複雜嗎？
                                          │
                                          ├── No → Orchestrator-Workers (D)
                                          │         (one agent, multiple Skills)
                                          │         調度者-工作者（一個 Agent，多個 Skills）
                                          │
                                          └── Yes → Multi-Agent (Pattern 4)
                                                    多代理
                                                    (last resort 最後手段)
```

And overlaying the foundational patterns:

疊加基礎模式：

- **Add Reflection** to any pattern when you need self-improvement 任何模式需要自我改善時加入反思
- **Add Tool Use** to any pattern when you need world interaction 任何模式需要與世界互動時加入工具使用
- **Add Planning** when the task has more than 3-4 non-obvious steps 任務有超過 3-4 個不明顯的步驟時加入規劃

---

## 8. The Simplicity Thesis ── 簡單論

We close with the insight that unifies all these patterns:

我們以統一所有這些模式的洞見作結：

> **The most effective agent architectures are simple loops with rich context.**
> **最有效的 Agent 架構是簡單迴圈搭配豐富的上下文。**

Claude Code proves this. Its agent loop is a `while` loop. Its power comes from:

Claude Code 證明了這一點。它的 Agent 迴圈是一個 `while` 迴圈。它的力量來自：

1. **Well-assembled context** 組裝良好的上下文: The right Skill definitions, file contents, and conversation history in the context window at the right time
2. **Good tool definitions** 好的工具定義: Clear, precise tool descriptions that help the LLM make correct decisions
3. **Robust infrastructure** 穩健的基礎設施: Permission systems, error recovery, context management — the 98.4% that isn't AI
4. **Human-in-the-loop** 人類在迴圈中: The human can see what's happening, intervene when needed, and provide course corrections

The patterns in this document are not about building **more complex** systems. They're about choosing the **right level of complexity** for each task. And the right level is almost always simpler than you think.

本文件中的模式不是關於建構**更複雜的**系統。它們是關於為每個任務選擇**正確的複雜度等級**。而正確的等級幾乎總是比你想的更簡單。

---

## Cross-References ── 相關文件

- [The Agentic Substrate: Core Architecture](../01-foundations/agentic-substrate.md) — Where these patterns were first introduced (Section 4)
  核心架構——這些模式首次被介紹之處（第 4 節）
- [The Five-Layer Model](../01-foundations/five-layer-model.md) — The stack these patterns operate within
  五層模型——這些模式運作其中的堆疊
- [Anatomy of a Skill](../01-foundations/skill-anatomy.md) — Layer 3 internals, including the validation loop (Evaluator-Optimizer in practice)
  技能模組解剖學——第三層內部，包含驗證迴圈
- [Landscape Analysis](landscape.md) — Andrew Ng and Anthropic frameworks in comparative context
  生態比較——Andrew Ng 和 Anthropic 框架的比較脈絡

## References ── 參考資料

1. Andrew Ng, ["Agentic Design Patterns"](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/) — DeepLearning.AI / Sequoia AI Ascent, 2024
2. Anthropic, ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — Composable patterns for agent design, 2025
3. Liu et al., ["Dive into Claude Code"](https://arxiv.org/abs/2604.14228) — Architecture analysis showing 1.6% AI decision logic, 2025

---

*Next: [Skill Composition Patterns →](skill-composition.md)*
*下一篇：[Skill 組合模式 →](skill-composition.md)*
