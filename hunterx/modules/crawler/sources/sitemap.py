from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.sitemap import SitemapParser
from hunterx.modules.crawler.source import CrawlerSource


class SitemapSource(CrawlerSource):

    name = "sitemap.xml"

    field = "sitemap"

    def __init__(self) -> None:

        self.parser = SitemapParser()

    def fetch(
        self,
        context: ScanContext,
    ) -> list[str]:

        url = f"https://{context.target}/sitemap.xml"

        try:

            response = context.http.get(
                url,
            )

        except Exception:

            return []

        if response.status_code != 200:

            return []

        return self.parser.parse(
            response.text,
        )