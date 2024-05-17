from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field


class OrderOutput(BaseModel):
    order_id: int = Field(serialization_alias='id', validation_alias='id')
    status: str
    items: list[OrderItemOutput]
    description: str
    shipping_info: ShippingInfoOutput
    customer_info: CustomerInfoOutput


class OrderItemOutput(BaseModel):
    order_item_id: int
    title: str
    price: float
    quantity: int
    currency: str


class ShippingInfoOutput(BaseModel):
    country: str
    city: str
    street: str
    post_code: str


class CustomerInfoOutput(BaseModel):
    first_name: str | None
    second_name: str | None
    phone_number: str
    email: str
