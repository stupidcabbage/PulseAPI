from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


class AbstractException(Exception):
    def __init__(self, reason: str, status_code: int):
        self.reason = reason
        self.status_code = status_code

class CountryDoesNotExists(AbstractException):
    def __init__(self):
        self.reason = "Подобный страны не существует."
        self.status_code = 404

router = APIRouter()

async def base_exception_handler(request: Request, exc: AbstractException):
    return JSONResponse(
            status_code=exc.status_code,
            content={"reason": exc.reason})
