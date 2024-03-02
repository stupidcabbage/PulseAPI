from datetime import datetime
from pydantic import BaseModel, Field


class AddFriendSchema(BaseModel):
    login: str = Field(max_length=30,
                       pattern=r"[a-zA-Z0-9-]+",
                       examples=["yellowMonkey"])


class FriendSchema(BaseModel):
    added: str = Field(summary="Login добавившего",
                       exclude=True)
    add: str = Field(summary="Login добавленного",
                     alias="login")
    added_at: str = Field(summary="Дата добавления в формате RFC3339",
                          alias="addedAt")