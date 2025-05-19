from aiogram.filters.callback_data import CallbackData


class BotCallback(CallbackData, prefix="nav"):
    action: str
