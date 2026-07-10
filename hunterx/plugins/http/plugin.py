from __future__ import annotations

from rich.table import Table

from hunterx.cli.console import console
from hunterx.core.context import ScanContext
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.cookies import HTTPCookiesAnalyzer
from hunterx.modules.http.cors import HTTPCORSAnalyzer
from hunterx.modules.http.fingerprint import HTTPFingerprint
from hunterx.modules.http.security import HTTPSecurityAnalyzer
from hunterx.modules.http.technologies import TechnologyDetector
from hunterx.plugins.base import Plugin


class HTTPPlugin(Plugin):

    name = "http"

    def __init__(self) -> None:

        self.client = HTTPClient()
        self.fingerprint = HTTPFingerprint()
        self.technologies = TechnologyDetector()
        self.security = HTTPSecurityAnalyzer()
        self.cookies = HTTPCookiesAnalyzer()
        self.cors = HTTPCORSAnalyzer()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        response = self.client.fetch(context)

        if not response:
            return

        context.result.http.status = response.status_code
        context.result.http.server = response.headers.get("Server")
        context.result.http.url = str(response.url)
        context.result.http.headers = dict(response.headers)

        self.fingerprint.analyze(context)

        context.result.http.security_headers = (
            self.security.analyze(
                context,
                response,
            )
        )

        context.result.http.cors = (
            self.cors.analyze(
                context,
                response,
            )
        )

        context.result.http.cookies = (
            self.cookies.analyze(
                context,
                response,
            )
        )

        technologies = self.technologies.analyze(
            context,
            response,
        )

        context.result.http.technologies = technologies

        if technologies:

            table = Table(
                title="Technologies",
                header_style="bold cyan",
                border_style="bright_blue",
                expand=False,
            )

            table.add_column(
                "Technology",
                style="bold cyan",
            )

            for tech in technologies:
                table.add_row(tech)

            console.print(table)

        self.save_workspace(
            context,
            context.result.http,
        )