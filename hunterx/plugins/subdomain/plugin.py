from __future__ import annotations

from hunterx.plugins.base import Plugin

from hunterx.modules.subdomain.scanner import SubdomainScanner


class SubdomainPlugin(Plugin):

    name = "subdomain"

    def __init__(self) -> None:

        self.scanner = SubdomainScanner()

    def run(
        self,
        target: str,
        result,
    ) -> None:

        hosts = self.scanner.scan(target)

        result.subdomains.hosts = hosts