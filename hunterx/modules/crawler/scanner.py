from __future__ import annotations

import time

from hunterx.cli.tables import key_value
from hunterx.cli.tables import simple

from hunterx.core.context import ScanContext
from hunterx.core.result import CrawlerResult

from hunterx.modules.crawler.manager import CrawlerManager


class CrawlerScanner:

    def __init__(self) -> None:

        self.manager = CrawlerManager()

    def scan(
        self,
        context: ScanContext,
    ) -> CrawlerResult:

        start = time.perf_counter()

        result = self.manager.scan(
            context,
        )

        elapsed = (
            time.perf_counter()
            - start
        )

        key_value(
            "Crawler Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "URLs",
                    str(len(result.urls)),
                ),
                (
                    "robots.txt entries",
                    str(len(result.robots)),
                ),
                (
                    "sitemap.xml URLs",
                    str(len(result.sitemap)),
                ),
                (
                    "Elapsed",
                    f"{elapsed:.2f}s",
                ),
            ],
        )

        if result.urls:

            simple(
                "Discovered URLs",
                "URL",
                result.urls,
            )

        else:

            context.logger.warning(
                "No URLs discovered."
            )

        if result.robots:

            simple(
                "robots.txt",
                "Path",
                result.robots,
            )

        if result.sitemap:

            simple(
                "sitemap.xml",
                "URL",
                result.sitemap,
            )

        return result