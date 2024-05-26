from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic import Field

from domain.order.model.order import OrderStatus
from shared.pydantic_.enum_.serializer import EnumNameSerializer


class CompanyOrderOutput(BaseModel):
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
    finished_to: datetime = Field(
        examples=[datetime.now()],
    )
    finished_at: datetime | None = Field(
        examples=[datetime.now()],
    )

