from rich.panel import Panel

from hunterx.cli.console import console


def section(
    title: str,
) -> None:

    console.print(
        Panel.fit(
            "",
            title=f"[header]{title}[/header]",
            border_style="border",
        )
    )