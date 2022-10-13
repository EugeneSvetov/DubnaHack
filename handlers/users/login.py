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
    def add_schedule():
        scheduler.add_job(scheduled, "interval", seconds=5)

    async def scheduled():
        restaurant_name = session.execute(
            f'SELECT * FROM webapp_restaurant WHERE id={restaurant_id}').fetchall()[0][1]
        last_order = session.execute(
            f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
        await asyncio.sleep(5)
        if last_order != session.execute(
                f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first():
            last_order = session.execute(
                f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
            names_prices = dict(zip(ast.literal_eval(last_order[1]), ast.literal_eval(last_order[2])))
            l = []
            for key in names_prices:
                m = f'▪️<b>{key}</b> в количестве <b>{names_prices[key]}</b> шт.'
                l.append(m)
            message = '\n'.join(l)
            print(last_order)
            session.close()
            await bot.send_message(call.from_user.id,
                                   f'{"✅" if last_order[4] == True else "❎"}Cостав заказа по адресу <b>{last_order[11]}</b> :\n{message} ')

    owner_id = str(call.from_user.id)
    query = session.execute(
        f'SELECT * FROM webapp_stuff WHERE profile={owner_id}').fetchall()
    if len(query) != 0:
        await call.answer("Вы успешно вошли как сотрудник своего ресторана ✅", show_alert=True)
        await StateBot.is_employee.set()
        restaurant_id = query[0][2]
        add_schedule()




    else:
        await call.answer(f'Вы не сотрудник 😡', show_alert=True)
