from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot.states import ChannelsState

from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "create_text_ai"))
async def handle_create_text_ai(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Test")
