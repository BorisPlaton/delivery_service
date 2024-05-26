from functools import cached_property

from sqlalchemy import func

from domain.order.model.order import Order
from domain.order.repository.interface import IOrderRepository


class OrderRepository(IOrderRepository):

    async def get_overdue_orders(self) -> list[Order]:
        # TODO: Think how to implement filtering without accessing
        #  private attributes
        return await self.get_all_by_filter(
            Order._finished_to < func.now(),
        )

    @cached_property
    def entity_class(self) -> type[Order]:
        return Order
