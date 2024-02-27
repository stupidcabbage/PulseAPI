from datetime import datetime

from pydantic import BaseModel, Field


class PostInSchema(BaseModel):
    content: str = Field(
            max_length=1000,
            description="Текст публикации"
    )
    tags: list[str] = Field(
            max_length=20,
            description="Список тегов публикации",
            examples=[["тинькофф", "спббиржа", "moex"]]
    )


class PostSchema(BaseModel):
    id: str = Field(
            description="Уникальный идентификатор публикации,\
                    присвоенный сервером.",
            examples=["550e8400-e29b-41d4-a716-446655440000"]
    )
    content: str = Field(
            max_length=1000,
            description="Текст публикации"
    )
    author: str = Field(description="Автор публикации")
    tags: list[str] = Field(
            max_length=20,
            description="Список тегов публикации",
            examples=[["тинькофф", "спббиржа", "moex"]]
    )
    created_at: datetime = Field(
            description="Серверная дата и время в момент, когда пользователь\
                    отправил данную публикацию. Передается в формате RFC3339.",
            examples=["2006-01-02T15:04:05Z07:00"],
            alias="createdAt"
    )
    likes_count: int = Field(
            description="Число лайков, набранное публикацией.",
            alias="likesCount"
    )
    dislikes_count: int = Field(
            description="Число дизлайков, набранное публикацией.",
            alias="dislikesCount"
    )
