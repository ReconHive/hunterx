from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.dns import DNSPool
from hunterx.core.events.bus import EventBus
from hunterx.core.hooks.manager import HookManager
from hunterx.core.http import HTTPPool
from hunterx.core.metrics.manager import MetricsManager
from hunterx.core.cache.manager import CacheManager

class ServiceContainer:

    def __init__(
        self,
        config: Config,
    ) -> None:

        self.config = config

        self.http = HTTPPool(config)

        self.dns = DNSPool(config)

        self.events = EventBus()

        self.metrics = MetricsManager()

        self.hooks = HookManager()

        from hunterx.core.hooks.timing import TimingHook

        self.hooks.register(
            TimingHook()
        )

        from hunterx.core.metrics.hook import MetricsHook

        self.hooks.register(
            MetricsHook()
        )

        self.cache = CacheManager()

    def close(self) -> None:

        self.http.close()

        self.events.clear()

        self.hooks.clear()
        