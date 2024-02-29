from typing import Annotated, List

from fastapi import APIRouter, Path

from schemas.countries import Countries, CountrySchema
from services.countries import CountriesService
from dependencies import UOWDep

router = APIRouter(prefix="/countries",
                   tags=["countries"])


@router.get("", summary="Получить список стран")
async def get_countries(uow: UOWDep,
                        region: Countries = Countries.all_)-> List[CountrySchema]:
    """
    Получение списка стран с возможной фильтрацией.\n
    Используется на странице регистрации для предоставления
    возможности выбора страны, к которой относится пользователь.\n
    Если никакие из фильтров не переданы, необходимо вернуть все страны.
    """
    match region:
        case Countries.all_:
            countries = await CountriesService().get_countries(uow)
        case _:
            countries = await CountriesService().get_countries_by_region(uow, region.value)
    return countries


@router.get("/{alpha2}", summary="Получить страну по alpha2 коду")
async def get_country_by_alpha2(
        alpha2: Annotated[str,
                          Path(max_length=2, min_length=2, example="RU")]
) -> CountrySchema:
    """
    Получение одной страны по её уникальному двухбуквенному коду.\n
    Используется для получения информации по определенной стране
    """
    # Бизнес логика.
    return CountrySchema(name="Hello World",
                    alpha2="as", alpha3="asd", region="Europe")
