"""
HTTP Technology Detection
"""

from __future__ import annotations

import re

import httpx

from hunterx.core.context import ScanContext


class TechnologyDetector:

    signatures = {
        "Cloudflare": [
            ("Server", "cloudflare"),
        ],
        "Nginx": [
            ("Server", "nginx"),
        ],
        "Apache": [
            ("Server", "apache"),
        ],
        "IIS": [
            ("Server", "iis"),
        ],
        "ASP.NET": [
            ("X-Powered-By", "ASP.NET"),
        ],
        "PHP": [
            ("X-Powered-By", "PHP"),
        ],
        "Laravel": [
            ("Set-Cookie", "laravel_session"),
        ],
        "WordPress": [
            ("HTML", "wp-content"),
        ],
        "Bootstrap": [
            ("HTML", "bootstrap"),
        ],
        "React": [
            ("HTML", "__NEXT_DATA__"),
            ("HTML", "react"),
        ],
    }

    def analyze(
        self,
        context: ScanContext,
        response: httpx.Response,
    ) -> list[str]:

        html = response.text

        detected: list[str] = []

        for tech, rules in self.signatures.items():

            for header, value in rules:

                if header == "HTML":

                    if re.search(
                        re.escape(value),
                        html,
                        re.IGNORECASE,
                    ):

                        detected.append(tech)

                        break

                else:

                    header_value = response.headers.get(
                        header,
                        "",
                    )

                    if value.lower() in header_value.lower():

                        detected.append(tech)

                        break

        return sorted(set(detected))