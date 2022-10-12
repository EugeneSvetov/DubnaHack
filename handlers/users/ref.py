# -*- coding: utf-8 -*-

from aiogram import types

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['ref'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    link = 'https://t.me/dubna_hack_bot?start=' + str(message.from_user.id)
    await message.answer(f'Твоя ссылка для приглашения: {link}\n\nТвои бонусы: 0 б')
