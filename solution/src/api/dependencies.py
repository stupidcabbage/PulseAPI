from typing import Annotated

from fastapi import Depends
from schemas.users import FullUserSchema

from utils.unitofwork import IUnitOfWork, UnitOfWork
from api.auth.bearer import JWTBearer


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
JWTAuth = Annotated[FullUserSchema, Depends(JWTBearer(UnitOfWork()))]