from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils.access import admin_only
from bot.utils import keyboards
from bot.utils.callback_data import BotCallback

router = Router()


@router.callback_query(BotCallback.filter(F.action == "other_commands"))
@admin_only
async def handle_other_commands(callback: CallbackQuery, state: FSMContext):
    await callback.answer("⏳ Обробляємо ваш запит...")

    user = callback.message.from_user
    text = f"{user.first_name}, Ви повернулися до меню адміністратора."

    await callback.message.answer(
        text, reply_markup=keyboards.create_other_commands_keyboard()
    )
