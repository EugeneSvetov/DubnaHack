# -*- coding: utf-8 -*-
import ast

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from loader import *
from states.state import StateBot


@dp.message_handler(commands=['last_order'], state=StateBot.is_employee)
async def bot_employee(message: types.Message):
    engine = create_engine(
        f'postgresql://mchdxzgiplfwal:62a4b84119b5d0420e513481504d6dde8fb1b7c1b7371f289453e1aa0696acf2@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d1bku3sv3h5gug')
    session = Session(bind=engine)
    owner_id = str(message.from_user.id)
    query = session.execute(
        f'SELECT * FROM webapp_stuff WHERE profile={owner_id}').fetchall()
    restaurant_id = query[0][2]
    restaurant_name = session.execute(
        f'SELECT * FROM webapp_restaurant WHERE id={restaurant_id}').fetchall()[0][1]
    last_order = session.execute(
        f'SELECT * FROM webapp_order WHERE restaurant_id={restaurant_id} ORDER BY date_of_create DESC').first()
    print('BOT', type(last_order))
    names_prices = dict(zip(ast.literal_eval(last_order[1]), ast.literal_eval(last_order[2])))
    l = []
    for key in names_prices:
        m = f'▪️<b>{key}</b> в количестве <b>{names_prices[key]}</b> шт.'
        l.append(m)
    messages = '\n'.join(l)
    print(last_order)
    session.close()
    await message.answer(f'{"✅" if last_order[4] == True else "❎"}Cостав заказа по адресу <b>{last_order[11]}</b> :\n{messages} ')
