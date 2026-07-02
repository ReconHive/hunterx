"""
HunterX Logger

Centralized logging system for HunterX.
"""

from __future__ import annotations

from rich.console import Console


class Logger:
    """
    HunterX logger wrapper around Rich Console.
    """

    def __init__(self) -> None:
        self.console = Console()

    def info(self, message: str) -> None:
        self.console.print(f"[cyan][INFO][/cyan] {message}")

    def success(self, message: str) -> None:
        self.console.print(f"[green][SUCCESS][/green] {message}")

    def warning(self, message: str) -> None:
        self.console.print(f"[yellow][WARNING][/yellow] {message}")

    def error(self, message: str) -> None:
        self.console.print(f"[bold red][ERROR][/bold red] {message}")

    def debug(self, message: str) -> None:
        self.console.print(f"[magenta][DEBUG][/magenta] {message}")


logger = Logger()