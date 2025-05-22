from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils import keyboards
from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "go_back"))
async def handle_go_back(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    await callback.message.answer(
        text="Головне меню",
        reply_markup=keyboards.create_admin_keyboard(),
    )
