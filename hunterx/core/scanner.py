"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.context import ScanContext
from hunterx.core.dns import DNSPool
from hunterx.core.http import HTTPPool
from hunterx.core.logger import logger
from hunterx.core.result import ScanResult
from hunterx.plugins.loader import PluginLoader


class ScanEngine:
    """
    Coordinates all plugins.
    """

    def __init__(
        self,
        config: Config,
        result: ScanResult,
    ) -> None:

        self.config = config

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

        http = HTTPPool(self.config)

        dns = DNSPool(self.config)

        context = ScanContext(
            target=target,
            config=self.config,
            result=self.result,
            http=http,
            dns=dns,
        )

        selected = self.plugins.select(
            plugins
        )

        if plugins and not selected:

            logger.warning(
                "No matching plugins were found."
            )

            http.close()

            return

        for plugin in selected:

            logger.info(
                f"Running plugin: {plugin.name}"
            )

            plugin.run(context)

        http.close()

        logger.success("Scan completed.")