from src.repositories.repository import SQLAlchemyRepository

from src.db.models.users import User


class UsersRepository(SQLAlchemyRepository):
    model = User
