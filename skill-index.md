# Skill Index
### Agent 可查詢的 Skill 地圖

> Auto-generated on 2026-05-02 00:47
> 於 2026-05-02 00:47 自動產生
>
> Do not edit manually. Run `python3 scripts/skill-index.py` to regenerate.
> 不要手動編輯。執行 `python3 scripts/skill-index.py` 重新產生。

---

## Summary 摘要

- **Total Skills**: 9
- **Relationships**: 0 bidirectional

## Quick Lookup 快速查找

| Name 名稱 | Type 類型 | Domain 領域 | Path 路徑 |
|---|---|---|---|
| `conversation-to-skill` | Transform | Productivity / Knowledge Management | `skills/conversation-to-skill/SKILL.md` |
| `accounting-reconciler` | Transform | Accounting / Finance | `skills/examples/accounting-reconciler/SKILL.md` |
| `content-pipeline` | Process | Marketing / Content | `skills/examples/content-pipeline/SKILL.md` |
| `document-reviewer` | Process | Administration / Quality | `skills/examples/document-reviewer/SKILL.md` |
| `meeting-notes-to-actions` | Transform | General / Productivity | `skills/examples/meeting-notes-to-actions/SKILL.md` |
| `project-status-tracker` | Orchestration | Project Management | `skills/examples/project-status-tracker/SKILL.md` |
| `research-and-summarize` | Process | Research / Analysis | `skills/examples/research-and-summarize/SKILL.md` |
| `skill-builder` | Process | Skill Creation | `skills/skill-builder/SKILL.md` |
| `skill-self-discovery` | Process | Learning / Onboarding | `skills/skill-self-discovery/SKILL.md` |

## Detailed Listings 詳細列表

### conversation-to-skill

> >

- **Path**: `skills/conversation-to-skill/SKILL.md`
- **Type**: Transform
- **Domain**: Productivity / Knowledge Management
- **Version**: 0.2.0

### accounting-reconciler

> >

- **Path**: `skills/examples/accounting-reconciler/SKILL.md`
- **Type**: Transform
- **Domain**: Accounting / Finance
- **Version**: 0.2.0

### content-pipeline

> >

- **Path**: `skills/examples/content-pipeline/SKILL.md`
- **Type**: Process
- **Domain**: Marketing / Content
- **Version**: 0.2.0

### document-reviewer

> >

- **Path**: `skills/examples/document-reviewer/SKILL.md`
- **Type**: Process
- **Domain**: Administration / Quality
- **Version**: 0.2.0

### meeting-notes-to-actions

> >

- **Path**: `skills/examples/meeting-notes-to-actions/SKILL.md`
- **Type**: Transform
- **Domain**: General / Productivity
- **Version**: 0.2.0

### project-status-tracker

> >

- **Path**: `skills/examples/project-status-tracker/SKILL.md`
- **Type**: Orchestration
- **Domain**: Project Management
- **Version**: 0.2.0

### research-and-summarize

> >

- **Path**: `skills/examples/research-and-summarize/SKILL.md`
- **Type**: Process
- **Domain**: Research / Analysis
- **Version**: 0.2.0

### skill-builder

> >

- **Path**: `skills/skill-builder/SKILL.md`
- **Type**: Process
- **Domain**: Skill Creation
- **Version**: 0.2.0

### skill-self-discovery

> >

- **Path**: `skills/skill-self-discovery/SKILL.md`
- **Type**: Process
- **Domain**: Learning / Onboarding
- **Version**: 0.2.0

---

## Skill Relationship Graph
### Skill 關聯圖

No relationships detected between Skills.
尚未偵測到 Skill 之間的關聯。
---

## Agent Query Protocol - Agent 查詢協議

To find relevant Skills for a task:

```yaml
step_1: Read this file (skill-index.md)
step_2: Match task keywords to Skill names, types, or domains
step_3: Check Related / Depends on / Reuses for connected Skills
step_4: Read the matched SKILL.md for full definition
step_5: Load only the Skills needed (Tier 0 → Tier 2)
```

## Integration With Memory Protocol - 與記憶協議整合

This file is referenced by:

- `agent-education/memory-system/memory-protocol.md` — as part of session start routing
- `agent-education/decision-patterns/pattern-matrix.md` — for Skill-based routing decisions
- `agent-education/skill-system/skill-creation-protocol.md` — to check existing Skills before creating new ones
