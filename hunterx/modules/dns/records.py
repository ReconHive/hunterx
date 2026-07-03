"""
DNS Records Module
"""

from __future__ import annotations

from hunterx.core.dns import DNSPool
from hunterx.core.logger import logger


class DNSRecords:
    """
    Retrieve DNS records for a target.
    """

    def __init__(self) -> None:

        self.pool = DNSPool()

    def lookup(
        self,
        target: str,
    ) -> dict[str, list[str]]:

        record_types = [
            "A",
            "AAAA",
            "MX",
            "NS",
            "TXT",
            "CNAME",
        ]

        results: dict[str, list[str]] = {}

        for record_type in record_types:

            logger.info(f"{record_type} records")

            try:

                answers = self.pool.resolver.resolve(
                    target,
                    record_type,
                )

                values = [
                    str(answer)
                    for answer in answers
                ]

                results[record_type] = values

                for value in values:

                    logger.success(value)

            except Exception:

                logger.warning("Not found")

                results[record_type] = []

        return results