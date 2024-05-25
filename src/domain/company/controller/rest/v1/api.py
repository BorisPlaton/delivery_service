from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path
from fastapi import Response
from fastapi import status
from punq import Container

from domain.company.command.delete_company.command import DeleteCompanyCommand
from domain.company.controller.rest.v1.docs.delete_company import DELETE_COMPANY_RESPONSES
from domain.company.controller.rest.v1.docs.get_companies import GET_COMPANIES_RESPONSES
from domain.company.controller.rest.v1.docs.get_company import GET_COMPANY_RESPONSES
from domain.company.controller.rest.v1.docs.get_company_orders import GET_COMPANY_ORDERS_RESPONSES
from domain.company.controller.rest.v1.docs.save_company import SAVE_COMPANY_RESPONSES
from domain.company.controller.rest.v1.types.input.save_company import SaveCompanyInput
from domain.company.controller.rest.v1.types.output.company import CompanyOutput
from domain.company.controller.rest.v1.types.output.order import CompanyOrderOutput
from domain.company.repository.interface import ICompanyRepository
from shared.fastapi_.dependency import get_registry
from shared.message_bus.command_bus.interface.bus import ICommandBus


router = APIRouter()


@router.get(
    '/',
    responses=GET_COMPANIES_RESPONSES,
)
async def get_companies(
    registry: Annotated[Container, Depends(get_registry)],
) -> list[CompanyOutput]:
    """
    Returns all existing companies.
    """
    return await registry.resolve(ICompanyRepository).get_all()


@router.get(
    '/{id:int}/',
    responses=GET_COMPANY_RESPONSES,
)
async def get_company(
    company_id: Annotated[int, Path(alias='id', description="Company's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
    response: Response,
) -> CompanyOutput | None:
    """
    Returns a specific company by its `ID`.
    """
    if not (company := await registry.resolve(ICompanyRepository).get(id_=company_id)):
        response.status_code = status.HTTP_204_NO_CONTENT
    return company


@router.get(
    '/{id:int}/orders/',
    responses=GET_COMPANY_ORDERS_RESPONSES,
)
async def get_company_orders(
    company_id: Annotated[int, Path(alias='id', description="Company's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
    response: Response,
) -> list[CompanyOrderOutput] | None:
    """
    Returns company's orders.
    """
    if not (company := await registry.resolve(ICompanyRepository).get(id_=company_id)):
        response.status_code = status.HTTP_204_NO_CONTENT
        return
    return company.orders


@router.put(
    '/',
    responses=SAVE_COMPANY_RESPONSES,
)
async def save_company(
    company_data: Annotated[SaveCompanyInput, Body(description="Company's data to save.")],
    registry: Annotated[Container, Depends(get_registry)],
    response: Response,
) -> int:
    """
    Creates company if it doesn't exist or updates the existing one.
    """
    company_id = await registry.resolve(ICommandBus).handle(
        message=company_data.to_command(),
    )
    if company_id != company_data.company_id:
        response.status_code = status.HTTP_201_CREATED
    return company_id


@router.delete(
    '/{id:int}/',
    responses=DELETE_COMPANY_RESPONSES,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_company(
    company_id: Annotated[int, Path(alias='id', description="Company's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> None:
    """
    Deletes the company by its `ID`.
    """
    await registry.resolve(ICommandBus).handle(
        message=DeleteCompanyCommand(
            company_id=company_id,
        )
    )
