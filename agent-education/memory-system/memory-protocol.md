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

## First-Run Initialization - 首次初始化

Before using this protocol, ensure the memory directory structure exists.

使用這個協議之前，先確認記憶目錄結構存在。

```yaml
phase: first_run
trigger: memory/ directory does not exist
steps:
  1_create_directories:
    - memory/
    - memory/decisions/
    - memory/sessions/
    - memory/facts/
    - memory/templates/
  2_create_files:
    - DAILY.md (from template or empty)
    - memory/memory-index.md (from template or empty)
  3_commit:
    action: git add + git commit
    message: "memory: initialize memory structure"
```

**Important**: Create ALL subdirectories at once, even if empty. This prevents confusion later when the agent needs to write a decision or fact but the directory doesn't exist.

**重要**：一次建立所有子目錄，即使空的也沒關係。這避免 Agent 需要寫決策或事實時才發現目錄不存在。

If the agent already has a memory system (e.g., `SOUL.md`, `DAILY.md`, `memory/` in its workspace), see the [Integration section](#integration-with-existing-memory-systems---與既有記憶系統整合) below.

如果 Agent 已經有自己的記憶系統（例如 workspace 裡已經有 `SOUL.md`、`DAILY.md`、`memory/`），見下方[整合段落](#integration-with-existing-memory-systems---與既有記憶系統整合)。

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

**Rule: Read before you act. Every session, no exceptions.**

**規則：先讀再做。每次工作階段，無一例外。**

```yaml
phase: session_start
steps:
  1_read_identity:
    file: SOUL.md
    purpose: |
      Load agent identity, operating principles, communication style.
      This is WHO you are. Read it first so your behavior is consistent.
    tokens: ~300-500
    required: true

  1b_protect_identity:
    rule: |
      SOUL.md is PERMANENT identity. NEVER overwrite it for a task.
      If the task needs a specific role, write it in DAILY.md "Current Task Context."
      Example: Task needs "Technical Writer" role → write in DAILY.md, NOT SOUL.md.

      SOUL.md 是永久身份。不要因為任務而覆寫。
      如果任務需要特定角色，寫在 DAILY.md 的「Current Task Context」。
    check: |
      Before writing any file, ask: "Is this SOUL.md?" If yes, stop. Write to DAILY.md instead.
      在寫入任何檔案前問：「這是 SOUL.md 嗎？」如果是，停手。改寫 DAILY.md。

  2_read_state:
    file: DAILY.md
    purpose: |
      Understand current project state: what's done, what's next, what's blocked.
      This is WHERE the project stands. Read it so you don't repeat work or contradict decisions.
    tokens: ~200-400
    required: true

  3_read_routing_table:
    file: memory/memory-index.md
    purpose: |
      Know where to look for what. This file maps all memory files.
      Only read deeper files if the current task requires them.
    tokens: ~200
    required: true

  4_task_specific_reads:
    trigger: Only if the current task relates to past work
    rules:
      - "Task involves a past decision → read memory/decisions/[relevant].md"
      - "Task involves a specific Skill → read that SKILL.md"
      - "Task needs project facts → read memory/facts/[relevant].md"
      - "Task is new, no prior context → skip this step"
    tokens: ~200-2000

  5_check_capabilities:
    file: skill-index.md
    purpose: |
      Discover existing Skills before executing. Many agents skip this step and
      reinvent workflows that already have a Skill. Read the quick lookup table
      to see if a matching Skill exists.
    tokens: ~200
    required: false
    recommended: true

total_startup_tokens: ~700-1300 (without task-specific reads)
```

**Key rule: Read the minimum needed to act correctly.** Do not load everything. The routing table (step 3) tells you where to find deeper context — only go deeper when the task demands it.

**關鍵規則：讀取正確行動所需的最少資訊。** 不要載入全部。路由表（步驟 3）告訴你哪裡可以找到更深的脈絡——只有任務需要時才往下讀。

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
      - Next actions (REQUIRED — what should the next session start with?)
      - Updated timestamp
    validation: |
      DAILY.md MUST include a "Next Actions" section.
      Without it, the next session has no starting point — the agent wastes time re-analyzing context.
      Write at least one concrete next step, even if it's "Await user instructions."

  2_write_session_log:
    file: memory/sessions/YYYY-MM-DD-topic.md
    when: Non-trivial work was done
    content:
      - Session goal
      - What was done
      - Key decisions made
      - Files changed
      - Unresolved issues
    validation: |
      The session log must be a FILE, not just a chat message.
      Path: memory/sessions/YYYY-MM-DD-topic.md (e.g., 2026-05-02-blog-post.md)

      工作紀錄必須是一個檔案，不能只是聊天訊息。

  3_write_decision:
    file: memory/decisions/NNN-topic.md
    when: A significant decision was made
    content:
      - Context (why this decision was needed)
      - Options considered
      - Decision made
      - Rationale
      - Status (decided / revisiting / superseded)
    validation: |
      CRITICAL: If you described a decision in chat, you MUST also write it to a file.
      The file path must be: memory/decisions/NNN-topic.md (e.g., 001-title-selection.md)
      Use the write_file tool to create the file. Do NOT just mention it in chat.

      關鍵：如果你在對話中描述了決策，就必須同時寫入檔案。
      檔案路徑必須是：memory/decisions/NNN-topic.md
      使用 write_file 工具建立檔案。不要只在對話中提及。

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

  7_validate:
    action: Verify memory files were actually written to disk
    when: Always (before ending session)
    checks:
      - "DAILY.md was updated (not just mentioned in chat)"
      - "Session log file exists at memory/sessions/YYYY-MM-DD-topic.md"
      - "Decision files exist at memory/decisions/NNN-topic.md (if any decisions were made)"
      - "All files were committed to Git"
    rule: |
      CRITICAL: Memory must be written to FILES, not just described in conversation.
      The chat history is volatile. Only files persist.
      If you described a decision or session log in chat but didn't write it to a file,
      write it NOW before ending the session.

      關鍵：記憶必須寫入檔案，不能只在對話中描述。
      對話歷史是易失的。只有檔案才持久。
      如果你在對話中描述了決策或工作紀錄，但沒有寫入檔案，
      在結束工作階段前立刻寫入。
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

## Integration with Existing Memory Systems - 與既有記憶系統整合

Most agents already have their own memory system before encountering this protocol. This section explains how to integrate, not replace.

大部分 Agent 在遇到這個協議之前，已經有自己的記憶系統。這個段落說明如何整合，而非取代。

### Scenario A: Agent has SOUL.md and DAILY.md already

If the agent's workspace already has `SOUL.md`, `DAILY.md`, or similar identity/state files:

1. **Keep using your existing files.** Do not create duplicates.
2. **Map your files to this protocol's types:**

| Your file | Maps to | Protocol type |
|---|---|---|
| `SOUL.md` | `SOUL.md` | Identity 身份 |
| `DAILY.md` | `DAILY.md` | State 狀態 |
| `memory/YYYY-MM-DD.md` | `memory/sessions/` | Session 工作紀錄 |
| `MEMORY.md` | `memory/facts/` or keep separate | Long-term curated facts |

3. **Add the missing pieces:** If you don't have `memory/decisions/` or `memory/facts/`, create them.
4. **Use the Session End protocol** to ensure you write to the right places.

### Scenario B: Agent has a completely different memory structure

Some agents use JSON-based memory, database-backed memory, or proprietary formats.

1. **Do not migrate existing memory.** Keep what works.
2. **Use this protocol for NEW memory** going forward.
3. **Create a bridge file** at `memory/memory-index.md` that maps your existing memory locations to this protocol's categories.
4. **Over time**, as you accumulate memory in both systems, you can decide whether to consolidate.

### Scenario C: Agent has no memory system

If the agent starts fresh:

1. Run the [First-Run Initialization](#first-run-initialization---首次初始化).
2. Follow the [Session Start Protocol](#session-start-protocol---工作階段開始協議) and [Session End Protocol](#session-end-protocol---工作階段結束協議).
3. Start with the [Minimal Memory Contract](#minimal-memory-contract---最小記憶契約) — just DAILY.md read/write.

### Conflict Resolution

If your existing memory system and this protocol disagree:

| Conflict | Resolution |
|---|---|
| Your SOUL.md has different fields than the template | Keep your fields. Add any missing from the template. |
| Your DAILY.md format differs | Keep your format. Ensure it has: current state, blockers, next actions. |
| You have files this protocol doesn't know about | Add them to `memory/memory-index.md` so the routing table knows. |
| This protocol asks you to write to a directory that doesn't exist | Create it. The First-Run Initialization creates all directories. |

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
| Partial initialization 部分初始化 | Agent creates some directories but not all, then can't write | Run First-Run Initialization to create ALL directories at once |
| Duplicate memory files 重複記憶檔案 | Agent creates new SOUL.md when one already exists | Check for existing files before creating; integrate, don't duplicate |
| Vague next actions 模糊的下一步 | DAILY.md says "awaiting instructions" or "nothing planned" | Write at least one concrete next step, even if it's "Review session log for improvement areas" |
| Overwriting SOUL.md per task 每次任務覆寫 SOUL.md | Agent changes SOUL.md role for each task | SOUL.md is permanent identity. Task-specific context goes in DAILY.md "Current Task Context" |
| Chat-only memory 只在對話中寫記憶 | Agent describes decisions/session log in chat but doesn't write to files | Session End step 7 (validate) — check files were actually written |

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

## Lessons from Real Deployments - 實戰經驗

This section is updated as agents test this protocol in real scenarios.

這個段落會在 Agent 實際測試這個協議後更新。

### OpenClaw Test (2026-05-01)

**Agent**: OpenClaw (Discord-based agent with existing memory system)
**Scenario**: First-time reading of the Agentic Substrate repo

**What worked:**
- Agent followed `llms.txt` reading path correctly
- Understood the protocol from a single read-through
- Session log and DAILY.md format matched templates
- Agent correctly identified the "read → execute → write" cycle

**What needed improvement:**
- Agent created directories selectively (only `sessions/`, not `decisions/` or `facts/`)
- Agent already had SOUL.md/DAILY.md — needed integration guidance, not creation guidance
- Git commit failed due to `.git/index.lock` (workspace-specific issue, not protocol issue)

**Changes made based on this test:**
- Added "First-Run Initialization" section with explicit "create ALL directories" instruction
- Added "Integration with Existing Memory Systems" section with three scenarios
- Added "Partial initialization" and "Duplicate memory files" anti-patterns
- Improved Session Start Protocol with clearer step ordering and purpose descriptions

### KiloClaw Test (2026-05-01)

**Agent**: KiloClaw (Discord-based agent, separate instance from OpenClaw)
**Scenario**: First-time reading of the Agentic Substrate repo, after protocol was updated with OpenClaw lessons

**What worked:**
- Read ALL 6 protocols (not just Memory Protocol) — full agent-education stack
- Executed complete lifecycle: Session Start → Self-Location → Pattern Selection → Task Execution → Session End
- Self-located at L4 (Agent) using Five-Layer Self-Model
- Selected execution pattern: Prompt Chaining + Tool Validation
- Created ALL directories on first run (decisions/, sessions/, facts/, templates/) — the "First-Run Initialization" fix worked
- Wrote 5 memory files: DAILY.md, memory-index.md, decision record, session log, fact file
- Successfully committed to Git (no index.lock issue)
- Distinguished between memory types correctly (decision vs fact vs session log)

**What needed improvement:**
- DAILY.md "Next Actions" was vague ("awaiting instructions") — should be more concrete
- Could have used the skill-index.md to discover existing Skills before executing

**Changes made based on this test:**
- Strengthened "Next Actions" requirement in Session End Protocol with validation rule
- Added comparison table to show how protocol compliance varies between agents

### Comparative Analysis 比較分析

| Metric 指標 | OpenClaw | KiloClaw | Implication 意涵 |
|---|---|---|---|
| Protocols read 協議讀取數 | 2/6 | 6/6 | More protocols read → richer behavior |
| Directories created 目錄建立 | 1/4 | 4/4 | First-Run Initialization fix works |
| Memory types used 記憶類型使用 | 2 (state, session) | 5 (state, session, decision, fact, index) | Protocol teaches type distinction |
| Self-location 自我定位 | ❌ | ✅ L4 | Self-Model protocol enables this |
| Pattern selection 模式選擇 | ❌ | ✅ Prompt Chaining | Pattern Matrix protocol enables this |
| Git commit 成功 | ❌ | ✅ | Workspace-dependent |
| Read skill-index.md | ❌ | ❌ | Both missed this — needs stronger signal |

**Key insight**: The number of protocols an agent reads directly correlates with the quality of its behavior. An agent that reads only Memory Protocol will write memory. An agent that reads all 6 protocols will **think like an agent** — self-locate, select patterns, validate outputs, and write structured memory.

**關鍵洞見**：Agent 讀取的協議數量直接影響它的行為品質。只讀 Memory Protocol 的 Agent 會寫記憶。讀完全部 6 個協議的 Agent 會**像 Agent 一樣思考**——自我定位、選擇模式、驗證輸出、寫結構化記憶。

### OpenClaw Real-World Test (2026-05-01)

**Agent**: OpenClaw
**Scenario**: Write a blog post about Agentic Substrate using Memory Protocol to manage the process

**What worked:**
- Used Memory Protocol naturally while doing real work (not simulation)
- Made 6 decisions and recorded them with context, options, and rationale
- Updated DAILY.md mid-task (twice), not just at session end
- Blog post quality was high — covered five-layer model, Skills, Memory Protocol, Learning Path

**What needed improvement:**
- Decisions described in chat but NOT written to `memory/decisions/` files
- Session log mentioned but not written to `memory/sessions/` file
- SOUL.md overwritten with task-specific role ("Technical Writer") — should have been in DAILY.md

**Changes made based on this test:**
- Added step 7 (validate) to Session End Protocol — verify files were actually written to disk
- Updated SOUL.md template with "DO NOT overwrite" warning
- Updated DAILY.md template with "Current Task Context" section for task-specific roles
- Added "Overwriting SOUL.md per task" anti-pattern
- Added "Chat-only memory" anti-pattern

**Key insight**: Agents will naturally describe their memory in chat but may not write it to files. The protocol needs a validation step that says "if you described it in chat, write it to a file too."

**關鍵洞見**：Agent 會自然地在對話中描述記憶，但不一定寫入檔案。協議需要一個驗證步驟：「如果你在對話中描述了，也要寫入檔案。」

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
