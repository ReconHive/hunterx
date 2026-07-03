from __future__ import annotations

from hunterx.plugins.registry import PluginRegistry

from hunterx.plugins.dns.plugin import DNSPlugin
from hunterx.plugins.http.plugin import HTTPPlugin
from hunterx.plugins.subdomain.plugin import SubdomainPlugin


class PluginLoader:

    def __init__(self) -> None:

        self.registry = PluginRegistry()

    def load(self) -> PluginRegistry:

        self.registry.register(DNSPlugin())

        self.registry.register(HTTPPlugin())

        self.registry.register(SubdomainPlugin())

        return self.registry