from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.utils import keyboards
from bot.states import ChannelsState


router = Router()


@router.message(F.text == "/get_channel_id")
async def get_channel_id(message: Message, state: FSMContext):
    await message.answer("Select a channel:", reply_markup=(keyboards.channel))
    await state.set_state(ChannelsState.choosing_channel)


@router.message(ChannelsState.choosing_channel, F.text.in_(["ua", "us"]))
async def on_channel_chosen(message: Message, state: FSMContext):
    await message.answer("Send a message from the selected channel")
    await state.clear()


@router.message(F.forward_from_chat)
async def show_channel_id(message: Message):
    chat = message.forward_from_chat

    if chat.type == "channel":
        await message.answer(f"Channel ID: {chat.id}", parse_mode="Markdown")
    else:
        await message.answer("Please forward a message from a channel.")
