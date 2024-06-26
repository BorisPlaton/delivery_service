from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Awaitable
from typing import Callable

from shared.message_bus.command_bus.interface.command import ICommand


class ICommandBusMiddleware[T](ABC):

    @abstractmethod
    async def handle(
        self,
        command: ICommand,
        next_: Callable[[ICommand], Awaitable[Any]],
    ) -> T:
        raise NotImplementedError()
