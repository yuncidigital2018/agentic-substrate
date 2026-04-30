# From Workflow to Skill
# 從工作流程到 Skill

> *A concrete example of how everyday professional knowledge becomes an executable AI workflow.*
> *一個具體範例：日常專業知識如何變成 AI 可執行的工作流程。*

---

## The Everyday Workflow ── 日常工作流程

A project manager prepares a weekly status update every Friday.

一位專案經理每週五要整理專案週報。

They usually do this:

通常流程是：

1. Collect notes from meetings, chat, task boards, and email.
2. Identify what changed since last week.
3. Separate completed work, blocked items, risks, and next actions.
4. Check whether each action has an owner and due date.
5. Write a concise update for stakeholders.
6. Flag decisions that need approval.

換成中文：

1. 收集會議紀錄、聊天訊息、任務看板與 email。
2. 找出和上週相比有哪些變化。
3. 分成已完成事項、卡住事項、風險與下一步行動。
4. 檢查每個行動是否有負責人與期限。
5. 寫成給利害關係人的簡潔週報。
6. 標出需要決策或核准的事項。

This is not "just experience." It is already a workflow specification.

這不是「只是經驗」。它其實已經是一份工作流程規格。

---

## The Same Knowledge as a Skill ── 同一份知識變成 Skill

```markdown
# Weekly Status Synthesizer

## Description
Use this Skill when the user provides project notes, task updates,
meeting notes, or chat history and asks for a weekly status update.

## Inputs
- Raw project notes
- Last week's status update, if available
- Current milestone or delivery target
- Known stakeholder audience

## Process
1. Read all source notes and identify dated events.
2. Compare with last week's known state.
3. Group findings into:
   - completed work
   - in-progress work
   - blockers
   - risks
   - decisions needed
   - next actions
4. For each action, check for owner and due date.
5. Produce a stakeholder-ready status update.
6. Add a short internal QA checklist.

## Validation
- Every blocker has an owner or an explicit "owner missing" marker.
- Every next action has an owner and due date, or is flagged incomplete.
- Risks are separated from current blockers.
- The final update is concise enough to send without heavy editing.

## Output
- Executive summary
- Status by workstream
- Blockers and risks
- Decisions needed
- Next actions table
- QA checklist
```

---

## Why This Matters ── 為什麼這重要

The project manager did not learn programming. They simply described how good work is done.

這位專案經理沒有學程式設計。他只是把「好工作是怎麼完成的」描述出來。

That is the central idea of Agentic Substrate:

這就是 Agentic Substrate 的核心：

> Domain experts are not only AI users.
> They are builders of the Skill layer.

> 領域專家不只是 AI 使用者。
> 他們是 Skill 層的建構者。

---

## Try It ── 你可以試試看

Take one task you repeat every week and answer seven questions:

拿一件你每週都會重複做的任務，回答七個問題：

1. What is this task responsible for?
2. When should it start?
3. What inputs does it need?
4. What steps do you follow?
5. What should the output look like?
6. How do you know the output is correct?
7. What happens before and after this task?

If you can answer these, you already have the skeleton of a Skill.

如果你能回答這些，你就已經有一個 Skill 的骨架。

