from __future__ import annotations

from hunterx.core.plugins import PluginCollection

from hunterx.plugins.crawler.crawler import CrawlerPlugin
from hunterx.plugins.directory.plugin import DirectoryPlugin
from hunterx.plugins.dns.plugin import DNSPlugin
from hunterx.plugins.http.plugin import HTTPPlugin
from hunterx.plugins.javascript.plugin import JavaScriptPlugin
from hunterx.plugins.ports.plugin import PortScannerPlugin
from hunterx.plugins.subdomain.plugin import SubdomainPlugin
from hunterx.plugins.takeover.plugin import TakeoverPlugin
from hunterx.plugins.tls.plugin import TLSPlugin
from hunterx.plugins.params.plugin import ParamsPlugin


class PluginLoader:

    def load(
        self,
    ) -> PluginCollection:

        plugins = PluginCollection()

        plugins.register(
            DNSPlugin(),
        )

        plugins.register(
            HTTPPlugin(),
        )

        plugins.register(
            SubdomainPlugin(),
        )

        plugins.register(
            CrawlerPlugin(),
        )

        plugins.register(
            DirectoryPlugin(),
        )

        plugins.register(
            PortScannerPlugin(),
        )

        plugins.register(
            TLSPlugin(),
        )

        plugins.register(
            JavaScriptPlugin(),
        )

        plugins.register(
            TakeoverPlugin(),
        )

        plugins.register(
            ParamsPlugin(),
        )

        return plugins