import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
import os

load_dotenv()
logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}! I'm a Telegram bot.")

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

@dp.startup()
async def on_startup() -> None:
    logging.info("Bot started with polling")

@dp.shutdown()
async def on_shutdown() -> None:
    logging.info("Bot stopped")

async def main() -> None:
    # Using polling mode instead of webhooks
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped!")