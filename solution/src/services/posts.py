import re

from src.schemas.posts import PostInSchema, PostSchema
from src.repositories.excpetions import ProfileAccessDenied
from src.services.users import UsersService
from src.utils.unitofwork import IUnitOfWork


class PostsService:
    ID_REGEX = r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    async def add_post(self, uow: IUnitOfWork, from_login: str,
                       post: PostInSchema) -> PostSchema:
        async with uow:
            new_post = await uow.posts.add_one(data={"author_login": from_login,
                                                 "content": post.content})
            all_tags = []
            for i in post.tags:
                tag = await uow.tags.add_one(data={"post_id": new_post.id,
                                                   "tag": i.tag})
                all_tags.append(tag)
            new_post.tags = all_tags
            await uow.commit()
            return new_post

    async def get_post(self, uow: IUnitOfWork, from_login: str,
                       data: dict[str, list | str]) -> PostSchema:
        async with uow:
            if data.get("id"):
                is_valid = re.match(self.ID_REGEX, data.get("id"))
                if not is_valid:
                    raise ProfileAccessDenied(reason="Публикации не существует.")
                
            post = await uow.posts.get_where(data=data)
            if not post:
                raise ProfileAccessDenied(reason="Публикации не существует.")
            if not await UsersService().is_user_has_access(uow, from_login,
                                                                post.author):
                raise ProfileAccessDenied(reason="Нет доступа к публикации.")
            return post

    async def get_posts(self, uow: IUnitOfWork, from_login: str, login: str,
                        limit: int, offset: int) -> list[PostSchema]:
        async with uow:
            if not await UsersService().is_user_has_access(uow, from_login,
                                                           login):
                raise ProfileAccessDenied(reason="Нет доступа к публикациям.")

            posts = await uow.posts.pagination_get(data={"author_login": login},
                                                   limit=limit, offset=offset,
                                                   order_by="created_at")
            return posts
