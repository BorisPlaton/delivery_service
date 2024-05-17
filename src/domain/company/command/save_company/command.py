from dataclasses import dataclass

from shared.message_bus.command_bus.interface.command import ICommand


@dataclass(kw_only=True, slots=True)
class SaveCompanyCommand(ICommand):
    company_id: int | None
    title: str
    description: str | None
