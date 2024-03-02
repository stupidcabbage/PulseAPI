from dotenv import load_dotenv
from os import getenv

load_dotenv()

class ServerSettings:
    SERVER_ADRESS: str = getenv("SERVER_ADRESS")
    SERVER_PORT: int = int(getenv("SERVER_PORT"))


class PostgresSettings:
    POSTGRES_CONN: str = getenv("POSTGRES_CONN")
    POSTGRES_JDBC_URL: str = getenv("POSTGRES_JDBC_URL")
    POSTGRES_USERNAME: str =  getenv("POSTGRES_USERNAME")
    POSTGRES_PASSWORD: str = getenv("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = getenv("POSTGRES_HOST")
    POSTGRES_PORT: str = getenv("POSTGRES_PORT")
    POSTGRES_DATABASE: str = getenv("POSTGRES_DATABASE")

class DevPostgresSettings:
    POSTGRES_CONN: str = "postgresql://prodtest:prodtest@localhost:5432/prodtest"
    POSTGRES_USERNAME: str = "prodtest"
    POSTGRES_PASSWORD: str = "prodtest"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DATABASE: str = "prodtest"

class JWTSettings:
    SECRET_KEY: str = getenv("RANDOM_SECRET")
    ALGORITHM: str = "HS256"
    ACCSES_TOKEN_EXPIRE_MINUTES = 30


server_settings = ServerSettings()
postgres_settings = PostgresSettings()
jwt_settings = JWTSettings()
