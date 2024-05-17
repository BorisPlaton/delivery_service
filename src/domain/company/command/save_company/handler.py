from domain.company.command.save_company.command import SaveCompanyCommand
from domain.company.model.company import Company
from domain.company.repository.interface import ICompanyRepository
from shared.message_bus.command_bus.interface.handler import ICommandHandler


class SaveCompanyCommandHandler(ICommandHandler[int, SaveCompanyCommand]):

    def __init__(
        self,
        company_repository: ICompanyRepository,
    ):
        self._company_repository = company_repository

    async def __call__(
        self,
        command: SaveCompanyCommand,
    ) -> int:
        company = await self._company_repository.get(id_=command.company_id)

        if not company:
            company = await self._create_company(
                command=command,
            )
        else:
            await self._update_company(
                company=company,
                command=command,
            )

        return company.id

    async def _create_company(
        self,
        command: SaveCompanyCommand,
    ) -> Company:
        company = Company.create(
            description=command.description,
            title=command.title,
        )
        await self._company_repository.create(company)
        return company

    async def _update_company(
        self,
        company: Company,
        command: SaveCompanyCommand,
    ) -> None:
        company.description = command.description
        company.title = command.title
        await self._company_repository.update(company)
