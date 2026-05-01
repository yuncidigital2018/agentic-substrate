# Scripts

Automation scripts for Agentic Substrate.

## skill-index.py

Scans all `SKILL.md` files in the repo, extracts YAML frontmetadata, and generates `skill-index.md` — a human and agent-readable map of all Skills and their relationships.

掃描 repo 中所有 `SKILL.md` 檔案，提取 YAML frontmatter 元資料，並產生 `skill-index.md`——一份人類和 Agent 都可讀的 Skill 地圖和關聯圖。

### Usage 使用方式

```bash
# From repo root
python3 scripts/skill-index.py

# Specify a different repo root
python3 scripts/skill-index.py --repo-root /path/to/repo

# Specify a different output path
python3 scripts/skill-index.py --output custom-index.md
```

### What It Does 做什麼

1. Recursively finds all `SKILL.md` files
2. Extracts YAML frontmatter (name, description, type, domain, version, related_skills, depends_on, reuses)
3. Builds a relationship graph between Skills
4. Generates `skill-index.md` with:
   - Quick lookup table
   - Detailed listings with metadata
   - Text-based relationship graph
   - Agent query protocol

### When to Run 何時執行

- After adding a new Skill
- After modifying a Skill's frontmatter metadata
- Before committing changes to the `skills/` directory
- As part of CI/CD (optional)

### Integration 整合

The generated `skill-index.md` is referenced by:
- `agent-education/memory-system/memory-protocol.md` — session start routing
- `agent-education/decision-patterns/pattern-matrix.md` — Skill-based routing
- `agent-education/skill-system/skill-creation-protocol.md` — duplicate detection
