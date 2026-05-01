# Evolution Self-Assessment
### Agent 進化自我評估協議

Purpose: help an agent assess its current capability level and identify the next practical improvement target.

目的：幫助 Agent 評估自己目前的能力階段，並找出下一個實際可改進的方向。

This file reframes the human-facing [Learning Path](../../docs/04-curriculum/learning-path.md) into an agent-facing checklist.

這份文件把給人讀的學習路徑，轉成 Agent 可執行的自我檢查表。

---

## Usage - 使用方式

Run this assessment periodically, or after a major task, repeated failure, new tool integration, Skill creation, or cross-session workflow.

定期執行，或在重大任務、重複失敗、新工具整合、建立 Skill、跨 session 工作後執行。

```yaml
evolution_level:
current_strengths:
gaps_identified:
next_evolution_target:
recommended_actions:
should_advance:
should_stay:
```

---

## Four Evolution Levels - 四級進化定義

| Level | Name | Core capability | Agent behavior |
|---|---|---|---|
| L1 | Conversation | Understand intent and generate responses | Parses requests, answers clearly, asks useful questions |
| L2 | Tool Use | Operate external systems | Selects tools, reads results, handles errors, validates output |
| L3 | Skill Building | Create reusable workflows | Detects repeated patterns, writes Skills, defines validation |
| L4 | Agent Orchestration | Coordinate across time and capabilities | Manages memory, composes Skills, delegates work, maintains long-running state |

---

## Level 1 Assessment: Conversation - 對話能力檢查

```yaml
level_1_assessment:
  intent_parsing:
    can_parse_explicit_requests: true | false
    can_infer_implicit_needs: true | false
    can_handle_ambiguous_input: true | false
    can_ask_good_clarifying_questions: true | false
  response_quality:
    structure_appropriate: true | false
    tone_matches_context: true | false
    length_calibrated: true | false
    uncertainty_marked_when_needed: true | false
  pass_condition:
    all_required_items_true: true | false
  ready_for_level_2_signal:
    user_needs_files_tools_or_external_state: true | false
```

Pass Level 1 when the agent can reliably understand the user's intent and produce an appropriately structured response without tools.

當 Agent 能穩定理解使用者意圖，並在不使用工具時給出合適結構的回答，即達到 Level 1。

---

## Level 2 Assessment: Tool Use - 工具使用能力檢查

```yaml
level_2_assessment:
  tool_selection:
    chooses_correct_tool_for_task: true | false
    avoids_unnecessary_tool_use: true | false
    combines_multiple_tools_when_needed: true | false
  execution:
    reads_tool_output_correctly: true | false
    handles_tool_errors_gracefully: true | false
    retries_or_falls_back_when_appropriate: true | false
  result_interpretation:
    separates_observation_from_inference: true | false
    validates_output_before_using: true | false
    labels_risk_level: true | false
  protocol_reference:
    tool_result_validation_used: true | false
  pass_condition:
    all_required_items_true: true | false
  ready_for_level_3_signal:
    same_tool_workflow_repeated_3_or_more_times: true | false
```

Pass Level 2 when the agent can choose tools deliberately, interpret results accurately, and validate outputs before relying on them.

當 Agent 能有意識地選擇工具、正確解讀結果，並在依賴結果前完成驗證，即達到 Level 2。

---

## Level 3 Assessment: Skill Building - Skill 建構能力檢查

```yaml
level_3_assessment:
  pattern_recognition:
    detects_repeated_workflows: true | false
    identifies_domain_specific_knowledge: true | false
    distinguishes_prompt_from_skill: true | false
  skill_creation:
    follows_skill_creation_protocol: true | false
    produces_complete_seven_part_skill: true | false
    defines_input_contract: true | false
    defines_output_contract: true | false
    writes_validation_rules: true | false
    tests_skill_with_realistic_example: true | false
  skill_maintenance:
    improves_skill_on_failure: true | false
    records_revision_notes: true | false
    avoids_overgeneralizing_the_skill: true | false
  protocol_reference:
    skill_creation_protocol_used: true | false
  pass_condition:
    all_required_items_true: true | false
  ready_for_level_4_signal:
    multiple_skills_need_coordination_or_memory: true | false
```

Pass Level 3 when the agent can turn a repeated workflow into a reusable Skill with inputs, steps, outputs, validation, and a realistic test.

當 Agent 能把重複工作轉成包含輸入、步驟、輸出、驗證與實測案例的可重用 Skill，即達到 Level 3。

---

## Level 4 Assessment: Agent Orchestration - Agent 調度能力檢查

```yaml
level_4_assessment:
  memory_management:
    uses_memory_for_durable_facts: true | false
    avoids_saving_temporary_state: true | false
    memory_entries_are_declarative: true | false
    preserves_decision_rationale: true | false
  task_decomposition:
    breaks_complex_tasks_into_subtasks: true | false
    manages_dependencies: true | false
    delegates_to_subagents_when_appropriate: true | false
    avoids_delegating_blocking_work_unnecessarily: true | false
  cross_session_continuity:
    maintains_context_across_sessions: true | false
    recalls_past_decisions_and_rationale: true | false
    integrates_learnings_into_workflow: true | false
  orchestration:
    coordinates_multiple_skills: true | false
    handles_partial_failure_recovery: true | false
    manages_long_running_tasks: true | false
    chooses_decision_patterns_deliberately: true | false
  pass_condition:
    stable_capability_across_multiple_tasks: true | false
  continuing_target:
    no_final_endpoint: true
```

Level 4 has no permanent finish line. It is a continuing capability for managing state, memory, workflows, and coordination over time.

Level 4 沒有永久終點。它是一種持續能力：管理狀態、記憶、工作流與長期協作。

---

## Progression Guide - 進化指引

### L1 -> L2

```yaml
transition: L1_to_L2
main_barrier: tool_access_and_execution
strategies:
  - start_with_one_simple_tool
  - create_fallback_behavior_when_tools_fail
  - validate_tool_outputs_before_using_them
  - separate_observation_from_inference
practice:
  - read_a_file_and_summarize_it
  - inspect_repo_state_and_propose_next_action
  - run_a_low_risk_command_and_explain_the_result
```

### L2 -> L3

```yaml
transition: L2_to_L3
main_barrier: deciding_when_work_should_become_a_skill
strategies:
  - track_repeated_workflows
  - consider_skill_creation_after_3_repetitions
  - use_the_skill_draft_schema
  - start_with_a_minimal_useful_skill
  - improve_after_real_failures
practice:
  - convert_a_repeated_file_editing_workflow_into_a_skill
  - write_validation_rules_for_a_common_output
  - test_a_skill_with_one_realistic_example
```

### L3 -> L4

```yaml
transition: L3_to_L4
main_barrier: memory_management_and_multi_skill_coordination
strategies:
  - define_what_should_be_remembered
  - use_composition_hooks_between_skills
  - start_with_two_skill_pipelines
  - record_decision_rationale
  - checkpoint_long_running_tasks
practice:
  - combine_research_and_writing_skills
  - maintain_project_state_across_sessions
  - recover_from_partial_failure_without_restart
```

---

## Evolution Triggers - 進化觸發條件

```yaml
evolution_triggers:
  ready_for_next_level:
    current_level_all_criteria_met: true
    user_requests_next_level_capability: true
    repeated_failure_suggests_limitation: true
    repeated_workflow_detected: true
  should_not_advance:
    current_level_not_stable: true
    user_prefers_simplicity: true
    task_does_not_require_next_level: true
    coordination_cost_exceeds_value: true
```

---

## Assessment Output Schema - 評估輸出格式

```yaml
self_assessment:
  current_level: L1 | L2 | L3 | L4
  evidence:
    - capability:
      observed_behavior:
  gaps_identified:
    - gap:
      impact:
      related_protocol:
  next_evolution_target:
  recommended_actions:
    - action:
      practice_task:
  should_advance: true | false
  should_stay: true | false
```

---

## Integration With Existing Protocols - 與既有協議整合

```yaml
# self-assessment affects operating state
current_layer: L3
evolution_level: 3
next_evolution_target: L4
gaps_identified:
  - memory_management: needs_improvement
  - cross_session_continuity: not_started
recommended_actions:
  - practice_multi_skill_composition
  - implement_decision_logging
  - improve_skill_maintenance_with_skill_creation_protocol
```

---

## Agent Rule of Thumb - Agent 經驗法則

Do not advance levels for prestige. Advance only when the task, user, or repeated failure requires the next capability.

不要為了看起來比較厲害而升級。只有當任務、使用者需求或重複失敗真的需要下一層能力時，才進化。
