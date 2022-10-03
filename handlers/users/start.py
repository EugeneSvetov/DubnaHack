# -*- coding: utf-8 -*-

from aiogram import types
from keyboards.inline.webappbutton import webapp_button

from loader import dp
from states.state import StateBot


def ex_referal_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


@dp.message_handler(commands=['start'], state=None)
async def bot_start(message: types.Message):
    referal_code = ex_referal_code(message.text)
    if referal_code:
        if message.from_user.id != int(referal_code):
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\nВы перешли по реф.ссылке\n\n"
                                 f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                                 reply_markup=webapp_button)
            #Надо id того кто пригласил добавить в базу
            await StateBot.is_client.set()
        else:
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                                 f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                                 reply_markup=webapp_button)
    else:
        await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                             f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                             reply_markup=webapp_button)
