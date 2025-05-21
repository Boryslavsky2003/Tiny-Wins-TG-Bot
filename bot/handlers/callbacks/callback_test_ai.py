from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from loguru import logger

from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "test_ai"))
async def handle_test_ai(callback: CallbackQuery, state: FSMContext):
    try:
        # 1. Логування події
        logger.debug(f"Користувач {callback.from_user.id} натиснув test_ai")

        # 2. Відповідь на натискання (важливо робити першим)
        await callback.answer("🔄 Обробка запиту...", show_alert=False)

        # 3. Основна логіка
        await callback.message.answer(
            "✅ Тестовий запит отримано!", parse_mode="Markdown"
        )

        # Додатковий debug
        logger.debug(f"Повідомлення успішно відправлено для {callback.from_user.id}")

    except Exception as e:
        logger.error(f"Помилка в handle_test_ai: {str(e)}")
        await callback.answer("❌ Сталася помилка", show_alert=True)
