from aiogram import Bot
from bot.config import settings


async def publish_to_channels(bot: Bot, text: str):
    await bot.send_message(chat_id=settings.UA_CHANNEL_ID, text=text)
    await bot.send_message(chat_id=settings.US_CHANNEL_ID, text=text)


