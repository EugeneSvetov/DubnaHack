from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import types

inline_button_1 = InlineKeyboardButton('Войти как сотрудник ресторана', callback_data = 'data')
rest_button = InlineKeyboardMarkup().add(inline_button_1)
