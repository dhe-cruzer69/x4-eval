# x4-eval

X4 independent parent — **evaluation** (runner, evaluator, reporter). API/CLI. Fleet id **14**.

| Field | Value |
|-------|-------|
| Completion | **L0** — bootstrapped |
| Boundary | independent-parent |

No production evaluation is claimed until evidence states advance.

<!-- X4-APEX-DIAGRAM-START:x4-eval -->

```mermaid
flowchart LR
    INPUT[Evaluation Input] --> RUNNER[Runner]
    RUNNER --> EVALUATOR[Evaluator]
    EVALUATOR --> REPORTER[Reporter]
    REPORTER --> OUTPUT[Score and Report Artifact]
    FIXTURE[Known Input / Expected Result] -. validates .-> EVALUATOR
    LINEAGE[Run and Source Lineage] -. required for trust .-> REPORTER
    NOTE[L0 bootstrapped: no production evaluation claim] -. current boundary .-> OUTPUT
```

<!-- X4-APEX-DIAGRAM-END:x4-eval -->

