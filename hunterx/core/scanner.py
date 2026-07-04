"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.core.config import Config
from hunterx.core.container import ServiceContainer
from hunterx.core.context import ScanContext
from hunterx.core.events.events import (
    PluginFinished,
    PluginStarted,
    ScanFinished,
    ScanStarted,
)
from hunterx.core.hooks.logger import LoggerHook
from hunterx.core.logger import logger
from hunterx.core.result import ScanResult
from hunterx.plugins.loader import PluginLoader


class ScanEngine:
    """
    Coordinates all plugins.
    """

    def __init__(
        self,
        config: Config,
        result: ScanResult,
    ) -> None:

        self.config = config
        self.result = result

        loader = PluginLoader()
        self.plugins = loader.load()

    def run(
        self,
        target: str,
        plugins: list[str] | None = None,
        custom_headers: dict[str, str] | None = None,
    ) -> None:

        container = ServiceContainer(
            self.config,
        )

        container.hooks.register(
            LoggerHook()
        )

        selected = self.plugins.select(
            plugins
        )

        context = ScanContext(
            target=target,
            config=self.config,
            result=self.result,
            container=container,
            http=container.http,
            dns=container.dns,
            events=container.events,
            metrics=container.metrics,
            progress=container.progress,
            cache=container.cache,
            selected_plugins=selected,
            custom_headers=custom_headers or {},
        )

        container.hooks.before_scan(
            context,
        )

        context.events.publish(
            ScanStarted(
                target=target,
            )
        )

        selected = self.plugins.select(
            plugins,
        )

        if plugins and not selected:

            logger.warning(
                "No matching plugins were found."
            )

            container.close()

            return

        for plugin in selected:

            container.hooks.before_plugin(
                context,
                plugin,
            )

            context.events.publish(
                PluginStarted(
                    plugin=plugin.name,
                )
            )

            plugin.run(
                context,
            )

            context.events.publish(
                PluginFinished(
                    plugin=plugin.name,
                )
            )

            container.hooks.after_plugin(
                context,
                plugin,
            )

        context.events.publish(
            ScanFinished(
                target=target,
            )
        )

        container.hooks.after_scan(
            context,
        )

        logger.info("Metrics")

        logger.success(
            f"Elapsed : {context.metrics.elapsed:.2f}s"
        )

        for name, elapsed in (
            context.metrics.metrics.plugins.items()
        ):

            logger.success(
                f"{name} : {elapsed:.2f}s"
            )

        container.close()