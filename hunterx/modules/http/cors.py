from __future__ import annotations

from httpx import Response
from rich.table import Table

from hunterx.cli.console import console
from hunterx.core.context import ScanContext


class HTTPCORSAnalyzer:

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> dict[str, str]:

        headers: dict[str, str] = {}

        interesting = [
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Credentials",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Methods",
            "Access-Control-Expose-Headers",
            "Vary",
        ]

        table = Table(
            title="CORS",
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
            "Value",
            style="white",
        )

        for header in interesting:

            value = response.headers.get(header)

            if value:

                headers[header] = value

                table.add_row(
                    header,
                    value,
                )

            else:

                table.add_row(
                    header,
                    "[yellow]Missing[/yellow]",
                )

        console.print(table)

        return headers