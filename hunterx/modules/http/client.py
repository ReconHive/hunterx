"""
HTTP Client Module
"""

from __future__ import annotations

import time

import httpx

from hunterx.core.context import ScanContext
from hunterx.core.logger import logger


class HTTPClient:
    """
    Retrieve basic HTTP information.
    """

    def fetch(
        self,
        context: ScanContext,
    ) -> httpx.Response | None:

        url = f"https://{context.target}"

        logger.info(f"Connecting to {url}")

        start = time.perf_counter()

        try:

            response = context.http.client.get(url)

            elapsed = time.perf_counter() - start

            logger.success(f"Status Code : {response.status_code}")
            logger.success(f"Response Time : {elapsed:.2f}s")

            server = response.headers.get(
                "Server",
                "Unknown",
            )

            logger.success(f"Server : {server}")

            content = response.headers.get(
                "Content-Type",
                "Unknown",
            )

            logger.success(f"Content-Type : {content}")

            logger.success(f"Final URL : {response.url}")

            return response

        except Exception as exc:

            logger.error(str(exc))

            return None