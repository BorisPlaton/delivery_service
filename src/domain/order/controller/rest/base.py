from fastapi import APIRouter

from domain.order.controller.rest.v1.api import router as v1_router


tag = 'Order'
order_router = APIRouter(
    prefix='/order',
    tags=[tag],
)

order_router.include_router(
    router=v1_router,
    prefix='/v1',
)
