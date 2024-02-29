from typing import Sequence
from schemas.countries import CountrySchema
from utils.unitofwork import IUnitOfWork


class CountriesService:
    async def get_countries(self, uow: IUnitOfWork) -> Sequence[CountrySchema]:
        async with uow:
            countries = await uow.countries.find_all()
            return countries 

    async def get_countries_by(self, uow: IUnitOfWork, data: dict[str, str]) -> Sequence[CountrySchema]:
        async with uow:
            countries = await uow.countries.find_where(data=data)
            return countries

    async def get_country_by(self, uow: IUnitOfWork, data: dict[str, str]) -> CountrySchema:
        async with uow:
            country = await uow.countries.get_where(data=data)
            return country
