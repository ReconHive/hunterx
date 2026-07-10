from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.crawler import WebCrawler
from hunterx.modules.crawler.source import CrawlerSource


class LinksSource(CrawlerSource):

    name = "Links"

    field = "urls"

    def __init__(self) -> None:

        self.crawler = WebCrawler()

    def fetch(
        self,
        context: ScanContext,
    ) -> list[str]:

        return self.crawler.crawl(
            context,
        )