# -*- coding: utf-8 -*-
from aiogram import types
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from loader import dp
from states.state import StateBot


def ex_referal_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


def post_id(tg_id):
    engine = create_engine(
        f'postgresql://mchdxzgiplfwal:62a4b84119b5d0420e513481504d6dde8fb1b7c1b7371f289453e1aa0696acf2@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d1bku3sv3h5gug')
    flag = engine.execute(f"SELECT tg_id FROM webapp_profile WHERE tg_id = {tg_id}").first()
    engine.dispose()
    if flag != None:
        print("")
    else:
        query = f'INSERT INTO webapp_profile (tg_id, bonus) VALUES ({int(tg_id)},{0})'
        engine.execute(query)
        engine.dispose()

def update_bonus_for_ref(tg_id, referal_code):
    engine = create_engine(
        f'postgresql://mchdxzgiplfwal:62a4b84119b5d0420e513481504d6dde8fb1b7c1b7371f289453e1aa0696acf2@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d1bku3sv3h5gug')
    session = Session(bind=engine)
    bonus = session.execute(f'SELECT bonus FROM webapp_profile WHERE tg_id={tg_id}').first()[0]
    tg_ref = session.execute(f'SELECT ref_id FROM webapp_profile WHERE tg_id={tg_id}').first()[0]
    session.close()
    if tg_ref == None:
        query1 = f'UPDATE webapp_profile SET bonus=bonus+{int(200)} WHERE tg_id = {int(referal_code)}'
        query = f'UPDATE webapp_profile SET bonus={int(200)} WHERE tg_id = {tg_id}'
        tg_ref_update = f'UPDATE webapp_profile SET ref_id={int(referal_code)} WHERE tg_id={tg_id}'
        engine.execute(query1)
        engine.execute(query)
        engine.execute(tg_ref_update)
        engine.dispose()



@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    referal_code = ex_referal_code(message.text)
    if referal_code:
        if message.from_user.id != int(referal_code):
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                                 f'Вы попали в Ex Minus ut Food 👑 — лучший сервис по доставке еды в Дубне.\n\nВведите <b>/makeorder</b>, чтобы сделать заказ или <b>/login</b>, чтобы войти как сотрудник ресторана и отслеживть заказы\n\n')
            tg_id = message.from_user.id
            post_id(tg_id)
            update_bonus_for_ref(tg_id, referal_code)
            await StateBot.is_client.set()

        else:
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                                 f'Вы попали в Ex Minus ut Food 👑 — лучший сервис по доставке еды в Дубне.\n\nВведите <b>/makeorder</b>, чтобы сделать заказ или <b>/login</b>, чтобы войти как сотрудник ресторана и отслеживть заказы\n\n')
            tg_id = message.from_user.id
            post_id(tg_id)
            await StateBot.is_client.set()


    else:
        await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                             f'Вы попали в Ex Minus ut Food 👑 — лучший сервис по доставке еды в Дубне.\n\nВведите <b>/makeorder</b>, чтобы сделать заказ или <b>/login</b>, чтобы войти как сотрудник ресторана и отслеживть заказы\n\n')
        tg_id = message.from_user.id
        post_id(tg_id)
        await StateBot.is_client.set()
