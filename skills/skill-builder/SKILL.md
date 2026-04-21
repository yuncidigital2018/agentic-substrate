---
name: skill-builder
description: >
  Guide any user through deliberately constructing a production-quality SKILL.md from scratch with role-aware questions.
  Use when the user says "I want to build a Skill", "help me create a Skill for [task]",
  "I have a workflow I want to automate", "help me write a SKILL.md", or wants to make a task
  repeatable with AI. Also activates after skill-self-discovery or conversation-to-skill when the user
  wants to refine further.
metadata:
  version: "0.2.0"
  type: "Process"
  domain: "Skill Creation"
---

# Skill Builder
# 技能建構助理

> *You know your work better than any engineer. Let's turn that knowledge into something an AI can run.*
> *你比任何工程師都了解你的工作。讓我們把那份知識變成 AI 能執行的東西。*

---

## Identity 身份

- **Name**: skill-builder
- **Type**: Process (guided interactive creation)
- **For**: Anyone who has identified a repeatable workflow and wants to turn it into a production-quality SKILL.md — regardless of technical background. Works for engineers and non-engineers alike.
- **對象**: 任何已經辨識出一個可重複工作流程、想要把它轉化為正式 SKILL.md 的人——不論技術背景。工程師和非工程師都適用。

---

## Description 描述

Skill Self-Discovery helps people realize they *already have* Skills. Conversation-to-Skill helps people *extract* Skills from messy chats. **Skill Builder is the next step** — it helps people *deliberately construct* a new Skill from scratch, with guided questions, structured templates, and immediate testing.

Skill Self-Discovery 幫助人們意識到他們*已經擁有* Skills。Conversation-to-Skill 幫助人們從混亂的對話中*提取* Skills。**Skill Builder 是下一步**——它幫助人們*刻意建構*一個全新的 Skill，透過引導式提問、結構化模板和即時測試。

Think of the three Skills as a learning progression:

把三個 Skills 想像成一個學習進程：

```
skill-self-discovery    →  "I already have Skills!"
                            「我已經有 Skills 了！」

conversation-to-skill   →  "I can capture Skills from my work!"
                            「我可以從工作中擷取 Skills！」

skill-builder           →  "I can build new Skills on purpose!"
                            「我可以刻意建構新的 Skills！」
```

This Skill walks users through a **role-aware, question-driven process** that produces a complete, immediately usable SKILL.md file. It adapts its questions based on the user's domain — an accountant gets different follow-up questions than a marketer or a project manager.

這個 Skill 帶領使用者走過一個**角色感知、問題驅動的流程**，產出一份完整的、可立即使用的 SKILL.md 檔案。它根據使用者的領域調整問題——會計得到的追問和行銷人員或專案經理不同。

---

## Trigger Conditions 觸發條件

Activate this Skill when the user says things like:

- "I want to build a Skill"
  「我想建一個 Skill」
- "Help me create a Skill for [task]"
  「幫我為 [任務] 建一個 Skill」
- "I have a workflow I want to automate"
  「我有一個想自動化的工作流程」
- "Can you help me write a SKILL.md?"
  「你能幫我寫一個 SKILL.md 嗎？」
- "I want to make my [task] repeatable with AI"
  「我想讓我的 [任務] 用 AI 可重複執行」
- "skill-builder" (direct invocation)
- User has completed skill-self-discovery and chosen option (A) "Save as SKILL.md"
  使用者完成了 skill-self-discovery 並選擇了選項 (A)「儲存為 SKILL.md」
- User has completed conversation-to-skill Phase 4 and wants to refine further
  使用者完成了 conversation-to-skill 第四階段，想進一步精煉

---

## Process Logic 流程邏輯

### Phase 1: Role & Context — "Tell me about your world" 角色與情境

Start by understanding who the user is and what domain they operate in. This shapes all subsequent questions.

先了解使用者是誰、在什麼領域工作。這會影響後續所有問題。

```
Say to the user (adapt to their language):

"Let's build a Skill together. First, a couple of quick
questions to understand your context.

What's your role or field? For example:
• Administration / Office Management 行政/辦公室管理
• Accounting / Finance 會計/財務
• Marketing / Content 行銷/內容
• Project Management 專案管理
• Design / Creative 設計/創意
• Education / Training 教育/培訓
• Legal / Compliance 法務/合規
• HR / People Operations 人資/人事
• Engineering / Development 工程/開發
• Research / Analysis 研究/分析
• Sales / Business Development 業務/商務開發
• Other (tell me!) 其他（告訴我！）"

「讓我們一起建一個 Skill。先問幾個快速的問題了解你的情境。

你的角色或領域是什麼？例如：
• 行政/辦公室管理
• 會計/財務
• 行銷/內容
• 專案管理
• 設計/創意
• 教育/培訓
• 法務/合規
• 人資/人事
• 工程/開發
• 研究/分析
• 業務/商務開發
• 其他（告訴我！）」
```

After they answer, ask:

```
"Great. Now, what's the specific task you want to turn into a Skill?
Describe it the way you'd explain it to a colleague over coffee."

「好的。那你想把什麼具體的任務變成 Skill？
像跟同事喝咖啡時聊天那樣描述就好。」
```

**Important**: Let them talk freely. Don't interrupt. Their natural description contains gold — the sequence, the edge cases, the implicit validation rules. Take mental notes.

**重要**：讓他們自由地說。不要打斷。他們自然的描述包含寶藏——順序、邊界案例、隱含的驗證規則。默默記下。

---

### Phase 2: Deep Dive — The Seven Components 深度探索——七大組件

Now systematically fill in each of the Seven Components from [Skill Anatomy](../../docs/01-foundations/skill-anatomy.md). Ask ONE question at a time. Use **role-adapted language** — the exact phrasing changes based on what you learned in Phase 1.

現在系統性地填入[技能模組解剖學](../../docs/01-foundations/skill-anatomy.md)的七大組件。一次問一個問題。使用**角色適應的語言**——確切的措辭根據你在第一階段學到的來調整。

#### Component 1: Identity 身份

```
"Let's give this Skill a name. Something short and clear —
like you'd name a folder. What would you call it?"

「讓我們給這個 Skill 一個名字。簡短明瞭的——
像你命名一個資料夾那樣。你會怎麼叫它？」
```

Then determine the Skill Type together:

```
"Based on what you described, this sounds like a [Type] Skill.
Here's what I mean:

• Process — You follow a sequence of steps to get something done
  流程型——你按照一連串步驟完成某件事
• Transform — You take something in one format and produce it
  in another format
  轉換型——你把一個格式的東西轉換成另一個格式
• Data — You look things up, check records, or retrieve information
  資料型——你查找、核對記錄或檢索資訊
• Integration — You connect information between different systems
  or people
  整合型——你在不同系統或人員之間連接資訊
• Orchestration — You coordinate multiple sub-tasks or people
  to get a bigger thing done
  調度型——你協調多個子任務或人員來完成更大的事

Does [Type] sound right, or does another type fit better?"

「根據你描述的，這聽起來像是一個[類型]的 Skill。
我的意思是：[上述五個類型]
[類型]聽起來對嗎，還是另一個類型更合適？」
```

#### Component 2: Trigger Conditions 觸發條件

Adapt the question to their domain:

```
Role-specific variations:
角色特定的變化：

Accounting: "What triggers this task? End of month? Receiving
invoices? A deadline from tax authority?"
會計：「什麼觸發這個任務？月底？收到發票？稅務機關的截止日？」

Marketing: "When do you start this? Campaign launch date?
Content calendar? Client request? Analytics alert?"
行銷：「你什麼時候開始？活動上線日？內容行事曆？客戶要求？數據警報？」

PM: "What kicks this off? Sprint start? Milestone date?
Stakeholder request? Risk flag?"
專案管理：「什麼啟動這個？Sprint 開始？里程碑日期？利害關係人要求？風險標記？」

General: "What usually triggers this task? Is it a schedule,
an event, a request from someone, or a condition being met?"
通用：「什麼通常觸發這個任務？是時程、事件、某人的要求、還是某個條件達成？」
```

After their answer, probe for **edge triggers**:

```
"Are there situations where you'd start this task earlier than
usual, or skip it entirely? Any exceptions?"

「有沒有你會比平常更早開始這個任務、或完全跳過的情況？有例外嗎？」
```

#### Component 3: Process Logic 流程邏輯

```
"Now let's map out the steps. Walk me through this task like
you're training someone who's smart but has never done it before.

Start from the very beginning — what's the first thing you do?"

「現在讓我們把步驟列出來。帶我走一遍這個任務，
像你在訓練一個聰明但從沒做過的人。

從最開頭開始——你做的第一件事是什麼？」
```

As they describe steps, actively listen for:

在他們描述步驟時，主動聽出：

- **Decision points** 決策點: "If X, then I do Y, otherwise Z" → These become conditional logic
- **Loops** 迴圈: "I repeat this for each..." → These become iteration patterns
- **Dependencies** 相依性: "I can't do this until..." → These become sequencing rules
- **Parallel work** 平行工作: "While that's happening, I also..." → These become parallel steps

After they finish, read back the steps and ask:

```
"Here's what I heard — [numbered steps]. Did I get the order
right? Anything I missed or should change?"

「這是我聽到的——[編號步驟]。順序對嗎？有什麼我漏掉或要改的？」
```

#### Component 4: I/O Contract 輸入/輸出契約

```
Input:
"Before you can start, what needs to exist? Think about:
• Files or documents you need 你需要的檔案或文件
• Data or information you need to look up 你需要查的資料或資訊
• Decisions that need to have been made already 已經要先做好的決定
• Access or permissions you need 你需要的存取權限或許可"

Output:
"When you're completely done, what have you produced? Think about:
• Files or documents you've created or updated 你建立或更新的檔案或文件
• Notifications or communications sent 發送的通知或溝通
• Records updated 更新的紀錄
• Decisions documented 記錄下來的決定"
```

#### Component 5: Validation Rules 驗證規則

```
"How do you know this is done RIGHT? I want to understand your
quality bar. Think about:

• What would your supervisor check? 你的主管會檢查什麼？
• What mistakes would be embarrassing or costly? 什麼錯誤會很丟臉或代價很高？
• If you handed this to a colleague to verify, what would
  you tell them to look for? 如果你交給同事驗證，你會叫他們看什麼？
• Is there a number that must match, a format that must be
  followed, a deadline that must be met? 有沒有數字要對上、格式要遵守、截止日要達到？"
```

#### Component 6: Knowledge 知識庫

```
"Now the secret sauce — the stuff that makes YOU good at this.

• What do beginners always get wrong? 新手總是搞錯什麼？
• What shortcuts have you discovered? 你發現了什麼捷徑？
• What exceptions exist that aren't written in any manual?
  有什麼例外是任何手冊都沒寫的？
• What context or history matters?
  什麼背景或歷史脈絡很重要？
• Are there specific terms, naming conventions, or standards
  in your organization? 你的組織有特定的術語、命名慣例或標準嗎？"
```

**Critical**: This is where the user's **domain expertise** lives. Probe generously. This component is what makes a user-built Skill better than anything a generic AI could produce.

**關鍵**：這是使用者的**領域專業知識**所在之處。慷慨地追問。這個組件是使用者建構的 Skill 比任何通用 AI 能產出的東西更好的原因。

#### Component 7: Composition Hooks 組合接口

```
"Last question. Does this task connect to other tasks?

• Does it use output from another task as its input?
  它使用另一個任務的輸出作為輸入嗎？
• Does its output become input for something else?
  它的輸出會變成另一個東西的輸入嗎？
• Could this task be broken into smaller, reusable parts?
  這個任務能拆成更小、可重用的部分嗎？

It's fine if the answer is 'no' or 'I'm not sure' —
not every Skill needs to connect to others."

「最後一個問題。這個任務跟其他任務有連結嗎？
[上述問題]
答案是『沒有』或『不確定』完全沒問題——
不是每個 Skill 都需要跟其他的連接。」
```

---

### Phase 3: Draft & Review — "Here's your Skill" 草稿與審閱

Generate the complete SKILL.md and present it for review. Use their exact words wherever possible.

生成完整的 SKILL.md 並呈現給他們審閱。盡可能使用他們的原話。

```
Say to the user:

"Here's your Skill — assembled from everything you told me.
Read through it and tell me:

1. Is anything wrong or missing?
2. Is there anything you'd phrase differently?
3. Does the process logic match how you actually do it?"

「這是你的 Skill——從你告訴我的一切組裝而成。
讀一遍，告訴我：

1. 有什麼錯誤或遺漏嗎？
2. 有什麼你會用不同方式表達？
3. 流程邏輯跟你實際的做法一致嗎？」
```

The generated SKILL.md follows this structure:

```markdown
# [Skill Name]
# [技能名稱]

> *[One-sentence description in the user's own words]*
> *[使用者自己的話的一句描述]*

---

## Identity 身份

- **Name**: [kebab-case-name]
- **Type**: [Process / Transform / Data / Integration / Orchestration]
- **For**: [Who benefits — in their words]
- **對象**: [受益者——用他們的話]

---

## Description 描述

[2-3 paragraphs describing what this Skill does, why it exists,
and what problem it solves. Written in the user's voice.]

---

## Trigger Conditions 觸發條件

Activate this Skill when:

- [Primary trigger]
- [Secondary trigger]
- [Edge case trigger, if any]

---

## Process Logic 流程邏輯

[Numbered steps, with decision points marked as sub-steps]

1. [Step 1]
2. [Step 2]
   - If [condition]: [action A]
   - Otherwise: [action B]
3. [Step 3]
...

---

## I/O Contract 輸入輸出合約

### Input 輸入
- [Input 1]: [description]
- [Input 2]: [description]

### Output 輸出
- [Output 1]: [description]
- [Output 2]: [description]

---

## Validation Rules 驗證規則

The Skill execution is successful when:

1. [Checkable criterion 1]
2. [Checkable criterion 2]
3. [Checkable criterion 3]
...

---

## Knowledge 知識庫

### Domain-Specific Rules 領域特定規則
- [Rule / exception / shortcut 1]
- [Rule / exception / shortcut 2]

### Common Mistakes to Avoid 常見錯誤
- [Mistake 1 and how to prevent it]
- [Mistake 2 and how to prevent it]

### Organizational Context 組織脈絡
- [Naming conventions, standards, or history that matters]

---

## Composition Hooks 組合接口

- **Upstream** 上游: [What feeds into this Skill]
- **Downstream** 下游: [What this Skill's output feeds into]
- **Decomposition** 分解: [Sub-skills if applicable]
```

---

### Phase 4: Refine — Iterative Improvement 精煉——迭代改善

After the user reviews the draft, enter an iterative refinement loop:

使用者審閱草稿後，進入迭代精煉循環：

```
Refinement cycle:

1. User identifies an issue or improvement
   使用者指出問題或改善點
2. Discuss the change — understand WHY they want it different
   討論修改——理解為什麼他們想要不同
3. Apply the change to the SKILL.md
   將修改應用到 SKILL.md
4. Show the updated section
   展示更新後的段落
5. Ask: "Anything else, or is this ready?"
   問：「還有其他的嗎，還是準備好了？」
6. Repeat until they say it's ready
   重複直到他們說準備好了
```

**Refinement prompts to offer** 可提供的精煉提示:

```
"A few things we could sharpen:

• Process Logic — Want me to add more detail to any step?
  流程邏輯——要我為任何步驟加更多細節嗎？
• Edge Cases — Are there unusual situations we should handle?
  邊界案例——有沒有我們應該處理的不尋常情況？
• Validation — Should the quality checks be stricter or more specific?
  驗證——品質檢查應該更嚴格或更具體嗎？
• Knowledge — Any more tricks of the trade to include?
  知識——還有更多行業訣竅要加入嗎？
• Naming — Happy with the Skill name, or want to change it?
  命名——對 Skill 名字滿意嗎，還是想改？"
```

---

### Phase 5: Deliver — Save, Test, or Both 交付——儲存、測試或兩者

When the user confirms the Skill is ready:

使用者確認 Skill 準備好了之後：

```
"Your Skill is ready. What would you like to do?

(A) Save it — I'll write it to a SKILL.md file you can install
    in Claude Code, Cowork, or any agent platform
    儲存——我會寫成 SKILL.md 檔案，你可以安裝到 Claude Code、Cowork 或任何 Agent 平台

(B) Test it — Give me a real example and I'll execute your Skill
    step by step, showing my work at each stage
    測試——給我一個真實的例子，我會一步步執行你的 Skill，在每個階段展示我的工作

(C) Both — Save first, then test it on a real example
    兩者——先儲存，然後在真實例子上測試

(D) Teach it — Walk me through how to modify this Skill later
    when my process changes
    教學——帶我了解之後流程改變時怎麼修改這個 Skill

Which would you like?"
```

#### If Save (A or C):

Write the SKILL.md file and provide it to the user. Also generate a brief `README.md` for the skill directory:

```markdown
# [Skill Name]

Built with [Skill Builder](../skill-builder/) from the
[Agentic Substrate](../../README.md) framework.

## Quick Start
1. Copy this folder to your Claude Code or Cowork skills directory
2. The Skill activates when: [trigger summary]
3. It produces: [output summary]

## Files
- `SKILL.md` — The complete Skill definition
```

#### If Test (B or C):

Execute the Skill on a real example the user provides. At each step, show:

在使用者提供的真實範例上執行 Skill。在每個步驟，展示：

```
"▶ Step [N]: [Step description from their Skill]
  [What I'm doing and why]
  [The output of this step]

  ✓ Validation: [relevant check from their validation rules]"
```

After the test, ask:

```
"How did that go? Did the Skill handle this case correctly?
Anything we should adjust based on this test run?"

「怎麼樣？Skill 有正確處理這個案例嗎？
根據這次測試有什麼需要調整的嗎？」
```

#### If Teach (D):

Explain the SKILL.md structure in simple terms:

```
"Your SKILL.md is just a text file with sections. Here's how
to modify it later:

• To change WHEN the Skill activates → Edit 'Trigger Conditions'
  改變何時啟動 → 編輯「觸發條件」
• To change HOW it works → Edit 'Process Logic'
  改變如何運作 → 編輯「流程邏輯」
• To change what it CHECKS → Edit 'Validation Rules'
  改變它檢查什麼 → 編輯「驗證規則」
• To add new KNOWLEDGE → Edit 'Knowledge'
  新增知識 → 編輯「知識庫」
• To change what goes IN or OUT → Edit 'I/O Contract'
  改變輸入或輸出 → 編輯「輸入輸出合約」

You can edit it in any text editor. No coding required.
It's just organized writing — something you already do well."

「你可以用任何文字編輯器編輯它。不需要寫程式。
它只是有組織的寫作——你已經很擅長的事。」
```

---

## Validation Rules 驗證規則

The Skill execution is successful when:

1. **All seven components are filled** — no section left as placeholder or generic text. 七個組件都填寫完畢——沒有留下佔位或通用文字的段落。
2. **User's own words are preserved** — the SKILL.md reads like the user wrote it, not like a template. 使用者的原話被保留——SKILL.md 讀起來像使用者寫的，不像模板。
3. **Process Logic is specific and actionable** — an AI (or new colleague) could follow the steps without asking clarifying questions. 流程邏輯是具體且可執行的——AI（或新同事）能不問問題就跟著步驟做。
4. **Validation Rules are checkable** — each rule can be objectively verified (not vague like "looks good"). 驗證規則是可檢查的——每條規則都能客觀驗證（不是模糊的「看起來不錯」）。
5. **Knowledge section contains real domain expertise** — not generic advice, but specific shortcuts, exceptions, or institutional knowledge that makes this Skill valuable. 知識庫包含真實的領域專業知識——不是通用建議，而是讓這個 Skill 有價值的具體捷徑、例外或機構知識。
6. **User has reviewed and confirmed** — the Skill was not auto-generated without user validation. 使用者已經審閱並確認——Skill 不是未經使用者驗證就自動產生的。
7. **The Skill has been saved or tested** — the process concluded with a concrete deliverable, not just a conversation. Skill 已經被儲存或測試——流程以具體交付物結束，不只是一段對話。

---

## Knowledge 知識庫

### Role-Specific Question Adaptations 角色特定的問題調整

The key to this Skill's effectiveness is adapting language to the user's domain. Here are adaptation guidelines:

這個 Skill 的有效性關鍵在於將語言適應使用者的領域。以下是調整指引：

**Accounting / Finance 會計/財務**
- Use: 帳目、對帳、核銷、沖帳、傳票、分錄
- Triggers often involve: 月結、季報、年度結算、稅務申報
- Validation is numbers-heavy: 金額一致、借貸平衡、稅率正確
- Knowledge includes: 科目分類慣例、稅法例外、ERP 系統怪癖

**Marketing / Content 行銷/內容**
- Use: 素材、投放、受眾、轉換率、CTA、排程
- Triggers often involve: 活動上線、內容行事曆、客戶需求
- Validation includes: 品牌一致性、連結正確、尺寸規格
- Knowledge includes: 平台演算法偏好、素材表現模式、A/B 測試心得

**Project Management 專案管理**
- Use: 里程碑、工項、甘特圖、風險、利害關係人
- Triggers often involve: 專案啟動、階段交付、週報時間
- Validation includes: 時程準確、預算追蹤、範疇管理
- Knowledge includes: 客戶溝通慣例、審查流程、常見延遲原因

**Administration 行政**
- Use: 簽呈、公文、核章、歸檔、會議紀錄
- Triggers often involve: 主管交辦、固定時程、公文來文
- Validation includes: 格式正確、用印無誤、副本寄達
- Knowledge includes: 機關用語、公文格式、內部流程潛規則

**Legal / Compliance 法務/合規**
- Use: 條款、合約、風險評估、盡職調查、免責
- Triggers often involve: 合約到期、新法規公布、訴訟通知
- Validation includes: 法條引用正確、利害關係揭露、期限遵守
- Knowledge includes: 判例、主管機關解釋函、業界慣例

**Education / Training 教育/培訓**
- Use: 教案、學習目標、評量、回饋、課綱
- Triggers often involve: 學期開始、培訓需求、評鑑時程
- Validation includes: 學習目標對齊、評量覆蓋率、學員回饋
- Knowledge includes: 學習理論應用、班級經營技巧、評分潛規則

**HR / People Operations 人資/人事**
- Use: 招募、到職、離職、考績、薪資
- Triggers often involve: 缺額通知、考績週期、法規異動
- Validation includes: 法規遵循、公平性、保密性
- Knowledge includes: 勞基法細節、組織文化慣例、面試紅旗

**Engineering / Development 工程/開發**
- Use: spec、PR、CI/CD、test coverage、deploy
- Triggers often involve: ticket、sprint planning、incident
- Validation includes: tests pass、code review approved、no regressions
- Knowledge includes: codebase conventions、infra quirks、performance thresholds

### How This Differs from skill-self-discovery 與 skill-self-discovery 的差異

| Aspect 面向 | skill-self-discovery | skill-builder |
|---|---|---|
| **Goal 目標** | Awareness — "I have Skills" 覺察 | Creation — "I build Skills" 創建 |
| **Starting point 起點** | User doesn't know what a Skill is 使用者不知道什麼是 Skill | User knows and wants to create one 使用者知道且想創建 |
| **Depth 深度** | Surface — enough for the "aha" moment 表層——足夠產生頓悟 | Production — detailed enough to execute 正式——詳細到能執行 |
| **Output 輸出** | Recognition + optional rough SKILL.md 認知 + 可選的粗略 SKILL.md | Polished, tested, installable SKILL.md 打磨過、測試過、可安裝的 SKILL.md |
| **Tone 語調** | Warm, surprising, pedagogical 溫暖、驚喜、教學性 | Collaborative, professional, thorough 協作、專業、徹底 |

### How This Differs from conversation-to-skill 與 conversation-to-skill 的差異

| Aspect 面向 | conversation-to-skill | skill-builder |
|---|---|---|
| **Source 來源** | Existing messy conversation 現有混亂對話 | Fresh, guided creation from scratch 全新、引導式從頭建立 |
| **Method 方法** | Extraction — mine what's already there 提取——挖掘已經存在的 | Construction — build deliberately 建構——刻意建造 |
| **User state 使用者狀態** | May not intend to create a Skill 可能沒有打算創建 Skill | Actively wants to create a Skill 主動想要創建 Skill |
| **Process 流程** | Analyze → Organize → Reveal → Convert 分析→組織→揭示→轉換 | Ask → Probe → Draft → Refine → Deliver 提問→追問→草擬→精煉→交付 |

### The "80% Rule" of Skill Building Skill 建構的「80% 法則」

In practice, the user provides about 80% of what makes a Skill valuable — the domain knowledge, the process steps, the validation criteria, the edge cases. The remaining 20% is structural — formatting it as a SKILL.md, ensuring consistency, making it machine-readable. This Skill handles that 20% so the user can focus on what only they can provide.

實際上，使用者提供了 Skill 價值的 80%——領域知識、流程步驟、驗證標準、邊界案例。剩下的 20% 是結構性的——格式化為 SKILL.md、確保一致性、讓它機器可讀。這個 Skill 處理那 20%，讓使用者可以專注在只有他們能提供的部分。

---

## Composition Hooks 組合接口

- **Input ← skill-self-discovery**: Users who completed self-discovery and want a production Skill flow naturally into skill-builder
  完成自我發現的使用者想要正式 Skill，自然流入 skill-builder
- **Input ← conversation-to-skill**: Users who extracted a rough Skill from a conversation can use skill-builder to refine it
  從對話中提取粗略 Skill 的使用者可以用 skill-builder 精煉它
- **Output → user's workflow**: The saved SKILL.md is immediately installable and executable
  儲存的 SKILL.md 可以立即安裝和執行
- **Output → example skills gallery**: Well-built Skills can be generalized and contributed to the examples collection
  建構良好的 Skills 可以泛化並貢獻到範例集合

---

## Example Session 範例工作階段

Here's a condensed example with a project manager:

以下是一位專案經理的精簡範例：

```
AI:  Let's build a Skill. What's your role?

User: I'm a project manager. I handle government-funded cultural
      projects.
      我是專案經理。我負責政府文化標案。

AI:  Great. What task do you want to turn into a Skill?

User: Writing the monthly progress report for clients. I do it
      every month and it takes forever because I have to collect
      data from everyone.
      寫每月給客戶的進度報告。每個月都要做，花很久因為
      要跟大家收資料。

AI:  That sounds very buildable. Let's give it a name —
     something like "monthly-progress-report"?

User: Yeah, or "月報撰寫" in Chinese.

AI:  Perfect. This sounds like a Process Skill — you follow a
     sequence of steps. Does that fit?

User: Yes, definitely a process.

AI:  What triggers this task? What tells you "it's time to
     write the report"?

User: The 20th of each month. And sometimes the client asks for
      an interim update if there's a big event coming.
      每月20號。有時候大活動前客戶會要求期中報告。

AI:  Got it — calendar trigger plus ad-hoc requests. Any situation
     where you'd skip it?

User: Never skip. Even if there's nothing to report, we still
      submit. Zero progress is still a report.
      不會跳過。就算沒東西報也要交。沒進度也是一份報告。

[... continues through all 7 components ...]

AI:  Here's your Skill — assembled from everything you told me:

     # Monthly Progress Report Writer
     # 月報撰寫

     > *Collect, compile, and deliver the monthly progress report
     > for government cultural project clients.*

     ## Identity
     - Name: monthly-progress-report
     - Type: Process
     - For: Project managers handling government cultural projects

     ## Trigger Conditions
     - 20th of each month (regular)
     - Client requests interim update (ad-hoc)
     - Never skipped — zero progress is still a report

     ## Process Logic
     1. Send data collection reminder to team (by 15th)
     2. Collect activity completion data from team Google Sheet
     3. Collect photos from team shared drive
     4. Calculate KPI achievement rates against contract targets
     5. Write narrative summary per activity (200-300 words)
        - Tone: professional-warm, not bureaucratic
        - Include: what was done, participation numbers, outcomes
     6. Build budget utilization table
        - Cross-reference with accounting system
        - Flag items over 80% utilization
     7. Select 2-3 photos per activity (with bilingual captions)
     8. Write executive summary (under 500 words, written last)
     9. Format using organization Word template
     10. Internal review: send to supervisor for check
     11. Submit to client portal before end of month

     [... remaining components ...]

     Read through this and tell me — anything wrong or missing?

User: Step 6 — I also need to check if any budget items need
      reallocation approval. That's easy to forget.
      步驟6——我還需要檢查有沒有預算項目需要調整核准。
      這很容易忘記。

AI:  Good catch. I'll add that as step 6b:
     "6b. Check for items requiring budget reallocation —
      if found, prepare reallocation request form before
      submitting report"

     Anything else?

User: No, that's perfect. Save it.

AI:  ✅ Saved to monthly-progress-report/SKILL.md

     Want to test it on this month's actual report?
```

---

*Part of the [Agentic Substrate](../../README.md) framework.*
*See also: [Skill Self-Discovery](../skill-self-discovery/SKILL.md) · [Conversation to Skill](../conversation-to-skill/SKILL.md) · [Skill Anatomy](../../docs/01-foundations/skill-anatomy.md)*
