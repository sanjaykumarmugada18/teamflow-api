from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DataBase_URL: str

    model_config = SettingsConfigDict(env_file=".env")
settings = Settings()