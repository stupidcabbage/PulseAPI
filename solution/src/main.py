from fastapi import FastAPI

from routers import countries, posts

app = FastAPI(root_path="/api")

app.include_router(countries.router)
app.include_router(posts.router)


@app.get("/ping")
async def ping():
    return "ok"
