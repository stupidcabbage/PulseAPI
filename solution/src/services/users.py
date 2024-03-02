import datetime
from typing import Literal
import bcrypt
from repositories.users import UsersRepository

from schemas.users import FullUserSchema, UserEditSchema, UserRegisterSchema, UserSchema, UserUpdatePasswordSchema
from services.countries import CountriesService
from schemas.tokens import SignInSchema
from utils.unitofwork import IUnitOfWork
from repositories.excpetions import CountryDoesNotExists


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserRegisterSchema):
        if not await self._is_country_exists(uow, user.country_code):
            raise CountryDoesNotExists

        user.password = self._hash_password(user.password)
        user_dict = user.model_dump(by_alias=False)
        async with uow:
            user = await uow.users.add_one(data=user_dict)
            await uow.commit()
            return user

    async def get_user(self, uow: IUnitOfWork, data: dict[str, list | str]):
        async with uow:
            return await uow.users.get_where(data=data)

    async def edit_user(self, uow: IUnitOfWork,
                        login: str, data: dict[str, str]):
        if (data.get("country_code") and
            not await self._is_country_exists(uow, data.get("country_code"))):
            raise CountryDoesNotExists
        
        async with uow:
            return await uow.users.edit_one(login, data=data)

    async def _is_country_exists(self, uow: IUnitOfWork,
                                 alpha2: str) -> bool:
        country = await CountriesService().get_country_by(
                uow, {"alpha2": alpha2})
        return bool(country)
    
    async def update_password(self, uow: IUnitOfWork,
                              user: FullUserSchema, 
                              passwords: UserUpdatePasswordSchema) -> bool:
        if await self.verify_password(user, passwords.old_password):
            new_password = self._hash_password(passwords.new_password)
            await self.edit_user(uow, login=user.login, data={"password": new_password,
                                                        "last_password_change": datetime.datetime.now()})
            return True
        return False
    
    async def verify_password(self, user, password: str) -> bool:
        check_password = user.password.encode()
        is_valid = bcrypt.checkpw(password.encode(), check_password)
        if is_valid:
            return True
        return False

    async def authenticate_user(self, uow: IUnitOfWork,
                                data: SignInSchema) -> Literal[False] | str:
        user = await self.get_user(uow, data={"login": data.login})
        if not user:
            return False
        if not await self.verify_password(user, data.password):
            return False
        return user.login

    def _hash_password(self, password: str) -> str:
        hash_ = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return str(hash_.decode())
    
