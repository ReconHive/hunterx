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
def main():
    """
    HunterX CLI
    """
    pass


@app.command()
def version():
    """
    Show HunterX version.
    """

    print_banner()

    console.print()

    console.print(
        "[bold cyan]Version[/bold cyan] : 0.1.0"
    )


@app.command()
def modules():
    """
    List available modules.
    """

    print_banner()

    console.print()

    console.print(
        "[bold green]Available Modules[/bold green]\n"
    )

    modules = [
        "DNS",
        "HTTP",
        "Subdomain Enumeration",
        "Technology Detection",
        "Security Headers",
        "Port Scanner (Coming Soon)",
        "TLS Scanner (Coming Soon)",
        "Report Generator",
    ]

    for module in modules:

        console.print(f" • {module}")


@app.command()
def scan(
    target: str = typer.Argument(
        ...,
        help="Target domain",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Save report to file (.json/.md)",
    ),
):
    """
    Scan target.
    """

    print_banner()

    hunter = HunterX()

    hunter.run(target)

    if output:

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