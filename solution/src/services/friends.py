from repositories.excpetions import UserDoesNotExists
from services.users import UsersService
from schemas.friends import FriendSchema
from utils.unitofwork import IUnitOfWork


class FriendsService:
    async def add_friend(self, uow: IUnitOfWork,
                         from_login: str, login: str) -> bool:
        if from_login == login:
            return True
            
        if await self.get_friend(uow, from_login, login):
            return True

        if not await self._is_user_exists(uow, login):
            raise UserDoesNotExists
        
        async with uow:
            await uow.friends.add_one(
                {"who_added_user_login": from_login,
                 "added_user_login": login})
            await uow.commit()
        return True
    
    async def get_friend(self, uow: IUnitOfWork,
                         from_login: str, login: str) -> FriendSchema:
        async with uow:
            return await uow.friends.get_where(data={"who_added_user_login": from_login,
                                                     "added_user_login": login})


    async def remove_friend(self, uow: IUnitOfWork,
                            from_login: str, login: str) -> bool:
        if not await self.get_friend(uow, from_login, login):
            return True
        async with uow:
            await uow.friends.remove_where(data={"who_added_user_login": from_login,
                                                 "added_user_login": login})
            await uow.commit()
        return True


    async def _is_user_exists(self, uow: IUnitOfWork, login: str) -> bool:
        if await UsersService().get_user(uow, {"login": login}):
            return True
        return False