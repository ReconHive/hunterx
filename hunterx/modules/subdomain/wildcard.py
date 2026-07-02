"""
Wildcard DNS Detection
"""

from __future__ import annotations

import uuid

from hunterx.core.dns import DNSPool


class WildcardDetector:

    def __init__(self) -> None:
        self.pool = DNSPool()

    def detect(self, target: str) -> bool:
        """
        Return True if wildcard DNS is enabled.
        """

        random_host = (
            f"hunterx-{uuid.uuid4().hex}.{target}"
        )

        try:
            self.pool.resolve(random_host)
            return True

        except Exception:
            return False