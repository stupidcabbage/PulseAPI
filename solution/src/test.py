import asyncio

from sqlalchemy import or_, select
from db.models.countries import Country

from utils.unitofwork import UnitOfWork
from services.countries import CountriesService
from repositories import countries

from db.db import async_session_maker


async def test():
    session = async_session_maker()
    data = {"region": "asd"}
    async with session:
        regions = ["Africa", "Europe"]
        values = [Country.region == regions[0], Country.region == regions[1]]
        stmt = select(Country).where(or_(*values))
        res = await session.scalars(stmt)
        return res.all()

print(asyncio.run(test()))
