from fastapi import FastAPI

from routers import countries, posts, auth
from routers.exceptions import base_exception_handler, BaseRouterException, validation_exception_handler
from fastapi.exceptions import RequestValidationError


app = FastAPI(root_path="/api")

app.include_router(countries.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.add_exception_handler(BaseRouterException, base_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/ping")
async def ping():
    return "ok"
