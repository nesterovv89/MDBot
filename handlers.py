import asyncio
import logging
import os
import re

from aiogram import Bot, F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, KeyboardButton, Message,
                           ReplyKeyboardMarkup, ReplyKeyboardRemove)
from dotenv import load_dotenv

import keyboards as k
import media as m
import texts as t
from config import config
from db import profile, request
from states import Application

load_dotenv()


logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()

admin_ids = os.getenv('ADMINS')
admin_ids = list(map(int, admin_ids.split(',')))

bot = Bot(token=config.bot_token.get_secret_value())
router = Router()

@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer_video(video=m.START_1)
    await asyncio.sleep(4)
    await message.answer_video(video=m.START_2, reply_markup=k.keyboard)
    await profile(user_id=message.from_user.id, name=message.from_user.full_name, surname=message.from_user.last_name)


@router.callback_query(F.data == 'methods')
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

@router.message(Command('id'))
async def handle_video(message: types.Message):
    video_id = message.video.file_id
    await message.reply(f"ID вашего видео: {video_id}")

@router.message(Command('id_p'))
async def handle_photo(message: types.Message):
    photo_id = message.photo[-1].file_id
    await message.reply(f"ID вашего фото: {photo_id}")

@router.callback_query(F.data == 'ei')
async def ei(callback_query: types.CallbackQuery):
    await send_text_and_photo_ei(callback_query.message)
    
async def send_text_and_photo_ei(message: Message):
    await message.answer_video(video=m.EI_1, caption=t.ABOUT_EI, parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(2)
    await message.answer_video(video=m.EI_2, caption=t.ABOUT_EI_2, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_4)


@router.callback_query(F.data == 'tech_ei')
async def tech_ei(callback: types.CallbackQuery):
    await callback.message.answer_video(video=m.EI_TECH, caption=t.TECH_EI , parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)

@router.callback_query(F.data == 'sk')
async def speed(callback_query: types.CallbackQuery, state: FSMContext):
    await send_text_and_photo_sk(callback_query.message)

async def send_text_and_photo_sk(message: Message):
    await message.answer_video(video=m.SK_1)
    await message.answer(text=t.ABOUT_SK, parse_mode=ParseMode.MARKDOWN)
    await asyncio.sleep(2)
    await message.answer_video(video=m.SK_2, caption=t.ABOUT_SK_2, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_5)

@router.callback_query(F.data == 'tech_sk')
async def tech_ei(callback: types.CallbackQuery):
    await callback.message.answer_video(video=m.SK_TECH, caption=t.TECH_SK , parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)

@router.callback_query(F.data == 'ma')
async def menthal(callback_query: types.CallbackQuery, state: FSMContext):
    await send_text_and_photo_ma(callback_query.message)

async def send_text_and_photo_ma(message: Message):
    await message.answer_video(video=m.MA_1, caption=t.ABOUT_MA, parse_mode=ParseMode.MARKDOWN, reply_markup=k.keyboard_3)
    #await message.answer(text=t.ABOUT_MA)

@router.callback_query(F.data == 'prep')
async def prep(callback_query: types.CallbackQuery):
    await send_text_and_photo_prep(callback_query.message)
    
async def send_text_and_photo_prep(message: Message):
    await message.answer_photo(photo=m.PREP, caption=t.PREPARING, reply_markup=k.keyboard_6, parse_mode=ParseMode.MARKDOWN)

#@dp.callback_query(F.data == 'tech_prep')
#async def tech_prep(callback: types.CallbackQuery):
    #await callback.message.answer_video(video=m.PREP_2, reply_markup=k.keyboard_3)

@router.callback_query(F.data == 'atention')
async def prep(callback_query: types.CallbackQuery):
    await send_text_and_photo_at(callback_query.message)
    
async def send_text_and_photo_at(message: Message):
    await message.answer_photo(photo=m.ATNT)
    await message.answer(text=t.ATTENTION, reply_markup=k.keyboard_3, parse_mode=ParseMode.MARKDOWN)
    

@router.callback_query(F.data == 'mm')
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


@router.callback_query(F.data == 'contacts')
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
    
@router.callback_query(F.data == 'about')
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

@router.callback_query(StateFilter(None), F.data == 'to')
async def name(callback: CallbackQuery, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text='Главное меню')]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
    await callback.message.answer(
            text='Введите ваше имя:',
            reply_markup=keyboard,
        )
    await state.set_state(Application.name)

@router.message(Application.name)
async def age(message: Message, state: FSMContext):
    keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text='Главное меню')]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
    if message.text == 'Главное меню':
        await start(message)
        await state.set_state(None)
    else:    
        await state.update_data(name=message.text.capitalize())
        await message.answer(
            text='Укажите возраст ребёнка:',
            reply_markup=keyboard
        )
        await state.set_state(Application.age)

@router.message(Application.age)
async def method(message: Message, state: FSMContext):
    await state.update_data(age=message.text.lower())
    keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text='Главное меню')]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
    if message.text == 'Главное меню':
        await start(message)
        await state.set_state(None)
    keyboard_2 = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text='Эмоциональный интеллект'), KeyboardButton(text='Ментальная арифметика')],
                    [KeyboardButton(text='Скорочтение'), KeyboardButton(text='Курс на внимание')],
                    [KeyboardButton(text='Подготовка к школе'), KeyboardButton(text='Ваш вариант')],
                    [KeyboardButton(text='Главное меню')],
                ],
                resize_keyboard=True,
                one_time_keyboard=True,
            )
    await message.answer(
        text='Какое направление вас интересует?',
        reply_markup=keyboard_2
    )
    await state.set_state(Application.method)

@router.message(Application.method)
async def comment(message: Message, state: FSMContext):
    await state.update_data(method=message.text.lower())
    keyboard = ReplyKeyboardMarkup(
                keyboard=[
                    [KeyboardButton(text='Главное меню')]
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
    if message.text == 'Главное меню':
        await start(message)
        await state.set_state(None)
    elif message.text == 'Ваш вариант':
        await message.answer('Введите ваш вариант:', reply_markup=keyboard)
        await state.set_state(Application.method)
    else: 
        await state.update_data(what=message.text.capitalize())
        await message.answer(
            text='Укажите свой номер в формате "+00000000000"',
            reply_markup=keyboard
        )
        await state.set_state(Application.comment)

@router.message(Application.comment)
async def result(message: Message, state: FSMContext):
    if message.text == 'Главное меню':
        await start(message)
        await state.set_state(None)
    elif re.match(r'^\+?\d+$', message.text):
        k_2 = ReplyKeyboardRemove()
        await state.update_data(comment=message.text.lower())
        user_data = await state.get_data()
        await message.answer(
            text=f"Ваше имя ***{user_data['name']}***, возраст {user_data['age']}, желаемый курс {user_data['method']}, контактный номер {user_data['comment']}\n"
                f'С вами свяжутся в ближайшее время',
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=k_2
        )
        text=f"Заявка с бота: Имя {user_data['name']}, возраст {user_data['age']}, курс {user_data['method']}, контактный номер {user_data['comment']}\n"
        await request(user_id=message.from_user.id, name=user_data['name'], age=user_data['age'], method=user_data['method'], contact=user_data['comment'])
        for admin in admin_ids:
            await bot.send_message(admin, text=text)
        await start(message)
        await state.clear()
    else:
        await message.answer(text='Пожалуйста, введите свой номер в правильном формате.')
