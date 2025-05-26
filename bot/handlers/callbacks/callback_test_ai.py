from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext
from loguru import logger
import os

from bot.utils.callback_data import BotCallback
from bot.utils.gen_huggingface import test_ai_model


router = Router()


@router.callback_query(BotCallback.filter(F.action == "test_ai"))
async def handle_test_ai(callback: CallbackQuery, state: FSMContext):
    try:
        logger.debug(f"User {callback.from_user.id} button test_ai")

        await callback.answer("🔄 Обробка запиту...", show_alert=False)

        waiting_msg = await callback.message.answer(
            "Будь ласка, зачекайте ⏳",
            parse_mode="Markdown",
        )

        await test_ai_model.complex_test_ai_model()

        image_path = "ai/ai_test_gen/test_generated_image.png"
        text_path = "ai/ai_test_gen/test_generated_text.txt"

        if not os.path.exists(image_path) or os.path.getsize(image_path) == 0:
            await waiting_msg.delete()
            await callback.message.answer(
                "Вибачте, сталася тимчасова проблема з генерацією зображення. Спробуйте пізніше."
            )
            return

        if os.path.exists(text_path):
            with open(text_path, "r", encoding="utf-8") as f:
                generated_text = f.read()
        else:
            generated_text = "Текст не знайдено."

        photo = FSInputFile(image_path)

        await waiting_msg.delete()

        await callback.message.answer_photo(
            photo=photo,
            caption=generated_text,
        )

    except Exception as e:
        logger.error(f"Error in handle_test_ai: {str(e)}")
        await callback.answer("❌ Сталася помилка", show_alert=True)
