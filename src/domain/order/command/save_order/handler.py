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
        order: Order = await self._order_repository.get(id_=command.order_id)

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
            company_id=command.company_id,
            customer=OrderCustomer.create(
                first_name=command.customer.first_name,
                second_name=command.customer.second_name,
                email=command.customer.email,
                phone_number=command.customer.phone_number,
                order_id=None,
            ),
            shipping=OrderShipping.create(
                country=command.shipping.country,
                city=command.shipping.city,
                post_code=command.shipping.post_code,
                street=command.shipping.street,
                order_id=None,
            ),
            items=[
                OrderItem.create(
                    price=item.price,
                    title=item.title,
                    quantity=item.quantity,
                    currency=item.currency,
                    order_id=None,
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
        order.company_id = command.company_id
        order.shipping = OrderShipping.create(
            country=command.shipping.country,
            city=command.shipping.city,
            post_code=command.shipping.post_code,
            order_id=order.id,
            street=command.shipping.street,
        )
        order.customer = OrderCustomer.create(
            first_name=command.customer.first_name,
            second_name=command.customer.second_name,
            email=command.customer.email,
            phone_number=command.customer.phone_number,
            order_id=order.id,
        )
        order.items = [
            OrderItem.create(
                price=item.price,
                title=item.title,
                quantity=item.quantity,
                currency=item.currency,
                order_id=order.id,
            ) for item in command.items
        ]
        await self._order_repository.update(order)
