from src.repositories.repository import SQLAlchemyRepository

from src.db.models.users import Friend


class FriendsRepository(SQLAlchemyRepository):
    model = Friend
