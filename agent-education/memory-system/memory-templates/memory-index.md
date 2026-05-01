# Memory Index

> Routing table for agent memory. Read this first.
> Agent 記憶的路由表。優先讀取這個。
>
> Update this file whenever memory structure changes.
> 記憶結構改變時更新這個檔案。

## Always Read 每次必讀

| File | Purpose | When to read |
|---|---|---|
| `SOUL.md` | Agent identity and principles | Every session start |
| `DAILY.md` | Current project state | Every session start |
| `memory/memory-index.md` | This file — routing table | Every session start |

## Read by Context 按情境讀取

### Decisions 決策

| File | Topic | Date |
|---|---|---|
| `memory/decisions/001-[topic].md` | [Brief description] | [Date] |
| `memory/decisions/002-[topic].md` | [Brief description] | [Date] |

### Facts 事實

| File | Category | Last Updated |
|---|---|---|
| `memory/facts/project.md` | Project metadata | [Date] |
| `memory/facts/environment.md` | Tech stack, configs | [Date] |
| `memory/facts/conventions.md` | Naming, coding conventions | [Date] |

### Session Logs 工作紀錄

| File | Topic | Date |
|---|---|---|
| `memory/sessions/YYYY-MM-DD-[topic].md` | [Brief description] | [Date] |

### Skill Index

| File | Purpose |
|---|---|
| `skill-index.md` | Auto-generated map of all Skills and their relationships |

## Reading Rules 讀取規則

1. **Working on a deliverable?** → Read related decisions + facts
2. **Making a decision?** → Read past decisions on the same topic
3. **Using a Skill?** → Read the SKILL.md + related facts
4. **Starting a new task?** → Read DAILY.md + relevant session logs
5. **Debugging something?** → Read recent session logs + environment facts
