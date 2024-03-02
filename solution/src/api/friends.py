from fastapi import APIRouter

from api.dependencies import JWTAuth, UOWDep
from schemas.friends import FriendOutInSchema
from schemas.statuses import OKStatus
from services.friends import FriendsService


router = APIRouter(prefix="/friends", tags=["friends"])


@router.post("/add")
async def add_friend(uow: UOWDep, user: JWTAuth,
                     data: FriendOutInSchema) -> OKStatus:
    await FriendsService().add_friend(uow,
                                      from_login=user.login,
                                      login=data.login)
    return OKStatus


@router.post("/remove")
async def remove_friend(uow: UOWDep, user: JWTAuth,
                        data: FriendOutInSchema) -> OKStatus:
    await FriendsService().remove_friend(uow,
                                         from_login=user.login,
                                         login=data.login)
    return OKStatus

