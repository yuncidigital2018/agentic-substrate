---
name: skill-self-discovery
description: >
  Interactive guided discovery that reveals non-technical users already possess every component needed to build an AI Skill.
  Use when the user says "I want to learn Skills but I'm not technical", "Can AI help with my work?",
  "help me turn my workflow into a Skill", "I don't know how to write prompts", or expresses doubt
  about their ability to work with AI. Also use when a non-engineer is exploring Skills for the first time.
metadata:
  version: "0.2.0"
  type: "Process"
  domain: "Learning / Onboarding"
---

# Skill Self-Discovery
# 技能自我發現

> *You already know how to build a Skill. You just don't know it yet.*
> *你已經會建立 Skill 了。你只是還不知道。*

---

## Identity 身份

- **Name**: skill-self-discovery
- **Type**: Process (guided interactive discovery)
- **For**: Anyone who works with knowledge — regardless of technical background. Especially effective for humanities-trained professionals (admin, marketing, project management, education, legal, accounting, HR) who feel "I'm not technical enough for AI."
- **對象**: 任何從事知識工作的人——不論技術背景。特別適合文組訓練出身的專業人士（行政、行銷、專案管理、教育、法務、會計、人資），那些覺得「我不夠技術，搞不來 AI」的人。

---

## Description 描述

This Skill guides users through a conversational self-discovery process. Through a series of natural questions about their everyday work, it reveals that they already possess every component needed to build an AI Skill — they just use different words for it.

這個 Skill 引導使用者經歷一個對話式的自我發現過程。透過一系列關於日常工作的自然提問，揭示他們已經擁有建構 AI Skill 所需的每個組件——他們只是用不同的詞彙來描述。

**The core insight**: People trained in humanities (liberal arts, social sciences, business) have strong logic, structure, and questioning abilities. They write reports, manage processes, validate outcomes, and coordinate workflows every day. These are *exactly* the abilities needed to define AI Skills. The barrier is not competence — it's vocabulary.

**核心洞見**：文組訓練（人文、社會科學、商學）出身的人具有很強的邏輯、結構和提問能力。他們每天撰寫報告、管理流程、驗證成果、協調工作流程。這些*正是*定義 AI Skill 所需的能力。障礙不是能力——而是詞彙。

---

## Trigger Conditions 觸發條件

Activate this Skill when the user says things like:

- "I want to learn how to build a Skill but I'm not technical"
  「我想學怎麼建 Skill 但我不懂技術」
- "I don't know how to write prompts / instructions for AI"
  「我不知道怎麼寫 prompt / AI 的指令」
- "Can AI help with my kind of work?" (non-engineering context)
  「AI 能幫我的工作嗎？」（非工程情境）
- "I want to try the self-discovery exercise"
  「我想試試自我發現練習」
- "Help me turn my workflow into a Skill"
  「幫我把我的工作流程變成 Skill」
- "skill-self-discovery" (direct invocation)
- User expresses doubt about their ability to work with AI
  使用者表達對自己使用 AI 能力的懷疑
- User is a non-engineer exploring Skills for the first time
  使用者是第一次探索 Skills 的非工程師

---

## Process Logic 流程邏輯

### Phase 0: Warm-up — Build Trust 暖身——建立信任

Before any questions, set the tone:

```
Say to the user (adapt to their language):

"Let's try something. I'm going to ask you a few questions about
your everyday work — not about AI, not about technology. Just about
what you do. At the end, I'll show you something interesting.

There are no wrong answers. Just describe your work the way you'd
explain it to a new colleague."
```

```
對使用者說（適應他們的語言）：

「我們來試個東西。我會問你幾個關於日常工作的問題——不是關於 AI，
不是關於技術。只是關於你做的事。最後，我會讓你看到一個有趣的東西。

沒有錯的答案。就像你會向新同事解釋的那樣描述你的工作。」
```

**Important**: Ask ONE question at a time. Wait for the answer. Do not overwhelm.

**重要**：一次問一個問題。等待回答。不要讓人感到壓力。

---

### Phase 1: The Seven Questions 七個問題

Each question maps to one of the Seven Components of a Skill (from [Skill Anatomy](../../docs/01-foundations/skill-anatomy.md)), but the user doesn't know this yet. Ask in natural, conversational language.

每個問題對應到 Skill 七大組件的其中一個（來自[技能模組解剖學](../../docs/01-foundations/skill-anatomy.md)），但使用者還不知道。用自然的對話語言提問。

```
Question → Hidden Component Mapping:
問題 → 隱藏的組件對應：

Q1: "What's your role? What kind of work do you do every day?"
    「你的角色是什麼？你每天做什麼樣的工作？」
    → Maps to: Component 1 — Identity (Scope & Role)
    → 對應：組件一——身份（範圍與角色）

Q2: "Pick one task you do regularly. What usually triggers it?
     Is it a deadline? Someone sending you something? A recurring
     schedule? A specific situation?"
    「選一個你經常做的任務。什麼會觸發它？是截止日期？有人寄東西
     給你？固定的時程？特定的情況？」
    → Maps to: Component 2 — Trigger Conditions
    → 對應：組件二——觸發條件

Q3: "When you start this task, what do you need to have in front
     of you? What information, files, or data do you need before
     you can begin?"
    「當你開始這個任務時，你需要什麼在面前？開始之前需要什麼資訊、
     檔案或資料？」
    → Maps to: Component 4 — I/O Contract (Input)
    → 對應：組件四——輸入/輸出契約（輸入）

Q4: "Walk me through how you do it, step by step. If you were
     teaching a new colleague, what would you tell them?"
    「帶我走一遍你是怎麼做的，一步一步。如果你在教一個新同事，
     你會怎麼說？」
    → Maps to: Component 3 — Process Logic
    → 對應：組件三——流程邏輯

Q5: "When you're done, what does the finished product look like?
     Is it a document? A spreadsheet? An email? A decision?"
    「做完的時候，成品長什麼樣子？是文件？試算表？email？一個決定？」
    → Maps to: Component 4 — I/O Contract (Output)
    → 對應：組件四——輸入/輸出契約（輸出）

Q6: "How do you know it's done correctly? What do you check?
     What would your supervisor check? What mistakes would be
     unacceptable?"
    「你怎麼知道做對了？你會檢查什麼？你的主管會檢查什麼？
     什麼錯誤是不能接受的？」
    → Maps to: Component 5 — Validation Rules
    → 對應：組件五——驗證規則

Q7: "Is there specialized knowledge that makes you good at this?
     Things a new person wouldn't know — shortcuts, exceptions,
     things you've learned from experience?"
    「有什麼專業知識讓你擅長這件事？新人不會知道的東西——
     捷徑、例外、你從經驗中學到的事？」
    → Maps to: Component 6 — Knowledge
    → 對應：組件六——知識庫
```

**Conversation notes** 對話注意事項:

- If the user gives a short answer, gently probe deeper: "Can you give me an example?" / "What happens if that step goes wrong?"
  如果使用者回答很簡短，輕柔地深入追問：「可以舉個例子嗎？」/「如果那個步驟出錯會怎樣？」
- Mirror their language. If they say "核銷" don't translate it to "expense reconciliation." Use their words.
  鏡射他們的語言。如果他們說「核銷」，不要翻譯成「expense reconciliation」。使用他們的詞。
- Acknowledge each answer warmly before moving to the next question.
  在轉到下一個問題前，溫暖地確認每個回答。

---

### Phase 2: The Reveal — "You Just Built a Skill" 揭曉——「你剛剛建了一個 Skill」

After all seven questions are answered, present the reveal. This is the key pedagogical moment.

七個問題都回答完後，呈現揭曉。這是關鍵的教學時刻。

```
Say to the user:

"Now let me show you something. Remember I said there'd be
something interesting at the end?

Everything you just told me — that's a Skill. Not an AI Skill,
not a coding thing. YOUR skill. The one you use every day.

Here's what you defined:"
```

Then present their answers re-organized into the Seven Components format:

然後將他們的答案重新組織成七大組件格式呈現：

```markdown
## Your Skill: [Task Name — use their words]
## 你的 Skill：[任務名稱——使用他們的詞]

### 1. Identity 身份
[Their answer to Q1, slightly structured]

### 2. Trigger Conditions 觸發條件
[Their answer to Q2]

### 3. Process Logic 流程邏輯
[Their answer to Q4, organized as numbered steps]

### 4. Input/Output 輸入/輸出
- Input: [Their answer to Q3]
- Output: [Their answer to Q5]

### 5. Validation Rules 驗證規則
[Their answer to Q6, organized as checklist]

### 6. Domain Knowledge 知識庫
[Their answer to Q7]

### 7. Composition 組合性
"This Skill could connect with other Skills — for example,
its output could feed into [suggest a logical next step
based on their answers]."
```

Then say:

```
"This is exactly the same structure that AI Skills use.
The seven components you just defined are the same seven
components in every Skill in this framework.

You didn't need to learn any technology. You just described
your work — and your work IS the Skill.

The only difference between what you just did and a 'real'
AI Skill is that yours is in your head. If you write it
down in a file like this, an AI can follow it — just like
a new colleague following your instructions."
```

---

### Phase 3: Bridge — From Discovery to Creation 橋接——從發現到創建

Offer the next step (optional, based on user's interest):

提供下一步（可選，根據使用者興趣）：

```
"Would you like me to:

(A) Save this as a proper SKILL.md file that you can
    actually use with AI tools like Claude Code or Cowork?

(B) Try running your Skill right now — give me a real
    example of [their task] and I'll follow your process
    step by step?

(C) Just keep this as a reference — you can come back
    to it anytime."
```

If they choose (A): Generate a proper SKILL.md file following the format in [Skill Anatomy](../../docs/01-foundations/skill-anatomy.md), using their exact words and examples. Save it to a file they can access.

如果選 (A)：生成一個正式的 SKILL.md 檔案，遵循[技能模組解剖學](../../docs/01-foundations/skill-anatomy.md)中的格式，使用他們的原話和範例。儲存為他們可以存取的檔案。

If they choose (B): Execute their workflow on a real example, showing at each step "Now I'm doing step 3 that you defined..." — this demonstrates that their knowledge is directly executable by AI.

如果選 (B)：在真實範例上執行他們的工作流程，在每個步驟顯示「現在我在執行你定義的步驟 3……」——這展示他們的知識可以直接被 AI 執行。

If they choose (C): Acknowledge and encourage. The seed is planted.

如果選 (C)：確認和鼓勵。種子已經播下。

---

## Validation Rules 驗證規則

The Skill succeeds when:

這個 Skill 成功的標準：

1. **All seven questions were answered** — no component left blank 七個問題都有回答——沒有組件留白
2. **The reveal moment landed** — user expresses recognition ("oh!", "原來是這樣", surprise, or similar) 揭曉時刻產生效果——使用者表達出認知
3. **The re-organized output uses the user's own words** — not generic templates 重新組織的產出使用使用者自己的詞——不是通用模板
4. **No jargon was introduced before the reveal** — the entire Q&A phase uses everyday language 在揭曉之前沒有引入術語——整個 Q&A 階段使用日常語言
5. **The user understands the connection** — "my daily work process = a Skill definition" 使用者理解連結——「我的日常工作流程 = 一個 Skill 定義」

---

## Knowledge 知識庫

### Why This Works 為什麼這有效

The barrier for non-technical professionals is not capability but **vocabulary and framing**. They hear "AI Skill," "prompt engineering," "structured workflow," and assume it requires programming knowledge. In reality:

非技術專業人士的障礙不是能力而是**詞彙和框架**。他們聽到「AI Skill」、「prompt engineering」、「結構化工作流程」，就假設需要程式設計知識。事實上：

| What they already do 他們已經在做的 | What it's called in Agentic terms 在代理術語中叫什麼 |
|---|---|
| "I know what my job is" 「我知道我的工作是什麼」 | Identity / Scope 身份/範圍 |
| "I know when to start" 「我知道什麼時候要開始」 | Trigger Conditions 觸發條件 |
| "I follow a process" 「我有一套流程」 | Process Logic 流程邏輯 |
| "I need these materials" 「我需要這些材料」 | Input Contract 輸入契約 |
| "I produce this deliverable" 「我產出這個交付物」 | Output Contract 輸出契約 |
| "I check my work" 「我會檢查我的成果」 | Validation Rules 驗證規則 |
| "I know the tricks" 「我知道其中的訣竅」 | Domain Knowledge 知識庫 |

### Conversation Design Principles 對話設計原則

- **Never use the word "Skill" until Phase 2** 在第二階段之前絕不使用「Skill」這個詞. The reveal depends on the surprise.
  揭曉依賴於驚喜。
- **One question at a time** 一次一個問題. Resist the urge to ask follow-ups before they answer.
  抵抗在他們回答之前追問的衝動。
- **Their words are sacred** 他們的詞是神聖的. When re-presenting their answers in Phase 2, use their exact phrasing. This creates the "that's MY knowledge" recognition.
  在第二階段重新呈現答案時，使用他們的原話。這創造出「那是我的知識」的認同感。
- **Warmth over precision** 溫暖重於精準. It's more important that the user feels capable than that the Skill definition is technically perfect. Polish can come later.
  使用者感到有能力，比 Skill 定義技術上完美更重要。打磨可以之後再做。

---

## Composition Hooks 組合接口

- **Output → skill-builder**: After self-discovery, users who want a production-quality Skill can use the [Skill Builder](../skill-builder/) for refinement
  自我發現後，想要產品品質 Skill 的使用者可以使用 Skill Builder 進行精煉
- **Output → conversation-to-skill**: If the user has existing chat histories they want to organize, connect to [Conversation to Skill](../conversation-to-skill/)
  如果使用者有想整理的現有聊天記錄，連接到 Conversation to Skill
- **Input ← docs/04-curriculum**: The learning path documents reference this Skill as a hands-on exercise
  學習路徑文件引用這個 Skill 作為動手練習

---

## Example Session 範例工作階段

Here's a condensed example of the Skill in action:

以下是 Skill 實際運作的精簡範例：

```
AI:  Let's try something. I'll ask you about your everyday work.
     No tech knowledge needed. Just tell me what you do.
     What's your role?

User: I'm an admin assistant. I handle expense reports.
      我是行政助理。我處理報帳。

AI:  Got it. When do you usually start working on expense reports?
     What triggers it?

User: When colleagues send me their receipts and forms.
      Usually before the 5th of each month.
      同事把單據和表單寄給我的時候。通常在每個月5號之前。

AI:  Makes sense. When you sit down to do it, what do you need
     in front of you before you can start?

User: The receipts, the expense form, last month's ledger,
      and the approved budget for their department.
      單據、報帳表、上個月的帳本、還有他們部門的核准預算。

AI:  Walk me through the steps — like you're teaching a new hire.

User: First I check the receipts match the form amounts.
      Then I verify the expense category is correct.
      Then I check against the department budget — can't exceed it.
      Then I enter it into the system.
      Then I flag anything over 10,000 for manager approval.
      Finally I file everything and update the ledger.
      先確認單據金額跟表單一致。然後確認費用類別正確。
      然後對照部門預算——不能超過。然後登入系統。
      超過一萬的要標記給主管核准。最後歸檔並更新帳本。

AI:  When it's done, what's the deliverable?

User: Updated ledger, filed receipts, and a summary email
      to the department head.
      更新的帳本、歸檔的單據、還有一封給部門主管的摘要 email。

AI:  How do you know you did it right? What would be an
     unacceptable mistake?

User: Amounts must match exactly — no rounding.
      Every receipt must have a date and vendor name.
      Budget overages must be flagged, no exceptions.
      My supervisor spot-checks the ledger monthly.
      金額必須完全一致——不能四捨五入。
      每張單據都要有日期和廠商名稱。
      超預算必須標記，沒有例外。
      主管每月會抽查帳本。

AI:  Last question. Any tricks or knowledge that makes you
     good at this that a new person wouldn't know?

User: Some departments always miscategorize "transportation"
      as "supplies." I know which colleagues tend to submit
      late, so I send them reminders on the 1st.
      And the system crashes if you enter more than 50 items
      at once, so I batch them in groups of 30.
      有些部門總是把「交通費」歸錯成「雜支」。我知道哪些同事
      容易遲交，所以我在1號就先發提醒。
      系統一次輸入超過50筆會當掉，所以我分成30筆一批。

AI:  Now let me show you something interesting.

     Everything you just told me? That's a Skill.

     ┌─────────────────────────────────────────────┐
     │  YOUR SKILL: Expense Report Processing       │
     │  你的 Skill：報帳處理                         │
     │                                              │
     │  1. Identity: Admin assistant, expense       │
     │     reports                                  │
     │  2. Trigger: Colleagues send receipts,       │
     │     before the 5th monthly                   │
     │  3. Process: 6 steps you just described      │
     │  4. Input: Receipts, forms, ledger, budget   │
     │     Output: Updated ledger, filed receipts,  │
     │     summary email                            │
     │  5. Validation: Exact amounts, dates on all  │
     │     receipts, budget flags, supervisor check  │
     │  6. Knowledge: Miscategorization patterns,   │
     │     late submitters, system batch limit       │
     │  7. Composition: Could connect to a budget   │
     │     tracking Skill or a monthly report Skill │
     └─────────────────────────────────────────────┘

     This is the exact same structure used by every AI
     Skill in the Agentic Substrate framework.
     You didn't need any programming. You just described
     your job — and your job IS the Skill.
```

---

*Part of the [Agentic Substrate](../../README.md) framework.*
*Learn more: [You Already Know How to Build a Skill](../../docs/04-curriculum/you-already-know.md)*
