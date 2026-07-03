from __future__ import annotations

from hunterx.plugins.base import Plugin

from hunterx.modules.dns.resolver import DNSResolver
from hunterx.modules.dns.records import DNSRecords
from hunterx.core.result import ScanResult


class DNSPlugin(Plugin):

    name = "dns"

    def __init__(self) -> None:

        self.resolver = DNSResolver()

        self.records = DNSRecords()

    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:

        ip = self.resolver.resolve(target)

        result.dns.ip = ip

        result.dns.records = self.records.lookup(target)