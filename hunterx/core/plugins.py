from __future__ import annotations

from hunterx.plugins.base import Plugin


class PluginCollection:

    def __init__(self) -> None:

        self._plugins: dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:

        self._plugins[
            plugin.name
        ] = plugin

    def get(
        self,
        name: str,
    ) -> Plugin | None:

        return self._plugins.get(
            name,
        )

    def all(
        self,
    ) -> list[Plugin]:

        return list(
            self._plugins.values(),
        )

    def names(
        self,
    ) -> list[str]:

        return sorted(
            self._plugins.keys(),
        )

    def select(
        self,
        names: list[str] | None,
    ) -> list[Plugin]:

        if not names:

            return self.all()

        plugins: list[Plugin] = []

        for name in names:

            plugin = self.get(
                name,
            )

            if plugin is not None:

                plugins.append(
                    plugin,
                )

        return plugins

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self._plugins

    def __contains__(
        self,
        name: str,
    ) -> bool:

        return self.exists(
            name,
        )

    def __iter__(self):

        return iter(
            self._plugins.values(),
        )

    def __len__(
        self,
    ) -> int:

        return len(
            self._plugins,
        )