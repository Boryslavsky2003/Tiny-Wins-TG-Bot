from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext


router = Router()


@router.message(Command("lo"))
async def check_admin_status(message: Message, state: FSMContext):
    pass
