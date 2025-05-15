from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot.states import ChannelsState
from bot.config import settings
from functools import lru_cache
import logging


router = Router()

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1)
def get_admin_ids() -> list[int]:
    """Безпечне отримання ID адміністраторів з кешуванням"""
    try:
        return [int(admin_id.strip()) for admin_id in settings.ADMIN_ID.split(",")]
    except Exception as e:
        logger.error(f"Помилка завантаження ADMIN_ID: {e}")
        return []


@router.message(Command("i_admin"))
async def check_admin_status(message: Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        admin_ids = get_admin_ids()

        logger.info(f"Перевірка адміна: user_id={user_id}, admins={admin_ids}")

        if not admin_ids:
            await message.answer("⚠️ Список адміністраторів не налаштовано")
            return

        if user_id in admin_ids:
            await message.answer(
                "✅ Ви адміністратор!\nДоступні адмін-команди: /admin_panel"
            )
        else:
            await message.answer("⛔ Ви не маєте прав адміністратора")
            await state.set_state(ChannelsState.waiting_for_channel_id)

    except Exception as e:
        logger.error(f"Помилка перевірки адміна: {e}")
        await message.answer("🔧 Технічна помилка. Спробуйте пізніше")
