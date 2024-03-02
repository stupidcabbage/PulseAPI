from abc import ABC, abstractmethod

from sqlalchemy import desc, func, insert, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from asyncpg.exceptions import UniqueViolationError

from repositories.excpetions import DBUniqueException
from repositories.excpetions import BaseDBException


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

    async def add_one(self, data: dict) -> model:
        try:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await self.session.execute(stmt)
            return (res.scalar_one()).to_read_model()
        except IntegrityError as error:
            raise DBUniqueException(details=error.args)

    async def edit_one(self, data: dict, **filter_by) -> model:
        try:
            stmt = update(self.model).values(**data).filter_by(
                    **filter_by).returning(self.model)
            res = await self.session.execute(stmt)
            return (res.scalar_one()).to_read_model()
        except IntegrityError as error:
            raise DBUniqueException(details=error.args)
    

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_where(self,
                         data: dict,
                         order_by: str | None = None,
                         order_desc: bool = False):
        stmt = select(self.model)
        for k, v in data.items():
            if isinstance(v, (tuple, list)):
                for i in v:
                    values = [getattr(self.model, k) == i for i in v]
                    stmt = stmt.where(or_(*values))
            else:
                stmt = stmt.where(getattr(self.model, k) == v)

        if order_by:
            stmt = await self._order_by(stmt, order_by, order_desc)

        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res
    
    async def get_where(self, data: dict):
        stmt = select(self.model)
        for k, v in data.items():
            stmt = stmt.where(getattr(self.model, k) == v)
        res = await self.session.scalar(stmt)
        if res:
            return res.to_read_model()
        else:
            return None

    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res

    async def _order_by(self, stmt, value: str, _desc: bool = False):
        if _desc:
            return stmt.order_by(desc(getattr(self.model, value)))
        return stmt.order_by(getattr(self.model, value))
