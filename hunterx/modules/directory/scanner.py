from __future__ import annotations

from hunterx.core.context import ScanContext
from hunterx.modules.directory.wordlist import DEFAULT_WORDLIST


class DirectoryScanner:

    VALID_STATUS = {
        200,
        204,
        301,
        302,
        307,
        308,
        401,
        403,
    }

    def scan(
        self,
        context: ScanContext,
    ) -> list[str]:

        base = f"https://{context.target}".rstrip("/")

        discovered: list[str] = []

        for word in DEFAULT_WORDLIST:

            url = f"{base}/{word}"

            try:

                response = context.http.client.get(
                    url,
                    follow_redirects=False,
                )

            except Exception:
                continue

            if response.status_code not in self.VALID_STATUS:
                continue

            line = f"[{response.status_code}] {url}"

            location = response.headers.get("Location")

            if location:
                line += f" -> {location}"

            discovered.append(line)

        return discovered