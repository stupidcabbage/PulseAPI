import asyncio

from sqlalchemy import select
from db.models.countries import Country

from utils.unitofwork import UnitOfWork
from services.countries import CountriesService
from repositories import countries

from db.db import async_session_maker


async def test():
    session = async_session_maker()
    data = {"region": "asd"}
    async with session:
        stmt = select(Country)
        for k, v in data.items():
            stmt = stmt.where(getattr(Country, k) == v)
        res = await session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

print(asyncio.run(test()))
