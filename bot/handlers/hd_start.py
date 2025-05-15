from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from loguru import logger


router = Router()


@router.message(Command("start"))
async def cmd_start_handler(message: Message) -> None:
    try:
        await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    except Exception as e:
        logger.error(f"Error sending message: {e}")
