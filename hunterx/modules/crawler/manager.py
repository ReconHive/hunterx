from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.core.result import CrawlerResult

from hunterx.modules.crawler.sources import (
    LinksSource,
    RobotsSource,
    SitemapSource,
)


class CrawlerManager:

    def __init__(self) -> None:

        self.sources = [
            LinksSource(),
            RobotsSource(),
            SitemapSource(),
        ]

    def scan(
        self,
        context: ScanContext,
    ) -> CrawlerResult:

        result = CrawlerResult()

        context.logger.info(
            "Running crawler sources..."
        )

        for source in self.sources:

            try:

                items = source.fetch(
                    context,
                )

                existing = getattr(
                    result,
                    source.field,
                )

                merged = sorted(
                    set(existing) | set(items)
                )

                setattr(
                    result,
                    source.field,
                    merged,
                )

                context.logger.success(
                    f"{source.name:<12} {len(items)}"
                )

            except Exception as exc:

                context.logger.warning(
                    f"{source.name:<12} Failed ({exc})"
                )

        return result