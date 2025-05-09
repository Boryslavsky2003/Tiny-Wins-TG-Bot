from aiogram import Router

from bot.handlers import (
    hd_get_channel_id,
    hd_get_user_id,
    hd_start,
)

router = Router()


router.include_router(hd_get_channel_id.router)
router.include_router(hd_get_user_id.router)
router.include_router(hd_start.router)
