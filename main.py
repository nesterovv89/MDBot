import asyncio
import logging
import re
import keyboards as k
import texts as t
import media as m
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery, Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from states import Mailing, Application
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import admins, handlers
from config import config
from db import profile, request, users, createtables
from aiogram import F
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

admin_ids = [375959767, 505958678, 314310391]
# , 505958678, 314310391

async def main():
    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(admins.router, handlers.router)
    await createtables()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



