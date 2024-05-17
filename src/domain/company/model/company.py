from __future__ import annotations

from typing import Self

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from shared.database.sqlalchemy.base import Base
from shared.database.sqlalchemy.mixins import IdMixin


class Company(IdMixin, Base):
    __tablename__ = 'company'

    _title: Mapped[str] = mapped_column(
        String(
            length=256,
        ),
        name='status',
        nullable=False,
    )
    _description: Mapped[str | None] = mapped_column(
        String(
            length=256,
        ),
        name='description',
        nullable=True,
    )

    @classmethod
    def create(
        cls,
        title: str,
        description: str,
    ) -> Company:
        return Company(
            _title=title,
            _description=description,
        )

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self: Self
        self._title = value

    @property
    def description(self) -> str | None:
        return self._description

    @description.setter
    def description(self, value: str | None) -> None:
        self: Self
        self._description = value
