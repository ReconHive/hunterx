"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.modules.dns.resolver import DNSResolver


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self) -> None:
        self.resolver = DNSResolver()

    def run(self, target: str) -> None:
        """
        Execute scan pipeline.
        """

        logger.info("Starting scan pipeline...")

        self.resolver.resolve(target)

        logger.success("Scan pipeline finished.")