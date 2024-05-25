from fastapi import APIRouter

from domain.company.controller.rest.v1.api import router as v1_router


tag = 'Company'
company_router = APIRouter(
    prefix='/company',
    tags=[tag],
)

company_router.include_router(
    router=v1_router,
    prefix='/v1',
)
