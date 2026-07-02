"""
DNS Records Module
"""

from __future__ import annotations

import dns.resolver

from hunterx.core.logger import logger


class DNSRecords:
    """
    Retrieve DNS records for a target.
    """

    def __init__(self) -> None:
        self.resolver = dns.resolver.Resolver()

    def lookup(self, target: str) -> None:

        record_types = [
            "A",
            "AAAA",
            "MX",
            "NS",
            "TXT",
            "CNAME",
        ]

        for record_type in record_types:

            logger.info(f"{record_type} records")

            try:

                answers = self.resolver.resolve(target, record_type)

                for answer in answers:
                    logger.success(str(answer))

            except Exception:
                logger.warning("Not found")