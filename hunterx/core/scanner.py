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

        self.registry = loader.load()

    def run(
        self,
        target: str,
    ) -> None:

        logger.info("Starting scan pipeline...")

        for plugin in self.registry.plugins():

            logger.info(
                f"Running plugin: {plugin.name}"
            )

            plugin.run(
                target,
                self.result,
            )

        logger.success("Scan completed.")