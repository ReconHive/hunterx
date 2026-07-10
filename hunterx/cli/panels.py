from __future__ import annotations

from rich.panel import Panel
from rich.table import Table

from hunterx.cli.console import console


def section(
    title: str,
) -> None:

    console.print(
        Panel.fit(
            "",
            title=f"[bold cyan]{title}[/bold cyan]",
            border_style="bright_blue",
            padding=(0, 2),
        )
    )


def scan_configuration(
    context,
) -> None:

    table = Table(
        show_header=False,
        box=None,
        pad_edge=False,
        expand=False,
    )

    table.add_column(
        style="bold cyan",
        no_wrap=True,
    )

    table.add_column(
        style="white",
    )

    plugins = ", ".join(
        plugin.name
        for plugin in context.selected_plugins
    )

    workspace = (
        f"./.hunterx/{context.target}"
    )

    table.add_row(
        "Target",
        context.target,
    )

    table.add_row(
        "Plugins",
        plugins,
    )

    table.add_row(
        "Method",
        context.method,
    )

    table.add_row(
        "Workspace",
        workspace,
    )

    table.add_row(
        "Cache",
        "Enabled",
    )

    console.print(
        Panel.fit(
            table,
            title="[bold cyan]Scan Configuration[/bold cyan]",
            border_style="bright_blue",
            padding=(0, 2),
        )
    )