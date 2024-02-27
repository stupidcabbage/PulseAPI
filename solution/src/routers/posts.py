from fastapi import APIRouter

from schemas.posts import PostInSchema, PostSchema

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/new", summary="Отправить публикацию")
async def add_new_post(post: PostInSchema) -> PostSchema:
    pass
