# Skill Composition Patterns
# Skill 組合模式

> *"The power of Agentic software is not in any single Skill. It's in what happens when Skills meet."*
> *「代理型軟體的力量不在任何單一 Skill。而在於 Skills 相遇時發生的事。」*

---

## 1. The Composition Problem ── 組合的問題

Software is powerful because components combine. A web application is dozens of libraries, APIs, and services working together. A spreadsheet is formulas referencing other formulas. The value isn't in any single piece — it's in the **composition**.

軟體之所以強大，是因為組件可以組合。一個網頁應用程式是數十個函式庫、API 和服務協同運作。一個試算表是公式引用其他公式。價值不在任何單一部件——而在**組合**。

But traditional composition is **hard**. It requires:

但傳統的組合很**難**。它需要：

- Strict type matching (Module A outputs `TypeX`, Module B must accept `TypeX`)
  嚴格的型別匹配（模組 A 輸出 `TypeX`，模組 B 必須接受 `TypeX`）
- Explicit interface definitions (written in code, enforced by compiler)
  明確的介面定義（用程式碼撰寫，由編譯器強制）
- Pre-coded integration logic (someone writes the glue code)
  預先寫好的整合邏輯（有人撰寫膠水程式碼）
- Compile-time or deploy-time binding (integration is locked before runtime)
  編譯時或部署時綁定（整合在執行前就鎖定）

This means every new combination requires **engineering work**. Want Module A to talk to Module C instead of Module B? Someone has to write a new adapter. This is why enterprise software integration is a multi-billion dollar industry — and why most organizations are trapped in tool silos.

這意味著每個新的組合都需要**工程工作**。想讓模組 A 跟模組 C 而不是模組 B 溝通？有人就得寫新的適配器。這就是為什麼企業軟體整合是一個數十億美元的產業——也是為什麼大多數組織被困在工具孤島中。

Agentic software solves this differently.

代理型軟體用不同的方式解決這個問題。

---

## 2. Semantic Composition: The Core Breakthrough ── 語義式組合：核心突破

### What Changes ── 什麼改變了

In the Agentic Substrate, the LLM acts as a **universal adapter** between Skills. It doesn't need type matching or interface definitions. It understands the **meaning** of each Skill's output and can transform it into whatever the next Skill needs.

在 Agentic Substrate 中，LLM 充當 Skills 之間的**通用適配器**。它不需要型別匹配或介面定義。它理解每個 Skill 輸出的**含義**，並能將其轉換為下一個 Skill 需要的任何東西。

```
Traditional (Syntactic) Composition:
傳統（語法式）組合：

  Module A ──→ { type: "ReportData",         ──→ Module B
                 fields: ["revenue", "cost"],      MUST accept exactly
                 format: "JSON" }                  this type, these fields,
                                                   this format.
                                                   Mismatch = compile error.

Agentic (Semantic) Composition:
代理型（語義式）組合：

  Skill A  ──→ "Here's a report with revenue    ──→  LLM understands
                and cost data for Q1,                  this is financial
                formatted as a Markdown table"         data for Q1
                                                          │
                                                          ▼
                                                  Skill B needs
                                                  "quarterly financial
                                                  summary for trending"
                                                          │
                                                          ▼
                                                  LLM adapts the
                                                  content to match
                                                  what Skill B expects.
                                                  No code needed.
```

### Why This Works ── 為什麼這行得通

Three properties make semantic composition possible:

三個特性讓語義式組合成為可能：

**1. LLMs understand meaning, not just format** LLM 理解含義，不只是格式

When Skill A outputs "Revenue: $2.3M, Cost: $1.8M, Margin: 22%", the LLM doesn't see a string — it understands that these are financial metrics, that margin is derived from revenue minus cost, and that this data could feed into a trend analysis, a budget comparison, or an executive summary. This semantic understanding is the "universal adapter."

當 Skill A 輸出「營收：230 萬，成本：180 萬，毛利率：22%」時，LLM 看到的不是一個字串——它理解這些是財務指標、毛利率是從營收減成本得出的、這些資料可以餵入趨勢分析、預算比較或執行摘要。這種語義理解就是「通用適配器」。

**2. Markdown carries structure AND meaning** Markdown 承載結構和含義

Markdown is both human-readable and machine-parseable. A Markdown table of financial data carries the **semantic structure** (headers tell you what each column means) without requiring a formal schema definition. This is why Markdown works as the universal interchange format — see [Markdown as the Native Medium](../01-foundations/markdown-as-medium.md).

Markdown 既是人類可讀也是機器可解析的。一個財務資料的 Markdown 表格承載了**語義結構**（表頭告訴你每一欄的含義），不需要正式的 schema 定義。

**3. I/O contracts are semantic, not syntactic** 輸入/輸出契約是語義式的，不是語法式的

A Skill's I/O contract says things like: "I accept a project description and produce a list of work items with estimated hours." This is a **semantic promise** — the LLM can match this against another Skill's output by understanding meaning, not by checking types.

一個 Skill 的 I/O 契約說的是像：「我接受一份專案描述，產出一份帶估算工時的工作項目清單。」這是一個**語義承諾**——LLM 可以透過理解含義來匹配另一個 Skill 的輸出，不是檢查型別。

---

## 3. The "a235bc1e" Pattern ── 雜湊組合模式

### The Name ── 名稱由來

The name "a235bc1e" is a visual metaphor. Given two linear Skill chains:

「a235bc1e」這個名字是一個視覺隱喻。給定兩條線性 Skill 鏈：

```
Chain A:  [a] → [b] → [c] → [d] → [e]
Chain 1:  [1] → [2] → [3] → [4] → [5]
```

The LLM can dynamically compose them into a new sequence:

LLM 可以動態將它們組合成新序列：

```
Composed: [a] → [2] → [3] → [5] → [b] → [c] → [1] → [e]
           ↑     ↑     ↑     ↑     ↑     ↑     ↑     ↑
           A     1     1     1     A     A     1     A
```

The resulting sequence — a,2,3,5,b,c,1,e — looks like a **hash value**: unpredictable from the inputs, determined by the task's actual needs, different every time the context changes. Hence "a235bc1e."

得出的序列——a,2,3,5,b,c,1,e——看起來像一個**雜湊值**：從輸入無法預測、由任務的實際需求決定、每次上下文改變都不同。因此叫「a235bc1e」。

### How It Actually Works ── 實際如何運作

Let's trace through a concrete example. Imagine a Knowledge Worker has these Skills available:

讓我們追蹤一個具體的範例。假設一位知識工作者有這些可用的 Skills：

```
Proposal Pipeline:
提案管線：
  [A] Requirement Analysis    需求分析    → produces: requirement_summary.md
  [B] Structure Planning      架構規劃    → produces: table_of_contents.md
  [C] Chapter Writing         章節撰寫    → produces: chapter_XX.md
  [D] Chapter Validation      章節驗證    → produces: validation_report.md
  [E] Document Assembly       文件組裝    → produces: final_proposal.docx

Project Pipeline:
專案管線：
  [1] Deliverable Parsing     交付物解析  → produces: work_items.md
  [2] Repo Structure          Repo 架構   → produces: directory tree + state files
  [3] Milestone Definition    里程碑定義  → produces: milestones.md
  [4] Monitoring Setup        監控設定    → produces: trigger.yaml
  [5] Handbook Generation     手冊產出    → produces: agent_handbook.md
```

Now the user says: **"We won the contract. Take our proposal and set up the project for execution."**

現在使用者說：**「我們得標了。拿我們的提案來建置執行專案。」**

The Agent (Layer 4) reasons through this:

Agent（第四層）推理如下：

```
Step 1: The proposal already exists (Skills A-E were run previously).
        The validated chapters (D's output) contain the deliverables.
        → No need to re-run A, B, C, E.
        → Start from D's output.

Step 2: Parse the deliverables from the proposal into work items.
        → Call Skill [1] with D's output as input.

Step 3: Create the repo structure for execution tracking.
        → Call Skill [2] with [1]'s output.

Step 4: Define milestones based on the proposal timeline.
        → Call Skill [3] with [2]'s output + original proposal's
          timeline section (from C's output).

Step 5: Generate the execution handbook.
        → Call Skill [5] with all accumulated outputs.

Step 6: Package into a formatted document for the team.
        → Call Skill [E] to assemble the final deliverable.

Dynamic Composition: [D] → [1] → [2] → [3] → [5] → [E]
                      ↑     ↑     ↑     ↑     ↑     ↑
                      A     1     1     1     1     A
```

Notice what happened:

注意發生了什麼：

- Skills from **two different pipelines** were combined 來自**兩條不同管線**的 Skills 被組合
- The order was **determined at runtime** by the task's needs 順序在**執行時**由任務需求決定
- Skills [A], [B], [C], [4] were **skipped** because they weren't needed Skills [A]、[B]、[C]、[4] 被**跳過**因為不需要
- Skill [E] (from Pipeline A) was used at the **end** of a Pipeline-1-heavy sequence Skill [E]（來自管線 A）被用在以管線 1 為主的序列**末端**
- No engineer wrote this specific combination 沒有工程師寫過這個特定的組合

**This is the "a235bc1e" pattern in action**: dynamic, semantic, intent-driven composition.

**這就是「a235bc1e」模式的實踐**：動態的、語義式的、意圖驅動的組合。

---

## 4. Composition Mechanics ── 組合的機制

### The Three Requirements ── 三個要求

For semantic composition to work, each Skill needs to provide three things:

語義式組合要運作，每個 Skill 需要提供三件事：

```
┌─────────────────────────────────────────────┐
│  Requirement 1: Semantic I/O Contract        │
│  語義式輸入/輸出契約                          │
│                                              │
│  Not: "accepts JSON with fields x, y, z"    │
│  But: "accepts a project description with    │
│        scope, timeline, and budget"          │
│                                              │
│  The contract describes MEANING,             │
│  not FORMAT.                                 │
│  契約描述的是含義，不是格式。                  │
├─────────────────────────────────────────────┤
│  Requirement 2: Markdown as Output Medium    │
│  Markdown 作為輸出媒介                        │
│                                              │
│  Every Skill produces .md files that are:    │
│  • Human-readable (inspectable)              │
│  • LLM-parseable (composable)                │
│  • Git-trackable (versionable)               │
│  • Self-documenting (headers = schema)       │
├─────────────────────────────────────────────┤
│  Requirement 3: Independence                 │
│  獨立性                                      │
│                                              │
│  Each Skill must be executable alone.        │
│  It should not assume any specific           │
│  predecessor or successor Skill.             │
│  每個 Skill 必須能獨立執行。                  │
│  不應假設任何特定的前驅或後繼 Skill。          │
└─────────────────────────────────────────────┘
```

### How the LLM Bridges Skills ── LLM 如何橋接 Skills

When the Agent needs to pass output from Skill A to Skill B, the LLM performs a **semantic bridge** operation:

當 Agent 需要把 Skill A 的輸出傳給 Skill B 時，LLM 執行一個**語義橋接**操作：

```
Skill A Output                    Skill B Input Contract
Skill A 的輸出                     Skill B 的輸入契約

"## Validated Chapters            "Accepts: structured content
 - Ch1: Introduction ✓             with identifiable sections
 - Ch2: Methodology ✓              and deliverable items"
 - Ch3: Budget ✓
 - Ch4: Timeline ✓
   - Deliverable 1: ...
   - Deliverable 2: ..."

        │                                  │
        └──────────── LLM ────────────────┘
                       │
                       ▼
              Semantic Bridge:
              「A's output contains validated chapters
               with identifiable deliverables in Ch4.
               B needs structured content with sections
               and deliverable items.
               → Extract Ch4's deliverable list
               → Format as B's expected input.」
```

The LLM doesn't need to "convert formats." It **understands** that A's validated chapters contain deliverables, and B needs deliverables as input. The bridge is semantic, not syntactic.

LLM 不需要「轉換格式」。它**理解** A 的已驗證章節包含交付物，而 B 需要交付物作為輸入。橋接是語義式的，不是語法式的。

### Composition at Different Scales ── 不同尺度的組合

Composition isn't just about chaining entire Skills. It operates at multiple scales:

組合不只是串接整個 Skills。它在多個尺度上運作：

```
Scale 1: Intra-Skill (within a single Skill)
尺度一：Skill 內部

  A Skill's process steps compose internally:
  [Read data] → [Analyze] → [Validate] → [Format]
  
  This is Prompt Chaining (see Design Patterns).


Scale 2: Inter-Skill (between Skills)
尺度二：Skills 之間

  Multiple Skills chain, with LLM adapting outputs:
  [Skill A] → LLM bridge → [Skill B] → LLM bridge → [Skill C]
  
  This is the "a235bc1e" pattern.


Scale 3: Inter-Pipeline (across entire workflows)
尺度三：跨管線

  Entire pipelines connect through shared artifacts:
  [Proposal Pipeline] → produces .md files → [Execution Pipeline]
  
  The connection happens through files in the repo,
  not through direct Skill-to-Skill calls.


Scale 4: Inter-Agent (across agents)
尺度四：跨 Agent

  Different agents (possibly on different machines)
  compose through shared repositories:
  [PM Agent] writes milestones.md → [Writer Agent] reads it
  
  No direct communication needed — the repo IS the protocol.
```

---

## 5. Composition Patterns ── 組合模式

### Pattern 1: Linear Chain ── 線性鏈

```
[A] → [B] → [C]

Each Skill's output feeds directly into the next.
每個 Skill 的輸出直接餵入下一個。
```

**When to use** 適用時機: Tasks with a clear sequential dependency. Step 2 genuinely can't start until Step 1 is complete.

有清楚順序依賴的任務。步驟 2 確實無法在步驟 1 完成前開始。

**Example** 範例: Research → Draft → Review. You can't draft without research, can't review without a draft.

研究 → 起草 → 審查。沒有研究就不能起草，沒有草稿就不能審查。

**Composition contract** 組合契約:
```
Skill A.output_contract ──semantic match──→ Skill B.input_contract
```

---

### Pattern 2: Fan-Out / Fan-In ── 扇出/扇入

```
         ┌──→ [B1] ──→ result 1 ──┐
[A] ─────┼──→ [B2] ──→ result 2 ──┼──→ [C] (merge)
         └──→ [B3] ──→ result 3 ──┘
```

**When to use** 適用時機: When a task can be split into independent parallel subtasks. The merge step (C) synthesizes the parallel results.

任務可以分成獨立的平行子任務時。合併步驟 (C) 綜合平行結果。

**Example** 範例: A comprehensive research report where B1 searches academic papers, B2 searches industry data, B3 searches practitioner forums. C synthesizes all findings.

綜合研究報告，B1 搜尋學術論文、B2 搜尋產業數據、B3 搜尋實務論壇。C 綜合所有發現。

**Composition contract** 組合契約:
```
Skill A.output ──(split by topic)──→ Skill B1.input, B2.input, B3.input
Skill B1.output + B2.output + B3.output ──(merge)──→ Skill C.input
```

The LLM handles both the split and the merge semantically. It decides how to partition the work and how to combine the results.

LLM 語義式地處理分割和合併。它決定如何分配工作以及如何組合結果。

---

### Pattern 3: Conditional Routing ── 條件式路由

```
         ┌──→ [B] (if condition X)
[A] ─────┤
         └──→ [C] (if condition Y)
```

**When to use** 適用時機: When the next step depends on what Skill A discovers. Different inputs require different specialized handling.

下一步取決於 Skill A 發現了什麼時。不同的輸入需要不同的專業處理。

**Example** 範例: A document analysis Skill (A) determines the document type. Financial documents route to a financial review Skill (B). Legal documents route to a compliance check Skill (C).

文件分析 Skill (A) 確定文件類型。財務文件路由到財務審查 Skill (B)。法律文件路由到合規檢查 Skill (C)。

**Composition contract** 組合契約:
```
Skill A.output includes: classification + content
LLM reads classification → selects Skill B or C → feeds content
```

---

### Pattern 4: Iterative Loop ── 迭代迴圈

```
[A] → output → [B] (evaluate)
 ↑                    │
 └── feedback ────────┘
 (loop until B approves)
```

**When to use** 適用時機: Quality-critical tasks where the first attempt is rarely good enough. The evaluator (B) provides specific feedback that the generator (A) uses to improve.

品質關鍵的任務，第一次嘗試很少夠好。評估者 (B) 提供具體回饋讓生成者 (A) 用來改善。

**Example** 範例: A chapter writing Skill (A) drafts content. A validation Skill (B) checks against requirements, identifies gaps, and provides revision instructions. A revises. B re-evaluates. Loop until passing.

章節撰寫 Skill (A) 起草內容。驗證 Skill (B) 對照需求檢查、識別缺口、提供修改指示。A 修改。B 重新評估。迴圈直到通過。

**Composition contract** 組合契約:
```
Skill A.output → content (Markdown)
Skill B.output → { pass: boolean, feedback: string }
If not pass: A receives B's feedback as additional input
```

---

### Pattern 5: Dynamic Composition (a235bc1e) ── 動態組合

```
Available Skills: [A] [B] [C] [D] [E] [1] [2] [3] [4] [5]

Task: "Take the validated proposal and set up project execution"

Agent reasons: → Need D's output, then 1, 2, 3, 5, then E

Composed: [D] → [1] → [2] → [3] → [5] → [E]
```

**When to use** 適用時機: Complex, novel tasks that don't match any single pipeline. The Agent must compose a new workflow from available Skills based on the task's unique requirements.

不匹配任何單一管線的複雜新穎任務。Agent 必須根據任務獨特的需求從可用 Skills 組合新的工作流程。

**This is the most powerful pattern** because it means your Skill library grows in combinatorial value: 10 Skills don't give you 10 capabilities — they give you **hundreds of possible compositions**.

**這是最強大的模式**，因為它意味著你的 Skill 庫以組合方式增長價值：10 個 Skills 不是給你 10 種能力——而是給你**數百種可能的組合**。

---

## 6. The Role of Markdown ── Markdown 的角色

Markdown is not just a convenience — it's the **architectural enabler** of Skill composition. Without a shared medium that is simultaneously human-readable, LLM-parseable, and git-trackable, dynamic composition would require complex serialization protocols.

Markdown 不只是方便——它是 Skill 組合的**架構上的推動力**。沒有一個同時是人類可讀、LLM 可解析、Git 可追蹤的共享媒介，動態組合就需要複雜的序列化協議。

### Why Not JSON / XML / Database? ── 為什麼不用 JSON / XML / 資料庫？

| Medium 媒介 | Human Readable 人類可讀 | LLM Parseable LLM 可解析 | Git Friendly Git 友善 | Semantic Structure 語義結構 |
|---|---|---|---|---|
| **Markdown** | Yes (native) | Yes (trained on it) | Yes (text diff) | Yes (headers, tables) |
| JSON | With tooling | Yes but verbose | Yes | Structure only, no semantics |
| XML | Barely | Verbose, error-prone | Yes | Formal but heavyweight |
| Database | No (requires client) | Not directly | No (binary) | Schema-dependent |
| Plain text | Yes | Yes but no structure | Yes | No |

Markdown hits the sweet spot: it has **enough structure** (headers, lists, tables, code blocks) to carry semantic information, but **not so much formality** that it becomes a barrier. The LLM was trained on millions of Markdown files and understands their conventions natively.

Markdown 恰好在甜蜜點：它有**足夠的結構**（標題、列表、表格、程式碼區塊）來承載語義資訊，但**沒有太多的形式化**以至於成為障礙。LLM 在數百萬個 Markdown 檔案上訓練過，原生理解它們的慣例。

For the full treatment of Markdown's role, see [Markdown as the Native Medium](../01-foundations/markdown-as-medium.md).

---

## 7. Composition Failures ── 組合的失敗

Semantic composition is powerful, but it can fail. Understanding failure modes helps you design more robust Skills.

語義式組合很強大，但可能失敗。理解失敗模式幫助你設計更穩健的 Skills。

### Failure 1: Semantic Mismatch ── 語義不匹配

```
Skill A outputs: "List of team members with roles"
Skill B expects: "Budget breakdown by category"

LLM attempts bridge → produces nonsensical output
因為兩個 Skill 的語義不匹配，LLM 嘗試橋接但產出無意義的結果
```

**Cause** 原因: The Agent selected the wrong Skill, or the task decomposition was flawed.

**Prevention** 預防: Write clear I/O contracts. The Agent should verify semantic compatibility before composing.

寫清楚的 I/O 契約。Agent 應在組合前驗證語義相容性。

### Failure 2: Information Loss ── 資訊流失

```
Skill A outputs: Detailed 5-page analysis with footnotes
LLM bridge: Summarizes to 1 paragraph to fit Skill B's expected input
Skill B receives: Insufficient detail to do its job
```

**Cause** 原因: The bridge over-compressed the information. The LLM tried to be concise and lost critical details.

**Prevention** 預防: Design I/O contracts that specify the **level of detail** needed. "Accepts a detailed analysis with specific metrics" is better than "accepts analysis."

設計指定**所需詳細程度**的 I/O 契約。「接受帶有具體指標的詳細分析」比「接受分析」好。

### Failure 3: Context Window Overflow ── 上下文窗口溢出

```
Skill A outputs: 30,000 tokens
Skill B's definition: 2,000 tokens
Conversation history: 50,000 tokens
LLM bridge + reasoning: needs ~20,000 tokens
Total: 102,000 tokens → may exceed window or starve reasoning space
```

**Cause** 原因: Passing large artifacts directly through the LLM's context window instead of using file references.

**Prevention** 預防: Large outputs should be **written to files**, with only a summary and file path passed through the context window. The next Skill reads the file via Layer 2 tools.

大型輸出應該**寫入檔案**，只有摘要和檔案路徑通過上下文窗口傳遞。下一個 Skill 透過第二層工具讀取檔案。

```
Good pattern 好的模式:
  Skill A → writes analysis.md (30K tokens) to disk
          → passes to LLM: "Analysis saved to analysis.md.
            Key findings: X, Y, Z. 3 sections, 12 pages."
          → Skill B reads analysis.md via file tool when needed

Bad pattern 壞的模式:
  Skill A → dumps entire 30K token output into context window
          → Skill B drowns in context
```

### Failure 4: Circular Composition ── 循環組合

```
Skill A's output → feeds Skill B
Skill B's output → feeds Skill C
Skill C's output → feeds Skill A (!)
→ Infinite loop
```

**Cause** 原因: The Agent's planning didn't detect the cycle, or the task decomposition creates a circular dependency.

**Prevention** 預防: Keep a composition trace — a log of which Skills have been called in the current sequence. If a Skill appears twice, stop and re-evaluate.

保持組合追蹤——當前序列中已呼叫哪些 Skills 的日誌。如果一個 Skill 出現兩次，停下來重新評估。

### Failure 5: Skill Granularity Mismatch ── Skill 粒度不匹配

```
Skill A: A massive "do everything" Skill (too coarse)
Skill B: A tiny "capitalize first letter" Skill (too fine)

Composing them produces awkward, unbalanced workflows.
```

**Cause** 原因: Skills weren't designed with composition in mind. Too-coarse Skills can't be reused in new contexts. Too-fine Skills create overhead without adding meaningful structure.

**Prevention** 預防: Follow the **"one Skill, one job"** principle. A Skill should represent a **meaningful unit of work** — significant enough to be worth naming, focused enough to be reusable.

遵循**「一個 Skill，一個工作」**原則。一個 Skill 應代表一個**有意義的工作單元**——重要到值得命名，聚焦到可以重用。

---

## 8. Designing for Composability ── 為可組合性而設計

### The Composability Checklist ── 可組合性檢查清單

When designing a Skill, verify:

設計 Skill 時，驗證：

```
□ Can this Skill run independently?
  這個 Skill 能獨立運行嗎？
  → If it REQUIRES another specific Skill to run first,
    they should probably be one Skill.

□ Is the output self-explanatory?
  輸出是否不言自明？
  → Someone (or some LLM) reading only the output should
    understand what it contains, without knowing which
    Skill produced it.

□ Is the output in Markdown?
  輸出是 Markdown 嗎？
  → Non-Markdown outputs (binary files, images) should
    be accompanied by a Markdown summary describing
    what was produced.

□ Does the I/O contract describe meaning, not format?
  I/O 契約描述的是含義還是格式？
  → "Produces a prioritized list of action items with
    deadlines" > "Produces a JSON array of objects."

□ Is the Skill focused on one job?
  Skill 聚焦在一個工作上嗎？
  → If you need "and" to describe what it does, consider
    splitting.

□ Does it handle graceful degradation?
  它是否處理優雅降級？
  → What happens if the input is incomplete or unexpected?
    A composable Skill should report what's missing rather
    than silently producing garbage.
```

### The Output Header Convention ── 輸出標頭慣例

A practical convention that dramatically improves composability: every Skill's output starts with a **header block** that describes what it contains.

一個大幅改善可組合性的實務慣例：每個 Skill 的輸出以描述其內容的**標頭區塊**開始。

```markdown
# [Skill Name] Output
- **Produced by**: requirement-analysis
- **Date**: 2026-04-21
- **Input was**: RFP document for "2026 Youth Innovation Program"
- **Contains**: Requirement summary, evaluation criteria,
  key constraints, risk factors
- **Can feed into**: structure-planning, milestone-definition,
  budget-estimation

---

## Requirement Summary
...
```

This header serves as a **composition hint** — telling the LLM (and humans) what this artifact is, where it came from, and where it could go next. It makes the "semantic bridge" operation much more reliable.

這個標頭作為**組合提示**——告訴 LLM（和人類）這個產物是什麼、從哪裡來、可以去哪裡。它讓「語義橋接」操作更加可靠。

---

## 9. Combinatorial Value ── 組合價值

### Why This Changes Everything ── 為什麼這改變了一切

In traditional software, the value of your component library grows **linearly**: 10 modules give you ~10 capabilities. Each new capability requires new integration code.

在傳統軟體中，你的元件庫價值**線性**增長：10 個模組給你約 10 種能力。每個新能力需要新的整合程式碼。

In the Agentic Substrate, value grows **combinatorially**: 10 Skills give you potentially **hundreds** of compositions. Each new Skill doesn't just add one capability — it multiplies the possible compositions with every existing Skill.

在 Agentic Substrate 中，價值**組合式**增長：10 個 Skills 給你潛在**數百種**組合。每個新 Skill 不只增加一個能力——它與每個現有 Skill 相乘可能的組合。

```
Skills:  5       10       20       50
         │        │        │        │
         ▼        ▼        ▼        ▼
Linear:  5       10       20       50     (traditional)
Combinatorial:
         ~20     ~100     ~400    ~2500    (agentic)

(Not all combinations are meaningful, but many unexpected
 ones turn out to be exactly what a novel task needs.)
```

This is why **building more Skills is always a good investment**. Each Skill you add doesn't just solve one problem — it enriches the entire Skill ecosystem by creating new composition possibilities.

這就是為什麼**建立更多 Skills 永遠是好的投資**。你添加的每個 Skill 不只是解決一個問題——它透過創造新的組合可能性，豐富了整個 Skill 生態系。

And this is also why the [Skill Self-Discovery](../../skills/skill-self-discovery/) exercise matters: every domain expert who converts their daily workflow into a Skill isn't just capturing one process — they're adding a new composable node to the organizational Skill network.

這也是為什麼[技能自我發現](../../skills/skill-self-discovery/)練習很重要：每位將日常工作流程轉換為 Skill 的領域專家，不只是捕捉一個流程——他們是在組織的 Skill 網路中添加一個新的可組合節點。

---

## Summary ── 總結

Skill composition is the mechanism that transforms a collection of individual Skills into a **software ecosystem**. The key insights:

Skill 組合是將個別 Skills 的集合轉變為**軟體生態系**的機制。關鍵洞見：

1. **Semantic over syntactic** 語義式優於語法式: The LLM understands meaning, enabling composition without type matching or interface code.
   LLM 理解含義，無需型別匹配或介面程式碼即可組合。

2. **Markdown as the universal protocol** Markdown 作為通用協議: Human-readable, LLM-parseable, git-trackable — the shared medium that makes composition practical.
   人類可讀、LLM 可解析、Git 可追蹤——讓組合成為實際可行的共享媒介。

3. **Dynamic composition (a235bc1e)** 動態組合: The LLM composes Skills at runtime based on the task's unique needs — no pre-coded pipelines required.
   LLM 在執行時根據任務獨特需求組合 Skills——不需要預先寫好的管線。

4. **Combinatorial value** 組合價值: Each new Skill multiplies the possible compositions with every existing Skill. 10 Skills >> 10 capabilities.
   每個新 Skill 與每個現有 Skill 相乘可能的組合。10 個 Skills >> 10 種能力。

5. **Design for independence** 為獨立性而設計: Each Skill should run alone, produce self-explanatory Markdown output, and describe its I/O in semantic terms.
   每個 Skill 應能獨立運行、產出不言自明的 Markdown 輸出、用語義術語描述 I/O。

---

## Cross-References ── 相關文件

- [Anatomy of a Skill](../01-foundations/skill-anatomy.md) — The seven components, including I/O Contract and Composition Hooks
  技能模組解剖學——七大組件，包含 I/O 契約和組合掛鉤
- [Markdown as the Native Medium](../01-foundations/markdown-as-medium.md) — Why Markdown is the composition protocol
  Markdown 作為原生媒介——為什麼 Markdown 是組合協議
- [The Five-Layer Model](../01-foundations/five-layer-model.md) — Where composition happens (Layer 3-4 interaction)
  五層模型——組合發生的位置（第三-四層互動）
- [Agentic Design Patterns](agentic-design-patterns.md) — Orchestration patterns that use composition
  代理型設計模式——使用組合的調度模式

---

*Next: [Memory & State Management →](memory-and-state.md)*
*下一篇：[記憶與狀態管理 →](memory-and-state.md)*
