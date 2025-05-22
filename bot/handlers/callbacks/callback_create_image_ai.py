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
