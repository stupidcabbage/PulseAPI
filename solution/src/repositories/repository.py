from abc import ABC, abstractmethod

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError

    @abstractmethod
    async def find_one():
        raise NotImplementedError

    @abstractmethod
    async def edit_one():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.scalar(stmt)
        return res

    async def find_all(self):
        ...

    async def find_one(self):
        ...

    async def edit_one(self):
        ...
