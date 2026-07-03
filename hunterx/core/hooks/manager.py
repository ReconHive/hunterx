from __future__ import annotations

from hunterx.core.hooks.base import Hook


class HookManager:

    def __init__(self) -> None:

        self._hooks: list[Hook] = []

    def register(
        self,
        hook: Hook,
    ) -> None:

        self._hooks.append(hook)

    def before_scan(
        self,
        context,
    ) -> None:

        for hook in self._hooks:

            hook.before_scan(context)

    def after_scan(
        self,
        context,
    ) -> None:

        for hook in self._hooks:

            hook.after_scan(context)

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        for hook in self._hooks:

            hook.before_plugin(
                context,
                plugin,
            )

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        for hook in self._hooks:

            hook.after_plugin(
                context,
                plugin,
            )

    def clear(self) -> None:

        self._hooks.clear()