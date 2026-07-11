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

        try:

            #
            # Use the operating system resolver configuration.
            #

            self.resolver = dns.resolver.Resolver()

        except (
            dns.resolver.NoResolverConfiguration,
            FileNotFoundError,
            OSError,
        ):

            #
            # Fallback for environments without resolv.conf
            # (e.g. Termux, some containers).
            #

            self.resolver = dns.resolver.Resolver(
                configure=False,
            )

        #
        # Configure resolver.
        #

        self.resolver.timeout = (
            config.dns.timeout
        )

        self.resolver.lifetime = (
            config.dns.lifetime
        )

        #
        # Use configured nameservers when provided.
        #

        if config.dns.nameservers:

            self.resolver.nameservers = (
                config.dns.nameservers
            )

        #
        # Otherwise provide sane defaults when the resolver
        # has no nameservers (Termux, minimal containers, etc.).
        #

        elif not self.resolver.nameservers:

            self.resolver.nameservers = [
                "1.1.1.1",
                "1.0.0.1",
                "8.8.8.8",
                "8.8.4.4",
            ]

    def resolve(
        self,
        host: str,
    ):

        return self.resolver.resolve(host)