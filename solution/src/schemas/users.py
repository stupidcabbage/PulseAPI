from pydantic import BaseModel, Field



class UserSchema(BaseModel):
    login: str = Field(
            title="Логин пользователя",
            max_length=30,
            pattern=r"[a-zA-Z0-9-]+",
            examples=["yellowMonkey"]
    )
    email: str = Field(
            title="E-mail пользователя",
            max_length=30,
            examples=["yellowstone1980@you.ru"],
            pattern=r"^\S+@\S+\.\S+$"
    )
    country_code: str = Field(
            alias="countryCode",
            title="Двухбуквенный код, уникально идентифицирующий страну",
            max_length=2,
            pattern=r"[a-zA-Z]{2}",
            examples=["RU"]
    )
    is_public: bool = Field(
            alias="isPublic",
            title="Является ли данный профиль публичным.",
            description="Публичные профили доступны другим пользователям:\
                    если профиль публичный, любой пользователь платформы\
                    сможет получить информацию о пользователе.",
            examples=[True, False]
    )
    phone: str = Field(
            title="Номер телефона пользователя в формате +123456789",
            pattern=r"\+[\d]+",
            max_length=20,
            examples=["+74951239922"]
    )
    image: str = Field(
        title="Ссылка на фото для аватара пользователя",
        max_length=200,
        min_length=1,
        examples=["https://http.cat/images/100.jpg"]
    )


class UserRegisterSchema(UserSchema):
    password: str = Field(
        min_length=6,
        max_length=100,
        #pattern=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{6,}$",
        examples=["$aba4821FWfew01#.fewA$"]
    )


class ProfileSchemaOut(BaseModel):
    profile: UserSchema
