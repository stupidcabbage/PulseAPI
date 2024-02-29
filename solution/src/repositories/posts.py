from repositories.repository import SQLAlchemyRepository
from db.models.posts import Post, Tag


class PostsRepositories(SQLAlchemyRepository):
    model = Post


class TagsRepositories(SQLAlchemyRepository):
    model = Tag 
