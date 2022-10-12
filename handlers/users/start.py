# -*- coding: utf-8 -*-
import aiogram
import sqlalchemy as db
from aiogram import types
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import insert

from keyboards.inline.webappbutton import webapp_button
from loader import dp
from states.state import StateBot


def ex_referal_code(text):
    return text.split()[1] if len(text.split()) > 1 else None


def post_id(tg_id):
    engine = create_engine(
        f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
    flag = engine.execute(f"SELECT * FROM webapp_profile WHERE tg_id = {tg_id}").fetchall()
    engine.dispose()
    if len(flag) > 0:
        print("")
    else:
        query = f'INSERT INTO webapp_profile (tg_id, bonus) VALUES ({int(tg_id)}, {int(200)})'
        aiogram.WebAppInitData
        engine.execute(query)
        engine.dispose()
    return print('')


@dp.message_handler(commands=['start'])
async def bot_start(message: types.Message):
    referal_code = ex_referal_code(message.text)

    if referal_code:
        if message.from_user.id != int(referal_code):
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\nВы перешли по реф.ссылке\n\n"
                                 f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                                 reply_markup=webapp_button)
            await message.answer('После оформления заказа напишите команду "/buy", чтобы оплатить и получить ваш чек')
            tg_id = message.from_user.id
            post_id(tg_id)
            await StateBot.is_client.set()

        else:
            await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                                 f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                                 reply_markup=webapp_button)
            await message.answer('После оформления заказа напишите команду "/buy", чтобы оплатить и получить ваш чек')
            tg_id = message.from_user.id
            post_id(tg_id)
            await StateBot.is_client.set()


    else:
        await message.answer(f"Привет,  {message.from_user.full_name} 👋 !\n\n"
                             f"Вы попали в Ex Minus ut Food — лучший сервис по доставке еды в Дубне.\n\n Нажмите кнопку ниже, чтобы оформить заказ 👇\n\n",
                             reply_markup=webapp_button)
        await message.answer('После оформления заказа напишите команду "/buy", чтобы оплатить и получить ваш чек')
        tg_id = message.from_user.id
        post_id(tg_id)
        await StateBot.is_client.set()


