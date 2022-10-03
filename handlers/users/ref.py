# -*- coding: utf-8 -*-

from aiogram import types

from loader import dp

@dp.message_handler(commands=['ref'])
async def bot_start(message: types.Message):
    link = 'https://t.me/dubna_hack_bot?start=' + str(message.from_user.id)
    await message.answer(f'Твоя ссылка для приглашения: {link}')

