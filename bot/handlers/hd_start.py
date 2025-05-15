from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.utils.access import is_admin


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    if not is_admin(message.from_user.id):
        await message.answer("⛔ Доступ заборонено")
        return

    await message.answer(f"Вітаю, адміне {message.from_user.full_name}!")
