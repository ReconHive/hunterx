"""
HTTP Security Headers Analyzer
"""

from __future__ import annotations

from httpx import Response

from hunterx.core.context import ScanContext


class HTTPSecurityAnalyzer:

    SECURITY_HEADERS = {
        "Content-Security-Policy": {
            "description": "Prevents XSS attacks",
            "expected": None,
        },
        "Strict-Transport-Security": {
            "description": "Forces HTTPS",
            "expected": (
                "max-age=",
            ),
        },
        "X-Frame-Options": {
            "description": "Clickjacking protection",
            "expected": (
                "DENY",
                "SAMEORIGIN",
            ),
        },
        "X-Content-Type-Options": {
            "description": "MIME sniffing protection",
            "expected": (
                "nosniff",
            ),
        },
        "Referrer-Policy": {
            "description": "Controls Referer header",
            "expected": None,
        },
        "Permissions-Policy": {
            "description": "Browser feature restrictions",
            "expected": None,
        },
        "Cross-Origin-Resource-Policy": {
            "description": "Cross-origin resource policy",
            "expected": (
                "same-origin",
                "same-site",
            ),
        },
        "Cross-Origin-Embedder-Policy": {
            "description": "Cross-origin embedder policy",
            "expected": (
                "require-corp",
            ),
        },
        "Cross-Origin-Opener-Policy": {
            "description": "Cross-origin opener policy",
            "expected": (
                "same-origin",
            ),
        },
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

        for header, info in self.SECURITY_HEADERS.items():

            value = response.headers.get(header)

            if value is None:

                context.logger.warning(
                    f"{header}: Missing"
                )

                result[header] = "Missing"

                continue

            expected = info["expected"]

            if expected is None:

                context.logger.success(
                    f"{header}: Present"
                )

                result[header] = value

                continue

            value_lower = value.lower()

            valid = any(
                item.lower() in value_lower
                for item in expected
            )

            if valid:

                context.logger.success(
                    f"{header}: OK"
                )

            else:

                context.logger.warning(
                    f"{header}: Weak ({value})"
                )

            result[header] = value

        return result