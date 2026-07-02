"""
DNS Resolver Module
"""

from __future__ import annotations

from hunterx.core.dns import DNSPool
from hunterx.core.logger import logger


class DNSResolver:
    """
    Resolve domain names to IPv4 addresses.
    """

    def __init__(self) -> None:
        self.pool = DNSPool()

    def resolve(self, target: str) -> str | None:
        """
        Resolve an IPv4 address for the target.
        """

        logger.info(f"Resolving {target}...")

        try:
            answers = self.pool.resolve(target)

            ip = answers[0].to_text()

            logger.success(f"Resolved: {ip}")

            return ip

        except Exception:

            logger.error("Failed to resolve target.")

            return None