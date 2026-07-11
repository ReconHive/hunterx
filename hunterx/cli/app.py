from __future__ import annotations

from pathlib import Path

import typer

from hunterx.cli.banner import print_banner
from hunterx.cli.console import console
from hunterx.core.application import HunterX
from hunterx.core.output.manager import OutputManager
from hunterx.modules.ports.common import parse_ports

app = typer.Typer(
    help="[bold cyan]HunterX[/bold cyan] — Modern Reconnaissance Framework "
    "for bug bounty and security research.",
    no_args_is_help=True,
    add_completion=False,
    rich_markup_mode="rich",
    epilog=(
        "Run [bold]hunterx COMMAND --help[/bold] for detailed "
        "help on a specific command.\n\n"
        "Examples:\n"
        "  hunterx scan example.com\n"
        "  hunterx scan example.com -p subdomain,crawler\n"
        "  hunterx modules"
    ),
)


@app.callback()
def main() -> None:
    """
    HunterX CLI
    """
    pass


@app.command()
def help_command(
    ctx: typer.Context,
) -> None:
    """
    Show this help message.
    """

    console.print(
        ctx.parent.get_help(),
    )


app.info.name = "hunterx"

app.registered_commands[-1].name = "help"


@app.command()
def version() -> None:
    """
    Show HunterX version.
    """

    print_banner()

    console.print()

    console.print(
        "[header]Version[/header] : [success]0.2.4[/success]"
    )

    console.print()


@app.command()
def author() -> None:
    """
    Show HunterX Author.
    """

    print_banner()

    console.print()

    console.print(
        "[header]Author[/header] : The author of HunterX is Alireza."
    )

    console.print()


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
        "portscanner",
        "takeover",
        "report-generator",
    ]

    for module in modules:
        console.print(
            f" • [plugin]{module}[/plugin]"
        )

    console.print()


@app.command(
    epilog=(
        "[bold]Examples:[/bold]\n\n"
        "  Basic scan (all modules):\n"
        "    hunterx scan example.com\n\n"
        "  Run specific modules only:\n"
        "    hunterx scan example.com -p subdomain,crawler\n\n"
        "  Auto-dependency resolution "
        "(takeover pulls in subdomain automatically):\n"
        "    hunterx scan example.com -p takeover\n\n"
        "  Directory brute-force with a custom wordlist:\n"
        "    hunterx scan example.com -p directory "
        "--wordlist wordlists/big.txt -x php,bak,old\n\n"
        "  Port scan — single port, list, range, or all 65535:\n"
        "    hunterx scan example.com -p portscanner -P 22\n"
        "    hunterx scan example.com -p portscanner -P 22,25,1000\n"
        "    hunterx scan example.com -p portscanner -P 1-1000\n"
        "    hunterx scan example.com -p portscanner -P -\n\n"
        "  Custom headers and HTTP method:\n"
        "    hunterx scan example.com -H \"Authorization: "
        "Bearer xyz\" -X POST\n\n"
        "  Fresh scan, ignoring any cached workspace data:\n"
        "    hunterx scan example.com --fresh\n\n"
        "  Save a report:\n"
        "    hunterx scan example.com -o report.json\n"
        "    hunterx scan example.com -o report.md"
    ),
)
def scan(
    target: str = typer.Argument(
        ...,
        help="Target domain or IP address. Example: example.com",
    ),
    plugins: str | None = typer.Option(
        None,
        "--plugins",
        "-p",
        help="Comma separated plugins to run. If omitted, all "
        "registered plugins run. Dependent plugins (e.g. "
        "javascript needs crawler, takeover needs subdomain) "
        "are auto-resolved from workspace or run automatically. "
        "Example: dns,http,subdomain",
        rich_help_panel="Target & Plugins",
    ),
    fresh: bool = typer.Option(
        False,
        "--fresh",
        help="Wipe this target's saved workspace before scanning, "
        "ignoring any cached results from previous runs.",
        rich_help_panel="Target & Plugins",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save the full scan report. Format is inferred from "
        "the extension: .json or .md",
        rich_help_panel="Target & Plugins",
    ),
    method: str = typer.Option(
        "GET",
        "--method",
        "-X",
        help="HTTP request method used by modules that make "
        "requests (http, directory, crawler, etc.)",
        rich_help_panel="Network",
    ),
    headers: list[str] | None = typer.Option(
        None,
        "--header",
        "-H",
        help="Custom HTTP header, repeatable. "
        'Format: "Key: Value". Example: -H "Authorization: Bearer xyz"',
        rich_help_panel="Network",
    ),
    timeout: int | None = typer.Option(
        None,
        "--timeout",
        "-t",
        help="HTTP and DNS request timeout, in seconds.",
        rich_help_panel="Network",
    ),
    threads: int | None = typer.Option(
        None,
        "--threads",
        help="Global worker thread count, used by any module "
        "without its own override (subdomain bruteforce, "
        "crawler, javascript, ports, takeover).",
        rich_help_panel="Network",
    ),
    depth: int = typer.Option(
        2,
        "--depth",
        help="Maximum crawl depth for the crawler module.",
        rich_help_panel="Module: crawler",
    ),
    wordlist: str | None = typer.Option(
        None,
        "--wordlist",
        help="Custom wordlist file for the directory module. "
        "Falls back to the built-in default list if omitted.",
        rich_help_panel="Module: directory",
    ),
    extensions: str | None = typer.Option(
        None,
        "--extensions",
        "-x",
        help="File extensions to append to directory wordlist "
        "entries. Example: php,txt,bak",
        rich_help_panel="Module: directory",
    ),
    dir_threads: int | None = typer.Option(
        None,
        "--dir-threads",
        help="Override worker thread count for the directory "
        "module specifically (independent of --threads).",
        rich_help_panel="Module: directory",
    ),
    ports: str | None = typer.Option(
        None,
        "--ports",
        "-P",
        help="Ports for the portscanner module. Accepts a single "
        "port (22), a list (22,25,1000), a range (1-1000), or "
        "- / all for the full 1-65535 range (prompts for "
        "confirmation above 5000 ports).",
        rich_help_panel="Module: portscanner",
    ),
) -> None:
    """
    Run a scan against a target.

    Modules run in the order given by --plugins, with automatic
    dependency injection where needed (e.g. requesting takeover
    alone will also run subdomain first if no workspace data
    exists yet).
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
    # Ports
    #

    if ports:

        try:

            parsed_ports = parse_ports(
                ports,
            )

        except ValueError:

            console.print()

            console.print(
                "[error]Invalid port specification. "
                "Example: 22 or 22,25,1000 or 1-1000 or -[/error]"
            )

            raise typer.Exit(code=1)

        if not parsed_ports:

            console.print()

            console.print(
                "[error]No valid ports parsed from input.[/error]"
            )

            raise typer.Exit(code=1)

        if len(parsed_ports) > 5000:

            console.print()

            console.print(
                f"[warning]This will scan {len(parsed_ports)} ports "
                f"against {target}. This may take a long time and "
                "could trigger rate limiting or IDS/IPS alerts.[/warning]"
            )

            confirmed = typer.confirm(
                "Continue?",
            )

            if not confirmed:

                console.print(
                    "[error]Aborted.[/error]"
                )

                raise typer.Exit(code=0)

        hunter.config.ports.ports = parsed_ports

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