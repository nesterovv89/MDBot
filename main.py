import asyncio
import os
import sqlite3
import logging
import re
import keyboards as k
import texts as t
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import URLInputFile
from aiogram.filters.command import Command
from aiogram.utils.formatting import Text, Bold
from aiogram.filters import Command, StateFilter
from aiogram.types import ContentType
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InputMediaPhoto
from admins import IsAdmin
from config import config
from db import profile, request, users, createtables
from aiogram import F
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
admin_ids = [375959767, 505958678, 314310391]



class ToState(StatesGroup):
    name = State()
    age = State()
    method = State()
    comment = State()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAIIeGYVajglbWJTHAwIgGFR-IqDsbVCAAKGTQACI5axSEwRlfTbZ3pMNAQ')
    await asyncio.sleep(4)
    await message.answer_video(video='BAACAgIAAxkBAAIIemYValgg1URHBH43z2GgWzLYsCXcAAKITQACI5axSB4KaPRgInTTNAQ', reply_markup=k.keyboard)
    await profile(user_id=message.from_user.id, name=message.from_user.full_name, surname=message.from_user.last_name)


@dp.callback_query(F.data == 'methods')
async def methods(callback: CallbackQuery):
    if callback.message.text:
        await callback.message.edit_text(
            text='Ознакомьтесь подробнее:',
            reply_markup=k.keyboard_2,
        )
    else:
        await callback.message.answer(
            text='Ознакомьтесь подробнее:',
            reply_markup=k.keyboard_2,
        )
    
#@dp.callback_query(F.data == 'ei')
#async def emotion(callback: CallbackQuery):
    #await callback.message.edit_text(
            #text='Это наша способность понимать свои эмоции и эмоции других людей, управлять ими и использовать эмоции для решения задач. Программа школ ЭИ Дети — это комплексная система развития эмоционально — интеллектуального потенциала и социальной компетентности Вашего ребенка, которая позволит ему уже в детском возрасте научиться решать важные жизненные задачи.',
            #reply_markup=keyboard_2
        #)

@dp.message(Command('id'))
async def handle_video(message: types.Message):
    video_id = message.video.file_id
    await message.reply(f"ID вашего видео: {video_id}")

@dp.callback_query(F.data == 'ei')
async def ei(callback_query: types.CallbackQuery, state: FSMContext):
    await send_text_and_photo_ei(callback_query.message)
    
async def send_text_and_photo_ei(message: Message):
    text = t.ABOUT_EI
    await message.answer_video(video='BAACAgIAAxkBAAIIVWYVZDvNPu-mHJw4yQiuu5oZCxogAAJNTQACI5axSKXovgTck6w2NAQ', caption=text, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)


async def send_text_and_photo_sk(message: Message):
    await message.answer_video(video='BAACAgIAAxkBAAIISmYVYgYKF1m4-d2LLbKATOqxWPx_AAI2TQACI5axSIQ03ZDkq5lBNAQ')
    await message.answer(text=t.ABOUT_SK, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)

@dp.callback_query(F.data == 'sk')
async def speed(callback_query: types.CallbackQuery, state: FSMContext):
    await send_text_and_photo_sk(callback_query.message)
    

@dp.callback_query(F.data == 'ma')
async def menthal(callback_query: types.CallbackQuery, state: FSMContext):
    await send_text_and_photo_ma(callback_query.message)

async def send_text_and_photo_ma(message: Message):
    text = t.ABOUT_MA
    await message.answer_video(video='BAACAgIAAxkBAAIIUGYVY4G0ZOxJGIlHTfBC7TDubVKQAAJKTQACI5axSNEKOM9XHcQqNAQ', caption=text, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)
    #await message.answer(text=t.ABOUT_MA)

    

@dp.callback_query(F.data == 'mm')
async def main_menu(callback: CallbackQuery):
    if callback.message.text:
        await callback.message.edit_text(
            text='Главное меню',
            reply_markup=k.keyboard
        )
    else:
        await callback.message.answer(
            text='Главное меню',
            reply_markup=k.keyboard
        )


@dp.callback_query(F.data == 'contacts')
async def contacts(callback: CallbackQuery):
    if callback.message.text:
        await callback.message.edit_text(
                text='https://yandex.ru/maps/-/CDRwi-1g',
                reply_markup=k.keyboard_3
            )
    else:
        await callback.message.answer(
                text='https://yandex.ru/maps/-/CDRwi-1g',
                reply_markup=k.keyboard_3
            )
    
@dp.callback_query(F.data == 'about')
async def about(callback: CallbackQuery):
    if callback.message.text:
        await callback.message.edit_text(
                text=t.COMMON_ABOUT,
                reply_markup=callback.message.reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )
    else:
        await callback.message.answer(
                text=t.COMMON_ABOUT,
                reply_markup=callback.message.reply_markup,
                parse_mode=ParseMode.MARKDOWN
            )

@dp.callback_query(StateFilter(None), F.data == 'to')
async def name(callback: CallbackQuery, state: FSMContext):
    if callback.message.text:
        await callback.message.edit_text(
                text='Введите ваше имя',
            )
    else:
        await callback.message.answer(
            text='Введите ваше имя:',
        )
    await state.set_state(ToState.name)

@dp.message(ToState.name)
async def age(message: Message, state: FSMContext):
    await state.update_data(name=message.text.capitalize())
    await message.answer(
        text='Укажите возраст ребёнка:',
    )
    await state.set_state(ToState.age)

@dp.message(ToState.age)
async def method(message: Message, state: FSMContext):
    await state.update_data(age=message.text.lower())
    await message.answer(
        text='Какое направление вас интересует?',
    )
    await state.set_state(ToState.method)

@dp.message(ToState.method)
async def comment(message: Message, state: FSMContext):
    await state.update_data(method=message.text.lower())
    await message.answer(
        text='Укажите свой номер в формате "+00000000000"',
    )
    await state.set_state(ToState.comment)

@dp.message(ToState.comment)
async def result(message: Message, state: FSMContext):
    if re.match(r'^\+?\d+$', message.text):
        await state.update_data(comment=message.text.lower())
        user_data = await state.get_data()
        await message.answer(
            text=f"Ваше имя ***{user_data['name']}***, возраст {user_data['age']}, желаемый курс {user_data['method']}, контактный номер {user_data['comment']}\n"
                f'С вами свяжутся в ближайшее время',
            parse_mode=ParseMode.MARKDOWN
        )
        text=f"Заявка с бота: Имя {user_data['name']}, возраст {user_data['age']}, курс {user_data['method']}, контактный номер {user_data['comment']}\n"
        await request(user_id=message.from_user.id, name=user_data['name'], age=user_data['age'], method=user_data['method'], contact=user_data['comment'])
        for admin in admin_ids:
            await bot.send_message(admin, text=text)
        await start(message)
        await state.clear()
    else:
        await message.answer(text='Пожалуйста, введите свой номер в правильном формате.')


class Mailing(StatesGroup):
    draft = State()

@dp.message(Command('mailing'), IsAdmin(admin_ids))
async def create_message(message: types.Message, state: FSMContext):
    await message.answer('Напишите сообщение для рассылки')
    await state.set_state(Mailing.draft)

@dp.message(Command('stop_mailing'), IsAdmin(admin_ids))
async def cancel_mailing(message: types.Message, state: FSMContext):
    await message.answer('Рассылка отменена')
    await state.clear()

@dp.message(IsAdmin(admin_ids), Mailing.draft)
async def mailing(message: types.Message, state: FSMContext):
    state_message = message.text
    chat_id = message.chat.id
    user_ids = await users()
    members = len(user_ids)
    for member in user_ids:
        user_id = member
        if message.text:
            await bot.send_message(user_id, state_message)
        if message.photo:
            await bot.send_photo(user_id, photo=message.photo[0].file_id, caption=message.caption)
        if message.video:
            await bot.send_video(user_id, video=message.video.file_id, caption=message.caption)
    await message.answer(f'Рассылка успешно завершена!, отправлено {members} сообщений')
    await state.clear()


async def main():
    await createtables()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



