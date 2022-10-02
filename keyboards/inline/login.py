from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import types

inline_button_2 = InlineKeyboardButton('Войти по TGid 🆔',callback_data='press')
login_button = InlineKeyboardMarkup().add(inline_button_2)