"""
Subdomain Scanner
"""

from __future__ import annotations

from hunterx.core.logger import logger

from hunterx.modules.subdomain.wordlist import Wordlist
from hunterx.modules.subdomain.bruteforce import Bruteforce


class SubdomainScanner:

    def __init__(self):

        self.wordlist = Wordlist()

        self.bruteforce = Bruteforce()

    def scan(self, target: str):

        logger.info("Starting subdomain scan...")

        words = self.wordlist.load()

        hosts = self.bruteforce.scan(
            target,
            words,
        )

        for host in hosts:

            logger.success(host)

        logger.info(
            f"Found {len(hosts)} subdomains."
        )