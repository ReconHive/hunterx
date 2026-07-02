"""
HTTP Fingerprint Module
"""

from __future__ import annotations

import re

import httpx

from hunterx.core.logger import logger


class HTTPFingerprint:

    def analyze(self, target: str) -> None:

        url = f"https://{target}"

        logger.info("Analyzing HTTP fingerprint...")

        try:

            response = httpx.get(
                url,
                timeout=10,
                follow_redirects=True,
            )

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

                    logger.success(f"{header} : {value}")

        except Exception as exc:

            logger.error(str(exc))