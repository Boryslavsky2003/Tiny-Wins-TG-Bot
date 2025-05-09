from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states import ChannelsState


router = Router()


@router.message(F.text == "/get_channel_id")
async def get_channel_id(message: Message, state: FSMContext):
    await message.answer("send me a message from the telegram channel:")
    await state.set_state(ChannelsState.waiting_for_forward)


@router.message(ChannelsState.waiting_for_forward, F.forward_from_chat)
async def show_channel_id(message: Message, state: FSMContext):
    chat = message.forward_from_chat

    if chat.type == "channel":
        await message.answer(
            f"Channel:\nID: {chat.id}\nChannel name: {chat.title}",
            parse_mode="Markdown",
        )
        await state.clear()
    else:
        await message.answer("Please forward a message from a channel.")
