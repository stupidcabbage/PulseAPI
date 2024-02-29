from db.models.countries import Country
from repositories.repository import SQLAlchemyRepository


class CountriesRepository(SQLAlchemyRepository):
    model = Country
