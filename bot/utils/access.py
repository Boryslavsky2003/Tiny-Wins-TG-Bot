from aiogram.types import Message
from bot.config import settings


def is_admin(user_id: int) -> bool:
    return user_id in settings.ADMIN_ID


def admin_only(handler):
    async def wrapper(message: Message, *args, **kwargs):
        if not is_admin(message.from_user.id):
            await message.answer("⛔ Ця команда доступна лише адміністраторам.")
            return
        return await handler(message, *args, **kwargs)

    return wrapper
