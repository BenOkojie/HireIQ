from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_SERVICE_KEY: str
    AI_API_KEY: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
