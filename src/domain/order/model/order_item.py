from typing import Self

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from shared.database.sqlalchemy.base import Base
from shared.database.sqlalchemy.mixins import IdMixin


class OrderItem(IdMixin, Base):
    __tablename__ = 'order_item'

    _price: Mapped[float] = mapped_column(
        name='price',
        nullable=False,
    )
    _title: Mapped[str] = mapped_column(
        String(
            length=256,
        ),
        name='title',
        nullable=False,
    )
    _quantity: Mapped[int] = mapped_column(
        name='quantity',
        nullable=False,
    )
    _currency: Mapped[str] = mapped_column(
        name='currency',
        nullable=False,
    )
    _order_id: Mapped[int] = mapped_column(
        ForeignKey(
            "order.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        name="order_id",
        index=True,
        nullable=False,
    )

    @classmethod
    def create(
        cls,
        price: float,
        title: str,
        quantity: int,
        currency: str,
        order_id: int | None,
    ) -> Self:
        return cls(
            _price=price,
            _title=title,
            _quantity=quantity,
            _currency=currency,
            _order_id=order_id,
        )

    @property
    def price(self) -> float:
        return self._price

    @property
    def title(self) -> str:
        return self._title

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def currency(self) -> str:
        return self._currency
