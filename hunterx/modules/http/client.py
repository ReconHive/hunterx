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

        cache_key = f"http:{url}"

        cached = context.cache.get(cache_key)

        if cached:

            logger.info("HTTP cache hit.")

            return cached

        context.http.clear_headers()

        if context.custom_headers:

            context.http.set_headers(
                context.custom_headers
            )

        logger.info("")
        logger.info("Request")
        logger.info(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

        logger.success(f"Method : {context.method}")
        logger.success(f"URL : {url}")

        for key, value in (
            context.http.client.headers.items()
        ):

            logger.success(
                f"{key}: {value}"
            )

        start = time.perf_counter()

        try:

            response = context.http.client.request(
                method=context.method,
                url=url,
            )

            elapsed = (
                time.perf_counter() - start
            )

            context.cache.set(
                cache_key,
                response,
            )

            logger.info("")
            logger.info("Response")
            logger.info(
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )

            logger.success(
                f"Status : {response.status_code} {response.reason_phrase}"
            )

            logger.success(
                f"Elapsed : {elapsed:.2f}s"
            )

            logger.success(
                f"Size : {len(response.content)} bytes"
            )

            logger.success(
                f"Final URL : {response.url}"
            )

            logger.info("")
            logger.info("Response Headers")
            logger.info(
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            )

            for key, value in (
                response.headers.items()
            ):

                logger.success(
                    f"{key}: {value}"
                )

            return response

        except Exception as exc:

            logger.error(str(exc))

            return None