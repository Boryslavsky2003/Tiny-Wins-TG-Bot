from aiogram import Router

from bot.handlers import (
    hd_get_id,
    hd_start,
    hd_test_ai_model,
)

router = Router()


router.include_router(hd_get_id.router)
router.include_router(hd_start.router)
router.include_router(hd_test_ai_model.router)
