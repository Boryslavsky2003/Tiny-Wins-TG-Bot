from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Bot settings
    BOT_TOKEN: str

    # Database settings
    DATABASE_URL: str

    # API settings
    API_URL: str = "https://api.example.com"
    API_KEY: str = ""

    # Application settings
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # Web server settings (if applicable)
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
