from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils.access import admin_only


router = Router()


@router.callback_query(F.data == "help_bot")
@admin_only
async def handle_help_bot(callback: CallbackQuery, state: FSMContext):
    await callback.answer("⏳ Обробляємо ваш запит...")
    await callback.message.answer("ПРАЦЮЄ")
