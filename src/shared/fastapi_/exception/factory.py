from fastapi import HTTPException
from fastapi import status

from shared.exception.base import BaseAppException
from shared.exception.not_found import NotFound


def exception_factory(exc: BaseAppException) -> HTTPException:
    if isinstance(exc, NotFound):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    raise ValueError(f"{type(exc)} can't be handled as HTTPException.")
