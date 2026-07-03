"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.logger import logger
from hunterx.core.module_manager import ModuleManager
from hunterx.core.result import ScanResult

from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.fingerprint import HTTPFingerprint
from hunterx.modules.subdomain.scanner import SubdomainScanner


class ScanEngine:
    """
    Coordinates all scan modules.
    """

    def __init__(self, result: ScanResult) -> None:

        self.result = result

        self.manager = ModuleManager()

        self.resolver = DNSResolver()
        self.records = DNSRecords()
        self.http = HTTPClient()
        self.fingerprint = HTTPFingerprint()
        self.subdomain = SubdomainScanner()

        self.manager.register(self.run_dns)
        self.manager.register(self.run_http)
        self.manager.register(self.run_subdomain)

    def run(self, target: str) -> None:
        """
        Execute scan pipeline.
        """

        logger.info("Starting scan pipeline...")

        self.manager.execute(target)

        logger.success("Scan completed.")

    def run_dns(self, target: str) -> None:

        ip = self.resolver.resolve(target)

        self.result.dns.ip = ip

        records = self.records.lookup(target)

        self.result.dns.records = records

    def run_http(self, target: str) -> None:

        response = self.http.fetch(target)

        if response:

            self.result.http.status = response.status_code

            self.result.http.server = response.headers.get("Server")

            self.result.http.url = str(response.url)

            self.result.http.headers = dict(response.headers)

        self.fingerprint.analyze(target)

    def run_subdomain(self, target: str) -> None:

        hosts = self.subdomain.scan(target)

        self.result.subdomains.hosts = hosts