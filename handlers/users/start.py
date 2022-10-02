# -*- coding: utf-8 -*-

from aiogram import types
from keyboards.inline.webappbutton import webapp_button

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['start'], state = None)
async def bot_start(message: types.Message):
    await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                         f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n", reply_markup=webapp_button)
    await StateBot.is_client.set()