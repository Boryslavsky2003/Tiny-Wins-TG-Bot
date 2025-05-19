from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from bot.utils.access import admin_only
from bot.utils import keyboards


router = Router()


@router.message(CommandStart())
@admin_only
async def cmd_start(message: Message):
    user = message.from_user
    user_id = user.id
    user_name = user.full_name or user.first_name or "Користувач"

    logger.debug(f"Command /start from the user: {user_name} (ID: {user_id})")

    try:
        welcome_text = f"👋 Вітаю, {user_name}. Ви увійшли як адміністратор."
        await message.answer(
            welcome_text, reply_markup=keyboards.create_admin_keyboard()
        )

        logger.info(f"Sent a greeting to the admin: {user_name} (ID: {user_id})")

    except AttributeError as e:
        logger.critical(f"Error receiving user data: {e} | Message: {message}")
        await message.answer("⚠️ Помилка при обробці вашого профілю.")

    except Exception as e:
        logger.exception(f"Невідома помилка під час виконання /start: {e}")
        await message.answer("🔧 Виникла технічна помилка. Спробуйте пізніше.")
