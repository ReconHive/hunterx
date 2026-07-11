import shutil

from hunterx.cli.console import Console

console = Console()

FULL_BANNER_WIDTH = 84


def print_banner() -> None:

    width = shutil.get_terminal_size(
        fallback=(80, 24),
    ).columns

    if width >= FULL_BANNER_WIDTH:

        _print_full_banner()

    else:

        _print_compact_banner()


def _print_full_banner() -> None:

    console.print(
        r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║         ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ██╗  ██╗         ║
║         ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗╚██╗██╔╝         ║
║         ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝ ╚███╔╝          ║
║         ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗ ██╔██╗          ║
║         ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║██╔╝ ██╗         ║
║         ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝         ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  [bold white]HunterX[/bold white]   [bold green]v0.2.5[/bold green]                                                            ║
║                                                                              ║
║  [cyan]Modern Reconnaissance Framework[/cyan]                                             ║
║                                                                              ║
║  [bright_black]Fast • Modular • Extensible • Workspace Driven[/bright_black]                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    )


def _print_compact_banner() -> None:

    console.print(
        r"""
┌──────────────────────────────┐
│  [bold white]HunterX[/bold white]  [bold green]v0.2.5[/bold green]         │
│  [cyan]Recon Framework[/cyan]              │
│  [bright_black]Fast • Modular • Ext.[/bright_black]     │
└──────────────────────────────┘
"""
    )