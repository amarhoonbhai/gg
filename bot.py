# bot.py

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_CONFIG
from db.base import init_db
from handlers import register_all_handlers


async def main() -> None:
    # Basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    # Init DB (we'll create db/base.py next)
    await init_db(BOT_CONFIG.mongo_uri, BOT_CONFIG.db_name)

    # Init bot & dispatcher
    bot = Bot(token=BOT_CONFIG.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())

    # Register all handlers/routers (we'll define handlers/__init__.py next)
    register_all_handlers(dp)

    logging.info("ClasherGG Bot started ✅")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
