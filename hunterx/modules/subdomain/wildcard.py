"""
Wildcard DNS Detection
"""

from __future__ import annotations

import uuid

from hunterx.core.context import ScanContext


class WildcardDetector:

    def detect(
        self,
        context: ScanContext,
    ) -> bool:
        """
        Return True if wildcard DNS is enabled.
        """

        random_host = (
            f"hunterx-{uuid.uuid4().hex}.{context.target}"
        )

        try:

            context.dns.resolve(random_host)

            return True

        except Exception:

            return False