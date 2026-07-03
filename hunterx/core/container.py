from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.dns import DNSPool
from hunterx.core.events.bus import EventBus
from hunterx.core.http import HTTPPool


class ServiceContainer:

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.config = config

        self.http = HTTPPool(config)

        self.dns = DNSPool(config)

        self.events = EventBus()

    def close(self) -> None:

        self.http.close()

        self.events.clear()