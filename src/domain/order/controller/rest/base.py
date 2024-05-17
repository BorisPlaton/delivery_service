from fastapi import APIRouter

from domain.order.controller.rest.v1.api import router as v1_router


order_router = APIRouter(
    prefix='/order',
    tags=['Order'],
)

order_router.include_router(
    router=v1_router,
    prefix='/v1',
)
