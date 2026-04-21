# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

---

## [0.2.0] - 2026-04-22

### Added
- **Plugin Distribution**: `.claude-plugin/plugin.json` configuration for Claude Code and Cowork plugin installation
- **YAML Frontmatter**: All 9 SKILL.md files now include proper YAML frontmatter with `name`, `description`, and `metadata` fields for plugin system progressive discovery
- **Install Script** (`install.sh`): One-command installer with interactive target selection (project-level plugin, user-level skills, or custom path), color output, verification
- **Quick Start Guide** (`QUICK-START.md`): 5-minute onboarding guide with four paths (Not Technical → Self-Discovery, Messy Chat → Conversation-to-Skill, Build Now → Skill Builder, Browse → Example Gallery), bilingual

- **Curriculum Level Guides**: Four practical, hands-on deep-dive documents for each learning level — `level-1-conversation.md` (five conversation patterns, three exercises), `level-2-tools.md` (tool categories, practical patterns, MCP introduction), `level-3-skills.md` (three paths to first Skill, seven components in plain language, example gallery reference), `level-4-agents.md` (Agent vs Skill comparison, SOUL.md design, session cycle, four Agent patterns)
- **Cursor Plugin** (`.cursor-plugin/plugin.json`): Plugin configuration for Cursor IDE compatibility
- **Community Skill Template**: Complete Skill submission guide added to CONTRIBUTING.md with YAML frontmatter template, seven-component checklist, and quality verification checklist

### Changed
- Version bumped from 0.1.0 to 0.2.0 (Phase 1-3 complete)
- README: all curriculum docs now ★, added Quick Start link, install script, .claude-plugin, .cursor-plugin, index.html in repo structure
- ROADMAP: Phase 1 ✅, Phase 2 ✅, Phase 3 ✅ (core items), Phase 4 partially started
- CONTRIBUTING.md: expanded with detailed Skill submission workflow and quality checklist

---

## [0.1.0] - 2026-04-21

### Added
- Initial repo structure with four documentation areas
- **Core Architecture** (`docs/01-foundations/agentic-substrate.md`): The Agentic Substrate five-layer model, paradigm shift narrative, six design principles
- **Skill Anatomy** (`docs/01-foundations/skill-anatomy.md`): Seven components of a Skill, five Skill types (Data, Process, Transform, Integration, Orchestration), maturity model (L0-L4), composition patterns
- **Skill Self-Discovery** (`skills/skill-self-discovery/SKILL.md`): Interactive Skill that guides non-technical users through seven conversational questions to reveal they already know how to build a Skill — with Phase 0 warm-up, Phase 1 seven questions mapped to seven components, Phase 2 reveal moment, Phase 3 bridge to creation
- **"You Already Know"** (`docs/04-curriculum/you-already-know.md`): Learning document for the curriculum — tells the story of why the vocabulary gap (not capability gap) blocks non-engineers, includes Mei-Ling the accountant narrative, vocabulary translation table, and references to the interactive Skill
- **Skill Composition Patterns** (`docs/02-architecture/skill-composition.md`): Deep dive into the "a235bc1e" dynamic composition pattern — semantic vs syntactic composition, LLM as universal adapter, five composition patterns, five failure modes, composability checklist, combinatorial value analysis, output header convention
- **Agentic Design Patterns** (`docs/02-architecture/agentic-design-patterns.md`): Nine patterns from Andrew Ng (4 foundational) and Anthropic (5 compositional) mapped to the Five-Layer Model, with decision guide, anti-patterns, and complexity spectrum
- **Five-Layer Model Deep Dive** (`docs/01-foundations/five-layer-model.md`): Complete architectural analysis of each layer — internal mechanics, boundary contracts, failure modes, cross-layer dynamics, computer analogy extension, real request flow trace
- **Markdown as Native Medium** (`docs/01-foundations/markdown-as-medium.md`): Seven roles of Markdown in Agentic workflows, .md file taxonomy (5 categories), lifecycle diagrams, failed alternatives comparison, design principles for .md-centric systems
- **Interactive Architecture Visualization** (`index.html`): Single-page React app with four interactive sections — Five-Layer Model (click-to-expand with bilingual detail), Product Layer Coverage table, Learning Path timeline, Dynamic Skill Composition demo. Dark theme, responsive, deployable to GitHub Pages
- **Learning Path** (`docs/04-curriculum/learning-path.md`): Four-level progressive curriculum (Conversation → Tool Use → Skill Building → Agent Orchestration), five-layer mapping per level, "Who You Are" column showing domain experts as the key to Level 3, complete curriculum document connection map, entry points for four reader types
- **Claude Architecture Case Study** (`docs/03-claude-case-study/claude-architecture.md`): Claude product family layer coverage analysis, layer-by-layer anatomy (six cognitive operations per LLM turn, tool inventory, Skill lifecycle with progressive discovery, Agent loop pseudocode, 1.6%/98.4% breakdown diagram, interface spectrum), Agent SDK architecture (agents-as-tools, tool-use-first philosophy), five insights from Five-Layer Model analysis, five design lessons, limitations disclosure
- **Memory & State** (`docs/02-architecture/memory-and-state.md`): Three-tier memory model (Working/Session/Persistent), context window as RAM analogy, Repo-as-Memory pattern with file anatomy and session cycle, four practical memory patterns (SOUL.md, DAILY.md, Decision Records, Memory Index), memory across the Five-Layer Model, three anti-patterns, six design principles, state-of-the-art comparison
- **Example Skills Gallery** (`skills/examples/`): Six ready-to-use Skills demonstrating the framework across knowledge-work domains — `meeting-notes-to-actions` (Transform: unstructured notes → decisions + action items with owners), `document-reviewer` (Process: four-pass systematic review with severity classification), `research-and-summarize` (Process: structured research with source evaluation and gap disclosure), `project-status-tracker` (Orchestration: multi-source data → unified health dashboard with risk management), `accounting-reconciler` (Transform: two financial datasets → reconciliation report with categorized discrepancies), `content-pipeline` (Process: six-stage end-to-end content creation with platform-specific guidelines)
- **Skill Builder** (`skills/skill-builder/SKILL.md`): Guided interactive Skill creation for any role — five-phase process (Role & Context → Deep Dive Seven Components → Draft & Review → Refine → Deliver), role-specific question adaptations for 8+ domains (Accounting, Marketing, PM, Admin, Legal, Education, HR, Engineering), comparison with skill-self-discovery and conversation-to-skill, complete PM example session, save/test/teach delivery options
- **Conversation-to-Skill** (`skills/conversation-to-skill/SKILL.md`): Transform Skill that analyzes messy LLM conversations, generates structured work-record.md, then reveals the work record is 80% of a reusable Skill — four phases (Analyze → Present → Reveal → Convert), six extraction elements, complete example with quarterly report scenario, connected to Learning Path (Level 1 → Level 3 bridge)
- **Landscape Analysis** (`docs/02-architecture/landscape.md`): Comparison with AIOS, Superpowers, SKILL.md, Skills vs MCP discourse, Andrew Ng's patterns, Anthropic's Building Effective Agents, and Agent Skills Open Standard (anthropics/skills, 122K+ stars, agentskills.io) — seven pillars total
- README with bilingual (EN/ZH-TW) overview
- Dual license: CC BY-SA 4.0 (content) + MIT (code)
- Contributing guidelines
