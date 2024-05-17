from domain.company.command.delete_company.command import DeleteCompanyCommand
from domain.company.repository.repository import ICompanyRepository
from shared.message_bus.command_bus.interface.handler import ICommandHandler


class DeleteCompanyCommandHandler(ICommandHandler[None, DeleteCompanyCommand]):

    def __init__(
        self,
        company_repository: ICompanyRepository,
    ):
        self._company_repository = company_repository

    async def __call__(
        self,
        command: DeleteCompanyCommand,
    ) -> None:
        company = await self._company_repository.get(id_=command.company_id)
        await self._company_repository.delete(company)
