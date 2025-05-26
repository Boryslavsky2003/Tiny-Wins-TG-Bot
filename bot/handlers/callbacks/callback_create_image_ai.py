from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext
from loguru import logger
import os
from asyncio import to_thread

from bot.states import CreateImageState
from bot.utils.gen_huggingface.gen_image_model import generate_image_with_prompt
from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "create_image_ai"))
async def handle_create_image_ai(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("✏️ Опишіть зображення, яке ви хочете згенерувати:")
    await state.set_state(CreateImageState.waiting_for_prompt)
    await callback.answer()


@router.message(CreateImageState.waiting_for_prompt)
async def handle_user_prompt(message: Message, state: FSMContext):
    prompt = message.text.strip()

    waiting_msg = await message.answer("🎨 Генерація зображення, зачекайте...")

    try:
        image_path = "ai/ai_image_gen/user_generated_image.png"

        logger.debug(
            f"⏳ Починаємо генерацію зображення: prompt='{prompt}' → {image_path}"
        )

        await to_thread(
            generate_image_with_prompt,
            prompt,
            image_path,
        )

        logger.debug(
            f"✅ Перевіряємо файл після генерації: {os.path.exists(image_path)}, size={os.path.getsize(image_path) if os.path.exists(image_path) else 'N/A'}"
        )

        if not os.path.exists(image_path) or os.path.getsize(image_path) == 0:
            await waiting_msg.delete()
            await message.answer(
                "❌ Не вдалося згенерувати зображення. Спробуйте пізніше."
            )
            return

        await waiting_msg.delete()
        await message.answer_photo(photo=FSInputFile(image_path))

    except Exception as e:
        logger.error(f"Image generation failed: {str(e)}")
        await waiting_msg.delete()
        await message.answer("❌ Сталася помилка під час генерації зображення.")
    finally:
        await state.clear()
