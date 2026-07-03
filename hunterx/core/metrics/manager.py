from __future__ import annotations

from hunterx.core.metrics.models import Metrics


class MetricsManager:

    def __init__(self) -> None:

        self.metrics = Metrics()

    @property
    def elapsed(self) -> float:

        return (
            self.metrics.scan_finished
            - self.metrics.scan_started
        )

    def plugin_time(
        self,
        name: str,
    ) -> float:

        return self.metrics.plugins.get(
            name,
            0.0,
        )