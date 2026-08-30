# Deep Research Team

Deploy a team of specialized AI research agents that work in parallel, cross-validate findings, and deliver structured, source-cited reports — all inside your coding environment.

## Quick Start

### Trigger the skill

Say any of:
- `"deep research [topic]"`
- `"深度研究 [topic]"`
- `"research team [topic]"`

### Choose a mode

| Mode | Agents | Best for | Time |
|------|--------|----------|------|
| **Quick** | 3 research + orchestrator | Rapid topic overview, initial exploration | 5-10 min |
| **Full** | 3-10 research + synthesis + review + final | Due diligence, investment research, competitive analysis | 15-30 min |

If you don't specify, the skill auto-selects based on your depth requirement.

## What You Get

```
your-research-topic/
├── 00_planning/research_plan.md      ← Research architecture
├── 01_market/research.md + sources.md
├── 02_technology/research.md + sources.md
├── 03_competition/research.md + sources.md
├── ...
├── synthesis/synthesis.md            ← Cross-module analysis
├── review/review_report.md           ← Quality audit with score
└── final_report/
    ├── full_report.md                ← Complete report
    └── executive_summary.md          ← 1000-word summary
```

Every fact is cited in `sources.md`. Every module is independently auditable.

## How It Works

```
You → Define topic & depth
       ↓
PM Agent → Designs research architecture (you approve before execution)
       ↓
Research Agents → 3-10 specialists investigate in parallel
       ↓
Synthesis Agent → Finds consensus, contradictions, and causal links
       ↓
Review Agent → Adversarial quality audit (scores 1-10)
       ↓
Final Report Agent → Assembles publication-ready deliverable
```

## Why Not Just Use ChatGPT Deep Research?

| | Built-in Deep Research | This Skill |
|---|---|---|
| Research architecture | Black box — AI decides | **You design & approve** |
| Output format | Chat message | **Structured files on disk** |
| Cross-validation | None | **Dedicated contradiction detection** |
| Quality audit | None | **Adversarial review agent** |
| Source tracking | Inline citations | **Per-module sources.md** |
| Reproducibility | Not reproducible | **Full audit trail** |
| Workflow integration | Copy-paste | **Files ready for next step** |

## Supported Languages

Reports can be generated in any language. Default: Traditional Chinese (繁體中文).

## Requirements

- Claude Code (or compatible SKILL.md agent)
- Web search capability (for research agents to gather sources)
