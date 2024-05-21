import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

import admins
import handlers
import keyboards as k
import media as m
import texts as t
from config import config
from db import createtables

load_dotenv()


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(admins.router, handlers.router)
    await createtables()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



