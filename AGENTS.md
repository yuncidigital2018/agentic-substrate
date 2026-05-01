# Agent Guidance for Agentic Substrate

This repository is both a conceptual framework and a practical toolkit. When helping a user understand or modify it, preserve that dual identity.

## Project Thesis

Agentic Substrate argues that the next software paradigm is not "AI features added to existing apps." It is a new computational substrate where:

- LLMs are the computation layer.
- Tools and protocols let models act on the world.
- Skills are reusable workflow units that encode domain expertise.
- Agents orchestrate Skills, tools, memory, and long-running work.
- Interfaces expose the system through chat, IDEs, CLIs, APIs, and future ambient surfaces.

## How to Read This Repo

Start here:

1. `README.md` for the public overview.
2. `docs/START-HERE.md` for routing by audience.
3. `docs/01-foundations/agentic-substrate.md` for the core architecture.
4. `docs/01-foundations/five-layer-model.md` for the layer model.
5. `agent-education/README.md` for the agent-readable operational layer.
6. `docs/04-curriculum/learning-path.md` for the educational path.
7. `skills/` for installable, practical examples.

## Agent Self-Model

If you are using this repo to guide agent behavior rather than only editing the repo, read `agent-education/README.md` before acting.

Before non-trivial work, identify:

- Which layer you are operating in: LLM computation, tool/protocol, Skill, Agent, or interface.
- Whether an existing Skill should be reused (check `skill-index.md`).
- Which decision pattern fits the task: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, reflection, planning, or multi-agent.
- Whether tool use is required.
- What validation level is needed.
- Whether the workflow should become reusable documentation, memory, or a Skill.
- What to read from and write to persistent memory (see `agent-education/memory-system/memory-protocol.md`).

## Writing Style

- Keep the bilingual English/Traditional Chinese style when editing public-facing docs.
- Prefer clear architecture language over hype.
- Keep non-engineers central: domain experts are Skill builders, not merely end users.
- Explain technical ideas through workflow, process, and everyday work examples.
- Avoid turning this into a generic AI tools list.

## Contribution Priorities

High-value changes:

- Make the first five minutes clearer for a new visitor.
- Add examples that show a real workflow becoming a Skill.
- Improve AI-agent-readable navigation such as `llms.txt`, concise summaries, and canonical reading paths.
- Strengthen installability and verification of Skills.
- Add public-facing visuals, diagrams, and examples that help the project spread.

Be careful with:

- Over-engineering the framework before the public narrative is clear.
- Adding too many concepts to the README before the value proposition lands.
- Removing the practical Skills, because they prove the framework is not only theory.
