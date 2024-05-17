from abc import ABC

from domain.company.model.company import Company
from shared.database.sqlalchemy.repository import AsyncSQLAlchemyRepository


class ICompanyRepository[T: int, U: Company](
    AsyncSQLAlchemyRepository[T, U],
    ABC,
):
    pass
