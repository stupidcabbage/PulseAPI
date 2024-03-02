from repositories.excpetions import UserDoesNotExists
from services.users import UsersService
from utils.unitofwork import IUnitOfWork


class FriendsService:
    async def add_friend(self, uow: IUnitOfWork,
                       who_add_login: str, login: str) -> bool:
        if who_add_login == login:
            return True
        
        if not await self._is_user_exists(uow, login):
            raise UserDoesNotExists
        
        async with uow:
            await uow.friends.add_one(
                {"who_added_user_login": who_add_login,
                 "added_user_login": login})
            await uow.commit()
            return True
    
    async def _is_user_exists(uow: IUnitOfWork, login: str) -> bool:
        if await UsersService().get_user(uow, {"login": login}):
            return True
        return False
