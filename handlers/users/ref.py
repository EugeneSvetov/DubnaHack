# -*- coding: utf-8 -*-

from aiogram import types

from loader import dp

@dp.message_handler(commands=['ref'])
async def bot_start(message: types.Message):
    await message.answer('рефка')

