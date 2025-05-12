from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states import ChannelsState

from bot.utils.access import admin_only


router = Router()


@router.message(F.text == "/get_id")
@admin_only
async def get_channel_id(message: Message, state: FSMContext):
    await message.answer(
        "👀 Send me a forwarded message from a channel or from a user:"
    )
    await state.set_state(ChannelsState.waiting_for_forward)


@router.message(ChannelsState.waiting_for_forward)
@admin_only
async def show_channel_id(message: Message, state: FSMContext):
    chat = message.forward_from_chat
    user = message.forward_from

    if chat and chat.type == "channel":
        await message.answer(
            f"📢 *Channel:*\nID: `{chat.id}`\nTitle: {chat.title}",
            parse_mode="Markdown",
        )
    elif user:
        await message.answer(
            f"👤 *User:*\nID: `{user.id}`\nFull name: {user.full_name}",
            parse_mode="Markdown",
        )
    else:
        await message.answer("⚠️ Please forward a message from a *channel* or a *user*.")

    await state.clear()
