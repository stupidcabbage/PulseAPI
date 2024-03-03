from src.repositories.repository import SQLAlchemyRepository
from src.db.models.posts import Post, Tag


class PostsRepositories(SQLAlchemyRepository):
    model = Post


class TagsRepositories(SQLAlchemyRepository):
    model = Tag