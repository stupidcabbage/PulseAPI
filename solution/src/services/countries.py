from typing import Sequence
from src.schemas.countries import CountrySchema
from src.utils.unitofwork import IUnitOfWork


class CountriesService:
    async def get_countries(
            self, uow: IUnitOfWork) -> Sequence[CountrySchema]:
        async with uow:
            countries = await uow.countries.find_all()
            return countries

    async def get_countries_by(
            self, uow: IUnitOfWork,
            data: dict[str, str | list | tuple],
            order_by: str = "alpha2") -> Sequence[CountrySchema]:
        async with uow:
            countries = await uow.countries.find_where(data=data,
                                                       order_by=order_by,
                                                       order_desc=True)
            return countries

    async def get_country_by(
            self, uow: IUnitOfWork, data: dict[str, str]) -> CountrySchema:
        async with uow:
            country = await uow.countries.get_where(data=data)
            return country
