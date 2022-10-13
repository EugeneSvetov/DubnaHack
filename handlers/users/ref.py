# -*- coding: utf-8 -*-

from aiogram import types
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['ref'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    engine = create_engine(
        f'postgresql://mchdxzgiplfwal:62a4b84119b5d0420e513481504d6dde8fb1b7c1b7371f289453e1aa0696acf2@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d1bku3sv3h5gug')
    owner_id = str(message.from_user.id)
    session = Session(bind=engine)
    bonus = session.execute(f'SELECT bonus FROM webapp_profile WHERE tg_id={owner_id}').first()[0]
    session.close()
    link = 'https://t.me/dubna_hack_bot?start=' + str(message.from_user.id)
    await message.answer(f'Твоя ссылка для приглашения 👇 :\n{link} \n\n🎁 Твои бонусы: {bonus} б.')
