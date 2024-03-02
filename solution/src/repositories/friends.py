from repositories.repository import SQLAlchemyRepository

from db.models.users import Friend


class FriendsRepository(SQLAlchemyRepository):
    model = Friend
