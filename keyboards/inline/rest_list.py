from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import types

inline_button_1 = InlineKeyboardButton('DON Food',callback_data='press')
inline_button_2 = InlineKeyboardButton('Luky Maki',callback_data='press')
inline_button_3 = InlineKeyboardButton('Mahnatic dish',callback_data='press')
inline_button_4 = InlineKeyboardButton('Seledka rdon',callback_data='press')
inline_button_5 = InlineKeyboardButton('PELMEN BRO',callback_data='press')
rest_button = InlineKeyboardMarkup().add(inline_button_1,inline_button_2,inline_button_3,inline_button_4,inline_button_5)
