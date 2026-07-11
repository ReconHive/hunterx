from __future__ import annotations

from rich.table import Table

import re

from hunterx.cli.console import console


_STATUS_RE = re.compile(
    r"^\[(\d{3})\]\s+(.*)$"
)

_FINDING_SEVERITY = {
    "Expired Certificate": "error",
    "Certificate expires soon": "warning",
    "Self Signed Certificate": "warning",
    "Wildcard Certificate": "info",
}

_SEVERITY_ICON = {
    "error": "✗",
    "warning": "⚠",
    "info": "ℹ",
}

_SENSITIVE_SERVICES = {
    "ftp": "warning",
    "ftp-data": "warning",
    "telnet": "error",
    "rpcbind": "warning",
    "netbios": "warning",
    "smb": "error",
    "mssql": "error",
    "oracle": "error",
    "docker": "error",
    "mysql": "error",
    "rdp": "error",
    "postgres": "error",
    "vnc": "error",
    "winrm": "error",
    "redis": "error",
    "elasticsearch": "error",
    "memcached": "warning",
    "mongodb": "error",
    "nfs": "warning",
}

_CONFIDENCE_STYLE = {
    "high": "error",
    "medium": "warning",
    "low": "info",
}


def takeover_findings(
    title: str,
    rows: list[dict],
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
        "Host",
        style="white",
    )

    table.add_column(
        "Service",
        style="bold warning",
    )

    table.add_column(
        "CNAME",
        style="white",
    )

    table.add_column(
        "Signal",
        justify="center",
        width=12,
    )

    table.add_column(
        "Confidence",
        justify="center",
        width=10,
    )

    for index, row in enumerate(
        rows,
        start=1,
    ):

        signal = (
            "Dangling DNS"
            if row["dangling_dns"]
            else row["matched_via"].replace(
                "_",
                " ",
            ).title()
        )

        confidence = row.get(
            "confidence",
            "medium",
        )

        style = _CONFIDENCE_STYLE.get(
            confidence,
            "warning",
        )

        table.add_row(
            str(index),
            row["host"],
            row["service"],
            row["cname"],
            signal,
            f"[{style}]{confidence.upper()}[/{style}]",
        )

    console.print(table)


def _service_style(
    service: str,
) -> str:

    return _SENSITIVE_SERVICES.get(
        service,
        "success",
    )


def ports_table(
    title: str,
    ports: list[int],
    services: dict[int, str],
    versions: dict[int, str | None],
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
        "Port",
        justify="right",
        width=8,
    )

    table.add_column(
        "Service",
        width=16,
    )

    table.add_column(
        "Version / Banner",
        style="white",
    )

    for index, port in enumerate(
        ports,
        start=1,
    ):

        service = services.get(
            port,
            "unknown",
        )

        style = _service_style(
            service,
        )

        version = versions.get(
            port,
        ) or "-"

        table.add_row(
            str(index),
            f"[{style}]{port}/tcp[/{style}]",
            f"[{style}]{service}[/{style}]",
            version,
        )

    console.print(table)

def findings(
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
        "Severity",
        justify="center",
        width=10,
    )

    table.add_column(
        "Finding",
        style="white",
    )

    for index, row in enumerate(
        rows,
        start=1,
    ):

        severity = _FINDING_SEVERITY.get(
            row,
            "warning",
        )

        icon = _SEVERITY_ICON.get(
            severity,
            "⚠",
        )

        table.add_row(
            str(index),
            f"[{severity}]{icon} {severity.upper()}[/{severity}]",
            row,
        )

    console.print(table)

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