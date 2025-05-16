from aiogram.types import Message, CallbackQuery
from functools import lru_cache, wraps
from loguru import logger
from typing import Union

from bot.config import settings


@lru_cache(maxsize=1)
def get_admin_ids() -> list[int]:
    """Кешований список ID адміністраторів"""
    return settings.admin_ids


def is_admin(user_id: int) -> bool:
    """Надійна перевірка адміністратора"""
    return user_id in get_admin_ids()


def admin_only(handler):
    """Універсальний декоратор для перевірки прав адміна"""

    @wraps(handler)
    async def wrapper(event: Union[Message, CallbackQuery], *args, **kwargs):
        try:
            user = event.from_user
            if not user:
                logger.error("Подія без користувача")
                return

            if not is_admin(user.id):
                if isinstance(event, CallbackQuery):
                    await event.answer("⛔ Доступ заборонено!", show_alert=True)
                else:
                    await event.answer("⛔ Ви не адміністратор!")
                return

            return await handler(event, *args, **kwargs)

        except Exception as e:
            logger.error(f"Помилка в admin_only: {e}")
            if isinstance(event, CallbackQuery):
                await event.answer("🔧 Помилка обробки запиту")
            raise

    return wrapper
