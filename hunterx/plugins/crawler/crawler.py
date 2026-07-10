from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.scanner import CrawlerScanner
from hunterx.plugins.base import Plugin


class CrawlerPlugin(Plugin):

    name = "crawler"

    def __init__(self) -> None:

        self.scanner = CrawlerScanner()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        result = self.scanner.scan(
            context,
        )

        context.result.crawler.urls = result.urls

        context.result.crawler.robots = result.robots

        context.result.crawler.sitemap = result.sitemap

        self.save_workspace(
            context,
            context.result.crawler,
        )