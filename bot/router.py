from aiogram import Router

from bot.handlers import (
    hd_start,
)

router = Router()


router.include_router(hd_start.router)
