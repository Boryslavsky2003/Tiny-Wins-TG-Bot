from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "complex_ai_generation"))
async def handle_complex_ai_generation(callback: CallbackQuery, state: FSMContext):
    await callback.answer("")

    await callback.message.answer(
        text="🏗️ Дотримуйтесь інструкцій.",
    )
