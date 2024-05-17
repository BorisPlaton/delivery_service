from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import Path
from punq import Container

from domain.company.command.delete_company.command import DeleteCompanyCommand
from domain.company.controller.rest.v1.docs import DELETE_COMPANY_RESPONSES
from domain.company.controller.rest.v1.docs import GET_COMPANIES_RESPONSES
from domain.company.controller.rest.v1.docs import GET_COMPANY_RESPONSES
from domain.company.controller.rest.v1.docs import SAVE_COMPANY_RESPONSES
from domain.company.controller.rest.v1.types.input.save_company import SaveCompanyInput
from domain.company.controller.rest.v1.types.output.company import CompanyOutput
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
    repository: ICompanyRepository = registry.resolve(ICompanyRepository)
    return await repository.get_all()


@router.get(
    '/{id:int}/',
    responses=GET_COMPANY_RESPONSES,
)
async def get_company(
    company_id: Annotated[int, Path(alias='id', description="Company's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> CompanyOutput | None:
    """
    Returns a specific company by its `ID`.
    """
    repository: ICompanyRepository = registry.resolve(ICompanyRepository)
    return await repository.get(id_=company_id)


@router.put(
    '/',
    responses=SAVE_COMPANY_RESPONSES,
)
async def save_company(
    company_data: Annotated[SaveCompanyInput, Body(description="Company's data to save.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> int:
    """
    Creates company if it doesn't exist or updates the existing one.
    """
    command_bus: ICommandBus = registry.resolve(ICommandBus)
    return await command_bus.handle(
        message=company_data.to_command(),
    )


@router.delete(
    '/{id:int}/',
    responses=DELETE_COMPANY_RESPONSES,
)
async def delete_company(
    company_id: Annotated[int, Path(alias='id', description="Company's `ID`.")],
    registry: Annotated[Container, Depends(get_registry)],
) -> None:
    """
    Deletes the company by its `ID`.
    """
    command_bus: ICommandBus = registry.resolve(ICommandBus)
    await command_bus.handle(
        message=DeleteCompanyCommand(
            company_id=company_id,
        )
    )
