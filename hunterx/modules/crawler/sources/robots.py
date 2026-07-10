from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.robots import RobotsParser
from hunterx.modules.crawler.source import CrawlerSource


class RobotsSource(CrawlerSource):

    name = "robots.txt"

    field = "robots"

    def __init__(self) -> None:

        self.parser = RobotsParser()

    def fetch(
        self,
        context: ScanContext,
    ) -> list[str]:

        url = f"https://{context.target}/robots.txt"

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