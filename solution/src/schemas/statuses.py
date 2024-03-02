from pydantic import BaseModel


class OKStatus(BaseModel):
    status: str = "ok"
