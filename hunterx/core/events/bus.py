from __future__ import annotations

from collections import defaultdict
from typing import Callable

from hunterx.core.events.base import Event


Listener = Callable[[Event], None]


class EventBus:

    def __init__(self) -> None:

        self._listeners = defaultdict(list)

    def subscribe(
        self,
        event_type: type[Event],
        listener: Listener,
    ) -> None:

        self._listeners[event_type].append(
            listener
        )

    def publish(
        self,
        event: Event,
    ) -> None:

        for listener in self._listeners[
            type(event)
        ]:

            listener(event)