from __future__ import annotations

import time

from hunterx.core.hooks.base import Hook


class MetricsHook(Hook):

    def __init__(self) -> None:

        self._plugin_start = 0.0

    def before_scan(
        self,
        context,
    ) -> None:

        context.metrics.metrics.scan_started = (
            time.perf_counter()
        )

    def after_scan(
        self,
        context,
    ) -> None:

        context.metrics.metrics.scan_finished = (
            time.perf_counter()
        )

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        self._plugin_start = (
            time.perf_counter()
        )

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        elapsed = (
            time.perf_counter()
            - self._plugin_start
        )

        context.metrics.metrics.plugins[
            plugin.name
        ] = elapsed