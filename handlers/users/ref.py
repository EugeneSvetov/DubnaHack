# -*- coding: utf-8 -*-

from aiogram import types
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from loader import dp
from states.state import StateBot


@dp.message_handler(commands=['ref'], state=StateBot.is_client)
async def bot_start(message: types.Message):
    engine = create_engine(
        f'postgresql://etmlokgwbnykro:c41c54ac5c89c73e23a3ee26e827115b04acbdf6322a5cefad144bab37ae1aef@ec2-52-4-87-74.compute-1.amazonaws.com:5432/d5n6nt2sh4lhdl')
    owner_id = str(message.from_user.id)
    session = Session(bind=engine)
    bonus = session.execute(f'SELECT bonus FROM webapp_profile WHERE tg_id={owner_id}').first()[0]
    session.close()
    link = 'https://t.me/dubna_hack_bot?start=' + str(message.from_user.id)
    await message.answer(f'Твоя ссылка для приглашения 👉 <a href = {link}>отправить другу и поолучить бонусы</a>\n\n🎁 Твои бонусы: {bonus} б.')
