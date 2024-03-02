from fastapi import APIRouter

from api.dependencies import JWTAuth, UOWDep
from schemas.friends import AddFriendSchema
from schemas.statuses import OKStatus
from services.friends import FriendsService


router = APIRouter(prefix="/friends", tags=["friends"])


@router.post("/add")
async def add_friend(uow: UOWDep, user: JWTAuth,
                     data: AddFriendSchema) -> OKStatus:
    await FriendsService().add_friend(uow,
                                      who_add_login=user.login,
                                      login=data.login)
    return OKStatus