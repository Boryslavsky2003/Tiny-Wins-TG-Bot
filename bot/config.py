from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Telegram Bot
    BOT_TOKEN: str
    ADMIN_ID: str

    # Webhook
    WEBHOOK_DOMAIN: str

    # Channels
    UA_CHANNEL_ID: str
    US_CHANNEL_ID: str

    # API Keys
    HUGGINGFACE_TOKEN: str
    MODEL_TEXT_URL: str
    MODEL_IMAGE_URL: str

    # Scheduling
    SCHEDULED_TIME: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
