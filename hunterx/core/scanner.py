"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self) -> None:
        self.resolver = DNSResolver()
        self.records = DNSRecords()

    def run(self, target: str) -> None:
        """
        Execute scan pipeline.
        """

        self.resolver.resolve(target)

        self.records.lookup(target)