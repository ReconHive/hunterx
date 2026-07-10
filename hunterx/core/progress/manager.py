from __future__ import annotations

from hunterx.core.logger import logger


class ProgressManager:

    def __init__(self) -> None:

        self.total = 0
        self.current = 0

    def start(
        self,
        total: int,
    ) -> None:

        self.total = total
        self.current = 0

    def plugin(
        self,
        name: str,
    ) -> None:

        self.current += 1

        logger.blank()

        logger.info(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

        logger.info(
            f"[{self.current}/{self.total}] {name.upper()}"
        )

        logger.info(
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        )

    def finish(self) -> None:

        logger.blank()

        logger.success(
            "All plugins finished."
        )