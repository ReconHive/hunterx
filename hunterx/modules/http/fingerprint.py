"""
HTTP Fingerprint Module
"""

from __future__ import annotations

import re

from rich.table import Table

from hunterx.cli.console import console
from hunterx.core.context import ScanContext


class HTTPFingerprint:

    def analyze(
        self,
        context: ScanContext,
    ) -> None:

        url = f"https://{context.target}"

        try:

            response = context.http.get(url)

        except Exception as exc:

            context.logger.error(str(exc))
            return

        html = response.text

        title = "Unknown"

        match = re.search(
            r"<title>(.*?)</title>",
            html,
            re.IGNORECASE | re.DOTALL,
        )

        if match:

            title = match.group(1).strip()

        context.result.http.title = title

        table = Table(
            title="HTTP Fingerprint",
            header_style="bold cyan",
            border_style="bright_blue",
            expand=False,
        )

        table.add_column(
            "Property",
            style="bold cyan",
            no_wrap=True,
        )

        table.add_column(
            "Value",
            style="white",
        )

        table.add_row(
            "Title",
            title,
        )

        interesting = [
            "Server",
            "X-Powered-By",
            "Content-Length",
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-Content-Type-Options",
            "Referrer-Policy",
        ]

        for header in interesting:

            value = response.headers.get(header)

            if value:

                table.add_row(
                    header,
                    value,
                )

        console.print(table)