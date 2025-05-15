from aiogram import Router

from bot.handlers import (
    hd_get_id,
    hd_start,
    hd_i_admin,
    hd_admin_panel,
)
from bot.handlers.ai import (
    hd_test_ai,
    hd_create_text_ai,
    hd_create_image_ai,
)

router = Router()


router.include_router(hd_get_id.router)
router.include_router(hd_start.router)
router.include_router(hd_i_admin.router)
router.include_router(hd_admin_panel.router)

router.include_router(hd_test_ai.router)
router.include_router(hd_create_text_ai.router)
router.include_router(hd_create_image_ai.router)
