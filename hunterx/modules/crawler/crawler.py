from __future__ import annotations

from hunterx.core.context import ScanContext

from hunterx.modules.crawler.extractor import LinkExtractor
from hunterx.modules.crawler.normalizer import URLNormalizer


class WebCrawler:

    def __init__(self):

        self.extractor = LinkExtractor()

        self.normalizer = URLNormalizer()

    def crawl(
        self,
        context: ScanContext,
    ) -> list[str]:

        url = f"https://{context.target}"

        response = context.http.client.get(
            url,
        )

        html = response.text

        links = self.extractor.extract(
            html,
        )

        found: set[str] = set()

        for link in links:

            normalized = self.normalizer.normalize(
                url,
                link,
            )

            if not self.normalizer.same_origin(
                url,
                normalized,
            ):

                continue

            found.add(
                normalized
            )

        return sorted(found)