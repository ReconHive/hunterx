from __future__ import annotations

from httpx import Response

from hunterx.core.context import ScanContext


class HTTPCORSAnalyzer:

    def analyze(
        self,
        context: ScanContext,
        response: Response,
    ) -> dict[str, str]:

        context.logger.info(
            "Analyzing CORS..."
        )

        headers = {}

        interesting = [
            "Access-Control-Allow-Origin",
            "Access-Control-Allow-Credentials",
            "Access-Control-Allow-Headers",
            "Access-Control-Allow-Methods",
            "Access-Control-Expose-Headers",
            "Vary",
        ]

        for header in interesting:

            value = response.headers.get(
                header
            )

            if value:

                context.logger.success(
                    f"{header}: {value}"
                )

                headers[header] = value

            else:

                context.logger.warning(
                    f"{header}: Missing"
                )

        return headers