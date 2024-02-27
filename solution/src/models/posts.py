import uuid
from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from models.users import User


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[str] = mapped_column(primary_key=True, default_factory=uuid.uuid4)
    content: Mapped[str] = mapped_column()
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
    tags: Mapped[List["Tag"]] = relationship(back_populates="post")
    created_at: Mapped[datetime] = mapped_column(default_factory=func.now)


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[str] = mapped_column(primary_key=True, default_factory=uuid.uuid4)
    name: Mapped[str] = mapped_column()
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship(back_populates="tags")
