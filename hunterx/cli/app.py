from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console

from hunterx.cli.banner import print_banner
from hunterx.core.application import HunterX
from hunterx.core.output.manager import OutputManager

app = typer.Typer(
    help="Modern Reconnaissance Framework",
    no_args_is_help=True,
    add_completion=False,
)

console = Console()


@app.callback()
def main() -> None:
    """
    HunterX CLI
    """
    pass


@app.command()
def version() -> None:
    """
    Show HunterX version.
    """

    print_banner()

    console.print()

    console.print(
        "[bold cyan]Version[/bold cyan] : 0.1.0"
    )


@app.command()
def modules() -> None:
    """
    List available modules.
    """

    print_banner()

    console.print()

    console.print(
        "[bold green]Available Modules[/bold green]\n"
    )

    modules = [
        "dns",
        "http",
        "subdomain",
        "technology",
        "security-headers",
        "port-scanner (coming soon)",
        "tls-scanner (coming soon)",
        "report-generator",
    ]

    for module in modules:
        console.print(f" • {module}")


@app.command()
def scan(
    target: str = typer.Argument(
        ...,
        help="Target domain or IP address",
    ),
    plugins: str | None = typer.Option(
        None,
        "--plugins",
        "-p",
        help="Comma separated plugins. Example: dns,http,subdomain",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save report (.json/.md)",
    ),
    timeout: int | None = typer.Option(
        None,
        "--timeout",
        "-t",
        help="HTTP/DNS timeout",
    ),
    threads: int | None = typer.Option(
        None,
        "--threads",
        help="Worker threads",
    ),
    headers: list[str] = typer.Option(
        None,
        "--header",
        "-H",
        help="Custom HTTP header",
    ),
) -> None:
    """
    Scan target.
    """

    print_banner()

    hunter = HunterX()

    if timeout is not None:
        hunter.config.http.timeout = timeout
        hunter.config.dns.timeout = timeout

    if threads is not None:
        hunter.config.scanner.workers = threads

    selected_plugins: list[str] | None = None

    if plugins:

        selected_plugins = [
            plugin.strip().lower()
            for plugin in plugins.split(",")
            if plugin.strip()
        ]

    custom_headers: dict[str, str] = {}

    if headers:

        for header in headers:

            if ":" not in header:

                continue

            key, value = header.split(
                ":",
                1,
            )

            custom_headers[
                key.strip()
            ] = value.strip()

    hunter.run(
        target=target,
        plugins=selected_plugins,
        custom_headers=custom_headers,
    )

    if output is None:
        return

    manager = OutputManager()

    extension = Path(output).suffix.lower()

    formats = {
        ".json": "json",
        ".md": "md",
    }

    fmt = formats.get(extension)

    if fmt is None:

        console.print()

        console.print(
            "[bold red]Unsupported output format.[/bold red]"
        )

        raise typer.Exit(code=1)

    manager.write(
        fmt,
        hunter.result,
        output,
    )

    console.print()

    console.print(
        f"[bold green]Report saved to[/bold green] {output}"
    )