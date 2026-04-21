---
name: project-status-tracker
description: >
  Gather data from multiple sources and produce a unified project status report with health indicators, risk management, and milestone tracking.
  Use when the user asks "what's the project status", "are we on track", "what's blocked",
  "generate the weekly status report", or needs to prepare for a status meeting.
metadata:
  version: "0.2.0"
  type: "Orchestration"
  domain: "Project Management"
---

# Project Status Tracker
# 專案狀態追蹤器

> *Ask "where are we?" and get a real answer — not a guess.*
> *問「我們到哪了？」然後得到真實的答案——不是猜測。*

---

## Identity 身份

- **Name**: project-status-tracker
- **Type**: Orchestration (coordinates data from multiple sources → unified view)
- **For**: Project managers, team leads, and anyone who needs to report on or understand the current state of a project with multiple moving parts.
- **對象**: 專案經理、團隊主管，以及任何需要報告或了解一個有多個進行中部分的專案現狀的人。

---

## Description 描述

"What's the status of the project?" is the most common question in any organization — and the hardest to answer well. The information is scattered: some in spreadsheets, some in chat messages, some in people's heads, some in documents that haven't been updated. This Skill provides a systematic way to gather, organize, and present project status.

「專案的進度怎麼樣了？」是任何組織中最常見的問題——也是最難回答好的。資訊是散落的：有些在試算表、有些在聊天訊息、有些在人的腦子裡、有些在還沒更新的文件中。這個 Skill 提供系統性的方法來收集、組織和呈現專案狀態。

It's an Orchestration Skill because it doesn't do one thing — it coordinates information from multiple inputs and produces a unified status view.

它是一個調度型 Skill，因為它不只做一件事——它協調多個輸入的資訊，產出統一的狀態視圖。

---

## Trigger Conditions 觸發條件

- "What's the project status?" / 「專案進度怎麼樣？」
- "Give me a status update on [project]" / 「給我 [專案] 的狀態更新」
- "I need to prepare for a status meeting" / 「我需要準備狀態會議」
- "Are we on track?" / 「我們在正軌上嗎？」
- "What's blocked?" / 「什麼被卡住了？」
- "Generate the weekly status report" / 「產出週報」
- User shares project data (task lists, timelines, meeting notes) and asks for synthesis
  使用者分享專案資料並要求綜合

---

## Process Logic 流程邏輯

1. **Identify the project scope** — understand what project we're tracking:
   **辨識專案範圍**：
   - What's the project name and objective? 專案名稱和目標？
   - What are the major workstreams or phases? 主要工作流或階段？
   - What's the overall timeline? 整體時程？
   - Who are the key stakeholders? 關鍵利害關係人？

2. **Gather status data** from available sources:
   **從可用來源收集狀態資料**：
   - Task lists or project plans (spreadsheets, Gantt charts, kanban boards)
     任務清單或專案計畫
   - Recent meeting notes or decisions 最近的會議紀錄或決策
   - Communications about progress or blockers 關於進度或阻礙的溝通
   - Budget or resource utilization data 預算或資源使用資料
   - KPI or metric data KPI 或指標資料

3. **Assess each workstream** using a consistent framework:
   **用一致的框架評估每個工作流**：

   For each workstream, determine:
   - **Status**: 🟢 On Track / 🟡 At Risk / 🔴 Blocked / ✅ Complete
   - **Progress**: % complete (based on milestones, not time elapsed)
   - **What was accomplished** since last update 上次更新以來完成了什麼
   - **What's coming next** 接下來什麼
   - **Risks or blockers** 風險或阻礙
   - **Needs** from leadership or other teams 需要上層或其他團隊的什麼

4. **Calculate overall project health**:
   **計算整體專案健康度**：
   - Timeline: Are we ahead, on time, or behind? 時程：超前、準時、落後？
   - Budget: Under, on, or over budget? 預算：低於、等於、超過？
   - Scope: Any scope changes since baseline? 範圍：基準以來有變更嗎？
   - Quality: Any quality concerns raised? 品質：有品質問題被提出嗎？
   - Team: Any resource or capacity issues? 團隊：有資源或產能問題嗎？

5. **Identify the top 3 risks** and their mitigation status.
   **辨識前 3 大風險**和它們的緩解狀態。

6. **Generate structured output**.
   **生成結構化輸出**。

7. **Highlight what needs attention** — don't bury critical issues in the middle of a long report. Lead with what matters.
   **突顯需要注意的事項**——不要把關鍵問題埋在長報告中間。

---

## I/O Contract 輸入輸出合約

### Input 輸入
- Project information: plan, task list, timeline, or description
  專案資訊：計畫、任務清單、時程或描述
- Status data: what's been done, what's in progress, what's blocked
  狀態資料：完成了什麼、進行中什麼、卡住什麼
- Optional: previous status reports, meeting notes, budget data
  可選：之前的狀態報告、會議紀錄、預算資料

### Output 輸出

```markdown
# Project Status: [Project Name]
# 專案狀態：[專案名稱]
**Report Date**: [date] | **Period**: [date range]

## Executive Summary 摘要
[2-3 sentences: overall health, key achievement, biggest concern]

## Overall Health 整體健康度
| Dimension 面向 | Status 狀態 | Notes 備註 |
|---|---|---|
| Timeline 時程 | 🟢/🟡/🔴 | [detail] |
| Budget 預算 | 🟢/🟡/🔴 | [detail] |
| Scope 範圍 | 🟢/🟡/🔴 | [detail] |
| Quality 品質 | 🟢/🟡/🔴 | [detail] |
| Team 團隊 | 🟢/🟡/🔴 | [detail] |

## Workstream Status 工作流狀態
### [Workstream 1]
- **Status**: 🟢 On Track
- **Progress**: [X]% complete
- **Accomplished**: [what was done]
- **Next**: [what's coming]
- **Risks**: [if any]

### [Workstream 2]
[same structure]

## Top Risks 前 3 大風險
| # | Risk 風險 | Impact 影響 | Likelihood 可能性 | Mitigation 緩解 | Owner 負責人 |
|---|---|---|---|---|---|
| 1 | [risk] | High/Med/Low | High/Med/Low | [plan] | [person] |

## Decisions Needed 需要的決策
- [Decision 1 — who needs to decide, by when]

## Key Milestones 關鍵里程碑
| Milestone 里程碑 | Planned 計畫 | Actual 實際 | Status 狀態 |
|---|---|---|---|
| [milestone] | [date] | [date or —] | ✅/🔄/⬜ |

## Next Period Focus 下一期重點
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

---

## Validation Rules 驗證規則

1. **Status is evidence-based** — every 🟢/🟡/🔴 is supported by data, not optimism. 狀態有證據支持。
2. **No surprises buried** — if something is 🔴, it appears in the executive summary, not just in a workstream detail. 嚴重問題不被埋沒。
3. **Progress is milestone-based** — "50% of time elapsed" ≠ "50% complete." Track against deliverables, not calendar. 進度以里程碑為基準。
4. **Risks have owners** — a risk without an owner is just a worry, not a managed risk. 風險有負責人。
5. **Decisions needed are explicit** — if the project needs a decision from leadership, say so clearly with a deadline. 需要的決策要明確。
6. **Consistent with previous reports** — if last report said 🟢 and this one says 🔴, explain what changed. 與先前報告一致。

---

## Knowledge 知識庫

### The "Watermelon Project" Anti-Pattern 「西瓜專案」反模式
Projects that are green on the outside (reported as on-track) but red on the inside (actually struggling). This Skill fights this by requiring evidence for every status indicator, not just self-reporting.

表面綠色（報告正軌）內部紅色（實際掙扎）的專案。這個 Skill 藉由要求每個狀態指標都有證據來對抗這種情況。

### Status Assessment Heuristics 狀態評估啟發法
- **🟢 On Track**: Progress matches or exceeds plan; no unmitigated risks; team capacity adequate
- **🟡 At Risk**: Minor delay or emerging risk; recoverable with action; needs monitoring
- **🔴 Blocked/Behind**: Significant delay or unresolved blocker; needs escalation or scope change

### What Makes a Good Status Report 好的狀態報告的特質
- **Honest** 誠實: Bad news delivered early is manageable; bad news delivered late is a crisis
- **Actionable** 可行動: Ends with clear next steps and decisions needed
- **Comparative** 比較: Shows change from last period, not just a snapshot
- **Audience-aware** 讀者意識: Executive summary for leadership, detail for the team

---

## Composition Hooks 組合接口

- **Upstream** 上游: meeting-notes-to-actions (action items feed task tracking), any data collection Skill
- **Downstream** 下游: Report generation Skills, presentation Skills, stakeholder communication
- **Pairs with** 搭配: research-and-summarize (research context for risks), document-reviewer (review before sending)

---

*Part of the [Agentic Substrate](../../../README.md) Example Skills Gallery.*
