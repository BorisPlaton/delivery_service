from typing import Any
from typing import Awaitable
from typing import Callable

from shared.database.sqlalchemy.connection.interface import IAsyncSQLAlchemyConnection
from shared.message_bus.command_bus.interface.command import ICommand
from shared.message_bus.command_bus.interface.middleware import ICommandBusMiddleware


class TransactionMiddleware(ICommandBusMiddleware):

    def __init__(
        self,
        connection: IAsyncSQLAlchemyConnection,
    ):
        self._connection = connection

    async def handle(
        self,
        command: ICommand,
        next_: Callable[[ICommand], Awaitable[Any]],
    ) -> Any:
        async with self._connection.connect() as session:
            async with session.begin():
                return await next_(command)
