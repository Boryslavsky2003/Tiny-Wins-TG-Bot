from aiogram import Router
from aiogram.filters import Command


router = Router()


@router.message(Command("create_image_ai"))
def create_image_ai():
    pass
