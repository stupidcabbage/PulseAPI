from enum import Enum
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Regions(Enum):
    europe = "Europe"
    afirca = "Africa"
    oceania = "Ocenia"
    asia = "Asia"


class Country(Base):
    __tablename__ = "countries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()
    alpha2: Mapped[str] = mapped_column()
    alpha3: Mapped[str] = mapped_column()
    region: Mapped[Regions] = mapped_column()
