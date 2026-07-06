from __future__ import annotations

from queue import Queue
from threading import Lock
from threading import Thread
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

        workers = context.config.scanner.workers

        root = f"https://{context.target}"

        queue: Queue[tuple[str, int] | None] = Queue()

        queue.put(
            (
                root,
                0,
            )
        )

        visited: set[str] = set()

        discovered: set[str] = set()

        lock = Lock()

        def worker() -> None:

            while True:

                item = queue.get()

                if item is None:

                    queue.task_done()

                    break

                url, depth = item

                try:

                    with lock:

                        if url in visited:
                            continue

                        if len(visited) >= config.max_pages:
                            continue

                        visited.add(url)

                    if depth > config.depth:
                        continue

                    try:

                        response = context.http.get(
                            url,
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
                        "application/xhtml+xml" not in content_type
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
                        ).split("#")[0]

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

                        with lock:

                            if absolute in discovered:
                                continue

                            discovered.add(
                                absolute,
                            )

                        queue.put(
                            (
                                absolute,
                                depth + 1,
                            )
                        )

                finally:

                    queue.task_done()

        threads: list[Thread] = []

        for _ in range(workers):

            thread = Thread(
                target=worker,
                daemon=True,
            )

            thread.start()

            threads.append(
                thread,
            )

        queue.join()

        for _ in range(workers):

            queue.put(None)

        for thread in threads:

            thread.join()

        return sorted(
            discovered,
        )