"""
HunterX Application Core
"""

from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.logger import logger
from hunterx.core.result import ScanResult
from hunterx.core.scanner import ScanEngine


class HunterX:
    """
    Main HunterX application.
    """

    VERSION = "0.1.0"

    def __init__(self) -> None:

        self.config = Config()

        self.result = ScanResult()

        self.initialized = False

    def initialize(self) -> None:

        logger.info("Initializing HunterX framework...")

        self.initialized = True

        logger.success("Framework initialized.")

    def run(
        self,
        target: str,
        plugins: list[str] | None = None,
    ) -> None:

        if not self.initialized:
            self.initialize()

        engine = ScanEngine(self.result)

        engine.run(
            target,
            plugins=plugins,
        )