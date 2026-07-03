from __future__ import annotations

import time

from hunterx.core.hooks.base import Hook


class TimingHook(Hook):

    def __init__(self) -> None:

        self.scan_start = 0.0

        self.plugin_start = 0.0

    def before_scan(
        self,
        context,
    ) -> None:

        self.scan_start = time.perf_counter()

    def after_scan(
        self,
        context,
    ) -> None:

        elapsed = (
            time.perf_counter()
            - self.scan_start
        )

        context.logger.success(
            f"Scan Time : {elapsed:.2f}s"
        )

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        self.plugin_start = time.perf_counter()

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        elapsed = (
            time.perf_counter()
            - self.plugin_start
        )

        context.logger.success(
            f"{plugin.name} : {elapsed:.2f}s"
        )