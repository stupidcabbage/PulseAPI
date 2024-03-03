import time
from typing import Literal

from fastapi import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.api.auth.handler import decodeJWT
from src.api.exceptions import BaseRouterException
from src.schemas.users import FullUserSchema, UserSchema
from src.services.users import UsersService
from src.utils.unitofwork import UnitOfWork


class JWTBearer(HTTPBearer):
    def __init__(self, uow: UnitOfWork , auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.uow = uow
        
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise BaseRouterException(status_code=401, reason="Некорректная схема авторизации.")
            verify_jwt_status = await self.verify_jwt(self.uow, credentials.credentials)
            if not verify_jwt_status:
                raise BaseRouterException(status_code=401, reason="Невалидный или устаревший токен.")
            return verify_jwt_status
        else:
            raise BaseRouterException(status_code=401, reason="Неправильный токен авторизации.")

    async def verify_jwt(self, uow: UnitOfWork, jwtoken: str) -> Literal[False] | FullUserSchema:
        try:
            payload = await decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            user = await UsersService().get_user(uow,
                                                 {"login": payload.get("login")})
            if (payload["expires"] and payload["expires"] >= time.time()
                and payload["created_at"] and payload["created_at"] > user.last_password_change.timestamp()):
                return user
        return False
