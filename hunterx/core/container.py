"""
HunterX Service Container
"""

from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.http import HTTPPool
from hunterx.core.dns import DNSPool


class ServiceContainer:

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.config = config

        self.http = HTTPPool(config)

        self.dns = DNSPool(config)

    def close(self) -> None:

        self.http.close()