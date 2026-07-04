"""
HTTP Cookies Analyzer
"""

from __future__ import annotations

from httpx import Response

from hunterx.core.context import ScanContext


class HTTPCookiesAnalyzer:

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> list[dict]:

        context.logger.info(
            "Analyzing cookies..."
        )

        cookies: list[dict] = []

        for cookie in response.cookies.jar:

            data = {
                "name": cookie.name,
                "secure": cookie.secure,
                "httponly": (
                    "HttpOnly" in (
                        cookie._rest or {}
                    )
                ),
                "samesite": (
                    cookie._rest.get(
                        "SameSite",
                        "None",
                    )
                    if cookie._rest
                    else "None"
                ),
            }

            cookies.append(data)

            context.logger.success(
                f"Cookie : {cookie.name}"
            )

            context.logger.info(
                f"  Secure : {data['secure']}"
            )

            context.logger.info(
                f"  HttpOnly : {data['httponly']}"
            )

            context.logger.info(
                f"  SameSite : {data['samesite']}"
            )

        if not cookies:

            context.logger.warning(
                "No cookies found."
            )

        return cookies