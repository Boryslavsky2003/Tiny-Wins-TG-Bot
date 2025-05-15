from aiogram import Router, F


router = Router()


@router.message(F.text == "/create_text_ai")
def create_image_ai():
    pass
