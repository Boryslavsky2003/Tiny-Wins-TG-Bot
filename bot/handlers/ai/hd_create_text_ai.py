from aiogram import Router, F

from bot.utils.access import admin_only


router = Router()


@router.message(F.text == "/create_text_ai")
@admin_only
def create_image_ai():
    pass
