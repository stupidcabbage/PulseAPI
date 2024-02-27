import uuid

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserSchema


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int]
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    country_code: Mapped[str] = mapped_column()
    is_public: Mapped[bool] = mapped_column(default=True)
    phone: Mapped[str] = mapped_column(unique=True)
    image: Mapped[str] = mapped_column()
