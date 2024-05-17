from functools import cached_property

from domain.company.model.company import Company
from domain.company.repository.interface import ICompanyRepository


class CompanyRepository(ICompanyRepository):

    @cached_property
    def entity_class(self) -> type[Company]:
        return Company
