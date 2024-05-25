from pydantic import BaseModel
from pydantic import Field

from domain.company.command.save_company.command import SaveCompanyCommand


class SaveCompanyInput(BaseModel):
    company_id: int | None = Field(
        serialization_alias='id',
        validation_alias='id',
        examples=[1],
        ge=1,
    )
    title: str = Field(
        examples=["NovaPoshta"],
        max_length=256,
    )
    description: str | None = Field(
        examples=[
            '«Nova Poshta» is a Ukrainian company that provides express '
            'delivery services for documents, cargo and parcels.'
        ],
        max_length=256,
    )

    def to_command(self) -> SaveCompanyCommand:
        return SaveCompanyCommand(
            company_id=self.company_id,
            title=self.title,
            description=self.description,
        )
