#!/usr/bin/env python3
"""
Skill Index Generator
Skill 索引產生器

Scans all SKILL.md files in a repository, extracts YAML frontmatter metadata,
scans markdown body for [[wikilink]] references, and generates a skill-index.md
with relationships and a text-based graph.

掃描 repo 中所有 SKILL.md 檔案，提取 YAML frontmatter 元資料，
掃描 markdown 內文中的 [[wikilink]] 引用，
並產生包含關聯和文字圖的 skill-index.md。

Usage:
    python3 scripts/skill-index.py [--repo-root /path/to/repo] [--output skill-index.md]

Output:
    - skill-index.md: Human and agent-readable skill map
    - Console: Summary of skills found
"""

import os
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from a Markdown file."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}

    metadata = {}
    current_key = None
    for line in match.group(1).split('\n'):
        line = line.rstrip()
        if not line or line.startswith('#'):
            continue

        # Top-level key: value
        key_match = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if key_match:
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            if value:
                metadata[current_key] = value.strip('"').strip("'")
            continue

        # Nested key under metadata
        nested_match = re.match(r'^\s+(\w[\w-]*):\s*(.*)', line)
        if nested_match and current_key:
            nested_key = nested_match.group(1)
            nested_value = nested_match.group(2).strip()
            if current_key not in metadata:
                metadata[current_key] = {}
            if isinstance(metadata[current_key], dict):
                metadata[current_key][nested_key] = nested_value.strip('"').strip("'")

    return metadata


def extract_description(content: str) -> str:
    """Extract the first non-frontmatter paragraph as description."""
    # Skip frontmatter
    match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    if match:
        content = content[match.end():]

    # Find first non-empty, non-header line
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('>') and not line.startswith('---'):
            return line[:120]

    return ''


def extract_wikilinks(content: str) -> list:
    """Extract [[wikilink]] references from markdown body text.

    Supports [[target]], [[target#anchor]], and [[target|display text]] formats.
    Returns the target part (before | or #) for each wikilink.
    """
    # Match [[target]] or [[target#anchor]] or [[target|display text]] or [[target#anchor|display]]
    matches = re.findall(r'\[\[([^\]|]+?)(?:#[^\]]*?)?(?:\|[^\]]+?)?\]\]', content)
    seen = set()
    result = []
    for m in matches:
        m = m.strip()
        if m not in seen:
            seen.add(m)
            result.append(m)
    return result


def find_skills(repo_root: Path) -> list:
    """Find all SKILL.md files and extract their metadata."""
    skills = []

    for skill_path in sorted(repo_root.rglob('SKILL.md')):
        # Skip node_modules, .git, etc.
        if any(part.startswith('.') for part in skill_path.parts):
            continue
        if 'node_modules' in str(skill_path):
            continue

        try:
            content = skill_path.read_text(encoding='utf-8')
        except Exception:
            continue

        metadata = parse_frontmatter(content)
        relative_path = skill_path.relative_to(repo_root)
        skill_dir = relative_path.parent

        # Extract body content (everything after frontmatter)
        fm_match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
        body_content = content[fm_match.end():] if fm_match else content

        # Extract wikilinks from body content
        body_wikilinks = extract_wikilinks(body_content)

        # Extract relationships from metadata
        related = metadata.get('metadata', {})
        if isinstance(related, dict):
            related_skills = related.get('related_skills', '')
            depends_on = related.get('depends_on', '')
            reuses = related.get('reuses', '')
        else:
            related_skills = ''
            depends_on = ''
            reuses = ''

        skill_info = {
            'name': metadata.get('name', skill_dir.name),
            'description': metadata.get('description', extract_description(content)),
            'version': metadata.get('metadata', {}).get('version', '') if isinstance(metadata.get('metadata'), dict) else '',
            'type': metadata.get('metadata', {}).get('type', '') if isinstance(metadata.get('metadata'), dict) else '',
            'domain': metadata.get('metadata', {}).get('domain', '') if isinstance(metadata.get('metadata'), dict) else '',
            'path': str(relative_path),
            'dir': str(skill_dir),
            'related_skills': [s.strip() for s in related_skills.split(',') if s.strip()] if related_skills else [],
            'depends_on': [s.strip() for s in depends_on.split(',') if s.strip()] if depends_on else [],
            'reuses': [s.strip() for s in reuses.split(',') if s.strip()] if reuses else [],
            'body_wikilinks': body_wikilinks,
        }
        skills.append(skill_info)

    return skills


def build_relationship_graph(skills: list) -> dict:
    """Build a graph of skill relationships."""
    graph = defaultdict(set)
    skill_names = {s['name'] for s in skills}

    for skill in skills:
        for related in skill['related_skills']:
            if related in skill_names:
                graph[skill['name']].add(related)
                graph[related].add(skill['name'])
        for dep in skill['depends_on']:
            if dep in skill_names:
                graph[skill['name']].add(dep)
        for reuse in skill['reuses']:
            if reuse in skill_names:
                graph[skill['name']].add(reuse)
                graph[reuse].add(skill['name'])
        for wikilink in skill.get('body_wikilinks', []):
            if wikilink in skill_names:
                graph[skill['name']].add(wikilink)
                graph[wikilink].add(skill['name'])

    return graph


def render_text_graph(skills: list, graph: dict) -> str:
    """Render a simple text-based relationship graph."""
    lines = []
    lines.append('## Skill Relationship Graph')
    lines.append('### Skill 關聯圖')
    lines.append('')

    if not graph:
        lines.append('No relationships detected between Skills.')
        lines.append('尚未偵測到 Skill 之間的關聯。')
        return '\n'.join(lines)

    # Group connected components
    visited = set()
    components = []

    for skill_name in graph:
        if skill_name in visited:
            continue
        component = set()
        queue = [skill_name]
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            component.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        if len(component) > 1:
            components.append(sorted(component))

    if not components:
        lines.append('All Skills are independent (no cross-references).')
        lines.append('所有 Skill 都是獨立的（沒有互相引用）。')
    else:
        for i, component in enumerate(components, 1):
            lines.append(f'### Cluster {i}')
            lines.append('```')
            for name in component:
                connections = graph.get(name, set())
                lines.append(f'  {name}')
                for conn in sorted(connections):
                    lines.append(f'    └──> {conn}')
            lines.append('```')
            lines.append('')

    return '\n'.join(lines)


def generate_index(skills: list, graph: dict) -> str:
    """Generate the complete skill-index.md content."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    lines = []
    lines.append('# Skill Index')
    lines.append('### Agent 可查詢的 Skill 地圖')
    lines.append('')
    lines.append(f'> Auto-generated on {now}')
    lines.append(f'> 於 {now} 自動產生')
    lines.append('>')
    lines.append('> Do not edit manually. Run `python3 scripts/skill-index.py` to regenerate.')
    lines.append('> 不要手動編輯。執行 `python3 scripts/skill-index.py` 重新產生。')
    lines.append('')
    lines.append('---')
    lines.append('')

    # Summary
    lines.append(f'## Summary 摘要')
    lines.append('')
    lines.append(f'- **Total Skills**: {len(skills)}')
    lines.append(f'- **Relationships**: {sum(len(v) for v in graph.values()) // 2} bidirectional')
    lines.append('')

    # Quick lookup table
    lines.append('## Quick Lookup 快速查找')
    lines.append('')
    lines.append('| Name 名稱 | Type 類型 | Domain 領域 | Path 路徑 |')
    lines.append('|---|---|---|---|')
    for skill in skills:
        name = skill['name']
        stype = skill['type'] or '-'
        domain = skill['domain'] or '-'
        path = skill['path']
        lines.append(f'| `{name}` | {stype} | {domain} | `{path}` |')
    lines.append('')

    # Detailed listings
    lines.append('## Detailed Listings 詳細列表')
    lines.append('')
    for skill in skills:
        lines.append(f'### {skill["name"]}')
        lines.append('')
        if skill['description']:
            # Truncate long descriptions
            desc = skill['description']
            if len(desc) > 200:
                desc = desc[:200] + '...'
            lines.append(f'> {desc}')
            lines.append('')
        lines.append(f'- **Path**: `{skill["path"]}`')
        if skill['type']:
            lines.append(f'- **Type**: {skill["type"]}')
        if skill['domain']:
            lines.append(f'- **Domain**: {skill["domain"]}')
        if skill['version']:
            lines.append(f'- **Version**: {skill["version"]}')
        if skill['related_skills']:
            lines.append(f'- **Related**: {", ".join("`" + s + "`" for s in skill["related_skills"])}')
        if skill['depends_on']:
            lines.append(f'- **Depends on**: {", ".join("`" + s + "`" for s in skill["depends_on"])}')
        if skill['reuses']:
            lines.append(f'- **Reuses**: {", ".join("`" + s + "`" for s in skill["reuses"])}')
        if skill.get('body_wikilinks'):
            lines.append(f'- **Body Wikilinks**: {", ".join("`" + s + "`" for s in skill["body_wikilinks"])}')
        lines.append('')

    # Relationship graph
    lines.append('---')
    lines.append('')
    lines.append(render_text_graph(skills, graph))

    # Agent query protocol
    lines.append('---')
    lines.append('')
    lines.append('## Agent Query Protocol - Agent 查詢協議')
    lines.append('')
    lines.append('To find relevant Skills for a task:')
    lines.append('')
    lines.append('```yaml')
    lines.append('step_1: Read this file (skill-index.md)')
    lines.append('step_2: Match task keywords to Skill names, types, or domains')
    lines.append('step_3: Check Related / Depends on / Reuses for connected Skills')
    lines.append('step_4: Read the matched SKILL.md for full definition')
    lines.append('step_5: Load only the Skills needed (Tier 0 → Tier 2)')
    lines.append('```')
    lines.append('')
    lines.append('## Integration With Memory Protocol - 與記憶協議整合')
    lines.append('')
    lines.append('This file is referenced by:')
    lines.append('')
    lines.append('- `agent-education/memory-system/memory-protocol.md` — as part of session start routing')
    lines.append('- `agent-education/decision-patterns/pattern-matrix.md` — for Skill-based routing decisions')
    lines.append('- `agent-education/skill-system/skill-creation-protocol.md` — to check existing Skills before creating new ones')
    lines.append('')

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate skill-index.md from SKILL.md files')
    parser.add_argument('--repo-root', type=str, default='.',
                        help='Root directory of the repository (default: current directory)')
    parser.add_argument('--output', type=str, default=None,
                        help='Output file path (default: [repo-root]/skill-index.md)')
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output_path = Path(args.output) if args.output else repo_root / 'skill-index.md'

    if not repo_root.exists():
        print(f'Error: Repository root not found: {repo_root}', file=sys.stderr)
        sys.exit(1)

    print(f'Scanning for SKILL.md files in: {repo_root}')
    skills = find_skills(repo_root)

    if not skills:
        print('No SKILL.md files found.')
        sys.exit(0)

    print(f'Found {len(skills)} Skills:')
    for skill in skills:
        print(f'  - {skill["name"]} ({skill["path"]})')

    graph = build_relationship_graph(skills)
    index_content = generate_index(skills, graph)

    output_path.write_text(index_content, encoding='utf-8')
    print(f'\nGenerated: {output_path}')


if __name__ == '__main__':
    main()
