from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel
from pydantic import Field

from domain.order.command.save_order.command import CustomerInfoCommandInput
from domain.order.command.save_order.command import OrderItemCommandInput
from domain.order.command.save_order.command import SaveOrderCommand
from domain.order.command.save_order.command import ShippingInfoCommandInput
from domain.order.model.order import OrderStatus
from shared.pydantic_.enum_.validator import enum_name_validator


class SaveOrderInput(BaseModel):
    order_id: int | None = Field(
        serialization_alias='id',
        validation_alias='id',
        examples=[1],
        ge=1,
    )
    description: str | None = Field(
        examples=["This is an order with the books for my friend."],
        max_length=512,
    )
    status: Annotated[OrderStatus, enum_name_validator(OrderStatus)] = Field(
        examples=[OrderStatus.NEW.name],

    )
    company_id: int = Field(
        examples=[1],
        ge=1,
    )
    finished_to: datetime = Field(
        examples=[datetime.now()],
    )
    finished_at: datetime | None = Field(
        examples=[datetime.now()],
    )
    items: list[OrderItemInput]
    shipping: ShippingInfoInput
    customer: CustomerInfoInput

    def to_command(self) -> SaveOrderCommand:
        return SaveOrderCommand(
            order_id=self.order_id,
            description=self.description,
            status=self.status,
            finished_to=self.finished_to,
            finished_at=self.finished_at,
            company_id=self.company_id,
            items=[item.to_command_input() for item in self.items],
            shipping=self.shipping.to_command_input(),
            customer=self.customer.to_command_input(),
        )


class OrderItemInput(BaseModel):
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

    def to_command_input(self) -> OrderItemCommandInput:
        return OrderItemCommandInput(
            title=self.title,
            price=float(self.price),
            quantity=self.quantity,
            currency=self.currency,
        )


class ShippingInfoInput(BaseModel):
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

    def to_command_input(self) -> ShippingInfoCommandInput:
        return ShippingInfoCommandInput(
            country=self.country,
            city=self.city,
            street=self.street,
            post_code=self.post_code,
        )


class CustomerInfoInput(BaseModel):
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

    def to_command_input(self) -> CustomerInfoCommandInput:
        return CustomerInfoCommandInput(
            first_name=self.first_name,
            second_name=self.second_name,
            phone_number=self.phone_number,
            email=self.email,
        )
