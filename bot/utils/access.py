from aiogram.types import Message
from bot.config import settings
from functools import lru_cache


@lru_cache(maxsize=1)
def get_admin_ids() -> list[int]:
    """Кешований список ID адміністраторів"""
    return settings.admin_ids


def is_admin(user_id: int) -> bool:
    """Надійна перевірка адміністратора"""
    return user_id in get_admin_ids()


def admin_only(handler):
    """Декоратор для адмін-команд з обробкою помилок"""

    async def wrapper(message: Message, *args, **kwargs):
        if not is_admin(message.from_user.id):
            await message.answer("⛔ Доступ заборонено")
            return
        try:
            return await handler(message, *args, **kwargs)
        except Exception:
            await message.answer("🔧 Помилка виконання команди")
            raise

    return wrapper
