"""
HunterX Shared HTTP Pool
"""

from __future__ import annotations

import time

import httpx

from hunterx.core.config import Config


class HTTPPool:
    """
    Shared HTTP client with automatic retry/backoff.
    """

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.config = config

        self.client = httpx.Client(
            timeout=config.http.timeout,
            follow_redirects=config.http.follow_redirects,
            http2=True,
        )

    def request(
        self,
        method: str,
        url: str,
        **kwargs,
    ) -> httpx.Response:

        retries = self.config.http.retries

        backoff = self.config.http.backoff

        last_error: Exception | None = None

        for attempt in range(
            retries + 1,
        ):

            try:

                return self.client.request(
                    method=method,
                    url=url,
                    **kwargs,
                )

            except (
                httpx.TimeoutException,
                httpx.ConnectError,
                httpx.NetworkError,
                httpx.RemoteProtocolError,
                httpx.ReadError,
                httpx.WriteError,
            ) as exc:

                last_error = exc

                if attempt >= retries:
                    raise

                time.sleep(
                    backoff * (2**attempt)
                )

        raise RuntimeError(
            "Unexpected HTTP retry failure."
        ) from last_error

    def get(
        self,
        url: str,
        **kwargs,
    ) -> httpx.Response:

        return self.request(
            "GET",
            url,
            **kwargs,
        )

    def post(
        self,
        url: str,
        **kwargs,
    ) -> httpx.Response:

        return self.request(
            "POST",
            url,
            **kwargs,
        )

    def head(
        self,
        url: str,
        **kwargs,
    ) -> httpx.Response:

        return self.request(
            "HEAD",
            url,
            **kwargs,
        )

    def set_headers(
        self,
        headers: dict[str, str],
    ) -> None:

        self.client.headers.update(
            headers,
        )

    def clear_headers(
        self,
    ) -> None:

        self.client.headers.clear()

    def close(
        self,
    ) -> None:

        self.client.close()