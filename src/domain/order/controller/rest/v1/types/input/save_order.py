from __future__ import annotations

from pydantic import BaseModel
from pydantic import Field

from domain.order.command.save_order.command import CustomerInfoCommandInput
from domain.order.command.save_order.command import OrderItemCommandInput
from domain.order.command.save_order.command import SaveOrderCommand
from domain.order.command.save_order.command import ShippingInfoCommandInput
from domain.order.model.order import OrderStatus


class SaveOrderInput(BaseModel):
    order_id: int | None = Field(serialization_alias='id', validation_alias='id')
    description: str | None
    status: OrderStatus
    items: list[OrderItemInput]
    shipping: ShippingInfoInput
    customer: CustomerInfoInput

    def to_command(self) -> SaveOrderCommand:
        return SaveOrderCommand(
            order_id=self.order_id,
            description=self.description,
            status=self.status,
            items=[item.to_command_input() for item in self.items],
            shipping=self.shipping.to_command_input(),
            customer=self.customer.to_command_input(),
        )


class OrderItemInput(BaseModel):
    title: str
    price: str
    quantity: int

    def to_command_input(self) -> OrderItemCommandInput:
        return OrderItemCommandInput(
            title=self.title,
            price=self.price,
            quantity=self.quantity,
        )


class ShippingInfoInput(BaseModel):
    country: str
    city: str
    street: str
    post_code: str

    def to_command_input(self) -> ShippingInfoCommandInput:
        return ShippingInfoCommandInput(
            country=self.country,
            city=self.city,
            street=self.street,
            post_code=self.post_code,
        )


class CustomerInfoInput(BaseModel):
    first_name: str | None
    second_name: str | None
    phone_number: str
    email: str

    def to_command_input(self) -> CustomerInfoCommandInput:
        return CustomerInfoCommandInput(
            first_name=self.first_name,
            second_name=self.second_name,
            phone_number=self.phone_number,
            email=self.email,
        )
