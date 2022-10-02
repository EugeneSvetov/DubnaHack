from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram import types

inline_button_1 = InlineKeyboardButton('🍽 Оформить заказ', web_app=WebAppInfo(url='https://yandex.ru'))
webapp_button = InlineKeyboardMarkup().add(inline_button_1)

