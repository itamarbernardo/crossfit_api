from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    DB_URL: str = Field(default='postgresql+asyncpg://admin:1234@localhost:5433/crossfit_db')


settings = Settings()