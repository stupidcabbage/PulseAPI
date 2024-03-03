from repositories.repository import SQLAlchemyRepository
from db.models.likes import Like


class LikesRepositories(SQLAlchemyRepository):
    model = Like