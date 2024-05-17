from domain.order.command.delete_order.command import DeleteOrderCommand
from domain.order.repository.interface import IOrderRepository
from shared.message_bus.command_bus.interface.handler import ICommandHandler


class DeleteOrderCommandHandler(ICommandHandler[None, DeleteOrderCommand]):

    def __init__(
        self,
        order_repository: IOrderRepository,
    ):
        self._order_repository = order_repository

    async def __call__(
        self,
        command: DeleteOrderCommand,
    ) -> None:
        order = await self._order_repository.get(id_=command.order_id)
        await self._order_repository.delete(order)
