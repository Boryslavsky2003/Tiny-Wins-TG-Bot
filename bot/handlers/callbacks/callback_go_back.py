from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils.access import admin_only
from bot.utils import keyboards


router = Router()


@router.callback_query(F.data == "go_back")
@admin_only
async def handle_go_back(callback: CallbackQuery, state: FSMContext):
    await callback.answer("⏳ Обробляємо ваш запит...")

    await callback.message.answer(reply_markup=keyboards.create_admin_keyboard())
