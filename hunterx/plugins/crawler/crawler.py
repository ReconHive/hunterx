from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.crawler import WebCrawler
from hunterx.plugins.base import Plugin


class CrawlerPlugin(Plugin):

    name = "crawler"

    def __init__(self) -> None:

        self.crawler = WebCrawler()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Starting crawler..."
        )

        urls = self.crawler.crawl(
            context,
        )

        context.result.crawler.urls = urls

        context.logger.success(
            f"Found {len(urls)} URLs"
        )

        for url in urls:

            context.logger.success(
                url
            )