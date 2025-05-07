from aiogram.fsm.state import StatesGroup, State


class ChannelsState(StatesGroup):
    choosing_channel = State()
