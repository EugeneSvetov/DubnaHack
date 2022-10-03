from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import types

inline_button_1 = InlineKeyboardButton('DON Food',callback_data='DON Food')
inline_button_2 = InlineKeyboardButton('Luky Maki',callback_data='Luky Maki')
inline_button_3 = InlineKeyboardButton('Mahnatic dish',callback_data='Mahnatic dish')
inline_button_4 = InlineKeyboardButton('Seledka rdon',callback_data='Seledka rdon')
inline_button_5 = InlineKeyboardButton('PELMEN BRO',callback_data='PELMEN BRO')
rest_button = InlineKeyboardMarkup().add(inline_button_1,inline_button_2,inline_button_3,inline_button_4,inline_button_5)
