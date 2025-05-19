from aiogram import Router

from bot.handlers import (
    hd_start,
    any_messages,
)
from bot.handlers.callbacks import (
    callback_create_image_ai,
    callback_create_text_ai,
    callback_get_id,
    callback_test_ai,
    callback_other_commands,
    callback_go_back,
)


router = Router()


router.include_router(hd_start.router)
router.include_router(any_messages.router)

router.include_router(callback_create_image_ai.router)
router.include_router(callback_create_text_ai.router)
router.include_router(callback_get_id.router)
router.include_router(callback_test_ai.router)
router.include_router(callback_other_commands.router)
router.include_router(callback_go_back.router)
