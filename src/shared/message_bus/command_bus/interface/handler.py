from abc import ABC
from abc import abstractmethod

from shared.message_bus.interface.handler import IMessageHandler
from shared.message_bus.command_bus.interface.command import ICommand


class ICommandHandler[T, U: ICommand](IMessageHandler[U, T], ABC):

    @abstractmethod
    async def __call__(self, command: U) -> T:
        raise NotImplementedError()
