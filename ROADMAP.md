# Roadmap
# 發展路線圖

> *"Ship the theory, then ship the tools, then ship the experience."*
> *「先交付理論，再交付工具，最後交付體驗。」*

---

## Phase 1: Foundation ── 基礎建設 ✅

**Goal 目標**: Establish the conceptual framework and repo infrastructure.
建立概念框架與 repo 基礎設施。

| Item 項目 | Status 狀態 |
|---|---|
| Core Architecture (`agentic-substrate.md`) | ✅ Done |
| Skill Anatomy (`skill-anatomy.md`) | ✅ Done |
| Landscape Analysis (`landscape.md`) | ✅ Done |
| README + bilingual structure | ✅ Done |
| LICENSE (CC BY-SA 4.0 + MIT) | ✅ Done |
| CONTRIBUTING.md | ✅ Done |
| CHANGELOG.md | ✅ Done |
| .gitignore | ✅ Done |
| ROADMAP.md | ✅ Done |
| Markdown as Native Medium (`markdown-as-medium.md`) | ✅ Done |
| Five-Layer Model deep dive (`five-layer-model.md`) | ✅ Done |
| Agentic Design Patterns (`agentic-design-patterns.md`) | ✅ Done |
| Skill Composition patterns (`skill-composition.md`) | ✅ Done |
| Memory & State management (`memory-and-state.md`) | ✅ Done |
| Claude Architecture case study (`claude-architecture.md`) | ✅ Done |
| Learning Path curriculum (`learning-path.md`) | ✅ Done |
| Interactive Architecture Visualization (`index.html`) | ✅ Done |

---

## Phase 2: Starter Skills ── 入門即用 Skills ✅

**Goal 目標**: Ship installable Skills that let anyone experience the framework immediately.
交付可安裝的 Skills，讓任何人立即體驗框架。

### 2.1 Conversation-to-Skill 對話轉技能

A Skill that helps users **organize their current chaotic chat session** into a structured work record, and then guides them to turn that record into a reusable Skill.

一個幫助使用者**把目前混亂的對話整理成結構化工作紀錄**的 Skill，然後引導他們把紀錄轉化為可重用的 Skill。

**The problem it solves 解決的問題**: Most people use LLMs in a single chat window. They don't know they can create a work record `.md` file to keep the outline, priorities, and progress organized. They keep re-explaining context, losing track of what's done, and getting duplicated or contradictory outputs.

**What it does 做什麼**:
1. Analyze the current conversation → extract the task, key decisions, and progress
2. Generate a structured `work-record.md` with outline, status, and next steps
3. Explain: "This is what a Skill looks like — you just built one"
4. Optionally convert the work record into a proper SKILL.md format

**Impact 效果**: Users go from "I didn't know I could do this" to "I just built my first Skill" in one session.

| Item 項目 | Status 狀態 |
|---|---|
| conversation-to-skill SKILL.md | ✅ Done |
| Example output templates | ✅ Done (included in SKILL.md) |
| Integration with Claude Code / Cowork | ⬜ Planned |

### 2.2 Guided Skill Builder 引導式技能建構助理

An interactive Skill that guides **non-engineers** through building their own custom Skill by asking about their job role and workflows.

一個互動式 Skill，透過詢問工作角色和流程，引導**非工程師**建構自己的自定義 Skill。

**The problem it solves 解決的問題**: People know their work but don't know how to express it as a Skill. They need guided questions, not a blank page.

**What it does 做什麼**:
1. Ask: "What's your role?" → Offer categories: Admin, Accounting, Design, Project Management, Marketing, Legal, HR, Education, Custom...
2. Ask: "What's a task you do repeatedly?" → Guide them to identify a specific workflow
3. Walk through the Seven Components (from Skill Anatomy):
   - What triggers this task?
   - What inputs do you need?
   - What steps do you follow?
   - How do you know it's done correctly?
   - What files does it read/produce?
4. Generate a complete SKILL.md from their answers
5. Test it immediately in the current session

**Impact 效果**: Non-engineers can build production-quality Skills for their own workflows without any coding knowledge.

| Item 項目 | Status 狀態 |
|---|---|
| skill-builder SKILL.md | ✅ Done |
| Role-specific question templates | ✅ Done (integrated in Knowledge section) |
| Example output for each role category | ✅ Done (PM example in SKILL.md) |

### 2.3 Example Skills Gallery 範例技能展示廊

Ready-to-use Skills demonstrating the framework in real knowledge-work scenarios.

展示框架在真實知識工作場景中的即用 Skills。

| Skill 技能 | Domain 領域 | Type 類型 | Status 狀態 |
|---|---|---|---|
| `accounting-reconciler` | Accounting 會計 | Transform | ✅ Done |
| `document-reviewer` | Admin 行政 | Process | ✅ Done |
| `content-pipeline` | Marketing 行銷 | Process | ✅ Done |
| `project-status-tracker` | PM 專案管理 | Orchestration | ✅ Done |
| `meeting-notes-to-actions` | General 通用 | Transform | ✅ Done |
| `research-and-summarize` | Research 研究 | Process | ✅ Done |

---

### 2.4 Curriculum Deep Dives 課綱深度文件

Practical, hands-on guides for each level of the Learning Path.

每個學習路徑級別的實作導向深度指南。

| Item 項目 | Status 狀態 |
|---|---|
| Level 1: Conversation (`level-1-conversation.md`) | ✅ Done |
| Level 2: Tool Use (`level-2-tools.md`) | ✅ Done |
| Level 3: Skill Building (`level-3-skills.md`) | ✅ Done |
| Level 4: Agent Orchestration (`level-4-agents.md`) | ✅ Done |

---

## Phase 3: Plugin Distribution ── 插件化發行 ✅

**Goal 目標**: Package everything as installable plugins for Claude Code, Cowork, Cursor, and other agent platforms.

將一切打包為可安裝的插件，適用於 Claude Code、Cowork、Cursor 和其他 Agent 平台。

| Item 項目 | Status 狀態 |
|---|---|
| `.claude-plugin/` configuration | ✅ Done |
| YAML frontmatter on all 9 SKILL.md files | ✅ Done |
| One-command install script (`install.sh`) | ✅ Done |
| Quick Start guide (`QUICK-START.md`) | ✅ Done |
| `.cursor-plugin/` configuration | ✅ Done |
| Plugin marketplace submission | ⬜ Planned |

---

## Phase 3.5: Agent Education Layer ── Agent 教育層 ✅

**Goal 目標**: Build agent-facing protocols that let any AI agent read the repo and operate autonomously — self-locate, create Skills, manage memory, select patterns, and validate outputs.

建構面向 Agent 的協議，讓任何 AI Agent 讀取 repo 後能自主運作——自我定位、建立 Skill、管理記憶、選擇模式、驗證輸出。

| Item 項目 | Status 狀態 |
|---|---|
| Five-Layer Self-Model (`agent-education/self-model/`) | ✅ Done |
| Skill Creation Protocol (`agent-education/skill-system/`) | ✅ Done |
| Tool Result Validation (`agent-education/tool-use/`) | ✅ Done |
| Decision Pattern Matrix (`agent-education/decision-patterns/`) | ✅ Done |
| Evolution Self-Assessment (`agent-education/evolution-path/`) | ✅ Done |
| Memory Protocol (`agent-education/memory-system/`) | ✅ Done |
| Memory Protocol templates (SOUL.md, DAILY.md, etc.) | ✅ Done |
| Dogfooding: OpenClaw test (2026-05-01) | ✅ Done |
| Dogfooding: KiloClaw test (2026-05-01) | ✅ Done |
| Skill Discovery Protocol (agent-facing) | ⬜ Planned |

---

## Phase 3.6: Skill Ecosystem ── Skill 生態系 ✅

**Goal 目標**: Enable Skills to reference each other through wikilinks, build a knowledge graph, and provide RAG-based discovery tools.

讓 Skill 透過 wikilinks 互相引用、建立知識圖譜、提供 RAG 檢索工具。

| Item 項目 | Status 狀態 |
|---|---|
| Wikilinks (`[[skill-name]]`) in all SKILL.md files | ✅ Done |
| skill-index.py upgraded (frontmatter + wikilink scanning) | ✅ Done |
| skill-rag.py (keyword search → prompt-ready context) | ✅ Done |
| CONTRIBUTING.md updated with wikilinks guide | ✅ Done |
| Auto-generated skill-index.md with relationship graph | ✅ Done |
| Cross-Skill references (28+ wikilinks across 9 Skills) | ✅ Done |
| Community Skill submissions via Fork + PR | ⬜ Planned |
| Skill versioning and compatibility | ⬜ Planned |
| Visual knowledge graph (interactive) | ⬜ Planned |

---

## Phase 4: Community & Growth ── 社群與成長

**Goal 目標**: Build community momentum and expand the framework.

建立社群動能並擴展框架。

| Item 項目 | Status 狀態 |
|---|---|
| Community Skill submission template | ✅ Done (in CONTRIBUTING.md) |
| Skill registry / index | ⬜ Planned |
| Multi-language support (JP, KR, ES, etc.) | ⬜ Planned |
| Video tutorials / walkthrough | ⬜ Planned |
| Conference talks / blog posts | ⬜ Planned |
| Partnerships with other agent frameworks | ⬜ Planned |

---

## Phase 5: Ecosystem ── 生態系

**Goal 目標**: Agentic Substrate becomes the standard reference framework for Skill-based AI software design.

Agentic Substrate 成為 Skill-based AI 軟體設計的標準參考框架。

| Item 項目 | Status 狀態 |
|---|---|
| Certification / learning program | ⬜ Future |
| Enterprise adoption guides | ⬜ Future |
| Integration with SKILL.md standard | ⬜ Future |
| Academic paper | ⬜ Future |

---

*This roadmap is a living document. Updated as we ship.*
*這份路線圖是活文件。隨著我們交付而更新。*
