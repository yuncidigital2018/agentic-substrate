# Landscape: Existing Frameworks & Where Agentic Substrate Fits
# 生態地圖：現有框架與 Agentic Substrate 的定位

> *"If I have seen further, it is by standing on the shoulders of giants."*
> *「如果我看得更遠，那是因為站在巨人的肩膀上。」*
> — Isaac Newton

Agentic Substrate does not exist in a vacuum. Multiple researchers, companies, and open-source communities are exploring overlapping territories. This document maps the landscape — what exists, what each framework contributes, and where Agentic Substrate's unique position lies.

Agentic Substrate 不是憑空產生的。多位研究者、企業和開源社群正在探索重疊的領域。本文件繪製這張地圖——什麼已經存在、每個框架貢獻了什麼、以及 Agentic Substrate 的獨特定位在哪裡。

---

## 1. The Seven Pillars of the Current Landscape ── 現有地貌的七根支柱

### 1.1 AIOS — LLM Agent Operating System
**Origin 來源**: Rutgers University (2024), published at COLM 2025
**Repo**: [github.com/agiresearch/AIOS](https://github.com/agiresearch/AIOS)

**Core Idea 核心概念**: Embed an LLM into the operating system kernel as the "brain" of the OS. Redesign traditional OS components — scheduler, context manager, memory manager, access control — around LLM agent needs.

**核心概念**：將 LLM 嵌入作業系統核心作為 OS 的「大腦」。圍繞 LLM Agent 需求重新設計傳統 OS 元件——排程器、情境管理器、記憶管理器、存取控制。

**Architecture 架構**:
```
┌─────────────────────────────┐
│     Application Layer        │  ← Agents built with AIOS SDK
├─────────────────────────────┤
│     AIOS Kernel              │  ← Agent Scheduler, Context Manager,
│                              │     Memory Manager, Storage Manager
├─────────────────────────────┤
│     Traditional OS Kernel    │  ← Hardware abstraction, file system
└─────────────────────────────┘
```

**Strengths 優勢**:
- Rigorous academic framing — maps traditional OS concepts to AI agent needs 嚴謹的學術框架——將傳統 OS 概念映射到 AI Agent 需求
- Published and peer-reviewed at major conference 在主要學術會議發表並經過同儕審查
- Supports multiple agent frameworks (ReAct, AutoGen, MetaGPT) 支援多種 Agent 框架

**Limitations 局限**:
- Purely systems-level — no concept of "Skills" as composable workflow units 純系統層級——沒有「Skills」作為可組合工作流程單元的概念
- Academic orientation — not designed for practitioner learning 學術導向——不是為實踐者學習而設計
- No treatment of the "what do I build on top of this" question 沒有處理「我在這上面建什麼」的問題

---

### 1.2 Superpowers Framework
**Origin 來源**: Jesse Vincent (obra), 2026
**Repo**: [github.com/obra/superpowers](https://github.com/obra/superpowers) — 121K+ stars in 5 months

**Core Idea 核心概念**: A complete software development methodology for coding agents, built on composable Markdown-based Skills. The agent doesn't just write code — it follows a structured process: clarify requirements → produce spec → plan implementation → execute → verify.

**核心概念**：一套完整的 coding agent 軟體開發方法論，建立在可組合的 Markdown-based Skills 上。Agent 不只是寫程式——它遵循結構化流程：釐清需求→產出規格→規劃實作→執行→驗證。

**Architecture 架構**:
```
User Intent
    ↓
[Superpowers Methodology]
    ↓
┌──────────────────────────────────┐
│  Skill: Clarify Requirements      │
│  Skill: Write Spec                │
│  Skill: Plan Implementation       │
│  Skill: Subagent-Driven Dev       │
│  Skill: Quality Verification      │
└──────────────────────────────────┘
    ↓
Production Code
```

**Strengths 優勢**:
- Proven at massive scale — 121K GitHub stars signals real adoption 在大規模得到驗證——121K stars 代表真實的採用
- Practical, opinionated methodology — not just a toolbox 實際的、有主張的方法論——不只是工具箱
- Clear Skill composition patterns with SKILL.md format 清楚的 Skill 組合模式與 SKILL.md 格式
- Created by an experienced practitioner (Perl project lead, Keyboardio founder) 由經驗豐富的實踐者創建

**Limitations 局限**:
- **Coding-only** — exclusively designed for software development workflows **僅限寫程式**——專為軟體開發工作流設計
- No architectural theory — doesn't explain *why* this paradigm works 沒有架構理論——不解釋*為什麼*這個典範有效
- No learning path for non-engineers 沒有為非工程師設計的學習路徑
- English-only, engineer-only audience 僅英文、僅工程師受眾

---

### 1.3 SKILL.md Format Standard
**Origin 來源**: Community-driven initiative, 2025-2026
**Reference**: [The SKILL.md Format: A Standard for Portable AI Agent Capabilities](https://dev.to/zacvibecodez/the-skillmd-format-a-standard-for-portable-ai-agent-capabilities-1mf5)
**Related**: [awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills)

**Core Idea 核心概念**: Define a standardized Markdown format for AI agent Skills — specifying inputs, outputs, behavior, and constraints — so Skills can be portable across different agent frameworks.

**核心概念**：定義一種標準化的 Markdown 格式來描述 AI Agent Skills——指定輸入、輸出、行為和約束——讓 Skills 可以在不同 Agent 框架之間移植。

**Strengths 優勢**:
- Addresses the portability problem — Skills shouldn't be locked to one framework 解決了可攜性問題——Skills 不應被鎖定在某個框架
- Simple and practical — just Markdown with conventions 簡單實用——只是帶有慣例的 Markdown
- Growing ecosystem with curated skill collections 有策展的 skill 集合的成長生態系

**Limitations 局限**:
- Format specification only — no architecture, no learning path, no design philosophy 僅格式規格——沒有架構、沒有學習路徑、沒有設計哲學
- Doesn't address how Skills compose or how Agents orchestrate them 沒有處理 Skills 如何組合或 Agents 如何調度它們
- No conceptual model for understanding the larger system 沒有理解更大系統的概念模型

---

### 1.4 The "Skills vs MCP" Discourse
**Origin 來源**: Industry discourse, early 2026
**Key Article**: [Skills vs MCP: Agent Architecture (The New Stack)](https://thenewstack.io/skills-vs-mcp-agent-architecture/)

**Core Idea 核心概念**: An emerging consensus that Skills (Markdown-based knowledge/workflow definitions) and MCP (Model Context Protocol for tool integration) serve complementary roles in a layered architecture, not competing ones.

**核心概念**：一個正在形成的共識——Skills（Markdown-based 知識/工作流程定義）和 MCP（用於工具整合的 Model Context Protocol）在分層架構中扮演互補角色，而非競爭。

**The Emerging Three-Layer Stack 正在浮現的三層堆疊**:
```
┌──────────────────────────┐
│  Skills Layer             │  ← Knowledge, workflow, quality bar
│  (Markdown files)         │     知識、工作流程、品質標準
├──────────────────────────┤
│  MCP Layer                │  ← Standardized tool access
│  (Protocol + servers)     │     標準化的工具存取
├──────────────────────────┤
│  Tools Layer              │  ← Individual action execution
│  (Functions, APIs, CLI)   │     個別動作執行
└──────────────────────────┘
```

**Key Data Point 關鍵數據**: An 800-token Markdown skill file outperformed a 28,000-token MCP schema — the agent made fewer tool calls and finished faster.

**關鍵數據**：一個 800 token 的 Markdown skill 檔案，效果優於 28,000 token 的 MCP schema——Agent 呼叫更少的工具且更快完成。

**Strengths 優勢**:
- Grounded in real performance data 基於真實性能數據
- Clarifies a confusing either/or debate into a complementary model 將混淆的二選一辯論釐清為互補模型
- Practical implications for token efficiency and system design 對 token 效率和系統設計有實際意涵

**Limitations 局限**:
- Descriptive, not prescriptive — observes what's happening but doesn't provide a design framework 描述性而非規範性——觀察正在發生的事但不提供設計框架
- Focused on the Skill-vs-MCP layer only — doesn't address Agent layer or the full stack 只聚焦在 Skill vs MCP 層——不涉及 Agent 層或完整堆疊

---

### 1.5 Andrew Ng's Four Agentic Design Patterns
**Origin 來源**: Andrew Ng, 2024 (Sequoia AI Ascent, DeepLearning.AI)

**Core Idea 核心概念**: Four foundational patterns that make LLM-based agents effective: Reflection, Tool Use, Planning, and Multi-Agent Collaboration.

**核心概念**：四種使 LLM-based Agent 有效的基礎模式：反思、工具使用、規劃、多代理協作。

| Pattern 模式 | Key Insight 關鍵洞見 |
|---|---|
| **Reflection** 反思 | Self-critique and iterative improvement dramatically increases output quality 自我批評和迭代改善大幅提升產出品質 |
| **Tool Use** 工具使用 | External tools transform text generators into operational systems 外部工具將文字生成器轉變為可運作的系統 |
| **Planning** 規劃 | Goal decomposition enables autonomous multi-step execution 目標分解使自主多步驟執行成為可能 |
| **Multi-Agent** 多代理 | Specialized agents collaborating outperform generalist agents 專業化 Agent 協作優於通才 Agent |

**Key Evidence 關鍵證據**: GPT-3.5 wrapped in an agentic loop achieved **95.1%** on HumanEval coding benchmarks vs. **48.1%** in zero-shot mode. Architecture matters as much as the model.

GPT-3.5 套上代理迴圈在 HumanEval 編碼基準測試達到 **95.1%**，而零次提示模式只有 **48.1%**。架構的重要性等同於模型本身。

**Strengths 優勢**:
- Foundational vocabulary adopted by the entire industry 全產業採用的基礎詞彙
- Backed by compelling empirical evidence 有令人信服的實證支持
- Simple, memorable, teachable 簡單、好記、可教學

**Limitations 局限**:
- Design patterns only — no system architecture, no implementation guidance 僅設計模式——沒有系統架構、沒有實作指引
- Doesn't address Skill composition, state management, or learning paths 沒有涉及 Skill 組合、狀態管理或學習路徑
- Targeted at AI researchers and engineers, not broader audience 面向 AI 研究者和工程師，而非更廣泛的受眾

---

### 1.6 Anthropic's "Building Effective Agents"
**Origin 來源**: Anthropic, December 2024
**Reference**: [anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)

**Core Idea 核心概念**: Practical guide to building agents with composable patterns. Core philosophy: **start simple, add complexity only when needed.** Defines five compositional patterns: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer.

**核心概念**：使用可組合模式建構 Agent 的實務指南。核心哲學：**從簡單開始，只在需要時才加複雜度。**定義五種組合模式。

**Complemented by 搭配**:
- ["Dive into Claude Code" (arXiv 2604.14228)](https://arxiv.org/abs/2604.14228) — Third-party analysis revealing Claude Code's architecture: **1.6% AI logic, 98.4% deterministic infrastructure** 第三方分析揭示 Claude Code 架構：**1.6% AI 邏輯、98.4% 確定性基礎設施**
- [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) — Tool-use-first approach, agents invoke other agents as tools 工具優先方法，Agent 可作為工具調用其他 Agent

**Strengths 優勢**:
- Battle-tested by the company that builds Claude 由建構 Claude 的公司實戰驗證
- Grounded in real customer deployment patterns 基於真實客戶部署模式
- The "1.6% / 98.4%" insight is one of the most powerful framing devices in the field 「1.6% / 98.4%」的洞見是領域中最有力的框架表述之一

**Limitations 局限**:
- Practical guide, not a conceptual framework — tells you *how* but not *what this all means* 實務指南，不是概念框架——告訴你*怎麼做*但不是*這一切代表什麼*
- No learning path or curriculum 沒有學習路徑或課綱
- Doesn't attempt to describe the paradigm shift at a philosophical level 沒有嘗試在哲學層級描述典範轉移

---

### 1.7 Agent Skills Open Standard (Anthropic)
**Origin 來源**: Anthropic, October 2025 (concept) → December 2025 (open standard)
**Repo**: [github.com/anthropics/skills](https://github.com/anthropics/skills) — 122K+ stars
**Specification**: [agentskills.io](https://agentskills.io)

**Core Idea 核心概念**: A standardized, open specification for defining portable AI agent Skills — launched by Anthropic and adopted by OpenAI, Microsoft (VS Code, GitHub Copilot), Cursor, Goose, and Amp. This is Anthropic's **second industry standard** after MCP (Model Context Protocol): MCP standardized tool access; Agent Skills standardizes the knowledge/workflow layer above it.

**核心概念**：一個標準化、開放的 AI Agent Skills 定義規格——由 Anthropic 推出，被 OpenAI、Microsoft（VS Code、GitHub Copilot）、Cursor、Goose 和 Amp 採用。這是 Anthropic 繼 MCP 之後的**第二個產業標準**：MCP 標準化了工具存取；Agent Skills 標準化了工具之上的知識/工作流程層。

**Architecture 架構**:
```
                Agent Skills Open Standard
                ┌─────────────────────────────────┐
                │  Specification (agentskills.io)  │
                │  ─ Portable Skill definition     │
                │  ─ Progressive discovery         │
                │  ─ Cross-platform compatibility   │
                └──────────────┬──────────────────┘
                               │
           ┌──────────┬────────┼────────┬──────────┐
           ▼          ▼        ▼        ▼          ▼
       Claude Code  Cursor  VS Code   Goose       Amp
       / Cowork             / GitHub
                            Copilot
```

**The 17 Reference Skills 17 個參考 Skills**:
The `anthropics/skills` repo ships 17 production-quality Skills spanning creative, technical, and enterprise domains — from `docx`, `pdf`, `pptx`, `xlsx` (document generation) to `skill-creator` (meta-skill for building new Skills), `frontend-design`, `web-artifacts-builder`, and `mcp-builder`.

`anthropics/skills` repo 提供 17 個生產品質的 Skills，橫跨創意、技術和企業領域——從 `docx`、`pdf`、`pptx`、`xlsx`（文件生成）到 `skill-creator`（建構新 Skills 的元技能）、`frontend-design`、`web-artifacts-builder` 和 `mcp-builder`。

**Key Innovation: Progressive Discovery 關鍵創新：漸進式發現**:
Skills load in token-efficient tiers — name only → name + description → full definition. The LLM decides which Skills to fully load based on task relevance, avoiding context window bloat.

Skills 以節省 token 的分層方式載入——僅名稱→名稱 + 描述→完整定義。LLM 根據任務相關性決定完整載入哪些 Skills，避免 context window 膨脹。

**Strengths 優勢**:
- Industry-backed open standard with multi-vendor adoption 由產業支持的開放標準，多廠商採用
- 122K+ stars — the largest Skill-based repo in existence 122K+ stars——現存最大的 Skill-based repo
- Proven progressive discovery mechanism for token efficiency 經過驗證的漸進式發現機制，提升 token 效率
- Practical, installable, battle-tested Skills 實用、可安裝、經過實戰驗證的 Skills

**Limitations 局限**:
- **Zero theory** — no conceptual framework explaining *why* Skills work or what they mean architecturally **零理論**——沒有概念框架解釋*為什麼* Skills 有效或它們在架構上代表什麼
- No five-layer model, no paradigm-shift narrative, no learning path 沒有五層模型、沒有典範轉移敘事、沒有學習路徑
- Focused exclusively on installable artifacts — the "what to install," not the "what to understand" 專注於可安裝的產物——「裝什麼」，而非「理解什麼」
- Engineer audience only — no pathway for non-technical users 僅工程師受眾——沒有為非技術使用者設計的路徑

---

## 2. The Landscape Map ── 地貌總圖

Plotting each framework across two axes: **Abstraction Level** (how theoretical vs. practical) and **Scope** (how much of the full stack it covers):

用兩個軸繪製每個框架的位置：**抽象層級**（多理論 vs 多實務）和**涵蓋範圍**（覆蓋完整堆疊的程度）：

```
                        Abstraction Level 抽象層級
                        (Theoretical 理論)
                              ↑
                              │
                   AIOS       │
                   ●          │        ★ Agentic Substrate
                              │          (Ours 我們的)
                              │
          Andrew Ng ●         │
                              │
                              │
       Skills vs MCP ●       │      ● Anthropic
                              │        "Building Effective
                              │         Agents"
                              │
              SKILL.md ●      │
                              │          ● Superpowers
                              │
                              │     ● Agent Skills
                              │       Open Standard
         ──────────────────────┼──────────────────────→
         Narrow 狹窄           │                    Full Stack 全堆疊
         (Single Layer)        │                    (All Layers)
                              │
                        (Practical 實務)
```

**Key Observation 關鍵觀察**: There is a gap in the **upper-right quadrant** — a framework that is both **theoretically grounded** (explains the paradigm shift) and **full-stack** (covers all layers from LLM computation to user interface). That's where Agentic Substrate sits.

**關鍵觀察**：在**右上象限**存在一個空缺——一個既有**理論基礎**（解釋典範轉移）又是**全堆疊**（涵蓋從 LLM 運算到使用者介面的所有層）的框架。那就是 Agentic Substrate 的位置。

---

## 3. What Makes Agentic Substrate Different ── Agentic Substrate 的獨特之處

### Difference 1: "Computer Science Fundamentals" for the AI Era 差異一：AI 時代的「計算機概論」

Every other framework answers a **how** question:
其他每個框架都在回答**怎麼做**的問題：

- AIOS: *How* do you build an OS for agents? 如何為 Agent 建構 OS？
- Superpowers: *How* do you structure coding agent workflows? 如何結構化 coding agent 工作流程？
- SKILL.md: *How* do you format a portable Skill? 如何格式化一個可攜式 Skill？
- Agent Skills Open Standard: *What* should you install, and how do agents discover Skills? 該安裝什麼，Agent 如何發現 Skills？
- Andrew Ng: *What* patterns make agents effective? 什麼模式使 Agent 有效？
- Anthropic: *How* do you compose agent patterns in practice? 如何在實務中組合 Agent 模式？

Agentic Substrate answers a **what and why** question:
Agentic Substrate 回答的是**是什麼和為什麼**的問題：

> *What is the fundamental architecture of this new computing paradigm, why is it different from everything before, and how do I build a mental model to understand it?*
>
> *這個新運算典範的基礎架構是什麼、為什麼它與之前的一切不同、以及我如何建立心智模型來理解它？*

This is the difference between a **programming tutorial** and a **computer science textbook**. Both are valuable. But the textbook creates understanding that transfers across all future tools and frameworks.

這是**程式教學**和**計算機科學教科書**的差別。兩者都有價值。但教科書創造的理解可以轉移到所有未來的工具和框架。

### Difference 2: The Five-Layer Model as Unifying Theory 差異二：五層模型作為統一理論

No existing framework provides a complete layered model that maps the entire stack:

沒有任何現有框架提供一個映射完整堆疊的分層模型：

| Layer 層 | AIOS | Superpowers | SKILL.md | Agent Skills | Skills vs MCP | Ng | Anthropic | **Ours** |
|---|---|---|---|---|---|---|---|---|
| L1: LLM Computation 運算 | ✅ | — | — | — | — | — | ○ | **✅** |
| L2: Tools & Protocols 工具 | ✅ | ○ | — | ○ | ✅ | ○ | ✅ | **✅** |
| L3: Skills 技能 | — | ✅ | ✅ | ✅ | ✅ | — | ○ | **✅** |
| L4: Agents 代理 | ○ | — | — | ○ | — | ✅ | ✅ | **✅** |
| L5: Interface 介面 | — | — | — | — | — | — | — | **✅** |

✅ = Core focus 核心焦點 · ○ = Partially addressed 部分涉及 · — = Not covered 未涵蓋

### Difference 3: Non-Engineer Audience 差異三：非工程師受眾

| Framework 框架 | Target Audience 目標受眾 |
|---|---|
| AIOS | OS researchers, systems engineers OS 研究者、系統工程師 |
| Superpowers | Software developers using coding agents 使用 coding agent 的軟體開發者 |
| SKILL.md | Agent framework developers Agent 框架開發者 |
| Agent Skills Open Standard | Developers using Claude Code, Cursor, VS Code, and compatible agent platforms 使用 Claude Code、Cursor、VS Code 及相容 Agent 平台的開發者 |
| Skills vs MCP | DevOps / platform engineers DevOps / 平台工程師 |
| Andrew Ng | AI researchers and engineers AI 研究者和工程師 |
| Anthropic | Developers building with Claude API 用 Claude API 建構的開發者 |
| **Agentic Substrate** | **Practitioners of all technical levels — including non-engineers who use AI for knowledge work 所有技術水平的實踐者——包括使用 AI 進行知識工作的非工程師** |

The learning curriculum (Level 1→4) is designed so that someone who has only used ChatGPT for conversation can progressively build understanding up to designing their own Agent workflows.

學習課綱（Level 1→4）的設計讓一個只用 ChatGPT 聊過天的人，也能逐步建構理解，直到設計自己的 Agent 工作流程。

### Difference 4: Real-World Non-Engineering Evidence 差異四：真實的非工程場景實證

Superpowers' 121K stars prove Skills work for coding. But where's the evidence that Skills work for **knowledge work**?

Superpowers 的 121K stars 證明 Skills 對寫程式有效。但 Skills 對**知識工作**有效的證據在哪裡？

Agentic Substrate is grounded in 40+ real projects:

Agentic Substrate 基於 40 多個真實專案：

- **Proposal writing** 提案撰寫: A Process Skill that guides chapter-by-chapter authoring with per-chapter validation — like unit testing for documents 逐章引導撰寫，每章都有驗證——像文件的單元測試
- **Organization knowledge base** 組織知識庫: A Data Skill functioning as a lightweight, controlled RAG system for 40+ project records 作為輕量級受控 RAG 系統，管理 40+ 專案記錄
- **Document generation pipeline** 文件生成管線: Skills composing from Markdown chapters → formatted Word documents with auto-generated TOC Skill 從 Markdown 章節組合成含自動目錄的格式化 Word 文件
- **Project execution** 專案執行: An Orchestration Skill turning proposals into tracked, Git-based execution plans with agent handbooks 將提案轉化為可追蹤的 Git-based 執行計畫，含 Agent 工作手冊

This is evidence that the Skill paradigm works **beyond coding** — for proposals, reports, project management, and team coordination.

這是 Skill 典範**超越寫程式**有效的證據——適用於提案、報告、專案管理和團隊協作。

### Difference 5: Markdown as Universal Protocol 差異五：Markdown 作為通用協議

The Skills vs MCP discourse notes that Markdown skills are more token-efficient than MCP schemas. But it doesn't elevate this observation to a **design principle**.

Skills vs MCP 的論述指出 Markdown skills 比 MCP schemas 更省 token。但它沒有將這個觀察提升為**設計原則**。

Agentic Substrate explicitly defines:

Agentic Substrate 明確定義：

> **Markdown is the universal interchange protocol of the Agentic era** — the "JSON of AI."
>
> **Markdown 是代理型時代的通用交換協議**——「AI 的 JSON」。

This is because Markdown uniquely satisfies all requirements:

這是因為 Markdown 獨特地滿足所有需求：

| Requirement 需求 | JSON | SQL | Markdown | Natural Language |
|---|---|---|---|---|
| Human-readable 人類可讀 | ○ | ○ | ✅ | ✅ |
| LLM-native LLM 原生 | ○ | — | ✅ | ✅ |
| Structured 結構化 | ✅ | ✅ | ✅ | — |
| Versionable 可版控 | ✅ | ○ | ✅ | ○ |
| Composable 可組合 | ○ | — | ✅ | — |
| Non-technical friendly 非技術友好 | — | — | ✅ | ✅ |

No other format scores ✅ on all six dimensions. 沒有其他格式在六個維度上都得到 ✅。

### Difference 6: The Three-Track Transition Model 差異六：三軌過渡模型

Most discussions focus on one evolution track. Agentic Substrate maps **three parallel tracks** converging toward the same destination:

大多數討論聚焦在一條演化軌道。Agentic Substrate 映射**三條平行軌道**匯聚到同一目的地：

```
Cloud Track 雲端軌:    SaaS → SaaS+AI → AI-Native SaaS → Agent Services
Local Track 地端軌:    CLI → IDE+AI → Claude Code/Cowork → Full Agent Infra
Mobile Track 行動軌:   Apps+Siri → OS AI → AI-First Device → Edge Node

                    All converge → Agentic Substrate
                    全部匯聚 →     代理型基底
```

This three-track model explains why the transition feels chaotic — it's not one change, it's three simultaneous evolutions that will merge.

這個三軌模型解釋了為什麼轉型感覺混亂——這不是一個變化，而是三個同時發生的演化，最終將會合併。

---

## 4. What We Build Upon ── 我們建構在什麼之上

Agentic Substrate doesn't replace these frameworks — it **integrates and contextualizes** them:

Agentic Substrate 不取代這些框架——它**整合和賦予它們脈絡**：

| From 來自 | We Adopt 我們採用 |
|---|---|
| **AIOS** | The insight that LLM needs OS-level primitives (scheduling, memory, context management) LLM 需要 OS 層級原語的洞見 |
| **Superpowers** | The proof that Markdown-based composable Skills work at scale Markdown-based 可組合 Skills 大規模有效的證明 |
| **SKILL.md** | The push toward standardized, portable Skill definitions 推動標準化、可攜式 Skill 定義 |
| **Agent Skills Open Standard** | The industry-backed specification for Skill portability, progressive discovery mechanism, and the 17 reference Skills as validation of the Skill paradigm 產業支持的 Skill 可攜規格、漸進式發現機制，以及 17 個參考 Skills 作為 Skill 典範的驗證 |
| **Skills vs MCP** | The three-layer complementary model (Skills + MCP + Tools) 三層互補模型 |
| **Andrew Ng** | The four foundational design patterns as shared vocabulary 四種基礎設計模式作為共同詞彙 |
| **Anthropic** | The "simplicity first" philosophy and compositional patterns 「簡單優先」哲學和組合模式 |

What we **add** is the connective tissue — the unified theory, the five-layer model, the learning path, the non-engineering evidence, and the paradigm-shift narrative that ties it all together.

我們**添加**的是結締組織——統一理論、五層模型、學習路徑、非工程場景實證，以及將這一切綁在一起的典範轉移敘事。

**A note on Agent Skills Open Standard 關於 Agent Skills 開放標準的說明**: The relationship between Agentic Substrate and `anthropics/skills` is perhaps the clearest illustration of our positioning. Their repo has 122K+ stars and 17 high-quality installable Skills — but zero pages explaining *why* Skills are the new unit of software, *how* they compose dynamically, or *what* the architectural shift means. We are the **"why"**; they are the **"what to install."** Together, they form a complete picture: Agentic Substrate provides the conceptual understanding, and Agent Skills provides the production artifacts.

Agentic Substrate 和 `anthropics/skills` 之間的關係，也許是我們定位最清楚的說明。他們的 repo 有 122K+ stars 和 17 個高品質的可安裝 Skills——但沒有任何一頁解釋*為什麼* Skills 是新的軟體單元、它們*如何*動態組合、或這個架構轉移*意味著什麼*。我們是**「為什麼」**；他們是**「裝什麼」**。兩者結合形成完整的圖景：Agentic Substrate 提供概念理解，Agent Skills 提供生產產物。

---

## 5. A Note on Timing ── 關於時機的說明

The fact that this landscape is forming *right now* — in 2025-2026 — is itself significant:

這個地貌*此刻*正在形成——在 2025-2026 年——這本身就很重要：

- Anthropic launched MCP (Model Context Protocol) as the tool-access standard — adopted industry-wide Anthropic 推出 MCP 作為工具存取標準——全產業採用
- Anthropic launched the Agent Skills Open Standard (Oct 2025 concept → Dec 2025 open spec) — adopted by OpenAI, Microsoft, Cursor Anthropic 推出 Agent Skills 開放標準（2025/10 概念 → 2025/12 開放規格）——被 OpenAI、Microsoft、Cursor 採用
- `anthropics/skills` reached 122K+ stars — making it the largest Skills repo on GitHub `anthropics/skills` 達到 122K+ stars——成為 GitHub 上最大的 Skills repo
- Superpowers went from 0 to 121K stars in 5 months (late 2025 → early 2026) Superpowers 在 5 個月內從 0 到 121K stars
- The "Skills vs MCP" debate emerged in early 2026 「Skills vs MCP」辯論在 2026 年初浮現
- AIOS was published at COLM 2025 AIOS 在 COLM 2025 發表
- Anthropic's Agent SDK launched in 2025 Anthropic 的 Agent SDK 在 2025 年推出

We are at the **inflection point** where the Agentic paradigm is shifting from "interesting experiment" to "dominant architecture." The frameworks that define how people *think about* this shift — not just how they *implement* it — will shape the next decade of software.

我們正處於**轉折點**，代理型典範正從「有趣的實驗」轉變為「主導架構」。定義人們如何*思考*這個轉變——而不只是如何*實作*它——的框架，將塑造軟體的下一個十年。

That's the gap Agentic Substrate aims to fill.

那就是 Agentic Substrate 要填補的空缺。

---

## References 參考資料

1. Mei, K., Li, Z., et al. ["AIOS: LLM Agent Operating System"](https://arxiv.org/abs/2403.16971) — COLM 2025
2. Vincent, J. (obra). [Superpowers Framework](https://github.com/obra/superpowers) — GitHub, 2026
3. Community. ["The SKILL.md Format: A Standard for Portable AI Agent Capabilities"](https://dev.to/zacvibecodez/the-skillmd-format-a-standard-for-portable-ai-agent-capabilities-1mf5) — DEV Community, 2025
4. Simons, J. ["The Case for Running AI Agents on Markdown Files Instead of MCP Servers"](https://thenewstack.io/skills-vs-mcp-agent-architecture/) — The New Stack, 2026
5. Andrew Ng. ["Agentic Design Patterns"](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/) — DeepLearning.AI, 2024
6. Anthropic. ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) — 2024
7. Liu, J., et al. ["Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"](https://arxiv.org/abs/2604.14228) — arXiv, 2025
8. Skillmatic AI. [awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills) — GitHub, 2026
9. Anthropic. [Agent Skills Open Standard](https://github.com/anthropics/skills) — GitHub, 2025
10. Anthropic. [Agent Skills Specification](https://agentskills.io) — agentskills.io, 2025

---

*Previous: [The Agentic Substrate: Core Architecture ←](../01-foundations/agentic-substrate.md)*
*Next: [Agentic Design Patterns →](agentic-design-patterns.md)*
