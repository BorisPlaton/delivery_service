from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path
from punq import Container

from domain.order.command.delete_order.command import DeleteOrderCommand
from domain.order.controller.rest.v1.docs import DELETE_ORDER_RESPONSES
from domain.order.controller.rest.v1.docs import GET_ORDERS_RESPONSES
from domain.order.controller.rest.v1.docs import GET_ORDER_RESPONSES
from domain.order.controller.rest.v1.docs import SAVE_ORDER_RESPONSES
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
    repository: IOrderRepository = registry.resolve(IOrderRepository)
    return await repository.get_all()


@router.get(
    '/{id:int}/',
    responses=GET_ORDER_RESPONSES,
)
async def get_order(
    order_id: Annotated[int, Path(alias='id', description="Order's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> OrderOutput:
    """
    Returns a specific order by its `ID`.
    """
    repository: IOrderRepository = registry.resolve(IOrderRepository)
    return await repository.get(id_=order_id)


@router.put(
    '/',
    responses=SAVE_ORDER_RESPONSES,
)
async def save_order(
    order_data: Annotated[SaveOrderInput, Body(description="Order's data to save.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> int:
    """
    Creates order if it doesn't exist or updates the existing one.
    """
    command_bus: ICommandBus = registry.resolve(ICommandBus)
    return await command_bus.handle(
        message=order_data.to_command(),
    )


@router.delete(
    '/{id:int}/',
    responses=DELETE_ORDER_RESPONSES,
)
async def delete_order(
    order_id: Annotated[int, Path(alias='id', description="Order's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> None:
    """
    Deletes the order by its `ID`.
    """
    command_bus: ICommandBus = registry.resolve(ICommandBus)
    await command_bus.handle(
        message=DeleteOrderCommand(
            order_id=order_id,
        )
    )
