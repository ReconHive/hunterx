from __future__ import annotations

from bs4 import BeautifulSoup


class SitemapParser:

    def parse(
        self,
        xml: str,
    ) -> list[str]:

        soup = BeautifulSoup(
            xml,
            "xml",
        )

        urls = []

        for loc in soup.find_all("loc"):

            if loc.text:

                urls.append(
                    loc.text.strip()
                )

        return sorted(
            set(urls)
        )