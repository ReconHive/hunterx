from __future__ import annotations

from hunterx.core.hooks.base import Hook


class ProgressHook(Hook):

    def before_scan(
        self,
        context,
    ) -> None:

        total = len(
            context.selected_plugins
        )

        context.progress.start(total)

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        context.progress.plugin(
            plugin.name
        )

    def after_scan(
        self,
        context,
    ) -> None:

        context.progress.finish()