from abc import ABC

from domain.order.model.order import Order
from shared.database.sqlalchemy.repository import AsyncSQLAlchemyRepository


class IOrderRepository[T: int, U: Order](
    AsyncSQLAlchemyRepository[T, U],
    ABC
):
    pass
