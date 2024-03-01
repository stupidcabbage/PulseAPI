import bcrypt

from schemas.users import UserRegisterSchema
from repositories.excpetions import CountryDoesNotExists
from services.countries import CountriesService
from utils.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, user: UserRegisterSchema):
        country = await CountriesService().get_country_by(
                uow, {"alpha2": user.country_code})
        if not country:
            raise CountryDoesNotExists

        user.password = self._hash_password(user.password)
        user_dict = user.model_dump(by_alias=False)
        async with uow:
            user_id = await uow.users.add_one(data=user_dict)
            await uow.commit()
            return user_id

    def _hash_password(self, password: str) -> str:
        bytes_ = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hash_ = bcrypt.hashpw(bytes_, salt)
        return hash_.decode()
