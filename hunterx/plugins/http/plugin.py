from __future__ import annotations

from hunterx.plugins.base import Plugin

from hunterx.modules.http.client import HTTPClient
from hunterx.modules.http.fingerprint import HTTPFingerprint
from hunterx.core.result import ScanResult


class HTTPPlugin(Plugin):

    name = "http"

    def __init__(self) -> None:

        self.client = HTTPClient()

        self.fingerprint = HTTPFingerprint()

    def run(
        self,
        target: str,
        result: ScanResult,
    ) -> None:

        response = self.client.fetch(target)

        if response:

            result.http.status = response.status_code

            result.http.server = response.headers.get("Server")

            result.http.url = str(response.url)

            result.http.headers = dict(response.headers)

        self.fingerprint.analyze(target)