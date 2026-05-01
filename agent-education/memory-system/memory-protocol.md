# Memory Protocol
### Agent 記憶操作協議

Purpose: define how an agent reads, writes, retrieves, and maintains persistent memory using a Git repository as the storage layer.

目的：定義 Agent 如何使用 Git repo 作為儲存層，來讀取、寫入、檢索和維護持久記憶。

This file reframes the human-facing [Memory & State](../../docs/02-architecture/memory-and-state.md) into an agent-facing operational protocol.

這份文件把給人讀的「記憶與狀態」文件，轉成 Agent 可執行的操作協議。

---

## Core Principle - 核心原則

```
Git repo = Agent 的長期記憶體
Markdown = 記憶的格式
Git commit = 記憶的版本
RAG / Index = 記憶的檢索層
```

The repo IS the memory. Do not build a separate memory database. Use structured Markdown files with Git versioning, and an index layer for retrieval.

repo 就是記憶。不要另建記憶資料庫。用結構化的 Markdown 檔案配合 Git 版本控制，再加上索引層來檢索。

---

## Usage - 使用方式

Run this protocol at two points:

在兩個時間點執行這個協議：

1. **Session start** — Read memory before acting.
   工作階段開始 — 行動前讀取記憶。
2. **Session end** — Write memory after completing work.
   工作階段結束 — 完成工作後寫入記憶。

```yaml
session_start:
  action: read_memory
  files: [memory-index, soul, daily]

session_end:
  action: write_memory
  files: [daily, decisions, session-log]
  commit: true
  push: false  # push is a separate decision
```

---

## Memory Types - 記憶類型

| Type 類型 | What 說明 | Format 格式 | Lifespan 壽命 | Example 範例 |
|---|---|---|---|---|
| Identity 身份 | Who the agent is, how it behaves | `SOUL.md` | Rarely changes | Agent 角色、原則、風格 |
| State 狀態 | Current project snapshot | `DAILY.md` | Updated every session | 進度、阻擋、下一步 |
| Decision 決策 | Why a choice was made | `decisions/NNN-topic.md` | Permanent | 技術選型、設計決策 |
| Session 工作紀錄 | What happened in a session | `sessions/YYYY-MM-DD-topic.md` | Permanent but rarely read | 工作摘要、產出紀錄 |
| Skill Reference | Which skills exist and relate | `skill-index.md` | Auto-generated | Skill 元資料、關聯圖 |
| Fact 事實 | Durable facts about the project/domain | `facts/category.md` | Permanent | API endpoints, conventions |

---

## Directory Structure - 目錄結構

```
project-repo/
│
├── SOUL.md                          ← Identity (read once per session)
│
├── DAILY.md                         ← State snapshot (read every session)
│
├── memory/                          ← All memory files
│   ├── memory-index.md              ← Routing table (read first)
│   ├── decisions/                   ← Decision records
│   │   ├── 001-vendor-selection.md
│   │   └── 002-architecture.md
│   ├── sessions/                    ← Session logs
│   │   ├── 2026-05-01-setup.md
│   │   └── 2026-05-02-feature.md
│   ├── facts/                       ← Durable facts
│   │   ├── project.md               ← Project metadata
│   │   ├── environment.md           ← Tech stack, configs
│   │   └── conventions.md           ← Coding/naming conventions
│   └── templates/                   ← Reusable templates
│       ├── session-log.md
│       └── decision-record.md
│
├── skill-index.md                   ← Auto-generated skill map
│
├── skills/                          ← Existing skill definitions
│   └── ...
│
└── agent-education/                 ← Agent protocols
    └── memory-system/
        └── memory-protocol.md       ← This file
```

---

## Session Start Protocol - 工作階段開始協議

```yaml
phase: session_start
steps:
  1_read_routing_table:
    file: memory/memory-index.md
    purpose: Know where to look for what
    tokens: ~200
  2_read_identity:
    file: SOUL.md
    purpose: Load agent identity and operating principles
    tokens: ~300-500
  3_read_state:
    file: DAILY.md
    purpose: Understand current project state, blockers, next actions
    tokens: ~200-400
  4_check_relevance:
    query: What is the current task?
    action: |
      If the task relates to a past decision → read decisions/
      If the task involves a specific Skill → read that SKILL.md
      If the task needs project facts → read facts/
      Otherwise → proceed to execution
total_startup_tokens: ~700-1100
```

Key rule: **Read the minimum needed to act correctly.** Do not load everything.

關鍵規則：**讀取正確行動所需的最少資訊。** 不要載入全部。

---

## Session End Protocol - 工作階段結束協議

```yaml
phase: session_end
trigger: Task complete or session about to end
steps:
  1_update_state:
    file: DAILY.md
    when: Always
    content:
      - What was completed (✅)
      - What is in progress (🔄)
      - What is blocked (🚫)
      - Next actions
      - Updated timestamp

  2_write_session_log:
    file: memory/sessions/YYYY-MM-DD-topic.md
    when: Non-trivial work was done
    content:
      - Session goal
      - What was done
      - Key decisions made
      - Files changed
      - Unresolved issues

  3_write_decision:
    file: memory/decisions/NNN-topic.md
    when: A significant decision was made
    content:
      - Context (why this decision was needed)
      - Options considered
      - Decision made
      - Rationale
      - Status (decided / revisiting / superseded)

  4_write_fact:
    file: memory/facts/category.md
    when: A new durable fact was discovered
    content:
      - The fact (declarative, not procedural)
      - Source/context
      - Confidence level

  5_commit:
    action: git add + git commit
    message: "memory: [brief description of what was updated]"
    when: Any memory file was changed

  6_update_index:
    file: memory/memory-index.md
    when: New files were added or structure changed
```

---

## Decision to Write - 什麼該寫、什麼不該寫

This is the most important judgment call an agent makes with memory.

這是 Agent 在記憶方面最重要的判斷。

### WRITE 該寫

| Signal 信號 | Example 範例 |
|---|---|
| User corrects you 使用者糾正你 | "Don't use that library, use X instead" |
| A significant decision was made 做了重大決定 | "We chose PostgreSQL over SQLite" |
| A durable fact was discovered 發現持久事實 | "The API endpoint is always /v2/" |
| A blocker emerged or was resolved 阻塞出現或解除 | "Client hasn't approved D3 yet" |
| A repeated workflow was identified 識別出重複工作流 | "Every Friday we do status reports" |
| Project state changed 專案狀態改變 | "Phase 2 is now complete" |

### DO NOT WRITE 不該寫

| Signal 信號 | Why Not 為什麼不 |
|---|---|
| Temporary task progress 臨時任務進度 | Use TODO/issue tracking, not memory |
| Conversation context 對話脈絡 | Volatile by nature, use session files |
| Tool output that was already processed 已處理的工具輸出 | The output matters, not the raw data |
| Obvious/derivable facts 顯而易見的事實 | Don't memorize what you can compute |
| Opinions without evidence 無根據的意見 | Memory is for facts and decisions |

### The Declarative Test - 宣示性測試

Before writing, ask: **"Is this a fact that will be true in 30 days?"**

寫之前問：**「這是一個 30 天後仍然為真的事實嗎？」**

- ✅ "We use React 18 with TypeScript" → declarative fact
- ✅ "We chose Vite over Webpack because..." → decision with rationale
- ❌ "I'm currently working on the login page" → temporary state (use DAILY.md)
- ❌ "The build failed because of a typo" → ephemeral

---

## Memory and Skills Connection - 記憶與 Skill 的關聯

Memory and Skills are two sides of the same coin:

記憶和 Skill 是一體兩面：

```
Memory = What happened (episodic) + What is true (semantic)
記憶 = 發生了什麼（情節性）+ 什麼是真實的（語義性）

Skills = How to do it (procedural)
Skill = 怎麼做（程序性）
```

Connection points:

關聯點：

1. **Skill discovery through memory**: When the agent detects a repeated workflow in session logs, it should trigger the [Skill Creation Protocol](../skill-system/skill-creation-protocol.md).

   **透過記憶發現 Skill**：當 Agent 在工作紀錄中偵測到重複工作流，應觸發 Skill 建立協議。

2. **Memory informs Skill selection**: Before executing a task, check memory for past decisions about which Skill or pattern to use.

   **記憶影響 Skill 選擇**：執行任務前，查記憶中過去關於使用哪個 Skill 或模式的決定。

3. **Skills generate memory**: Every Skill execution that produces a non-trivial result should write a session log entry.

   **Skill 產生記憶**：每次 Skill 執行產生非平凡結果時，應寫入工作紀錄。

4. **Skill index as memory**: The `skill-index.md` is itself a form of memory — it tells the agent what capabilities exist.

   **Skill 索引即記憶**：`skill-index.md` 本身就是一種記憶——它告訴 Agent 存在哪些能力。

---

## Retrieval Strategy - 檢索策略

Three levels of retrieval, from cheapest to most expensive:

三層檢索，從最便宜到最昂貴：

### Level 1: Index Lookup（~200 tokens）

Read `memory/memory-index.md` to find the right file.

讀取 `memory/memory-index.md` 找到對的檔案。

### Level 2: File Read（~200-2000 tokens）

Read the specific file identified by the index.

讀取索引指向的具體檔案。

### Level 3: Search（~500-5000 tokens）

When index lookup is insufficient, search across memory files:

當索引查找不足時，搜尋記憶檔案：

```bash
# Search for a topic across memory files
grep -r "keyword" memory/

# Search for decisions about a specific topic
grep -l "PostgreSQL" memory/decisions/

# Search session logs for a date range
ls memory/sessions/2026-04-*
```

### RAG Layer (Future) - RAG 層（未來）

For large repos (100+ memory files), consider:

對於大型 repo（100+ 記憶檔案），考慮：

1. **Vector index**: Embed all memory files, retrieve by semantic similarity
2. **SQL index**: Structured queries over frontmatter metadata
3. **Hybrid**: Vector for recall, SQL for precision

The Git repo remains the source of truth. RAG is a cache, not the primary store.

Git repo 仍然是真相來源。RAG 是快取，不是主要儲存。

---

## Anti-Patterns - 反模式

| Anti-pattern 反模式 | Symptom 症狀 | Correction 修正 |
|---|---|---|
| Memory hoarding 記憶囤積 | Every interaction becomes a memory entry | Apply the "30-day test" |
| Memory starvation 記憶飢餓 | Agent never writes, re-learns every session | Enforce session-end protocol |
| Monolithic memory 單體記憶 | One giant file for everything | One concern per file |
| Memory without index 無索引記憶 | Files exist but agent can't find them | Maintain memory-index.md |
| Stale memory 過時記憶 | Files contradict current reality | Update or archive outdated entries |
| Premature RAG 過早 RAG | Complex indexing for <50 files | Use grep + index until scale demands more |

---

## Integration With Existing Protocols - 與既有協議整合

```yaml
# Memory protocol connects to all other protocols

on_session_start:
  - read: memory-protocol (this file)
  - read: five-layer-self-model → identify current layer
  - read: memory/memory-index → route to relevant memory
  - read: SOUL.md → load identity
  - read: DAILY.md → load state

on_task_execution:
  - check: memory for past decisions about this task type
  - check: skill-index for existing Skills
  - use: pattern-matrix to select execution pattern
  - use: tool-result-validation to validate outputs

on_session_end:
  - write: DAILY.md (state update)
  - write: session log (if non-trivial work)
  - write: decision record (if significant decision)
  - write: fact (if new durable knowledge)
  - check: should this become a Skill? (skill-creation-protocol)
  - commit: all memory changes
```

---

## Minimal Memory Contract - 最小記憶契約

If the agent does nothing else with memory, it must:

如果 Agent 在記憶方面只做一件事，它必須：

1. **Read DAILY.md at session start** — to know the current state
   工作階段開始時讀取 DAILY.md — 了解當前狀態
2. **Update DAILY.md at session end** — to preserve the state
   工作階段結束時更新 DAILY.md — 保存狀態

This two-step contract alone prevents the "amnesia problem" — the agent always knows where the project stands.

僅這兩步契約就能預防「失憶問題」——Agent 永遠知道專案的狀態。

---

## References - 參考

- Human-facing theory: [Memory & State](../../docs/02-architecture/memory-and-state.md)
- Five-layer model context: [Five-Layer Self-Model](../self-model/five-layer-self-model.md)
- Skill creation from memory: [Skill Creation Protocol](../skill-system/skill-creation-protocol.md)
- Pattern selection: [Pattern Matrix](../decision-patterns/pattern-matrix.md)
