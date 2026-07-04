"""
HTTP Security Headers Analyzer
"""

from __future__ import annotations

from httpx import Response

from hunterx.core.context import ScanContext


class HTTPSecurityAnalyzer:

    SECURITY_HEADERS = {
        "Content-Security-Policy":
            "Prevents XSS attacks",

        "Strict-Transport-Security":
            "Forces HTTPS",

        "X-Frame-Options":
            "Clickjacking protection",

        "X-Content-Type-Options":
            "MIME sniffing protection",

        "Referrer-Policy":
            "Controls Referer header",

        "Permissions-Policy":
            "Browser feature restrictions",

        "Cross-Origin-Resource-Policy":
            "Cross-origin resource policy",

        "Cross-Origin-Embedder-Policy":
            "Cross-origin embedder policy",

        "Cross-Origin-Opener-Policy":
            "Cross-origin opener policy",
    }

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> dict[str, str]:

        context.logger.info(
            "Analyzing security headers..."
        )

        result: dict[str, str] = {}

        for header, description in (
            self.SECURITY_HEADERS.items()
        ):

            value = response.headers.get(header)

            if value:

                context.logger.success(
                    f"{header}: {value}"
                )

                result[header] = value

            else:

                context.logger.warning(
                    f"{header}: Missing"
                )

        return result