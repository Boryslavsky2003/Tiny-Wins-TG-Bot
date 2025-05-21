from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.states import ChannelsState
from bot.utils.callback_data import BotCallback


router = Router()


@router.callback_query(BotCallback.filter(F.action == "get_id"))
async def handle_get_id(callback: CallbackQuery, state: FSMContext):
    try:
        await callback.answer("")
        await callback.message.edit_reply_markup()

        await callback.message.answer(
            "👀 Надішліть переслане повідомлення з каналу або від користувача:",
            parse_mode="Markdown",
        )

        await state.set_state(ChannelsState.waiting_for_forward)
        await callback.answer()

    except Exception as e:
        await callback.answer("🔧 Помилка обробки запиту", show_alert=True)
        raise e


@router.message(ChannelsState.waiting_for_forward)
async def show_id_handler(message: Message, state: FSMContext):
    try:
        chat = message.forward_from_chat
        user = message.forward_from

        if chat and chat.type == "channel":
            response = f"📢 *Канал:*\nID: `{chat.id}`\nНазва: {chat.title}"
        elif user:
            response = f"👤 *Користувач:*\nID: `{user.id}`\nІм'я: {user.full_name}"
        else:
            response = (
                "⚠️ Будь ласка, перешліть повідомлення з *каналу* або *користувача*."
            )

        await message.answer(response, parse_mode="Markdown")

    finally:
        await state.clear()
