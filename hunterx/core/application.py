from __future__ import annotations
"""
HunterX Application Core
"""
import asyncio

from hunterx.modules.test.plugin import TestPlugin

from hunterx.core.config import Settings
from hunterx.core.logger import logger
from hunterx.modules.dns.resolver import DNSResolver


class HunterX:
    """
    Main HunterX application.
    """

    VERSION = "0.1.0"

    def __init__(self) -> None:

        self.settings = Settings()

        self.initialized = False

    def initialize(self) -> None:

        logger.info("Initializing HunterX framework...")

        self.initialized = True

        logger.success("Framework initialized.")


    def run(self, target: str) -> None:

        if not self.initialized:
            self.initialize()

        resolver = DNSResolver()

        resolver.resolve(target)