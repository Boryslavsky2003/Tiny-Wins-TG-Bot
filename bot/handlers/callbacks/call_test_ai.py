from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import ChannelsState
from bot.utils.access import admin_only

from loguru import logger


router = Router()


@router.callback_query(F.data == "test_ai")
async def handle_create_image_ai(callback: CallbackQuery, state: FSMContext):
    logger.debug(f"Received callback: {callback.data}")
    await callback.answer()
    await callback.message.answer("Test received!")