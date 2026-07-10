"""
HunterX Logger

Centralized logging system for HunterX.
"""

from __future__ import annotations

from hunterx.cli.console import console


class Logger:
    """
    HunterX logger wrapper around Rich Console.
    """

    def __init__(self) -> None:
        self.console = console

    def info(self, message: str) -> None:
        self.console.print(
            f"[info]ℹ[/info] {message}"
        )

    def success(self, message: str) -> None:
        self.console.print(
            f"[success]✓[/success] {message}"
        )

    def warning(self, message: str) -> None:
        self.console.print(
            f"[warning]⚠[/warning] {message}"
        )

    def error(self, message: str) -> None:
        self.console.print(
            f"[error]✖[/error] {message}"
        )

    def debug(self, message: str) -> None:
        self.console.print(
            f"[plugin]●[/plugin] {message}"
        )

    def line(self) -> None:
        self.console.print(
            "────────────────────────────────────────────",
            style="dim",
        )

    def blank(self) -> None:
        self.console.print()


logger = Logger()