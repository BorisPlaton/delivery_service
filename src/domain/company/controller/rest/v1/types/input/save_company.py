from pydantic import BaseModel
from pydantic import Field

from domain.company.command.save_company.command import SaveCompanyCommand


class SaveCompanyInput(BaseModel):
    company_id: int | None = Field(serialization_alias='id', validation_alias='id')
    title: str
    description: str | None

    def to_command(self) -> SaveCompanyCommand:
        return SaveCompanyCommand(
            company_id=self.company_id,
            title=self.title,
            description=self.description,
        )
