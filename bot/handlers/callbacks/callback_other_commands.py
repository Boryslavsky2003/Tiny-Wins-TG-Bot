from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils import keyboards
from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "other_commands"))
async def handle_other_commands(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    await callback.message.answer(
        text="Меню адміністратора",
        reply_markup=keyboards.create_other_commands_keyboard(),
    )
