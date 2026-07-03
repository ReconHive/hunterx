"""
Subdomain Scanner
"""

from __future__ import annotations

import time

from hunterx.core.context import ScanContext

from hunterx.modules.subdomain.wordlist import Wordlist
from hunterx.modules.subdomain.bruteforce import Bruteforce
from hunterx.modules.subdomain.wildcard import WildcardDetector


class SubdomainScanner:

    def __init__(self) -> None:

        self.wordlist = Wordlist()

        self.detector = WildcardDetector()

        self.bruteforce = Bruteforce()

    def scan(
        self,
        context: ScanContext,
    ) -> list[str]:

        context.logger.info(
            "Checking wildcard DNS..."
        )

        wildcard = self.detector.detect(
            context
        )

        if wildcard:

            context.logger.warning(
                "Wildcard DNS detected."
            )

        else:

            context.logger.success(
                "Wildcard DNS not detected."
            )

        context.logger.info(
            "Starting subdomain scan..."
        )

        start = time.perf_counter()

        words = self.wordlist.load()

        hosts = self.bruteforce.scan(
            context,
            words,
        )

        elapsed = (
            time.perf_counter() - start
        )

        for host in hosts:

            context.logger.success(host)

        context.logger.info(
            f"Found {len(hosts)} subdomains."
        )

        context.logger.info(
            f"Elapsed: {elapsed:.2f}s"
        )

        return hosts