# -*- coding: utf-8 -*-

import ast
import asyncio

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from keyboards.inline.rest_list import rest_button
from loader import *
from states.state import StateBot

loop = asyncio.get_event_loop()
delay = 10.0
engine = create_engine(
    f'postgresql://mchdxzgiplfwal:62a4b84119b5d0420e513481504d6dde8fb1b7c1b7371f289453e1aa0696acf2@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d1bku3sv3h5gug')
session = Session(bind=engine)


@dp.message_handler(commands=['login'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer(
        f"👨‍🍳 Вы сотрудник ресторана?\n\nНажмите кнопку и мы сами определим где вы работаете и будем присылать данные о <b>каждом</b> заказе",
        reply_markup=rest_button)


@dp.callback_query_handler(state=StateBot.is_client)
async def about_bot_message(call: types.CallbackQuery):
    owner_id = str(call.from_user.id)
    query = session.execute(
        f'SELECT * FROM webapp_stuff WHERE profile={owner_id}').fetchall()
    if len(query) != 0:
        await call.answer("Вы успешно вошли как сотрудник вашего ресторана ✅", show_alert=True)
        await bot.send_message(call.from_user.id,'❗️ Введите <b>/last_order</b>, чтобы увидеть последний заказ или <b>/log_out</b>, чтобы выйти из режима сотрудника')
        await StateBot.is_employee.set()
        restaurant_id = query[0][2]

    else:
        await call.answer(f'Вы не сотрудник 😡', show_alert=True)
