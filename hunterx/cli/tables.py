from __future__ import annotations

from rich.table import Table

from hunterx.cli.console import console


def key_value(
    title: str,
    rows: list[tuple[str, str]],
) -> None:

    table = Table(
        title=f"[bold cyan]{title}[/bold cyan]",
        border_style="bright_blue",
        header_style="bold cyan",
        show_header=True,
        expand=False,
        pad_edge=True,
    )

    table.add_column(
        "Key",
        style="bold cyan",
        no_wrap=True,
        width=22,
    )

    table.add_column(
        "Value",
        style="white",
    )

    for key, value in rows:

        table.add_row(
            str(key),
            str(value),
        )

    console.print(table)


def simple(
    title: str,
    column: str,
    rows: list[str],
) -> None:

    table = Table(
        title=f"[bold cyan]{title}[/bold cyan]",
        border_style="bright_blue",
        header_style="bold cyan",
        show_header=True,
        expand=False,
        pad_edge=True,
    )

    table.add_column(
        "#",
        justify="right",
        style="cyan",
        width=4,
    )

    table.add_column(
        column,
        style="white",
    )

    for index, row in enumerate(
        rows,
        start=1,
    ):

        table.add_row(
            str(index),
            str(row),
        )

    console.print(table)


def status(
    title: str,
    rows: list[tuple[str, bool, str]],
) -> None:

    table = Table(
        title=f"[bold cyan]{title}[/bold cyan]",
        border_style="bright_blue",
        header_style="bold cyan",
        show_header=True,
        expand=False,
        pad_edge=True,
    )

    table.add_column(
        "Item",
        style="bold cyan",
        no_wrap=True,
    )

    table.add_column(
        "Status",
        justify="center",
        no_wrap=True,
    )

    table.add_column(
        "Value",
        style="white",
    )

    for name, ok, value in rows:

        table.add_row(
            name,
            "[green]✓[/green]" if ok else "[yellow]⚠[/yellow]",
            value,
        )

    console.print(table)