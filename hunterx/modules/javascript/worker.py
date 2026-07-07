from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.javascript.downloader import JavaScriptDownloader
from hunterx.modules.javascript.parser import JavaScriptParser


class JavaScriptWorker:

    def __init__(self) -> None:

        self.downloader = JavaScriptDownloader()

        self.parser = JavaScriptParser()

    def process(
        self,
        context: ScanContext,
        url: str,
    ) -> dict | None:

        source = self.downloader.download(
            context,
            url,
        )

        if source is None:
            return None

        data = self.parser.parse(
            source,
        )

        data["url"] = url

        data["source"] = source

        return data