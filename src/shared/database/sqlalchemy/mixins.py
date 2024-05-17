from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class IdMixin:
    id: Mapped[int] = mapped_column(
        primary_key=True,
        name='id',
    )
