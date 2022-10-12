# -*- coding: utf-8 -*-

import ast
import asyncio
from typing import Final

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from keyboards.inline.rest_list import rest_button
from loader import *
from states.state import StateBot

loop = asyncio.get_event_loop()
delay = 10.0
engine = create_engine(
    f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
session = Session(bind=engine)


@dp.message_handler(commands=['login'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    await message.answer(
        "👨‍🍳 Вы сотрудник ресторана? Выберете ресторан, на заказы из которого хотите получать уведомления",
        reply_markup=rest_button)


@dp.callback_query_handler(state=StateBot.is_client)
async def about_bot_message(call: types.CallbackQuery):
    def my_callback():
        asyncio.ensure_future(check())

    owner_id: Final = str(call.from_user.id)
    query = session.execute(
        f'SELECT * FROM webapp_stuff WHERE profile={owner_id}').fetchall()
    if query != None:
        restaurant_id = query[0][2]
        restaurant_name = session.execute(
            f'SELECT * FROM webapp_restaurant WHERE id={restaurant_id}').fetchall()[0][1]
        last_order = session.execute(
            f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
        # names_prices = dict(zip(ast.literal_eval(last_order[1]), ast.literal_eval(last_order[2])))
        # l = []
        # for key in names_prices:
        #     m = f'▪️"{key}" в количестве {names_prices[key]} шт.'
        #     l.append(m)
        # message = '\n'.join(l)
        # await bot.send_message(call.from_user.id, f'Cостав заказа по адресу "{last_order[6]}" :\n{message} ')
        last_order = session.execute(
            f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
        async def check():
            if last_order != session.execute(
                    f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first():
                names_prices = dict(zip(ast.literal_eval(last_order[1]), ast.literal_eval(last_order[2])))
                l = []
                for key in names_prices:
                    m = f'▪️{key} в количестве {names_prices[key]} шт.'
                    l.append(m)
                message = '\n'.join(l)
                await bot.send_message(call.from_user.id, f'Cостав заказа по адресу "{last_order[6]}" :\n{message} ')
            else:
                when_to_call = loop.time() + delay
                loop.call_at(when_to_call, my_callback)
        await check()




    else:
        await call.answer(f'Вы не сотрудник 😡', show_alert=True)
        await StateBot.is_employee.set()
