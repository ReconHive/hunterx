import typer
from rich.console import Console
from hunterx.core.application import HunterX
from hunterx.core.logger import logger

from hunterx.cli.banner import print_banner

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


@app.command()
def modules():
    """
    List available modules.
    """

    print_banner()

    console.print()

    console.print("[bold green]Available Modules[/bold green]\n")

    console.print(" • DNS")
    console.print(" • HTTP")
    console.print(" • Port Scanner")
    console.print(" • Subdomain Enumeration")
    console.print(" • Screenshot")
    console.print(" • Report")

@app.command()
def scan(target: str):

    hunter = HunterX()

    hunter.run(target)