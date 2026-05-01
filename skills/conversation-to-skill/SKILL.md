---
name: conversation-to-skill
description: >
  Analyze a messy LLM conversation and extract it into a structured work record, then reveal it's 80% of a reusable Skill.
  Use when the user says "this conversation is getting messy", "help me organize this chat",
  "I want to save what we've done", "I keep re-explaining the same thing", "turn this into a work record",
  or has been in a long conversation (20+ turns) showing context fatigue.
metadata:
  version: "0.2.0"
  type: "Transform"
  domain: "Productivity / Knowledge Management"
---

# Conversation to Skill
# 對話轉技能

> *Every messy chat contains the seed of a reusable Skill. This Skill finds it.*
> *每一段混亂的對話都包含一個可重用 Skill 的種子。這個 Skill 找到它。*

---

## Identity 身份

- **Name**: conversation-to-skill
- **Type**: Transform (conversation → structured record → Skill)
- **For**: Anyone who has been working with an LLM in a long, messy conversation and wants to capture what they've built — so they never have to re-explain it again.
- **對象**: 任何在一段冗長、混亂的 LLM 對話中工作、想要捕捉他們建立的東西的人——這樣他們再也不需要重新解釋。

---

## Description 描述

Most people's first experience with AI is a long, unstructured conversation. They explain their task, make decisions, iterate on drafts, change direction, and eventually produce something useful. Then the session ends — and all that context, those decisions, that workflow knowledge, is gone.

大多數人與 AI 的第一次體驗是一段冗長、無結構的對話。他們解釋任務、做決策、反覆修改草稿、改變方向，最終產出有用的東西。然後工作階段結束——所有那些脈絡、那些決策、那些工作流程知識，都消失了。

This Skill solves that problem in three phases:

這個 Skill 分三個階段解決這個問題：

1. **Extract**: Analyze the current conversation and pull out the structure that's hiding in the chaos — the task, the decisions, the process, the current state
2. **Organize**: Generate a clean `work-record.md` that captures everything in a structured, reusable format
3. **Reveal**: Show the user that their work record is already 80% of a Skill — and offer to convert it into a proper SKILL.md they can use forever

1. **提取**：分析當前對話，從混亂中拉出隱藏的結構——任務、決策、流程、當前狀態
2. **組織**：生成一份乾淨的 `work-record.md`，以結構化、可重用的格式捕捉一切
3. **揭示**：向使用者展示他們的工作紀錄已經是一個 Skill 的 80%——並提供轉換為正式 SKILL.md 的選項

**The pedagogical arc**: The user starts thinking "I just want to organize this mess." They end up realizing "I just created a reusable AI workflow." The transition happens naturally — no jargon, no pressure.

**教學弧線**：使用者一開始想「我只是想整理這團混亂」。最後他們意識到「我剛剛建立了一個可重用的 AI 工作流程」。轉變自然發生——沒有術語、沒有壓力。

---

## Trigger Conditions 觸發條件

Activate this Skill when the user says things like:

- "This conversation is getting messy, can you help me organize it?"
  「這段對話越來越亂了，你能幫我整理嗎？」
- "I want to save what we've done so I can continue later"
  「我想把我們做的存起來，之後可以繼續」
- "Can you summarize what we've decided?"
  「你能摘要我們決定了什麼嗎？」
- "I keep re-explaining the same thing every session"
  「我每次工作階段都在重複解釋同樣的事」
- "Turn this into a work record"
  「把這個變成工作紀錄」
- "conversation-to-skill" (direct invocation)
- User has been in a long conversation (20+ turns) and is showing signs of context fatigue
  使用者已經在一段長對話（20+ 輪）中，表現出脈絡疲勞的跡象
- User asks how to "not lose" what they've done
  使用者問如何「不遺失」他們做過的東西

---

## Process Logic 流程邏輯

### Phase 1: Analyze the Conversation 分析對話

Silently (without explaining the analysis to the user), scan the entire conversation and extract:

安靜地（不向使用者解釋分析過程），掃描整段對話並提取：

```
Extract:
1. TASK: What is the user trying to accomplish?
   任務：使用者想完成什麼？
   
2. DECISIONS: What choices were made along the way?
   決策：過程中做了哪些選擇？
   (Include: what was decided, why, and what was rejected)
   （包含：決定了什麼、為什麼、以及什麼被拒絕）

3. PROCESS: What steps were followed?
   流程：遵循了什麼步驟？
   (Look for the implicit workflow — the sequence of actions
   that produced the output, even if the user never stated
   it as a "process")
   （尋找隱含的工作流程——產出輸出的動作序列，
   即使使用者從未把它表述為「流程」）

4. CURRENT STATE: Where are we now?
   當前狀態：我們現在在哪裡？
   - What's done ✅
   - What's in progress 🔄
   - What's remaining ⬜
   - What's blocked ❌

5. KEY OUTPUTS: What files, documents, or artifacts were produced?
   關鍵輸出：產出了什麼檔案、文件或產物？

6. PREFERENCES: What quality standards or style preferences
   emerged during the conversation?
   偏好：在對話中浮現了什麼品質標準或風格偏好？
```

### Phase 2: Present the Work Record 呈現工作紀錄

Generate and present a structured work record to the user:

生成並向使用者呈現結構化的工作紀錄：

```
Say to the user (adapt to their language):

"I've analyzed our conversation and organized it into a 
structured work record. Here's what I found:"

「我分析了我們的對話，把它整理成一份結構化的工作紀錄。
這是我發現的：」
```

Then generate the following Markdown structure:

```markdown
# Work Record: [Task Name]
# 工作紀錄：[任務名稱]

## Task 任務
[One-paragraph description of what we're trying to accomplish]

## Decisions Made 已做的決策
| # | Decision 決策 | Rationale 理由 | Date 日期 |
|---|---|---|---|
| 1 | [decision] | [why] | [when in conversation] |
| 2 | ... | ... | ... |

## Process Steps 流程步驟
1. [Step 1]
2. [Step 2]
3. ...

## Current Status 當前狀態
- ✅ [Completed items]
- 🔄 [In progress items]
- ⬜ [Remaining items]

## Outputs Produced 已產出的輸出
- [File/artifact 1]: [description]
- [File/artifact 2]: [description]

## Quality Standards 品質標準
- [Preference 1 discovered during conversation]
- [Preference 2]

## Next Steps 下一步
1. [What should happen next]
2. [Then what]
```

**Critical rule**: Use the user's own words. Don't "improve" their language or add jargon. If they said "check if the numbers match," write that — not "perform data reconciliation."

**關鍵規則**：使用使用者自己的話。不要「改善」他們的語言或加入術語。如果他們說「檢查數字是不是對得上」，就寫那個——不是「執行資料調節」。

### Phase 3: The Reveal — "This Is Already a Skill" 揭示——「這已經是一個 Skill 了」

After the user has reviewed and confirmed the work record is accurate:

在使用者審查並確認工作紀錄準確之後：

```
Say to the user:

"Notice something? This work record has everything a 
reusable AI Skill needs:

- A clear task description → That's the Skill's Identity
- When to start → That's the Trigger
- The steps you followed → That's the Process Logic
- How to check the work → That's the Validation
- What you need and produce → That's the I/O Contract

You didn't just organize a conversation. 
You wrote 80% of a Skill.

Want me to convert this into a proper SKILL.md file 
that you can use in any future session?"

「注意到了嗎？這份工作紀錄已經有一個可重用的 AI Skill 
所需的一切：

- 清楚的任務描述 → 那就是 Skill 的身份
- 何時開始 → 那就是觸發條件
- 你遵循的步驟 → 那就是流程邏輯
- 如何檢查工作 → 那就是驗證
- 你需要什麼和產出什麼 → 那就是 I/O 合約

你不只是整理了一段對話。
你寫了一個 Skill 的 80%。

要我把這個轉換成正式的 SKILL.md 檔案，
讓你在任何未來的工作階段都能使用嗎？」
```

### Phase 4: Convert (Optional) 轉換（可選）

If the user says yes, convert the work record into a proper SKILL.md using the seven-component format from [Skill Anatomy](../../docs/01-foundations/skill-anatomy.md). For more advanced construction, see [[skill-builder]]:

如果使用者同意，使用[技能解剖學](../../docs/01-foundations/skill-anatomy.md)的七組件格式將工作紀錄轉換為正式的 SKILL.md：

```markdown
# [Skill Name]

## Identity 身份
- Name: [derived from task]
- Type: [Process / Transform / Data / Integration / Orchestration]
- For: [who benefits]

## Description 描述
[From the Task section of the work record]

## Trigger Conditions 觸發條件
[Derived from when/why the user started this work]

## Process Logic 流程邏輯
[The Process Steps from the work record, refined into
clear instructions an LLM can follow]

## I/O Contract 輸入輸出合約
### Input 輸入
[What the Skill needs to start]
### Output 輸出
[What the Skill produces when done]

## Validation Rules 驗證規則
[From the Quality Standards section, converted into
checkable criteria]

## Knowledge 知識
[Any domain-specific knowledge, preferences, or institutional
requirements that emerged during the conversation]
```

After generating, offer:

生成之後，提供選項：

```
"Here's your SKILL.md. You have three options:

(A) Save it — I'll write it to a file you can install
    in Claude Code or Cowork
(B) Test it — Let's try using the Skill right now on a 
    new task to see if it works
(C) Refine it — Let's improve specific sections together

Which would you like?"

「這是你的 SKILL.md。你有三個選項：

(A) 儲存它——我會寫成一個檔案，你可以安裝到 
    Claude Code 或 Cowork
(B) 測試它——讓我們現在就用這個 Skill 在新任務上
    試試看它是否有效
(C) 改善它——讓我們一起改進特定的部分

你想要哪個？」
```

---

## Validation Rules 驗證規則

The Skill execution is successful when:

Skill 執行成功的條件：

1. **Extraction is complete**: All six elements (Task, Decisions, Process, State, Outputs, Preferences) are captured from the conversation. None are fabricated. 六個要素全部從對話中捕捉，沒有捏造。
2. **User's words are preserved**: The work record uses the user's vocabulary, not technical jargon. 工作紀錄使用使用者的詞彙，不用技術術語。
3. **User confirms accuracy**: The user agrees the work record reflects what actually happened. 使用者同意工作紀錄反映了實際發生的事。
4. **The reveal lands**: The user has an "aha" moment — they see the connection between their work record and a Skill ([[skill-self-discovery]] teaches this same pattern). 使用者有「啊哈」的時刻——看到工作紀錄和 Skill 之間的連結。
5. **If converted**: The SKILL.md follows the seven-component format and is immediately usable. 如果轉換了，SKILL.md 遵循七組件格式且可立即使用。

---

## Knowledge 知識

### What makes a good work record 什麼是好的工作紀錄

- **Specific, not generic**: "Review the monthly expense report for miscategorized items over NT$5,000" beats "Review financial documents" 具體而非泛泛
- **Decision-aware**: Captures not just what was done, but why — and what was considered but rejected 捕捉不只做了什麼，還有為什麼——以及考慮過但被拒絕的
- **State-aware**: Clearly marks what's done vs. what's remaining 清楚標記完成和待完成的
- **Process-honest**: Records the actual steps taken, including backtracking and corrections — not an idealized linear path 記錄實際採取的步驟，包括回溯和修正——不是理想化的直線路徑

### Common conversation patterns to look for 常見的對話模式

- **The pivot**: "Actually, let's try a different approach" → Decision record 「其實，我們試試不同的方法」→ 決策紀錄
- **The preference**: "I like this format better" → Quality standard 「我比較喜歡這個格式」→ 品質標準
- **The correction**: "No, that's not right, it should be..." → Refined process step 「不對，不是那樣，應該是...」→ 改進的流程步驟
- **The validation**: "Let me check... yes, that looks correct" → Validation criteria 「讓我檢查... 是的，那看起來正確」→ 驗證標準
- **The scope boundary**: "We don't need to include X" → Skill boundary 「我們不需要包含 X」→ Skill 邊界

### Connection to the framework 與框架的連結

This Skill implements the transition from **Level 1 (Conversation)** to **Level 3 (Skill Building)** described in the [Learning Path](../../docs/04-curriculum/learning-path.md). It's the bridge that takes unstructured chat and transforms it into structured, reusable expertise.

這個 Skill 實現了[學習路徑](../../docs/04-curriculum/learning-path.md)中描述的從 **Level 1（對話）** 到 **Level 3（技能建構）** 的轉變。它是將非結構化的對話轉化為結構化、可重用專業知識的橋樑。

---

## Example: What the Output Looks Like 範例：輸出長什麼樣

### Input: A messy 30-turn conversation about writing a project report 輸入：一段關於撰寫專案報告的混亂 30 輪對話

### Output: Work Record 輸出：工作紀錄

```markdown
# Work Record: Quarterly Project Report for Client X
# 工作紀錄：X 客戶的季度專案報告

## Task 任務
Write a quarterly progress report for the city government 
cultural affairs project. Must cover: activities completed, 
budget utilization, KPI achievement, and next quarter plan.

## Decisions Made 已做的決策
| # | Decision | Rationale |
|---|---|---|
| 1 | Use narrative format, not bullet points | Client prefers reading prose; previous bullet-point reports got low satisfaction scores |
| 2 | Include photos from events | Client specifically asked; budget allows 2 pages of photos |
| 3 | Put budget table in appendix, not main body | Main body focuses on outcomes; detailed financials in appendix |

## Process Steps 流程步驟
1. Collect activity data from team Google Sheet
2. Calculate KPI achievement rates
3. Write narrative summary for each activity (200-300 words)
4. Select representative photos (2-3 per activity)
5. Build budget utilization table
6. Write executive summary (last, after all sections done)
7. Format in Word with organization template
8. Internal review before submission

## Current Status 當前狀態
- ✅ Activity data collected
- ✅ KPI calculations done
- ✅ Narrative for activities 1-3 written
- 🔄 Narrative for activities 4-6 in progress
- ⬜ Photo selection
- ⬜ Budget table
- ⬜ Executive summary
- ⬜ Formatting and review

## Quality Standards 品質標準
- Narrative tone: professional but warm, not bureaucratic
- All numbers must be cross-referenced with the Google Sheet
- Photos must have captions in both Chinese and English
- Executive summary under 500 words
```

### After Reveal: The same content, converted to SKILL.md

```markdown
# Quarterly Report Writer

## Identity
- Name: quarterly-report-writer
- Type: Process
- For: Project managers writing government progress reports

## Trigger Conditions
- "Write the quarterly report"
- "It's reporting season"
- End of quarter approaching

## Process Logic
1. Read activity data source (Google Sheet or equivalent)
2. Calculate KPI achievement rates against targets
3. Write narrative summary per activity (200-300 words, 
   professional-warm tone, not bureaucratic)
4. Select 2-3 representative photos per activity
5. Build budget utilization table (appendix format)
6. Write executive summary (under 500 words, written last)
7. Format using organization Word template
8. Run internal review checklist

## Validation Rules
- All numbers cross-referenced with data source
- Photo captions bilingual (ZH-TW + EN)
- Executive summary ≤ 500 words
- Narrative tone check: no bureaucratic language
- Budget table totals match source data
```

---

## Related Skills

- [[skill-self-discovery]] — Guided discovery that reveals users already possess every component needed to build a Skill
- [[skill-builder]] — Deliberately construct a production-quality SKILL.md from scratch with guided questions

*Related: [Skill Self-Discovery](../skill-self-discovery/SKILL.md) · [You Already Know](../../docs/04-curriculum/you-already-know.md) · [Learning Path](../../docs/04-curriculum/learning-path.md)*
