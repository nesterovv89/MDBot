from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

btn_1 = InlineKeyboardButton(text='О нас и о методиках', callback_data='about')
btn_2 = InlineKeyboardButton(text='Наши направления', callback_data='methods')
btn_3 = InlineKeyboardButton(text='Как нас найти', callback_data='contacts')
btn_4 = InlineKeyboardButton(text='Эмоциональный интеллект', callback_data='ei')
btn_5 = InlineKeyboardButton(text='Ментальная арифметика', callback_data='ma')
btn_6 = InlineKeyboardButton(text='Скорочтение', callback_data='sk')
btn_7 = InlineKeyboardButton(text='Главное меню', callback_data='mm')
btn_8 = InlineKeyboardButton(text='Отправить заявку', callback_data='to')
btn_9 = InlineKeyboardButton(text='Посмотреть технику', callback_data='tech_ei')
btn_10 = InlineKeyboardButton(text='Посмотреть технику', callback_data='tech_sk')
btn_11 = InlineKeyboardButton(text='Курс на внимание', callback_data='atention')
btn_12 = InlineKeyboardButton(text='Подготовка к школе', callback_data='prep')
btn_13 = InlineKeyboardButton(text='Почему?', callback_data='tech_prep')


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[btn_1],
                     [btn_2],
                     [btn_8],
                     [btn_3]]
)

keyboard_2 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_4],
                     [btn_5],
                     [btn_6],
                     [btn_11],
                     [btn_12],
                     [btn_7],
                     [btn_8]]
)

keyboard_3 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_7],
                     [btn_8]]
)

keyboard_4 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_7],
                     [btn_8],
                     [btn_9]]
)

keyboard_5 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_7],
                     [btn_8],
                     [btn_10]]
)

keyboard_6 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_7],
                     [btn_8]]
)


kb = [
        [
            KeyboardButton(text='О нас и о методиках'),
            KeyboardButton(text='Наши направления'),
            KeyboardButton(text='Отправить заявку'),
            KeyboardButton(text='Как нас найти'),
        ],
    ]