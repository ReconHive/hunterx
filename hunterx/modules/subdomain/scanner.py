"""
Subdomain Scanner
"""

from __future__ import annotations

import time

from hunterx.cli.tables import key_value
from hunterx.cli.tables import simple

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

        start = time.perf_counter()

        wildcard = self.detector.detect(
            context,
        )

        words = self.wordlist.load()

        hosts = self.bruteforce.scan(
            context,
            words,
        )

        elapsed = (
            time.perf_counter()
            - start
        )

        key_value(
            "Discovery Summary",
            [
                (
                    "Target",
                    context.target,
                ),
                (
                    "Wordlist",
                    "common.txt",
                ),
                (
                    "Wildcard DNS",
                    "Detected"
                    if wildcard
                    else "Not Detected",
                ),
                (
                    "Subdomains",
                    str(len(hosts)),
                ),
                (
                    "Elapsed",
                    f"{elapsed:.2f}s",
                ),
            ],
        )

        if hosts:

            simple(
                "Discovered Subdomains",
                "Host",
                sorted(hosts),
            )

        else:

            context.logger.warning(
                "No subdomains found."
            )

        return hosts