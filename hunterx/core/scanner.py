"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords
from hunterx.modules.http.client import HTTPClient


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self) -> None:
        self.resolver = DNSResolver()
        self.records = DNSRecords()
        self.http = HTTPClient()

    def run(self, target: str) -> None:

        self.resolver.resolve(target)

        self.records.lookup(target)

        self.http.fetch(target)