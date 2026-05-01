#!/usr/bin/env python3
"""
Skill RAG — Retrieval-Augmented Generation for Skills
Skill RAG — 為 Skill 做 RAG 檢索

Searches Skills by keyword and outputs prompt-ready context for LLMs.
Like taiwanmd rag, but for Skills.

Usage:
    python3 scripts/skill-rag.py "document review"
    python3 scripts/skill-rag.py "meeting notes" --limit 2
    python3 scripts/skill-rag.py "accounting" --json
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path


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

        key_match = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if key_match:
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            if value:
                metadata[current_key] = value.strip('"').strip("'")
            continue

        nested_match = re.match(r'^\s+(\w[\w-]*):\s*(.*)', line)
        if nested_match and current_key:
            nested_key = nested_match.group(1)
            nested_value = nested_match.group(2).strip()
            if current_key not in metadata:
                metadata[current_key] = {}
            if isinstance(metadata[current_key], dict):
                metadata[current_key][nested_key] = nested_value.strip('"').strip("'")

    return metadata


def extract_wikilinks(content: str) -> list:
    """Extract [[wikilink]] references from markdown body."""
    body_match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    body = content[body_match.end():] if body_match else content
    regex = r'\[\[([^|\]#]+?)(?:#[^\]]*?)?(?:\|[^\]]*?)?\]\]'
    matches = re.findall(regex, body)
    return list(dict.fromkeys(m.strip() for m in matches if m.strip()))


def get_body(content: str) -> str:
    """Get markdown body without frontmatter."""
    match = re.match(r'^---\s*\n.*?\n---\s*\n', content, re.DOTALL)
    return content[match.end():] if match else content


def search_skills(repo_root: Path, query: str, limit: int = 3) -> list:
    """Search Skills by keyword matching on name, description, body, and wikilinks."""
    query_lower = query.lower()
    query_terms = query_lower.split()
    results = []

    for skill_path in sorted(repo_root.rglob('SKILL.md')):
        if any(part.startswith('.') for part in skill_path.parts):
            continue
        if 'node_modules' in str(skill_path):
            continue

        try:
            content = skill_path.read_text(encoding='utf-8')
        except Exception:
            continue

        metadata = parse_frontmatter(content)
        body = get_body(content)
        wikilinks = extract_wikilinks(content)

        name = metadata.get('name', skill_path.parent.name)
        description = metadata.get('description', '')
        if isinstance(description, dict):
            description = str(description)

        # Build searchable text
        searchable = f"{name} {description} {body}".lower()

        # Score: count how many query terms match
        score = 0
        for term in query_terms:
            if term in name.lower():
                score += 3  # Name match is highest
            if term in description.lower():
                score += 2  # Description match
            if term in searchable:
                score += 1  # Body match

        if score > 0:
            relative_path = skill_path.relative_to(repo_root)
            results.append({
                'name': name,
                'description': description[:200] if description else '',
                'path': str(relative_path),
                'wikilinks': wikilinks,
                'score': score,
                'body_preview': body[:500].strip(),
            })

    # Sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:limit]


def format_prompt_ready(results: list) -> str:
    """Format search results as prompt-ready context for LLMs."""
    if not results:
        return "No matching Skills found."

    lines = []
    lines.append("# Relevant Skills Found")
    lines.append(f"Found {len(results)} matching Skill(s):\n")

    for i, skill in enumerate(results, 1):
        lines.append(f"## {i}. {skill['name']}")
        lines.append(f"**Path**: `{skill['path']}`")
        if skill['description']:
            lines.append(f"**Description**: {skill['description']}")
        if skill['wikilinks']:
            lines.append(f"**Related Skills**: {', '.join(f'[[{w}]]' for w in skill['wikilinks'])}")
        lines.append("")
        lines.append("### Content Preview")
        lines.append("```")
        lines.append(skill['body_preview'])
        lines.append("```")
        lines.append("")

    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Search Skills and output RAG context')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--repo-root', type=str, default='.',
                        help='Repository root (default: current directory)')
    parser.add_argument('--limit', type=int, default=3,
                        help='Number of results (default: 3)')
    parser.add_argument('--json', action='store_true',
                        help='Output as JSON instead of markdown')
    parser.add_argument('--no-prompt', action='store_true',
                        help='Skip the trailing question line')
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        print(f'Error: Repository root not found: {repo_root}', file=sys.stderr)
        sys.exit(1)

    results = search_skills(repo_root, args.query, args.limit)

    if args.json:
        output = {
            'query': args.query,
            'results': results,
            'context': format_prompt_ready(results),
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(format_prompt_ready(results))
        if not args.no_prompt and results:
            print("---")
            print(f"Based on the {len(results)} Skill(s) above, answer the user's query about: {args.query}")


if __name__ == '__main__':
    main()
