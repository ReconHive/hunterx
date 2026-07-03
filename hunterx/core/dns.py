"""
HunterX DNS Resolver Pool
"""

from __future__ import annotations

import dns.resolver

from hunterx.core.config import Config


class DNSPool:

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.resolver = dns.resolver.Resolver()

        self.resolver.timeout = (
            config.dns.timeout
        )

        self.resolver.lifetime = (
            config.dns.lifetime
        )

        self.resolver.nameservers = (
            config.dns.nameservers
        )

    def resolve(
        self,
        host: str,
    ):

        return self.resolver.resolve(host)