"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.fingerprint import HTTPFingerprint


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self) -> None:
        self.resolver = DNSResolver()
        self.records = DNSRecords()
        self.http = HTTPClient()
        self.fingerprint = HTTPFingerprint()

    def run(self, target: str) -> None:

        self.resolver.resolve(target)

        self.records.lookup(target)

        self.http.fetch(target)

        self.fingerprint.analyze(target)