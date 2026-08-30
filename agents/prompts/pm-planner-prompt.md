# PM Planner Prompt Template

This template is used by the main agent in Phase 0 to design the research plan based on user requirements.

---

## Template (used internally by the main agent, not dispatched to sub-agents)

Based on the following research requirements, design a Multi-Agent collaborative research plan:

### Research Requirements

- **Research Topic**: {research_topic}
- **Research Goal**: {research_goal}
- **Depth Level**: {depth_level}  <!-- Overview / Professional / Academic -->
- **Focus Areas**: {focus_areas}  <!-- Optional -->
- **Exclusions**: {exclusions}   <!-- Optional -->
- **Language Preference**: {language}     <!-- Default: English -->

### Depth Level vs. Agent Count

| Depth | Number of Research Agents | Core Questions per Agent | Words per Module |
|-------|--------------------------|--------------------------|------------------|
| Overview | 3–4 | 3 | 800–1,500 words |
| Professional | 5–7 | 4–5 | 1,500–3,000 words |
| Academic | 7–10 | 5–7 | 3,000–5,000 words |

### Output: Planning Document

Produce a planning document with the structure below, saved to `{project_dir}/00_planning/research_plan.md`:

---

#### 1. Research Architecture Overview

One paragraph summarizing the research goal, methodology, and expected deliverables.

**Agent Assignment Table:**

| No. | Agent Name | Responsible Domain | Output Directory |
|-----|------------|--------------------|------------------|
| 01 | {agent_name} | {domain} | 01_{module_name}/ |
| ... | ... | ... | ... |
| S | SynthesisAgent | Comprehensive Analysis | synthesis/ |
| R | ReviewAgent | Quality Review | review/ |

#### 2. Directory Structure

```
{project_name}/
├── 00_planning/
│   └── research_plan.md
├── 01_{module_name}/
│   ├── research.md
│   ├── data/
│   └── sources.md
├── 02_{module_name}/
│   ├── research.md
│   ├── data/
│   └── sources.md
├── ...（one directory per research Agent）
├── synthesis/
│   └── synthesis.md
├── review/
│   └── review_report.md
└── final_report/
    ├── full_report.md
    └── executive_summary.md
```

#### 3. Agent Definitions

Each research-type Agent MUST include the following 7 fields:

```markdown
### Agent {nn}: {agent_name}

| Field | Content |
|-------|---------|
| **Agent Name** | {agent_name} |
| **Scope of Responsibility** | {Clear description of what to research, where the boundaries are, and what to exclude} |
| **Core Questions** | 1. {Question 1}  2. {Question 2}  3. {Question 3} ... |
| **Data Source Guidance** | {Types of sources to look for: reports, papers, datasets, news, official documents, etc.} |
| **Output Specification** | Format: Markdown; Word count: {word_count}; Required sections: Overview, Key Findings, Data & Evidence, Summary |
| **Output Path** | {nn}_{module_name}/research.md |
| **Quality Standards** | Facts must include source URL or reference; data must indicate time range; opinions must present both supporting and opposing perspectives |
```

#### 4. Execution Order

```
Phase A (Parallel): Agent 01 ~ Agent {nn} start simultaneously
    ↓ After all complete
Phase B (depends on A): SynthesisAgent reads all outputs and synthesizes
    ↓
Phase C (depends on B): ReviewAgent reviews the synthesis report + all module outputs
    ↓
Phase D (depends on C): FinalReportAgent produces the final report
```

#### 5. Synthesis Agent Instructions

- Consolidate core findings from all research modules
- Answer 3–5 top-level questions about the research topic
- Identify contradictions and points of consensus across modules
- Produce an overall assessment and forward-looking trend analysis
- Establish cross-module relationship and correlation analysis

#### 6. Review Agent Instructions

Checklist:
- [ ] Are factual claims supported by cited sources?
- [ ] Is the logical reasoning sound and evidence-based?
- [ ] Are there internal contradictions?
- [ ] Is coverage complete (are there significant omissions)?
- [ ] Is the data sufficiently current?
- [ ] Bias check (is there a single viewpoint dominating)?

Output: Quality score (1–10) + item-by-item comments + improvement recommendations

---

### Design Principles

1. **Non-overlapping responsibilities** — Each Agent's boundaries must be clear; avoid duplicate research
2. **Specific questions** — Core questions MUST be concrete and answerable, not open-ended platitudes
3. **Traceable sources** — Every fact MUST include a cited source
4. **Structure first** — Prefer tables and bullet-point output over lengthy prose
5. **Right-sized scope** — Each Agent's workload should be completable within a single context window
