from __future__ import annotations

from hunterx.core.plugins import PluginCollection

from hunterx.plugins.dns.plugin import DNSPlugin
from hunterx.plugins.http.plugin import HTTPPlugin
from hunterx.plugins.subdomain.plugin import SubdomainPlugin


class PluginLoader:

    def load(self) -> PluginCollection:

        plugins = PluginCollection()

        plugins.register(DNSPlugin())

        plugins.register(HTTPPlugin())

        plugins.register(SubdomainPlugin())

        return plugins