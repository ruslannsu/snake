from typing import Callable

class EventBus:
    def __init__(self) -> None:
        self._handlers: dict[str, Callable] = {}
    
    def subscribe(self, event_name: str, handler: Callable) -> None:
        self._handlers[event_name] = handler

    def notify(self, *args, event_name: str):
        func = self._handlers[event_name]
        func(*args)

event_bus = EventBus()