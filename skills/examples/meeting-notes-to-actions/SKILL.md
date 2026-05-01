---
name: meeting-notes-to-actions
description: >
  Transform raw meeting notes or transcripts into structured decisions, action items with owners and deadlines, and open questions.
  Use when the user shares meeting notes, asks to "organize these meeting notes", "extract action items",
  "turn this into a meeting summary", or "what decisions came out of this meeting".
metadata:
  version: "0.2.0"
  type: "Transform"
  domain: "General / Productivity"
---

# Meeting Notes to Actions
# 會議紀錄轉行動項目

> *Every meeting produces decisions. This Skill makes sure none of them get lost.*
> *每場會議都產出決策。這個 Skill 確保沒有任何一個被遺失。*

---

## Identity 身份

- **Name**: meeting-notes-to-actions
- **Type**: Transform (unstructured notes → structured actions)
- **For**: Anyone who attends meetings and needs to track follow-ups — project managers, team leads, assistants, or anyone tired of "wait, who was supposed to do that?"
- **對象**: 任何參加會議且需要追蹤後續事項的人——專案經理、團隊主管、助理，或任何厭倦了「等等，那件事是誰要做的？」的人。

---

## Description 描述

You attend a meeting. Someone takes notes — messy, real-time, full of tangents and side conversations. The meeting ends. Now what? The critical decisions, action items, and deadlines are buried in paragraphs of discussion.

你參加了一場會議。有人做了筆記——凌亂的、即時的、充滿岔題和旁邊對話。會議結束了。然後呢？關鍵的決策、行動項目和截止日期都埋在一段段的討論中。

This Skill takes raw meeting notes (in any format — typed, voice transcription, bullet points, stream-of-consciousness) and produces a clean, actionable output: decisions made, action items with owners and deadlines, open questions, and a follow-up schedule.

這個 Skill 接收原始會議紀錄（任何格式——打字、語音轉文字、列點、意識流）並產出乾淨、可行動的輸出：已做的決策、有負責人和截止日的行動項目、未解問題，以及跟進時程。

---

## Trigger Conditions 觸發條件

- User shares meeting notes, transcript, or recording summary
  使用者分享會議紀錄、逐字稿或錄音摘要
- "Help me organize these meeting notes"
  「幫我整理這些會議紀錄」
- "What action items came out of this meeting?"
  「這場會議有什麼行動項目？」
- "Can you turn this into a meeting summary?"
  「你能把這個變成會議摘要嗎？」
- "Extract the decisions from this meeting"
  「從這場會議提取決策」

---

## Process Logic 流程邏輯

1. **Receive and read** the raw meeting notes. Accept any format — don't ask the user to clean them up first.
   **接收並閱讀**原始會議紀錄。接受任何格式——不要求使用者先整理。

2. **Identify participants** mentioned in the notes (by name, role, or pronoun reference).
   **辨識參與者**——筆記中提到的人（依姓名、角色或代名詞指涉）。

3. **Extract decisions** — statements where a choice was made. Look for phrases like "we decided," "let's go with," "agreed," "確定," "決定," "就這樣."
   **提取決策**——做出選擇的陳述。

4. **Extract action items** — tasks assigned to specific people. For each, identify:
   **提取行動項目**——指派給特定人的任務。每個都要辨識：
   - **What** 做什麼: the task itself
   - **Who** 誰做: the responsible person (if stated; mark "TBD" if unclear)
   - **When** 何時: deadline or timeframe (if stated; mark "TBD" if unclear)
   - **Context** 脈絡: why this action was decided (brief)

5. **Extract open questions** — things discussed but not resolved, needing further input or a future meeting.
   **提取未解問題**——討論了但未解決的事。

6. **Extract parking lot items** — topics raised but deliberately deferred ("let's discuss that next time").
   **提取暫擱項目**——提出但刻意延後的議題。

7. **Generate structured output** in the format below.
   **生成結構化輸出**。

8. **Ask for confirmation** — present the output and ask: "Did I miss anything? Are the owners and deadlines correct?"
   **要求確認**——呈現輸出並問：「我有漏掉什麼嗎？負責人和截止日正確嗎？」

---

## I/O Contract 輸入輸出合約

### Input 輸入
- Raw meeting notes (any format: text, markdown, transcript, bullet points)
  原始會議紀錄（任何格式）
- Optional: meeting date, attendee list, meeting purpose
  可選：會議日期、出席者名單、會議目的

### Output 輸出

```markdown
# Meeting Summary: [Meeting Name/Date]
# 會議摘要：[會議名稱/日期]

## Attendees 出席者
[List of participants identified]

## Key Decisions 關鍵決策
| # | Decision 決策 | Rationale 理由 |
|---|---|---|
| 1 | [decision] | [why] |

## Action Items 行動項目
| # | Task 任務 | Owner 負責人 | Deadline 截止日 | Context 脈絡 |
|---|---|---|---|---|
| 1 | [task] | [person] | [date] | [why] |

## Open Questions 未解問題
- [Question 1 — what needs to be resolved, and by whom]
- [Question 2]

## Parking Lot 暫擱項目
- [Topic deferred to future discussion]

## Next Steps 下一步
- Next meeting: [date/time if mentioned]
- Follow-up needed by: [date]
```

---

## Validation Rules 驗證規則

1. **Every action item has an owner** — even if the owner is "TBD (to be assigned by [person])." No orphaned tasks.
   每個行動項目都有負責人——即使是「待指派」。
2. **Decisions are distinguished from discussions** — something discussed but not concluded is an open question, not a decision.
   決策和討論要區分——討論了但沒結論的是未解問題，不是決策。
3. **No invented information** — if a deadline wasn't mentioned, mark it "TBD," don't guess.
   不捏造資訊——如果沒提到截止日，標記「待定」，不要猜。
4. **User's terminology preserved** — use the same project names, abbreviations, and terms from the notes.
   保留使用者的用語。
5. **Completeness check** — every substantive topic in the notes appears in at least one section of the output.
   完整性檢查——筆記中每個實質議題都出現在至少一個輸出段落中。

---

## Knowledge 知識庫

### Patterns That Signal Action Items 代表行動項目的模式
- "[Name] will..." / 「[人名]會...」
- "Let's have [name] handle..." / 「讓[人名]處理...」
- "We need someone to..." / 「我們需要有人...」
- "By [date], we should..." / 「在[日期]前，我們應該...」
- "Action: ..." / 「行動：...」
- Verbs: prepare, send, check, review, create, schedule, follow up / 準備、寄、檢查、審查、建立、排程、跟進

### Patterns That Signal Decisions 代表決策的模式
- "We agreed..." / 「我們同意...」
- "Decision: ..." / 「決定：...」
- "Let's go with option [X]" / 「我們選方案[X]」
- "Final answer is..." / 「最終答案是...」
- Unanimous or majority agreement language

### Common Edge Cases 常見邊界案例
- **Implicit actions**: "We should update the website" (who? when?) → Flag as action with TBD owner
- **Conditional decisions**: "If the budget is approved, then we'll..." → Mark as conditional
- **Verbal agreements vs. formal decisions**: In some cultures/organizations, a verbal "sounds good" is binding; in others it's not. When in doubt, include it as a decision with a note.

---

## Composition Hooks 組合接口

- **Upstream** 上游: Voice transcription tools, note-taking apps, calendar events
- **Downstream** 下游: project-status-tracker (action items feed into project tracking), task management systems (Asana, Jira, Notion)
- **Pairs with** 搭配: Any Process Skill that begins with "receive assignment" — this Skill creates those assignments

---

## Related

- [[skill-builder]] — Create new Skills using the guided Skill Builder process
- [[project-status-tracker]] — Action items feed into project tracking

*Part of the [Agentic Substrate](../../../README.md) Example Skills Gallery.*
