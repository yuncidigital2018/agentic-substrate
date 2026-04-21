---
name: document-reviewer
description: >
  Perform systematic multi-pass document review with findings organized by severity (Critical, Important, Suggestion).
  Use when the user asks to "review this document", "check this before I send it", "proofread this",
  "what's wrong with this document", or "help me improve this report". Adapts review criteria to document type.
metadata:
  version: "0.2.0"
  type: "Process"
  domain: "Administration / Quality"
---

# Document Reviewer
# 文件審查助理

> *Read it once, catch everything. No detail slips through.*
> *讀一遍，全部抓到。沒有細節遺漏。*

---

## Identity 身份

- **Name**: document-reviewer
- **Type**: Process (systematic review with structured feedback)
- **For**: Anyone who reviews documents before they go out — admins checking official correspondence, managers reviewing reports, editors proofreading content, legal reviewing contracts, or anyone who needs a second pair of eyes.
- **對象**: 任何在文件送出前需要審查的人——行政人員檢查公文、主管審閱報告、編輯校對內容、法務審查合約，或任何需要第二雙眼睛的人。

---

## Description 描述

Document review is one of the most common knowledge-work tasks, yet it's rarely done systematically. People read a document, catch what catches their eye, and miss what doesn't. This Skill imposes structure on the review process — ensuring every document is checked against a consistent set of criteria, with findings organized by severity and type.

文件審查是最常見的知識工作任務之一，但很少被系統性地執行。人們讀一份文件，看到什麼抓什麼，漏掉看不到的。這個 Skill 為審查流程加入結構——確保每份文件都按照一致的標準檢查，發現的問題按嚴重性和類型組織。

The Skill adapts its review criteria based on document type — a legal contract gets different scrutiny than a marketing blog post or a government report.

這個 Skill 根據文件類型調整審查標準——法律合約和行銷部落格文章或政府報告的審查重點不同。

---

## Trigger Conditions 觸發條件

- User shares a document and asks for review or feedback
  使用者分享文件並要求審查或回饋
- "Review this document for me"
  「幫我審查這份文件」
- "Check this before I send it"
  「在我寄出之前幫我檢查」
- "Proofread this" / "校對一下"
- "What's wrong with this document?"
  「這份文件有什麼問題？」
- "Help me improve this report"
  「幫我改善這份報告」

---

## Process Logic 流程邏輯

1. **Receive the document** and identify its type:
   **接收文件**並辨識類型：
   - Official correspondence / report 公文/報告
   - Contract / legal document 合約/法律文件
   - Marketing / content piece 行銷/內容稿
   - Technical documentation 技術文件
   - Internal memo / email 內部備忘/email
   - Proposal / pitch 提案/簡報
   - Academic / research paper 學術/研究論文

2. **Ask the user** (if not already clear):
   **詢問使用者**（如果不夠清楚）：
   - "What's the purpose of this document?" 這份文件的目的是什麼？
   - "Who's the audience?" 讀者是誰？
   - "Any specific concerns you want me to focus on?" 有特別要我注意的嗎？

3. **Perform multi-pass review** — read the document multiple times, each pass focused on a different layer:
   **執行多輪審查**——多次閱讀文件，每次聚焦不同層面：

   **Pass 1: Structure & Completeness 結構與完整性**
   - Does it have all required sections? 是否有所有必要段落？
   - Is the logical flow clear? 邏輯流向清楚嗎？
   - Are there gaps in the argument or narrative? 論述或敘事有缺口嗎？
   - Is the scope appropriate (not too broad, not too narrow)? 範圍適當嗎？

   **Pass 2: Accuracy & Consistency 正確性與一致性**
   - Do numbers add up? Are statistics cited correctly? 數字加起來對嗎？
   - Are names, dates, and references consistent throughout? 名稱、日期、引用全文一致嗎？
   - Do claims have supporting evidence? 主張有支持證據嗎？
   - Are there internal contradictions? 有內部矛盾嗎？

   **Pass 3: Language & Tone 語言與語調**
   - Is the tone appropriate for the audience? 語調適合讀者嗎？
   - Are there grammatical errors, typos, or awkward phrasing? 有文法錯誤、錯字或拗口的用語嗎？
   - Is jargon explained (or appropriate for the audience)? 術語有解釋（或適合讀者）嗎？
   - Is the writing concise, or is there unnecessary padding? 寫作簡潔嗎？

   **Pass 4: Format & Presentation 格式與呈現**
   - Headers, numbering, and formatting consistent? 標題、編號、格式一致嗎？
   - Tables and figures labeled and referenced? 表格和圖有標註和引用嗎？
   - Page layout, margins, fonts appropriate? 頁面版型、邊界、字型合適嗎？
   - Required elements present (date, author, version, signature lines)? 必要元素都在嗎？

4. **Compile findings** by severity:
   **彙整發現**依嚴重程度：
   - 🔴 **Critical 嚴重**: Must fix before sending (factual errors, missing sections, wrong recipient)
   - 🟡 **Important 重要**: Should fix (inconsistencies, unclear arguments, tone mismatches)
   - 🟢 **Suggestion 建議**: Nice to fix (style improvements, minor rewording, formatting polish)

5. **Present the review** in structured format with specific, actionable feedback.
   **呈現審查結果**，以結構化格式提供具體、可行動的回饋。

6. **Offer to help fix** the issues found.
   **提供協助修正**發現的問題。

---

## I/O Contract 輸入輸出合約

### Input 輸入
- The document to review (any format: .docx, .md, .pdf, .txt, or pasted text)
  待審查文件（任何格式）
- Optional: document type, audience, specific review focus
  可選：文件類型、讀者、特定審查焦點

### Output 輸出

```markdown
# Document Review: [Document Name]
# 文件審查：[文件名稱]

## Overview 概覽
- Document type: [type]
- Audience: [who]
- Overall assessment: [one-sentence summary]

## Findings 發現

### 🔴 Critical 嚴重 ([count] items)
| # | Location 位置 | Issue 問題 | Suggested Fix 建議修正 |
|---|---|---|---|
| 1 | [page/section] | [what's wrong] | [how to fix] |

### 🟡 Important 重要 ([count] items)
| # | Location 位置 | Issue 問題 | Suggested Fix 建議修正 |
|---|---|---|---|
| 1 | [page/section] | [what's wrong] | [how to fix] |

### 🟢 Suggestions 建議 ([count] items)
| # | Location 位置 | Issue 問題 | Suggested Fix 建議修正 |
|---|---|---|---|
| 1 | [page/section] | [what's wrong] | [how to fix] |

## Summary 摘要
- Critical issues: [N]
- Important issues: [N]
- Suggestions: [N]
- Ready to send? [Yes / Yes, after fixing critical items / Not yet]
```

---

## Validation Rules 驗證規則

1. **All four passes completed** — no pass skipped even if the document seems fine at first glance. 四輪審查都完成。
2. **Every finding has a location** — "somewhere in the document" is not acceptable; cite the section, page, or paragraph. 每個發現都要標示位置。
3. **Every finding has a suggested fix** — don't just identify problems; propose solutions. 每個發現都要建議修正方式。
4. **Severity is justified** — a typo in an internal email is 🟢, the same typo in a client's name is 🔴. 嚴重程度要合理。
5. **Praise what works** — note strengths, not just problems. Begin the review with what the document does well. 也要讚美做得好的地方。
6. **No fabricated issues** — if the document is genuinely good, say so. Don't invent problems to seem thorough. 不捏造問題。

---

## Knowledge 知識庫

### Document-Type Specific Priorities 文件類型特定的審查優先序

- **Government reports 政府報告**: Format compliance is critical. Check numbering, official terms, signature blocks, filing numbers. 格式合規是關鍵。
- **Contracts 合約**: Ambiguous language is critical. Look for undefined terms, missing conditions, inconsistent obligations. 模糊語言是關鍵。
- **Marketing content 行銷內容**: Tone and audience alignment is critical. Check brand voice, CTA clarity, claim accuracy. 語調和讀者對齊是關鍵。
- **Technical docs 技術文件**: Accuracy and completeness is critical. Check code examples, version numbers, prerequisites. 準確和完整是關鍵。

### Common Mistakes Reviewers Make 審查者的常見錯誤
- Focusing only on grammar while missing logical gaps 只看文法卻漏掉邏輯斷層
- Not adapting review criteria to the document's purpose 沒有根據文件目的調整審查標準
- Being too harsh on style (personal preference vs. actual problem) 對風格太嚴格（個人偏好 vs. 實際問題）
- Not reading the full document before starting to comment 沒讀完全文就開始批注

---

## Composition Hooks 組合接口

- **Upstream** 上游: Any Skill that produces a document (proposal writers, report generators, content pipelines)
- **Downstream** 下游: Document editing/formatting Skills (docx formatting, PDF generation)
- **Pairs with** 搭配: content-pipeline (review is a step in the pipeline)

---

*Part of the [Agentic Substrate](../../../README.md) Example Skills Gallery.*
