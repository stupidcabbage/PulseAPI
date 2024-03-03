from src.repositories.repository import SQLAlchemyRepository
from src.db.models.likes import Like


class LikesRepositories(SQLAlchemyRepository):
    model = Like