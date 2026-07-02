"""
Subdomain Scanner
"""

from __future__ import annotations
import time

from hunterx.core.logger import logger

from hunterx.modules.subdomain.wordlist import Wordlist
from hunterx.modules.subdomain.bruteforce import Bruteforce
from hunterx.modules.subdomain.wildcard import WildcardDetector


class SubdomainScanner:

    def __init__(self):

        self.wordlist = Wordlist()

        self.detector = WildcardDetector()

        self.bruteforce = Bruteforce()

    def scan(self, target: str):
        logger.info("Checking wildcard DNS...")

        wildcard = self.detector.detect(target)

        if wildcard:

            logger.warning(
                "Wildcard DNS detected."
            )

        else:

            logger.success(
                "Wildcard DNS not detected."
            )


        logger.info("Starting subdomain scan...")

        start = time.perf_counter()

        words = self.wordlist.load()

        hosts = self.bruteforce.scan(
            target,
            words,
        )

        elapsed = time.perf_counter() - start

        for host in hosts:

            logger.success(host)

        logger.info(
            f"Found {len(hosts)} subdomains."
        )

        logger.info(
            f"Elapsed: {elapsed:.2f}s"
        )