from __future__ import annotations

from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel
from pydantic import Field

from domain.order.model.order import OrderStatus
from shared.pydantic_.enum_.serializer import EnumNameSerializer


class OrderOutput(BaseModel):
    order_id: int = Field(
        serialization_alias='id',
        validation_alias='id',
        examples=[1],
        ge=1,
    )
    description: str | None = Field(
        examples=["This is an order with the books for my friend."],
        max_length=512,
    )
    status: Annotated[OrderStatus, EnumNameSerializer] = Field(
        examples=[OrderStatus.NEW.name],
    )
    company_id: int = Field(
        examples=[1],
    )
    items: list[OrderItemOutput]
    shipping: OrderShippingOutput
    customer: OrderCustomerOutput


class OrderItemOutput(BaseModel):
    order_item_id: int = Field(
        serialization_alias='id',
        validation_alias='id',
        examples=[1],
        ge=1,
    )
    title: str = Field(
        examples=["Book"],
        max_length=256,
    )
    price: Decimal = Field(
        examples=[59.99],
        decimal_places=2,
    )
    quantity: int = Field(
        examples=[2],
        ge=1,
    )
    currency: str = Field(
        examples=["$"],
    )


class OrderShippingOutput(BaseModel):
    country: str = Field(
        examples=["Ukraine"],
    )
    city: str = Field(
        examples=["Dnipro"],
    )
    street: str = Field(
        examples=["Nezalejna"]
    )
    post_code: str = Field(
        examples=["49000"],
    )


class OrderCustomerOutput(BaseModel):
    first_name: str | None = Field(
        examples=["Diana"],
    )
    second_name: str | None = Field(
        examples=["Stezhka"]
    )
    phone_number: str = Field(
        examples=["+380661235454"],
        min_length=10,
        max_length=14,
    )
    email: str = Field(
        examples=["customer@gmail.com"],
    )
