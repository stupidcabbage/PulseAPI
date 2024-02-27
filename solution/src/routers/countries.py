from typing import Annotated, List

from fastapi import APIRouter, Path

from schemas.countries import Countries, Country

router = APIRouter(prefix="/countries",
                   tags=["countries"])


@router.get("", summary="Получить список стран")
async def get_countries(region: Countries = Countries.all_) -> List[Country]:
    """
    Получение списка стран с возможной фильтрацией.\n
    Используется на странице регистрации для предоставления
    возможности выбора страны, к которой относится пользователь.\n
    Если никакие из фильтров не переданы, необходимо вернуть все страны.
    """
    # Здесь должна быть бизнес логика.
    return [Country(name="Hello World",
                    alpha2="as", alpha3="asd", region="Europe")]


@router.get("/{alpha2}", summary="Получить страну по alpha2 коду")
async def get_country_by_alpha2(
        alpha2: Annotated[str,
                          Path(max_length=2, min_length=2, example="RU")]
) -> Country:
    """
    Получение одной страны по её уникальному двухбуквенному коду.\n
    Используется для получения информации по определенной стране
    """
    # Бизнес логика.
    return Country(name="Hello World",
                    alpha2="as", alpha3="asd", region="Europe")
