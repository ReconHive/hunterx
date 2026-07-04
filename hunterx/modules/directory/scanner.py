from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.directory.wordlist import DEFAULT_WORDLIST


class DirectoryScanner:

    def scan(
        self,
        context: ScanContext,
    ) -> list[str]:

        config = context.config.directory

        base = f"https://{context.target}".rstrip("/")

        discovered: list[str] = []

        for word in DEFAULT_WORDLIST:

            url = f"{base}/{word}"

            try:

                response = context.http.client.get(
                    url,
                    follow_redirects=config.follow_redirects,
                )

            except Exception:
                continue

            if response.status_code not in config.include_status:
                continue

            if response.status_code in config.exclude_status:
                continue

            line = f"[{response.status_code}] {url}"

            location = response.headers.get("Location")

            if location:

                line += f" -> {location}"

            discovered.append(line)

        return discovered