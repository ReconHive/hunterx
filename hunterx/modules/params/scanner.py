from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.params.classifier import classify
from hunterx.modules.params.extractor import extract_directory_url
from hunterx.modules.params.extractor import extract_params


class ParamsScanner:

    def scan(
        self,
        context: ScanContext,
    ) -> dict:

        urls: set[str] = set()

        urls.update(
            context.result.crawler.urls,
        )

        urls.update(
            context.result.crawler.sitemap,
        )

        urls.update(
            context.result.javascript.urls,
        )

        urls.update(
            url
            for url in context.result.javascript.endpoints
            if url.startswith("http")
        )

        for row in context.result.directory.paths:

            cleaned = extract_directory_url(
                row,
            )

            if cleaned:

                urls.add(
                    cleaned,
                )

        parameters = extract_params(
            list(urls),
        )

        classified: dict[str, list[str]] = {}

        for name in parameters:

            for category in classify(
                name,
            ):

                classified.setdefault(
                    category,
                    [],
                ).append(
                    name,
                )

        for category in classified:

            classified[category] = sorted(
                set(classified[category])
            )

        return {
            "parameters": parameters,
            "classified": classified,
        }