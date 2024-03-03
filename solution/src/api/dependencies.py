from typing import Annotated

from fastapi import Depends
from schemas.users import FullUserSchema
from api.pagination import get_pagination_params

from utils.unitofwork import IUnitOfWork, UnitOfWork
from api.auth.bearer import JWTBearer


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
JWTAuth = Annotated[FullUserSchema, Depends(JWTBearer(UnitOfWork()))]
PaginationDep = Annotated[dict, Depends(get_pagination_params)]
