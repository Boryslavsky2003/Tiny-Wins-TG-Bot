from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Telegram Bot
    BOT_TOKEN: str
    ADMIN_ID: str

    # Webhook
    WEBHOOK_DOMAIN: str

    # Channels
    CHANNEL_ID_UA: str = ""
    CHANNEL_ID_US: str = ""

    # API Keys
    OPENAI_API_KEY: str = ""

    # Scheduling
    SCHEDULED_TIME: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
