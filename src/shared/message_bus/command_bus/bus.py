from typing import Any
from typing import Awaitable
from typing import Callable

from shared.message_bus.command_bus.interface.bus import ICommandBus
from shared.message_bus.command_bus.interface.command import ICommand
from shared.message_bus.command_bus.exception import NoCommandHandlersFound
from shared.message_bus.command_bus.interface.handler import ICommandHandler
from shared.message_bus.command_bus.interface.middleware import ICommandBusMiddleware


class CommandBus[T: ICommand, V: ICommandHandler](ICommandBus):

    def __init__(
        self,
        middlewares: list[ICommandBusMiddleware],
    ) -> None:
        self._message_handler_map: dict[type[T], V] = {}
        self._middlewares = middlewares
        self._middleware_chain = self._build_middlewares()

    def register(
        self,
        message: type[T],
        handler: V,
    ) -> None:
        self._message_handler_map[message] = handler

    async def handle(
        self,
        message: T,
    ) -> Any:
        return await self._middleware_chain(message)

    def _build_middlewares(self) -> Callable[[ICommand], Awaitable[Any]]:
        async def command_executor(command: ICommand) -> None:
            if not (handler := self._message_handler_map.get(command.__class__)):
                raise NoCommandHandlersFound()

            return await handler(
                command=command,
            )

        def wrapped_middleware(
            mdl: ICommandBusMiddleware,
            next_handler: Callable[[ICommand], Awaitable[Any]],
        ) -> Callable[[ICommand], Awaitable[Any]]:
            async def wrapped_handler(command: ICommand) -> Any:
                return await mdl.handle(
                    command=command,
                    next_=next_handler,
                )

            return wrapped_handler

        for middleware in self._middlewares[::-1]:
            command_executor = wrapped_middleware(
                mdl=middleware,
                next_handler=command_executor,
            )

        return command_executor
