from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import status
from fastapi import Depends
from fastapi import Path
from fastapi import Response
from punq import Container

from domain.order.command.delete_order.command import DeleteOrderCommand
from domain.order.controller.rest.v1.docs.delete_order import DELETE_ORDER_RESPONSES
from domain.order.controller.rest.v1.docs.get_order import GET_ORDER_RESPONSES
from domain.order.controller.rest.v1.docs.get_orders import GET_ORDERS_RESPONSES
from domain.order.controller.rest.v1.docs.save_order import SAVE_ORDER_RESPONSES
from domain.order.controller.rest.v1.types.input.save_order import SaveOrderInput
from domain.order.controller.rest.v1.types.output.order import OrderOutput
from domain.order.repository.interface import IOrderRepository
from shared.fastapi_.dependency import get_registry
from shared.message_bus.command_bus.interface.bus import ICommandBus


router = APIRouter()


@router.get(
    '/',
    responses=GET_ORDERS_RESPONSES,
)
async def get_orders(
    registry: Annotated[Container, Depends(get_registry)],
) -> list[OrderOutput]:
    """
    Returns all existing orders.
    """
    return await registry.resolve(IOrderRepository).get_all()


@router.get(
    '/{id:int}/',
    responses=GET_ORDER_RESPONSES,
)
async def get_order(
    order_id: Annotated[int, Path(alias='id', description="Order's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
    response: Response,
) -> OrderOutput | None:
    """
    Returns a specific order by its `ID`.
    """
    if not (order := await registry.resolve(IOrderRepository).get(id_=order_id)):
        response.status_code = status.HTTP_204_NO_CONTENT
    return order


@router.put(
    '/',
    responses=SAVE_ORDER_RESPONSES,
)
async def save_order(
    order_data: Annotated[SaveOrderInput, Body(description="Order's data to save.")],
    registry: Annotated[Container, Depends(get_registry)],
    response: Response,
) -> int:
    """
    Creates an order if it doesn't exist or updates the existing one.
    """
    order_id = await registry.resolve(ICommandBus).handle(
        message=order_data.to_command(),
    )
    if order_id != order_data.order_id:
        response.status_code = status.HTTP_201_CREATED
    return order_id


@router.delete(
    '/{id:int}/',
    responses=DELETE_ORDER_RESPONSES,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_order(
    order_id: Annotated[int, Path(alias='id', description="Order's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> None:
    """
    Deletes the order by its `ID`.
    """
    await registry.resolve(ICommandBus).handle(
        message=DeleteOrderCommand(
            order_id=order_id,
        )
    )
