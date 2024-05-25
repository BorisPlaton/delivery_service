from typing import Self

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from shared.database.sqlalchemy.base import Base
from shared.database.sqlalchemy.mixins import IdMixin


class OrderCustomer(IdMixin, Base):
    __tablename__ = 'order_customer'

    _first_name: Mapped[str | None] = mapped_column(
        String(
            length=32,
        ),
        name='first_name',
        nullable=True,
    )
    _second_name: Mapped[str | None] = mapped_column(
        String(
            length=32,
        ),
        name='second_name',
        nullable=True,
    )
    _phone_number: Mapped[str] = mapped_column(
        String(
            length=16,
        ),
        name='phone_number',
        nullable=False,
    )
    _email: Mapped[str] = mapped_column(
        String(
            length=128,
        ),
        name='email',
        nullable=False,
    )
    _order_id: Mapped[int] = mapped_column(
        ForeignKey(
            column="order.id",
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
        first_name: str | None,
        second_name: str | None,
        phone_number: str,
        email: str,
        order_id: int | None,
    ) -> Self:
        return cls(
            _first_name=first_name,
            _second_name=second_name,
            _phone_number=phone_number,
            _email=email,
            _order_id=order_id,
        )

    @property
    def first_name(self) -> str | None:
        return self._first_name

    @property
    def second_name(self) -> str | None:
        return self._second_name

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @property
    def email(self) -> str:
        return self._email
