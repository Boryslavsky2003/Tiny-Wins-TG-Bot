from aiogram import Router

from bot.handlers import (
    hd_channel_id,
    hd_start,
)

router = Router()


router.include_router(hd_channel_id.router)
router.include_router(hd_start.router)
