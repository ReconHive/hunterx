from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.javascript.common import MAX_JS_SIZE


class JavaScriptDownloader:

    def download(
        self,
        context: ScanContext,
        url: str,
    ) -> str | None:

        response = context.http.get(
            url,
        )

        if response is None:
            return None

        if response.status_code != 200:
            return None

        content_type = response.headers.get(
            "Content-Type",
            "",
        ).lower()

        if "javascript" not in content_type and not url.endswith(
            (
                ".js",
                ".mjs",
            )
        ):
            return None

        text = response.text

        if len(text) > MAX_JS_SIZE:
            return None

        return text