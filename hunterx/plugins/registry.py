from __future__ import annotations

from hunterx.plugins.base import Plugin


class PluginRegistry:

    def __init__(self) -> None:

        self._plugins: list[Plugin] = []

    def register(
        self,
        plugin: Plugin,
    ) -> None:

        self._plugins.append(plugin)

    def plugins(self) -> list[Plugin]:

        return self._plugins