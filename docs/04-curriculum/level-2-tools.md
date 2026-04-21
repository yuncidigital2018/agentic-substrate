# Level 2: Tool Use — From Thinking to Doing
# Level 2：工具使用——從想到做

> *"AI that can think is interesting. AI that can think AND act is transformative."*
> *「能想的 AI 很有趣。能想又能做的 AI 是革命性的。」*

---

## What This Level Covers 這一級涵蓋什麼

At Level 1, AI was a conversation partner. At Level 2, AI becomes a **capable assistant** — it can read your files, write documents, run calculations, search the web, and interact with external systems. The output is no longer chat text; it's real deliverables.

在 Level 1，AI 是一個對話夥伴。在 Level 2，AI 變成一個**有能力的助手**——它能讀你的檔案、寫文件、執行計算、搜尋網路、與外部系統互動。輸出不再是聊天文字；而是真正的交付物。

---

## The Tools That Change Everything 改變一切的工具

### File Operations 檔案操作

The single most impactful upgrade: AI that can read and write your actual files.

最有影響力的升級：AI 能讀寫你的實際檔案。

- "Read this spreadsheet and calculate the quarterly totals" 「讀取這份試算表並計算季度總計」
- "Write a summary report as a Word document" 「寫一份摘要報告成 Word 文件」
- "Compare these two PDFs and list the differences" 「比較這兩份 PDF 並列出差異」

### Code Execution 程式碼執行

Even if you don't write code, AI running code on your behalf is powerful:

即使你不寫程式，AI 代你執行程式碼也很強大：

- "Parse this CSV and create a chart showing the monthly trend" 「解析這份 CSV 並建立一個顯示月趨勢的圖表」
- "Calculate the compound interest on this loan scenario" 「計算這個貸款方案的複利」
- "Convert this data from one format to another" 「把這些資料從一種格式轉換成另一種」

### Web Access 網路存取

AI that can search and retrieve current information:

能搜尋和檢索當前資訊的 AI：

- "Search for the latest regulations on data privacy in Taiwan" 「搜尋台灣最新的資料隱私法規」
- "Find the current exchange rate and convert this budget" 「找到目前的匯率並轉換這份預算」

### External Services (MCP) 外部服務

Through MCP (Model Context Protocol), AI connects to external tools:

透過 MCP（模型上下文協議），AI 連接到外部工具：

- Slack: "Read the latest messages in #project-updates" 讀取 #project-updates 的最新訊息
- GitHub: "Show me the open pull requests" 顯示待處理的 pull requests
- Asana/Jira: "What tasks are assigned to me?" 什麼任務指派給我？
- Google Drive: "Find the latest version of the budget spreadsheet" 找到預算試算表的最新版本

---

## Where to Access Level 2 在哪裡使用 Level 2

| Product 產品 | What It Offers 提供什麼 | Best For 最適合 |
|---|---|---|
| **Claude Code** | Full tool access via CLI. Files, code, web, MCP. | Engineers, power users 工程師、進階使用者 |
| **Cowork** | Desktop app with file access and MCP. No CLI needed. | Non-engineers, knowledge workers 非工程師、知識工作者 |
| **Cursor** | IDE-integrated AI with code and file tools. | Developers 開發者 |
| **Claude.ai + Artifacts** | Basic file handling and code execution in browser. | Quick tasks 快速任務 |

---

## Practical Patterns 實用模式

### The "Read → Analyze → Produce" Pattern 讀取→分析→產出

The most common Level 2 workflow:

1. Give AI a source file (spreadsheet, document, data export)
2. Ask it to analyze specific aspects
3. Have it produce a deliverable (report, chart, summary, email)

Example: "Read this sales data CSV. Calculate month-over-month growth for each product line. Create a summary table and highlight any product lines that declined more than 10%."

### The "Multi-Source Synthesis" Pattern 多來源綜合

Combine information from different files:

- "Read the project plan, the latest meeting notes, and the budget spreadsheet. Give me a status update that covers all three."

### The "Transform" Pattern 轉換

Convert between formats or structures:

- "Read this Chinese contract and produce an English summary of the key terms, obligations, and deadlines in table format."

---

## Exercises 練習

### Exercise 1: The File Upgrade 檔案升級

Take a task you normally do by manually reading a document and writing a response. Instead, give the document to AI (Cowork or Claude Code) and have it read the actual file, process it, and produce the output as a saved file. Compare the experience.

### Exercise 2: The Automation Candidate 自動化候選

Identify one task where you currently: (a) open a file, (b) look for specific things, (c) produce a deliverable. Try having AI do all three steps in one interaction. If it works, you've found your first Skill candidate for Level 3.

### Exercise 3: The MCP Connection MCP 連線

If you use Cowork, connect one external tool (Slack, Google Drive, or a project tracker). Ask AI to fetch real data from it. The moment AI reads your actual work context — not something you pasted — is the Level 2 breakthrough.

---

## The Friction Point 摩擦點

Level 2 is the only level where **technical setup** is sometimes required. You might need to install software, configure connections, or navigate settings. This can be frustrating for non-engineers.

Level 2 是唯一一個有時需要**技術設置**的級別。你可能需要安裝軟體、設定連線或操作設定。這對非工程師可能令人沮喪。

Two things to know 兩件事要知道:

1. **You only set up once.** Once configured, tools work automatically in every future session. The setup cost is one-time; the benefit is permanent.
   你只需要設置一次。一旦配置好，工具在每個未來的工作階段自動運作。

2. **The industry is actively lowering this barrier.** Products like Cowork are specifically designed to give Level 2 capabilities with minimal setup. What required a terminal command last year now requires a button click.
   業界正積極降低這個門檻。像 Cowork 這樣的產品專門設計來用最少的設置提供 Level 2 能力。

---

## When You've Outgrown Level 2 當你超越 Level 2 的時候

You'll know it's time for Level 3 when:

- You keep giving the same instructions for the same task 你一直對同一個任務給同樣的指示
- The output is close but doesn't follow your organization's specific process 輸出很接近但不遵循你組織的特定流程
- You want to share a workflow with colleagues but can't 你想跟同事分享一個工作流程但做不到
- You realize the **process** is more valuable than any single output 你意識到**流程**比任何單一輸出更有價值

These are signals that you need **Skills** — reusable, shareable workflow definitions. That's [Level 3](level-3-skills.md).

---

*Previous: [Level 1: Conversation ←](level-1-conversation.md)*
*Next: [Level 3: Skill Building →](level-3-skills.md)*
