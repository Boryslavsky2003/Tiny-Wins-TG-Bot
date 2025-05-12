import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from dotenv import load_dotenv

from loguru import logger

from bot.config import settings
from bot.router import router
from bot.utils.huggingface import huggingface_text, huggingface_image

load_dotenv()


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


WEBHOOK_PATH = f"/webhook/{settings.BOT_TOKEN}"
WEBHOOK_URL = f"{settings.WEBHOOK_DOMAIN}{WEBHOOK_PATH}"

logger.info("Routers connected")


async def on_startup(app: web.Application):
    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook set to {WEBHOOK_URL}")


async def on_shutdown(app: web.Application):
    await bot.delete_webhook()
    print("Webhook deleted")


def main():
    app = web.Application()

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app.router.add_post(WEBHOOK_PATH, SimpleRequestHandler(dispatcher=dp, bot=bot))
    setup_application(app, dp, bot=bot)

    return app


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    print(settings.BOT_TOKEN)
    print(settings.WEBHOOK_DOMAIN)
    print(settings.HUGGINGFACE_TOKEN)

    text = huggingface_text.generate_text(
        "Give me a short motivational quote for women."
    )
    print(text)

    file = huggingface_image.generate_image(
        "a peaceful morning in a forest, watercolor style"
    )
    print("Saved image to:", file)

    port = int(os.getenv("PORT", "8080"))
    web.run_app(main(), port=port, host="0.0.0.0")
