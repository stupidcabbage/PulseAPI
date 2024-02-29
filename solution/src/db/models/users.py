from typing import List
import uuid
from sqlalchemy import ForeignKey, UniqueConstraint

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
# from db.models.posts import Post


class User(Base):
    __tablename__ = "users"
    __table_args__ = (
            UniqueConstraint("login", "email", "phone", name="user_uc"),
    )

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    country_code: Mapped[str] = mapped_column(ForeignKey("countries.alpha2",
                                                         use_alter=True))
    is_public: Mapped[bool] = mapped_column(default=True)
    phone: Mapped[str] = mapped_column(unique=True)
    image: Mapped[str] = mapped_column()
    posts: Mapped[List["Post"]] = relationship(back_populates="author")
