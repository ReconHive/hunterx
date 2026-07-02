"""
DNS Resolver Module
"""

from __future__ import annotations

import socket

from hunterx.core.logger import logger


class DNSResolver:
    """
    Resolve domain names to IPv4 addresses.
    """

    def resolve(self, target: str) -> str | None:
        """
        Resolve an IPv4 address for the target.
        """

        logger.info(f"Resolving {target}...")

        try:
            ip = socket.gethostbyname(target)

            logger.success(f"Resolved: {ip}")

            return ip

        except socket.gaierror:

            logger.error("Failed to resolve target.")

            return None