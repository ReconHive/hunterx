"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.core.result import ScanResult

from hunterx.plugins.loader import PluginLoader


class ScanEngine:
    """
    Coordinates all plugins.
    """

    def __init__(
        self,
        result: ScanResult,
    ) -> None:

        self.result = result

        loader = PluginLoader()

        self.plugins = loader.load()

    def run(
        self,
        target: str,
        plugins: list[str] | None = None,
    ) -> None:
        """
        Execute scan pipeline.
        """

        logger.info("Starting scan pipeline...")

        selected = self.plugins.select(plugins)

        if plugins and not selected:

            logger.warning(
                "No matching plugins were found."
            )

            return

        for plugin in selected:

            logger.info(
                f"Running plugin: {plugin.name}"
            )

            plugin.run(
                target=target,
                result=self.result,
            )

        logger.success("Scan completed.")