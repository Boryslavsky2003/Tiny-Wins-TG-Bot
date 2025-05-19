from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import ChannelsState
from bot.utils.access import admin_only


router = Router()


@router.callback_query(F.data == "create_text_ai")
async def handle_create_image_ai(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Test")
