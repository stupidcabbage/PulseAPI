from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class BaseRouterException(Exception):
    def __init__(self, reason: str, status_code: int):
        self.reason = reason
        self.status_code = status_code


class CountryDoesNotExists(BaseRouterException):
    def __init__(self):
        self.reason = "Подобный страны не существует."
        self.status_code = 404


class DBException(BaseRouterException):
    def __init__(self, reason: str):
        self.reason = reason
        self.status_code = 409


router = APIRouter()


async def base_exception_handler(request: Request, exc: BaseRouterException):
    return JSONResponse(
            status_code=exc.status_code,
            content={"reason": exc.reason})


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"reason":
                 _generate_validation_exception_reason(exc)}
    )

def _generate_validation_exception_reason(exc: RequestValidationError):
    error = exc.errors()[0]
    return f"Field: {error.get("loc")[-1]}. Error: {error.get('msg')}"
