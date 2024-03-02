from fastapi import FastAPI

from api import countries, posts, ping, users, friends
from api.auth import auth
from api.exceptions import base_exception_handler, BaseRouterException, db_unique_exception_handler, validation_exception_handler, doesnot_exists_handler
from fastapi.exceptions import RequestValidationError

from repositories.excpetions import DBUniqueException, CountryDoesNotExists, DoesNotExistsException, UserDoesNotExists


app = FastAPI(root_path="/api")


app.include_router(ping.router)
app.include_router(countries.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(friends.router)
app.add_exception_handler(DoesNotExistsException, doesnot_exists_handler)
app.add_exception_handler(BaseRouterException, base_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(DBUniqueException, db_unique_exception_handler)