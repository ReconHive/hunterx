from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.subdomain.scanner import SubdomainScanner
from hunterx.plugins.base import Plugin


class SubdomainPlugin(Plugin):

    name = "subdomain"

    def __init__(self) -> None:

        self.scanner = SubdomainScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        hosts = self.scanner.scan(
            context
        )

        context.result.subdomains.hosts = hosts

        self.save_workspace(
            context,
            context.result.subdomains,
        )