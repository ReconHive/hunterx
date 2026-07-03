"""
Subdomain Module
"""

from __future__ import annotations

from hunterx.core.module import Module
from hunterx.core.result import ScanResult

from hunterx.modules.subdomain.scanner import (
    SubdomainScanner,
)


class SubdomainModule(Module):

    name = "subdomain"

    def __init__(self):

        self.scanner = SubdomainScanner()

    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:

        result.subdomains.hosts = (
            self.scanner.scan(target)
        )