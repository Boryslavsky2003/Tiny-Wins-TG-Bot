from pydantic_settings import BaseSettings
from datetime import time
from typing import List
from pydantic import field_validator


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
    ONE_SCHEDULED_TIME: time
    TWO_SCHEDULED_TIME: time

    @property
    def admin_ids(self) -> List[int]:
        """Повертає список ID адміністраторів як цілі числа"""
        return [int(id.strip()) for id in self.ADMIN_ID.split(",")]

    @field_validator("ADMIN_ID")
    def validate_admin_ids(cls, v):
        """Валідація формату ADMIN_ID"""
        if not all(id.strip().isdigit() for id in v.split(",")):
            raise ValueError("ADMIN_ID має містити тільки цифри, розділені комами")
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
