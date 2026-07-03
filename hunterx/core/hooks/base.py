from __future__ import annotations

from abc import ABC


class Hook(ABC):
    """
    Base class for lifecycle hooks.
    """

    def before_scan(self, context) -> None:
        pass

    def after_scan(self, context) -> None:
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