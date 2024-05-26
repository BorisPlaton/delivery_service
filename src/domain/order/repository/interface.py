from abc import ABC
from abc import abstractmethod

from domain.order.model.order import Order
from shared.database.sqlalchemy.repository import AsyncSQLAlchemyRepository


class IOrderRepository[T: int, U: Order](
    AsyncSQLAlchemyRepository[T, U],
    ABC
):

    @abstractmethod
    def get_overdue_orders(self) -> list[U]:
        raise NotImplementedError()
