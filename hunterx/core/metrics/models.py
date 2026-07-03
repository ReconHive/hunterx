from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Metrics:

    scan_started: float = 0.0

    scan_finished: float = 0.0

    plugins: dict[str, float] = field(
        default_factory=dict
    )

    dns_queries: int = 0

    http_requests: int = 0

    warnings: int = 0

    errors: int = 0