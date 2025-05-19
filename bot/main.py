import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from dotenv import load_dotenv
from loguru import logger

from bot.config import settings
from bot.router import router
# from bot.utils.test_ai_model import test_ai_model

load_dotenv()

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

WEBHOOK_PATH = f"/webhook/{settings.BOT_TOKEN}"
WEBHOOK_URL = f"{settings.WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

logger.info("Routers connected")


async def on_startup(app: web.Application):
    try:
        await bot.set_webhook(WEBHOOK_URL)
        logger.success(f"Webhook successfully set to {WEBHOOK_URL}")

        # await test_ai_model()

    except Exception as e:
        logger.error(f"Startup error: {str(e)}")
        raise


async def on_shutdown(app: web.Application):
    try:
        await bot.delete_webhook()
        logger.info("Webhook deleted")
    except Exception as e:
        logger.error(f"Shutdown error: {str(e)}")
        raise


def main():
    app = web.Application()

    if not all(
        [settings.BOT_TOKEN, settings.WEBHOOK_DOMAIN, settings.HUGGINGFACE_TOKEN]
    ):
        logger.error("Missing required environment variables!")
        raise ValueError("Missing required environment variables")

    logger.info(f"Bot token: {settings.BOT_TOKEN[:5]}...{settings.BOT_TOKEN[-5:]}")
    logger.info(f"Webhook domain: {settings.WEBHOOK_DOMAIN}")
    logger.info("Token valid:", bool(settings.HUGGINGFACE_TOKEN))
    logger.info(
        f"HuggingFace token: {settings.HUGGINGFACE_TOKEN[:5]}...{settings.HUGGINGFACE_TOKEN[-5:]}"
    )

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.router.add_post(WEBHOOK_PATH, SimpleRequestHandler(dispatcher=dp, bot=bot))
    setup_application(app, dp, bot=bot)

    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        port = int(os.getenv("PORT", "8080"))
        web.run_app(main(), port=port, host="0.0.0.0")
    except Exception as e:
        logger.critical(f"Application failed to start: {str(e)}")
        raise
