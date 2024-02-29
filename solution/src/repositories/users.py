from repositories.repository import SQLAlchemyRepository

from db.models.users import User


class UsersRepository(SQLAlchemyRepository):
    model = User
