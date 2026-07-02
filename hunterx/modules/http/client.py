"""
HTTP Client Module
"""

from __future__ import annotations

import time

import httpx

from hunterx.core.config import Config
from hunterx.core.logger import logger


class HTTPClient:
    """
    Retrieve basic HTTP information.
    """

    def __init__(self) -> None:

        self.config = Config()

    def fetch(self, target: str) -> None:

        url = f"https://{target}"

        logger.info(f"Connecting to {url}")

        start = time.perf_counter()

        try:

            response = httpx.get(
                url,
                timeout=self.config.http.timeout,
                follow_redirects=self.config.http.follow_redirects,
            )

            elapsed = time.perf_counter() - start

            logger.success(f"Status Code : {response.status_code}")
            logger.success(f"Response Time : {elapsed:.2f}s")

            server = response.headers.get("Server", "Unknown")
            logger.success(f"Server : {server}")

            content = response.headers.get("Content-Type", "Unknown")
            logger.success(f"Content-Type : {content}")

            logger.success(f"Final URL : {response.url}")

        except Exception as exc:

            logger.error(str(exc))