"""
HunterX Scan Engine
"""

from __future__ import annotations

from hunterx.cli.progress import progress

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

    def _resolve_dependencies(
        self,
        context: ScanContext,
        selected: list,
    ) -> list:

        names = {
            plugin.name
            for plugin in selected
        }

        #
        # params -> crawler
        #

        if (
            "params" in names
            and "crawler" not in names
        ):

            if context.workspace.exists(
                context.target,
                "crawler",
            ):

                logger.info(
                    "Loading crawler data from workspace..."
                )

                data = context.workspace.load(
                    context.target,
                    "crawler",
                )

                if data:

                    context.result.crawler.urls = data.get(
                        "urls",
                        [],
                    )

                    context.result.crawler.robots = data.get(
                        "robots",
                        [],
                    )

                    context.result.crawler.sitemap = data.get(
                        "sitemap",
                        [],
                    )

            else:

                crawler = self.plugins.get(
                    "crawler",
                )

                if crawler is not None:

                    logger.info(
                        "Crawler workspace not found."
                    )

                    logger.info(
                        "Running crawler automatically..."
                    )

                    selected.insert(
                        0,
                        crawler,
                    )











        #
        # javascript -> crawler
        #

        if (
            "javascript" in names
            and "crawler" not in names
        ):

            if context.workspace.exists(
                context.target,
                "crawler",
            ):

                logger.info(
                    "Loading crawler data from workspace..."
                )

                data = context.workspace.load(
                    context.target,
                    "crawler",
                )

                if data:

                    context.result.crawler.urls = data.get(
                        "urls",
                        [],
                    )

                    context.result.crawler.robots = data.get(
                        "robots",
                        [],
                    )

                    context.result.crawler.sitemap = data.get(
                        "sitemap",
                        [],
                    )

            else:

                crawler = self.plugins.get(
                    "crawler",
                )

                if crawler is not None:

                    logger.info(
                        "Crawler workspace not found."
                    )

                    logger.info(
                        "Running crawler automatically..."
                    )

                    selected.insert(
                        0,
                        crawler,
                    )

        #
        # takeover -> subdomain
        #

        if (
            "takeover" in names
            and "subdomain" not in names
        ):

            if context.workspace.exists(
                context.target,
                "subdomain",
            ):

                logger.info(
                    "Loading subdomain data from workspace..."
                )

                data = context.workspace.load(
                    context.target,
                    "subdomain",
                )

                if data:

                    context.result.subdomains.hosts = data.get(
                        "hosts",
                        [],
                    )

            else:

                subdomain = self.plugins.get(
                    "subdomain",
                )

                if subdomain is not None:

                    logger.info(
                        "Subdomain workspace not found."
                    )

                    logger.info(
                        "Running subdomain scan automatically..."
                    )

                    selected.insert(
                        0,
                        subdomain,
                    )

        return selected

    def run(
        self,
        target: str,
        plugins: list[str] | None = None,
        custom_headers: dict[str, str] | None = None,
        method: str = "GET",
    ) -> None:

        container = ServiceContainer(
            self.config,
        )

        container.hooks.register(
            LoggerHook(),
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
            workspace=container.workspace,
            selected_plugins=selected,
            custom_headers=custom_headers or {},
            method=method.upper(),
        )

        selected = self._resolve_dependencies(
            context,
            selected,
        )

        context.selected_plugins = selected

        container.hooks.before_scan(
            context,
        )

        context.events.publish(
            ScanStarted(
                target=target,
            )
        )

        task = progress.add_task(
            "Running plugins...",
            total=len(selected),
        )

        progress.start()

        for plugin in selected:

            progress.update(
                task,
                description=f"[bold cyan]{plugin.name.upper()}",
            )

            progress.stop()

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

            progress.start()

            progress.advance(task)

            progress.stop()

        #
        # Everything below now runs ONCE, after all plugins finish
        #

        context.events.publish(
            ScanFinished(
                target=target,
            )
        )

        container.hooks.after_scan(
            context,
        )

        logger.blank()
        logger.success("Scan completed")

        logger.blank()
        logger.line()
        logger.success("Metrics")
        logger.line()

        logger.success(
            f"{'Total':<15} {context.metrics.elapsed:.2f}s"
        )

        for name, elapsed in context.metrics.metrics.plugins.items():

            logger.success(
                f"{name.upper():<15} {elapsed:.2f}s"
            )

        logger.blank()

        container.close()