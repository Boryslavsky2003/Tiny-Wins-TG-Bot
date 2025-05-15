from aiogram.types import Message
from bot.config import settings


def is_admin(user_id: int) -> bool:
    """Перевіряє, чи є користувач адміністратором"""
    admin_ids = [int(admin_id) for admin_id in settings.ADMIN_ID.split(",")]
    return user_id in admin_ids


def admin_only(handler):
    """Декоратор для обмеження доступу до команд адміністраторам"""

    async def wrapper(message: Message, *args, **kwargs):
        if not is_admin(message.from_user.id):
            await message.answer("⛔ Ця команда доступна лише адміністраторам.")
            return
        return await handler(message, *args, **kwargs)

    return wrapper
