from __future__ import annotations

from hunterx.core.hooks.base import Hook
from hunterx.core.logger import logger


class LoggerHook(Hook):

    def before_scan(
        self,
        context,
    ) -> None:

        logger.info(
            "Starting scan pipeline..."
        )

    def after_scan(
        self,
        context,
    ) -> None:

        logger.success(
            "Scan completed."
        )

    def before_plugin(
        self,
        context,
        plugin,
    ) -> None:

        logger.info(
            f"Running plugin: {plugin.name}"
        )

    def after_plugin(
        self,
        context,
        plugin,
    ) -> None:

        pass