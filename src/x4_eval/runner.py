"""Structural evaluation runner scaffold. No production claims at L0."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvalRunner:
    name: str = "x4-eval"
    version: str = "0.0.1"
    results: list[dict[str, Any]] = field(default_factory=list)

    def run(self, case: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(case, dict) or "id" not in case:
            raise ValueError("case must be a dict with an id")
        result = {"id": case["id"], "status": "PASS", "score": 1.0}
        self.results.append(result)
        return result

    def health(self) -> dict[str, str]:
        return {"status": "ok", "server": self.name, "version": self.version}
