## scripts/

Automation scripts for Agentic Substrate.

### skill-index.py

Scans all `SKILL.md` files, extracts YAML frontmetadata AND `[[wikilinks]]` from body content, and generates `skill-index.md` with a relationship graph.

```bash
python3 scripts/skill-index.py
```

### skill-rag.py

Searches Skills by keyword and outputs prompt-ready context for LLMs. Like `taiwanmd rag` for Skills.

```bash
# Basic search
python3 scripts/skill-rag.py "document review"

# Limit results
python3 scripts/skill-rag.py "meeting notes" --limit 2

# JSON output for programmatic use
python3 scripts/skill-rag.py "accounting" --json

# Pipe to LLM
python3 scripts/skill-rag.py "research" | llm "summarize"
```

## Integration

Both scripts reference:
- `agent-education/memory-system/memory-protocol.md` — memory routing
- `agent-education/decision-patterns/pattern-matrix.md` — pattern selection
- `agent-education/skill-system/skill-creation-protocol.md` — new Skill creation
