from aiogram.fsm.state import StatesGroup, State


class ChannelsState(StatesGroup):
    waiting_for_forward = State()
    waiting_for_channel_id = State()
