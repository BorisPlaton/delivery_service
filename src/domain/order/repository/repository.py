from functools import cached_property

from domain.order.model.order import Order
from domain.order.repository.interface import IOrderRepository


class OrderRepository(IOrderRepository):

    @cached_property
    def entity_class(self) -> type[Order]:
        return Order
