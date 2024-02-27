import uuid

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserSchema


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True, default_factory=uuid.uuid4)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    country_code: Mapped[str] = mapped_column()
    is_public: Mapped[bool] = mapped_column(default=True)
    phone: Mapped[str] = mapped_column(unique=True)
    image: Mapped[str] = mapped_column()

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            login=self.login,
            email=self.email,
            country_code=self.country_code,
            is_public=self.is_public,
            phone=self.phone,
            image=self.image
        )
