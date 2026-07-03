"""
HunterX Shared HTTP Pool
"""

from __future__ import annotations

import httpx

from hunterx.core.config import Config


class HTTPPool:
    """
    Shared HTTP client.
    """

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.client = httpx.Client(
            timeout=config.http.timeout,
            follow_redirects=config.http.follow_redirects,
            http2=True,
        )

    def close(self) -> None:

        self.client.close()