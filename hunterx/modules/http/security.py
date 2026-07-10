"""
HTTP Security Headers Analyzer
"""

from __future__ import annotations

from httpx import Response
from rich.table import Table

from hunterx.cli.console import console
from hunterx.core.context import ScanContext


class HTTPSecurityAnalyzer:

    SECURITY_HEADERS = {
        "Content-Security-Policy": {
            "description": "Prevents XSS attacks",
            "expected": None,
        },
        "Strict-Transport-Security": {
            "description": "Forces HTTPS",
            "expected": (
                "max-age=",
            ),
        },
        "X-Frame-Options": {
            "description": "Clickjacking protection",
            "expected": (
                "DENY",
                "SAMEORIGIN",
            ),
        },
        "X-Content-Type-Options": {
            "description": "MIME sniffing protection",
            "expected": (
                "nosniff",
            ),
        },
        "Referrer-Policy": {
            "description": "Controls Referer header",
            "expected": None,
        },
        "Permissions-Policy": {
            "description": "Browser feature restrictions",
            "expected": None,
        },
        "Cross-Origin-Resource-Policy": {
            "description": "Cross-origin resource policy",
            "expected": (
                "same-origin",
                "same-site",
            ),
        },
        "Cross-Origin-Embedder-Policy": {
            "description": "Cross-origin embedder policy",
            "expected": (
                "require-corp",
            ),
        },
        "Cross-Origin-Opener-Policy": {
            "description": "Cross-origin opener policy",
            "expected": (
                "same-origin",
            ),
        },
    }

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> dict[str, str]:

        result: dict[str, str] = {}

        table = Table(
            title="Security Headers",
            header_style="bold cyan",
            border_style="bright_blue",
            expand=False,
        )

        table.add_column(
            "Header",
            style="bold cyan",
            no_wrap=True,
        )

        table.add_column(
            "Status",
            justify="center",
            no_wrap=True,
        )

        table.add_column(
            "Value",
            style="white",
        )

        for header, info in self.SECURITY_HEADERS.items():

            value = response.headers.get(header)

            if value is None:

                result[header] = "Missing"

                table.add_row(
                    header,
                    "[yellow]Missing[/yellow]",
                    "-",
                )

                continue

            expected = info["expected"]

            if expected is None:

                result[header] = value

                table.add_row(
                    header,
                    "[green]Present[/green]",
                    value,
                )

                continue

            valid = any(
                item.lower() in value.lower()
                for item in expected
            )

            result[header] = value

            table.add_row(
                header,
                "[green]OK[/green]" if valid else "[yellow]Weak[/yellow]",
                value,
            )

        console.print(table)

        return result