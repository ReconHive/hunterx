from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.dns.records import DNSRecords
from hunterx.modules.dns.resolver import DNSResolver
from hunterx.plugins.base import Plugin


class DNSPlugin(Plugin):

    name = "dns"

    def __init__(self) -> None:

        self.resolver = DNSResolver()

        self.records = DNSRecords()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        ip = self.resolver.resolve(
            context
        )

        context.result.dns.ip = ip

        context.result.dns.records = (
            self.records.lookup(
                context
            )
        )

        self.save_workspace(
            context,
            context.result.dns,
        )