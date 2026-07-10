"""
HTTP Cookies Analyzer
"""

from __future__ import annotations

from httpx import Response
from rich.table import Table

from hunterx.cli.console import console
from hunterx.core.context import ScanContext


class HTTPCookiesAnalyzer:

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> list[dict]:

        cookies: list[dict] = []

        table = Table(
            title="Cookies",
            header_style="bold cyan",
            border_style="bright_blue",
            expand=False,
        )

        table.add_column(
            "Cookie",
            style="bold cyan",
            no_wrap=True,
        )

        table.add_column(
            "Secure",
            justify="center",
        )

        table.add_column(
            "HttpOnly",
            justify="center",
        )

        table.add_column(
            "SameSite",
            justify="center",
        )

        for cookie in response.cookies.jar:

            data = {
                "name": cookie.name,
                "secure": cookie.secure,
                "httponly": (
                    "HttpOnly" in (cookie._rest or {})
                ),
                "samesite": (
                    cookie._rest.get(
                        "SameSite",
                        "None",
                    )
                    if cookie._rest
                    else "None"
                ),
            }

            cookies.append(data)

            table.add_row(
                data["name"],
                "✓" if data["secure"] else "✗",
                "✓" if data["httponly"] else "✗",
                str(data["samesite"]),
            )

        if cookies:

            console.print(table)

        return cookies