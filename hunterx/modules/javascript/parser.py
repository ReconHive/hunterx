from __future__ import annotations

from hunterx.modules.javascript import regex


class JavaScriptParser:

    def parse(
        self,
        text: str,
    ) -> dict:

        endpoints = regex.ENDPOINT.findall(
            text,
        )

        urls = regex.URL.findall(
            text,
        )

        domains = regex.DOMAIN.findall(
            text,
        )

        secrets = []

        for pattern in (
            regex.JWT,
            regex.GOOGLE_API,
            regex.AWS_ACCESS_KEY,
            regex.SLACK_TOKEN,
            regex.PRIVATE_KEY,
        ):

            secrets.extend(
                pattern.findall(
                    text,
                )
            )

        return {
            "endpoints": sorted(
                set(endpoints),
            ),
            "urls": sorted(
                set(urls),
            ),
            "domains": sorted(
                set(domains),
            ),
            "secrets": sorted(
                set(secrets),
            ),
        }