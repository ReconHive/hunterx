"""
HunterX Application Core
"""

from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.logger import logger
from hunterx.core.scanner import ScanEngine


class HunterX:
    """
    Main HunterX application.
    """

    VERSION = "0.1.0"

    def __init__(self) -> None:

        self.config = Config()

        self.initialized = False

    def initialize(self) -> None:

        logger.info("Initializing HunterX framework...")

        self.initialized = True

        logger.success("Framework initialized.")

    def run(self, target: str) -> None:

        if not self.initialized:
            self.initialize()

        engine = ScanEngine()

        engine.run(target)