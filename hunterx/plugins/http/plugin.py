from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.fingerprint import HTTPFingerprint
from hunterx.plugins.base import Plugin
from hunterx.modules.http.technologies import TechnologyDetector

class HTTPPlugin(Plugin):

    name = "http"

    def __init__(self) -> None:

        self.client = HTTPClient()

        self.fingerprint = HTTPFingerprint()

        self.technologies = TechnologyDetector()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        response = self.client.fetch(context)

        if response:

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

        self.fingerprint.analyze(context)

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

            context.result.http.technologies = technologies