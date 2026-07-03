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
        """
        Resolve an IPv4 address for the target.
        """

        context.logger.info(
            f"Resolving {context.target}..."
        )

        try:

            answers = context.dns.resolve(
                context.target
            )

            ip = answers[0].to_text()

            context.logger.success(
                f"Resolved: {ip}"
            )

            return ip

        except Exception:

            context.logger.error(
                "Failed to resolve target."
            )

            return None