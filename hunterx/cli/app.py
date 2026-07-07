from __future__ import annotations

from pathlib import Path

import typer

from hunterx.cli.banner import print_banner
from hunterx.cli.console import console
from hunterx.core.application import HunterX
from hunterx.core.output.manager import OutputManager

app = typer.Typer(
    help="Modern Reconnaissance Framework",
    no_args_is_help=True,
    add_completion=False,
)


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
        "[header]Version[/header] : [success]0.1.0[/success]"
    )


@app.command()
def modules() -> None:
    """
    List available modules.
    """

    print_banner()

    console.print()

    console.print(
        "[header]Available Modules[/header]\n"
    )

    modules = [
        "dns",
        "http",
        "subdomain",
        "crawler",
        "directory",
        "javascript",
        "tls",
        "ports",
        "report-generator",
    ]

    for module in modules:
        console.print(
            f" • [plugin]{module}[/plugin]"
        )


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
        help="Comma separated plugins. Example: dns,http",
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
    headers: list[str] | None = typer.Option(
        None,
        "--header",
        "-H",
        help="Custom HTTP header",
    ),
    method: str = typer.Option(
        "GET",
        "--method",
        "-X",
        help="HTTP request method",
    ),
    depth: int = typer.Option(
        2,
        "--depth",
        help="Crawler depth",
    ),
    wordlist: str | None = typer.Option(
        None,
        "--wordlist",
        help="Custom directory wordlist",
    ),
    extensions: str | None = typer.Option(
        None,
        "--extensions",
        "-x",
        help="File extensions. Example: php,txt,bak",
    ),
    dir_threads: int | None = typer.Option(
        None,
        "--dir-threads",
        help="Override directory workers",
    ),
    fresh: bool = typer.Option(
        False,
        "--fresh",
        help="Start with a clean workspace.",
    ),
) -> None:
    """
    Scan target.
    """

    print_banner()

    hunter = HunterX()

    #
    # Extensions
    #

    if extensions:

        hunter.config.directory.extensions = [
            ext.strip().lstrip(".")
            for ext in extensions.split(",")
            if ext.strip()
        ]

    #
    # Timeout
    #

    if timeout is not None:

        hunter.config.http.timeout = timeout
        hunter.config.dns.timeout = timeout

    #
    # Global workers
    #

    if threads is not None:

        hunter.config.scanner.workers = threads

    #
    # Directory workers
    #

    if dir_threads is not None:

        hunter.config.directory.threads = dir_threads

    #
    # Crawler
    #

    hunter.config.crawler.depth = depth

    #
    # Plugins
    #

    selected_plugins: list[str] | None = None

    if plugins:

        selected_plugins = [
            plugin.strip().lower()
            for plugin in plugins.split(",")
            if plugin.strip()
        ]

    #
    # Headers
    #

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

    #
    # Run
    #

    hunter.run(
        target=target,
        plugins=selected_plugins,
        custom_headers=custom_headers,
        method=method,
        wordlist=wordlist,
        fresh=fresh,
    )

    #
    # Output
    #

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
            "[error]Unsupported output format.[/error]"
        )

        raise typer.Exit(code=1)

    manager.write(
        fmt,
        hunter.result,
        output,
    )

    console.print()

    console.print(
        f"[success]Report saved to[/success] {output}"
    )


if __name__ == "__main__":
    app()