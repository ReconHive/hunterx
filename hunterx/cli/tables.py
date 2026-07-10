from __future__ import annotations

from rich.table import Table

import re

from hunterx.cli.console import console


_STATUS_RE = re.compile(
    r"^\[(\d{3})\]\s+(.*)$"
)


def _status_style(
    code: str,
) -> str:

    if not code.isdigit():
        return "white"

    value = int(code)

    if value in (401, 403):
        return "info"

    if value < 300:
        return "success"

    if value < 400:
        return "warning"

    return "error"


def directory_results(
    title: str,
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
        "Status",
        justify="center",
        width=8,
    )

    table.add_column(
        "URL",
        style="white",
    )

    for index, row in enumerate(
        rows,
        start=1,
    ):

        match = _STATUS_RE.match(row)

        if match:

            code = match.group(1)

            rest = match.group(2)

        else:

            code = "?"

            rest = row

        style = _status_style(code)

        table.add_row(
            str(index),
            f"[{style}]{code}[/{style}]",
            rest,
        )

    console.print(table)


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


def secrets(
    title: str,
    rows: list[str],
) -> None:

    table = Table(
        title=f"[bold error]{title}[/bold error]",
        border_style="error",
        header_style="bold error",
        show_header=True,
        expand=False,
        pad_edge=True,
    )

    table.add_column(
        "#",
        justify="right",
        style="error",
        width=4,
    )

    table.add_column(
        "Possible Secret",
        style="bold warning",
    )

    for index, row in enumerate(
        rows,
        start=1,
    ):

        if len(row) > 90:

            display = f"{row[:50]}...{row[-20:]}"

        else:

            display = row

        table.add_row(
            str(index),
            display,
        )

    console.print(table)


def preview(
    title: str,
    column: str,
    rows: list[str],
    limit: int = 15,
) -> None:

    total = len(rows)

    shown = rows[:limit]

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
        shown,
        start=1,
    ):

        table.add_row(
            str(index),
            str(row),
        )

    if total > limit:

        table.caption = (
            f"[dim]+ {total - limit} more — "
            "see javascript.json for full results[/dim]"
        )

    console.print(table)