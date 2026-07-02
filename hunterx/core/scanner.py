"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.core.module_manager import ModuleManager

from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.fingerprint import HTTPFingerprint
from hunterx.modules.subdomain.scanner import SubdomainScanner


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self) -> None:
        self.manager = ModuleManager()

        resolver = DNSResolver()
        records = DNSRecords()
        http = HTTPClient()
        fingerprint = HTTPFingerprint()
        subdomain = SubdomainScanner()

        self.manager.register(resolver.resolve)
        self.manager.register(records.lookup)
        self.manager.register(http.fetch)
        self.manager.register(fingerprint.analyze)
        self.manager.register(subdomain.scan)


    def run(self, target: str) -> None:
        """
        Execute scan pipeline.
        """

        logger.info("Starting scan pipeline...")

        self.manager.execute(target)

        logger.success("Scan completed.")