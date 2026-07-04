from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.cookies import HTTPCookiesAnalyzer
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

    def run(
        self,
        context: ScanContext,
    ) -> None:

        response = self.client.fetch(context)

        if not response:
            return

        context.result.http.status = response.status_code

        context.result.http.server = (
            response.headers.get("Server")
        )

        context.result.http.url = str(
            response.url
        )

        context.result.http.headers = dict(
            response.headers
        )

        self.fingerprint.analyze(
            context
        )

        security = self.security.analyze(
            context,
            response,
        )

        context.result.http.security_headers = (
            security
        )

        cookies = self.cookies.analyze(
            context,
            response,
        )

        context.result.http.cookies = cookies

        technologies = self.technologies.analyze(
            context,
            response,
        )

        if technologies:

            context.logger.info(
                "Detected Technologies"
            )

            for tech in technologies:

                context.logger.success(
                    tech
                )

            context.result.http.technologies = (
                technologies
            )