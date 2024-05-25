from typing import Self

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from shared.database.sqlalchemy.base import Base
from shared.database.sqlalchemy.mixins import IdMixin


class OrderShipping(IdMixin, Base):
    __tablename__ = 'order_shipping'

    _country: Mapped[str] = mapped_column(
        String(
            length=128,
        ),
        name='country',
        nullable=False,
    )
    _city: Mapped[str] = mapped_column(
        String(
            length=128,
        ),
        name='city',
        nullable=False,
    )
    _post_code: Mapped[str] = mapped_column(
        String(
            length=128,
        ),
        name='post_code',
        nullable=False,
    )
    _street: Mapped[str] = mapped_column(
        String(
            length=128,
        ),
        name='street',
        nullable=False,
    )
    _order_id: Mapped[int] = mapped_column(
        ForeignKey("order.id", ondelete="CASCADE", onupdate="CASCADE"),
        name="order_id",
        index=True,
        nullable=False,
    )

    @classmethod
    def create(
        cls,
        country: str,
        city: str,
        post_code: str,
        street: str,
        order_id: int | None,
    ) -> Self:
        return cls(
            _country=country,
            _city=city,
            _post_code=post_code,
            _street=street,
            _order_id=order_id,
        )

    @property
    def country(self) -> str:
        return self._country

    @property
    def city(self) -> str:
        return self._city

    @property
    def post_code(self) -> str:
        return self._post_code

    @property
    def street(self) -> str:
        return self._street
