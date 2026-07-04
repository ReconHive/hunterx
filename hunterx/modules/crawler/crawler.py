from __future__ import annotations

from collections import deque
from urllib.parse import urljoin
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from hunterx.core.context import ScanContext


class WebCrawler:

    def crawl(
        self,
        context: ScanContext,
    ) -> list[str]:

        config = context.config.crawler

        root = f"https://{context.target}"

        queue = deque()

        queue.append(
            (
                root,
                0,
            )
        )

        visited: set[str] = set()

        discovered: set[str] = set()

        while queue:

            url, depth = queue.popleft()

            if url in visited:

                continue

            visited.add(url)

            if depth > config.depth:

                continue

            if len(visited) >= config.max_pages:

                break

            try:

                response = context.http.client.get(
                    url
                )

            except Exception:

                continue

            content_type = response.headers.get(
                "Content-Type",
                "",
            ).lower()

            if (
                "text/html" not in content_type
                and
                "application/xhtml+xml"
                not in content_type
            ):

                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser",
            )

            for tag in soup.find_all(
                "a",
                href=True,
            ):

                href = tag["href"]

                absolute = urljoin(
                    url,
                    href,
                )

                absolute = absolute.split(
                    "#",
                )[0]

                parsed = urlparse(
                    absolute,
                )

                if parsed.scheme not in (
                    "http",
                    "https",
                ):

                    continue

                if (
                    config.internal_only
                    and parsed.netloc != context.target
                ):

                    continue

                if absolute not in discovered:

                    discovered.add(
                        absolute,
                    )

                    queue.append(
                        (
                            absolute,
                            depth + 1,
                        )
                    )

        return sorted(
            discovered,
        )