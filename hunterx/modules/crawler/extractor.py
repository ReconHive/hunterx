from __future__ import annotations

from bs4 import BeautifulSoup


class LinkExtractor:

    def extract(
        self,
        html: str,
    ) -> list[str]:

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        urls: list[str] = []

        for tag in soup.find_all(
            "a",
            href=True,
        ):

            urls.append(
                tag["href"]
            )

        return urls