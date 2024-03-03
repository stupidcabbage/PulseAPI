from typing import Annotated

from fastapi import Depends
from src.schemas.users import FullUserSchema
from src.api.pagination import get_pagination_params

from src.utils.unitofwork import IUnitOfWork, UnitOfWork
from src.api.auth.bearer import JWTBearer


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
JWTAuth = Annotated[FullUserSchema, Depends(JWTBearer(UnitOfWork()))]
PaginationDep = Annotated[dict, Depends(get_pagination_params)]
