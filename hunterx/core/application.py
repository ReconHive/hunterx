"""
HunterX Application Core
"""

from __future__ import annotations

from hunterx.core.config import Settings


class HunterX:
    """
    Main HunterX application.
    """

    VERSION = "0.1.0"

    def __init__(self) -> None:

        self.settings = Settings()

        self.initialized = False

    def initialize(self) -> None:

        self.initialized = True

    def run(self) -> None:

        if not self.initialized:
            self.initialize()