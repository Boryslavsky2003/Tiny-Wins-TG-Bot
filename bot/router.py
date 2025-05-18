from aiogram import Router

from bot.handlers import hd_start
from bot.handlers.callbacks import (
    call_create_image_ai,
    call_create_text_ai,
    call_get_id,
    call_test_ai,
)


router = Router()


router.include_router(hd_start.router)

router.include_router(call_create_image_ai.router)
router.include_router(call_create_text_ai.router)
router.include_router(call_get_id.router)
router.include_router(call_test_ai.router)
