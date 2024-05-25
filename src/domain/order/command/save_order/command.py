from __future__ import annotations

from dataclasses import dataclass

from domain.order.model.order import OrderStatus
from shared.message_bus.command_bus.interface.command import ICommand


@dataclass(kw_only=True, slots=True)
class SaveOrderCommand(ICommand):
    order_id: int | None
    description: str | None
    status: OrderStatus
    company_id: int
    items: list[OrderItemCommandInput]
    shipping: ShippingInfoCommandInput
    customer: CustomerInfoCommandInput


@dataclass(kw_only=True, slots=True)
class OrderItemCommandInput:
    title: str
    price: float
    quantity: int
    currency: str


@dataclass(kw_only=True, slots=True)
class ShippingInfoCommandInput:
    country: str
    city: str
    street: str
    post_code: str


@dataclass(kw_only=True, slots=True)
class CustomerInfoCommandInput:
    first_name: str | None
    second_name: str | None
    phone_number: str
    email: str
