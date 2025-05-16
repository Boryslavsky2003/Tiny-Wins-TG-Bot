from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from bot.utils.access import is_admin
from bot.utils import keyboards

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    try:
        logger.debug(f"Start command from {message.from_user.id}")

        if not is_admin(message.from_user.id):
            logger.warning(f"Unauthorized access: {message.from_user.id}")
            await message.answer("⛔ Доступ заборонено")
            return

        user_name = (
            message.from_user.full_name or message.from_user.first_name or "користувач"
        )
        text = f"Вітаю, {user_name}."

        await message.answer(text, reply_markup=keyboards.create_admin_keyboard())

        logger.info(f"Sent welcome to admin: {user_name} ({message.from_user.id})")

    except AttributeError as e:
        logger.critical(f"User object error: {e} | Message: {message}")
        await message.answer("⚠️ Помилка ідентифікації")

    except Exception as e:
        logger.error(f"Unexpected error: {e} | User: {message.from_user}")
        await message.answer("🔧 Виникла технічна помилка")
