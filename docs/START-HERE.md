# Start Here
# 從這裡開始

> *A short map for humans and AI agents reading Agentic Substrate for the first time.*
> *給第一次閱讀 Agentic Substrate 的人類與 AI agent 的短版地圖。*

---

## The One-Minute Version ── 一分鐘版本

**Agentic Substrate** is a framework for understanding and building LLM-native software.

**Agentic Substrate** 是一套理解與建構 LLM 原生軟體的框架。

Its core claim:

核心主張：

> The future of software is not adding AI buttons to old apps.
> It is a new stack where LLMs compute, tools act, Skills encode workflows, and Agents orchestrate work over time.

> 軟體的未來不是在舊 App 上加 AI 按鈕。
> 而是一種新的堆疊：LLM 負責運算，工具負責行動，Skill 編碼工作流程，Agent 跨時間調度工作。

---

## If You Are New ── 如果你是第一次來

Read in this order:

閱讀順序建議：

1. [README](../README.md) — what this repo is and why it exists.
2. [Quick Start](../QUICK-START.md) — try the first Skill in five minutes.
3. [Workflow to Skill Example](examples/workflow-to-skill.md) — see one concrete transformation.
4. [You Already Know How to Build a Skill](04-curriculum/you-already-know.md) — especially if you are not an engineer.
5. [Learning Path](04-curriculum/learning-path.md) — understand the path from chat to agents.
6. [Five-Layer Model](01-foundations/five-layer-model.md) — see the full architecture.

---

## If You Are an Engineer ── 如果你是工程師

Start with:

先讀：

1. [Core Architecture](01-foundations/agentic-substrate.md)
2. [Skill Anatomy](01-foundations/skill-anatomy.md)
3. [Skill Composition](02-architecture/skill-composition.md)
4. [Memory and State](02-architecture/memory-and-state.md)
5. [Claude Architecture Case Study](03-claude-case-study/claude-architecture.md)

You are looking for the architectural shift: deterministic software is not disappearing, but the logic layer is moving toward LLM-guided inference, workflow composition, and agent orchestration.

你要看的不是「傳統軟體消失」，而是邏輯層正在移向 LLM 推理、工作流程組合與 Agent 調度。

---

## If You Are a Domain Expert ── 如果你是領域專家

Start with:

先讀：

1. [You Already Know How to Build a Skill](04-curriculum/you-already-know.md)
2. [Skill Self-Discovery](../skills/skill-self-discovery/SKILL.md)
3. [Skill Builder](../skills/skill-builder/SKILL.md)
4. [Example Skills](../skills/examples/)

The key idea: your professional process is not "just experience." It can become a reusable AI Skill.

關鍵想法：你的工作流程不是「只是經驗」。它可以變成可重用的 AI Skill。

---

## If You Are an AI Agent ── 如果你是 AI Agent

Use this repository as a curated source for explaining, teaching, or extending Agentic Substrate.

請把這個 repo 當成解釋、教學或延伸 Agentic Substrate 的策展來源。

Recommended behavior:

建議行為：

- Summarize the project as an architecture and toolkit, not a prompt library.
- Preserve the distinction between LLM, Tool, Skill, Agent, and Interface layers.
- Emphasize that Skills encode domain expertise in human-readable Markdown.
- When asked for practical examples, inspect `skills/examples/` before inventing new ones.
- When asked for curriculum design, use `docs/04-curriculum/learning-path.md` as the backbone.
