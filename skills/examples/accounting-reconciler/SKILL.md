---
name: accounting-reconciler
description: >
  Systematically compare two sets of financial records, identify and categorize discrepancies, and produce a reconciliation report with recommended actions.
  Use when the user asks to "reconcile these accounts", "compare bank statement with ledger",
  "check budget vs actuals", "find discrepancies", "月結對帳", "核帳", or "對帳".
metadata:
  version: "0.2.0"
  type: "Transform"
  domain: "Accounting / Finance"
---

# Accounting Reconciler
# 帳務核對助理

> *Every number tells a story. This Skill makes sure the stories match.*
> *每個數字都在說一個故事。這個 Skill 確保故事吻合。*

---

## Identity 身份

- **Name**: accounting-reconciler
- **Type**: Transform (raw financial data → reconciliation report with discrepancies)
- **For**: Accountants, bookkeepers, finance assistants, and anyone responsible for verifying that two sets of financial records agree — bank statements vs. ledgers, invoices vs. payments, budgets vs. actuals.
- **對象**: 會計、帳務人員、財務助理，以及任何負責驗證兩組財務記錄是否一致的人——銀行對帳單 vs. 帳本、發票 vs. 付款、預算 vs. 實際。

---

## Description 描述

Reconciliation is the backbone of financial accuracy. It's the process of comparing two sets of records to ensure they match, identifying discrepancies, and resolving them. It's repetitive, detail-intensive, and error-prone when done manually — exactly the kind of work where a structured Skill shines.

核對是財務正確性的骨幹。它是比較兩組記錄確保吻合、辨識差異並解決的過程。人工執行時是重複的、細節密集的、容易出錯的——正是結構化 Skill 發揮的地方。

This Skill handles the systematic comparison, flags discrepancies, categorizes them by likely cause, and produces a clean reconciliation report that an accountant can review and act on.

這個 Skill 處理系統性的比較，標記差異，按可能原因分類，並產出乾淨的核對報告讓會計可以審閱和處理。

---

## Trigger Conditions 觸發條件

- User provides two sets of financial data to compare
  使用者提供兩組財務資料比較
- "Help me reconcile these accounts" / 「幫我核對這些帳目」
- "Compare the bank statement with our ledger" / 「比較銀行對帳單和我們的帳本」
- "Check budget vs. actuals" / 「對照預算和實際」
- "Find the discrepancies between these two reports" / 「找出這兩份報告的差異」
- "月結對帳" / "核帳" / "對帳"
- End of month / quarter / year reconciliation cycle
  月/季/年底核對週期

---

## Process Logic 流程邏輯

1. **Identify what's being reconciled** — understand the two data sets:
   **辨識核對標的**：
   - Data Set A: [source, format, period] 資料集 A
   - Data Set B: [source, format, period] 資料集 B
   - Reconciliation type: bank reconciliation, intercompany, budget-vs-actual, invoice matching, other
     核對類型：銀行對帳、公司間、預算 vs. 實際、發票配對、其他

2. **Standardize the data** — before comparing, ensure both sets use:
   **標準化資料**：
   - Same date format 相同日期格式
   - Same currency and decimal precision 相同貨幣和小數精度
   - Same account/category naming 相同帳戶/類別命名
   - Same period boundaries 相同期間界線

3. **Perform line-by-line matching** using multiple matching strategies:
   **逐行配對**使用多重配對策略：
   - **Exact match** 精確配對: Amount + date + reference number all match
   - **Amount match** 金額配對: Amounts match but dates or references differ (timing difference)
   - **Partial match** 部分配對: Reference matches but amount differs (partial payment or error)
   - **One-to-many** 一對多: One record in A matches multiple records in B (split transactions)
   - **Many-to-one** 多對一: Multiple records in A match one record in B (batch deposits)

4. **Categorize unmatched items** by likely cause:
   **將未配對項目按可能原因分類**：
   - **Timing differences** 時間差異: Transaction recorded in different periods (e.g., check issued Dec 31, cleared Jan 2)
   - **Missing entries** 遺漏登錄: Present in one set but absent in the other
   - **Amount differences** 金額差異: Same transaction, different amounts (possible error)
   - **Classification differences** 分類差異: Same transaction, different categories
   - **Duplicates** 重複: Same transaction recorded twice in one set

5. **Calculate summary statistics**:
   **計算摘要統計**：
   - Total in Data Set A / Total in Data Set B
   - Difference (absolute and percentage) 差異（絕對值和百分比）
   - Number of matched / unmatched items 配對/未配對項目數
   - Breakdown of unmatched by category 未配對項目按分類細分

6. **Generate reconciliation report**.
   **生成核對報告**。

7. **Flag items requiring action** — sorted by impact (largest discrepancies first).
   **標記需要行動的項目**——按影響排序（最大差異優先）。

---

## I/O Contract 輸入輸出合約

### Input 輸入
- Data Set A: Financial records (spreadsheet, CSV, or structured text)
  資料集 A：財務記錄
- Data Set B: Financial records to compare against
  資料集 B：比對用的財務記錄
- Optional: tolerance threshold (e.g., ignore differences under NT$10), matching rules, period
  可選：容差閾值、配對規則、期間

### Output 輸出

```markdown
# Reconciliation Report: [A] vs. [B]
# 核對報告：[A] vs. [B]
**Period**: [date range] | **Date**: [report date]

## Summary 摘要
| Metric 指標 | Data Set A | Data Set B | Difference 差異 |
|---|---|---|---|
| Total amount 總金額 | [amount] | [amount] | [diff] |
| Item count 項目數 | [count] | [count] | [diff] |
| Matched items 已配對 | [count] ([%]) | | |
| Unmatched items 未配對 | [count] ([%]) | | |

## Reconciliation Status 核對狀態
[🟢 Reconciled / 🟡 Minor discrepancies / 🔴 Significant discrepancies]

## Matched Items 已配對項目
[Summary or full list depending on size]

## Discrepancies 差異項目

### Timing Differences 時間差異 ([count] items, [total amount])
| # | Description 描述 | Set A 集A | Set B 集B | Diff 差異 | Likely Cause 可能原因 |
|---|---|---|---|---|---|
| 1 | [item] | [amount/date] | [amount/date] | [diff] | [cause] |

### Missing Entries 遺漏登錄 ([count] items, [total amount])
| # | Missing From 遺漏於 | Description 描述 | Amount 金額 | Action 行動 |
|---|---|---|---|---|

### Amount Differences 金額差異 ([count] items, [total impact])
| # | Description 描述 | Set A | Set B | Diff | Action |
|---|---|---|---|---|---|

### Other 其他
[Classification differences, duplicates, etc.]

## Recommended Actions 建議行動
1. [Most impactful action first]
2. [Next action]
3. [Next action]

## Adjusting Entries Needed 需要的調整分錄
[If applicable — specific journal entries to correct discrepancies]
```

---

## Validation Rules 驗證規則

1. **Math is exact** — totals must be verifiable; no rounding errors in the reconciliation itself. 數學精確。
2. **Every unmatched item is categorized** — "miscellaneous" is not an acceptable category for more than 5% of items. 每個未配對項目都要分類。
3. **Discrepancies are ordered by impact** — largest dollar amounts first. 差異按影響排序。
4. **No items lost** — total items in A + total items in B = matched + unmatched from A + unmatched from B. 沒有項目遺失。
5. **Actions are specific** — "investigate further" is only acceptable with a specific person and deadline. 行動要具體。
6. **Tolerance is disclosed** — if a threshold was applied, state it clearly. 容差有揭露。

---

## Knowledge 知識庫

### Common Reconciliation Types 常見核對類型

- **Bank reconciliation 銀行對帳**: Company ledger vs. bank statement. Key issues: outstanding checks, deposits in transit, bank fees not yet recorded, interest not yet recorded.
- **Accounts receivable 應收帳款**: Customer ledger vs. aging report. Key issues: unapplied payments, disputed invoices, write-offs pending.
- **Budget vs. actual 預算 vs. 實際**: Planned budget vs. actual spending. Key issues: timing of expenditures, re-categorized expenses, approved overspends.
- **Intercompany 公司間**: Transactions between related entities. Key issues: transfer pricing, currency conversion, timing of recording.

### Domain-Specific Rules 領域特定規則
- Amounts must NEVER be rounded during comparison — compare to the cent/penny/分
  比較時金額絕不能四捨五入
- When matching by date, allow for ±3 business days for bank transactions
  銀行交易日期配對允許 ±3 個工作日
- A "reconciled" status requires discrepancies below the materiality threshold set by the organization
  「已核對」狀態要求差異低於組織設定的重大性門檻
- Always preserve the original data; never modify source records
  永遠保留原始資料；絕不修改來源記錄

### Red Flags 紅旗
- Same amount appearing multiple times on the same date (potential duplicate) 同日期同金額多次出現
- Round-number differences (potential manual adjustment without documentation) 整數差異
- Recurring unmatched items month after month (systemic issue) 月復一月重複出現的未配對項目
- Differences just below the review threshold (potential manipulation) 差異剛好低於審查門檻

---

## Composition Hooks 組合接口

- **Upstream** 上游: Data extraction Skills (reading bank statements, parsing invoices), data import tools
- **Downstream** 下游: Report generation (formatted reconciliation report), journal entry generation, escalation workflows
- **Pairs with** 搭配: document-reviewer (review the reconciliation report before filing)

---

*Part of the [Agentic Substrate](../../../README.md) Example Skills Gallery.*
