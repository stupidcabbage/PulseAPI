from typing import Annotated
from fastapi import APIRouter, Body
from api.dependencies import UOWDep

from schemas.users import UserRegisterSchema, ProfileSchemaOut 
from services.users import UsersService
from api.exceptions import BaseRouterException
from schemas.tokens import SignInSchema, TokenSchema
from api.auth.handler import signJWT


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", status_code=201,
             response_model_exclude_none=True)
async def register(uow: UOWDep,
                   user: Annotated[UserRegisterSchema, Body()]) -> ProfileSchemaOut:
    db_user = await UsersService().add_user(uow, user)
    return ProfileSchemaOut(profile=db_user)


@router.post("/sign-in")
async def sign_in(uow: UOWDep,
                  sign_data: Annotated[SignInSchema, Body()]) -> TokenSchema:
    is_authenticated = await UsersService().authenticate_user(uow, sign_data)
    if is_authenticated:
        return await signJWT(is_authenticated)
    raise BaseRouterException(reason="Invalid username or password",
                              status_code=401)