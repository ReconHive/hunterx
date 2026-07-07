from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from hunterx.core.context import ScanContext
from hunterx.modules.javascript.models import JavaScriptResult
from hunterx.modules.javascript.worker import JavaScriptWorker


class JavaScriptScanner:

    def __init__(self) -> None:

        self.worker = JavaScriptWorker()

    def scan(
        self,
        context: ScanContext,
    ) -> JavaScriptResult:

        result = JavaScriptResult()

        js_files = []

        for url in context.result.crawler.urls:

            if url.endswith(
                (
                    ".js",
                    ".mjs",
                )
            ):
                js_files.append(url)

        if not js_files:
            return result

        workers = context.config.scanner.workers

        with ThreadPoolExecutor(
            max_workers=workers,
        ) as executor:

            futures = [

                executor.submit(
                    self.worker.process,
                    context,
                    url,
                )

                for url in js_files

            ]

            for future in as_completed(
                futures,
            ):

                data = future.result()

                if data is None:
                    continue

                result.files.append(
                    data["url"],
                )

                result.endpoints.extend(
                    data["endpoints"],
                )

                result.urls.extend(
                    data["urls"],
                )

                result.domains.extend(
                    data["domains"],
                )

                result.secrets.extend(
                    data["secrets"],
                )

        result.files = sorted(
            set(result.files),
        )

        result.urls = sorted(
            set(result.urls),
        )

        result.domains = sorted(
            set(result.domains),
        )

        result.endpoints = sorted(
            set(result.endpoints),
        )

        result.secrets = sorted(
            set(result.secrets),
        )

        return result