import uuid
from sqlalchemy import ForeignKey, UniqueConstraint

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base


class Like(Base):
    __tablename__ = "likes"
    __table_args__ = (
            UniqueConstraint("user_login", "post_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True,
                                    autoincrement=True)
    user_login: Mapped[str] = mapped_column(ForeignKey("users.login"))
    post_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("posts.id"))
    post: Mapped["Post"] = relationship("Post")
    vote: Mapped[int] = mapped_column()
    