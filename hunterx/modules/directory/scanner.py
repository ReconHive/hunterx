from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from hunterx.core.context import ScanContext
from hunterx.modules.directory.wordlist import DEFAULT_WORDLIST


class DirectoryScanner:

    def scan(
        self,
        context: ScanContext,
    ) -> list[str]:

        config = context.config.directory

        base = f"https://{context.target}".rstrip("/")

        #
        # Load wordlist
        #

        words = DEFAULT_WORDLIST

        if config.wordlist:

            path = Path(config.wordlist).expanduser()

            if not path.is_absolute():
                path = Path.cwd() / path

            if path.exists() and path.is_file():

                try:

                    words = [
                        line.strip()
                        for line in path.read_text(
                            encoding="utf-8",
                            errors="ignore",
                        ).splitlines()
                        if line.strip()
                        and not line.startswith("#")
                    ]

                    context.logger.success(
                        f"Loaded {len(words)} words from {path}"
                    )

                except Exception as exc:

                    context.logger.warning(
                        f"Failed to read wordlist: {exc}"
                    )

            else:

                context.logger.warning(
                    f"Wordlist not found: {path}"
                )

        #
        # Build targets
        #

        targets: list[str] = []

        for word in words:

            targets.append(word)

            if "." not in word:

                for ext in config.extensions:

                    targets.append(
                        f"{word}.{ext}"
                    )

        #
        # Worker count
        #

        workers = (
            config.threads
            if config.threads is not None
            else context.config.scanner.workers
        )

        discovered: list[str] = []

        def request(path: str) -> str | None:

            url = f"{base}/{path}"

            try:

                response = context.http.client.get(
                    url,
                    follow_redirects=config.follow_redirects,
                )

            except Exception:
                return None

            if response.status_code not in config.include_status:
                return None

            if response.status_code in config.exclude_status:
                return None

            line = f"[{response.status_code}] {url}"

            location = response.headers.get(
                "Location"
            )

            if location:

                line += f" -> {location}"

            return line

        #
        # Multithreaded scan
        #

        with ThreadPoolExecutor(
            max_workers=workers,
        ) as executor:

            futures = [
                executor.submit(
                    request,
                    target,
                )
                for target in targets
            ]

            for future in as_completed(
                futures,
            ):

                result = future.result()

                if result is not None:

                    discovered.append(
                        result
                    )

        discovered.sort()

        return discovered