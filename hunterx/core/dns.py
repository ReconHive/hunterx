"""
HunterX DNS Resolver Pool
"""

from __future__ import annotations

import dns.resolver


class DNSPool:

    def __init__(self) -> None:

        self.resolver = dns.resolver.Resolver()

        self.resolver.nameservers = [
            "1.1.1.1",   # Cloudflare
            "8.8.8.8",   # Google
            "9.9.9.9",   # Quad9
        ]

        self.resolver.timeout = 2

        self.resolver.lifetime = 2

    def resolve(self, host: str):

        return self.resolver.resolve(host)