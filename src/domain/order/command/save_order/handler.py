from domain.order.command.save_order.command import SaveOrderCommand
from domain.order.model.order import Order
from domain.order.model.order_customer import OrderCustomer
from domain.order.model.order_item import OrderItem
from domain.order.model.order_shipping import OrderShipping
from domain.order.repository.interface import IOrderRepository
from shared.message_bus.command_bus.interface.handler import ICommandHandler


class SaveOrderCommandHandler(ICommandHandler[int, SaveOrderCommand]):

    def __init__(
        self,
        order_repository: IOrderRepository,
    ):
        self._order_repository = order_repository

    async def __call__(
        self,
        command: SaveOrderCommand,
    ) -> int:
        order = await self._order_repository.get(id_=command.order_id)

        if not order:
            order = await self._create_order(
                command=command,
            )
        else:
            await self._update_order(
                order=order,
                command=command,
            )

        return order.id

    async def _create_order(
        self,
        command: SaveOrderCommand,
    ) -> Order:
        order = Order.create(
            description=command.description,
            status=command.status,
            shipping=OrderShipping.create(
                country=command.shipping.country,
                city=command.shipping.city,
                post_code=command.shipping.post_code,
                order=None,
            ),
            customer=OrderCustomer.create(
                first_name=command.customer.first_name,
                second_name=command.customer.second_name,
                email=command.customer.email,
                phone_number=command.customer.phone_number,
                order=None,
            ),
            items=[
                OrderItem.create(
                    price=item.price,
                    title=item.title,
                    quantity=item.quantity,
                    currency=item.currency,
                    order=None,
                ) for item in command.items
            ],
        )
        await self._order_repository.create(order)
        return order

    async def _update_order(
        self,
        order: Order,
        command: SaveOrderCommand,
    ) -> None:
        order.description = command.description
        order.status = command.status
        order.shipping = command.shipping
        order.customer = command.customer
        order.items = command.items
        await self._order_repository.update(order)
