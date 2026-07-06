"""
HTTP Fingerprint Module
"""

from __future__ import annotations

import re

from hunterx.core.context import ScanContext
from hunterx.core.logger import logger


class HTTPFingerprint:

    def analyze(
        self,
        context: ScanContext,
    ) -> None:

        url = f"https://{context.target}"

        logger.info(
            "Analyzing HTTP fingerprint..."
        )

        try:

            response = context.http.get(url)

            html = response.text

            title = "Unknown"

            match = re.search(
                r"<title>(.*?)</title>",
                html,
                re.IGNORECASE | re.DOTALL,
            )

            if match:

                title = match.group(1).strip()

            logger.success(f"Title : {title}")

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

                    logger.success(
                        f"{header} : {value}"
                    )

        except Exception as exc:

            logger.error(str(exc))