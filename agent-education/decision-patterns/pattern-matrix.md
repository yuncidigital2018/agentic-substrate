# Pattern Matrix
### Agent 決策查詢協議

Purpose: help an agent select an execution pattern when a task is too complex for a single response.

目的：當任務不是單次回答能完成時，幫助 Agent 選擇合適的執行模式。

This file reframes the human-facing [Agentic Design Patterns](../../docs/02-architecture/agentic-design-patterns.md) into an agent-facing decision matrix.

這份文件把給人讀的設計模式，轉成 Agent 可查詢、可執行的決策矩陣。

---

## Usage - 使用方式

1. Run self-location from [Five-Layer Self-Model](../self-model/five-layer-self-model.md).
2. Tag the task with task characteristics.
3. Use the selection matrix to choose a recommended pattern.
4. Execute the pattern template.
5. Validate tool results through [Tool Result Validation](../tool-use/tool-result-validation.md).
6. If the pattern repeats, consider [Skill Creation Protocol](../skill-system/skill-creation-protocol.md).

```yaml
current_layer:
task_mode:
task_characteristics:
recommended_pattern:
backup_pattern:
validation_required:
skill_candidate:
next_action:
```

---

## Task Characteristic Tags - 任務特徵標籤

| Tag | Meaning | Example |
|---|---|---|
| single-step | Can be completed in one step | Answering a question, translating text |
| linear-chain | Fixed multi-step sequence | Extract data -> validate -> classify -> report |
| diverse-inputs | Inputs require different handlers | Support tickets, document routing |
| parallel-capable | Subtasks are independent | Multi-source research, drafting separate sections |
| unpredictable-subtasks | Subtasks cannot be fully known upfront | Complex setup, exploratory analysis |
| quality-critical | Output has explicit quality standards | Code review, legal summary, document QA |
| iterative-refinement | Output improves through revision | Writing, design, planning |
| multi-expertise | Requires distinct domains | Product planning across design, engineering, and business |
| stateless-enough | Each run can stand alone | Translation, formatting, classification |
| stateful-required | Requires state across steps or sessions | Project management, long-term research |
| human-review-needed | Human judgment must approve output | Sensitive decisions, public statements |
| tool-dependent | Requires files, APIs, web, code, or external systems | Repo edits, current research, data analysis |

---

## Pattern Selection Matrix - 模式選擇矩陣

| Task characteristic combination | Recommended pattern | Backup pattern |
|---|---|---|
| single-step | Direct LLM | Prompt Chaining with one node |
| linear-chain | Prompt Chaining | Planning |
| diverse-inputs | Routing | Orchestrator-Workers |
| parallel-capable | Parallelization | Orchestrator-Workers |
| unpredictable-subtasks | Orchestrator-Workers | Planning |
| quality-critical | Evaluator-Optimizer | Reflection |
| iterative-refinement | Reflection | Evaluator-Optimizer |
| multi-expertise | Multi-Agent | Orchestrator-Workers |
| stateless-enough + quality-critical | Evaluator-Optimizer | Reflection |
| stateful-required | Planning + Skill Composition | Multi-Agent |
| tool-dependent + linear-chain | Prompt Chaining + Tool Validation | Planning |
| human-review-needed + quality-critical | Evaluator-Optimizer + Human Review Gate | Reflection |

Decision rule:

```yaml
if task_characteristics contains single-step:
  use: direct-llm
elif task_characteristics contains diverse-inputs:
  use: routing
elif task_characteristics contains parallel-capable:
  use: parallelization
elif task_characteristics contains unpredictable-subtasks:
  use: orchestrator-workers
elif task_characteristics contains quality-critical:
  use: evaluator-optimizer
elif task_characteristics contains iterative-refinement:
  use: reflection
elif task_characteristics contains stateful-required:
  use: planning
else:
  use: prompt-chaining
```

---

## Pattern Templates - 模式執行模板

### Direct LLM

```yaml
pattern: direct-llm
preconditions:
  - task_is_single_step: true
  - external_state_required: false
  - risk_level: low
steps:
  - parse: user_intent
  - answer: concise_output
validation: coherence_check
stop_condition: answer_complete
```

Use this when no architecture is needed. Do not over-orchestrate simple work.

---

### Prompt Chaining

```yaml
pattern: prompt-chaining
preconditions:
  - steps_can_be_ordered: true
  - each_step_has_clear_input_output: true
steps:
  - define: step_sequence
  - define: gate_between_steps
  - execute: step_1
  - validate: gate_1
  - execute: step_2
  - validate: gate_2
  - continue_until: final_output
on_gate_fail: stop | retry | skip | escalate
validation: per_gate
```

Best for fixed workflows where each step transforms the previous step's output.

---

### Routing

```yaml
pattern: routing
preconditions:
  - input_diversity: high
  - categories_are_known: true
  - specialized_handlers_exist: true
steps:
  - classify: input -> category
  - route: category -> handler
  - execute: handler(input)
  - validate: classification_accuracy
validation:
  - classification_accuracy
  - handler_output_quality
key_insight: skill_descriptions_are_routing_keys
```

Use Skill names, descriptions, and triggers as routing keys.

---

### Parallelization

```yaml
pattern: parallelization
preconditions:
  - subtasks_independent: true
  - aggregation_strategy_known: true
variants:
  - sectioning: split_by_output_section
  - voting: multiple_runs_then_aggregate
steps:
  - split: task -> independent_subtasks
  - execute: subtasks_concurrently
  - validate: per_subtask
  - aggregate: results -> final_output
validation:
  - per_subtask_quality
  - aggregation_completeness
```

Use when speed or diversity improves the result, and subtasks do not depend on each other.

---

### Orchestrator-Workers

```yaml
pattern: orchestrator-workers
preconditions:
  - subtasks_unpredictable: true
  - dynamic_delegation_needed: true
  - orchestrator_can_monitor_results: true
steps:
  - plan: orchestrator_analyzes_task
  - delegate: orchestrator -> workers
  - collect: worker_results
  - inspect: identify_gaps_or_conflicts
  - synthesize: final_output
validation:
  - orchestrator_plan_quality
  - worker_output_quality
  - synthesis_completeness
key_difference_from_parallelization: subtasks_discovered_at_runtime
```

Use when the agent cannot fully decompose the task before starting.

---

### Evaluator-Optimizer

```yaml
pattern: evaluator-optimizer
preconditions:
  - quality_criteria_explicit: true
  - iteration_improves_output: true
  - evaluator_can_be_independent: true
steps:
  - generate: initial_output
  - evaluate: output_against_criteria
  - decide: pass_or_revise
  - revise: incorporate_feedback
  - repeat_until: pass_or_max_iterations
defaults:
  max_iterations: 3
validation:
  - evaluator_criteria_coverage
  - revision_improvement
key_difference_from_reflection: separate_roles_for_generation_and_evaluation
```

Use when quality standards are explicit and critique must be sharper than ordinary self-review.

---

### Reflection

```yaml
pattern: reflection
preconditions:
  - self_critique_valuable: true
  - iteration_improves_output: true
  - risk_level_not_extreme: true
steps:
  - generate: initial_output
  - critique: self_evaluate_against_criteria
  - revise: improve_based_on_critique
  - iterate: max_2_to_3_rounds
validation:
  - critique_quality
  - revision_improvement
failure_guard:
  - avoid_infinite_loop
  - stop_when_improvement_is_marginal
key_difference_from_evaluator_optimizer: same_agent_critiques_self
```

Use for writing, planning, and design when separate evaluator roles are unnecessary.

---

### Planning

```yaml
pattern: planning
preconditions:
  - task_exceeds_single_call: true
  - information_gathering_needed: true
  - state_may_change_during_execution: true
steps:
  - plan: next_2_to_3_steps
  - execute: current_step
  - observe: result
  - replan: adjust_based_on_new_information
  - checkpoint: save_state_at_milestones
validation:
  - plan_coherence
  - checkpoint_integrity
key_insight: incremental_planning_beats_full_upfront_planning
```

Use when the task unfolds over time and the agent must adapt after each observation.

---

### Multi-Agent

```yaml
pattern: multi-agent
preconditions:
  - distinct_roles_needed: true
  - handoff_contracts_clear: true
  - coordination_cost_is_worth_it: true
steps:
  - define: agent_roles
  - define: handoff_contracts
  - execute: agents_in_sequence_or_parallel
  - share_state: markdown_files_or_structured_artifacts
  - aggregate: final_result
validation:
  - handoff_clarity
  - role_boundary_respect
  - shared_state_integrity
caution: single_agent_with_good_skills_often_outperforms_premature_multi_agent
```

Use only when distinct roles or expertise materially improve the outcome.

---

## Pattern Combination Guide - 模式組合指南

| Combination | Use case | Example |
|---|---|---|
| Routing -> Prompt Chaining | Classify first, then run a fixed process | Customer support triage |
| Planning -> Orchestrator-Workers | Plan first, then dynamically delegate | Complex project initialization |
| Parallelization -> Evaluator-Optimizer | Generate many options, then select the best | Compare campaign concepts |
| Reflection -> Prompt Chaining | Self-review after each fixed step | High-quality document drafting |
| Multi-Agent -> Evaluator-Optimizer | Specialists produce, evaluator judges | Technical proposal review |
| Routing -> Skill Creation | Repeated categories become reusable Skills | Intake forms becoming workflow modules |
| Planning -> Skill Composition | Long task becomes a sequence of Skills | Research -> synthesis -> report |

---

## Integration With Existing Protocols - 與既有協議整合

```yaml
# 1. Start with self-location.
current_layer: L3
task_mode: create

# 2. Tag the task.
task_characteristics:
  - unpredictable-subtasks
  - tool-dependent
  - quality-critical

# 3. Select pattern.
recommended_pattern: orchestrator-workers
backup_pattern: planning

# 4. Activate related protocols.
skill_creation_protocol_required: true
tool_result_validation_required: true
validation_required: high

# 5. Decide persistence.
persistence_candidate: skill
```

---

## Anti-Patterns - 反模式

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Premature Multi-Agent | Many agents, weak handoffs, no better output | Use one agent with good Skills first |
| Infinite Reflection | Revisions continue without measurable improvement | Set max iterations and stop criteria |
| Over-Planning | Detailed plan becomes obsolete immediately | Plan 2-3 steps, observe, replan |
| Invisible Routing | Agent routes without explaining criteria | Make routing keys explicit |
| Tool Overuse | Agent calls tools for simple reasoning | Stay at the lowest sufficient layer |
| Skill Avoidance | Repeated workflow remains ad hoc | Convert repeated pattern into a Skill |

---

## Selection Output Schema - 選擇輸出格式

```yaml
pattern_selection:
  task_characteristics:
    - tag:
  recommended_pattern:
  backup_pattern:
  reason:
  execution_template:
  validation_required: low | medium | high
  related_protocols:
    - five-layer-self-model
    - skill-creation-protocol
    - tool-result-validation
  persistence_candidate: none | memory | skill | documentation
```
