"""
HTTP Client Module
"""

from __future__ import annotations

import time

import httpx

from hunterx.core.context import ScanContext


class HTTPClient:
    """
    Retrieve basic HTTP information.
    """

    def fetch(
        self,
        context: ScanContext,
    ) -> httpx.Response | None:

        url = f"https://{context.target}"

        cache_key = f"http:{url}"

        cached = context.cache.get(cache_key)

        if cached:

            context.result.http.status = (
                cached.status_code
            )

            context.result.http.server = (
                cached.headers.get(
                    "Server",
                )
            )

            context.result.http.url = str(
                cached.url,
            )

            context.result.http.headers = dict(
                cached.headers,
            )

            return cached

        context.http.clear_headers()

        if context.custom_headers:

            context.http.set_headers(
                context.custom_headers,
            )

        try:

            response = context.http.client.request(
                method=context.method,
                url=url,
            )

        except Exception as exc:

            context.logger.error(
                str(exc),
            )

            return None

        context.cache.set(
            cache_key,
            response,
        )

        context.result.http.status = (
            response.status_code
        )

        context.result.http.server = (
            response.headers.get(
                "Server",
            )
        )

        context.result.http.url = str(
            response.url,
        )

        context.result.http.headers = dict(
            response.headers,
        )

        return response