"""
Wordlist Loader
"""

from __future__ import annotations

from pathlib import Path


class Wordlist:

    def load(self) -> list[str]:

        path = (
            Path(__file__).parent
            / "wordlist.txt"
        )

        with path.open(
            encoding="utf-8"
        ) as file:

            return [
                line.strip()
                for line in file
                if line.strip()
            ]