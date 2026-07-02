"""
Subdomain Scanner
"""

from __future__ import annotations

import socket

from hunterx.core.logger import logger


class SubdomainScanner:

    def __init__(self) -> None:

        with open(
            "hunterx/modules/subdomain/wordlist.txt",
            encoding="utf-8",
        ) as f:

            self.words = [
                line.strip()
                for line in f
                if line.strip()
            ]

    def scan(self, target: str) -> None:

        logger.info("Starting subdomain scan...")

        found = 0

        for word in self.words:

            host = f"{word}.{target}"

            try:

                socket.gethostbyname(host)

                logger.success(host)

                found += 1

            except socket.gaierror:
                pass

        logger.info(f"Found {found} subdomains.")