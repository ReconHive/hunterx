"""
DNS Records Module
"""

from __future__ import annotations

from hunterx.cli.tables import key_value
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

        rows: list[tuple[str, str]] = []

        for record_type in record_types:

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

                if values:

                    for value in values:

                        rows.append(
                            (
                                record_type,
                                value,
                            )
                        )

                else:

                    rows.append(
                        (
                            record_type,
                            "-",
                        )
                    )

            except Exception:

                results[record_type] = []

                rows.append(
                    (
                        record_type,
                        "[yellow]Not found[/yellow]",
                    )
                )

        key_value(
            "DNS Records",
            rows,
        )

        return results