---
name: research-and-summarize
description: >
  Structured research process that gathers, evaluates, and synthesizes information into a sourced summary with confidence levels and gap disclosure.
  Use when the user asks to "research [topic]", "I need a summary of [topic]", "help me understand [topic]",
  "compare [X] and [Y]", "I need a briefing for a meeting", or needs to make a decision and lacks domain knowledge.
metadata:
  version: "0.2.0"
  type: "Process"
  domain: "Research / Analysis"
---

# Research and Summarize
# 研究與摘要

> *From a vague question to a clear, sourced answer — fast.*
> *從模糊的問題到清楚、有來源的答案——快速。*

---

## Identity 身份

- **Name**: research-and-summarize
- **Type**: Process (information gathering → synthesis → structured output)
- **For**: Anyone who needs to research a topic and produce a summary — strategists preparing for decisions, students learning new subjects, managers needing background on a new domain, or anyone facing the "I need to understand X by tomorrow" situation.
- **對象**: 任何需要研究某個主題並產出摘要的人——策略師為決策準備、學生學習新科目、主管需要了解新領域的背景，或任何面對「我明天之前需要搞懂 X」情境的人。

---

## Description 描述

Research is not just "find information." It's a structured process of defining what you need to know, gathering sources, evaluating their reliability, synthesizing findings, and presenting them in a format the reader can act on. Most people skip straight from "Google it" to "here's what I found" — missing the critical steps of evaluation and synthesis.

研究不只是「找資料」。它是一個結構化的過程：定義你需要知道什麼、收集來源、評估其可靠性、綜合發現、以讀者能據以行動的格式呈現。大多數人直接從「Google 一下」跳到「這是我找到的」——跳過了評估和綜合的關鍵步驟。

This Skill structures the research process and produces a summary that's not just a collection of facts, but a synthesized answer with sourcing, confidence levels, and identified gaps.

這個 Skill 結構化研究過程，產出的摘要不只是事實的集合，而是有來源、信心水準和已辨識缺口的綜合答案。

---

## Trigger Conditions 觸發條件

- "Research [topic] for me" / 「幫我研究 [主題]」
- "I need a summary of [topic]" / 「我需要 [主題] 的摘要」
- "What's the current state of [topic]?" / 「[主題] 目前的狀況是什麼？」
- "Help me understand [topic]" / 「幫我理解 [主題]」
- "I need a briefing on [topic] for a meeting" / 「我需要 [主題] 的簡報給開會用」
- "Compare [X] and [Y]" / 「比較 [X] 和 [Y]」
- User needs to make a decision and lacks domain knowledge
  使用者需要做決策但缺乏領域知識

---

## Process Logic 流程邏輯

1. **Clarify the research question** — before starting, make sure you understand:
   **澄清研究問題**——開始之前，確認你了解：
   - What specifically does the user want to know? 使用者具體想知道什麼？
   - What's the purpose? (Decision-making, learning, reporting, other) 目的是什麼？
   - How deep? (Quick overview, moderate depth, comprehensive) 要多深？
   - Any specific angle or constraint? 有特定角度或限制嗎？

2. **Define the scope** — break the question into sub-questions:
   **定義範圍**——把問題拆成子問題：
   - What are the key dimensions of this topic? 這個主題的關鍵面向是什麼？
   - What's the user's knowledge level? (Don't explain what they already know) 使用者的知識水準？
   - What time frame is relevant? 相關的時間範圍？

3. **Gather information** from available sources:
   **收集資訊**：
   - Existing knowledge (training data within reliability window) 既有知識
   - Web search (current information) 網路搜尋（當前資訊）
   - User-provided documents or data 使用者提供的文件或資料
   - Domain-specific sources as relevant 相關的領域特定來源

4. **Evaluate sources** — for each piece of information, assess:
   **評估來源**——每條資訊都要評估：
   - Reliability: How credible is this source? 可靠性
   - Recency: Is this current or potentially outdated? 時效性
   - Relevance: Does this directly address the question? 相關性
   - Consensus: Do multiple sources agree? 共識：多個來源一致嗎？

5. **Synthesize** — don't just list facts; connect them:
   **綜合**——不只列出事實；要連結它們：
   - What's the overall picture? 整體圖像是什麼？
   - Where do sources agree and disagree? 來源哪裡一致、哪裡分歧？
   - What patterns or trends emerge? 浮現什麼模式或趨勢？
   - What's the answer to the user's original question? 使用者原始問題的答案是什麼？

6. **Identify gaps and caveats** — be honest about what you don't know:
   **辨識缺口和注意事項**——誠實說出你不知道的：
   - What information was unavailable? 什麼資訊無法取得？
   - What might have changed since sources were published? 來源發布後什麼可能已經改變？
   - Where is the evidence weak or conflicting? 哪裡的證據薄弱或矛盾？

7. **Generate structured output** in the format below.
   **生成結構化輸出**。

---

## I/O Contract 輸入輸出合約

### Input 輸入
- Research question or topic (text) 研究問題或主題
- Optional: purpose, depth, specific angles, related documents
  可選：目的、深度、特定角度、相關文件

### Output 輸出

```markdown
# Research Summary: [Topic]
# 研究摘要：[主題]

## Key Findings 關鍵發現
[3-5 bullet points — the most important things to know]

## Background 背景
[Context the reader needs to understand the findings]

## Detailed Analysis 詳細分析
### [Sub-topic 1]
[Findings with source attribution]

### [Sub-topic 2]
[Findings with source attribution]

## Comparison Table 比較表 (if applicable)
| Dimension 面向 | [Option A] | [Option B] | [Option C] |
|---|---|---|---|
| [criterion] | [finding] | [finding] | [finding] |

## Gaps & Caveats 缺口與注意事項
- [What's unknown or uncertain]
- [Where evidence is conflicting]
- [What might have changed]

## Recommendation 建議 (if requested)
[Based on the research, here's what the evidence suggests...]

## Sources 來源
- [Source 1 with link if available]
- [Source 2]
```

---

## Validation Rules 驗證規則

1. **The research question is answered** — the summary directly addresses what the user asked, not tangential information. 研究問題被回答了。
2. **Sources are attributed** — claims are traceable to their origin. 來源有標註。
3. **Confidence levels are honest** — don't present uncertain information as definitive. 信心水準誠實。
4. **Gaps are disclosed** — what you couldn't find is as important as what you found. 缺口有揭露。
5. **Depth matches request** — a "quick overview" shouldn't be 5000 words; a "comprehensive analysis" shouldn't be 3 paragraphs. 深度符合要求。
6. **Synthesis, not just collection** — the output tells a coherent story, not just a list of facts from different sources. 是綜合，不只是收集。

---

## Knowledge 知識庫

### Research Quality Hierarchy 研究品質層級
- **Level 1**: Recitation — repeating information from a single source (weakest) 複述——重複單一來源
- **Level 2**: Aggregation — combining information from multiple sources 彙整——合併多個來源
- **Level 3**: Synthesis — connecting information to produce new insight (target) 綜合——連結資訊產出新洞見
- **Level 4**: Analysis — evaluating evidence and forming supported conclusions (strongest) 分析——評估證據並形成有支撐的結論

### Common Research Pitfalls 常見研究陷阱
- **Confirmation bias** 確認偏誤: Only finding sources that support the expected answer
- **Recency bias** 近期偏誤: Overweighting the newest information
- **Authority bias** 權威偏誤: Trusting a source because of who said it, not the evidence
- **Scope creep** 範圍蔓延: Researching tangentially related topics until the core question is buried

---

## Composition Hooks 組合接口

- **Upstream** 上游: Meeting notes (research on topics raised), project requirements, user questions
- **Downstream** 下游: document-reviewer (review the summary), content-pipeline (research feeds content creation), presentation generation
- **Pairs with** 搭配: Any decision-making or strategy Skill

---

*Part of the [Agentic Substrate](../../../README.md) Example Skills Gallery.*
