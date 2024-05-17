from abc import ABC
from abc import abstractmethod


class IAsyncCRUDRepository[T, U](ABC):

    @abstractmethod
    async def get(self, id_: T) -> U:
        raise NotImplementedError()

    @abstractmethod
    async def get_by_ids(self, ids: list[T]) -> U:
        raise NotImplementedError()

    @abstractmethod
    async def get_all(self) -> list[U]:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, entity: U) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, entity: U) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def update_many(self, entities: list[U]) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, entity: U) -> None:
        raise NotImplementedError()
