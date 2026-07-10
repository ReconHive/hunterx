from __future__ import annotations

from hunterx.cli.panels import scan_configuration
from hunterx.core.hooks.base import Hook
from hunterx.core.logger import logger


class LoggerHook(Hook):

    def before_scan(
        self,
        context,
    ) -> None:

        logger.blank()

        scan_configuration(
            context,
        )

        logger.blank()

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

        logger.blank()

        logger.success(
            plugin.name.upper(),
        )

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        elapsed = (
            context.metrics.metrics.plugins.get(
                plugin.name,
                0.0,
            )
        )

        logger.success(
            f"{plugin.name.upper()} completed ({elapsed:.2f}s)",
        )

        logger.blank()