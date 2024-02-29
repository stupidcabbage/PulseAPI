from fastapi import FastAPI

from routers import countries, posts
from routers.exceptions import base_exception_handler, AbstractException

app = FastAPI(root_path="/api")

app.include_router(countries.router)
app.include_router(posts.router)
app.add_exception_handler(AbstractException, base_exception_handler)


@app.get("/ping")
async def ping():
    return "ok"
