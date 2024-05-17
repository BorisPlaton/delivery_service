from pydantic import BaseModel
from pydantic import Field


class CompanyOutput(BaseModel):
    company_id: int = Field(serialization_alias='id', validation_alias='id')
    title: str
    description: str | None
