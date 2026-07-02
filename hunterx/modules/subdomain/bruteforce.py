"""
Subdomain Bruteforce Engine
"""

from __future__ import annotations

import socket


class Bruteforce:

    def scan(
        self,
        target: str,
        words: list[str],
    ) -> list[str]:

        found = []

        for word in words:

            host = f"{word}.{target}"

            try:

                socket.gethostbyname(host)

                found.append(host)

            except socket.gaierror:

                continue

        return found