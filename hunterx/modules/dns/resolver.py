"""
DNS Resolver Module
"""

from __future__ import annotations

from hunterx.core.context import ScanContext


class DNSResolver:
    """
    Resolve domain names to IPv4 addresses.
    """

    def resolve(
        self,
        context: ScanContext,
    ) -> str | None:

        cache_key = f"dns:{context.target}"

        cached = context.cache.get(cache_key)

        if cached:

            context.logger.info(
                "DNS cache hit."
            )

            return cached

        context.logger.info(
            f"Resolving {context.target}..."
        )

        try:

            answers = context.dns.resolve(
                context.target
            )

            ip = answers[0].to_text()

            context.cache.set(
                cache_key,
                ip,
            )

            context.logger.success(
                f"Resolved: {ip}"
            )

            return ip

        except Exception:

            context.logger.error(
                "Failed to resolve target."
            )

            return None