"""
DNS Records Module
"""

from __future__ import annotations

from hunterx.core.context import ScanContext


class DNSRecords:
    """
    Retrieve DNS records for a target.
    """

    def lookup(
        self,
        context: ScanContext,
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

            context.logger.info(
                f"{record_type} records"
            )

            try:

                answers = context.dns.resolver.resolve(
                    context.target,
                    record_type,
                )

                values = [
                    str(answer)
                    for answer in answers
                ]

                results[record_type] = values

                for value in values:

                    context.logger.success(value)

            except Exception:

                context.logger.warning(
                    "Not found"
                )

                results[record_type] = []

        return results