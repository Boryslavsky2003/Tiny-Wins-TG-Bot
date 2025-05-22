from aiogram import Router, F
from aiogram.types import Message

from bot.utils.access import admin_only


router = Router()


# @router.message(F.text)
# @admin_only
# async def echo(message: Message):
#     await message.answer(
#         await message.answer(
#             f"👋 {message.from_user.first_name}, щоб почати роботу, будь ласка, введіть команду /start",
#             parse_mode="Markdown",
#         ),
#         parse_mode="Markdown",
#     )
