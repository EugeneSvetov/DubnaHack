# -*- coding: utf-8 -*-

from aiogram import types
from keyboards.inline.webappbutton import webapp_button

from loader import dp

@dp.message_handler(commands=['help'])
async def bot_start(message: types.Message):
    await message.answer("❗️Справка по текущим командам:\n\n▪️ /help ➖ вывести список актуальных команд\n▪️ /start ➖ запустить бота\n▪️ /login ➖ войти как сотрудник ресторана")

