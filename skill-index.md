# Skill Index
### Agent 可查詢的 Skill 地圖

> Auto-generated on 2026-05-02 01:27
> 於 2026-05-02 01:27 自動產生
>
> Do not edit manually. Run `python3 scripts/skill-index.py` to regenerate.
> 不要手動編輯。執行 `python3 scripts/skill-index.py` 重新產生。

---

## Summary 摘要

- **Total Skills**: 9
- **Relationships**: 15 bidirectional

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
- **Body Wikilinks**: `skill-builder`, `skill-self-discovery`

### accounting-reconciler

> >

- **Path**: `skills/examples/accounting-reconciler/SKILL.md`
- **Type**: Transform
- **Domain**: Accounting / Finance
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `document-reviewer`

### content-pipeline

> >

- **Path**: `skills/examples/content-pipeline/SKILL.md`
- **Type**: Process
- **Domain**: Marketing / Content
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `research-and-summarize`, `document-reviewer`

### document-reviewer

> >

- **Path**: `skills/examples/document-reviewer/SKILL.md`
- **Type**: Process
- **Domain**: Administration / Quality
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `content-pipeline`

### meeting-notes-to-actions

> >

- **Path**: `skills/examples/meeting-notes-to-actions/SKILL.md`
- **Type**: Transform
- **Domain**: General / Productivity
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `project-status-tracker`

### project-status-tracker

> >

- **Path**: `skills/examples/project-status-tracker/SKILL.md`
- **Type**: Orchestration
- **Domain**: Project Management
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `meeting-notes-to-actions`, `document-reviewer`

### research-and-summarize

> >

- **Path**: `skills/examples/research-and-summarize/SKILL.md`
- **Type**: Process
- **Domain**: Research / Analysis
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `content-pipeline`, `document-reviewer`

### skill-builder

> >

- **Path**: `skills/skill-builder/SKILL.md`
- **Type**: Process
- **Domain**: Skill Creation
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-self-discovery`, `conversation-to-skill`

### skill-self-discovery

> >

- **Path**: `skills/skill-self-discovery/SKILL.md`
- **Type**: Process
- **Domain**: Learning / Onboarding
- **Version**: 0.2.0
- **Body Wikilinks**: `skill-builder`, `conversation-to-skill`

---

## Skill Relationship Graph
### Skill 關聯圖

### Cluster 1
```
  accounting-reconciler
    └──> document-reviewer
    └──> skill-builder
  content-pipeline
    └──> document-reviewer
    └──> research-and-summarize
    └──> skill-builder
  conversation-to-skill
    └──> skill-builder
    └──> skill-self-discovery
  document-reviewer
    └──> accounting-reconciler
    └──> content-pipeline
    └──> project-status-tracker
    └──> research-and-summarize
    └──> skill-builder
  meeting-notes-to-actions
    └──> project-status-tracker
    └──> skill-builder
  project-status-tracker
    └──> document-reviewer
    └──> meeting-notes-to-actions
    └──> skill-builder
  research-and-summarize
    └──> content-pipeline
    └──> document-reviewer
    └──> skill-builder
  skill-builder
    └──> accounting-reconciler
    └──> content-pipeline
    └──> conversation-to-skill
    └──> document-reviewer
    └──> meeting-notes-to-actions
    └──> project-status-tracker
    └──> research-and-summarize
    └──> skill-self-discovery
  skill-self-discovery
    └──> conversation-to-skill
    └──> skill-builder
```

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
