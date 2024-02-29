from typing import Sequence
from schemas.countries import CountrySchema
from utils.unitofwork import IUnitOfWork


class CountriesService:
    async def get_countries(self, uow: IUnitOfWork) -> Sequence[CountrySchema]:
        async with uow:
            countries = await uow.countries.find_all()
            return countries 

    async def get_countries_by_region(self, uow: IUnitOfWork, region: str) -> Sequence[CountrySchema]:
        async with uow:
            country = await uow.countries.find_where(data={"region": region})
            return country
