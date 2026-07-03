from __future__ import annotations

from dataclasses import dataclass

from hunterx.core.events.base import Event


@dataclass(slots=True)
class ScanStarted(Event):

    target: str


@dataclass(slots=True)
class ScanFinished(Event):

    target: str


@dataclass(slots=True)
class PluginStarted(Event):

    plugin: str


@dataclass(slots=True)
class PluginFinished(Event):

    plugin: str