from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.crawler.crawler import WebCrawler
from hunterx.modules.crawler.robots import RobotsParser
from hunterx.modules.crawler.sitemap import SitemapParser
from hunterx.plugins.base import Plugin


class CrawlerPlugin(Plugin):

    name = "crawler"

    def __init__(self) -> None:

        self.crawler = WebCrawler()

        self.robots = RobotsParser()

        self.sitemap = SitemapParser()

    def run(
        self,
        context: ScanContext,
    ) -> None:

        context.logger.info(
            "Starting crawler..."
        )

        crawl_urls = self.crawler.crawl(
            context,
        )

        context.result.crawler.urls = (
            crawl_urls
        )

        base = f"https://{context.target}"

        #
        # robots.txt
        #

        context.logger.info(
            "Checking robots.txt..."
        )

        try:

            response = context.http.client.get(
                f"{base}/robots.txt"
            )

            if response.status_code == 200:

                robot_paths = self.robots.parse(
                    response.text
                )

                context.result.crawler.robots = (
                    robot_paths
                )

                if robot_paths:

                    context.logger.success(
                        f"robots.txt ({len(robot_paths)} entries)"
                    )

                    for path in robot_paths:

                        context.logger.success(
                            path
                        )

                else:

                    context.logger.warning(
                        "robots.txt is empty."
                    )

            else:

                context.logger.warning(
                    "robots.txt not found."
                )

        except Exception:

            context.logger.warning(
                "Failed to retrieve robots.txt."
            )

        #
        # sitemap.xml
        #

        context.logger.info(
            "Checking sitemap.xml..."
        )

        try:

            response = context.http.client.get(
                f"{base}/sitemap.xml"
            )

            if response.status_code == 200:

                sitemap_urls = self.sitemap.parse(
                    response.text
                )

                context.result.crawler.sitemap = (
                    sitemap_urls
                )

                if sitemap_urls:

                    context.logger.success(
                        f"sitemap.xml ({len(sitemap_urls)} URLs)"
                    )

                    for url in sitemap_urls:

                        context.logger.success(
                            url
                        )

                else:

                    context.logger.warning(
                        "sitemap.xml is empty."
                    )

            else:

                context.logger.warning(
                    "sitemap.xml not found."
                )

        except Exception:

            context.logger.warning(
                "Failed to retrieve sitemap.xml."
            )

        #
        # Crawl Results
        #

        context.logger.success(
            f"Crawler discovered {len(crawl_urls)} URLs"
        )

        for url in crawl_urls:

            context.logger.success(
                url
            )