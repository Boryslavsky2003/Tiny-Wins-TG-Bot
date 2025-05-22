from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.fsm.context import FSMContext
from loguru import logger
import os

from bot.states import CreateImageState
from bot.utils.huggingface import huggingface_image
from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "create_image_ai"))
async def handle_create_image_ai(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("✏️ Опишіть зображення, яке ви хочете згенерувати:")
    await state.set_state(CreateImageState.waiting_for_prompt)


@router.message(CreateImageState.waiting_for_prompt)
async def handle_prompt(message: Message, state: FSMContext):
    prompt = message.text.strip()
    image_path = "ai/ai_image_gen/generated_image.png"

    await message.answer("⏳ Генерація зображення...")

    try:
        huggingface_image.generate_image(prompt, image_path)

        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
            photo = FSInputFile(image_path)
            await message.answer_photo(
                photo=photo,
                caption=f"🖼️ Згенеровано за описом: _{prompt}_",
                parse_mode="Markdown",
            )
        else:
            await message.answer(
                "⚠️ Вибачте, не вдалося згенерувати зображення. Спробуйте інший опис."
            )
    except Exception as e:
        logger.error(f"Image generation error: {str(e)}")
        await message.answer("❌ Сталася помилка під час генерації зображення.")
    finally:
        await state.clear()
