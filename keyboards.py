from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


btn_1 = InlineKeyboardButton(text='О нас и о методиках', callback_data='about')
btn_2 = InlineKeyboardButton(text='Наши направления', callback_data='methods')
btn_3 = InlineKeyboardButton(text='Как нас найти', callback_data='contacts')
btn_4 = InlineKeyboardButton(text='Эмоциональный интеллект', callback_data='ei')
btn_5 = InlineKeyboardButton(text='Ментальная арифметика', callback_data='ma')
btn_6 = InlineKeyboardButton(text='Скорочтение', callback_data='sk')
btn_7 = InlineKeyboardButton(text='Главное меню', callback_data='mm')
btn_8 = InlineKeyboardButton(text='Отправить заявку', callback_data='to')

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
                     [btn_7],
                     [btn_8]]
)

keyboard_3 = InlineKeyboardMarkup(
    inline_keyboard=[[btn_7],
                     [btn_8]]
)
