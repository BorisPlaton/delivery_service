from __future__ import annotations

from datetime import datetime
from typing import Self
from typing import TYPE_CHECKING
from enum import Enum
from enum import auto

from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from shared.database.sqlalchemy.base import Base
from shared.database.sqlalchemy.mixins import IdMixin


if TYPE_CHECKING:
    from domain.order.model.order_customer import OrderCustomer
    from domain.order.model.order_item import OrderItem
    from domain.order.model.order_shipping import OrderShipping


class OrderStatus(str, Enum):
    NEW = auto()
    PROCESSING = auto()
    DELIVERED = auto()
    FINISHED = auto()
    CANCELLED = auto()


class Order(IdMixin, Base):
    __tablename__ = 'order'

    _description: Mapped[str | None] = mapped_column(
        String(
            length=512,
        ),
        name='description',
        nullable=True,
    )
    _status: Mapped[OrderStatus] = mapped_column(
        SQLAlchemyEnum(OrderStatus),
        name='status',
        nullable=False,
    )
    _company_id: Mapped[int] = mapped_column(
        ForeignKey(
            column="company.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        name="company_id",
        index=True,
        nullable=False,
    )
    _finished_at: Mapped[datetime] = mapped_column(
        name="finished_at",
        nullable=True,
    )
    _finished_to: Mapped[datetime] = mapped_column(
        name="finished_to",
        nullable=False,
    )

    _items: Mapped[list[OrderItem]] = relationship(
        lazy="select",
        cascade='all, delete-orphan',
    )
    _shipping: Mapped[OrderShipping] = relationship(
        lazy="select",
        cascade='all, delete-orphan',
    )
    _customer: Mapped[OrderCustomer] = relationship(
        lazy="select",
        cascade='all, delete-orphan',
    )

    @classmethod
    def create(
        cls,
        description: str | None,
        status: OrderStatus,
        items: list[OrderItem] | None,
        shipping: OrderShipping | None,
        customer: OrderCustomer | None,
        company_id: int,
        finished_to: datetime,
        finished_at: datetime | None,
    ) -> Self:
        return cls(
            _description=description,
            _status=OrderStatus.FINISHED if finished_at else status,
            _company_id=company_id,
            _items=items,
            _shipping=shipping,
            _customer=customer,
            _finished_to=finished_to,
            _finished_at=finished_at,
        )

    @property
    def description(self) -> str | None:
        return self._description

    @description.setter
    def description(
        self,
        description: str | None,
    ) -> None:
        self: Self
        self._description = description

    @property
    def status(self) -> OrderStatus:
        return self._status

    @status.setter
    def status(
        self,
        status: OrderStatus,
    ) -> None:
        self: Self
        self._status = status

    @property
    def company_id(self) -> int:
        return self._company_id

    @company_id.setter
    def company_id(
        self,
        company_id: int,
    ) -> None:
        self: Self
        self._company_id = company_id

    @property
    def finished_to(self) -> datetime:
        return self._finished_to

    @finished_to.setter
    def finished_to(
        self,
        finished_to: datetime,
    ) -> None:
        self: Self
        self._finished_to = finished_to

    @property
    def finished_at(self) -> datetime | None:
        return self._finished_at

    @finished_at.setter
    def finished_at(
        self,
        finished_at: datetime,
    ) -> None:
        self: Self
        self._finished_to = finished_at
        if finished_at:
            self._status = OrderStatus.FINISHED

    @property
    def items(self) -> list[OrderItem]:
        return self._items

    @items.setter
    def items(
        self,
        order_items: list[OrderItem],
    ) -> None:
        self: Self
        self._items = order_items

    @property
    def shipping(self) -> OrderShipping:
        return self._shipping

    @shipping.setter
    def shipping(
        self,
        shipping: OrderShipping,
    ) -> None:
        self: Self
        self._shipping = shipping

    @property
    def customer(self) -> OrderCustomer:
        return self._customer

    @customer.setter
    def customer(
        self,
        customer: OrderCustomer,
    ) -> None:
        self: Self
        self._customer = customer
