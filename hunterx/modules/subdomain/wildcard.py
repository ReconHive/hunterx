"""
Wildcard DNS Detection
"""

from __future__ import annotations

import socket
import uuid


class WildcardDetector:

    def detect(self, target: str) -> bool:
        """
        Return True if wildcard DNS is enabled.
        """

        random_host = (
            f"hunterx-{uuid.uuid4().hex}.{target}"
        )

        try:

            socket.gethostbyname(random_host)

            return True

        except socket.gaierror:

            return False