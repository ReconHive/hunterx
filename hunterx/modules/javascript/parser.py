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

        secrets: list[str] = []

        endpoints.extend(
            regex.FETCH.findall(
                text,
            )
        )

        endpoints.extend(
            regex.AXIOS.findall(
                text,
            )
        )

        endpoints.extend(
            regex.XHR.findall(
                text,
            )
        )

        endpoints.extend(
            regex.GRAPHQL.findall(
                text,
            )
        )

        urls.extend(
            regex.WEBSOCKET.findall(
                text,
            )
        )

        urls.extend(
            regex.BASE_URL.findall(
                text,
            )
        )

        domains.extend(
            regex.FIREBASE.findall(
                text,
            )
        )

        domains.extend(
            regex.S3.findall(
                text,
            )
        )

        domains.extend(
            regex.CLOUDFRONT.findall(
                text,
            )
        )

        domains.extend(
            regex.AZURE.findall(
                text,
            )
        )

        for pattern in (
            regex.JWT,
            regex.GOOGLE_API,
            regex.GOOGLE_CLIENT,
            regex.AWS_ACCESS_KEY,
            regex.GITHUB,
            regex.STRIPE,
            regex.BEARER,
            regex.API_KEY,
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