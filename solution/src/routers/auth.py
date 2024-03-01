from typing import Annotated
from fastapi import APIRouter, Body
from dependencies import UOWDep

from schemas.users import UserRegisterSchema, ProfileSchemaOut 
from services.users import UsersService
from routers.exceptions import BaseRouterException
from repositories.excpetions import CountryDoesNotExists, DBUniqueException


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=201)
async def register(uow: UOWDep,
                   user: Annotated[UserRegisterSchema, Body()]) -> ProfileSchemaOut:
    try:
        db_user = await UsersService().add_user(uow, user)
        return ProfileSchemaOut(profile=db_user)
    except DBUniqueException:
        raise BaseRouterException(
                reason="Нарушено требование на уникальность авторизационных" +
                        "данных пользователей.",
                status_code=409)
        
    except CountryDoesNotExists:
        raise BaseRouterException(
                reason="Страны с указанным кодом не существует",
                status_code=404)
