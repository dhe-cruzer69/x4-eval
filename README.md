# x4-eval

X4 independent parent — **evaluation** (runner, evaluator, reporter). API/CLI. Fleet id **14**.

| Field | Value |
|-------|-------|
| Completion | **L0** — bootstrapped |
| Boundary | independent-parent |

No production evaluation is claimed until evidence states advance.

## APEX Architecture Map

> Status: architecture documentation; implementation and deployment claims require independent verification.

```mermaid
flowchart TB
  Input[Evaluation case] --> Normalize[Normalize case format]
  Normalize --> Execute[Run target evaluator]
  Execute --> Raw[Raw response / measurements]
  Raw --> Score[Compute declared metrics]
  Score --> Stamp[Attach corpus and evaluator version]
  Stamp --> Result[Emit compact score record]
  Harness[x4-eval-harness] --> Import[Consume score records]
  Result --> Import
  Import --> Aggregate[Aggregate by slice and metric]
  Aggregate --> Gate{Regression threshold exceeded?}
  Gate -->|yes| Fail[Flag regression for review]
  Gate -->|no| Pass[Eligible for broader evaluation]
```
**Consolidation note:** This diagram treats x4-eval as a narrow scoring component and x4-eval-harness as the orchestrator. Verify the overlap before deciding whether to merge or retain both repositories.

