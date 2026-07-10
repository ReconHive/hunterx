from __future__ import annotations

import time

from hunterx.core.hooks.base import Hook


class TimingHook(Hook):

    def __init__(self) -> None:

        self.scan_start = 0.0

    def before_scan(
        self,
        context,
    ) -> None:

        self.scan_start = time.perf_counter()

    def after_scan(
        self,
        context,
    ) -> None:

        pass

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        pass

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        pass