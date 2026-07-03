from __future__ import annotations

from hunterx.plugins.registry import PluginRegistry

from hunterx.plugins.http.plugin import HTTPPlugin
from hunterx.plugins.dns.plugin import DNSPlugin


class PluginLoader:

    def __init__(self) -> None:

        self.registry = PluginRegistry()

    def load(self) -> PluginRegistry:

        self.registry.register(DNSPlugin())

        self.registry.register(HTTPPlugin())

        return self.registry