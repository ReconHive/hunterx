"""
DNS Module
"""

from __future__ import annotations

from hunterx.core.module import Module
from hunterx.core.result import ScanResult

from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords


class DNSModule(Module):

    name = "dns"

    def __init__(self):

        self.resolver = DNSResolver()

        self.records = DNSRecords()

    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:

        result.dns.ip = self.resolver.resolve(
            target
        )

        result.dns.records = self.records.lookup(
            target
        )